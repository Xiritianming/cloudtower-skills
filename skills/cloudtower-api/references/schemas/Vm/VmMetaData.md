# VmMetaData

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `win_opt` | boolean | No |  |
| `vm_tools_status` | [VmToolsStatus](../Vm/VmToolsStatus.md) | No |  |
| `vm_nics` | Array of [VmNicMetaData](../Vm/VmNicMetaData.md) | No |  |
| `vm_disks` | Array of [VmDiskMetaData](../Vm/VmDiskMetaData.md) | No |  |
| `video_type` | [VmVideoType](../Vm/VmVideoType.md) | No |  |
| `vcpu` | integer (int32) | No |  |
| `sync_vm_time_on_resume` | boolean | No |  |
| `protected` | boolean | No |  |
| `nested_virtualization` | boolean | No |  |
| `name` | string | No |  |
| `memory` | number (double) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth` | number (double) | No |  |
| `local_id` | string | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `internal` | boolean | No |  |
| `host_local_id` | string | No |  |
| `ha_priority` | [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `ha` | boolean | No |  |
| `guest_os_type` | [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `description` | string | No |  |
| `cpu_sockets` | integer (int32) | No |  |
| `cpu_model` | string | No |  |
| `cpu_exclusive_expected_enabled` | boolean | No |  |
| `cpu_cores` | integer (int32) | No |  |
| `cluster_vhost_enabled` | boolean | No |  |
| `cluster_version` | string | No |  |
| `cluster_type` | [ClusterType](../Cluster/ClusterType.md) | No |  |
| `cluster_local_id` | string | No |  |
| `cluster_architecture` | [Architecture](../Architecture/Architecture.md) | No |  |
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `boot_with_host` | boolean | No |  |

