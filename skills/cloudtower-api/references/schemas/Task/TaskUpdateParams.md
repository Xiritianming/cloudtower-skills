# TaskUpdateParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [TaskWhereInput](../Task/TaskWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `finished_at` | string | No |  |
| `started_at` | string | No |  |
| `resource_rollback_retry_count` | integer (int32) | No |  |
| `resource_rollback_error` | string | No |  |
| `resource_rollbacked` | boolean | No |  |
| `steps` | Array of [TaskStepCreationParams](../Task/TaskStepCreationParams.md) | No |  |
| `error_message` | string | No |  |
| `error_code` | string | No |  |
| `progress` | number (float) | No |  |
| `status` | [TaskStatus](../Task/TaskStatus.md) | No |  |
| `snapshot` | string | No |  |
| `args` | object | No |  |
| `key` | string | No |  |
| `type` | [TaskType](../Task/TaskType.md) | No |  |
| `resource_id` | string | No |  |
| `cluster_id` | string | No |  |
| `user_id` | string | No |  |
| `resource_mutation` | string | No |  |
| `resource_type` | string | No |  |
| `description` | [TaskDescription](../Task/TaskDescription.md) | No |  |

