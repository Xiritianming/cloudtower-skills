# POST /v2/api/create-host

**Resource:** [Host](../resources/Host.md)
**Operation ID:** `CreateHost`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [HostCreationParams](../schemas/Host/HostCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "data": [
      {
        "ifaces": [
          {
            "netmask": "<netmask>",
            "name": [
              "<name>"
            ],
            "ip": "<ip>",
            "gateway_ip": "<gateway_ip>",
            "function": "ACCESS"
          }
        ],
        "disks": [
          {
            "drive": "<drive>"
          }
        ],
        "hostname": "<hostname>",
        "host_uuid": "<host_uuid>",
        "host_ip": "<host_ip>"
      }
    ],
    "cluster_id": "<cluster_id>"
  }
]
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py CreateHost /tmp/body.json
bash scripts/call.sh /v2/api/create-host /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_BatchHosts_](../schemas/With/WithTask-BatchHosts.md)

## Security

- **Authorization**
