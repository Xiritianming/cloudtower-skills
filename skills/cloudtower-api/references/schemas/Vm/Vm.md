# Vm

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | Yes |  |
| `cpu` | [NestedCpu](../Nested/NestedCpu.md) | Yes |  |
| `cpu_model` | string | Yes |  |
| `description` | string | Yes |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | Yes |  |
| `ha` | boolean | Yes |  |
| `id` | string | Yes |  |
| `in_recycle_bin` | boolean | Yes |  |
| `internal` | boolean | Yes |  |
| `ips` | string | Yes |  |
| `local_id` | string | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `name` | string | Yes |  |
| `nested_virtualization` | boolean | Yes |  |
| `node_ip` | string | Yes |  |
| `out_uninstall_usb` | string[] | Yes |  |
| `protected` | boolean | Yes |  |
| `status` | [VmStatus](../Vm/VmStatus.md) | Yes |  |
| `vcpu` | integer (int32) | Yes |  |
| `vm_tools_status` | [VmToolsStatus](../Vm/VmToolsStatus.md) | Yes |  |
| `win_opt` | boolean | Yes |  |
| `anti_malware_enabled` | boolean | No |  |
| `backup_plans` | Array of [NestedBackupPlan](../Nested/NestedBackupPlan.md) | No |  |
| `bios_uuid` | string | No |  |
| `cloud_init_supported` | boolean | No |  |
| `cluster` | any | No |  |
| `cpu_usage` | number (double) | No |  |
| `deleted_at` | string | No |  |
| `dns_servers` | string | No |  |
| `dpi_enabled` | boolean | No |  |
| `entityAsyncStatus` | any | No |  |
| `entity_filter_results` | Array of [NestedVmEntityFilterResult](../Nested/NestedVmEntityFilterResult.md) | No |  |
| `folder` | any | No |  |
| `gpu_devices` | Array of [NestedGpuDevice](../Nested/NestedGpuDevice.md) | No |  |
| `guest_cpu_model` | string | No |  |
| `guest_os_type` | any | No |  |
| `guest_size_usage` | number (double) | No |  |
| `guest_used_size` | integer (int64) | No |  |
| `ha_priority` | any | No |  |
| `host` | any | No |  |
| `hostname` | string | No |  |
| `internal_product` | string | No |  |
| `internal_product_name` | string | No |  |
| `io_policy` | any | No |  |
| `isolation_policy` | any | No |  |
| `kernel_info` | string | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `last_shutdown_time` | string | No |  |
| `local_created_at` | string | No |  |
| `logical_size_bytes` | integer (int64) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | any | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | any | No |  |
| `memory_usage` | number (double) | No |  |
| `original_name` | string | No |  |
| `os` | string | No |  |
| `pci_nics` | Array of [NestedNic](../Nested/NestedNic.md) | No |  |
| `provisioned_size` | integer (int64) | No |  |
| `size` | integer (int64) | No |  |
| `snapshot_plan` | any | No |  |
| `snapshots` | Array of [NestedVmSnapshot](../Nested/NestedVmSnapshot.md) | No |  |
| `unique_logical_size` | number (double) | No |  |
| `unique_size` | integer (int64) | No |  |
| `usb_devices` | Array of [NestedUsbDevice](../Nested/NestedUsbDevice.md) | No |  |
| `used_size` | integer (int64) | No |  |
| `used_size_usage` | number (double) | No |  |
| `video_type` | any | No |  |
| `vm_disks` | Array of [NestedVmDisk](../Nested/NestedVmDisk.md) | No |  |
| `vm_nics` | Array of [NestedVmNic](../Nested/NestedVmNic.md) | No |  |
| `vm_placement_group` | Array of [NestedVmPlacementGroup](../Nested/NestedVmPlacementGroup.md) | No |  |
| `vm_tools_version` | string | No |  |
| `vm_usage` | any | No |  |

