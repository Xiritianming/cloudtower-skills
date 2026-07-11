import type { OpenAPIV3 } from "openapi-types";

type Spec = OpenAPIV3.Document;
type SchemaOrRef = OpenAPIV3.SchemaObject | OpenAPIV3.ReferenceObject;

// WhereInput-style schemas are heavily self-recursive (AND/OR/NOT); the cap and
// the per-path seen-set below keep expansion finite.
const MAX_DEPTH = 8;

function refName(ref: string): string {
  return ref.split("/").pop() ?? ref;
}

function deref(
  spec: Spec,
  node: SchemaOrRef | undefined,
): { name?: string; schema?: OpenAPIV3.SchemaObject } {
  let name: string | undefined;
  const visited = new Set<string>();
  while (node && "$ref" in node) {
    name = refName(node.$ref);
    if (visited.has(name)) return { name };
    visited.add(name);
    node = spec.components?.schemas?.[name] as SchemaOrRef | undefined;
  }
  return { name, schema: node };
}

/**
 * Build a minimal example value for a schema: every required field present,
 * optional fields omitted. Values prefer spec-provided `example`/`default`,
 * then fall back to typed placeholders (`"<field_name>"` for strings, first
 * value for enums). The result always validates against the schema.
 */
function buildValue(spec: Spec, node: SchemaOrRef | undefined, hint: string, seen: readonly string[], depth: number): unknown {
  if (depth > MAX_DEPTH) return {};
  const { name, schema } = deref(spec, node);
  if (!schema) return `<${hint}>`;
  if (name) {
    if (seen.includes(name)) return {};
    seen = [...seen, name];
  }

  if (schema.example !== undefined) return schema.example;
  if (schema.default !== undefined) return schema.default;
  if (schema.enum?.length) {
    // Any member is shape-valid; prefer one that isn't a destructive/terminal
    // state so copy-and-modify callers who miss the note still send something
    // sane (e.g. VmStatus's first member is DELETED).
    const sane = schema.enum.find((v) => !/DELET|UNKNOWN|FAIL|ERROR|REMOV/i.test(String(v)));
    return sane ?? schema.enum[0];
  }

  if (schema.allOf?.length) {
    const merged: Record<string, unknown> = {};
    for (const part of schema.allOf) {
      const v = buildValue(spec, part, hint, seen, depth + 1);
      if (v && typeof v === "object" && !Array.isArray(v)) Object.assign(merged, v);
    }
    return merged;
  }
  const variants = schema.oneOf ?? schema.anyOf;
  if (variants?.length) return buildValue(spec, variants[0], hint, seen, depth + 1);

  if (schema.type === "array") {
    const items = (schema as OpenAPIV3.ArraySchemaObject).items;
    return [buildValue(spec, items, hint, seen, depth + 1)];
  }
  if (schema.type === "object" || schema.properties || schema.required?.length) {
    const out: Record<string, unknown> = {};
    for (const key of schema.required ?? []) {
      out[key] = buildValue(spec, schema.properties?.[key], key, seen, depth + 1);
    }
    return out;
  }
  switch (schema.type) {
    case "string":
      return `<${hint}>`;
    case "integer":
    case "number":
      return 1;
    case "boolean":
      return false;
    default:
      return `<${hint}>`;
  }
}

/**
 * Locate the raw spec operation by operationId and build a minimal JSON
 * request-body example. Returns null when the operation has no
 * `application/json` request body (e.g. multipart uploads).
 */
export function buildRequestExample(spec: Spec, operationId: string): string | null {
  for (const pathItem of Object.values(spec.paths ?? {})) {
    if (!pathItem) continue;
    for (const method of ["get", "post", "put", "patch", "delete"] as const) {
      const op = pathItem[method];
      if (!op || op.operationId !== operationId) continue;
      let body = op.requestBody;
      if (body && "$ref" in body) {
        const name = refName(body.$ref);
        body = spec.components?.requestBodies?.[name] as OpenAPIV3.RequestBodyObject | undefined;
      }
      const schema = body?.content?.["application/json"]?.schema;
      if (!schema) return null;
      return JSON.stringify(buildValue(spec, schema, "value", [], 0), null, 2);
    }
  }
  return null;
}
