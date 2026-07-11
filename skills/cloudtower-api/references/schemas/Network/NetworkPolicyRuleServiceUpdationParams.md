# NetworkPolicyRuleServiceUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [NetworkPolicyRuleServiceWhereInput](../Network/NetworkPolicyRuleServiceWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `members` | Array of [NetworkPolicyRuleServiceMemberParams](../Network/NetworkPolicyRuleServiceMemberParams.md) | No |  |
| `description` | string | No |  |
| `name` | string | No |  |

