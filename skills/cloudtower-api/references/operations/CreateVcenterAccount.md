# POST /v2/api/create-vcenter-account

**Resource:** [VcenterAccount](../resources/VcenterAccount.md)
**Operation ID:** `CreateVcenterAccount`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [CreateVcenterAccountParams](../schemas/Create/CreateVcenterAccountParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "data": {
    "port": 1,
    "password": "<password>",
    "username": "<username>",
    "ip": "<ip>",
    "cluster_id": "<cluster_id>"
  }
}
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateVcenterAccount /tmp/body.json
bash scripts/call.sh /v2/api/create-vcenter-account /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

[WithTask_VcenterAccount_](../schemas/With/WithTask-VcenterAccount.md)

## Security

- **Authorization**
