# BackupRestorePointRebuildParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [BackupRestorePointWhereInput](../Backup/BackupRestorePointWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rebuild_network_mapping` | Array of [BackupRestoreExecutionNetworkMapping](../Backup/BackupRestoreExecutionNetworkMapping.md) | Yes |  |
| `rebuild_target_host_id` | string | Yes |  |
| `rebuild_target_cluster_id` | string | Yes |  |
| `rebuild_name` | string | Yes |  |
| `startup_after_restore` | boolean | Yes |  |

