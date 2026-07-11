# VmUpdateNicParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VmWhereInput](../Vm/VmWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `nic_index` | integer (int32) | Yes |  |
| `vpc_nic` | [UpdateVpcNicPayloads](../Update/UpdateVpcNicPayloads.md) | No |  |
| `subnet_mask` | string | No |  |
| `gateway` | string | No |  |
| `ip_address` | string | No |  |
| `nic_id` | string | No |  |
| `connect_vlan_id` | string | No |  |
| `mirror` | boolean | No |  |
| `model` | [VmNicModel](../Vm/VmNicModel.md) | No |  |
| `enabled` | boolean | No |  |
| `mac_address` | string | No |  |

