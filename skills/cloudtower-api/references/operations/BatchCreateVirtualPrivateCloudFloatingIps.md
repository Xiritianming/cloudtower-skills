# POST /v2/api/batch-create-virtual-private-cloud-floating-ips

**Resource:** [VirtualPrivateCloudFloatingIp](../resources/VirtualPrivateCloudFloatingIp.md)
**Operation ID:** `BatchCreateVirtualPrivateCloudFloatingIps`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [BatchCreateVirtualPrivateCloudFloatingIpsParams](../schemas/Batch/BatchCreateVirtualPrivateCloudFloatingIpsParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "vpc_id": "<vpc_id>"
}
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py BatchCreateVirtualPrivateCloudFloatingIps /tmp/body.json
bash scripts/call.sh /v2/api/batch-create-virtual-private-cloud-floating-ips /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_BatchCreateVirtualPrivateCloudFloatingIp_](../schemas/With/WithTask-BatchCreateVirtualPrivateCloudFloatingIp.md)

## Security

- **Authorization**
