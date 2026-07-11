# Vlan

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `network_ids` | string[] | Yes |  |
| `type` | [NetworkType](../Network/NetworkType.md) | Yes |  |
| `vds` | [NestedVds](../Nested/NestedVds.md) | Yes |  |
| `vlan_id` | integer (int32) | Yes |  |
| `entityAsyncStatus` | any | No |  |
| `gateway_ip` | string | No |  |
| `gateway_subnetmask` | string | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `mode_type` | any | No |  |
| `qos_burst` | number (double) | No |  |
| `qos_max_bandwidth` | number (double) | No |  |
| `qos_min_bandwidth` | number (double) | No |  |
| `qos_priority` | integer (int32) | No |  |
| `subnetmask` | string | No |  |
| `vm_nics` | Array of [NestedVmNic](../Nested/NestedVmNic.md) | No |  |

