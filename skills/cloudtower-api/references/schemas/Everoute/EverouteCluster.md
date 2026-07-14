# EverouteCluster

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `controller_instances` | Array of [NestedEverouteControllerInstance](../Nested/NestedEverouteControllerInstance.md) | Yes |  |
| `global_default_action` | [GlobalPolicyAction](../Global/GlobalPolicyAction.md) | Yes |  |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `version` | string | Yes |  |
| `agent_elf_clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `agent_elf_vdses` | Array of [NestedVds](../Nested/NestedVds.md) | No |  |
| `controller_template` | [NestedEverouteControllerTemplate](../Nested/NestedEverouteControllerTemplate.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `global_whitelist` | [NestedEverouteClusterWhitelist](../Nested/NestedEverouteClusterWhitelist.md) | No |  |
| `installed` | boolean | No |  |
| `load_balancer_service` | [NestedLoadBalancerService](../Nested/NestedLoadBalancerService.md) | No |  |
| `phase` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `status` | [NestedEverouteClusterStatus](../Nested/NestedEverouteClusterStatus.md) | No |  |
| `vpc_service` | [NestedVirtualPrivateCloudService](../Nested/NestedVirtualPrivateCloudService.md) | No |  |

