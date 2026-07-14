# GpuDevice

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `brand` | string | Yes |  |
| `bus_location` | string | Yes |  |
| `description` | string | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `model` | string | Yes |  |
| `name` | string | Yes |  |
| `status` | [GpuDeviceStatus](../Gpu/GpuDeviceStatus.md) | Yes |  |
| `assigned_vgpus_num` | integer (int32) | No |  |
| `available_vgpus_num` | integer (int32) | No |  |
| `driver_info` | [NestedGpuDriverInfo](../Nested/NestedGpuDriverInfo.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `is_nvidia_tools_ready` | boolean | No |  |
| `is_nvidia_vfs_enabled` | boolean | No |  |
| `is_nvidia_vfs_supported` | boolean | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `mdev_supported_types` | Array of [NestedVgpuType](../Nested/NestedVgpuType.md) | No |  |
| `user_usage` | [GpuDeviceUsage](../Gpu/GpuDeviceUsage.md) | No |  |
| `user_vgpu_type_id` | string | No |  |
| `user_vgpu_type_name` | string | No |  |
| `vgpu_instance_num` | integer (int32) | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |

