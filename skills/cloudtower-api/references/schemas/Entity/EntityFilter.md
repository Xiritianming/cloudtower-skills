# EntityFilter

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entity_type` | [EntityType](../Entity/EntityType.md) | Yes |  |
| `exclude_ids` | string[] | Yes |  |
| `filter_error` | string[] | Yes |  |
| `filter_status` | [FilterStatus](../Filter/FilterStatus.md) | Yes |  |
| `id` | string | Yes |  |
| `ids` | string[] | Yes |  |
| `name` | string | Yes |  |
| `rules` | Array of [NestedFilterRule](../Nested/NestedFilterRule.md) | Yes |  |
| `apply_to_all_clusters` | boolean | No |  |
| `clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `exec_failed_cluster` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `last_executed_at` | string | No |  |
| `preset` | string | No |  |

