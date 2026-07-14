# VmTemplate

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | Yes |  |
| `cloud_init_supported` | boolean | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `cpu` | [NestedCpu](../Nested/NestedCpu.md) | Yes |  |
| `cpu_model` | string | Yes |  |
| `description` | string | Yes |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | Yes |  |
| `ha` | boolean | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `name` | string | Yes |  |
| `size` | integer (int64) | Yes |  |
| `vcpu` | integer (int32) | Yes |  |
| `win_opt` | boolean | Yes |  |
| `content_library_vm_template` | [NestedContentLibraryVmTemplate](../Nested/NestedContentLibraryVmTemplate.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `local_created_at` | string | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `video_type` | string | No |  |
| `vm_disks` | Array of [NestedFrozenDisks](../Nested/NestedFrozenDisks.md) | No |  |
| `vm_nics` | Array of [NestedTemplateNic](../Nested/NestedTemplateNic.md) | No |  |

