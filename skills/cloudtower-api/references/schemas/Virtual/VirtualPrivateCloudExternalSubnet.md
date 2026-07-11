# VirtualPrivateCloudExternalSubnet

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cidr` | string | Yes |  |
| `exclusive` | boolean | Yes |  |
| `gateway` | string | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `vlan` | [NestedVlan](../Nested/NestedVlan.md) | Yes |  |
| `description` | string | No |  |
| `edge_gateway` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `floating_ip_cidr` | string | No |  |
| `floating_ips` | Array of [NestedVirtualPrivateCloudFloatingIp](../Nested/NestedVirtualPrivateCloudFloatingIp.md) | No |  |
| `nat_gateway_cidr` | string | No |  |
| `nat_gateways` | Array of [NestedVirtualPrivateCloudNatGateway](../Nested/NestedVirtualPrivateCloudNatGateway.md) | No |  |
| `router_gateway_cidr` | string | No |  |
| `router_gateways` | Array of [NestedVirtualPrivateCloudRouterGateway](../Nested/NestedVirtualPrivateCloudRouterGateway.md) | No |  |
| `vpc` | any | No |  |

