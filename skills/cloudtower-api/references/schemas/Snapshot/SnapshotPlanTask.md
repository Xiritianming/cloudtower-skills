# SnapshotPlanTask

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `snapshotPlan` | [NestedSnapshotPlan](../Nested/NestedSnapshotPlan.md) | Yes |  |
| `start_time` | string | Yes |  |
| `status` | [SnapshotPlanExecuteStatus](../Snapshot/SnapshotPlanExecuteStatus.md) | Yes |  |
| `type` | [SnapshotPlanTaskType](../Snapshot/SnapshotPlanTaskType.md) | Yes |  |
| `end_time` | string | No |  |
| `entityAsyncStatus` | any | No |  |
| `internal` | boolean | No |  |
| `snapshotGroup` | any | No |  |

