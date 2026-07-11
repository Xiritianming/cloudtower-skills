# UpdateVmVolumeParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `where` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | Yes |  |
| `data` | object | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `size_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `size` | integer (int64) | No |  |
| `description` | string | No |  |
| `name` | string | No |  |

