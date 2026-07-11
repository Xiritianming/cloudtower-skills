# GpuDeviceUsageUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [GpuDeviceWhereInput](../Gpu/GpuDeviceWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vgpu_spec` | string | No |  |
| `usage` | [GpuDeviceUsage](../Gpu/GpuDeviceUsage.md) | No |  |

