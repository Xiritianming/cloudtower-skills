# GraphWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [GraphWhereInput](../Graph/GraphWhereInput.md) | No |  |
| `NOT` | Array of [GraphWhereInput](../Graph/GraphWhereInput.md) | No |  |
| `OR` | Array of [GraphWhereInput](../Graph/GraphWhereInput.md) | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `disks_every` | [DiskWhereInput](../Disk/DiskWhereInput.md) | No |  |
| `disks_none` | [DiskWhereInput](../Disk/DiskWhereInput.md) | No |  |
| `disks_some` | [DiskWhereInput](../Disk/DiskWhereInput.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `hosts_every` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `hosts_none` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `hosts_some` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
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
| `luns_every` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `luns_none` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `luns_some` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `metric_count` | integer (int32) | No |  |
| `metric_count_gt` | integer (int32) | No |  |
| `metric_count_gte` | integer (int32) | No |  |
| `metric_count_in` | integer[] | No |  |
| `metric_count_lt` | integer (int32) | No |  |
| `metric_count_lte` | integer (int32) | No |  |
| `metric_count_not` | integer (int32) | No |  |
| `metric_count_not_in` | integer[] | No |  |
| `metric_name` | string | No |  |
| `metric_name_contains` | string | No |  |
| `metric_name_ends_with` | string | No |  |
| `metric_name_gt` | string | No |  |
| `metric_name_gte` | string | No |  |
| `metric_name_in` | string[] | No |  |
| `metric_name_lt` | string | No |  |
| `metric_name_lte` | string | No |  |
| `metric_name_not` | string | No |  |
| `metric_name_not_contains` | string | No |  |
| `metric_name_not_ends_with` | string | No |  |
| `metric_name_not_in` | string[] | No |  |
| `metric_name_not_starts_with` | string | No |  |
| `metric_name_starts_with` | string | No |  |
| `metric_type` | [MetricType](../Metric/MetricType.md) | No |  |
| `metric_type_in` | Array of [MetricType](../Metric/MetricType.md) | No |  |
| `metric_type_not` | [MetricType](../Metric/MetricType.md) | No |  |
| `metric_type_not_in` | Array of [MetricType](../Metric/MetricType.md) | No |  |
| `namespaces_every` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `namespaces_none` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `namespaces_some` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `network` | [NetworkType](../Network/NetworkType.md) | No |  |
| `network_in` | Array of [NetworkType](../Network/NetworkType.md) | No |  |
| `network_not` | [NetworkType](../Network/NetworkType.md) | No |  |
| `network_not_in` | Array of [NetworkType](../Network/NetworkType.md) | No |  |
| `nics_every` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `nics_none` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `nics_some` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `resource_type` | string | No |  |
| `resource_type_contains` | string | No |  |
| `resource_type_ends_with` | string | No |  |
| `resource_type_gt` | string | No |  |
| `resource_type_gte` | string | No |  |
| `resource_type_in` | string[] | No |  |
| `resource_type_lt` | string | No |  |
| `resource_type_lte` | string | No |  |
| `resource_type_not` | string | No |  |
| `resource_type_not_contains` | string | No |  |
| `resource_type_not_ends_with` | string | No |  |
| `resource_type_not_in` | string[] | No |  |
| `resource_type_not_starts_with` | string | No |  |
| `resource_type_starts_with` | string | No |  |
| `service` | string | No |  |
| `service_contains` | string | No |  |
| `service_ends_with` | string | No |  |
| `service_gt` | string | No |  |
| `service_gte` | string | No |  |
| `service_in` | string[] | No |  |
| `service_lt` | string | No |  |
| `service_lte` | string | No |  |
| `service_not` | string | No |  |
| `service_not_contains` | string | No |  |
| `service_not_ends_with` | string | No |  |
| `service_not_in` | string[] | No |  |
| `service_not_starts_with` | string | No |  |
| `service_starts_with` | string | No |  |
| `title` | string | No |  |
| `title_contains` | string | No |  |
| `title_ends_with` | string | No |  |
| `title_gt` | string | No |  |
| `title_gte` | string | No |  |
| `title_in` | string[] | No |  |
| `title_lt` | string | No |  |
| `title_lte` | string | No |  |
| `title_not` | string | No |  |
| `title_not_contains` | string | No |  |
| `title_not_ends_with` | string | No |  |
| `title_not_in` | string[] | No |  |
| `title_not_starts_with` | string | No |  |
| `title_starts_with` | string | No |  |
| `type` | [GraphType](../Graph/GraphType.md) | No |  |
| `type_in` | Array of [GraphType](../Graph/GraphType.md) | No |  |
| `type_not` | [GraphType](../Graph/GraphType.md) | No |  |
| `type_not_in` | Array of [GraphType](../Graph/GraphType.md) | No |  |
| `view` | [ViewWhereInput](../View/ViewWhereInput.md) | No |  |
| `vmNics_every` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vmNics_none` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vmNics_some` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vmVolumes_every` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | No |  |
| `vmVolumes_none` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | No |  |
| `vmVolumes_some` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | No |  |
| `vms_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `witnesses_every` | [WitnessWhereInput](../Witness/WitnessWhereInput.md) | No |  |
| `witnesses_none` | [WitnessWhereInput](../Witness/WitnessWhereInput.md) | No |  |
| `witnesses_some` | [WitnessWhereInput](../Witness/WitnessWhereInput.md) | No |  |
| `zones_every` | [ZoneWhereInput](../Zone/ZoneWhereInput.md) | No |  |
| `zones_none` | [ZoneWhereInput](../Zone/ZoneWhereInput.md) | No |  |
| `zones_some` | [ZoneWhereInput](../Zone/ZoneWhereInput.md) | No |  |

