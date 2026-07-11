# ElfDataStore

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `external_use` | boolean | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `ip_whitelist` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `replica_num` | integer (int32) | Yes |  |
| `thin_provision` | boolean | Yes |  |
| `type` | [ElfDataStoreType](../Elf/ElfDataStoreType.md) | Yes |  |
| `iscsi_target` | any | No |  |
| `nfs_export` | any | No |  |
| `nvmf_subsystem` | any | No |  |

