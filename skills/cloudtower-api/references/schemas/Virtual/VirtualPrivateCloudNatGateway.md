# VirtualPrivateCloudNatGateway

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | Yes |  |
| `dnat_rules` | Array of [NestedVpcDnatRuleType](../Nested/NestedVpcDnatRuleType.md) | No |  |
| `enable_dnat` | boolean | No |  |
| `enable_snat` | boolean | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `external_ip` | string | No |  |
| `external_ips` | Array of [NestedVpcGatewaysCommonExternalIpsType](../Nested/NestedVpcGatewaysCommonExternalIpsType.md) | No |  |
| `external_subnet` | [NestedVirtualPrivateCloudExternalSubnet](../Nested/NestedVirtualPrivateCloudExternalSubnet.md) | No |  |
| `external_subnet_group` | [NestedVirtualPrivateCloudExternalSubnetGroup](../Nested/NestedVirtualPrivateCloudExternalSubnetGroup.md) | No |  |

