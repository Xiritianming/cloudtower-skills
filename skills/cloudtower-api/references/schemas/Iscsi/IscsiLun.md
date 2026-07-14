# IscsiLun

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allowed_initiators` | string | Yes |  |
| `assigned_size` | integer (int64) | Yes |  |
| `bps` | integer (int64) | Yes |  |
| `bps_max` | integer (int64) | Yes |  |
| `bps_max_length` | integer (int64) | Yes |  |
| `bps_rd` | integer (int64) | Yes |  |
| `bps_rd_max` | integer (int64) | Yes |  |
| `bps_rd_max_length` | integer (int64) | Yes |  |
| `bps_wr` | integer (int64) | Yes |  |
| `bps_wr_max` | integer (int64) | Yes |  |
| `bps_wr_max_length` | integer (int64) | Yes |  |
| `id` | string | Yes |  |
| `io_size` | integer (int64) | Yes |  |
| `iops` | integer (int64) | Yes |  |
| `iops_max` | integer (int64) | Yes |  |
| `iops_max_length` | integer (int64) | Yes |  |
| `iops_rd` | integer (int64) | Yes |  |
| `iops_rd_max` | integer (int64) | Yes |  |
| `iops_rd_max_length` | integer (int64) | Yes |  |
| `iops_wr` | integer (int64) | Yes |  |
| `iops_wr_max` | integer (int64) | Yes |  |
| `iops_wr_max_length` | integer (int64) | Yes |  |
| `iscsi_target` | [NestedIscsiTarget](../Nested/NestedIscsiTarget.md) | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `lun_id` | integer (int32) | Yes |  |
| `name` | string | Yes |  |
| `replica_num` | integer (int32) | Yes |  |
| `shared_size` | integer (int64) | Yes |  |
| `snapshot_num` | integer (int32) | Yes |  |
| `stripe_num` | integer (int32) | Yes |  |
| `stripe_size` | integer (int64) | Yes |  |
| `thin_provision` | boolean | Yes |  |
| `unique_size` | integer (int64) | Yes |  |
| `zbs_volume_id` | string | Yes |  |
| `business_host_groups` | Array of [NestedBusinessHostGroup](../Nested/NestedBusinessHostGroup.md) | No |  |
| `business_host_is_same_with_parent` | boolean | No |  |
| `business_hosts` | Array of [NestedBusinessHost](../Nested/NestedBusinessHost.md) | No |  |
| `configuration_method` | [ConfigurationMethod](../Configuration/ConfigurationMethod.md) | No |  |
| `consistency_group` | [NestedConsistencyGroup](../Nested/NestedConsistencyGroup.md) | No |  |
| `downgraded_prioritized_space` | integer (int64) | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `encrypt_method` | [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `prioritized` | boolean | No |  |
| `replication_plans` | Array of [NestedReplicationPlan](../Nested/NestedReplicationPlan.md) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `snapshot_plans` | Array of [NestedSnapshotPlan](../Nested/NestedSnapshotPlan.md) | No |  |
| `unique_logical_size` | number (double) | No |  |

