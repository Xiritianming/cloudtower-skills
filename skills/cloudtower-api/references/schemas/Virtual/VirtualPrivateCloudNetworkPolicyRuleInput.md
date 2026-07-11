# VirtualPrivateCloudNetworkPolicyRuleInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | [VirtualPrivateCloudNetworkPolicyRuleType](../Virtual/VirtualPrivateCloudNetworkPolicyRuleType.md) | Yes |  |
| `selector_ids` | string[] | No |  |
| `security_group_id` | string | No |  |
| `ports` | Array of [VirtualPrivateCloudNetworkPolicyRulePortInput](../Virtual/VirtualPrivateCloudNetworkPolicyRulePortInput.md) | No |  |
| `ip_block` | string | No |  |
| `except_ip_block` | string[] | No |  |

