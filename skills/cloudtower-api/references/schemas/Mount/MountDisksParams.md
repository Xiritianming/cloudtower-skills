# MountDisksParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_volume_id` | string | Yes |  |
| `bus` | [Bus](../Bus/Bus.md) | Yes |  |
| `boot` | integer (int32) | Yes |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int64) | No |  |
| `index` | integer (int32) | No |  |
| `key` | integer (int32) | No |  |

