# ElfImageWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
| `NOT` | Array of [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
| `OR` | Array of [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `content_library_image` | [ContentLibraryImageWhereInput](../Content/ContentLibraryImageWhereInput.md) | No |  |
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
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
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
| `path` | string | No |  |
| `path_contains` | string | No |  |
| `path_ends_with` | string | No |  |
| `path_gt` | string | No |  |
| `path_gte` | string | No |  |
| `path_in` | string[] | No |  |
| `path_lt` | string | No |  |
| `path_lte` | string | No |  |
| `path_not` | string | No |  |
| `path_not_contains` | string | No |  |
| `path_not_ends_with` | string | No |  |
| `path_not_in` | string[] | No |  |
| `path_not_starts_with` | string | No |  |
| `path_starts_with` | string | No |  |
| `size` | integer (int64) | No |  |
| `size_gt` | integer (int64) | No |  |
| `size_gte` | integer (int64) | No |  |
| `size_in` | integer[] | No |  |
| `size_lt` | integer (int64) | No |  |
| `size_lte` | integer (int64) | No |  |
| `size_not` | integer (int64) | No |  |
| `size_not_in` | integer[] | No |  |
| `vm_disks_every` | [VmDiskWhereInput](../Vm/VmDiskWhereInput.md) | No |  |
| `vm_disks_none` | [VmDiskWhereInput](../Vm/VmDiskWhereInput.md) | No |  |
| `vm_disks_some` | [VmDiskWhereInput](../Vm/VmDiskWhereInput.md) | No |  |
| `vm_snapshots_every` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `vm_snapshots_none` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `vm_snapshots_some` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `vm_templates_every` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_templates_none` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_templates_some` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |

