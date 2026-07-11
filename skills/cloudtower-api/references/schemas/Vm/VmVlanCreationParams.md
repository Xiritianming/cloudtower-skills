# VmVlanCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vds_id` | string | Yes |  |
| `name` | string | Yes |  |
| `qos_burst_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `qos_burst` | integer (int64) | No |  |
| `qos_max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `qos_max_bandwidth` | integer (int64) | No |  |
| `qos_min_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `qos_min_bandwidth` | integer (int64) | No |  |
| `qos_priority` | [Priority](../Priority/Priority.md) | No |  |
| `mode_type` | [VlanModeType](../Vlan/VlanModeType.md) | No |  |
| `network_ids` | string[] | No |  |
| `vlan_id` | [VlanId](../Vlan/VlanId.md) | No |  |

