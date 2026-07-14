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
| `backup_plan_execution` | [NestedBackupPlanExecution](../Nested/NestedBackupPlanExecution.md) | No |  |
| `backup_restore_point` | [NestedBackupRestorePoint](../Nested/NestedBackupRestorePoint.md) | No |  |
| `cluster_local_id` | string | No |  |
| `duration` | integer (int32) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `read_bytes` | integer (int64) | No |  |
| `retry_times` | integer (int32) | No |  |
| `status` | [BackupExecutionStatus](../Backup/BackupExecutionStatus.md) | No |  |
| `total_bytes` | integer (int64) | No |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | No |  |
| `vm_local_id` | string | No |  |
| `vm_name` | string | No |  |

