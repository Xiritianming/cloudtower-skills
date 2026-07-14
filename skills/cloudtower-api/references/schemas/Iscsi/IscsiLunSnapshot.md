# IscsiLunSnapshot

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `iscsi_target` | [NestedIscsiTarget](../Nested/NestedIscsiTarget.md) | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `unique_size` | integer (int64) | Yes |  |
| `consistency_group_snapshot` | [NestedConsistencyGroupSnapshot](../Nested/NestedConsistencyGroupSnapshot.md) | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `iscsi_lun` | [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `snapshot_group` | [NestedSnapshotGroup](../Nested/NestedSnapshotGroup.md) | No |  |

