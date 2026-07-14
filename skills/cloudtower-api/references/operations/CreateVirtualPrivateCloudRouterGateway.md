# POST /v2/api/create-virtual-private-cloud-router-gateway

**Resource:** [VirtualPrivateCloudRouterGateway](../resources/VirtualPrivateCloudRouterGateway.md)
**Operation ID:** `CreateVirtualPrivateCloudRouterGateway`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [VirtualPrivateCloudRouterGatewayCreationParams](../schemas/Virtual/VirtualPrivateCloudRouterGatewayCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "rules": [
      {
        "dst": "<dst>"
      }
    ],
    "associated_subnets_ids": [
      "<associated_subnets_ids>"
    ],
    "vpc_id": "<vpc_id>",
    "name": "<name>"
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateVirtualPrivateCloudRouterGateway /tmp/body.json
bash scripts/call.sh /v2/api/create-virtual-private-cloud-router-gateway /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_VirtualPrivateCloudRouterGateway_](../schemas/With/WithTask-VirtualPrivateCloudRouterGateway.md)

## Security

- **Authorization**
