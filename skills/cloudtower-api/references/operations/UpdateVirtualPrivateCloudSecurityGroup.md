# POST /v2/api/update-virtual-private-cloud-security-group

**Resource:** [VirtualPrivateCloudSecurityGroup](../resources/VirtualPrivateCloudSecurityGroup.md)
**Operation ID:** `UpdateVirtualPrivateCloudSecurityGroup`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [VirtualPrivateCloudSecurityGroupUpdationParams](../schemas/Virtual/VirtualPrivateCloudSecurityGroupUpdationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "data": {},
  "where": {}
}
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py UpdateVirtualPrivateCloudSecurityGroup /tmp/body.json
bash scripts/call.sh /v2/api/update-virtual-private-cloud-security-group /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_VirtualPrivateCloudSecurityGroup_](../schemas/With/WithTask-VirtualPrivateCloudSecurityGroup.md)

## Security

- **Authorization**
