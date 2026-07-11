# NvmfNamespace

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
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
| `is_shared` | boolean | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `namespace_id` | integer (int32) | Yes |  |
| `nqn_whitelist` | string | Yes |  |
| `nvmf_subsystem` | [NestedNvmfSubsystem](../Nested/NestedNvmfSubsystem.md) | Yes |  |
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
| `configuration_method` | any | No |  |
| `consistency_group` | any | No |  |
| `downgraded_prioritized_space` | integer (int64) | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `encrypt_method` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `namespace_group` | any | No |  |
| `prioritized` | boolean | No |  |
| `resiliency_type` | any | No |  |
| `snapshot_plans` | Array of [NestedSnapshotPlan](../Nested/NestedSnapshotPlan.md) | No |  |
| `unique_logical_size` | number (double) | No |  |

