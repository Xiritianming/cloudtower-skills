# VmUpdateAdvancedOptionsParams

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
| `video_type` | [VmVideoType](../Vm/VmVideoType.md) | No |  |
| `windows_optimize` | boolean | No |  |
| `cpu_model` | string | No |  |
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |

