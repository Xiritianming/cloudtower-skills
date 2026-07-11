# HostUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [HostWhereInput](../Host/HostWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ipmi` | [HostBatchCreateIpmiInput](../Host/HostBatchCreateIpmiInput.md) | No |  |
| `scvm_name` | string | No |  |
| `name` | string | No |  |

