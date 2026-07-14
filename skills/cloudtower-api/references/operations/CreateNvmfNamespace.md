# POST /v2/api/create-nvmf-namespace

**Resource:** [NvmfNamespace](../resources/NvmfNamespace.md)
**Operation ID:** `CreateNvmfNamespace`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [NvmfNamespaceCreationParams](../schemas/Nvmf/NvmfNamespaceCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "assigned_size": 1,
    "replica_num": 1,
    "nvmf_subsystem_id": "<nvmf_subsystem_id>",
    "name": "<name>"
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateNvmfNamespace /tmp/body.json
bash scripts/call.sh /v2/api/create-nvmf-namespace /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_NvmfNamespace_](../schemas/With/WithTask-NvmfNamespace.md)

## Security

- **Authorization**
