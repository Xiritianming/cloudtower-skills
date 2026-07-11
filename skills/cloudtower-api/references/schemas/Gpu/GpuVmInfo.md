# GpuVmInfo

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vms` | Array of [GpuVmDetail](../Gpu/GpuVmDetail.md) | Yes |  |
| `status` | [GpuDeviceStatus](../Gpu/GpuDeviceStatus.md) | Yes |  |
| `name` | string | Yes |  |
| `model` | string | Yes |  |
| `local_id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `id` | string | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `description` | string | Yes |  |
| `bus_location` | string | Yes |  |
| `brand` | string | Yes |  |
| `vgpu_instance_num` | integer (int32) | No |  |
| `user_vgpu_type_name` | string | No |  |
| `user_vgpu_type_id` | string | No |  |
| `user_usage` | any | No |  |
| `mdev_supported_types` | Array of [NestedVgpuType](../Nested/NestedVgpuType.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `is_nvidia_vfs_supported` | boolean | No |  |
| `is_nvidia_vfs_enabled` | boolean | No |  |
| `is_nvidia_tools_ready` | boolean | No |  |
| `entityAsyncStatus` | any | No |  |
| `driver_info` | any | No |  |
| `available_vgpus_num` | integer (int32) | No |  |
| `assigned_vgpus_num` | integer (int32) | No |  |

