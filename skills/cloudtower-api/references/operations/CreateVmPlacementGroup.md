# POST /v2/api/create-vm-placement-group

**Resource:** [VmPlacementGroup](../resources/VmPlacementGroup.md)
**Operation ID:** `CreateVmPlacementGroup`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [VmPlacementGroupCreationParams](../schemas/Vm/VmPlacementGroupCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "name": "<name>",
    "enabled": false,
    "cluster_id": "<cluster_id>"
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateVmPlacementGroup /tmp/body.json
bash scripts/call.sh /v2/api/create-vm-placement-group /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_VmPlacementGroup_](../schemas/With/WithTask-VmPlacementGroup.md)

## Security

- **Authorization**
