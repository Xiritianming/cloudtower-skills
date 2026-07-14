# BrickTopo

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `capacity` | [NestedCapacity](../Nested/NestedCapacity.md) | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `height` | integer (int32) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `position` | integer (int32) | Yes |  |
| `cluster_topo` | [NestedClusterTopo](../Nested/NestedClusterTopo.md) | No |  |
| `disk_layout` | [NestedBrickDiskLayout](../Nested/NestedBrickDiskLayout.md) | No |  |
| `model` | string | No |  |
| `node_topoes` | Array of [NestedNodeTopo](../Nested/NestedNodeTopo.md) | No |  |
| `power_layout` | [Direction](../Direction/Direction.md) | No |  |
| `power_position` | [PowerPosition](../Power/PowerPosition.md) | No |  |
| `powers` | Array of [NestedBrickPower](../Nested/NestedBrickPower.md) | No |  |
| `rack_topo` | [NestedRackTopo](../Nested/NestedRackTopo.md) | No |  |
| `tag_position_in_brick` | Array of [NestedTagPosition](../Nested/NestedTagPosition.md) | No |  |

