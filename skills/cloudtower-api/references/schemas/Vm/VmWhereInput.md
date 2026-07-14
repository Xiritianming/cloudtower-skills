# VmWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `NOT` | Array of [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `OR` | Array of [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `anti_malware_enabled` | boolean | No |  |
| `anti_malware_enabled_not` | boolean | No |  |
| `backup_plans_every` | [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | No |  |
| `backup_plans_none` | [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | No |  |
| `backup_plans_some` | [BackupPlanWhereInput](../Backup/BackupPlanWhereInput.md) | No |  |
| `bios_uuid` | string | No |  |
| `bios_uuid_contains` | string | No |  |
| `bios_uuid_ends_with` | string | No |  |
| `bios_uuid_gt` | string | No |  |
| `bios_uuid_gte` | string | No |  |
| `bios_uuid_in` | string[] | No |  |
| `bios_uuid_lt` | string | No |  |
| `bios_uuid_lte` | string | No |  |
| `bios_uuid_not` | string | No |  |
| `bios_uuid_not_contains` | string | No |  |
| `bios_uuid_not_ends_with` | string | No |  |
| `bios_uuid_not_in` | string[] | No |  |
| `bios_uuid_not_starts_with` | string | No |  |
| `bios_uuid_starts_with` | string | No |  |
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clock_offset_in` | Array of [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clock_offset_not` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clock_offset_not_in` | Array of [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `cloud_init_supported` | boolean | No |  |
| `cloud_init_supported_not` | boolean | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `cpu_model` | string | No |  |
| `cpu_model_contains` | string | No |  |
| `cpu_model_ends_with` | string | No |  |
| `cpu_model_gt` | string | No |  |
| `cpu_model_gte` | string | No |  |
| `cpu_model_in` | string[] | No |  |
| `cpu_model_lt` | string | No |  |
| `cpu_model_lte` | string | No |  |
| `cpu_model_not` | string | No |  |
| `cpu_model_not_contains` | string | No |  |
| `cpu_model_not_ends_with` | string | No |  |
| `cpu_model_not_in` | string[] | No |  |
| `cpu_model_not_starts_with` | string | No |  |
| `cpu_model_starts_with` | string | No |  |
| `cpu_usage` | number (double) | No |  |
| `cpu_usage_gt` | number (double) | No |  |
| `cpu_usage_gte` | number (double) | No |  |
| `cpu_usage_in` | number[] | No |  |
| `cpu_usage_lt` | number (double) | No |  |
| `cpu_usage_lte` | number (double) | No |  |
| `cpu_usage_not` | number (double) | No |  |
| `cpu_usage_not_in` | number[] | No |  |
| `deleted_at` | string | No |  |
| `deleted_at_gt` | string | No |  |
| `deleted_at_gte` | string | No |  |
| `deleted_at_in` | string[] | No |  |
| `deleted_at_lt` | string | No |  |
| `deleted_at_lte` | string | No |  |
| `deleted_at_not` | string | No |  |
| `deleted_at_not_in` | string[] | No |  |
| `description` | string | No |  |
| `description_contains` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_gt` | string | No |  |
| `description_gte` | string | No |  |
| `description_in` | string[] | No |  |
| `description_lt` | string | No |  |
| `description_lte` | string | No |  |
| `description_not` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_starts_with` | string | No |  |
| `description_starts_with` | string | No |  |
| `dns_servers` | string | No |  |
| `dns_servers_contains` | string | No |  |
| `dns_servers_ends_with` | string | No |  |
| `dns_servers_gt` | string | No |  |
| `dns_servers_gte` | string | No |  |
| `dns_servers_in` | string[] | No |  |
| `dns_servers_lt` | string | No |  |
| `dns_servers_lte` | string | No |  |
| `dns_servers_not` | string | No |  |
| `dns_servers_not_contains` | string | No |  |
| `dns_servers_not_ends_with` | string | No |  |
| `dns_servers_not_in` | string[] | No |  |
| `dns_servers_not_starts_with` | string | No |  |
| `dns_servers_starts_with` | string | No |  |
| `dpi_enabled` | boolean | No |  |
| `dpi_enabled_not` | boolean | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entity_filter_results_every` | [VmEntityFilterResultWhereInput](../Vm/VmEntityFilterResultWhereInput.md) | No |  |
| `entity_filter_results_none` | [VmEntityFilterResultWhereInput](../Vm/VmEntityFilterResultWhereInput.md) | No |  |
| `entity_filter_results_some` | [VmEntityFilterResultWhereInput](../Vm/VmEntityFilterResultWhereInput.md) | No |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `firmware_in` | Array of [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `firmware_not` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `firmware_not_in` | Array of [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `folder` | [VmFolderWhereInput](../Vm/VmFolderWhereInput.md) | No |  |
| `gpu_devices_every` | [GpuDeviceWhereInput](../Gpu/GpuDeviceWhereInput.md) | No |  |
| `gpu_devices_none` | [GpuDeviceWhereInput](../Gpu/GpuDeviceWhereInput.md) | No |  |
| `gpu_devices_some` | [GpuDeviceWhereInput](../Gpu/GpuDeviceWhereInput.md) | No |  |
| `guest_cpu_model` | string | No |  |
| `guest_cpu_model_contains` | string | No |  |
| `guest_cpu_model_ends_with` | string | No |  |
| `guest_cpu_model_gt` | string | No |  |
| `guest_cpu_model_gte` | string | No |  |
| `guest_cpu_model_in` | string[] | No |  |
| `guest_cpu_model_lt` | string | No |  |
| `guest_cpu_model_lte` | string | No |  |
| `guest_cpu_model_not` | string | No |  |
| `guest_cpu_model_not_contains` | string | No |  |
| `guest_cpu_model_not_ends_with` | string | No |  |
| `guest_cpu_model_not_in` | string[] | No |  |
| `guest_cpu_model_not_starts_with` | string | No |  |
| `guest_cpu_model_starts_with` | string | No |  |
| `guest_os_type` | [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `guest_os_type_in` | Array of [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `guest_os_type_not` | [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `guest_os_type_not_in` | Array of [VmGuestsOperationSystem](../Vm/VmGuestsOperationSystem.md) | No |  |
| `guest_size_usage` | number (double) | No |  |
| `guest_size_usage_gt` | number (double) | No |  |
| `guest_size_usage_gte` | number (double) | No |  |
| `guest_size_usage_in` | number[] | No |  |
| `guest_size_usage_lt` | number (double) | No |  |
| `guest_size_usage_lte` | number (double) | No |  |
| `guest_size_usage_not` | number (double) | No |  |
| `guest_size_usage_not_in` | number[] | No |  |
| `guest_used_size` | integer (int64) | No |  |
| `guest_used_size_gt` | integer (int64) | No |  |
| `guest_used_size_gte` | integer (int64) | No |  |
| `guest_used_size_in` | integer[] | No |  |
| `guest_used_size_lt` | integer (int64) | No |  |
| `guest_used_size_lte` | integer (int64) | No |  |
| `guest_used_size_not` | integer (int64) | No |  |
| `guest_used_size_not_in` | integer[] | No |  |
| `ha` | boolean | No |  |
| `ha_not` | boolean | No |  |
| `ha_priority` | [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `ha_priority_in` | Array of [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `ha_priority_not` | [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `ha_priority_not_in` | Array of [VmHaPriority](../Vm/VmHaPriority.md) | No |  |
| `host` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `hostname` | string | No |  |
| `hostname_contains` | string | No |  |
| `hostname_ends_with` | string | No |  |
| `hostname_gt` | string | No |  |
| `hostname_gte` | string | No |  |
| `hostname_in` | string[] | No |  |
| `hostname_lt` | string | No |  |
| `hostname_lte` | string | No |  |
| `hostname_not` | string | No |  |
| `hostname_not_contains` | string | No |  |
| `hostname_not_ends_with` | string | No |  |
| `hostname_not_in` | string[] | No |  |
| `hostname_not_starts_with` | string | No |  |
| `hostname_starts_with` | string | No |  |
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
| `in_recycle_bin` | boolean | No |  |
| `in_recycle_bin_not` | boolean | No |  |
| `internal` | boolean | No |  |
| `internal_not` | boolean | No |  |
| `internal_product` | string | No |  |
| `internal_product_contains` | string | No |  |
| `internal_product_ends_with` | string | No |  |
| `internal_product_gt` | string | No |  |
| `internal_product_gte` | string | No |  |
| `internal_product_in` | string[] | No |  |
| `internal_product_lt` | string | No |  |
| `internal_product_lte` | string | No |  |
| `internal_product_name` | string | No |  |
| `internal_product_name_contains` | string | No |  |
| `internal_product_name_ends_with` | string | No |  |
| `internal_product_name_gt` | string | No |  |
| `internal_product_name_gte` | string | No |  |
| `internal_product_name_in` | string[] | No |  |
| `internal_product_name_lt` | string | No |  |
| `internal_product_name_lte` | string | No |  |
| `internal_product_name_not` | string | No |  |
| `internal_product_name_not_contains` | string | No |  |
| `internal_product_name_not_ends_with` | string | No |  |
| `internal_product_name_not_in` | string[] | No |  |
| `internal_product_name_not_starts_with` | string | No |  |
| `internal_product_name_starts_with` | string | No |  |
| `internal_product_not` | string | No |  |
| `internal_product_not_contains` | string | No |  |
| `internal_product_not_ends_with` | string | No |  |
| `internal_product_not_in` | string[] | No |  |
| `internal_product_not_starts_with` | string | No |  |
| `internal_product_starts_with` | string | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `io_policy_in` | Array of [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `io_policy_not` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `io_policy_not_in` | Array of [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `ips` | string | No |  |
| `ips_contains` | string | No |  |
| `ips_ends_with` | string | No |  |
| `ips_gt` | string | No |  |
| `ips_gte` | string | No |  |
| `ips_in` | string[] | No |  |
| `ips_lt` | string | No |  |
| `ips_lte` | string | No |  |
| `ips_not` | string | No |  |
| `ips_not_contains` | string | No |  |
| `ips_not_ends_with` | string | No |  |
| `ips_not_in` | string[] | No |  |
| `ips_not_starts_with` | string | No |  |
| `ips_starts_with` | string | No |  |
| `isolation_policy` | [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `kernel_info` | string | No |  |
| `kernel_info_contains` | string | No |  |
| `kernel_info_ends_with` | string | No |  |
| `kernel_info_gt` | string | No |  |
| `kernel_info_gte` | string | No |  |
| `kernel_info_in` | string[] | No |  |
| `kernel_info_lt` | string | No |  |
| `kernel_info_lte` | string | No |  |
| `kernel_info_not` | string | No |  |
| `kernel_info_not_contains` | string | No |  |
| `kernel_info_not_ends_with` | string | No |  |
| `kernel_info_not_in` | string[] | No |  |
| `kernel_info_not_starts_with` | string | No |  |
| `kernel_info_starts_with` | string | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `last_shutdown_time` | string | No |  |
| `last_shutdown_time_gt` | string | No |  |
| `last_shutdown_time_gte` | string | No |  |
| `last_shutdown_time_in` | string[] | No |  |
| `last_shutdown_time_lt` | string | No |  |
| `last_shutdown_time_lte` | string | No |  |
| `last_shutdown_time_not` | string | No |  |
| `last_shutdown_time_not_in` | string[] | No |  |
| `local_created_at` | string | No |  |
| `local_created_at_gt` | string | No |  |
| `local_created_at_gte` | string | No |  |
| `local_created_at_in` | string[] | No |  |
| `local_created_at_lt` | string | No |  |
| `local_created_at_lte` | string | No |  |
| `local_created_at_not` | string | No |  |
| `local_created_at_not_in` | string[] | No |  |
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
| `logical_size_bytes` | integer (int64) | No |  |
| `logical_size_bytes_gt` | integer (int64) | No |  |
| `logical_size_bytes_gte` | integer (int64) | No |  |
| `logical_size_bytes_in` | integer[] | No |  |
| `logical_size_bytes_lt` | integer (int64) | No |  |
| `logical_size_bytes_lte` | integer (int64) | No |  |
| `logical_size_bytes_not` | integer (int64) | No |  |
| `logical_size_bytes_not_in` | integer[] | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_gt` | integer (int64) | No |  |
| `max_bandwidth_gte` | integer (int64) | No |  |
| `max_bandwidth_in` | integer[] | No |  |
| `max_bandwidth_lt` | integer (int64) | No |  |
| `max_bandwidth_lte` | integer (int64) | No |  |
| `max_bandwidth_not` | integer (int64) | No |  |
| `max_bandwidth_not_in` | integer[] | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_policy_in` | Array of [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_policy_not` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_policy_not_in` | Array of [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_gt` | integer (int32) | No |  |
| `max_iops_gte` | integer (int32) | No |  |
| `max_iops_in` | integer[] | No |  |
| `max_iops_lt` | integer (int32) | No |  |
| `max_iops_lte` | integer (int32) | No |  |
| `max_iops_not` | integer (int32) | No |  |
| `max_iops_not_in` | integer[] | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops_policy_in` | Array of [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops_policy_not` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops_policy_not_in` | Array of [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `memory` | integer (int64) | No |  |
| `memory_gt` | integer (int64) | No |  |
| `memory_gte` | integer (int64) | No |  |
| `memory_in` | integer[] | No |  |
| `memory_lt` | integer (int64) | No |  |
| `memory_lte` | integer (int64) | No |  |
| `memory_not` | integer (int64) | No |  |
| `memory_not_in` | integer[] | No |  |
| `memory_usage` | number (double) | No |  |
| `memory_usage_gt` | number (double) | No |  |
| `memory_usage_gte` | number (double) | No |  |
| `memory_usage_in` | number[] | No |  |
| `memory_usage_lt` | number (double) | No |  |
| `memory_usage_lte` | number (double) | No |  |
| `memory_usage_not` | number (double) | No |  |
| `memory_usage_not_in` | number[] | No |  |
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
| `nested_virtualization` | boolean | No |  |
| `nested_virtualization_not` | boolean | No |  |
| `node_ip` | string | No |  |
| `node_ip_contains` | string | No |  |
| `node_ip_ends_with` | string | No |  |
| `node_ip_gt` | string | No |  |
| `node_ip_gte` | string | No |  |
| `node_ip_in` | string[] | No |  |
| `node_ip_lt` | string | No |  |
| `node_ip_lte` | string | No |  |
| `node_ip_not` | string | No |  |
| `node_ip_not_contains` | string | No |  |
| `node_ip_not_ends_with` | string | No |  |
| `node_ip_not_in` | string[] | No |  |
| `node_ip_not_starts_with` | string | No |  |
| `node_ip_starts_with` | string | No |  |
| `original_name` | string | No |  |
| `original_name_contains` | string | No |  |
| `original_name_ends_with` | string | No |  |
| `original_name_gt` | string | No |  |
| `original_name_gte` | string | No |  |
| `original_name_in` | string[] | No |  |
| `original_name_lt` | string | No |  |
| `original_name_lte` | string | No |  |
| `original_name_not` | string | No |  |
| `original_name_not_contains` | string | No |  |
| `original_name_not_ends_with` | string | No |  |
| `original_name_not_in` | string[] | No |  |
| `original_name_not_starts_with` | string | No |  |
| `original_name_starts_with` | string | No |  |
| `os` | string | No |  |
| `os_contains` | string | No |  |
| `os_ends_with` | string | No |  |
| `os_gt` | string | No |  |
| `os_gte` | string | No |  |
| `os_in` | string[] | No |  |
| `os_lt` | string | No |  |
| `os_lte` | string | No |  |
| `os_not` | string | No |  |
| `os_not_contains` | string | No |  |
| `os_not_ends_with` | string | No |  |
| `os_not_in` | string[] | No |  |
| `os_not_starts_with` | string | No |  |
| `os_starts_with` | string | No |  |
| `pci_nics_every` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `pci_nics_none` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `pci_nics_some` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `protected` | boolean | No |  |
| `protected_not` | boolean | No |  |
| `provisioned_size` | integer (int64) | No |  |
| `provisioned_size_gt` | integer (int64) | No |  |
| `provisioned_size_gte` | integer (int64) | No |  |
| `provisioned_size_in` | integer[] | No |  |
| `provisioned_size_lt` | integer (int64) | No |  |
| `provisioned_size_lte` | integer (int64) | No |  |
| `provisioned_size_not` | integer (int64) | No |  |
| `provisioned_size_not_in` | integer[] | No |  |
| `size` | integer (int64) | No |  |
| `size_gt` | integer (int64) | No |  |
| `size_gte` | integer (int64) | No |  |
| `size_in` | integer[] | No |  |
| `size_lt` | integer (int64) | No |  |
| `size_lte` | integer (int64) | No |  |
| `size_not` | integer (int64) | No |  |
| `size_not_in` | integer[] | No |  |
| `snapshot_plan` | [SnapshotPlanWhereInput](../Snapshot/SnapshotPlanWhereInput.md) | No |  |
| `snapshots_every` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `snapshots_none` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `snapshots_some` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `status` | [VmStatus](../Vm/VmStatus.md) | No |  |
| `status_in` | Array of [VmStatus](../Vm/VmStatus.md) | No |  |
| `status_not` | [VmStatus](../Vm/VmStatus.md) | No |  |
| `status_not_in` | Array of [VmStatus](../Vm/VmStatus.md) | No |  |
| `unique_logical_size` | number (double) | No |  |
| `unique_logical_size_gt` | number (double) | No |  |
| `unique_logical_size_gte` | number (double) | No |  |
| `unique_logical_size_in` | number[] | No |  |
| `unique_logical_size_lt` | number (double) | No |  |
| `unique_logical_size_lte` | number (double) | No |  |
| `unique_logical_size_not` | number (double) | No |  |
| `unique_logical_size_not_in` | number[] | No |  |
| `unique_size` | integer (int64) | No |  |
| `unique_size_gt` | integer (int64) | No |  |
| `unique_size_gte` | integer (int64) | No |  |
| `unique_size_in` | integer[] | No |  |
| `unique_size_lt` | integer (int64) | No |  |
| `unique_size_lte` | integer (int64) | No |  |
| `unique_size_not` | integer (int64) | No |  |
| `unique_size_not_in` | integer[] | No |  |
| `usb_devices_every` | [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | No |  |
| `usb_devices_none` | [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | No |  |
| `usb_devices_some` | [UsbDeviceWhereInput](../Usb/UsbDeviceWhereInput.md) | No |  |
| `used_size` | integer (int64) | No |  |
| `used_size_gt` | integer (int64) | No |  |
| `used_size_gte` | integer (int64) | No |  |
| `used_size_in` | integer[] | No |  |
| `used_size_lt` | integer (int64) | No |  |
| `used_size_lte` | integer (int64) | No |  |
| `used_size_not` | integer (int64) | No |  |
| `used_size_not_in` | integer[] | No |  |
| `used_size_usage` | number (double) | No |  |
| `used_size_usage_gt` | number (double) | No |  |
| `used_size_usage_gte` | number (double) | No |  |
| `used_size_usage_in` | number[] | No |  |
| `used_size_usage_lt` | number (double) | No |  |
| `used_size_usage_lte` | number (double) | No |  |
| `used_size_usage_not` | number (double) | No |  |
| `used_size_usage_not_in` | number[] | No |  |
| `vcpu` | integer (int32) | No |  |
| `vcpu_gt` | integer (int32) | No |  |
| `vcpu_gte` | integer (int32) | No |  |
| `vcpu_in` | integer[] | No |  |
| `vcpu_lt` | integer (int32) | No |  |
| `vcpu_lte` | integer (int32) | No |  |
| `vcpu_not` | integer (int32) | No |  |
| `vcpu_not_in` | integer[] | No |  |
| `video_type` | [VmVideoType](../Vm/VmVideoType.md) | No |  |
| `video_type_in` | Array of [VmVideoType](../Vm/VmVideoType.md) | No |  |
| `video_type_not` | [VmVideoType](../Vm/VmVideoType.md) | No |  |
| `video_type_not_in` | Array of [VmVideoType](../Vm/VmVideoType.md) | No |  |
| `vm_disks_every` | [VmDiskWhereInput](../Vm/VmDiskWhereInput.md) | No |  |
| `vm_disks_none` | [VmDiskWhereInput](../Vm/VmDiskWhereInput.md) | No |  |
| `vm_disks_some` | [VmDiskWhereInput](../Vm/VmDiskWhereInput.md) | No |  |
| `vm_nics_every` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vm_nics_none` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vm_nics_some` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `vm_placement_group_every` | [VmPlacementGroupWhereInput](../Vm/VmPlacementGroupWhereInput.md) | No |  |
| `vm_placement_group_none` | [VmPlacementGroupWhereInput](../Vm/VmPlacementGroupWhereInput.md) | No |  |
| `vm_placement_group_some` | [VmPlacementGroupWhereInput](../Vm/VmPlacementGroupWhereInput.md) | No |  |
| `vm_tools_status` | [VmToolsStatus](../Vm/VmToolsStatus.md) | No |  |
| `vm_tools_status_in` | Array of [VmToolsStatus](../Vm/VmToolsStatus.md) | No |  |
| `vm_tools_status_not` | [VmToolsStatus](../Vm/VmToolsStatus.md) | No |  |
| `vm_tools_status_not_in` | Array of [VmToolsStatus](../Vm/VmToolsStatus.md) | No |  |
| `vm_tools_version` | string | No |  |
| `vm_tools_version_contains` | string | No |  |
| `vm_tools_version_ends_with` | string | No |  |
| `vm_tools_version_gt` | string | No |  |
| `vm_tools_version_gte` | string | No |  |
| `vm_tools_version_in` | string[] | No |  |
| `vm_tools_version_lt` | string | No |  |
| `vm_tools_version_lte` | string | No |  |
| `vm_tools_version_not` | string | No |  |
| `vm_tools_version_not_contains` | string | No |  |
| `vm_tools_version_not_ends_with` | string | No |  |
| `vm_tools_version_not_in` | string[] | No |  |
| `vm_tools_version_not_starts_with` | string | No |  |
| `vm_tools_version_starts_with` | string | No |  |
| `vm_usage` | [VmUsage](../Vm/VmUsage.md) | No |  |
| `vm_usage_in` | Array of [VmUsage](../Vm/VmUsage.md) | No |  |
| `vm_usage_not` | [VmUsage](../Vm/VmUsage.md) | No |  |
| `vm_usage_not_in` | Array of [VmUsage](../Vm/VmUsage.md) | No |  |
| `win_opt` | boolean | No |  |
| `win_opt_not` | boolean | No |  |

