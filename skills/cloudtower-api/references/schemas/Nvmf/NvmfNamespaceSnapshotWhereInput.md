# NvmfNamespaceSnapshotWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [NvmfNamespaceSnapshotWhereInput](../Nvmf/NvmfNamespaceSnapshotWhereInput.md) | No |  |
| `NOT` | Array of [NvmfNamespaceSnapshotWhereInput](../Nvmf/NvmfNamespaceSnapshotWhereInput.md) | No |  |
| `OR` | Array of [NvmfNamespaceSnapshotWhereInput](../Nvmf/NvmfNamespaceSnapshotWhereInput.md) | No |  |
| `consistency_group_snapshot` | [ConsistencyGroupSnapshotWhereInput](../Consistency/ConsistencyGroupSnapshotWhereInput.md) | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_k_gt` | integer (int32) | No |  |
| `ec_k_gte` | integer (int32) | No |  |
| `ec_k_in` | integer[] | No |  |
| `ec_k_lt` | integer (int32) | No |  |
| `ec_k_lte` | integer (int32) | No |  |
| `ec_k_not` | integer (int32) | No |  |
| `ec_k_not_in` | integer[] | No |  |
| `ec_m` | integer (int32) | No |  |
| `ec_m_gt` | integer (int32) | No |  |
| `ec_m_gte` | integer (int32) | No |  |
| `ec_m_in` | integer[] | No |  |
| `ec_m_lt` | integer (int32) | No |  |
| `ec_m_lte` | integer (int32) | No |  |
| `ec_m_not` | integer (int32) | No |  |
| `ec_m_not_in` | integer[] | No |  |
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
| `nvmf_namespace` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `nvmf_subsystem` | [NvmfSubsystemWhereInput](../Nvmf/NvmfSubsystemWhereInput.md) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_in` | Array of [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_not` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_not_in` | Array of [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `snapshot_group` | [SnapshotGroupWhereInput](../Snapshot/SnapshotGroupWhereInput.md) | No |  |
| `unique_size` | integer (int64) | No |  |
| `unique_size_gt` | integer (int64) | No |  |
| `unique_size_gte` | integer (int64) | No |  |
| `unique_size_in` | integer[] | No |  |
| `unique_size_lt` | integer (int64) | No |  |
| `unique_size_lte` | integer (int64) | No |  |
| `unique_size_not` | integer (int64) | No |  |
| `unique_size_not_in` | integer[] | No |  |

