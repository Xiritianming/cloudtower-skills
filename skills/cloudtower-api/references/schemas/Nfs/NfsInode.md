# NfsInode

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `assigned_size` | integer (int64) | Yes |  |
| `file` | boolean | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `local_updated_at` | string | Yes |  |
| `name` | string | Yes |  |
| `nfs_export` | [NestedNfsExport](../Nested/NestedNfsExport.md) | Yes |  |
| `parent_id` | string | Yes |  |
| `shared_size` | integer (int64) | Yes |  |
| `snapshot_num` | integer (int32) | Yes |  |
| `unique_size` | integer (int64) | Yes |  |
| `downgraded_prioritized_space` | integer (int64) | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `encrypt_method` | [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `prioritized` | boolean | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `unique_logical_size` | number (double) | No |  |

