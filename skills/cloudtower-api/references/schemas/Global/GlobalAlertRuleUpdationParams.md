# GlobalAlertRuleUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [GlobalAlertRuleWhereInput](../Global/GlobalAlertRuleWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `thresholds` | Array of [AlertRuleThresholds](../Alert/AlertRuleThresholds.md) | No |  |
| `disabled` | boolean | No |  |

