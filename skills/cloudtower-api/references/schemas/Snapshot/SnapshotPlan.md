# SnapshotPlan

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `auto_delete_num` | integer (int32) | Yes |  |
| `auto_execute_num` | integer (int32) | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `execute_intervals` | integer[] | Yes |  |
| `execute_plan_type` | [SnapshotPlanExecuteType](../Snapshot/SnapshotPlanExecuteType.md) | Yes |  |
| `healthy` | boolean | Yes |  |
| `id` | string | Yes |  |
| `last_execute_status` | [SnapshotPlanExecuteStatus](../Snapshot/SnapshotPlanExecuteStatus.md) | Yes |  |
| `local_id` | string | Yes |  |
| `logical_size_bytes` | integer (int64) | Yes |  |
| `manual_delete_num` | integer (int32) | Yes |  |
| `manual_execute_num` | integer (int32) | Yes |  |
| `mirror` | boolean | Yes |  |
| `name` | string | Yes |  |
| `object_num` | integer (int32) | Yes |  |
| `physical_size_bytes` | integer (int64) | Yes |  |
| `remain_snapshot_num` | integer (int32) | Yes |  |
| `snapshot_group_num` | integer (int32) | Yes |  |
| `start_time` | string | Yes |  |
| `status` | [SnapshotPlanStatus](../Snapshot/SnapshotPlanStatus.md) | Yes |  |
| `end_time` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `exec_h_m` | object | No |  |
| `execution_tasks` | Array of [NestedSnapshotPlanTask](../Nested/NestedSnapshotPlanTask.md) | No |  |
| `last_execute_end_time` | string | No |  |
| `last_execute_time` | string | No |  |
| `next_execute_time` | string | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |

## Nested Fields

### `exec_h_m`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


