# POST /v2/api/create-log-collection

**Resource:** [LogCollection](../resources/LogCollection.md)
**Operation ID:** `CreateLogCollection`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [LogCollectionCreationParams](../schemas/Log/LogCollectionCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "log_ended_at": "<log_ended_at>",
    "log_started_at": "<log_started_at>",
    "cluster_id": "<cluster_id>",
    "hosts": {}
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateLogCollection /tmp/body.json
bash scripts/call.sh /v2/api/create-log-collection /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_LogCollection_](../schemas/With/WithTask-LogCollection.md)

## Security

- **Authorization**
