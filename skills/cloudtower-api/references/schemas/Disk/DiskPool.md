# DiskPool

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `chunk_id` | integer (int32) | Yes |  |
| `chunk_ins_id` | integer (int32) | Yes |  |
| `data_space_usage` | number (double) | Yes |  |
| `dirty_cache_space` | integer (int64) | Yes |  |
| `dirty_cache_usage` | number (double) | Yes |  |
| `failure_cache_space` | integer (int64) | Yes |  |
| `failure_data_space` | integer (int64) | Yes |  |
| `hdd_disk_count` | integer (int32) | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `numa_node` | string | Yes |  |
| `nvme_ssd_disk_count` | integer (int32) | Yes |  |
| `perf_allocated_data_space` | integer (int64) | Yes |  |
| `perf_failure_data_space` | integer (int64) | Yes |  |
| `perf_total_data_capacity` | integer (int64) | Yes |  |
| `perf_used_data_space` | integer (int64) | Yes |  |
| `perf_valid_data_space` | integer (int64) | Yes |  |
| `planned_prioritized_space` | integer (int64) | Yes |  |
| `sata_or_sas_ssd_disk_count` | integer (int32) | Yes |  |
| `status` | [DiskPoolStatus](../Disk/DiskPoolStatus.md) | Yes |  |
| `total_cache_capacity` | integer (int64) | Yes |  |
| `total_data_capacity` | integer (int64) | Yes |  |
| `use_state` | [DiskPoolUseState](../Disk/DiskPoolUseState.md) | Yes |  |
| `used_cache_space` | integer (int64) | Yes |  |
| `used_data_space` | integer (int64) | Yes |  |
| `valid_cache_space` | integer (int64) | Yes |  |
| `valid_free_cache_space` | integer (int64) | Yes |  |
| `disks` | Array of [NestedDisk](../Nested/NestedDisk.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `prio_space_percentage` | number (double) | No |  |

