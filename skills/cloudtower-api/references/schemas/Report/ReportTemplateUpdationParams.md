# ReportTemplateUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [ReportTemplateWhereInput](../Report/ReportTemplateWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `resource_meta` | Array of [ResourceMeta](../Resource/ResourceMeta.md) | No |  |
| `execute_plan` | Array of [ExecutePlan](../Execute/ExecutePlan.md) | No |  |
| `description` | string | No |  |
| `name` | string | No |  |

