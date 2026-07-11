# SecurityPolicyCreateParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `everoute_cluster_id` | string | Yes |  |
| `name` | string | Yes |  |
| `is_blocklist` | boolean | No |  |
| `ingress` | Array of [SecurityPolicyIngressEgressInput](../Security/SecurityPolicyIngressEgressInput.md) | No |  |
| `egress` | Array of [SecurityPolicyIngressEgressInput](../Security/SecurityPolicyIngressEgressInput.md) | No |  |
| `apply_to` | Array of [SecurityPolicyApplyToInput](../Security/SecurityPolicyApplyToInput.md) | No |  |
| `policy_mode` | [PolicyMode](../Policy/PolicyMode.md) | No |  |
| `description` | string | No |  |

