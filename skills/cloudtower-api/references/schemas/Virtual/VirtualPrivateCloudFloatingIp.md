# VirtualPrivateCloudFloatingIp

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | Yes |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `external_ip` | string | No |  |
| `external_ips` | Array of [NestedVpcGatewaysCommonExternalIpsType](../Nested/NestedVpcGatewaysCommonExternalIpsType.md) | No |  |
| `external_subnet` | [NestedVirtualPrivateCloudExternalSubnet](../Nested/NestedVirtualPrivateCloudExternalSubnet.md) | No |  |
| `external_subnet_group` | [NestedVirtualPrivateCloudExternalSubnetGroup](../Nested/NestedVirtualPrivateCloudExternalSubnetGroup.md) | No |  |

