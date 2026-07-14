# VirtualPrivateCloudEdgeGateway

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `vpc_service` | [NestedVirtualPrivateCloudService](../Nested/NestedVirtualPrivateCloudService.md) | Yes |  |
| `description` | string | No |  |
| `edge_gateway_group` | [NestedVirtualPrivateCloudEdgeGatewayGroup](../Nested/NestedVirtualPrivateCloudEdgeGatewayGroup.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `status` | [NestedVirtualPrivateCloudEdgeGatewayStatus](../Nested/NestedVirtualPrivateCloudEdgeGatewayStatus.md) | No |  |
| `vdses` | Array of [NestedVds](../Nested/NestedVds.md) | No |  |

