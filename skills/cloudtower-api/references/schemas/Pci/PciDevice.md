# PciDevice

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `bus` | string | Yes |  |
| `bus_location` | string | Yes |  |
| `class_code` | string | Yes |  |
| `function_num` | string | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `product_id` | string | Yes |  |
| `slot` | string | Yes |  |
| `subsystem_product_id` | string | Yes |  |
| `subsystem_vendor_id` | string | Yes |  |
| `vendor_id` | string | Yes |  |
| `verdor_name` | string | Yes |  |
| `device_type` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `iommu_status` | [IommuStatus](../Iommu/IommuStatus.md) | No |  |
| `mdev_state` | [PciDeviceMdevState](../Pci/PciDeviceMdevState.md) | No |  |
| `mdev_type_id` | string | No |  |
| `partitioning_state` | [PciDevicePartitionState](../Pci/PciDevicePartitionState.md) | No |  |
| `sriov_state` | [PciDeviceSriovState](../Pci/PciDeviceSriovState.md) | No |  |
| `total_mdev_num` | integer (int32) | No |  |
| `total_partitioning_num` | integer (int32) | No |  |
| `total_vf_num` | integer (int32) | No |  |
| `usage_type` | [PciDeviceType](../Pci/PciDeviceType.md) | No |  |
| `used_mdev_num` | integer (int32) | No |  |
| `used_partitioning_num` | integer (int32) | No |  |
| `used_vf_num` | integer (int32) | No |  |
| `user_usage` | [PciDeviceUsage](../Pci/PciDeviceUsage.md) | No |  |

