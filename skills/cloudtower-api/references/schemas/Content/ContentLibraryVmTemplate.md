# ContentLibraryVmTemplate

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `architecture` | [Architecture](../Architecture/Architecture.md) | Yes |  |
| `cloud_init_supported` | boolean | Yes |  |
| `createdAt` | string | Yes |  |
| `description` | string | Yes |  |
| `id` | string | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `name` | string | Yes |  |
| `size` | integer (int64) | Yes |  |
| `vcpu` | integer (int32) | Yes |  |
| `vm_template_uuids` | string[] | Yes |  |
| `clock_offset` | [VmClockOffset](../Vm/VmClockOffset.md) | No |  |
| `clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `cpu` | [NestedCpu](../Nested/NestedCpu.md) | No |  |
| `cpu_model` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | No |  |
| `ha` | boolean | No |  |
| `io_policy` | [VmDiskIoPolicy](../Vm/VmDiskIoPolicy.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int32) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `os` | string | No |  |
| `template_config` | [NestedTemplateConfig](../Nested/NestedTemplateConfig.md) | No |  |
| `usage` | [ContentLibraryVmTemplateUsage](../Content/ContentLibraryVmTemplateUsage.md) | No |  |
| `video_type` | string | No |  |
| `vm_disks` | Array of [NestedContentLibraryVmTemplateDisk](../Nested/NestedContentLibraryVmTemplateDisk.md) | No |  |
| `vm_nics` | Array of [NestedContentLibraryVmTemplateNic](../Nested/NestedContentLibraryVmTemplateNic.md) | No |  |
| `vm_templates` | Array of [NestedVmTemplate](../Nested/NestedVmTemplate.md) | No |  |
| `win_opt` | boolean | No |  |
| `zbs_storage_info` | Array of [NestedZbsStorageInfo](../Nested/NestedZbsStorageInfo.md) | No |  |

