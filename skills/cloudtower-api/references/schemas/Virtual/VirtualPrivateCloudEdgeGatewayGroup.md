# VirtualPrivateCloudEdgeGatewayGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `active_edge_gateway_ids` | string[] | Yes |  |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `vpc_service` | [NestedVirtualPrivateCloudService](../Nested/NestedVirtualPrivateCloudService.md) | Yes |  |
| `description` | string | No |  |
| `edge_gateways` | Array of [NestedVirtualPrivateCloudEdgeGateway](../Nested/NestedVirtualPrivateCloudEdgeGateway.md) | No |  |
| `entityAsyncStatus` | any | No |  |
| `primary_edge_gateway_id` | string | No |  |

