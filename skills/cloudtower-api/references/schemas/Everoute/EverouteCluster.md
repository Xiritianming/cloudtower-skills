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
| `controller_template` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `global_whitelist` | any | No |  |
| `installed` | boolean | No |  |
| `load_balancer_service` | any | No |  |
| `phase` | any | No |  |
| `status` | any | No |  |
| `vpc_service` | any | No |  |

