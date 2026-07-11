# Disk

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `firmware` | string | Yes |  |
| `healthy` | boolean | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `model` | string | Yes |  |
| `mounted` | boolean | Yes |  |
| `name` | string | Yes |  |
| `offline` | boolean | Yes |  |
| `partitions` | Array of [NestedPartition](../Nested/NestedPartition.md) | Yes |  |
| `path` | string | Yes |  |
| `serial` | string | Yes |  |
| `size` | integer (int64) | Yes |  |
| `type` | [DiskType](../Disk/DiskType.md) | Yes |  |
| `usage` | [DiskUsage](../Disk/DiskUsage.md) | Yes |  |
| `entityAsyncStatus` | any | No |  |
| `failure_information` | any | No |  |
| `function` | any | No |  |
| `health_status` | any | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `numa_node` | integer (int32) | No |  |
| `persistent_memory_type` | string | No |  |
| `physical_slot_on_brick` | integer (int32) | No |  |
| `pmem_dimms` | Array of [NestedPmemDimm](../Nested/NestedPmemDimm.md) | No |  |
| `recommended_usage` | any | No |  |
| `remaining_life_percent` | integer (int32) | No |  |
| `usage_status` | any | No |  |

