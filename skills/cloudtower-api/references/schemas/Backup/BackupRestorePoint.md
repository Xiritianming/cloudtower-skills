# BackupRestorePoint

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `backup_plan` | [NestedBackupPlan](../Nested/NestedBackupPlan.md) | Yes |  |
| `backup_target_execution` | [NestedBackupTargetExecution](../Nested/NestedBackupTargetExecution.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `slice` | string | Yes |  |
| `backup_restore_executions` | Array of [NestedBackupRestoreExecution](../Nested/NestedBackupRestoreExecution.md) | No |  |
| `cluster_local_id` | string | No |  |
| `compressed` | boolean | No |  |
| `compression_ratio` | number (double) | No |  |
| `creation` | [BackupRestorePointCreation](../Backup/BackupRestorePointCreation.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `local_created_at` | string | No |  |
| `logical_size` | integer (int64) | No |  |
| `parent_restore_point` | string | No |  |
| `physical_size` | integer (int64) | No |  |
| `size` | integer (int64) | No |  |
| `snapshot_consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `type` | [BackupRestorePointType](../Backup/BackupRestorePointType.md) | No |  |
| `valid_capacity` | integer (int64) | No |  |
| `valid_size` | integer (int64) | No |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | No |  |
| `vm_local_id` | string | No |  |
| `vm_name` | string | No |  |

