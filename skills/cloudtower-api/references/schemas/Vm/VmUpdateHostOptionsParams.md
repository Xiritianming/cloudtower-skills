# VmUpdateHostOptionsParams

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
| `ntp_servers` | string[] | No |  |
| `dns_servers` | string[] | No |  |
| `hostname` | string | No |  |

