# BackupPlanUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disconnect_strategy` | [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `keep_policy_value` | integer (int32) | No |  |
| `keep_policy` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `backup_delay_option` | [BackupPlanDelayOption](../Backup/BackupPlanDelayOption.md) | No |  |
| `window_end` | string | No |  |
| `window_start` | string | No |  |
| `enable_window` | boolean | No |  |
| `full_time_point` | [BackupPlanTimePoint](../Backup/BackupPlanTimePoint.md) | No |  |
| `full_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `full_interval` | integer (int32) | No |  |
| `incremental_weekdays` | Array of [WeekdayTypeEnum](../Weekday/WeekdayTypeEnum.md) | No |  |
| `incremental_time_points` | Array of [BackupPlanTimePoint](../Backup/BackupPlanTimePoint.md) | No |  |
| `incremental_interval` | integer (int32) | No |  |
| `incremental_period` | [BackupPlanPeriod](../Backup/BackupPlanPeriod.md) | No |  |
| `snapshot_consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `compression` | boolean | No |  |
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `description` | string | No |  |
| `name` | string | No |  |

