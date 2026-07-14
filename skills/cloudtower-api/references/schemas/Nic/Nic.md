# Nic

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `mac_address` | string | Yes |  |
| `mtu` | integer (int32) | Yes |  |
| `name` | string | Yes |  |
| `physical` | boolean | Yes |  |
| `running` | boolean | Yes |  |
| `up` | boolean | Yes |  |
| `driver` | string | No |  |
| `driver_state` | [NicDriverState](../Nic/NicDriverState.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `gateway_ip` | string | No |  |
| `ibdev` | string | No |  |
| `iommu_status` | [IommuStatus](../Iommu/IommuStatus.md) | No |  |
| `ip_address` | string | No |  |
| `is_sriov` | boolean | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `max_vf_num` | integer (int32) | No |  |
| `model` | string | No |  |
| `nic_uuid` | string | No |  |
| `rdma_enabled` | boolean | No |  |
| `speed` | integer (int64) | No |  |
| `subnet_mask` | string | No |  |
| `total_vf_num` | integer (int32) | No |  |
| `type` | [NetworkType](../Network/NetworkType.md) | No |  |
| `used_vf_num` | integer (int32) | No |  |
| `user_usage` | [NicUserUsage](../Nic/NicUserUsage.md) | No |  |
| `vds` | [NestedVds](../Nested/NestedVds.md) | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |

