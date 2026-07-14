# ConsistencyGroupSnapshot

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `unique_size` | integer (int64) | Yes |  |
| `Iscsi_lun_snapshots` | Array of [NestedIscsiLunSnapshot](../Nested/NestedIscsiLunSnapshot.md) | No |  |
| `consistency_group` | [NestedConsistencyGroup](../Nested/NestedConsistencyGroup.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `nvmf_namespace_snapshots` | Array of [NestedNvmfNamespaceSnapshot](../Nested/NestedNvmfNamespaceSnapshot.md) | No |  |

