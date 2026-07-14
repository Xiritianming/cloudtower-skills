# VmDiskMetaData

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_volume_size` | number (double) | No |  |
| `vm_volume_sharing` | boolean | No |  |
| `vm_volume_path` | string | No |  |
| `vm_volume_name` | string | No |  |
| `vm_volume_mounting` | boolean | No |  |
| `vm_volume_lun_zbs_volume_id` | string | No |  |
| `vm_volume_elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `type` | [VmDiskType](../Vm/VmDiskType.md) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth` | number (double) | No |  |
| `disabled` | boolean | No |  |
| `bus` | [Bus](../Bus/Bus.md) | No |  |
| `boot` | integer (int32) | No |  |

