# VmDiskOperate

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `remove_disks` | object | No |  |
| `modify_disks` | Array of [DiskOperateModifyDisk](../Disk/DiskOperateModifyDisk.md) | No |  |
| `new_disks` | [VmDiskParams](../Vm/VmDiskParams.md) | No |  |

## Nested Fields

### `remove_disks`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disk_index` | integer[] | Yes |  |

