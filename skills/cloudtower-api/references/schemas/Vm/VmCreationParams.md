# VmCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `status` | [VmStatus](../Vm/VmStatus.md) | Yes |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | Yes |  |
| `ha` | boolean | Yes |  |
| `vm_nics` | Array of [VmNicParams](../Vm/VmNicParams.md) | Yes |  |
| `vm_disks` | [VmDiskParams](../Vm/VmDiskParams.md) | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `cpu_cores` | integer (int32) | Yes |  |
| `cpu_sockets` | integer (int32) | Yes |  |
| `name` | string | Yes |  |
| `cluster_id` | string | Yes |  |
| `owner` | [VmOwnerParams](../Vm/VmOwnerParams.md) | No |  |
| `gpu_devices` | Array of [VmGpuOperationParams](../Vm/VmGpuOperationParams.md) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int64) | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `vcpu` | integer (int32) | No |  |
| `ha_priority` | [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `pci_nics` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `vm_placement_group` | [VmPlacementGroupWhereInput](../Vm/VmPlacementGroupWhereInput.md) | No |  |
| `memory_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `guest_os_type` | [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `folder_id` | string | No |  |
| `description` | string | No |  |
| `host_id` | string | No |  |

