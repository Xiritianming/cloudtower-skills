# IsolationPolicyCreateParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mode` | [IsolationMode](../Isolation/IsolationMode.md) | Yes |  |
| `vm_id` | string | Yes |  |
| `everoute_cluster_id` | string | Yes |  |
| `ingress` | Array of [SecurityPolicyIngressEgressInput](../Security/SecurityPolicyIngressEgressInput.md) | No |  |
| `egress` | Array of [SecurityPolicyIngressEgressInput](../Security/SecurityPolicyIngressEgressInput.md) | No |  |

