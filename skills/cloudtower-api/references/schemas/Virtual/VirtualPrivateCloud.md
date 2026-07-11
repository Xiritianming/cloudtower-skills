# VirtualPrivateCloud

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `vpc_service` | [NestedVirtualPrivateCloudService](../Nested/NestedVirtualPrivateCloudService.md) | Yes |  |
| `associate_external_subnet_num` | integer (int32) | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | any | No |  |
| `isolation_policies` | Array of [NestedVirtualPrivateCloudIsolationPolicy](../Nested/NestedVirtualPrivateCloudIsolationPolicy.md) | No |  |
| `mtu` | integer (int32) | No |  |
| `route_tables` | Array of [NestedVirtualPrivateCloudRouteTable](../Nested/NestedVirtualPrivateCloudRouteTable.md) | No |  |
| `security_groups` | Array of [NestedVirtualPrivateCloudSecurityGroup](../Nested/NestedVirtualPrivateCloudSecurityGroup.md) | No |  |
| `security_policies` | Array of [NestedVirtualPrivateCloudSecurityPolicy](../Nested/NestedVirtualPrivateCloudSecurityPolicy.md) | No |  |
| `subnets` | Array of [NestedVirtualPrivateCloudSubnet](../Nested/NestedVirtualPrivateCloudSubnet.md) | No |  |

