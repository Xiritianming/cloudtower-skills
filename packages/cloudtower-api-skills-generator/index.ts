import { existsSync } from "node:fs";
import { cp, mkdir, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { createParser } from "openapi-to-skills";
import type { OpenAPIV3 } from "openapi-types";
import { CloudTowerRenderer, mergeSchemaGroups, toFileName } from "./src/renderer.ts";

type OpenAPISpec = OpenAPIV3.Document;

const packageDir = import.meta.dir;
const specsDir = join(packageDir, "specs");
const currentSpecPath = join(specsDir, "current-swagger.json");
const swaggerBaseUrl = "https://code.smartx.com/specs";
const templatesDir = join(packageDir, "templates");
const assetsDir = join(packageDir, "assets");
const outputDir = join(packageDir, "..", "..", "skills");

// CloudTower serves the API under this prefix; the spec's `servers` is just `/`.
const apiPrefix = "/v2/api";

function addCloudTowerTitle(spec: OpenAPISpec) {
  spec.info = {
    ...spec.info,
    title: "cloudtower-api",
  };
}

async function loadSpec(versionOrPath: string): Promise<OpenAPISpec> {
  if (existsSync(versionOrPath)) {
    console.log(`Using local spec: ${versionOrPath}`);
    return (await Bun.file(versionOrPath).json()) as OpenAPISpec;
  }
  const swaggerUrl = `${swaggerBaseUrl}/${versionOrPath}-swagger.json`;
  const response = await fetch(swaggerUrl);
  if (!response.ok) {
    throw new Error(`Swagger for version ${versionOrPath} does not exist: ${swaggerUrl}`);
  }
  console.log(`Downloaded swagger: ${swaggerUrl}`);
  return (await response.json()) as OpenAPISpec;
}

async function main() {
  const versionOrPath = process.argv[2];
  if (!versionOrPath) {
    throw new Error("Usage: bun run index.ts <version | path-to-swagger.json>");
  }

  const spec = await loadSpec(versionOrPath);
  addCloudTowerTitle(spec);

  await mkdir(specsDir, { recursive: true });
  await writeFile(currentSpecPath, `${JSON.stringify(spec, null, 2)}\n`);
  console.log(`Prepared spec: ${currentSpecPath}`);

  const parsed = parseSkill(spec);
  const { groups, canonical } = mergeSchemaGroups(parsed.schemaGroups);
  const doc = { ...parsed, schemaGroups: groups };

  const renderer = new CloudTowerRenderer(templatesDir, spec, canonical, apiPrefix);
  const skillDir = join(outputDir, doc.meta.name);

  await rm(skillDir, { recursive: true, force: true });
  await writeSkill(doc, skillDir, renderer);

  // validate.py resolves request schemas against this bundled spec.
  await writeFile(join(skillDir, "references", "openapi.json"), JSON.stringify(spec));

  await cp(assetsDir, skillDir, {
    recursive: true,
    filter: (src) => !src.includes("__pycache__") && !src.endsWith(".DS_Store"),
  });
  console.log(`Skill generated at: ${skillDir}`);
}

function parseSkill(spec: OpenAPISpec) {
  return createParser().parse(spec);
}

type SkillDoc = ReturnType<typeof parseSkill>;

async function writeSkill(doc: SkillDoc, skillDir: string, renderer: CloudTowerRenderer) {
  const referencesDir = join(skillDir, "references");
  const resourcesDir = join(referencesDir, "resources");
  const operationsDir = join(referencesDir, "operations");
  const schemasDir = join(referencesDir, "schemas");
  for (const dir of [resourcesDir, operationsDir, schemasDir]) {
    await mkdir(dir, { recursive: true });
  }

  await writeFile(join(skillDir, "SKILL.md"), renderer.renderSkill(doc));

  let totalOps = 0;
  for (const resource of doc.resources) {
    await writeFile(join(resourcesDir, `${toFileName(resource.tag)}.md`), renderer.renderResource(resource));
    for (const op of resource.operations) {
      await writeFile(join(operationsDir, `${toFileName(op.operationId)}.md`), renderer.renderOperation(op));
      totalOps++;
    }
  }

  let totalSchemas = 0;
  for (const group of doc.schemaGroups) {
    const prefixDir = join(schemasDir, toFileName(group.prefix));
    await mkdir(prefixDir, { recursive: true });
    await writeFile(join(prefixDir, "_index.md"), renderer.renderSchemaIndex(group));
    for (const schema of group.schemas) {
      await writeFile(join(prefixDir, `${toFileName(schema.name)}.md`), renderer.renderSchema(schema));
      totalSchemas++;
    }
  }

  if (doc.authSchemes.length > 0) {
    await writeFile(join(referencesDir, "authentication.md"), renderer.renderAuthentication(doc.authSchemes));
  }

  console.log(
    `${doc.resources.length} resources, ${totalOps} operations, ${doc.schemaGroups.length} schema groups, ${totalSchemas} schemas`,
  );
}

await main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(message);
  process.exit(1);
});
