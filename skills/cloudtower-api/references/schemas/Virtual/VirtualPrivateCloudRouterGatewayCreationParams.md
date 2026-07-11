# VirtualPrivateCloudRouterGatewayCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rules` | Array of [VirtualPrivateCloudRouterGatewayRuleInputType](../Virtual/VirtualPrivateCloudRouterGatewayRuleInputType.md) | Yes |  |
| `associated_subnets_ids` | string[] | Yes |  |
| `vpc_id` | string | Yes |  |
| `name` | string | Yes |  |
| `external_ips` | Array of [VirtualPrivateCloudExternalIpsParams](../Virtual/VirtualPrivateCloudExternalIpsParams.md) | No |  |
| `external_subnet_group_id` | string | No |  |
| `external_ip` | string | No |  |
| `external_subnet_id` | string | No |  |

