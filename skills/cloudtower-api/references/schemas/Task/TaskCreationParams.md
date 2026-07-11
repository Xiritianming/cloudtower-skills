# TaskCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `user_id` | string | Yes |  |
| `description` | [TaskDescription](../Task/TaskDescription.md) | Yes |  |
| `resource_mutation` | string | Yes |  |
| `resource_type` | string | Yes |  |
| `api_key_name` | string | No |  |
| `snapshot` | string | No |  |
| `status` | [TaskStatus](../Task/TaskStatus.md) | No |  |
| `id` | string | No |  |
| `finished_at` | string | No |  |
| `started_at` | string | No |  |
| `steps` | Array of [TaskStepCreationParams](../Task/TaskStepCreationParams.md) | No |  |
| `args` | object | No |  |
| `key` | string | No |  |
| `internal` | boolean | No |  |
| `type` | [TaskType](../Task/TaskType.md) | No |  |
| `resource_id` | string | No |  |
| `cluster_id` | string | No |  |

