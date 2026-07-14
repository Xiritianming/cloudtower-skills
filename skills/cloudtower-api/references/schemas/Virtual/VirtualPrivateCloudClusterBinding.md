# VirtualPrivateCloudClusterBinding

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `vds` | [NestedVds](../Nested/NestedVds.md) | Yes |  |
| `vlan_id` | integer (int32) | Yes |  |
| `vpc_service` | [NestedVirtualPrivateCloudService](../Nested/NestedVirtualPrivateCloudService.md) | Yes |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `mtu` | integer (int32) | No |  |

