# MigrationVlanUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `where` | [VlanWhereInput](../Vlan/VlanWhereInput.md) | Yes |  |
| `data` | object | No |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `extra_ip` | Array of [ExtraIp](../Extra/ExtraIp.md) | No |  |
| `subnetmask` | string | No |  |
| `gateway_ip` | string | No |  |
| `vlan_id` | [VlanId](../Vlan/VlanId.md) | No |  |

