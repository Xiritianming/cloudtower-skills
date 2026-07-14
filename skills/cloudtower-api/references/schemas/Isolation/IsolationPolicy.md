# IsolationPolicy

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `everoute_cluster` | [NestedEverouteCluster](../Nested/NestedEverouteCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `mode` | [IsolationMode](../Isolation/IsolationMode.md) | Yes |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | Yes |  |
| `egress` | Array of [NestedNetworkPolicyRule](../Nested/NestedNetworkPolicyRule.md) | No |  |
| `ingress` | Array of [NestedNetworkPolicyRule](../Nested/NestedNetworkPolicyRule.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `statistics` | [NestedSecurityPolicyStatistics](../Nested/NestedSecurityPolicyStatistics.md) | No |  |

