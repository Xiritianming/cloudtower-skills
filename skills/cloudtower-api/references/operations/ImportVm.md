# POST /v2/api/import-vm

**Resource:** [Vm](../resources/Vm.md)
**Operation ID:** `ImportVm`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [VmImportParams](../schemas/Vm/VmImportParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "name": "<name>",
    "cluster_id": "<cluster_id>",
    "upload_tasks": [
      "<upload_tasks>"
    ],
    "parsed_ovf": {
      "firmware": "BIOS",
      "disks": [
        {
          "size": 1,
          "type": "CD_ROM",
          "bus": "IDE",
          "name": "<name>"
        }
      ],
      "nics": [
        {
          "mac": "<mac>"
        }
      ],
      "memory": 1,
      "cpu": {
        "sockets": 1,
        "cores": 1
      },
      "vcpu": 1,
      "name": "<name>"
    }
  }
]
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py ImportVm /tmp/body.json
bash scripts/call.sh /v2/api/import-vm /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_Vm_](../schemas/With/WithTask-Vm.md)

## Security

- **Authorization**
