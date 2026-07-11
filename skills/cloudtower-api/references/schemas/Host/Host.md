# Host

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allocatable_memory_bytes` | integer (int64) | Yes |  |
| `chunk_id` | string | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `compatible_cpu_models` | string[] | Yes |  |
| `cpu_brand` | string | Yes |  |
| `cpu_fan_speed` | number[] | Yes |  |
| `cpu_hz_per_core` | integer (int64) | Yes |  |
| `cpu_model` | string | Yes |  |
| `cpu_temperature_celsius` | integer[] | Yes |  |
| `failure_data_space` | integer (int64) | Yes |  |
| `hdd_data_capacity` | integer (int64) | Yes |  |
| `hdd_disk_count` | integer (int32) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `lsm_cap_disk_safe_umount` | boolean | Yes |  |
| `management_ip` | string | Yes |  |
| `model` | string | Yes |  |
| `name` | string | Yes |  |
| `nested_virtualization` | boolean | Yes |  |
| `nic_count` | integer (int32) | Yes |  |
| `os_memory_bytes` | integer (int64) | Yes |  |
| `pmem_dimm_capacity` | integer (int64) | Yes |  |
| `pmem_dimm_count` | integer (int32) | Yes |  |
| `pmem_disk_count` | integer (int32) | Yes |  |
| `provisioned_cpu_cores` | integer (int32) | Yes |  |
| `provisioned_memory_bytes` | integer (int64) | Yes |  |
| `running_pause_vm_memory_bytes` | integer (int64) | Yes |  |
| `ssd_data_capacity` | integer (int64) | Yes |  |
| `ssd_disk_count` | integer (int32) | Yes |  |
| `state` | [HostState](../Host/HostState.md) | Yes |  |
| `status` | [HostStatus](../Host/HostStatus.md) | Yes |  |
| `total_cpu_cores` | integer (int32) | Yes |  |
| `total_cpu_hz` | integer (int64) | Yes |  |
| `total_data_capacity` | integer (int64) | Yes |  |
| `total_memory_bytes` | integer (int64) | Yes |  |
| `used_data_space` | integer (int64) | Yes |  |
| `access_ip` | string | No |  |
| `allocable_cpu_cores_for_vm_exclusive` | integer (int32) | No |  |
| `allocated_prioritized_space` | integer (int64) | No |  |
| `allocated_prioritized_space_usage` | number (double) | No |  |
| `commited_memory_bytes` | integer (int64) | No |  |
| `connect_status` | any | No |  |
| `cpu_fan_speed_unit` | any | No |  |
| `cpu_vendor` | string | No |  |
| `data_ip` | string | No |  |
| `dirty_cache_space` | integer (int64) | No |  |
| `dirty_cache_usage` | number (double) | No |  |
| `disk_pools` | Array of [NestedDiskPool](../Nested/NestedDiskPool.md) | No |  |
| `disks` | Array of [NestedDisk](../Nested/NestedDisk.md) | No |  |
| `downgraded_prioritized_space` | integer (int64) | No |  |
| `entityAsyncStatus` | any | No |  |
| `failure_cache_space` | integer (int64) | No |  |
| `gpu_devices` | Array of [NestedGpuDevice](../Nested/NestedGpuDevice.md) | No |  |
| `host_state` | any | No |  |
| `hypervisor_ip` | string | No |  |
| `iommu` | any | No |  |
| `ipmi` | any | No |  |
| `is_os_in_raid1` | boolean | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `merged_status` | any | No |  |
| `nics` | Array of [NestedNic](../Nested/NestedNic.md) | No |  |
| `node_topo_local_id` | string | No |  |
| `os_version` | string | No |  |
| `perf_allocated_data_space` | integer (int64) | No |  |
| `perf_failure_data_space` | integer (int64) | No |  |
| `perf_total_data_capacity` | integer (int64) | No |  |
| `perf_used_data_space` | integer (int64) | No |  |
| `perf_valid_data_space` | integer (int64) | No |  |
| `planned_prioritized_space` | integer (int64) | No |  |
| `pmem_dimms` | Array of [NestedPmemDimm](../Nested/NestedPmemDimm.md) | No |  |
| `prio_space_percentage` | number (double) | No |  |
| `running_vm_num` | integer (int32) | No |  |
| `scvm_cpu` | integer (int32) | No |  |
| `scvm_memory` | integer (int64) | No |  |
| `scvm_name` | string | No |  |
| `serial` | string | No |  |
| `stopped_vm_num` | integer (int32) | No |  |
| `suspended_vm_num` | integer (int32) | No |  |
| `total_cache_capacity` | integer (int64) | No |  |
| `total_cpu_sockets` | integer (int32) | No |  |
| `usb_devices` | Array of [NestedUsbDevice](../Nested/NestedUsbDevice.md) | No |  |
| `used_cache_space` | integer (int64) | No |  |
| `used_cpu_hz` | number (double) | No |  |
| `used_memory_bytes` | number (double) | No |  |
| `valid_cache_space` | integer (int64) | No |  |
| `valid_free_cache_space` | integer (int64) | No |  |
| `vm_num` | integer (int32) | No |  |
| `vmotion_ip` | string | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |
| `vsphereEsxiAccount` | any | No |  |
| `with_faster_ssd_as_cache` | boolean | No |  |
| `zone` | any | No |  |

