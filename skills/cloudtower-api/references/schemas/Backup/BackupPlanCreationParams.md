# BackupPlanCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `keep_policy_value` | integer (int32) | Yes |  |
| `keep_policy` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | Yes |  |
| `enable_window` | boolean | Yes |  |
| `full_time_point` | [BackupPlanTimePoint](../Backup/BackupPlanTimePoint.md) | Yes |  |
| `full_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | Yes |  |
| `full_interval` | integer (int32) | Yes |  |
| `incremental_interval` | integer (int32) | Yes |  |
| `incremental_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | Yes |  |
| `snapshot_consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | Yes |  |
| `compression` | boolean | Yes |  |
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | Yes |  |
| `backup_store_repository_id` | string | Yes |  |
| `backup_service_id` | string | Yes |  |
| `name` | string | Yes |  |
| `backup_delay_option` | [BackupPlanDelayOption](../Backup/BackupPlanDelayOption.md) | No |  |
| `window_end` | string | No |  |
| `window_start` | string | No |  |
| `incremental_weekdays` | Array of [WeekdayTypeEnum](../Weekday/WeekdayTypeEnum.md) | No |  |
| `incremental_time_points` | Array of [BackupPlanTimePoint](../Backup/BackupPlanTimePoint.md) | No |  |
| `description` | string | No |  |

