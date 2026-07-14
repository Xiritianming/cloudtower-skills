# SnapshotGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `deleted` | boolean | Yes |  |
| `id` | string | Yes |  |
| `keep` | boolean | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `logical_size_bytes` | integer (int64) | Yes |  |
| `name` | string | Yes |  |
| `object_num` | integer (int32) | Yes |  |
| `snapshotPlanTask` | [NestedSnapshotPlanTask](../Nested/NestedSnapshotPlanTask.md) | Yes |  |
| `vm_info` | Array of [NestedSnapshotGroupVmInfo](../Nested/NestedSnapshotGroupVmInfo.md) | Yes |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `estimated_recycling_time` | string | No |  |
| `internal` | boolean | No |  |
| `vm_snapshots` | Array of [NestedVmSnapshot](../Nested/NestedVmSnapshot.md) | No |  |

