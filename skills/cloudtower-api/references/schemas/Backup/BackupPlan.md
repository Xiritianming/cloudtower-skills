# BackupPlan

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `backup_service` | [NestedBackupService](../Nested/NestedBackupService.md) | Yes |  |
| `backup_store_repository` | [NestedBackupStoreRepository](../Nested/NestedBackupStoreRepository.md) | Yes |  |
| `createdAt` | string | Yes |  |
| `enable_window` | boolean | Yes |  |
| `full_interval` | integer (int32) | Yes |  |
| `full_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | Yes |  |
| `full_time_point` | [NestedBackupPlanTimePoint](../Nested/NestedBackupPlanTimePoint.md) | Yes |  |
| `id` | string | Yes |  |
| `incremental_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | Yes |  |
| `incremental_time_points` | Array of [NestedBackupPlanTimePoint](../Nested/NestedBackupPlanTimePoint.md) | Yes |  |
| `last_execute_status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | Yes |  |
| `last_manual_execute_status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | Yes |  |
| `logical_size` | integer (int64) | Yes |  |
| `name` | string | Yes |  |
| `physical_size` | integer (int64) | Yes |  |
| `status` | [BackupPlanStatus](../Backup/BackupPlanStatus.md) | Yes |  |
| `valid_size_of_backup_object` | integer (int64) | Yes |  |
| `valid_size_of_restore_point` | integer (int64) | Yes |  |
| `backup_delay_option` | any | No |  |
| `backup_plan_executions` | Array of [NestedBackupPlanExecution](../Nested/NestedBackupPlanExecution.md) | No |  |
| `backup_restore_point_count` | integer (int32) | No |  |
| `backup_restore_points` | Array of [NestedBackupRestorePoint](../Nested/NestedBackupRestorePoint.md) | No |  |
| `backup_total_size` | integer (int64) | No |  |
| `compression` | boolean | No |  |
| `compression_ratio` | number (double) | No |  |
| `delete_strategy` | any | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | any | No |  |
| `incremental_interval` | integer (int32) | No |  |
| `incremental_weekdays` | Array of [WeekdayTypeEnum](../Weekday/WeekdayTypeEnum.md) | No |  |
| `keep_policy` | any | No |  |
| `keep_policy_value` | integer (int32) | No |  |
| `last_execute_status_message` | string | No |  |
| `last_execute_success_job_count` | integer (int32) | No |  |
| `last_execute_total_job_count` | integer (int32) | No |  |
| `last_executed_at` | string | No |  |
| `last_manual_execute_status_message` | string | No |  |
| `last_manual_execute_success_job_count` | integer (int32) | No |  |
| `last_manual_execute_total_job_count` | integer (int32) | No |  |
| `last_manual_executed_at` | string | No |  |
| `next_execute_time` | string | No |  |
| `phase` | any | No |  |
| `snapshot_consistent_type` | any | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |
| `window_end` | string | No |  |
| `window_start` | string | No |  |

