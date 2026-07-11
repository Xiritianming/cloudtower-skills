# NvmfSubsystem

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `external_use` | boolean | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `ip_whitelist` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `nqn_name` | string | Yes |  |
| `nqn_whitelist` | string | Yes |  |
| `policy` | [NvmfSubsystemPolicyType](../Nvmf/NvmfSubsystemPolicyType.md) | Yes |  |
| `replica_num` | integer (int32) | Yes |  |
| `stripe_num` | integer (int32) | Yes |  |
| `stripe_size` | integer (int64) | Yes |  |
| `thin_provision` | boolean | Yes |  |
| `bps` | integer (int64) | No |  |
| `bps_max` | integer (int64) | No |  |
| `bps_max_length` | integer (int64) | No |  |
| `bps_rd` | integer (int64) | No |  |
| `bps_rd_max` | integer (int64) | No |  |
| `bps_rd_max_length` | integer (int64) | No |  |
| `bps_wr` | integer (int64) | No |  |
| `bps_wr_max` | integer (int64) | No |  |
| `bps_wr_max_length` | integer (int64) | No |  |
| `business_host_groups` | Array of [NestedBusinessHostGroup](../Nested/NestedBusinessHostGroup.md) | No |  |
| `business_hosts` | Array of [NestedBusinessHost](../Nested/NestedBusinessHost.md) | No |  |
| `configuration_adaptive` | boolean | No |  |
| `configuration_method` | any | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `encrypt_method` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `io_size` | integer (int64) | No |  |
| `iops` | integer (int64) | No |  |
| `iops_max` | integer (int64) | No |  |
| `iops_max_length` | integer (int64) | No |  |
| `iops_rd` | integer (int64) | No |  |
| `iops_rd_max` | integer (int64) | No |  |
| `iops_rd_max_length` | integer (int64) | No |  |
| `iops_wr` | integer (int64) | No |  |
| `iops_wr_max` | integer (int64) | No |  |
| `iops_wr_max_length` | integer (int64) | No |  |
| `iscsi_connections` | Array of [NestedIscsiConnection](../Nested/NestedIscsiConnection.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `namespace_groups` | Array of [NestedNamespaceGroup](../Nested/NestedNamespaceGroup.md) | No |  |
| `namespaces` | Array of [NestedNvmfNamespace](../Nested/NestedNvmfNamespace.md) | No |  |
| `nvmf_namespaces_num` | integer (int32) | No |  |
| `prioritized` | boolean | No |  |
| `resiliency_type` | any | No |  |

