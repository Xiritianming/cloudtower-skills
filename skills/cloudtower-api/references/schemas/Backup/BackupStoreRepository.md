# BackupStoreRepository

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `createdAt` | string | Yes |  |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `status` | [BackupStoreStatus](../Backup/BackupStoreStatus.md) | Yes |  |
| `total_capacity` | integer (int64) | Yes |  |
| `type` | [BackupStoreType](../Backup/BackupStoreType.md) | Yes |  |
| `used_data_space` | integer (int64) | Yes |  |
| `backup_plans` | Array of [NestedBackupPlan](../Nested/NestedBackupPlan.md) | No |  |
| `backup_restore_points` | Array of [NestedBackupRestorePoint](../Nested/NestedBackupRestorePoint.md) | No |  |
| `backup_service` | [NestedBackupService](../Nested/NestedBackupService.md) | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `error_code` | string | No |  |
| `iscsi_chap_name` | string | No |  |
| `iscsi_chap_secret` | string | No |  |
| `iscsi_ip` | string | No |  |
| `iscsi_lun_id` | string | No |  |
| `iscsi_port` | integer (int32) | No |  |
| `iscsi_target_iqn` | string | No |  |
| `nfs_path` | string | No |  |
| `nfs_server` | string | No |  |
| `update_timestamp` | string | No |  |
| `used_data_space_usage` | number (double) | No |  |
| `valid_data_space` | integer (int64) | No |  |

