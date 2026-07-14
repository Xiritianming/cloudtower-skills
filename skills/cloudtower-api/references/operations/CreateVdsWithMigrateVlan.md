# POST /v2/api/create-vds-with-migrate-vlan

**Resource:** [Vds](../resources/Vds.md)
**Operation ID:** `CreateVdsWithMigrateVlan`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [VdsCreationWithMigrateVlanParams](../schemas/Vds/VdsCreationWithMigrateVlanParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "nic_ids": [
      "<nic_ids>"
    ],
    "cluster_id": "<cluster_id>",
    "name": "<name>",
    "vlan": {
      "extra_ip": [
        {
          "management_ip": "<management_ip>",
          "host_id": "<host_id>"
        }
      ],
      "subnetmask": "<subnetmask>",
      "vlan_id": 1
    }
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateVdsWithMigrateVlan /tmp/body.json
bash scripts/call.sh /v2/api/create-vds-with-migrate-vlan /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_Vds_](../schemas/With/WithTask-Vds.md)

## Security

- **Authorization**
