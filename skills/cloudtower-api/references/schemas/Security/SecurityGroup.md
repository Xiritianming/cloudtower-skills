# SecurityGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `everoute_cluster` | [NestedEverouteCluster](../Nested/NestedEverouteCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `description` | string | No |  |
| `isolation_policies` | Array of [NestedIsolationPolicy](../Nested/NestedIsolationPolicy.md) | No |  |
| `label_groups` | Array of [NestedLabelGroup](../Nested/NestedLabelGroup.md) | No |  |
| `security_policies` | Array of [NestedSecurityPolicy](../Nested/NestedSecurityPolicy.md) | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |

