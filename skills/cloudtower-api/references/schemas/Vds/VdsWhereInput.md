# VdsWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `NOT` | Array of [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `OR` | Array of [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `bond_mode` | string | No |  |
| `bond_mode_contains` | string | No |  |
| `bond_mode_ends_with` | string | No |  |
| `bond_mode_gt` | string | No |  |
| `bond_mode_gte` | string | No |  |
| `bond_mode_in` | string[] | No |  |
| `bond_mode_lt` | string | No |  |
| `bond_mode_lte` | string | No |  |
| `bond_mode_not` | string | No |  |
| `bond_mode_not_contains` | string | No |  |
| `bond_mode_not_ends_with` | string | No |  |
| `bond_mode_not_in` | string[] | No |  |
| `bond_mode_not_starts_with` | string | No |  |
| `bond_mode_starts_with` | string | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `everoute_cluster` | [EverouteClusterWhereInput](../Everoute/EverouteClusterWhereInput.md) | No |  |
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
| `internal` | boolean | No |  |
| `internal_not` | boolean | No |  |
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
| `nics_every` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `nics_none` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `nics_some` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `ovsbr_name` | string | No |  |
| `ovsbr_name_contains` | string | No |  |
| `ovsbr_name_ends_with` | string | No |  |
| `ovsbr_name_gt` | string | No |  |
| `ovsbr_name_gte` | string | No |  |
| `ovsbr_name_in` | string[] | No |  |
| `ovsbr_name_lt` | string | No |  |
| `ovsbr_name_lte` | string | No |  |
| `ovsbr_name_not` | string | No |  |
| `ovsbr_name_not_contains` | string | No |  |
| `ovsbr_name_not_ends_with` | string | No |  |
| `ovsbr_name_not_in` | string[] | No |  |
| `ovsbr_name_not_starts_with` | string | No |  |
| `ovsbr_name_starts_with` | string | No |  |
| `type` | [NetworkType](../Network/NetworkType.md) | No |  |
| `type_in` | Array of [NetworkType](../Network/NetworkType.md) | No |  |
| `type_not` | [NetworkType](../Network/NetworkType.md) | No |  |
| `type_not_in` | Array of [NetworkType](../Network/NetworkType.md) | No |  |
| `vlans_every` | [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `vlans_none` | [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `vlans_num` | integer (int32) | No |  |
| `vlans_num_gt` | integer (int32) | No |  |
| `vlans_num_gte` | integer (int32) | No |  |
| `vlans_num_in` | integer[] | No |  |
| `vlans_num_lt` | integer (int32) | No |  |
| `vlans_num_lte` | integer (int32) | No |  |
| `vlans_num_not` | integer (int32) | No |  |
| `vlans_num_not_in` | integer[] | No |  |
| `vlans_some` | [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `work_mode` | string | No |  |
| `work_mode_contains` | string | No |  |
| `work_mode_ends_with` | string | No |  |
| `work_mode_gt` | string | No |  |
| `work_mode_gte` | string | No |  |
| `work_mode_in` | string[] | No |  |
| `work_mode_lt` | string | No |  |
| `work_mode_lte` | string | No |  |
| `work_mode_not` | string | No |  |
| `work_mode_not_contains` | string | No |  |
| `work_mode_not_ends_with` | string | No |  |
| `work_mode_not_in` | string[] | No |  |
| `work_mode_not_starts_with` | string | No |  |
| `work_mode_starts_with` | string | No |  |

