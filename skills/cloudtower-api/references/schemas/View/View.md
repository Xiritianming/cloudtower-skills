# View

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `time_span` | integer (int32) | Yes |  |
| `time_unit` | [TimeUnit](../Time/TimeUnit.md) | Yes |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `graphs` | Array of [NestedGraph](../Nested/NestedGraph.md) | No |  |

