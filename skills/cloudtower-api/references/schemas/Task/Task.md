# Task

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `args` | object | Yes |  |
| `description` | string | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `local_created_at` | string | Yes |  |
| `progress` | number (double) | Yes |  |
| `snapshot` | string | Yes |  |
| `status` | [TaskStatus](../Task/TaskStatus.md) | Yes |  |
| `steps` | Array of [NestedStep](../Nested/NestedStep.md) | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `error_code` | string | No |  |
| `error_message` | string | No |  |
| `finished_at` | string | No |  |
| `key` | string | No |  |
| `resource_id` | string | No |  |
| `resource_mutation` | string | No |  |
| `resource_rollback_error` | string | No |  |
| `resource_rollback_retry_count` | integer (int32) | No |  |
| `resource_rollbacked` | boolean | No |  |
| `resource_type` | string | No |  |
| `started_at` | string | No |  |
| `type` | [TaskType](../Task/TaskType.md) | No |  |
| `user` | [NestedUser](../Nested/NestedUser.md) | No |  |

## Nested Fields

### `args`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


