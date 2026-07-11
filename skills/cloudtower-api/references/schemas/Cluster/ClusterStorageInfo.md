# ClusterStorageInfo

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | [ClusterType](../Cluster/ClusterType.md) | Yes |  |
| `name` | string | Yes |  |
| `id` | string | Yes |  |
| `allocable_storage_capacity` | [AllocatableStorageCapacity](../Allocatable/AllocatableStorageCapacity.md) | No |  |
| `free_data_space` | integer (int64) | No |  |
| `failure_data_space` | integer (int64) | No |  |
| `used_data_space` | integer (int64) | No |  |
| `total_data_capacity` | integer (int64) | No |  |
| `storage_cluster` | Array of [ClusterStorageInfo](../Cluster/ClusterStorageInfo.md) | No |  |
| `stretch` | boolean | No |  |

