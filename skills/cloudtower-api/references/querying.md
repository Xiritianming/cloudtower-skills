# Query Guide — filters, counting, pagination

Applies to every `get-*` operation and to mutations that select targets via a `where` field.

## Where filters

A `where` filter (`XxxWhereInput` schema) is a flat object: field names carry operator **suffixes**. There is no nested operator syntax:

```json
{"where": {"id_in": ["a", "b"], "name_contains": "prod"}}     ✔
{"where": {"id": {"in": ["a", "b"]}}}                         ✘ no such syntax
```

- no suffix = equals: `{"name": "vm-1"}`
- `_in` / `_not_in` — list membership
- `_contains`, `_starts_with`, `_ends_with` (and `_not_*` forms) — string match
- `_gt`, `_gte`, `_lt`, `_lte` — comparison
- `AND` / `OR` / `NOT` — arrays of nested where objects
- `{}` matches everything

The exact fields available per resource are in the linked `XxxWhereInput` schema file — copy field names from there, never guess suffixes onto arbitrary fields.

## Counting

To count resources, use the `get-*-connection` operation instead of fetching the full list — the body `{}` works and the response is a few bytes:

```bash
echo '{}' > /tmp/count.json
bash scripts/call.sh /v2/api/get-vms-connection /tmp/count.json
# -> {"aggregate": {"count": 129}}
```

## Pagination and ordering

Query bodies accept `first` (page size), `skip` (offset), and `orderBy` (an enum value from the resource's `XxxOrderByInput` schema, formatted `<field>_ASC` / `<field>_DESC`):

```json
{"where": {}, "first": 50, "skip": 50, "orderBy": "name_ASC"}
```

Responses always carry full objects — there is no `expand`/`include`/field-selection parameter; extract the fields you need from the response file with `jq`.
