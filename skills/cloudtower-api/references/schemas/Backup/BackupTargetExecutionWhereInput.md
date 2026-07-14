# BackupTargetExecutionWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [BackupTargetExecutionWhereInput](../Backup/BackupTargetExecutionWhereInput.md) | No |  |
| `NOT` | Array of [BackupTargetExecutionWhereInput](../Backup/BackupTargetExecutionWhereInput.md) | No |  |
| `OR` | Array of [BackupTargetExecutionWhereInput](../Backup/BackupTargetExecutionWhereInput.md) | No |  |
| `backup_group` | string | No |  |
| `backup_group_contains` | string | No |  |
| `backup_group_ends_with` | string | No |  |
| `backup_group_gt` | string | No |  |
| `backup_group_gte` | string | No |  |
| `backup_group_in` | string[] | No |  |
| `backup_group_lt` | string | No |  |
| `backup_group_lte` | string | No |  |
| `backup_group_not` | string | No |  |
| `backup_group_not_contains` | string | No |  |
| `backup_group_not_ends_with` | string | No |  |
| `backup_group_not_in` | string[] | No |  |
| `backup_group_not_starts_with` | string | No |  |
| `backup_group_starts_with` | string | No |  |
| `backup_plan_execution` | [BackupPlanExecutionWhereInput](../Backup/BackupPlanExecutionWhereInput.md) | No |  |
| `backup_restore_point` | [BackupRestorePointWhereInput](../Backup/BackupRestorePointWhereInput.md) | No |  |
| `cluster_local_id` | string | No |  |
| `cluster_local_id_contains` | string | No |  |
| `cluster_local_id_ends_with` | string | No |  |
| `cluster_local_id_gt` | string | No |  |
| `cluster_local_id_gte` | string | No |  |
| `cluster_local_id_in` | string[] | No |  |
| `cluster_local_id_lt` | string | No |  |
| `cluster_local_id_lte` | string | No |  |
| `cluster_local_id_not` | string | No |  |
| `cluster_local_id_not_contains` | string | No |  |
| `cluster_local_id_not_ends_with` | string | No |  |
| `cluster_local_id_not_in` | string[] | No |  |
| `cluster_local_id_not_starts_with` | string | No |  |
| `cluster_local_id_starts_with` | string | No |  |
| `duration` | integer (int32) | No |  |
| `duration_gt` | integer (int32) | No |  |
| `duration_gte` | integer (int32) | No |  |
| `duration_in` | integer[] | No |  |
| `duration_lt` | integer (int32) | No |  |
| `duration_lte` | integer (int32) | No |  |
| `duration_not` | integer (int32) | No |  |
| `duration_not_in` | integer[] | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `executed_at` | string | No |  |
| `executed_at_gt` | string | No |  |
| `executed_at_gte` | string | No |  |
| `executed_at_in` | string[] | No |  |
| `executed_at_lt` | string | No |  |
| `executed_at_lte` | string | No |  |
| `executed_at_not` | string | No |  |
| `executed_at_not_in` | string[] | No |  |
| `id` | string | No |  |
| `id_contains` | string | No |  |
| `id_ends_with` | string | No |  |
| `id_gt` | string | No |  |
| `id_gte` | string | No |  |
| `id_in` | string[] | No |  |
| `id_lt` | string | No |  |
| `id_lte` | string | No |  |
| `id_not` | string | No |  |
| `id_not_contains` | string | No |  |
| `id_not_ends_with` | string | No |  |
| `id_not_in` | string[] | No |  |
| `id_not_starts_with` | string | No |  |
| `id_starts_with` | string | No |  |
| `local_id` | string | No |  |
| `local_id_contains` | string | No |  |
| `local_id_ends_with` | string | No |  |
| `local_id_gt` | string | No |  |
| `local_id_gte` | string | No |  |
| `local_id_in` | string[] | No |  |
| `local_id_lt` | string | No |  |
| `local_id_lte` | string | No |  |
| `local_id_not` | string | No |  |
| `local_id_not_contains` | string | No |  |
| `local_id_not_ends_with` | string | No |  |
| `local_id_not_in` | string[] | No |  |
| `local_id_not_starts_with` | string | No |  |
| `local_id_starts_with` | string | No |  |
| `parent_backup` | string | No |  |
| `parent_backup_contains` | string | No |  |
| `parent_backup_ends_with` | string | No |  |
| `parent_backup_gt` | string | No |  |
| `parent_backup_gte` | string | No |  |
| `parent_backup_in` | string[] | No |  |
| `parent_backup_lt` | string | No |  |
| `parent_backup_lte` | string | No |  |
| `parent_backup_not` | string | No |  |
| `parent_backup_not_contains` | string | No |  |
| `parent_backup_not_ends_with` | string | No |  |
| `parent_backup_not_in` | string[] | No |  |
| `parent_backup_not_starts_with` | string | No |  |
| `parent_backup_starts_with` | string | No |  |
| `read_bytes` | integer (int64) | No |  |
| `read_bytes_gt` | integer (int64) | No |  |
| `read_bytes_gte` | integer (int64) | No |  |
| `read_bytes_in` | integer[] | No |  |
| `read_bytes_lt` | integer (int64) | No |  |
| `read_bytes_lte` | integer (int64) | No |  |
| `read_bytes_not` | integer (int64) | No |  |
| `read_bytes_not_in` | integer[] | No |  |
| `retry_times` | integer (int32) | No |  |
| `retry_times_gt` | integer (int32) | No |  |
| `retry_times_gte` | integer (int32) | No |  |
| `retry_times_in` | integer[] | No |  |
| `retry_times_lt` | integer (int32) | No |  |
| `retry_times_lte` | integer (int32) | No |  |
| `retry_times_not` | integer (int32) | No |  |
| `retry_times_not_in` | integer[] | No |  |
| `status` | [BackupExecutionStatus](../Backup/BackupExecutionStatus.md) | No |  |
| `status_in` | Array of [BackupExecutionStatus](../Backup/BackupExecutionStatus.md) | No |  |
| `status_not` | [BackupExecutionStatus](../Backup/BackupExecutionStatus.md) | No |  |
| `status_not_in` | Array of [BackupExecutionStatus](../Backup/BackupExecutionStatus.md) | No |  |
| `total_bytes` | integer (int64) | No |  |
| `total_bytes_gt` | integer (int64) | No |  |
| `total_bytes_gte` | integer (int64) | No |  |
| `total_bytes_in` | integer[] | No |  |
| `total_bytes_lt` | integer (int64) | No |  |
| `total_bytes_lte` | integer (int64) | No |  |
| `total_bytes_not` | integer (int64) | No |  |
| `total_bytes_not_in` | integer[] | No |  |
| `type` | [BackupExecutionType](../Backup/BackupExecutionType.md) | No |  |
| `type_in` | Array of [BackupExecutionType](../Backup/BackupExecutionType.md) | No |  |
| `type_not` | [BackupExecutionType](../Backup/BackupExecutionType.md) | No |  |
| `type_not_in` | Array of [BackupExecutionType](../Backup/BackupExecutionType.md) | No |  |
| `vm` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_local_id` | string | No |  |
| `vm_local_id_contains` | string | No |  |
| `vm_local_id_ends_with` | string | No |  |
| `vm_local_id_gt` | string | No |  |
| `vm_local_id_gte` | string | No |  |
| `vm_local_id_in` | string[] | No |  |
| `vm_local_id_lt` | string | No |  |
| `vm_local_id_lte` | string | No |  |
| `vm_local_id_not` | string | No |  |
| `vm_local_id_not_contains` | string | No |  |
| `vm_local_id_not_ends_with` | string | No |  |
| `vm_local_id_not_in` | string[] | No |  |
| `vm_local_id_not_starts_with` | string | No |  |
| `vm_local_id_starts_with` | string | No |  |
| `vm_name` | string | No |  |
| `vm_name_contains` | string | No |  |
| `vm_name_ends_with` | string | No |  |
| `vm_name_gt` | string | No |  |
| `vm_name_gte` | string | No |  |
| `vm_name_in` | string[] | No |  |
| `vm_name_lt` | string | No |  |
| `vm_name_lte` | string | No |  |
| `vm_name_not` | string | No |  |
| `vm_name_not_contains` | string | No |  |
| `vm_name_not_ends_with` | string | No |  |
| `vm_name_not_in` | string[] | No |  |
| `vm_name_not_starts_with` | string | No |  |
| `vm_name_starts_with` | string | No |  |

