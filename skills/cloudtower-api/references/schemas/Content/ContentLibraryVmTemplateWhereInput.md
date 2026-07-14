# ContentLibraryVmTemplateWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ContentLibraryVmTemplateWhereInput](../Content/ContentLibraryVmTemplateWhereInput.md) | No |  |
| `NOT` | Array of [ContentLibraryVmTemplateWhereInput](../Content/ContentLibraryVmTemplateWhereInput.md) | No |  |
| `OR` | Array of [ContentLibraryVmTemplateWhereInput](../Content/ContentLibraryVmTemplateWhereInput.md) | No |  |
| `architecture` | [Architecture](../Architecture/Architecture.md) | No |  |
| `architecture_in` | Array of [Architecture](../Architecture/Architecture.md) | No |  |
| `architecture_not` | [Architecture](../Architecture/Architecture.md) | No |  |
| `architecture_not_in` | Array of [Architecture](../Architecture/Architecture.md) | No |  |
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clock_offset_in` | Array of [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clock_offset_not` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clock_offset_not_in` | Array of [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `cloud_init_supported` | boolean | No |  |
| `cloud_init_supported_not` | boolean | No |  |
| `clusters_every` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `clusters_none` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `clusters_some` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
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
| `createdAt` | string | No |  |
| `createdAt_gt` | string | No |  |
| `createdAt_gte` | string | No |  |
| `createdAt_in` | string[] | No |  |
| `createdAt_lt` | string | No |  |
| `createdAt_lte` | string | No |  |
| `createdAt_not` | string | No |  |
| `createdAt_not_in` | string[] | No |  |
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
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `firmware_in` | Array of [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `firmware_not` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `firmware_not_in` | Array of [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `ha` | boolean | No |  |
| `ha_not` | boolean | No |  |
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
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `io_policy_in` | Array of [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `io_policy_not` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `io_policy_not_in` | Array of [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
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
| `size` | integer (int64) | No |  |
| `size_gt` | integer (int64) | No |  |
| `size_gte` | integer (int64) | No |  |
| `size_in` | integer[] | No |  |
| `size_lt` | integer (int64) | No |  |
| `size_lte` | integer (int64) | No |  |
| `size_not` | integer (int64) | No |  |
| `size_not_in` | integer[] | No |  |
| `usage` | [ContentLibraryVmTemplateUsage](../Content/ContentLibraryVmTemplateUsage.md) | No |  |
| `usage_in` | Array of [ContentLibraryVmTemplateUsage](../Content/ContentLibraryVmTemplateUsage.md) | No |  |
| `usage_not` | [ContentLibraryVmTemplateUsage](../Content/ContentLibraryVmTemplateUsage.md) | No |  |
| `usage_not_in` | Array of [ContentLibraryVmTemplateUsage](../Content/ContentLibraryVmTemplateUsage.md) | No |  |
| `vcpu` | integer (int32) | No |  |
| `vcpu_gt` | integer (int32) | No |  |
| `vcpu_gte` | integer (int32) | No |  |
| `vcpu_in` | integer[] | No |  |
| `vcpu_lt` | integer (int32) | No |  |
| `vcpu_lte` | integer (int32) | No |  |
| `vcpu_not` | integer (int32) | No |  |
| `vcpu_not_in` | integer[] | No |  |
| `video_type` | string | No |  |
| `video_type_contains` | string | No |  |
| `video_type_ends_with` | string | No |  |
| `video_type_gt` | string | No |  |
| `video_type_gte` | string | No |  |
| `video_type_in` | string[] | No |  |
| `video_type_lt` | string | No |  |
| `video_type_lte` | string | No |  |
| `video_type_not` | string | No |  |
| `video_type_not_contains` | string | No |  |
| `video_type_not_ends_with` | string | No |  |
| `video_type_not_in` | string[] | No |  |
| `video_type_not_starts_with` | string | No |  |
| `video_type_starts_with` | string | No |  |
| `vm_templates_every` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_templates_none` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_templates_some` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `win_opt` | boolean | No |  |
| `win_opt_not` | boolean | No |  |

