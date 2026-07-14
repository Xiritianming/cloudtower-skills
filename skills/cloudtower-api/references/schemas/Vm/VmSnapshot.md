# VmSnapshot

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | Yes |  |
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
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `ha_priority` | [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `local_created_at` | string | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `snapshot_group` | [NestedSnapshotGroup](../Nested/NestedSnapshotGroup.md) | No |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | No |  |
| `vm_disks` | Array of [NestedFrozenDisks](../Nested/NestedFrozenDisks.md) | No |  |
| `vm_nics` | Array of [NestedFrozenNic](../Nested/NestedFrozenNic.md) | No |  |

