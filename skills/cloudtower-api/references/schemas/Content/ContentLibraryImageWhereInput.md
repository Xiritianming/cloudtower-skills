# ContentLibraryImageWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ContentLibraryImageWhereInput](../Content/ContentLibraryImageWhereInput.md) | No |  |
| `NOT` | Array of [ContentLibraryImageWhereInput](../Content/ContentLibraryImageWhereInput.md) | No |  |
| `OR` | Array of [ContentLibraryImageWhereInput](../Content/ContentLibraryImageWhereInput.md) | No |  |
| `clusters_every` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `clusters_none` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `clusters_some` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
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
| `elf_images_every` | [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
| `elf_images_none` | [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
| `elf_images_some` | [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
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
| `iscsi_luns_every` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `iscsi_luns_none` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `iscsi_luns_some` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
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

