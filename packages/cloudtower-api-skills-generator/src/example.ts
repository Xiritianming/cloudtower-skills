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

function requestBodySchema(spec: Spec, operationId: string): SchemaOrRef | undefined {
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
      return body?.content?.["application/json"]?.schema;
    }
  }
  return undefined;
}

/**
 * Build a minimal JSON request-body example for an operation. Returns null
 * when the operation has no `application/json` request body (e.g. multipart
 * uploads).
 */
export function buildRequestExample(spec: Spec, operationId: string): string | null {
  const schema = requestBodySchema(spec, operationId);
  if (!schema) return null;
  return JSON.stringify(buildValue(spec, schema, "value", [], 0), null, 2);
}

/**
 * True when the operation's request body carries a `metrics: string[]` field —
 * metric names are free strings the schema cannot validate, so these
 * operations get a pointer to the hand-authored metrics guide.
 */
export function requestUsesMetricNames(spec: Spec, operationId: string): boolean {
  let { schema } = deref(spec, requestBodySchema(spec, operationId));
  if (schema?.type === "array") {
    ({ schema } = deref(spec, (schema as OpenAPIV3.ArraySchemaObject).items));
  }
  const metrics = deref(spec, schema?.properties?.metrics).schema;
  return metrics?.type === "array";
}

/**
 * True when the operation's request body carries a `where` filter — those
 * operations get a pointer to the hand-authored query guide.
 */
export function requestUsesWhere(spec: Spec, operationId: string): boolean {
  let { schema } = deref(spec, requestBodySchema(spec, operationId));
  if (schema?.type === "array") {
    ({ schema } = deref(spec, (schema as OpenAPIV3.ArraySchemaObject).items));
  }
  return Boolean(schema?.properties?.where);
}

/**
 * Resolve the schema name a property points at, seeing through the
 * `allOf: [$ref]` (+ nullable) idiom the upstream parser renders as a bare,
 * linkless `any`. Returns `Name`, `Name[]`, or null.
 */
export function fieldRefName(spec: Spec, prop: SchemaOrRef | undefined): string | null {
  const directRef = (node: SchemaOrRef | undefined): string | null => {
    if (!node) return null;
    if ("$ref" in node) return refName(node.$ref);
    const only = (node as OpenAPIV3.SchemaObject).allOf?.length === 1
      ? (node as OpenAPIV3.SchemaObject).allOf?.[0]
      : undefined;
    if (only && "$ref" in only) return refName(only.$ref);
    return null;
  };
  const direct = directRef(prop);
  if (direct) return direct;
  const schema = prop && !("$ref" in prop) ? prop : undefined;
  if (schema?.type === "array") {
    const inner = directRef((schema as OpenAPIV3.ArraySchemaObject).items);
    if (inner) return `${inner}[]`;
  }
  return null;
}

/** Look up a component schema's raw properties, following $ref chains. */
export function rawProperties(
  spec: Spec,
  schemaName: string,
): Record<string, SchemaOrRef> | undefined {
  const { schema } = deref(spec, { $ref: `#/components/schemas/${schemaName}` });
  return schema?.properties as Record<string, SchemaOrRef> | undefined;
}
