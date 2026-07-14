# VirtualPrivateCloudSubnet

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cidr` | string | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `route_table` | [NestedVirtualPrivateCloudRouteTable](../Nested/NestedVirtualPrivateCloudRouteTable.md) | Yes |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | Yes |  |
| `description` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `gateway` | string | No |  |
| `ip_pools` | Array of [NestedVpcSubnetIpPooType](../Nested/NestedVpcSubnetIpPooType.md) | No |  |
| `total_ip_count` | integer (int32) | No |  |
| `unused_ip_count` | integer (int32) | No |  |

