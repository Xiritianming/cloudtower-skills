# PmemDimm

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `capacity` | integer (int64) | Yes |  |
| `device_locator` | string | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `numa_node` | integer (int32) | Yes |  |
| `part_number` | string | Yes |  |
| `version` | string | Yes |  |
| `disk` | [NestedDisk](../Nested/NestedDisk.md) | No |  |
| `health_status` | [DiskHealthStatus](../Disk/DiskHealthStatus.md) | No |  |
| `local_id` | string | No |  |
| `remaining_life_percent` | integer (int32) | No |  |

