# BackupService

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `kube_config` | string | Yes |  |
| `name` | string | Yes |  |
| `application` | any | No |  |
| `backup_clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `backup_network_gateway` | string | No |  |
| `backup_network_ip` | string | No |  |
| `backup_network_subnet_mask` | string | No |  |
| `backup_network_type` | any | No |  |
| `backup_network_vlan` | string | No |  |
| `backup_plans` | Array of [NestedBackupPlan](../Nested/NestedBackupPlan.md) | No |  |
| `backup_rd_iops_max` | integer (int64) | No |  |
| `backup_store_repositories` | Array of [NestedBackupStoreRepository](../Nested/NestedBackupStoreRepository.md) | No |  |
| `backup_wr_iops_max` | integer (int64) | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | any | No |  |
| `management_network_gateway` | string | No |  |
| `management_network_ip` | string | No |  |
| `management_network_subnet_mask` | string | No |  |
| `management_network_vlan` | string | No |  |
| `max_job_retry_times` | integer (int32) | No |  |
| `max_parallel_backup_jobs` | integer (int32) | No |  |
| `max_parallel_restore_jobs` | integer (int32) | No |  |
| `network_status` | Array of [NestedBackupServiceNetworkStatus](../Nested/NestedBackupServiceNetworkStatus.md) | No |  |
| `restore_rd_iops_max` | integer (int64) | No |  |
| `restore_wr_iops_max` | integer (int64) | No |  |
| `retry_interval` | integer (int32) | No |  |
| `running_vm` | any | No |  |
| `status` | any | No |  |
| `storage_network_gateway` | string | No |  |
| `storage_network_ip` | string | No |  |
| `storage_network_subnet_mask` | string | No |  |
| `storage_network_type` | any | No |  |
| `storage_network_vlan` | string | No |  |

