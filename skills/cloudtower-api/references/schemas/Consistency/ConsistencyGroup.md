# ConsistencyGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `unique_size` | integer (int64) | Yes |  |
| `consistency_group_snapshots` | Array of [NestedConsistencyGroupSnapshot](../Nested/NestedConsistencyGroupSnapshot.md) | No |  |
| `entityAsyncStatus` | any | No |  |
| `iscsi_luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `namespaces` | Array of [NestedNvmfNamespace](../Nested/NestedNvmfNamespace.md) | No |  |

