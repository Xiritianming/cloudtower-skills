# NfsExportUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `where` | [NfsExportWhereInput](../Nfs/NfsExportWhereInput.md) | Yes |  |
| `data` | object | No |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ec_m` | number (double) | No |  |
| `ec_k` | number (double) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `replica_num` | number (double) | No |  |
| `ip_whitelist` | string | No |  |
| `name` | string | No |  |

