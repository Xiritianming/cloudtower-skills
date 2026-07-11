# SecurityPolicy

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `apply_to` | Array of [NestedSecurityPolicyApply](../Nested/NestedSecurityPolicyApply.md) | Yes |  |
| `description` | string | Yes |  |
| `everoute_cluster` | [NestedEverouteCluster](../Nested/NestedEverouteCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `is_blocklist` | boolean | Yes |  |
| `name` | string | Yes |  |
| `egress` | Array of [NestedNetworkPolicyRule](../Nested/NestedNetworkPolicyRule.md) | No |  |
| `ingress` | Array of [NestedNetworkPolicyRule](../Nested/NestedNetworkPolicyRule.md) | No |  |
| `policy_mode` | any | No |  |
| `statistics` | any | No |  |

