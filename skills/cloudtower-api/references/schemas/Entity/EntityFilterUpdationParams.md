# EntityFilterUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [EntityFilterWhereInput](../Entity/EntityFilterWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `exclude_vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `apply_to_all_clusters` | boolean | No |  |
| `rules` | Array of [FilterRuleInput](../Filter/FilterRuleInput.md) | No |  |
| `name` | string | No |  |

