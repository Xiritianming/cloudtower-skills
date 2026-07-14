# NfsExportWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [NfsExportWhereInput](../Nfs/NfsExportWhereInput.md) | No |  |
| `NOT` | Array of [NfsExportWhereInput](../Nfs/NfsExportWhereInput.md) | No |  |
| `OR` | Array of [NfsExportWhereInput](../Nfs/NfsExportWhereInput.md) | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
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
| `encrypt_method` | [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `encrypt_method_in` | Array of [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `encrypt_method_not` | [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `encrypt_method_not_in` | Array of [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `export_inode_id` | string | No |  |
| `export_inode_id_contains` | string | No |  |
| `export_inode_id_ends_with` | string | No |  |
| `export_inode_id_gt` | string | No |  |
| `export_inode_id_gte` | string | No |  |
| `export_inode_id_in` | string[] | No |  |
| `export_inode_id_lt` | string | No |  |
| `export_inode_id_lte` | string | No |  |
| `export_inode_id_not` | string | No |  |
| `export_inode_id_not_contains` | string | No |  |
| `export_inode_id_not_ends_with` | string | No |  |
| `export_inode_id_not_in` | string[] | No |  |
| `export_inode_id_not_starts_with` | string | No |  |
| `export_inode_id_starts_with` | string | No |  |
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
| `inodes_every` | [NfsInodeWhereInput](../Nfs/NfsInodeWhereInput.md) | No |  |
| `inodes_none` | [NfsInodeWhereInput](../Nfs/NfsInodeWhereInput.md) | No |  |
| `inodes_some` | [NfsInodeWhereInput](../Nfs/NfsInodeWhereInput.md) | No |  |
| `internal` | boolean | No |  |
| `internal_not` | boolean | No |  |
| `ip_whitelist` | string | No |  |
| `ip_whitelist_contains` | string | No |  |
| `ip_whitelist_ends_with` | string | No |  |
| `ip_whitelist_gt` | string | No |  |
| `ip_whitelist_gte` | string | No |  |
| `ip_whitelist_in` | string[] | No |  |
| `ip_whitelist_lt` | string | No |  |
| `ip_whitelist_lte` | string | No |  |
| `ip_whitelist_not` | string | No |  |
| `ip_whitelist_not_contains` | string | No |  |
| `ip_whitelist_not_ends_with` | string | No |  |
| `ip_whitelist_not_in` | string[] | No |  |
| `ip_whitelist_not_starts_with` | string | No |  |
| `ip_whitelist_starts_with` | string | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
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
| `prioritized` | boolean | No |  |
| `prioritized_not` | boolean | No |  |
| `replica_num` | integer (int32) | No |  |
| `replica_num_gt` | integer (int32) | No |  |
| `replica_num_gte` | integer (int32) | No |  |
| `replica_num_in` | integer[] | No |  |
| `replica_num_lt` | integer (int32) | No |  |
| `replica_num_lte` | integer (int32) | No |  |
| `replica_num_not` | integer (int32) | No |  |
| `replica_num_not_in` | integer[] | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_in` | Array of [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_not` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_not_in` | Array of [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `thin_provision` | boolean | No |  |
| `thin_provision_not` | boolean | No |  |

