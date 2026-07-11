# GetTopNMetricInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `metrics` | string[] | Yes |  |
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | Yes |  |
| `type` | enum: top, bottom | Yes |  |
| `n` | integer (int32) | Yes |  |
| `range` | string | Yes |  |

