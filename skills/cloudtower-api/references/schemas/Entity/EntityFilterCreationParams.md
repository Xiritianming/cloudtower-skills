# EntityFilterCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rules` | Array of [FilterRuleInput](../Filter/FilterRuleInput.md) | Yes |  |
| `name` | string | Yes |  |
| `exclude_vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `apply_to_all_clusters` | boolean | No |  |

