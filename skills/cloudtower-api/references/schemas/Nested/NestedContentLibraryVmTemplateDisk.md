# NestedContentLibraryVmTemplateDisk

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `boot` | integer (int32) | Yes |  |
| `bus` | [Bus](../Bus/Bus.md) | Yes |  |
| `index` | integer (int32) | Yes |  |
| `type` | [VmDiskType](../Vm/VmDiskType.md) | Yes |  |
| `content_library_image_id` | string | No |  |
| `disabled` | boolean | No |  |
| `disk_name` | string | No |  |
| `elf_storage_policy_ec_k` | integer (int32) | No |  |
| `elf_storage_policy_ec_m` | integer (int32) | No |  |
| `elf_storage_policy_replica_num` | integer (int32) | No |  |
| `elf_storage_policy_thin_provision` | boolean | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `path` | string | No |  |
| `resident_in_cache` | boolean | No |  |
| `size` | integer (int64) | No |  |
| `storage_encrypted` | boolean | No |  |
| `storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |

