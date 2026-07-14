# GlobalAlertRule

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `boolean` | boolean | Yes |  |
| `cause` | string | Yes |  |
| `default_thresholds` | Array of [NestedThresholds](../Nested/NestedThresholds.md) | Yes |  |
| `disabled` | boolean | Yes |  |
| `id` | string | Yes |  |
| `impact` | string | Yes |  |
| `message` | string | Yes |  |
| `name` | string | Yes |  |
| `operator` | string | Yes |  |
| `solution` | string | Yes |  |
| `thresholds` | Array of [NestedThresholds](../Nested/NestedThresholds.md) | Yes |  |
| `unit` | [AlertRuleUnit](../Alert/AlertRuleUnit.md) | Yes |  |
| `alert_rules` | Array of [NestedAlertRule](../Nested/NestedAlertRule.md) | No |  |
| `object` | [AlertRuleObject](../Alert/AlertRuleObject.md) | No |  |

