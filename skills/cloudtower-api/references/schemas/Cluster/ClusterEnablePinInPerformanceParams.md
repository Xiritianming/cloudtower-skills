# ClusterEnablePinInPerformanceParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `hosts` | Array of [ClusterEnablePinInPerformanceHostType](../Cluster/ClusterEnablePinInPerformanceHostType.md) | Yes |  |
| `cluster_default_prio_percentage` | number (double) | Yes |  |

