# LoadBalancerInstanceWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [LoadBalancerInstanceWhereInput](../Load/LoadBalancerInstanceWhereInput.md) | No |  |
| `NOT` | Array of [LoadBalancerInstanceWhereInput](../Load/LoadBalancerInstanceWhereInput.md) | No |  |
| `OR` | Array of [LoadBalancerInstanceWhereInput](../Load/LoadBalancerInstanceWhereInput.md) | No |  |
| `createdAt` | string | No |  |
| `createdAt_gt` | string | No |  |
| `createdAt_gte` | string | No |  |
| `createdAt_in` | string[] | No |  |
| `createdAt_lt` | string | No |  |
| `createdAt_lte` | string | No |  |
| `createdAt_not` | string | No |  |
| `createdAt_not_in` | string[] | No |  |
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
| `load_balancer_service` | [LoadBalancerServiceWhereInput](../Load/LoadBalancerServiceWhereInput.md) | No |  |
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
| `phase` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_in` | Array of [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_not` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_not_in` | Array of [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `primary_in_load_balancer_group` | [LoadBalancerInstanceGroupWhereInput](../Load/LoadBalancerInstanceGroupWhereInput.md) | No |  |
| `secondary_in_load_balancer_group` | [LoadBalancerInstanceGroupWhereInput](../Load/LoadBalancerInstanceGroupWhereInput.md) | No |  |
| `vm_instances_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_instances_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_instances_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vnet_bonds_every` | [VnetBondWhereInput](../Vnet/VnetBondWhereInput.md) | No |  |
| `vnet_bonds_none` | [VnetBondWhereInput](../Vnet/VnetBondWhereInput.md) | No |  |
| `vnet_bonds_some` | [VnetBondWhereInput](../Vnet/VnetBondWhereInput.md) | No |  |

