# VmUpdateIoPolicyParams

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
| `each_disk` | Array of [VmUpdateEachDiskIoPolicyParams](../Vm/VmUpdateEachDiskIoPolicyParams.md) | No |  |
| `whole_vm` | [VmRestrictIoParamsData](../Vm/VmRestrictIoParamsData.md) | No |  |
| `io_policy` | any | No |  |

