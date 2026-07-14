# NestedNetworkPolicyRule

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | [NetworkPolicyRuleType](../Network/NetworkPolicyRuleType.md) | Yes |  |
| `except_ip_block` | string[] | No |  |
| `ip_block` | string | No |  |
| `ports` | Array of [NestedNetworkPolicyRulePort](../Nested/NestedNetworkPolicyRulePort.md) | No |  |
| `security_group` | [NestedSecurityGroup](../Nested/NestedSecurityGroup.md) | No |  |
| `security_group_id` | string | No |  |
| `selector` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `selector_ids` | string[] | No |  |
| `service_ids` | string[] | No |  |
| `services` | Array of [NestedNetworkPolicyRuleService](../Nested/NestedNetworkPolicyRuleService.md) | No |  |

