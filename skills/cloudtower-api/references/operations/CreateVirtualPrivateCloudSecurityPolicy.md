# POST /v2/api/create-virtual-private-cloud-security-policy

**Resource:** [VirtualPrivateCloudSecurityPolicy](../resources/VirtualPrivateCloudSecurityPolicy.md)
**Operation ID:** `CreateVirtualPrivateCloudSecurityPolicy`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [VirtualPrivateCloudSecurityPolicyCreateParams](../schemas/Virtual/VirtualPrivateCloudSecurityPolicyCreateParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "apply_to": [
      {
        "security_group_id": "<security_group_id>",
        "communicable": false
      }
    ],
    "vpc_id": "<vpc_id>",
    "name": "<name>"
  }
]
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py CreateVirtualPrivateCloudSecurityPolicy /tmp/body.json
bash scripts/call.sh /v2/api/create-virtual-private-cloud-security-policy /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_VirtualPrivateCloudSecurityPolicy_](../schemas/With/WithTask-VirtualPrivateCloudSecurityPolicy.md)

## Security

- **Authorization**
