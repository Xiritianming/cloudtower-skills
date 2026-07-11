# VmImportParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes |  |
| `cluster_id` | string | Yes |  |
| `upload_tasks` | string[] | Yes |  |
| `parsed_ovf` | [ParsedOVF](../Parsed/ParsedOVF.md) | Yes |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int64) | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `vcpu` | integer (int32) | No |  |
| `status` | [VmStatus](../Vm/VmStatus.md) | No |  |
| `ha` | boolean | No |  |
| `vm_nics` | Array of [VmImportNicParams](../Vm/VmImportNicParams.md) | No |  |
| `disk_operate` | [OvfDiskOperate](../Ovf/OvfDiskOperate.md) | No |  |
| `memory_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `memory` | integer (int64) | No |  |
| `cpu_cores` | integer (int32) | No |  |
| `cpu_sockets` | integer (int32) | No |  |
| `guest_os_type` | [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `folder_id` | string | No |  |
| `description` | string | No |  |
| `host_id` | string | No |  |
| `owner_id` | string | No |  |

