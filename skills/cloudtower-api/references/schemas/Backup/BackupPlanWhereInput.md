# BackupPlanWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | No |  |
| `NOT` | Array of [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | No |  |
| `OR` | Array of [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | No |  |
| `backup_delay_option` | [BackupPlanDelayOption](../Backup/BackupPlanDelayOption.md) | No |  |
| `backup_delay_option_in` | Array of [BackupPlanDelayOption](../Backup/BackupPlanDelayOption.md) | No |  |
| `backup_delay_option_not` | [BackupPlanDelayOption](../Backup/BackupPlanDelayOption.md) | No |  |
| `backup_delay_option_not_in` | Array of [BackupPlanDelayOption](../Backup/BackupPlanDelayOption.md) | No |  |
| `backup_plan_executions_every` | [BackupPlanExecutionWhereInput](../Backup/BackupPlanExecutionWhereInput.md) | No |  |
| `backup_plan_executions_none` | [BackupPlanExecutionWhereInput](../Backup/BackupPlanExecutionWhereInput.md) | No |  |
| `backup_plan_executions_some` | [BackupPlanExecutionWhereInput](../Backup/BackupPlanExecutionWhereInput.md) | No |  |
| `backup_restore_point_count` | integer (int32) | No |  |
| `backup_restore_point_count_gt` | integer (int32) | No |  |
| `backup_restore_point_count_gte` | integer (int32) | No |  |
| `backup_restore_point_count_in` | integer[] | No |  |
| `backup_restore_point_count_lt` | integer (int32) | No |  |
| `backup_restore_point_count_lte` | integer (int32) | No |  |
| `backup_restore_point_count_not` | integer (int32) | No |  |
| `backup_restore_point_count_not_in` | integer[] | No |  |
| `backup_restore_points_every` | [BackupRestorePointWhereInput](../Backup/BackupRestorePointWhereInput.md) | No |  |
| `backup_restore_points_none` | [BackupRestorePointWhereInput](../Backup/BackupRestorePointWhereInput.md) | No |  |
| `backup_restore_points_some` | [BackupRestorePointWhereInput](../Backup/BackupRestorePointWhereInput.md) | No |  |
| `backup_service` | [BackupServiceWhereInput](../Backup/BackupServiceWhereInput.md) | No |  |
| `backup_store_repository` | [BackupStoreRepositoryWhereInput](../Backup/BackupStoreRepositoryWhereInput.md) | No |  |
| `backup_total_size` | integer (int64) | No |  |
| `backup_total_size_gt` | integer (int64) | No |  |
| `backup_total_size_gte` | integer (int64) | No |  |
| `backup_total_size_in` | integer[] | No |  |
| `backup_total_size_lt` | integer (int64) | No |  |
| `backup_total_size_lte` | integer (int64) | No |  |
| `backup_total_size_not` | integer (int64) | No |  |
| `backup_total_size_not_in` | integer[] | No |  |
| `compression` | boolean | No |  |
| `compression_not` | boolean | No |  |
| `compression_ratio` | number (double) | No |  |
| `compression_ratio_gt` | number (double) | No |  |
| `compression_ratio_gte` | number (double) | No |  |
| `compression_ratio_in` | number[] | No |  |
| `compression_ratio_lt` | number (double) | No |  |
| `compression_ratio_lte` | number (double) | No |  |
| `compression_ratio_not` | number (double) | No |  |
| `compression_ratio_not_in` | number[] | No |  |
| `createdAt` | string | No |  |
| `createdAt_gt` | string | No |  |
| `createdAt_gte` | string | No |  |
| `createdAt_in` | string[] | No |  |
| `createdAt_lt` | string | No |  |
| `createdAt_lte` | string | No |  |
| `createdAt_not` | string | No |  |
| `createdAt_not_in` | string[] | No |  |
| `delete_strategy` | [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `delete_strategy_in` | Array of [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `delete_strategy_not` | [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `delete_strategy_not_in` | Array of [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `description` | string | No |  |
| `description_contains` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_gt` | string | No |  |
| `description_gte` | string | No |  |
| `description_in` | string[] | No |  |
| `description_lt` | string | No |  |
| `description_lte` | string | No |  |
| `description_not` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_starts_with` | string | No |  |
| `description_starts_with` | string | No |  |
| `enable_window` | boolean | No |  |
| `enable_window_not` | boolean | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `full_interval` | integer (int32) | No |  |
| `full_interval_gt` | integer (int32) | No |  |
| `full_interval_gte` | integer (int32) | No |  |
| `full_interval_in` | integer[] | No |  |
| `full_interval_lt` | integer (int32) | No |  |
| `full_interval_lte` | integer (int32) | No |  |
| `full_interval_not` | integer (int32) | No |  |
| `full_interval_not_in` | integer[] | No |  |
| `full_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `full_period_in` | Array of [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `full_period_not` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `full_period_not_in` | Array of [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
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
| `incremental_interval` | integer (int32) | No |  |
| `incremental_interval_gt` | integer (int32) | No |  |
| `incremental_interval_gte` | integer (int32) | No |  |
| `incremental_interval_in` | integer[] | No |  |
| `incremental_interval_lt` | integer (int32) | No |  |
| `incremental_interval_lte` | integer (int32) | No |  |
| `incremental_interval_not` | integer (int32) | No |  |
| `incremental_interval_not_in` | integer[] | No |  |
| `incremental_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `incremental_period_in` | Array of [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `incremental_period_not` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `incremental_period_not_in` | Array of [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `keep_policy` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_in` | Array of [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_not` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_not_in` | Array of [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_value` | integer (int32) | No |  |
| `keep_policy_value_gt` | integer (int32) | No |  |
| `keep_policy_value_gte` | integer (int32) | No |  |
| `keep_policy_value_in` | integer[] | No |  |
| `keep_policy_value_lt` | integer (int32) | No |  |
| `keep_policy_value_lte` | integer (int32) | No |  |
| `keep_policy_value_not` | integer (int32) | No |  |
| `keep_policy_value_not_in` | integer[] | No |  |
| `last_execute_status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_execute_status_in` | Array of [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_execute_status_message` | string | No |  |
| `last_execute_status_message_contains` | string | No |  |
| `last_execute_status_message_ends_with` | string | No |  |
| `last_execute_status_message_gt` | string | No |  |
| `last_execute_status_message_gte` | string | No |  |
| `last_execute_status_message_in` | string[] | No |  |
| `last_execute_status_message_lt` | string | No |  |
| `last_execute_status_message_lte` | string | No |  |
| `last_execute_status_message_not` | string | No |  |
| `last_execute_status_message_not_contains` | string | No |  |
| `last_execute_status_message_not_ends_with` | string | No |  |
| `last_execute_status_message_not_in` | string[] | No |  |
| `last_execute_status_message_not_starts_with` | string | No |  |
| `last_execute_status_message_starts_with` | string | No |  |
| `last_execute_status_not` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_execute_status_not_in` | Array of [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_execute_success_job_count` | integer (int32) | No |  |
| `last_execute_success_job_count_gt` | integer (int32) | No |  |
| `last_execute_success_job_count_gte` | integer (int32) | No |  |
| `last_execute_success_job_count_in` | integer[] | No |  |
| `last_execute_success_job_count_lt` | integer (int32) | No |  |
| `last_execute_success_job_count_lte` | integer (int32) | No |  |
| `last_execute_success_job_count_not` | integer (int32) | No |  |
| `last_execute_success_job_count_not_in` | integer[] | No |  |
| `last_execute_total_job_count` | integer (int32) | No |  |
| `last_execute_total_job_count_gt` | integer (int32) | No |  |
| `last_execute_total_job_count_gte` | integer (int32) | No |  |
| `last_execute_total_job_count_in` | integer[] | No |  |
| `last_execute_total_job_count_lt` | integer (int32) | No |  |
| `last_execute_total_job_count_lte` | integer (int32) | No |  |
| `last_execute_total_job_count_not` | integer (int32) | No |  |
| `last_execute_total_job_count_not_in` | integer[] | No |  |
| `last_executed_at` | string | No |  |
| `last_executed_at_gt` | string | No |  |
| `last_executed_at_gte` | string | No |  |
| `last_executed_at_in` | string[] | No |  |
| `last_executed_at_lt` | string | No |  |
| `last_executed_at_lte` | string | No |  |
| `last_executed_at_not` | string | No |  |
| `last_executed_at_not_in` | string[] | No |  |
| `last_manual_execute_status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_manual_execute_status_in` | Array of [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_manual_execute_status_message` | string | No |  |
| `last_manual_execute_status_message_contains` | string | No |  |
| `last_manual_execute_status_message_ends_with` | string | No |  |
| `last_manual_execute_status_message_gt` | string | No |  |
| `last_manual_execute_status_message_gte` | string | No |  |
| `last_manual_execute_status_message_in` | string[] | No |  |
| `last_manual_execute_status_message_lt` | string | No |  |
| `last_manual_execute_status_message_lte` | string | No |  |
| `last_manual_execute_status_message_not` | string | No |  |
| `last_manual_execute_status_message_not_contains` | string | No |  |
| `last_manual_execute_status_message_not_ends_with` | string | No |  |
| `last_manual_execute_status_message_not_in` | string[] | No |  |
| `last_manual_execute_status_message_not_starts_with` | string | No |  |
| `last_manual_execute_status_message_starts_with` | string | No |  |
| `last_manual_execute_status_not` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_manual_execute_status_not_in` | Array of [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | No |  |
| `last_manual_execute_success_job_count` | integer (int32) | No |  |
| `last_manual_execute_success_job_count_gt` | integer (int32) | No |  |
| `last_manual_execute_success_job_count_gte` | integer (int32) | No |  |
| `last_manual_execute_success_job_count_in` | integer[] | No |  |
| `last_manual_execute_success_job_count_lt` | integer (int32) | No |  |
| `last_manual_execute_success_job_count_lte` | integer (int32) | No |  |
| `last_manual_execute_success_job_count_not` | integer (int32) | No |  |
| `last_manual_execute_success_job_count_not_in` | integer[] | No |  |
| `last_manual_execute_total_job_count` | integer (int32) | No |  |
| `last_manual_execute_total_job_count_gt` | integer (int32) | No |  |
| `last_manual_execute_total_job_count_gte` | integer (int32) | No |  |
| `last_manual_execute_total_job_count_in` | integer[] | No |  |
| `last_manual_execute_total_job_count_lt` | integer (int32) | No |  |
| `last_manual_execute_total_job_count_lte` | integer (int32) | No |  |
| `last_manual_execute_total_job_count_not` | integer (int32) | No |  |
| `last_manual_execute_total_job_count_not_in` | integer[] | No |  |
| `last_manual_executed_at` | string | No |  |
| `last_manual_executed_at_gt` | string | No |  |
| `last_manual_executed_at_gte` | string | No |  |
| `last_manual_executed_at_in` | string[] | No |  |
| `last_manual_executed_at_lt` | string | No |  |
| `last_manual_executed_at_lte` | string | No |  |
| `last_manual_executed_at_not` | string | No |  |
| `last_manual_executed_at_not_in` | string[] | No |  |
| `logical_size` | integer (int64) | No |  |
| `logical_size_gt` | integer (int64) | No |  |
| `logical_size_gte` | integer (int64) | No |  |
| `logical_size_in` | integer[] | No |  |
| `logical_size_lt` | integer (int64) | No |  |
| `logical_size_lte` | integer (int64) | No |  |
| `logical_size_not` | integer (int64) | No |  |
| `logical_size_not_in` | integer[] | No |  |
| `name` | string | No |  |
| `name_contains` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_gt` | string | No |  |
| `name_gte` | string | No |  |
| `name_in` | string[] | No |  |
| `name_lt` | string | No |  |
| `name_lte` | string | No |  |
| `name_not` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_starts_with` | string | No |  |
| `name_starts_with` | string | No |  |
| `next_execute_time` | string | No |  |
| `next_execute_time_gt` | string | No |  |
| `next_execute_time_gte` | string | No |  |
| `next_execute_time_in` | string[] | No |  |
| `next_execute_time_lt` | string | No |  |
| `next_execute_time_lte` | string | No |  |
| `next_execute_time_not` | string | No |  |
| `next_execute_time_not_in` | string[] | No |  |
| `phase` | [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `phase_in` | Array of [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `phase_not` | [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `phase_not_in` | Array of [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `physical_size` | integer (int64) | No |  |
| `physical_size_gt` | integer (int64) | No |  |
| `physical_size_gte` | integer (int64) | No |  |
| `physical_size_in` | integer[] | No |  |
| `physical_size_lt` | integer (int64) | No |  |
| `physical_size_lte` | integer (int64) | No |  |
| `physical_size_not` | integer (int64) | No |  |
| `physical_size_not_in` | integer[] | No |  |
| `snapshot_consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `snapshot_consistent_type_in` | Array of [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `snapshot_consistent_type_not` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `snapshot_consistent_type_not_in` | Array of [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `status` | [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `status_in` | Array of [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `status_not` | [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `status_not_in` | Array of [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `valid_size_of_backup_object` | integer (int64) | No |  |
| `valid_size_of_backup_object_gt` | integer (int64) | No |  |
| `valid_size_of_backup_object_gte` | integer (int64) | No |  |
| `valid_size_of_backup_object_in` | integer[] | No |  |
| `valid_size_of_backup_object_lt` | integer (int64) | No |  |
| `valid_size_of_backup_object_lte` | integer (int64) | No |  |
| `valid_size_of_backup_object_not` | integer (int64) | No |  |
| `valid_size_of_backup_object_not_in` | integer[] | No |  |
| `valid_size_of_restore_point` | integer (int64) | No |  |
| `valid_size_of_restore_point_gt` | integer (int64) | No |  |
| `valid_size_of_restore_point_gte` | integer (int64) | No |  |
| `valid_size_of_restore_point_in` | integer[] | No |  |
| `valid_size_of_restore_point_lt` | integer (int64) | No |  |
| `valid_size_of_restore_point_lte` | integer (int64) | No |  |
| `valid_size_of_restore_point_not` | integer (int64) | No |  |
| `valid_size_of_restore_point_not_in` | integer[] | No |  |
| `vms_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `window_end` | string | No |  |
| `window_end_contains` | string | No |  |
| `window_end_ends_with` | string | No |  |
| `window_end_gt` | string | No |  |
| `window_end_gte` | string | No |  |
| `window_end_in` | string[] | No |  |
| `window_end_lt` | string | No |  |
| `window_end_lte` | string | No |  |
| `window_end_not` | string | No |  |
| `window_end_not_contains` | string | No |  |
| `window_end_not_ends_with` | string | No |  |
| `window_end_not_in` | string[] | No |  |
| `window_end_not_starts_with` | string | No |  |
| `window_end_starts_with` | string | No |  |
| `window_start` | string | No |  |
| `window_start_contains` | string | No |  |
| `window_start_ends_with` | string | No |  |
| `window_start_gt` | string | No |  |
| `window_start_gte` | string | No |  |
| `window_start_in` | string[] | No |  |
| `window_start_lt` | string | No |  |
| `window_start_lte` | string | No |  |
| `window_start_not` | string | No |  |
| `window_start_not_contains` | string | No |  |
| `window_start_not_ends_with` | string | No |  |
| `window_start_not_in` | string[] | No |  |
| `window_start_not_starts_with` | string | No |  |
| `window_start_starts_with` | string | No |  |

