# VmExportFile

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `createdAt` | string | Yes |  |
| `damaged` | boolean | Yes |  |
| `data_port_id` | string | Yes |  |
| `files` | Array of [VmExportFileFile](../Vm/VmExportFileFile.md) | Yes |  |
| `id` | string | Yes |  |
| `storage_cluster_id` | string | Yes |  |
| `type` | [VmExportFileType](../Vm/VmExportFileType.md) | Yes |  |
| `content_library_vm_template` | [NestedContentLibraryVmTemplate](../Nested/NestedContentLibraryVmTemplate.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | No |  |
| `vm_volume` | [NestedVmVolume](../Nested/NestedVmVolume.md) | No |  |

