# BrickTopoUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [BrickTopoWhereInput](../Brick/BrickTopoWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tag_position_in_brick` | Array of [NestedTagPosition](../Nested/NestedTagPosition.md) | No |  |
| `node_topoes` | [NodeTopoWhereInput](../Node/NodeTopoWhereInput.md) | No |  |
| `capacity` | [NestedCapacity](../Nested/NestedCapacity.md) | No |  |
| `height` | integer (int32) | No |  |
| `name` | string | No |  |
| `position` | integer (int32) | No |  |

