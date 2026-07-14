# NestedVirtualPrivateCloudNetworkPolicyRule

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | [VirtualPrivateCloudNetworkPolicyRuleType](../Virtual/VirtualPrivateCloudNetworkPolicyRuleType.md) | Yes |  |
| `except_ip_block` | string[] | No |  |
| `ip_block` | string | No |  |
| `ports` | Array of [NestedVirtualPrivateCloudNetworkPolicyRulePort](../Nested/NestedVirtualPrivateCloudNetworkPolicyRulePort.md) | No |  |
| `security_group` | [NestedVirtualPrivateCloudSecurityGroup](../Nested/NestedVirtualPrivateCloudSecurityGroup.md) | No |  |
| `security_group_id` | string | No |  |
| `selector` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `selector_ids` | string[] | No |  |

