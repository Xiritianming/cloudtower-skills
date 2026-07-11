# BackupTargetExecution

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `backup_group` | string | Yes |  |
| `executed_at` | string | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `parent_backup` | string | Yes |  |
| `type` | [BackupExecutionType](../Backup/BackupExecutionType.md) | Yes |  |
| `backup_plan_execution` | any | No |  |
| `backup_restore_point` | any | No |  |
| `cluster_local_id` | string | No |  |
| `duration` | integer (int32) | No |  |
| `entityAsyncStatus` | any | No |  |
| `read_bytes` | integer (int64) | No |  |
| `retry_times` | integer (int32) | No |  |
| `status` | any | No |  |
| `total_bytes` | integer (int64) | No |  |
| `vm` | any | No |  |
| `vm_local_id` | string | No |  |
| `vm_name` | string | No |  |

