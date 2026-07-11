# GetZoneMetricInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `range` | string | Yes |  |
| `type` | enum: primary-to-secondary, secondary-to-primary | Yes |  |
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | Yes |  |
| `metrics` | string[] | Yes |  |

