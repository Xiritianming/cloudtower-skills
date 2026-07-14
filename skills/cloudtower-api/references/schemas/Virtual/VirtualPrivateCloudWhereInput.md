# VirtualPrivateCloudWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |
| `NOT` | Array of [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |
| `OR` | Array of [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |
| `associate_external_subnet_num` | integer (int32) | No |  |
| `associate_external_subnet_num_gt` | integer (int32) | No |  |
| `associate_external_subnet_num_gte` | integer (int32) | No |  |
| `associate_external_subnet_num_in` | integer[] | No |  |
| `associate_external_subnet_num_lt` | integer (int32) | No |  |
| `associate_external_subnet_num_lte` | integer (int32) | No |  |
| `associate_external_subnet_num_not` | integer (int32) | No |  |
| `associate_external_subnet_num_not_in` | integer[] | No |  |
| `description` | string | No |  |
| `description_contains` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_gt` | string | No |  |
| `description_gte` | string | No |  |
| `description_in` | string[] | No |  |
| `description_lt` | string | No |  |
| `description_lte` | string | No |  |
| `description_not` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_starts_with` | string | No |  |
| `description_starts_with` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
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
| `isolation_policies_every` | [VirtualPrivateCloudIsolationPolicyWhereInput](../Virtual/VirtualPrivateCloudIsolationPolicyWhereInput.md) | No |  |
| `isolation_policies_none` | [VirtualPrivateCloudIsolationPolicyWhereInput](../Virtual/VirtualPrivateCloudIsolationPolicyWhereInput.md) | No |  |
| `isolation_policies_some` | [VirtualPrivateCloudIsolationPolicyWhereInput](../Virtual/VirtualPrivateCloudIsolationPolicyWhereInput.md) | No |  |
| `local_id` | string | No |  |
| `local_id_contains` | string | No |  |
| `local_id_ends_with` | string | No |  |
| `local_id_gt` | string | No |  |
| `local_id_gte` | string | No |  |
| `local_id_in` | string[] | No |  |
| `local_id_lt` | string | No |  |
| `local_id_lte` | string | No |  |
| `local_id_not` | string | No |  |
| `local_id_not_contains` | string | No |  |
| `local_id_not_ends_with` | string | No |  |
| `local_id_not_in` | string[] | No |  |
| `local_id_not_starts_with` | string | No |  |
| `local_id_starts_with` | string | No |  |
| `mtu` | integer (int32) | No |  |
| `mtu_gt` | integer (int32) | No |  |
| `mtu_gte` | integer (int32) | No |  |
| `mtu_in` | integer[] | No |  |
| `mtu_lt` | integer (int32) | No |  |
| `mtu_lte` | integer (int32) | No |  |
| `mtu_not` | integer (int32) | No |  |
| `mtu_not_in` | integer[] | No |  |
| `name` | string | No |  |
| `name_contains` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_gt` | string | No |  |
| `name_gte` | string | No |  |
| `name_in` | string[] | No |  |
| `name_lt` | string | No |  |
| `name_lte` | string | No |  |
| `name_not` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_starts_with` | string | No |  |
| `name_starts_with` | string | No |  |
| `route_tables_every` | [VirtualPrivateCloudRouteTableWhereInput](../Virtual/VirtualPrivateCloudRouteTableWhereInput.md) | No |  |
| `route_tables_none` | [VirtualPrivateCloudRouteTableWhereInput](../Virtual/VirtualPrivateCloudRouteTableWhereInput.md) | No |  |
| `route_tables_some` | [VirtualPrivateCloudRouteTableWhereInput](../Virtual/VirtualPrivateCloudRouteTableWhereInput.md) | No |  |
| `security_groups_every` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | No |  |
| `security_groups_none` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | No |  |
| `security_groups_some` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | No |  |
| `security_policies_every` | [VirtualPrivateCloudSecurityPolicyWhereInput](../Virtual/VirtualPrivateCloudSecurityPolicyWhereInput.md) | No |  |
| `security_policies_none` | [VirtualPrivateCloudSecurityPolicyWhereInput](../Virtual/VirtualPrivateCloudSecurityPolicyWhereInput.md) | No |  |
| `security_policies_some` | [VirtualPrivateCloudSecurityPolicyWhereInput](../Virtual/VirtualPrivateCloudSecurityPolicyWhereInput.md) | No |  |
| `subnets_every` | [VirtualPrivateCloudSubnetWhereInput](../Virtual/VirtualPrivateCloudSubnetWhereInput.md) | No |  |
| `subnets_none` | [VirtualPrivateCloudSubnetWhereInput](../Virtual/VirtualPrivateCloudSubnetWhereInput.md) | No |  |
| `subnets_some` | [VirtualPrivateCloudSubnetWhereInput](../Virtual/VirtualPrivateCloudSubnetWhereInput.md) | No |  |
| `vpc_service` | [VirtualPrivateCloudServiceWhereInput](../Virtual/VirtualPrivateCloudServiceWhereInput.md) | No |  |

