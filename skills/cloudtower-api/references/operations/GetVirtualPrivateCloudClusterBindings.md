# POST /v2/api/get-virtual-private-cloud-cluster-bindings

**Resource:** [VirtualPrivateCloudClusterBinding](../resources/VirtualPrivateCloudClusterBinding.md)
**Operation ID:** `GetVirtualPrivateCloudClusterBindings`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [GetVirtualPrivateCloudClusterBindingsRequestBody](../schemas/Get/GetVirtualPrivateCloudClusterBindingsRequestBody.md)

> `where` filters use flat suffix syntax (`id_in`, `name_contains`, …) — see the [Query Guide](../querying.md) for filter, counting, and pagination syntax.

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{}
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py GetVirtualPrivateCloudClusterBindings /tmp/body.json
bash scripts/call.sh /v2/api/get-virtual-private-cloud-cluster-bindings /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [VirtualPrivateCloudClusterBinding](../schemas/Virtual/VirtualPrivateCloudClusterBinding.md)

## Security

- **Authorization**
