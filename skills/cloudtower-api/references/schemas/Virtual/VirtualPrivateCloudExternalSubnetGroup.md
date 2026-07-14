# VirtualPrivateCloudExternalSubnetGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `edge_gateway_group` | [NestedVirtualPrivateCloudEdgeGatewayGroup](../Nested/NestedVirtualPrivateCloudEdgeGatewayGroup.md) | Yes |  |
| `exclusive` | boolean | Yes |  |
| `external_subnets_spec` | Array of [NestedVirtualPrivateCloudExternalSubnetGroupExternalSubnetsSpec](../Nested/NestedVirtualPrivateCloudExternalSubnetGroupExternalSubnetsSpec.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `shared_in_edge_gateway_group` | boolean | Yes |  |
| `description` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `floating_ips` | Array of [NestedVirtualPrivateCloudFloatingIp](../Nested/NestedVirtualPrivateCloudFloatingIp.md) | No |  |
| `nat_gateways` | Array of [NestedVirtualPrivateCloudNatGateway](../Nested/NestedVirtualPrivateCloudNatGateway.md) | No |  |
| `router_gateways` | Array of [NestedVirtualPrivateCloudRouterGateway](../Nested/NestedVirtualPrivateCloudRouterGateway.md) | No |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | No |  |

