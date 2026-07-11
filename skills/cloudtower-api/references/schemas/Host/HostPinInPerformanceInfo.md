# HostPinInPerformanceInfo

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes |  |
| `id` | string | Yes |  |
| `disk_pools` | Array of [DiskPoolPinInPerformanceInfo](../Disk/DiskPoolPinInPerformanceInfo.md) | No |  |
| `allocated_prioritized_space` | integer (int64) | No |  |
| `planned_prioritized_space` | integer (int64) | No |  |
| `allocated_prioritized_space_usage` | number (double) | No |  |
| `prio_space_percentage` | number (double) | No |  |
| `with_faster_ssd_as_cache` | boolean | No |  |

