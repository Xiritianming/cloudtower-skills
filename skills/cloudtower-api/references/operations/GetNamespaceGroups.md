# POST /v2/api/get-namespace-groups

**Resource:** [NamespaceGroup](../resources/NamespaceGroup.md)
**Operation ID:** `GetNamespaceGroups`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [GetNamespaceGroupsRequestBody](../schemas/Get/GetNamespaceGroupsRequestBody.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{}
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py GetNamespaceGroups /tmp/body.json
bash scripts/call.sh /v2/api/get-namespace-groups /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [NamespaceGroup](../schemas/Namespace/NamespaceGroup.md)

## Security

- **Authorization**
