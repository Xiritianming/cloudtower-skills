# VirtualPrivateCloudRouterGateway

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `rules` | Array of [NestedVpcRouterGatewayRuleType](../Nested/NestedVpcRouterGatewayRuleType.md) | Yes |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | Yes |  |
| `associated_subnets` | Array of [NestedVirtualPrivateCloudSubnet](../Nested/NestedVirtualPrivateCloudSubnet.md) | No |  |
| `entityAsyncStatus` | any | No |  |
| `external_ip` | string | No |  |
| `external_ips` | Array of [NestedVpcGatewaysCommonExternalIpsType](../Nested/NestedVpcGatewaysCommonExternalIpsType.md) | No |  |
| `external_subnet` | any | No |  |
| `external_subnet_group` | any | No |  |
| `nexthop_ip` | string | No |  |

