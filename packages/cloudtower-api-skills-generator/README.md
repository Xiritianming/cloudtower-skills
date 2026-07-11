# cloudtower-api-skills-generator

To install dependencies:

```bash
bun install
```

To run:

```bash
bun run index.ts 4.8.0                        # download by version
bun run index.ts specs/current-swagger.json   # or regenerate from a local spec
```

The script downloads `https://code.smartx.com/specs/<version>-swagger.json` (or
loads a local file), adds `cloudtower-api` to `info.title`, writes the spec to
`./specs/current-swagger.json`, and generates the skill using `openapi-to-skills`
as a library with local extensions:

- `src/example.ts` — builds the minimal required-fields request example inlined
  into every operation file (cycle-safe recursive schema resolution)
- `src/renderer.ts` — merges case-colliding schema groups (`Role`/`ROLE`) and
  emits cross-prefix schema links that stay valid on case-sensitive filesystems
- `templates/` — all six output templates (operation files carry the full
  `/v2/api` path and an `## Example` section; schema files list required fields
  first)
- `assets/scripts/` — `call.sh` (request wrapper) and `validate.py`
  (request-body validator) copied into the skill; `validate.py` reads the spec
  bundled at `references/openapi.json`
