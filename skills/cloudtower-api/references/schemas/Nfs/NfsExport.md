# NfsExport

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `export_inode_id` | string | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `ip_whitelist` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `replica_num` | integer (int32) | Yes |  |
| `thin_provision` | boolean | Yes |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `encrypt_method` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `inodes` | Array of [NestedNfsInode](../Nested/NestedNfsInode.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `prioritized` | boolean | No |  |
| `resiliency_type` | any | No |  |

