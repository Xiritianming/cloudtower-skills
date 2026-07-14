# LoadBalancerServiceWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [LoadBalancerServiceWhereInput](../Load/LoadBalancerServiceWhereInput.md) | No |  |
| `NOT` | Array of [LoadBalancerServiceWhereInput](../Load/LoadBalancerServiceWhereInput.md) | No |  |
| `OR` | Array of [LoadBalancerServiceWhereInput](../Load/LoadBalancerServiceWhereInput.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `everoute_cluster` | [EverouteClusterWhereInput](../Everoute/EverouteClusterWhereInput.md) | No |  |
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
| `load_balancer_instance_groups_every` | [LoadBalancerInstanceGroupWhereInput](../Load/LoadBalancerInstanceGroupWhereInput.md) | No |  |
| `load_balancer_instance_groups_none` | [LoadBalancerInstanceGroupWhereInput](../Load/LoadBalancerInstanceGroupWhereInput.md) | No |  |
| `load_balancer_instance_groups_some` | [LoadBalancerInstanceGroupWhereInput](../Load/LoadBalancerInstanceGroupWhereInput.md) | No |  |
| `load_balancer_instances_every` | [LoadBalancerInstanceWhereInput](../Load/LoadBalancerInstanceWhereInput.md) | No |  |
| `load_balancer_instances_none` | [LoadBalancerInstanceWhereInput](../Load/LoadBalancerInstanceWhereInput.md) | No |  |
| `load_balancer_instances_some` | [LoadBalancerInstanceWhereInput](../Load/LoadBalancerInstanceWhereInput.md) | No |  |
| `phase` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_in` | Array of [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_not` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `phase_not_in` | Array of [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `vm_instances_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_instances_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_instances_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vnet_bonds_every` | [VnetBondWhereInput](../Vnet/VnetBondWhereInput.md) | No |  |
| `vnet_bonds_none` | [VnetBondWhereInput](../Vnet/VnetBondWhereInput.md) | No |  |
| `vnet_bonds_some` | [VnetBondWhereInput](../Vnet/VnetBondWhereInput.md) | No |  |

