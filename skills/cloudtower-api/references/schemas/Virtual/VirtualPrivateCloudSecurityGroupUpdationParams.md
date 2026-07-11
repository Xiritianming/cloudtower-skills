# VirtualPrivateCloudSecurityGroupUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_ids` | string[] | No |  |
| `label_groups` | Array of [LabelGroup](../Label/LabelGroup.md) | No |  |
| `description` | string | No |  |
| `name` | string | No |  |

