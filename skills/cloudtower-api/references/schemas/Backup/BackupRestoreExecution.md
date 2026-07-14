# BackupRestoreExecution

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `executed_at` | string | Yes |  |
| `id` | string | Yes |  |
| `mode` | [BackupRestoreExecutionMode](../Backup/BackupRestoreExecutionMode.md) | Yes |  |
| `name` | string | Yes |  |
| `startup_after_restore` | boolean | Yes |  |
| `status` | [BackupExecutionStatus](../Backup/BackupExecutionStatus.md) | Yes |  |
| `backup_restore_point` | [NestedBackupRestorePoint](../Nested/NestedBackupRestorePoint.md) | No |  |
| `duration` | integer (int32) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `read_bytes` | integer (int64) | No |  |
| `rebuild_name` | string | No |  |
| `rebuild_network_mapping` | Array of [NestedBackupRestoreExecutionNetworkMapping](../Nested/NestedBackupRestoreExecutionNetworkMapping.md) | No |  |
| `rebuild_target_cluster` | string | No |  |
| `retry_times` | integer (int32) | No |  |
| `total_bytes` | integer (int64) | No |  |

