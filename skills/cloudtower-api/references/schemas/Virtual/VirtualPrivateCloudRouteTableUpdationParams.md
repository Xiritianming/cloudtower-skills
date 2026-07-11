# VirtualPrivateCloudRouteTableUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VirtualPrivateCloudRouteTableWhereInput](../Virtual/VirtualPrivateCloudRouteTableWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `routes` | Array of [VirtualPrivateCloudRouteParams](../Virtual/VirtualPrivateCloudRouteParams.md) | No |  |
| `description` | string | No |  |
| `name` | string | No |  |

