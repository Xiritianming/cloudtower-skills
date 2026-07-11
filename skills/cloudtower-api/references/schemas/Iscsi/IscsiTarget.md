# IscsiTarget

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `chap_enabled` | boolean | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `external_use` | boolean | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `ip_whitelist` | string | Yes |  |
| `iqn_name` | string | Yes |  |
| `iqn_whitelist` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
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
| `chap_name` | string | No |  |
| `chap_secret` | string | No |  |
| `configuration_adaptive` | boolean | No |  |
| `configuration_method` | any | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `encrypt_method` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `initiator_chaps` | Array of [NestedInitiatorChap](../Nested/NestedInitiatorChap.md) | No |  |
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
| `iscsi_luns_num` | integer (int32) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `prioritized` | boolean | No |  |
| `resiliency_type` | any | No |  |

