# VmDisk

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `boot` | integer (int32) | Yes |  |
| `bus` | [Bus](../Bus/Bus.md) | Yes |  |
| `id` | string | Yes |  |
| `type` | [VmDiskType](../Vm/VmDiskType.md) | Yes |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | Yes |  |
| `cloud_init_image_name` | string | No |  |
| `cloud_init_image_path` | string | No |  |
| `device` | string | No |  |
| `disabled` | boolean | No |  |
| `elf_image` | [NestedElfImage](../Nested/NestedElfImage.md) | No |  |
| `key` | integer (int32) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `serial` | string | No |  |
| `svt_image` | [NestedSvtImage](../Nested/NestedSvtImage.md) | No |  |
| `unsafe_image_path` | string | No |  |
| `unsafe_image_uuid` | string | No |  |
| `unsafe_provision` | string | No |  |
| `vm_volume` | [NestedVmVolume](../Nested/NestedVmVolume.md) | No |  |

