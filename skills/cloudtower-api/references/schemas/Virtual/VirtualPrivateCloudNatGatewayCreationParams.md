# VirtualPrivateCloudNatGatewayCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enable_dnat` | boolean | Yes |  |
| `enable_snat` | boolean | Yes |  |
| `vpc_id` | string | Yes |  |
| `name` | string | Yes |  |
| `external_ips` | Array of [VirtualPrivateCloudExternalIpsParams](../Virtual/VirtualPrivateCloudExternalIpsParams.md) | No |  |
| `external_ip` | string | No |  |
| `external_subnet_group_id` | string | No |  |
| `external_subnet_id` | string | No |  |
| `dnat_rules` | Array of [VirtualPrivateCloudDnatRuleParams](../Virtual/VirtualPrivateCloudDnatRuleParams.md) | No |  |

