# VmCreateVmFromContentLibraryTemplateParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `is_full_copy` | boolean | Yes |  |
| `template_id` | string | Yes |  |
| `name` | string | Yes |  |
| `cluster_id` | string | Yes |  |
| `owner` | [VmOwnerParams](../Vm/VmOwnerParams.md) | No |  |
| `gpu_devices` | Array of [VmGpuOperationParams](../Vm/VmGpuOperationParams.md) | No |  |
| `cloud_init` | [TemplateCloudInit](../Template/TemplateCloudInit.md) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int64) | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `vcpu` | integer (int32) | No |  |
| `status` | [VmStatus](../Vm/VmStatus.md) | No |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `ha_priority` | [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `ha` | boolean | No |  |
| `pci_nics` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `vm_placement_group` | [VmPlacementGroupWhereInput](../Vm/VmPlacementGroupWhereInput.md) | No |  |
| `vm_nics` | Array of [VmNicParams](../Vm/VmNicParams.md) | No |  |
| `disk_operate` | [VmDiskOperate](../Vm/VmDiskOperate.md) | No |  |
| `memory_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `memory` | integer (int64) | No |  |
| `cpu_cores` | integer (int32) | No |  |
| `cpu_sockets` | integer (int32) | No |  |
| `guest_os_type` | [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `folder_id` | string | No |  |
| `description` | string | No |  |
| `host_id` | string | No |  |

