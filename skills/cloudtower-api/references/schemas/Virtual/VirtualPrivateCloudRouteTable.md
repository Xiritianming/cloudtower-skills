# VirtualPrivateCloudRouteTable

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | Yes |  |
| `default_for_vpc` | boolean | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `routes` | Array of [NestedVirtualPrivateCloudRoute](../Nested/NestedVirtualPrivateCloudRoute.md) | No |  |
| `subnets` | Array of [NestedVirtualPrivateCloudSubnet](../Nested/NestedVirtualPrivateCloudSubnet.md) | No |  |

