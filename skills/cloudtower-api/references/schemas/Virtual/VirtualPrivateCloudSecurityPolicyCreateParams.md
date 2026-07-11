# VirtualPrivateCloudSecurityPolicyCreateParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `apply_to` | Array of [VirtualPrivateCloudSecurityPolicyApplyInput](../Virtual/VirtualPrivateCloudSecurityPolicyApplyInput.md) | Yes |  |
| `vpc_id` | string | Yes |  |
| `name` | string | Yes |  |
| `egress` | Array of [VirtualPrivateCloudNetworkPolicyRuleInput](../Virtual/VirtualPrivateCloudNetworkPolicyRuleInput.md) | No |  |
| `ingress` | Array of [VirtualPrivateCloudNetworkPolicyRuleInput](../Virtual/VirtualPrivateCloudNetworkPolicyRuleInput.md) | No |  |
| `policy_mode` | [VirtualPrivateCloudSecurityPolicyMode](../Virtual/VirtualPrivateCloudSecurityPolicyMode.md) | No |  |
| `description` | string | No |  |

