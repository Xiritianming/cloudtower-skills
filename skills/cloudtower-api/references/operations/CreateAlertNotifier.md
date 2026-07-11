# POST /v2/api/create-alert-notifier

**Resource:** [AlertNotifier](../resources/AlertNotifier.md)
**Operation ID:** `CreateAlertNotifier`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [AlertNotifierCreationParams](../schemas/Alert/AlertNotifierCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "notice_severities": [
      "CRITICAL"
    ],
    "language_code": "EN_US",
    "email_tos": [
      "<email_tos>"
    ],
    "email_from": "<email_from>",
    "disabled": false,
    "smtp_server_id": "<smtp_server_id>",
    "name": "<name>",
    "clusters": {}
  }
]
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py CreateAlertNotifier /tmp/body.json
bash scripts/call.sh /v2/api/create-alert-notifier /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_AlertNotifier_](../schemas/With/WithTask-AlertNotifier.md)

## Security

- **Authorization**
