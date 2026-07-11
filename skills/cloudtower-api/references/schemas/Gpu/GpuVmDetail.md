# GpuVmDetail

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `win_opt` | boolean | Yes |  |
| `vm_tools_status` | [VmToolsStatus](../Vm/VmToolsStatus.md) | Yes |  |
| `vcpu` | integer (int32) | Yes |  |
| `status` | [VmStatus](../Vm/VmStatus.md) | Yes |  |
| `protected` | boolean | Yes |  |
| `out_uninstall_usb` | string[] | Yes |  |
| `node_ip` | string | Yes |  |
| `nested_virtualization` | boolean | Yes |  |
| `name` | string | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `local_id` | string | Yes |  |
| `ips` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `in_recycle_bin` | boolean | Yes |  |
| `id` | string | Yes |  |
| `ha` | boolean | Yes |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | Yes |  |
| `description` | string | Yes |  |
| `cpu_model` | string | Yes |  |
| `cpu` | [NestedCpu](../Nested/NestedCpu.md) | Yes |  |
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | Yes |  |
| `vgpu_instance_on_vm_num` | integer (int32) | No |  |
| `vm_usage` | any | No |  |
| `vm_tools_version` | string | No |  |
| `vm_placement_group` | Array of [NestedVmPlacementGroup](../Nested/NestedVmPlacementGroup.md) | No |  |
| `vm_nics` | Array of [NestedVmNic](../Nested/NestedVmNic.md) | No |  |
| `vm_disks` | Array of [NestedVmDisk](../Nested/NestedVmDisk.md) | No |  |
| `video_type` | any | No |  |
| `usb_devices` | Array of [NestedUsbDevice](../Nested/NestedUsbDevice.md) | No |  |
| `unique_size` | integer (int64) | No |  |
| `snapshots` | Array of [NestedVmSnapshot](../Nested/NestedVmSnapshot.md) | No |  |
| `snapshot_plan` | any | No |  |
| `size` | integer (int64) | No |  |
| `provisioned_size` | integer (int64) | No |  |
| `pci_nics` | Array of [NestedNic](../Nested/NestedNic.md) | No |  |
| `os` | string | No |  |
| `original_name` | string | No |  |
| `memory_usage` | number (double) | No |  |
| `max_iops_policy` | any | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_bandwidth_policy` | any | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `logical_size_bytes` | integer (int64) | No |  |
| `local_created_at` | string | No |  |
| `last_shutdown_time` | string | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `kernel_info` | string | No |  |
| `isolation_policy` | any | No |  |
| `io_policy` | any | No |  |
| `hostname` | string | No |  |
| `host` | any | No |  |
| `guest_used_size` | integer (int64) | No |  |
| `guest_size_usage` | number (double) | No |  |
| `guest_os_type` | any | No |  |
| `guest_cpu_model` | string | No |  |
| `gpu_devices` | Array of [NestedGpuDevice](../Nested/NestedGpuDevice.md) | No |  |
| `folder` | any | No |  |
| `entityAsyncStatus` | any | No |  |
| `entity_filter_results` | Array of [NestedVmEntityFilterResult](../Nested/NestedVmEntityFilterResult.md) | No |  |
| `dns_servers` | string | No |  |
| `deleted_at` | string | No |  |
| `cpu_usage` | number (double) | No |  |
| `cluster` | any | No |  |
| `cloud_init_supported` | boolean | No |  |

