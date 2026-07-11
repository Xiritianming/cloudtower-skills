# VmUpdateNicBasicInfoParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `subnet_mask` | string | No |  |
| `gateway` | string | No |  |
| `ip_address` | string | No |  |

