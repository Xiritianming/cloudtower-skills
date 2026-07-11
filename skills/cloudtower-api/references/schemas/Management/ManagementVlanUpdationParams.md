# ManagementVlanUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VlanWhereInput](../Vlan/VlanWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `extra_ip` | Array of [ExtraIp](../Extra/ExtraIp.md) | No |  |
| `subnetmask` | string | No |  |
| `gateway_ip` | string | No |  |
| `vlan_id` | [VlanId](../Vlan/VlanId.md) | No |  |

