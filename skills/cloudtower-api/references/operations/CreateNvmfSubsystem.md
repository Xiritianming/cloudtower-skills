# POST /v2/api/create-nvmf-subsystem

**Resource:** [NvmfSubsystem](../resources/NvmfSubsystem.md)
**Operation ID:** `CreateNvmfSubsystem`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [NvmfSubsystemCreationParams](../schemas/Nvmf/NvmfSubsystemCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "replica_num": 1,
    "thin_provision": false,
    "stripe_size": 1,
    "stripe_num": 1,
    "policy": "BALANCE",
    "cluster_id": "<cluster_id>",
    "name": "<name>"
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateNvmfSubsystem /tmp/body.json
bash scripts/call.sh /v2/api/create-nvmf-subsystem /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_NvmfSubsystem_](../schemas/With/WithTask-NvmfSubsystem.md)

## Security

- **Authorization**
