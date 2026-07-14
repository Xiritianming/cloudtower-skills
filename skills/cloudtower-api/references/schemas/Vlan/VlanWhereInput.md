# VlanWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `NOT` | Array of [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `OR` | Array of [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `gateway_ip` | string | No |  |
| `gateway_ip_contains` | string | No |  |
| `gateway_ip_ends_with` | string | No |  |
| `gateway_ip_gt` | string | No |  |
| `gateway_ip_gte` | string | No |  |
| `gateway_ip_in` | string[] | No |  |
| `gateway_ip_lt` | string | No |  |
| `gateway_ip_lte` | string | No |  |
| `gateway_ip_not` | string | No |  |
| `gateway_ip_not_contains` | string | No |  |
| `gateway_ip_not_ends_with` | string | No |  |
| `gateway_ip_not_in` | string[] | No |  |
| `gateway_ip_not_starts_with` | string | No |  |
| `gateway_ip_starts_with` | string | No |  |
| `gateway_subnetmask` | string | No |  |
| `gateway_subnetmask_contains` | string | No |  |
| `gateway_subnetmask_ends_with` | string | No |  |
| `gateway_subnetmask_gt` | string | No |  |
| `gateway_subnetmask_gte` | string | No |  |
| `gateway_subnetmask_in` | string[] | No |  |
| `gateway_subnetmask_lt` | string | No |  |
| `gateway_subnetmask_lte` | string | No |  |
| `gateway_subnetmask_not` | string | No |  |
| `gateway_subnetmask_not_contains` | string | No |  |
| `gateway_subnetmask_not_ends_with` | string | No |  |
| `gateway_subnetmask_not_in` | string[] | No |  |
| `gateway_subnetmask_not_starts_with` | string | No |  |
| `gateway_subnetmask_starts_with` | string | No |  |
| `id` | string | No |  |
| `id_contains` | string | No |  |
| `id_ends_with` | string | No |  |
| `id_gt` | string | No |  |
| `id_gte` | string | No |  |
| `id_in` | string[] | No |  |
| `id_lt` | string | No |  |
| `id_lte` | string | No |  |
| `id_not` | string | No |  |
| `id_not_contains` | string | No |  |
| `id_not_ends_with` | string | No |  |
| `id_not_in` | string[] | No |  |
| `id_not_starts_with` | string | No |  |
| `id_starts_with` | string | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `local_id` | string | No |  |
| `local_id_contains` | string | No |  |
| `local_id_ends_with` | string | No |  |
| `local_id_gt` | string | No |  |
| `local_id_gte` | string | No |  |
| `local_id_in` | string[] | No |  |
| `local_id_lt` | string | No |  |
| `local_id_lte` | string | No |  |
| `local_id_not` | string | No |  |
| `local_id_not_contains` | string | No |  |
| `local_id_not_ends_with` | string | No |  |
| `local_id_not_in` | string[] | No |  |
| `local_id_not_starts_with` | string | No |  |
| `local_id_starts_with` | string | No |  |
| `mode_type` | [VlanModeType](../Vlan/VlanModeType.md) | No |  |
| `mode_type_in` | Array of [VlanModeType](../Vlan/VlanModeType.md) | No |  |
| `mode_type_not` | [VlanModeType](../Vlan/VlanModeType.md) | No |  |
| `mode_type_not_in` | Array of [VlanModeType](../Vlan/VlanModeType.md) | No |  |
| `name` | string | No |  |
| `name_contains` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_gt` | string | No |  |
| `name_gte` | string | No |  |
| `name_in` | string[] | No |  |
| `name_lt` | string | No |  |
| `name_lte` | string | No |  |
| `name_not` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_starts_with` | string | No |  |
| `name_starts_with` | string | No |  |
| `qos_burst` | number (double) | No |  |
| `qos_burst_gt` | number (double) | No |  |
| `qos_burst_gte` | number (double) | No |  |
| `qos_burst_in` | number[] | No |  |
| `qos_burst_lt` | number (double) | No |  |
| `qos_burst_lte` | number (double) | No |  |
| `qos_burst_not` | number (double) | No |  |
| `qos_burst_not_in` | number[] | No |  |
| `qos_max_bandwidth` | number (double) | No |  |
| `qos_max_bandwidth_gt` | number (double) | No |  |
| `qos_max_bandwidth_gte` | number (double) | No |  |
| `qos_max_bandwidth_in` | number[] | No |  |
| `qos_max_bandwidth_lt` | number (double) | No |  |
| `qos_max_bandwidth_lte` | number (double) | No |  |
| `qos_max_bandwidth_not` | number (double) | No |  |
| `qos_max_bandwidth_not_in` | number[] | No |  |
| `qos_min_bandwidth` | number (double) | No |  |
| `qos_min_bandwidth_gt` | number (double) | No |  |
| `qos_min_bandwidth_gte` | number (double) | No |  |
| `qos_min_bandwidth_in` | number[] | No |  |
| `qos_min_bandwidth_lt` | number (double) | No |  |
| `qos_min_bandwidth_lte` | number (double) | No |  |
| `qos_min_bandwidth_not` | number (double) | No |  |
| `qos_min_bandwidth_not_in` | number[] | No |  |
| `qos_priority` | integer (int32) | No |  |
| `qos_priority_gt` | integer (int32) | No |  |
| `qos_priority_gte` | integer (int32) | No |  |
| `qos_priority_in` | integer[] | No |  |
| `qos_priority_lt` | integer (int32) | No |  |
| `qos_priority_lte` | integer (int32) | No |  |
| `qos_priority_not` | integer (int32) | No |  |
| `qos_priority_not_in` | integer[] | No |  |
| `subnetmask` | string | No |  |
| `subnetmask_contains` | string | No |  |
| `subnetmask_ends_with` | string | No |  |
| `subnetmask_gt` | string | No |  |
| `subnetmask_gte` | string | No |  |
| `subnetmask_in` | string[] | No |  |
| `subnetmask_lt` | string | No |  |
| `subnetmask_lte` | string | No |  |
| `subnetmask_not` | string | No |  |
| `subnetmask_not_contains` | string | No |  |
| `subnetmask_not_ends_with` | string | No |  |
| `subnetmask_not_in` | string[] | No |  |
| `subnetmask_not_starts_with` | string | No |  |
| `subnetmask_starts_with` | string | No |  |
| `type` | [NetworkType](../Network/NetworkType.md) | No |  |
| `type_in` | Array of [NetworkType](../Network/NetworkType.md) | No |  |
| `type_not` | [NetworkType](../Network/NetworkType.md) | No |  |
| `type_not_in` | Array of [NetworkType](../Network/NetworkType.md) | No |  |
| `vds` | [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `vlan_id` | integer (int32) | No |  |
| `vlan_id_gt` | integer (int32) | No |  |
| `vlan_id_gte` | integer (int32) | No |  |
| `vlan_id_in` | integer[] | No |  |
| `vlan_id_lt` | integer (int32) | No |  |
| `vlan_id_lte` | integer (int32) | No |  |
| `vlan_id_not` | integer (int32) | No |  |
| `vlan_id_not_in` | integer[] | No |  |
| `vm_nics_every` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vm_nics_none` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vm_nics_some` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |

