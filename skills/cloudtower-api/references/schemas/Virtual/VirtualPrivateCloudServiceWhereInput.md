# VirtualPrivateCloudServiceWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VirtualPrivateCloudServiceWhereInput](../Virtual/VirtualPrivateCloudServiceWhereInput.md) | No |  |
| `NOT` | Array of [VirtualPrivateCloudServiceWhereInput](../Virtual/VirtualPrivateCloudServiceWhereInput.md) | No |  |
| `OR` | Array of [VirtualPrivateCloudServiceWhereInput](../Virtual/VirtualPrivateCloudServiceWhereInput.md) | No |  |
| `cluster_bindings_every` | [VirtualPrivateCloudClusterBindingWhereInput](../Virtual/VirtualPrivateCloudClusterBindingWhereInput.md) | No |  |
| `cluster_bindings_none` | [VirtualPrivateCloudClusterBindingWhereInput](../Virtual/VirtualPrivateCloudClusterBindingWhereInput.md) | No |  |
| `cluster_bindings_some` | [VirtualPrivateCloudClusterBindingWhereInput](../Virtual/VirtualPrivateCloudClusterBindingWhereInput.md) | No |  |
| `edge_gateway_groups_every` | [VirtualPrivateCloudEdgeGatewayGroupWhereInput](../Virtual/VirtualPrivateCloudEdgeGatewayGroupWhereInput.md) | No |  |
| `edge_gateway_groups_none` | [VirtualPrivateCloudEdgeGatewayGroupWhereInput](../Virtual/VirtualPrivateCloudEdgeGatewayGroupWhereInput.md) | No |  |
| `edge_gateway_groups_some` | [VirtualPrivateCloudEdgeGatewayGroupWhereInput](../Virtual/VirtualPrivateCloudEdgeGatewayGroupWhereInput.md) | No |  |
| `edge_gateways_every` | [VirtualPrivateCloudEdgeGatewayWhereInput](../Virtual/VirtualPrivateCloudEdgeGatewayWhereInput.md) | No |  |
| `edge_gateways_none` | [VirtualPrivateCloudEdgeGatewayWhereInput](../Virtual/VirtualPrivateCloudEdgeGatewayWhereInput.md) | No |  |
| `edge_gateways_some` | [VirtualPrivateCloudEdgeGatewayWhereInput](../Virtual/VirtualPrivateCloudEdgeGatewayWhereInput.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `everoute_cluster` | [EverouteClusterWhereInput](../Everoute/EverouteClusterWhereInput.md) | No |  |
| `external_subnets_every` | [VirtualPrivateCloudExternalSubnetWhereInput](../Virtual/VirtualPrivateCloudExternalSubnetWhereInput.md) | No |  |
| `external_subnets_none` | [VirtualPrivateCloudExternalSubnetWhereInput](../Virtual/VirtualPrivateCloudExternalSubnetWhereInput.md) | No |  |
| `external_subnets_some` | [VirtualPrivateCloudExternalSubnetWhereInput](../Virtual/VirtualPrivateCloudExternalSubnetWhereInput.md) | No |  |
| `id` | string | No |  |
| `id_contains` | string | No |  |
| `id_ends_with` | string | No |  |
| `id_gt` | string | No |  |
| `id_gte` | string | No |  |
| `id_in` | string[] | No |  |
| `id_lt` | string | No |  |
| `id_lte` | string | No |  |
| `id_not` | string | No |  |
| `id_not_contains` | string | No |  |
| `id_not_ends_with` | string | No |  |
| `id_not_in` | string[] | No |  |
| `id_not_starts_with` | string | No |  |
| `id_starts_with` | string | No |  |
| `internal_cidr` | string | No |  |
| `internal_cidr_contains` | string | No |  |
| `internal_cidr_ends_with` | string | No |  |
| `internal_cidr_gt` | string | No |  |
| `internal_cidr_gte` | string | No |  |
| `internal_cidr_in` | string[] | No |  |
| `internal_cidr_lt` | string | No |  |
| `internal_cidr_lte` | string | No |  |
| `internal_cidr_not` | string | No |  |
| `internal_cidr_not_contains` | string | No |  |
| `internal_cidr_not_ends_with` | string | No |  |
| `internal_cidr_not_in` | string[] | No |  |
| `internal_cidr_not_starts_with` | string | No |  |
| `internal_cidr_starts_with` | string | No |  |
| `phase` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_in` | Array of [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_not` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_not_in` | Array of [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `vpcs_every` | [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |
| `vpcs_none` | [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |
| `vpcs_some` | [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |

