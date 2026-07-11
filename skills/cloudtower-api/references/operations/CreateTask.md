# POST /v2/api/create-task

**Resource:** [Task](../resources/Task.md)
**Operation ID:** `CreateTask`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [TaskCreationParams](../schemas/Task/TaskCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "user_id": "<user_id>",
    "description": {
      "en-US": "<en-US>",
      "zh-CN": "<zh-CN>"
    },
    "resource_mutation": "<resource_mutation>",
    "resource_type": "<resource_type>"
  }
]
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py CreateTask /tmp/body.json
bash scripts/call.sh /v2/api/create-task /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_Task_](../schemas/With/WithTask-Task.md)

## Security

- **Authorization**
