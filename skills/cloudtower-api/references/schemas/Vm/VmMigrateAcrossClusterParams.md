# VmMigrateAcrossClusterParams

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
| `vm_config` | [MigrateVmConfig](../Migrate/MigrateVmConfig.md) | Yes |  |
| `cluster_id` | string | Yes |  |
| `host_id` | string | No |  |

