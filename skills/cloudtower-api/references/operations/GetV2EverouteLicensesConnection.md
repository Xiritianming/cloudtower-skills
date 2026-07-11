# POST /v2/api/get-v-2-everoute-licenses-connection

**Resource:** [V2EverouteLicense](../resources/V2EverouteLicense.md)
**Operation ID:** `GetV2EverouteLicensesConnection`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [GetV2EverouteLicensesConnectionRequestBody](../schemas/Get/GetV2EverouteLicensesConnectionRequestBody.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{}
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py GetV2EverouteLicensesConnection /tmp/body.json
bash scripts/call.sh /v2/api/get-v-2-everoute-licenses-connection /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

[V2EverouteLicenseConnection](../schemas/V2EverouteLicenseConnection/V2EverouteLicenseConnection.md)

## Security

- **Authorization**
