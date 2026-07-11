# NestedFrozenDisks

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `boot` | integer (int32) | Yes |  |
| `bus` | [Bus](../Bus/Bus.md) | Yes |  |
| `elf_image_local_id` | string | Yes |  |
| `index` | integer (int32) | Yes |  |
| `path` | string | Yes |  |
| `size` | integer (int64) | Yes |  |
| `storage_policy_uuid` | string | Yes |  |
| `svt_image_local_id` | string | Yes |  |
| `type` | [VmDiskType](../Vm/VmDiskType.md) | Yes |  |
| `vm_volume_local_id` | string | Yes |  |
| `disabled` | boolean | No |  |
| `disk_name` | string | No |  |
| `image_name` | string | No |  |
| `key` | integer (int32) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | any | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | any | No |  |
| `resident_in_cache` | boolean | No |  |
| `snapshot_local_id` | string | No |  |
| `vm_volume_snapshot_uuid` | string | No |  |
| `vm_volume_template_uuid` | string | No |  |

