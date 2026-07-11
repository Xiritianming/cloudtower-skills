# VmUpdateNicAdvanceInfoParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mirror` | boolean | No |  |
| `enabled` | boolean | No |  |
| `mac_address` | string | No |  |
| `nic_id` | string | No |  |
| `connect_vlan_id` | string | No |  |

