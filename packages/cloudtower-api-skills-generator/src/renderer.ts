import { Eta } from "eta";
import type { OpenAPIV3 } from "openapi-types";
import type {
  OperationDocument,
  Renderer,
  ResourceDocument,
  SchemaDocument,
  SchemaGroupDocument,
  SkillDocument,
} from "openapi-to-skills";

type AuthSchemes = Parameters<Renderer["renderAuthentication"]>[0];
import { buildRequestExample } from "./example.ts";

// Mirrors of openapi-to-skills' helpers — the package's exports map does not
// expose them, and file names/link paths must match its output exactly.
export function toFileName(name: string): string {
  const sanitized = name
    .normalize("NFC")
    .replace(/[^\p{L}\p{N}-]+/gu, "-")
    .replace(/^-+|-+$/g, "")
    .replace(/-{2,}/g, "-");
  return sanitized || "unnamed";
}

export function extractSchemaPrefix(name: string): string {
  const match = name.match(/^([A-Z][a-z]+)/);
  if (match?.[1]) return match[1];
  const underscoreMatch = name.match(/^([^_]+)/);
  if (underscoreMatch?.[1]) return underscoreMatch[1];
  return "Other";
}

/**
 * Merge schema groups whose prefixes differ only in case (e.g. `Role` and
 * `ROLE`) — on case-insensitive filesystems they collide into one directory
 * and the second `_index.md` silently overwrites the first. The canonical
 * prefix is the variant owning the most schemas. Returns the merged groups
 * plus a lowercase-prefix → canonical-prefix map used to keep every generated
 * link pointing at the canonical directory.
 */
export function mergeSchemaGroups(groups: SchemaGroupDocument[]): {
  groups: SchemaGroupDocument[];
  canonical: Map<string, string>;
} {
  const byKey = new Map<string, { variants: Map<string, number>; schemas: SchemaDocument[] }>();
  for (const group of groups) {
    const key = group.prefix.toLowerCase();
    let entry = byKey.get(key);
    if (!entry) {
      entry = { variants: new Map(), schemas: [] };
      byKey.set(key, entry);
    }
    entry.variants.set(group.prefix, (entry.variants.get(group.prefix) ?? 0) + group.schemas.length);
    entry.schemas.push(...group.schemas);
  }
  const merged: SchemaGroupDocument[] = [];
  const canonical = new Map<string, string>();
  for (const [key, entry] of byKey) {
    const prefix = [...entry.variants.entries()].sort((a, b) => b[1] - a[1])[0]?.[0] ?? key;
    canonical.set(key, prefix);
    merged.push({ prefix, schemas: entry.schemas });
  }
  return { groups: merged, canonical };
}

export class CloudTowerRenderer implements Renderer {
  private eta: Eta;
  private spec: OpenAPIV3.Document;
  private canonical: Map<string, string>;
  private apiPrefix: string;
  private schemaNames: Set<string>;

  constructor(templateDir: string, spec: OpenAPIV3.Document, canonical: Map<string, string>, apiPrefix: string) {
    this.eta = new Eta({ views: templateDir, autoEscape: false, autoTrim: false });
    this.spec = spec;
    this.canonical = canonical;
    this.apiPrefix = apiPrefix;
    this.schemaNames = new Set(Object.keys(spec.components?.schemas ?? {}));
  }

  private canonicalPrefix = (name: string): string => {
    const prefix = extractSchemaPrefix(name);
    return this.canonical.get(prefix.toLowerCase()) ?? prefix;
  };

  /**
   * Render a type-cell for a schema field: known schema names become links to
   * `../<canonical prefix>/<name>.md` (correct across prefix directories,
   * unlike the upstream same-directory links), `Name[]` array references
   * included; anything else is returned verbatim.
   */
  private schemaLink = (type: string): string => {
    const isArray = type.endsWith("[]");
    const name = isArray ? type.slice(0, -2) : type;
    if (!this.schemaNames.has(name)) return type;
    const link = `[${name}](../${toFileName(this.canonicalPrefix(name))}/${toFileName(name)}.md)`;
    return isArray ? `Array of ${link}` : link;
  };

  private helpers() {
    return {
      toFileName,
      extractSchemaPrefix: this.canonicalPrefix,
      schemaLink: this.schemaLink,
      apiPrefix: this.apiPrefix,
    };
  }

  renderSkill(doc: SkillDocument): string {
    const totalOps = doc.resources.reduce((sum, r) => sum + r.operations.length, 0);
    const totalSchemas = doc.schemaGroups.reduce((sum, g) => sum + g.schemas.length, 0);
    return this.eta.render("skill.md.eta", { ...doc, totalOps, totalSchemas, ...this.helpers() });
  }

  renderResource(doc: ResourceDocument): string {
    return this.eta.render("resource.md.eta", { ...doc, ...this.helpers() });
  }

  renderOperation(doc: OperationDocument): string {
    return this.eta.render("operation.md.eta", {
      ...doc,
      ...this.helpers(),
      exampleJson: buildRequestExample(this.spec, doc.operationId),
    });
  }

  renderSchema(doc: SchemaDocument): string {
    return this.eta.render("schema.md.eta", { ...doc, ...this.helpers() });
  }

  renderSchemaIndex(group: SchemaGroupDocument): string {
    return this.eta.render("schema-index.md.eta", { ...group, ...this.helpers() });
  }

  renderAuthentication(schemes: AuthSchemes): string {
    return this.eta.render("authentication.md.eta", { schemes, ...this.helpers() });
  }
}
