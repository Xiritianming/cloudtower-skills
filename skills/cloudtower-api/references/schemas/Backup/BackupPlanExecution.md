# BackupPlanExecution

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `method` | [BackupExecutionMethod](../Backup/BackupExecutionMethod.md) | Yes |  |
| `status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | Yes |  |
| `type` | [BackupExecutionType](../Backup/BackupExecutionType.md) | Yes |  |
| `backup_plan` | any | No |  |
| `deletable_flag_marked` | boolean | No |  |
| `duration` | integer (int32) | No |  |
| `entityAsyncStatus` | any | No |  |
| `executed_at` | string | No |  |
| `state` | any | No |  |
| `success_job_count` | integer (int32) | No |  |
| `total_job_count` | integer (int32) | No |  |

