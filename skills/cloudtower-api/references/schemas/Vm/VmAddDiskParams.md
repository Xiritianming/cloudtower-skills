# VmAddDiskParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VmWhereInput](../Vm/VmWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_disks` | object | Yes |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int64) | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |

#### `data.vm_disks`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mount_disks` | Array of [MountDisksParams](../Mount/MountDisksParams.md) | No |  |
| `mount_new_create_disks` | Array of [MountNewCreateDisksParams](../Mount/MountNewCreateDisksParams.md) | No |  |

