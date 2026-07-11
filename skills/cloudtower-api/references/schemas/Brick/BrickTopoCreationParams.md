# BrickTopoCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster_id` | string | Yes |  |
| `height` | integer (int32) | Yes |  |
| `name` | string | Yes |  |
| `position` | integer (int32) | Yes |  |
| `tag_position_in_brick` | Array of [NestedTagPosition](../Nested/NestedTagPosition.md) | No |  |
| `node_topoes` | [NodeTopoWhereInput](../Node/NodeTopoWhereInput.md) | No |  |
| `rack_topo_id` | string | No |  |
| `capacity` | [NestedCapacity](../Nested/NestedCapacity.md) | No |  |

