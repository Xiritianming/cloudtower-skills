# Alert

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cause` | string | Yes |  |
| `ended` | boolean | Yes |  |
| `id` | string | Yes |  |
| `impact` | string | Yes |  |
| `labels` | object | Yes |  |
| `local_create_time` | string | Yes |  |
| `local_end_time` | string | Yes |  |
| `local_id` | string | Yes |  |
| `local_start_time` | string | Yes |  |
| `local_update_time` | string | Yes |  |
| `message` | string | Yes |  |
| `severity` | string | Yes |  |
| `solution` | string | Yes |  |
| `threshold` | number (double) | Yes |  |
| `value` | number (double) | Yes |  |
| `alert_rule` | [NestedAlertRule](../Nested/NestedAlertRule.md) | No |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `create_time` | string | No |  |
| `disk` | [NestedDisk](../Nested/NestedDisk.md) | No |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |

## Nested Fields

### `labels`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


