# ConsistencyGroupWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `NOT` | Array of [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `OR` | Array of [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `consistency_group_snapshots_every` | [ConsistencyGroupSnapshotWhereInput](../Consistency/ConsistencyGroupSnapshotWhereInput.md) | No |  |
| `consistency_group_snapshots_none` | [ConsistencyGroupSnapshotWhereInput](../Consistency/ConsistencyGroupSnapshotWhereInput.md) | No |  |
| `consistency_group_snapshots_some` | [ConsistencyGroupSnapshotWhereInput](../Consistency/ConsistencyGroupSnapshotWhereInput.md) | No |  |
| `description` | string | No |  |
| `description_contains` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_gt` | string | No |  |
| `description_gte` | string | No |  |
| `description_in` | string[] | No |  |
| `description_lt` | string | No |  |
| `description_lte` | string | No |  |
| `description_not` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_starts_with` | string | No |  |
| `description_starts_with` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `id` | string | No |  |
| `id_contains` | string | No |  |
| `id_ends_with` | string | No |  |
| `id_gt` | string | No |  |
| `id_gte` | string | No |  |
| `id_in` | string[] | No |  |
| `id_lt` | string | No |  |
| `id_lte` | string | No |  |
| `id_not` | string | No |  |
| `id_not_contains` | string | No |  |
| `id_not_ends_with` | string | No |  |
| `id_not_in` | string[] | No |  |
| `id_not_starts_with` | string | No |  |
| `id_starts_with` | string | No |  |
| `iscsi_luns_every` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `iscsi_luns_none` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `iscsi_luns_some` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `local_created_at` | string | No |  |
| `local_created_at_gt` | string | No |  |
| `local_created_at_gte` | string | No |  |
| `local_created_at_in` | string[] | No |  |
| `local_created_at_lt` | string | No |  |
| `local_created_at_lte` | string | No |  |
| `local_created_at_not` | string | No |  |
| `local_created_at_not_in` | string[] | No |  |
| `local_id` | string | No |  |
| `local_id_contains` | string | No |  |
| `local_id_ends_with` | string | No |  |
| `local_id_gt` | string | No |  |
| `local_id_gte` | string | No |  |
| `local_id_in` | string[] | No |  |
| `local_id_lt` | string | No |  |
| `local_id_lte` | string | No |  |
| `local_id_not` | string | No |  |
| `local_id_not_contains` | string | No |  |
| `local_id_not_ends_with` | string | No |  |
| `local_id_not_in` | string[] | No |  |
| `local_id_not_starts_with` | string | No |  |
| `local_id_starts_with` | string | No |  |
| `name` | string | No |  |
| `name_contains` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_gt` | string | No |  |
| `name_gte` | string | No |  |
| `name_in` | string[] | No |  |
| `name_lt` | string | No |  |
| `name_lte` | string | No |  |
| `name_not` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_starts_with` | string | No |  |
| `name_starts_with` | string | No |  |
| `namespaces_every` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `namespaces_none` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `namespaces_some` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `unique_size` | integer (int64) | No |  |
| `unique_size_gt` | integer (int64) | No |  |
| `unique_size_gte` | integer (int64) | No |  |
| `unique_size_in` | integer[] | No |  |
| `unique_size_lt` | integer (int64) | No |  |
| `unique_size_lte` | integer (int64) | No |  |
| `unique_size_not` | integer (int64) | No |  |
| `unique_size_not_in` | integer[] | No |  |

