# SnapshotPlanUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `where` | [SnapshotPlanWhereInput](../Snapshot/SnapshotPlanWhereInput.md) | Yes |  |
| `data` | object | No |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_ids` | string[] | No |  |
| `execute_intervals` | integer[] | No |  |
| `execute_plan_type` | [SnapshotPlanExecuteType](../Snapshot/SnapshotPlanExecuteType.md) | No |  |
| `exec_h_m` | string | No |  |
| `end_time` | string | No |  |
| `remain_snapshot_num` | integer (int32) | No |  |
| `name` | string | No |  |

