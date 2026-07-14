# LogCollection

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `groups` | string[] | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `log_ended_at` | string | Yes |  |
| `log_started_at` | string | Yes |  |
| `owner` | string | Yes |  |
| `path` | string | Yes |  |
| `progress` | number (double) | Yes |  |
| `services` | string[] | Yes |  |
| `size` | integer (int64) | Yes |  |
| `started_at` | string | Yes |  |
| `status` | [LogCollectionStatus](../Log/LogCollectionStatus.md) | Yes |  |
| `hosts` | Array of [NestedHost](../Nested/NestedHost.md) | No |  |
| `service_groups` | object | No |  |
| `witness` | [NestedWitness](../Nested/NestedWitness.md) | No |  |

## Nested Fields

### `service_groups`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


