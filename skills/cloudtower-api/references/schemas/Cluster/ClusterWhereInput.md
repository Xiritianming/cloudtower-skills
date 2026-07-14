# ClusterWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `NOT` | Array of [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `OR` | Array of [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `access_write_compress_enabled` | boolean | No |  |
| `access_write_compress_enabled_not` | boolean | No |  |
| `allocated_prioritized_space` | integer (int64) | No |  |
| `allocated_prioritized_space_gt` | integer (int64) | No |  |
| `allocated_prioritized_space_gte` | integer (int64) | No |  |
| `allocated_prioritized_space_in` | integer[] | No |  |
| `allocated_prioritized_space_lt` | integer (int64) | No |  |
| `allocated_prioritized_space_lte` | integer (int64) | No |  |
| `allocated_prioritized_space_not` | integer (int64) | No |  |
| `allocated_prioritized_space_not_in` | integer[] | No |  |
| `allocated_prioritized_space_usage` | number (double) | No |  |
| `allocated_prioritized_space_usage_gt` | number (double) | No |  |
| `allocated_prioritized_space_usage_gte` | number (double) | No |  |
| `allocated_prioritized_space_usage_in` | number[] | No |  |
| `allocated_prioritized_space_usage_lt` | number (double) | No |  |
| `allocated_prioritized_space_usage_lte` | number (double) | No |  |
| `allocated_prioritized_space_usage_not` | number (double) | No |  |
| `allocated_prioritized_space_usage_not_in` | number[] | No |  |
| `application_highest_version` | string | No |  |
| `application_highest_version_contains` | string | No |  |
| `application_highest_version_ends_with` | string | No |  |
| `application_highest_version_gt` | string | No |  |
| `application_highest_version_gte` | string | No |  |
| `application_highest_version_in` | string[] | No |  |
| `application_highest_version_lt` | string | No |  |
| `application_highest_version_lte` | string | No |  |
| `application_highest_version_not` | string | No |  |
| `application_highest_version_not_contains` | string | No |  |
| `application_highest_version_not_ends_with` | string | No |  |
| `application_highest_version_not_in` | string[] | No |  |
| `application_highest_version_not_starts_with` | string | No |  |
| `application_highest_version_starts_with` | string | No |  |
| `applications_every` | [ApplicationWhereInput](../Application/ApplicationWhereInput.md) | No |  |
| `applications_none` | [ApplicationWhereInput](../Application/ApplicationWhereInput.md) | No |  |
| `applications_some` | [ApplicationWhereInput](../Application/ApplicationWhereInput.md) | No |  |
| `architecture` | [Architecture](../Architecture/Architecture.md) | No |  |
| `architecture_in` | Array of [Architecture](../Architecture/Architecture.md) | No |  |
| `architecture_not` | [Architecture](../Architecture/Architecture.md) | No |  |
| `architecture_not_in` | Array of [Architecture](../Architecture/Architecture.md) | No |  |
| `auto_converge` | boolean | No |  |
| `auto_converge_not` | boolean | No |  |
| `commited_memory_bytes` | integer (int64) | No |  |
| `commited_memory_bytes_gt` | integer (int64) | No |  |
| `commited_memory_bytes_gte` | integer (int64) | No |  |
| `commited_memory_bytes_in` | integer[] | No |  |
| `commited_memory_bytes_lt` | integer (int64) | No |  |
| `commited_memory_bytes_lte` | integer (int64) | No |  |
| `commited_memory_bytes_not` | integer (int64) | No |  |
| `commited_memory_bytes_not_in` | integer[] | No |  |
| `connect_state` | [ConnectState](../Connect/ConnectState.md) | No |  |
| `connect_state_in` | Array of [ConnectState](../Connect/ConnectState.md) | No |  |
| `connect_state_not` | [ConnectState](../Connect/ConnectState.md) | No |  |
| `connect_state_not_in` | Array of [ConnectState](../Connect/ConnectState.md) | No |  |
| `consistency_groups_every` | [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `consistency_groups_none` | [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `consistency_groups_some` | [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `current_cpu_model` | string | No |  |
| `current_cpu_model_contains` | string | No |  |
| `current_cpu_model_ends_with` | string | No |  |
| `current_cpu_model_gt` | string | No |  |
| `current_cpu_model_gte` | string | No |  |
| `current_cpu_model_in` | string[] | No |  |
| `current_cpu_model_lt` | string | No |  |
| `current_cpu_model_lte` | string | No |  |
| `current_cpu_model_not` | string | No |  |
| `current_cpu_model_not_contains` | string | No |  |
| `current_cpu_model_not_ends_with` | string | No |  |
| `current_cpu_model_not_in` | string[] | No |  |
| `current_cpu_model_not_starts_with` | string | No |  |
| `current_cpu_model_starts_with` | string | No |  |
| `data_reduction_ratio` | number (double) | No |  |
| `data_reduction_ratio_gt` | number (double) | No |  |
| `data_reduction_ratio_gte` | number (double) | No |  |
| `data_reduction_ratio_in` | number[] | No |  |
| `data_reduction_ratio_lt` | number (double) | No |  |
| `data_reduction_ratio_lte` | number (double) | No |  |
| `data_reduction_ratio_not` | number (double) | No |  |
| `data_reduction_ratio_not_in` | number[] | No |  |
| `data_reduction_saving` | number (double) | No |  |
| `data_reduction_saving_gt` | number (double) | No |  |
| `data_reduction_saving_gte` | number (double) | No |  |
| `data_reduction_saving_in` | number[] | No |  |
| `data_reduction_saving_lt` | number (double) | No |  |
| `data_reduction_saving_lte` | number (double) | No |  |
| `data_reduction_saving_not` | number (double) | No |  |
| `data_reduction_saving_not_in` | number[] | No |  |
| `datacenters_every` | [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `datacenters_none` | [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `datacenters_some` | [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `dirty_cache_space` | integer (int64) | No |  |
| `dirty_cache_space_gt` | integer (int64) | No |  |
| `dirty_cache_space_gte` | integer (int64) | No |  |
| `dirty_cache_space_in` | integer[] | No |  |
| `dirty_cache_space_lt` | integer (int64) | No |  |
| `dirty_cache_space_lte` | integer (int64) | No |  |
| `dirty_cache_space_not` | integer (int64) | No |  |
| `dirty_cache_space_not_in` | integer[] | No |  |
| `dirty_cache_usage` | number (double) | No |  |
| `dirty_cache_usage_gt` | number (double) | No |  |
| `dirty_cache_usage_gte` | number (double) | No |  |
| `dirty_cache_usage_in` | number[] | No |  |
| `dirty_cache_usage_lt` | number (double) | No |  |
| `dirty_cache_usage_lte` | number (double) | No |  |
| `dirty_cache_usage_not` | number (double) | No |  |
| `dirty_cache_usage_not_in` | number[] | No |  |
| `disconnected_date` | string | No |  |
| `disconnected_date_gt` | string | No |  |
| `disconnected_date_gte` | string | No |  |
| `disconnected_date_in` | string[] | No |  |
| `disconnected_date_lt` | string | No |  |
| `disconnected_date_lte` | string | No |  |
| `disconnected_date_not` | string | No |  |
| `disconnected_date_not_in` | string[] | No |  |
| `disconnected_reason` | [ClusterConnectorErrorCode](../Cluster/ClusterConnectorErrorCode.md) | No |  |
| `disconnected_reason_in` | Array of [ClusterConnectorErrorCode](../Cluster/ClusterConnectorErrorCode.md) | No |  |
| `disconnected_reason_not` | [ClusterConnectorErrorCode](../Cluster/ClusterConnectorErrorCode.md) | No |  |
| `disconnected_reason_not_in` | Array of [ClusterConnectorErrorCode](../Cluster/ClusterConnectorErrorCode.md) | No |  |
| `downgraded_prioritized_space` | integer (int64) | No |  |
| `downgraded_prioritized_space_gt` | integer (int64) | No |  |
| `downgraded_prioritized_space_gte` | integer (int64) | No |  |
| `downgraded_prioritized_space_in` | integer[] | No |  |
| `downgraded_prioritized_space_lt` | integer (int64) | No |  |
| `downgraded_prioritized_space_lte` | integer (int64) | No |  |
| `downgraded_prioritized_space_not` | integer (int64) | No |  |
| `downgraded_prioritized_space_not_in` | integer[] | No |  |
| `ecp_license` | [EcpLicenseWhereInput](../Ecp/EcpLicenseWhereInput.md) | No |  |
| `enable_tiering` | boolean | No |  |
| `enable_tiering_not` | boolean | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `everoute_cluster` | [EverouteClusterWhereInput](../Everoute/EverouteClusterWhereInput.md) | No |  |
| `failure_cache_space` | integer (int64) | No |  |
| `failure_cache_space_gt` | integer (int64) | No |  |
| `failure_cache_space_gte` | integer (int64) | No |  |
| `failure_cache_space_in` | integer[] | No |  |
| `failure_cache_space_lt` | integer (int64) | No |  |
| `failure_cache_space_lte` | integer (int64) | No |  |
| `failure_cache_space_not` | integer (int64) | No |  |
| `failure_cache_space_not_in` | integer[] | No |  |
| `failure_data_space` | integer (int64) | No |  |
| `failure_data_space_gt` | integer (int64) | No |  |
| `failure_data_space_gte` | integer (int64) | No |  |
| `failure_data_space_in` | integer[] | No |  |
| `failure_data_space_lt` | integer (int64) | No |  |
| `failure_data_space_lte` | integer (int64) | No |  |
| `failure_data_space_not` | integer (int64) | No |  |
| `failure_data_space_not_in` | integer[] | No |  |
| `has_metrox` | boolean | No |  |
| `has_metrox_not` | boolean | No |  |
| `host_num` | integer (int32) | No |  |
| `host_num_gt` | integer (int32) | No |  |
| `host_num_gte` | integer (int32) | No |  |
| `host_num_in` | integer[] | No |  |
| `host_num_lt` | integer (int32) | No |  |
| `host_num_lte` | integer (int32) | No |  |
| `host_num_not` | integer (int32) | No |  |
| `host_num_not_in` | integer[] | No |  |
| `hosts_every` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `hosts_none` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `hosts_some` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `hypervisor` | [Hypervisor](../Hypervisor/Hypervisor.md) | No |  |
| `hypervisor_in` | Array of [Hypervisor](../Hypervisor/Hypervisor.md) | No |  |
| `hypervisor_not` | [Hypervisor](../Hypervisor/Hypervisor.md) | No |  |
| `hypervisor_not_in` | Array of [Hypervisor](../Hypervisor/Hypervisor.md) | No |  |
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
| `ip` | string | No |  |
| `ip_contains` | string | No |  |
| `ip_ends_with` | string | No |  |
| `ip_gt` | string | No |  |
| `ip_gte` | string | No |  |
| `ip_in` | string[] | No |  |
| `ip_lt` | string | No |  |
| `ip_lte` | string | No |  |
| `ip_not` | string | No |  |
| `ip_not_contains` | string | No |  |
| `ip_not_ends_with` | string | No |  |
| `ip_not_in` | string[] | No |  |
| `ip_not_starts_with` | string | No |  |
| `ip_starts_with` | string | No |  |
| `is_all_flash` | boolean | No |  |
| `is_all_flash_not` | boolean | No |  |
| `iscsi_vip` | string | No |  |
| `iscsi_vip_contains` | string | No |  |
| `iscsi_vip_ends_with` | string | No |  |
| `iscsi_vip_gt` | string | No |  |
| `iscsi_vip_gte` | string | No |  |
| `iscsi_vip_in` | string[] | No |  |
| `iscsi_vip_lt` | string | No |  |
| `iscsi_vip_lte` | string | No |  |
| `iscsi_vip_not` | string | No |  |
| `iscsi_vip_not_contains` | string | No |  |
| `iscsi_vip_not_ends_with` | string | No |  |
| `iscsi_vip_not_in` | string[] | No |  |
| `iscsi_vip_not_starts_with` | string | No |  |
| `iscsi_vip_starts_with` | string | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `license_expire_date` | string | No |  |
| `license_expire_date_gt` | string | No |  |
| `license_expire_date_gte` | string | No |  |
| `license_expire_date_in` | string[] | No |  |
| `license_expire_date_lt` | string | No |  |
| `license_expire_date_lte` | string | No |  |
| `license_expire_date_not` | string | No |  |
| `license_expire_date_not_in` | string[] | No |  |
| `license_serial` | string | No |  |
| `license_serial_contains` | string | No |  |
| `license_serial_ends_with` | string | No |  |
| `license_serial_gt` | string | No |  |
| `license_serial_gte` | string | No |  |
| `license_serial_in` | string[] | No |  |
| `license_serial_lt` | string | No |  |
| `license_serial_lte` | string | No |  |
| `license_serial_not` | string | No |  |
| `license_serial_not_contains` | string | No |  |
| `license_serial_not_ends_with` | string | No |  |
| `license_serial_not_in` | string[] | No |  |
| `license_serial_not_starts_with` | string | No |  |
| `license_serial_starts_with` | string | No |  |
| `license_sign_date` | string | No |  |
| `license_sign_date_gt` | string | No |  |
| `license_sign_date_gte` | string | No |  |
| `license_sign_date_in` | string[] | No |  |
| `license_sign_date_lt` | string | No |  |
| `license_sign_date_lte` | string | No |  |
| `license_sign_date_not` | string | No |  |
| `license_sign_date_not_in` | string[] | No |  |
| `license_type` | [LicenseType](../License/LicenseType.md) | No |  |
| `license_type_in` | Array of [LicenseType](../License/LicenseType.md) | No |  |
| `license_type_not` | [LicenseType](../License/LicenseType.md) | No |  |
| `license_type_not_in` | Array of [LicenseType](../License/LicenseType.md) | No |  |
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
| `logical_used_data_space` | integer (int64) | No |  |
| `logical_used_data_space_gt` | integer (int64) | No |  |
| `logical_used_data_space_gte` | integer (int64) | No |  |
| `logical_used_data_space_in` | integer[] | No |  |
| `logical_used_data_space_lt` | integer (int64) | No |  |
| `logical_used_data_space_lte` | integer (int64) | No |  |
| `logical_used_data_space_not` | integer (int64) | No |  |
| `logical_used_data_space_not_in` | integer[] | No |  |
| `maintenance_end_date` | string | No |  |
| `maintenance_end_date_gt` | string | No |  |
| `maintenance_end_date_gte` | string | No |  |
| `maintenance_end_date_in` | string[] | No |  |
| `maintenance_end_date_lt` | string | No |  |
| `maintenance_end_date_lte` | string | No |  |
| `maintenance_end_date_not` | string | No |  |
| `maintenance_end_date_not_in` | string[] | No |  |
| `maintenance_start_date` | string | No |  |
| `maintenance_start_date_gt` | string | No |  |
| `maintenance_start_date_gte` | string | No |  |
| `maintenance_start_date_in` | string[] | No |  |
| `maintenance_start_date_lt` | string | No |  |
| `maintenance_start_date_lte` | string | No |  |
| `maintenance_start_date_not` | string | No |  |
| `maintenance_start_date_not_in` | string[] | No |  |
| `management_vip` | string | No |  |
| `management_vip_contains` | string | No |  |
| `management_vip_ends_with` | string | No |  |
| `management_vip_gt` | string | No |  |
| `management_vip_gte` | string | No |  |
| `management_vip_in` | string[] | No |  |
| `management_vip_lt` | string | No |  |
| `management_vip_lte` | string | No |  |
| `management_vip_not` | string | No |  |
| `management_vip_not_contains` | string | No |  |
| `management_vip_not_ends_with` | string | No |  |
| `management_vip_not_in` | string[] | No |  |
| `management_vip_not_starts_with` | string | No |  |
| `management_vip_starts_with` | string | No |  |
| `max_chunk_num` | integer (int32) | No |  |
| `max_chunk_num_gt` | integer (int32) | No |  |
| `max_chunk_num_gte` | integer (int32) | No |  |
| `max_chunk_num_in` | integer[] | No |  |
| `max_chunk_num_lt` | integer (int32) | No |  |
| `max_chunk_num_lte` | integer (int32) | No |  |
| `max_chunk_num_not` | integer (int32) | No |  |
| `max_chunk_num_not_in` | integer[] | No |  |
| `max_physical_data_capacity` | integer (int64) | No |  |
| `max_physical_data_capacity_gt` | integer (int64) | No |  |
| `max_physical_data_capacity_gte` | integer (int64) | No |  |
| `max_physical_data_capacity_in` | integer[] | No |  |
| `max_physical_data_capacity_lt` | integer (int64) | No |  |
| `max_physical_data_capacity_lte` | integer (int64) | No |  |
| `max_physical_data_capacity_not` | integer (int64) | No |  |
| `max_physical_data_capacity_not_in` | integer[] | No |  |
| `max_physical_data_capacity_per_node` | integer (int64) | No |  |
| `max_physical_data_capacity_per_node_gt` | integer (int64) | No |  |
| `max_physical_data_capacity_per_node_gte` | integer (int64) | No |  |
| `max_physical_data_capacity_per_node_in` | integer[] | No |  |
| `max_physical_data_capacity_per_node_lt` | integer (int64) | No |  |
| `max_physical_data_capacity_per_node_lte` | integer (int64) | No |  |
| `max_physical_data_capacity_per_node_not` | integer (int64) | No |  |
| `max_physical_data_capacity_per_node_not_in` | integer[] | No |  |
| `mgt_gateway` | string | No |  |
| `mgt_gateway_contains` | string | No |  |
| `mgt_gateway_ends_with` | string | No |  |
| `mgt_gateway_gt` | string | No |  |
| `mgt_gateway_gte` | string | No |  |
| `mgt_gateway_in` | string[] | No |  |
| `mgt_gateway_lt` | string | No |  |
| `mgt_gateway_lte` | string | No |  |
| `mgt_gateway_not` | string | No |  |
| `mgt_gateway_not_contains` | string | No |  |
| `mgt_gateway_not_ends_with` | string | No |  |
| `mgt_gateway_not_in` | string[] | No |  |
| `mgt_gateway_not_starts_with` | string | No |  |
| `mgt_gateway_starts_with` | string | No |  |
| `mgt_netmask` | string | No |  |
| `mgt_netmask_contains` | string | No |  |
| `mgt_netmask_ends_with` | string | No |  |
| `mgt_netmask_gt` | string | No |  |
| `mgt_netmask_gte` | string | No |  |
| `mgt_netmask_in` | string[] | No |  |
| `mgt_netmask_lt` | string | No |  |
| `mgt_netmask_lte` | string | No |  |
| `mgt_netmask_not` | string | No |  |
| `mgt_netmask_not_contains` | string | No |  |
| `mgt_netmask_not_ends_with` | string | No |  |
| `mgt_netmask_not_in` | string[] | No |  |
| `mgt_netmask_not_starts_with` | string | No |  |
| `mgt_netmask_starts_with` | string | No |  |
| `migration_data_size` | integer (int64) | No |  |
| `migration_data_size_gt` | integer (int64) | No |  |
| `migration_data_size_gte` | integer (int64) | No |  |
| `migration_data_size_in` | integer[] | No |  |
| `migration_data_size_lt` | integer (int64) | No |  |
| `migration_data_size_lte` | integer (int64) | No |  |
| `migration_data_size_not` | integer (int64) | No |  |
| `migration_data_size_not_in` | integer[] | No |  |
| `migration_speed` | integer (int64) | No |  |
| `migration_speed_gt` | integer (int64) | No |  |
| `migration_speed_gte` | integer (int64) | No |  |
| `migration_speed_in` | integer[] | No |  |
| `migration_speed_lt` | integer (int64) | No |  |
| `migration_speed_lte` | integer (int64) | No |  |
| `migration_speed_not` | integer (int64) | No |  |
| `migration_speed_not_in` | integer[] | No |  |
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
| `no_performance_layer` | boolean | No |  |
| `no_performance_layer_not` | boolean | No |  |
| `ntp_mode` | [NtpMode](../Ntp/NtpMode.md) | No |  |
| `ntp_mode_in` | Array of [NtpMode](../Ntp/NtpMode.md) | No |  |
| `ntp_mode_not` | [NtpMode](../Ntp/NtpMode.md) | No |  |
| `ntp_mode_not_in` | Array of [NtpMode](../Ntp/NtpMode.md) | No |  |
| `nvme_over_rdma_enabled` | boolean | No |  |
| `nvme_over_rdma_enabled_not` | boolean | No |  |
| `nvme_over_tcp_enabled` | boolean | No |  |
| `nvme_over_tcp_enabled_not` | boolean | No |  |
| `nvmf_enabled` | boolean | No |  |
| `nvmf_enabled_not` | boolean | No |  |
| `overall_efficiency` | number (double) | No |  |
| `overall_efficiency_gt` | number (double) | No |  |
| `overall_efficiency_gte` | number (double) | No |  |
| `overall_efficiency_in` | number[] | No |  |
| `overall_efficiency_lt` | number (double) | No |  |
| `overall_efficiency_lte` | number (double) | No |  |
| `overall_efficiency_not` | number (double) | No |  |
| `overall_efficiency_not_in` | number[] | No |  |
| `perf_allocated_data_space` | integer (int64) | No |  |
| `perf_allocated_data_space_gt` | integer (int64) | No |  |
| `perf_allocated_data_space_gte` | integer (int64) | No |  |
| `perf_allocated_data_space_in` | integer[] | No |  |
| `perf_allocated_data_space_lt` | integer (int64) | No |  |
| `perf_allocated_data_space_lte` | integer (int64) | No |  |
| `perf_allocated_data_space_not` | integer (int64) | No |  |
| `perf_allocated_data_space_not_in` | integer[] | No |  |
| `perf_failure_data_space` | integer (int64) | No |  |
| `perf_failure_data_space_gt` | integer (int64) | No |  |
| `perf_failure_data_space_gte` | integer (int64) | No |  |
| `perf_failure_data_space_in` | integer[] | No |  |
| `perf_failure_data_space_lt` | integer (int64) | No |  |
| `perf_failure_data_space_lte` | integer (int64) | No |  |
| `perf_failure_data_space_not` | integer (int64) | No |  |
| `perf_failure_data_space_not_in` | integer[] | No |  |
| `perf_total_data_capacity` | integer (int64) | No |  |
| `perf_total_data_capacity_gt` | integer (int64) | No |  |
| `perf_total_data_capacity_gte` | integer (int64) | No |  |
| `perf_total_data_capacity_in` | integer[] | No |  |
| `perf_total_data_capacity_lt` | integer (int64) | No |  |
| `perf_total_data_capacity_lte` | integer (int64) | No |  |
| `perf_total_data_capacity_not` | integer (int64) | No |  |
| `perf_total_data_capacity_not_in` | integer[] | No |  |
| `perf_used_data_space` | integer (int64) | No |  |
| `perf_used_data_space_gt` | integer (int64) | No |  |
| `perf_used_data_space_gte` | integer (int64) | No |  |
| `perf_used_data_space_in` | integer[] | No |  |
| `perf_used_data_space_lt` | integer (int64) | No |  |
| `perf_used_data_space_lte` | integer (int64) | No |  |
| `perf_used_data_space_not` | integer (int64) | No |  |
| `perf_used_data_space_not_in` | integer[] | No |  |
| `perf_valid_data_space` | integer (int64) | No |  |
| `perf_valid_data_space_gt` | integer (int64) | No |  |
| `perf_valid_data_space_gte` | integer (int64) | No |  |
| `perf_valid_data_space_in` | integer[] | No |  |
| `perf_valid_data_space_lt` | integer (int64) | No |  |
| `perf_valid_data_space_lte` | integer (int64) | No |  |
| `perf_valid_data_space_not` | integer (int64) | No |  |
| `perf_valid_data_space_not_in` | integer[] | No |  |
| `planned_prioritized_space` | integer (int64) | No |  |
| `planned_prioritized_space_gt` | integer (int64) | No |  |
| `planned_prioritized_space_gte` | integer (int64) | No |  |
| `planned_prioritized_space_in` | integer[] | No |  |
| `planned_prioritized_space_lt` | integer (int64) | No |  |
| `planned_prioritized_space_lte` | integer (int64) | No |  |
| `planned_prioritized_space_not` | integer (int64) | No |  |
| `planned_prioritized_space_not_in` | integer[] | No |  |
| `pmem_enabled` | boolean | No |  |
| `pmem_enabled_not` | boolean | No |  |
| `prio_space_percentage` | number (double) | No |  |
| `prio_space_percentage_gt` | number (double) | No |  |
| `prio_space_percentage_gte` | number (double) | No |  |
| `prio_space_percentage_in` | number[] | No |  |
| `prio_space_percentage_lt` | number (double) | No |  |
| `prio_space_percentage_lte` | number (double) | No |  |
| `prio_space_percentage_not` | number (double) | No |  |
| `prio_space_percentage_not_in` | number[] | No |  |
| `provisioned_cpu_cores` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm_gt` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm_gte` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm_in` | integer[] | No |  |
| `provisioned_cpu_cores_for_active_vm_lt` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm_lte` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm_not` | integer (int32) | No |  |
| `provisioned_cpu_cores_for_active_vm_not_in` | integer[] | No |  |
| `provisioned_cpu_cores_gt` | integer (int32) | No |  |
| `provisioned_cpu_cores_gte` | integer (int32) | No |  |
| `provisioned_cpu_cores_in` | integer[] | No |  |
| `provisioned_cpu_cores_lt` | integer (int32) | No |  |
| `provisioned_cpu_cores_lte` | integer (int32) | No |  |
| `provisioned_cpu_cores_not` | integer (int32) | No |  |
| `provisioned_cpu_cores_not_in` | integer[] | No |  |
| `provisioned_for_active_vm_ratio` | number (double) | No |  |
| `provisioned_for_active_vm_ratio_gt` | number (double) | No |  |
| `provisioned_for_active_vm_ratio_gte` | number (double) | No |  |
| `provisioned_for_active_vm_ratio_in` | number[] | No |  |
| `provisioned_for_active_vm_ratio_lt` | number (double) | No |  |
| `provisioned_for_active_vm_ratio_lte` | number (double) | No |  |
| `provisioned_for_active_vm_ratio_not` | number (double) | No |  |
| `provisioned_for_active_vm_ratio_not_in` | number[] | No |  |
| `provisioned_memory_bytes` | integer (int64) | No |  |
| `provisioned_memory_bytes_gt` | integer (int64) | No |  |
| `provisioned_memory_bytes_gte` | integer (int64) | No |  |
| `provisioned_memory_bytes_in` | integer[] | No |  |
| `provisioned_memory_bytes_lt` | integer (int64) | No |  |
| `provisioned_memory_bytes_lte` | integer (int64) | No |  |
| `provisioned_memory_bytes_not` | integer (int64) | No |  |
| `provisioned_memory_bytes_not_in` | integer[] | No |  |
| `provisioned_ratio` | number (double) | No |  |
| `provisioned_ratio_gt` | number (double) | No |  |
| `provisioned_ratio_gte` | number (double) | No |  |
| `provisioned_ratio_in` | number[] | No |  |
| `provisioned_ratio_lt` | number (double) | No |  |
| `provisioned_ratio_lte` | number (double) | No |  |
| `provisioned_ratio_not` | number (double) | No |  |
| `provisioned_ratio_not_in` | number[] | No |  |
| `rdma_enabled` | boolean | No |  |
| `rdma_enabled_not` | boolean | No |  |
| `recover_data_size` | integer (int64) | No |  |
| `recover_data_size_gt` | integer (int64) | No |  |
| `recover_data_size_gte` | integer (int64) | No |  |
| `recover_data_size_in` | integer[] | No |  |
| `recover_data_size_lt` | integer (int64) | No |  |
| `recover_data_size_lte` | integer (int64) | No |  |
| `recover_data_size_not` | integer (int64) | No |  |
| `recover_data_size_not_in` | integer[] | No |  |
| `recover_speed` | integer (int64) | No |  |
| `recover_speed_gt` | integer (int64) | No |  |
| `recover_speed_gte` | integer (int64) | No |  |
| `recover_speed_in` | integer[] | No |  |
| `recover_speed_lt` | integer (int64) | No |  |
| `recover_speed_lte` | integer (int64) | No |  |
| `recover_speed_not` | integer (int64) | No |  |
| `recover_speed_not_in` | integer[] | No |  |
| `replica_capacity_only` | boolean | No |  |
| `replica_capacity_only_not` | boolean | No |  |
| `reserved_cpu_cores_for_system_service` | integer (int32) | No |  |
| `reserved_cpu_cores_for_system_service_gt` | integer (int32) | No |  |
| `reserved_cpu_cores_for_system_service_gte` | integer (int32) | No |  |
| `reserved_cpu_cores_for_system_service_in` | integer[] | No |  |
| `reserved_cpu_cores_for_system_service_lt` | integer (int32) | No |  |
| `reserved_cpu_cores_for_system_service_lte` | integer (int32) | No |  |
| `reserved_cpu_cores_for_system_service_not` | integer (int32) | No |  |
| `reserved_cpu_cores_for_system_service_not_in` | integer[] | No |  |
| `running_vm_num` | integer (int32) | No |  |
| `running_vm_num_gt` | integer (int32) | No |  |
| `running_vm_num_gte` | integer (int32) | No |  |
| `running_vm_num_in` | integer[] | No |  |
| `running_vm_num_lt` | integer (int32) | No |  |
| `running_vm_num_lte` | integer (int32) | No |  |
| `running_vm_num_not` | integer (int32) | No |  |
| `running_vm_num_not_in` | integer[] | No |  |
| `settings` | [ClusterSettingsWhereInput](../Cluster/ClusterSettingsWhereInput.md) | No |  |
| `software_edition` | [SoftwareEdition](../Software/SoftwareEdition.md) | No |  |
| `software_edition_in` | Array of [SoftwareEdition](../Software/SoftwareEdition.md) | No |  |
| `software_edition_not` | [SoftwareEdition](../Software/SoftwareEdition.md) | No |  |
| `software_edition_not_in` | Array of [SoftwareEdition](../Software/SoftwareEdition.md) | No |  |
| `stopped_vm_num` | integer (int32) | No |  |
| `stopped_vm_num_gt` | integer (int32) | No |  |
| `stopped_vm_num_gte` | integer (int32) | No |  |
| `stopped_vm_num_in` | integer[] | No |  |
| `stopped_vm_num_lt` | integer (int32) | No |  |
| `stopped_vm_num_lte` | integer (int32) | No |  |
| `stopped_vm_num_not` | integer (int32) | No |  |
| `stopped_vm_num_not_in` | integer[] | No |  |
| `stretch` | boolean | No |  |
| `stretch_not` | boolean | No |  |
| `suspended_vm_num` | integer (int32) | No |  |
| `suspended_vm_num_gt` | integer (int32) | No |  |
| `suspended_vm_num_gte` | integer (int32) | No |  |
| `suspended_vm_num_in` | integer[] | No |  |
| `suspended_vm_num_lt` | integer (int32) | No |  |
| `suspended_vm_num_lte` | integer (int32) | No |  |
| `suspended_vm_num_not` | integer (int32) | No |  |
| `suspended_vm_num_not_in` | integer[] | No |  |
| `total_cache_capacity` | integer (int64) | No |  |
| `total_cache_capacity_gt` | integer (int64) | No |  |
| `total_cache_capacity_gte` | integer (int64) | No |  |
| `total_cache_capacity_in` | integer[] | No |  |
| `total_cache_capacity_lt` | integer (int64) | No |  |
| `total_cache_capacity_lte` | integer (int64) | No |  |
| `total_cache_capacity_not` | integer (int64) | No |  |
| `total_cache_capacity_not_in` | integer[] | No |  |
| `total_cpu_cores` | integer (int32) | No |  |
| `total_cpu_cores_gt` | integer (int32) | No |  |
| `total_cpu_cores_gte` | integer (int32) | No |  |
| `total_cpu_cores_in` | integer[] | No |  |
| `total_cpu_cores_lt` | integer (int32) | No |  |
| `total_cpu_cores_lte` | integer (int32) | No |  |
| `total_cpu_cores_not` | integer (int32) | No |  |
| `total_cpu_cores_not_in` | integer[] | No |  |
| `total_cpu_hz` | integer (int64) | No |  |
| `total_cpu_hz_gt` | integer (int64) | No |  |
| `total_cpu_hz_gte` | integer (int64) | No |  |
| `total_cpu_hz_in` | integer[] | No |  |
| `total_cpu_hz_lt` | integer (int64) | No |  |
| `total_cpu_hz_lte` | integer (int64) | No |  |
| `total_cpu_hz_not` | integer (int64) | No |  |
| `total_cpu_hz_not_in` | integer[] | No |  |
| `total_cpu_sockets` | integer (int32) | No |  |
| `total_cpu_sockets_gt` | integer (int32) | No |  |
| `total_cpu_sockets_gte` | integer (int32) | No |  |
| `total_cpu_sockets_in` | integer[] | No |  |
| `total_cpu_sockets_lt` | integer (int32) | No |  |
| `total_cpu_sockets_lte` | integer (int32) | No |  |
| `total_cpu_sockets_not` | integer (int32) | No |  |
| `total_cpu_sockets_not_in` | integer[] | No |  |
| `total_data_capacity` | integer (int64) | No |  |
| `total_data_capacity_gt` | integer (int64) | No |  |
| `total_data_capacity_gte` | integer (int64) | No |  |
| `total_data_capacity_in` | integer[] | No |  |
| `total_data_capacity_lt` | integer (int64) | No |  |
| `total_data_capacity_lte` | integer (int64) | No |  |
| `total_data_capacity_not` | integer (int64) | No |  |
| `total_data_capacity_not_in` | integer[] | No |  |
| `total_memory_bytes` | integer (int64) | No |  |
| `total_memory_bytes_gt` | integer (int64) | No |  |
| `total_memory_bytes_gte` | integer (int64) | No |  |
| `total_memory_bytes_in` | integer[] | No |  |
| `total_memory_bytes_lt` | integer (int64) | No |  |
| `total_memory_bytes_lte` | integer (int64) | No |  |
| `total_memory_bytes_not` | integer (int64) | No |  |
| `total_memory_bytes_not_in` | integer[] | No |  |
| `total_prio_volume_size` | integer (int64) | No |  |
| `total_prio_volume_size_gt` | integer (int64) | No |  |
| `total_prio_volume_size_gte` | integer (int64) | No |  |
| `total_prio_volume_size_in` | integer[] | No |  |
| `total_prio_volume_size_lt` | integer (int64) | No |  |
| `total_prio_volume_size_lte` | integer (int64) | No |  |
| `total_prio_volume_size_not` | integer (int64) | No |  |
| `total_prio_volume_size_not_in` | integer[] | No |  |
| `total_prio_volume_size_usage` | number (double) | No |  |
| `total_prio_volume_size_usage_gt` | number (double) | No |  |
| `total_prio_volume_size_usage_gte` | number (double) | No |  |
| `total_prio_volume_size_usage_in` | number[] | No |  |
| `total_prio_volume_size_usage_lt` | number (double) | No |  |
| `total_prio_volume_size_usage_lte` | number (double) | No |  |
| `total_prio_volume_size_usage_not` | number (double) | No |  |
| `total_prio_volume_size_usage_not_in` | number[] | No |  |
| `type` | [ClusterType](../Cluster/ClusterType.md) | No |  |
| `type_in` | Array of [ClusterType](../Cluster/ClusterType.md) | No |  |
| `type_not` | [ClusterType](../Cluster/ClusterType.md) | No |  |
| `type_not_in` | Array of [ClusterType](../Cluster/ClusterType.md) | No |  |
| `upgrade_for_tiering` | boolean | No |  |
| `upgrade_for_tiering_not` | boolean | No |  |
| `upgrade_tool_version` | string | No |  |
| `upgrade_tool_version_contains` | string | No |  |
| `upgrade_tool_version_ends_with` | string | No |  |
| `upgrade_tool_version_gt` | string | No |  |
| `upgrade_tool_version_gte` | string | No |  |
| `upgrade_tool_version_in` | string[] | No |  |
| `upgrade_tool_version_lt` | string | No |  |
| `upgrade_tool_version_lte` | string | No |  |
| `upgrade_tool_version_not` | string | No |  |
| `upgrade_tool_version_not_contains` | string | No |  |
| `upgrade_tool_version_not_ends_with` | string | No |  |
| `upgrade_tool_version_not_in` | string[] | No |  |
| `upgrade_tool_version_not_starts_with` | string | No |  |
| `upgrade_tool_version_starts_with` | string | No |  |
| `used_cache_space` | integer (int64) | No |  |
| `used_cache_space_gt` | integer (int64) | No |  |
| `used_cache_space_gte` | integer (int64) | No |  |
| `used_cache_space_in` | integer[] | No |  |
| `used_cache_space_lt` | integer (int64) | No |  |
| `used_cache_space_lte` | integer (int64) | No |  |
| `used_cache_space_not` | integer (int64) | No |  |
| `used_cache_space_not_in` | integer[] | No |  |
| `used_cpu_hz` | number (double) | No |  |
| `used_cpu_hz_gt` | number (double) | No |  |
| `used_cpu_hz_gte` | number (double) | No |  |
| `used_cpu_hz_in` | number[] | No |  |
| `used_cpu_hz_lt` | number (double) | No |  |
| `used_cpu_hz_lte` | number (double) | No |  |
| `used_cpu_hz_not` | number (double) | No |  |
| `used_cpu_hz_not_in` | number[] | No |  |
| `used_data_space` | integer (int64) | No |  |
| `used_data_space_gt` | integer (int64) | No |  |
| `used_data_space_gte` | integer (int64) | No |  |
| `used_data_space_in` | integer[] | No |  |
| `used_data_space_lt` | integer (int64) | No |  |
| `used_data_space_lte` | integer (int64) | No |  |
| `used_data_space_not` | integer (int64) | No |  |
| `used_data_space_not_in` | integer[] | No |  |
| `used_memory_bytes` | number (double) | No |  |
| `used_memory_bytes_gt` | number (double) | No |  |
| `used_memory_bytes_gte` | number (double) | No |  |
| `used_memory_bytes_in` | number[] | No |  |
| `used_memory_bytes_lt` | number (double) | No |  |
| `used_memory_bytes_lte` | number (double) | No |  |
| `used_memory_bytes_not` | number (double) | No |  |
| `used_memory_bytes_not_in` | number[] | No |  |
| `valid_cache_space` | integer (int64) | No |  |
| `valid_cache_space_gt` | integer (int64) | No |  |
| `valid_cache_space_gte` | integer (int64) | No |  |
| `valid_cache_space_in` | integer[] | No |  |
| `valid_cache_space_lt` | integer (int64) | No |  |
| `valid_cache_space_lte` | integer (int64) | No |  |
| `valid_cache_space_not` | integer (int64) | No |  |
| `valid_cache_space_not_in` | integer[] | No |  |
| `valid_data_space` | integer (int64) | No |  |
| `valid_data_space_gt` | integer (int64) | No |  |
| `valid_data_space_gte` | integer (int64) | No |  |
| `valid_data_space_in` | integer[] | No |  |
| `valid_data_space_lt` | integer (int64) | No |  |
| `valid_data_space_lte` | integer (int64) | No |  |
| `valid_data_space_not` | integer (int64) | No |  |
| `valid_data_space_not_in` | integer[] | No |  |
| `vcenterAccount` | [VcenterAccountWhereInput](../Vcenter/VcenterAccountWhereInput.md) | No |  |
| `vdses_every` | [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `vdses_none` | [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `vdses_some` | [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `version` | string | No |  |
| `version_contains` | string | No |  |
| `version_ends_with` | string | No |  |
| `version_gt` | string | No |  |
| `version_gte` | string | No |  |
| `version_in` | string[] | No |  |
| `version_lt` | string | No |  |
| `version_lte` | string | No |  |
| `version_not` | string | No |  |
| `version_not_contains` | string | No |  |
| `version_not_ends_with` | string | No |  |
| `version_not_in` | string[] | No |  |
| `version_not_starts_with` | string | No |  |
| `version_starts_with` | string | No |  |
| `vhost_enabled` | boolean | No |  |
| `vhost_enabled_not` | boolean | No |  |
| `vm_folders_every` | [VmFolderWhereInput](../Vm/VmFolderWhereInput.md) | No |  |
| `vm_folders_none` | [VmFolderWhereInput](../Vm/VmFolderWhereInput.md) | No |  |
| `vm_folders_some` | [VmFolderWhereInput](../Vm/VmFolderWhereInput.md) | No |  |
| `vm_num` | integer (int32) | No |  |
| `vm_num_gt` | integer (int32) | No |  |
| `vm_num_gte` | integer (int32) | No |  |
| `vm_num_in` | integer[] | No |  |
| `vm_num_lt` | integer (int32) | No |  |
| `vm_num_lte` | integer (int32) | No |  |
| `vm_num_not` | integer (int32) | No |  |
| `vm_num_not_in` | integer[] | No |  |
| `vm_templates_every` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_templates_none` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_templates_some` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vms_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `witness` | [WitnessWhereInput](../Witness/WitnessWhereInput.md) | No |  |
| `zones_every` | [ZoneWhereInput](../Zone/ZoneWhereInput.md) | No |  |
| `zones_none` | [ZoneWhereInput](../Zone/ZoneWhereInput.md) | No |  |
| `zones_some` | [ZoneWhereInput](../Zone/ZoneWhereInput.md) | No |  |

