# ContentLibraryImage

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `createdAt` | string | Yes |  |
| `description` | string | Yes |  |
| `elf_image_uuids` | string[] | Yes |  |
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `path` | string | Yes |  |
| `size` | integer (int64) | Yes |  |
| `clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `elf_images` | Array of [NestedElfImage](../Nested/NestedElfImage.md) | No |  |
| `entityAsyncStatus` | any | No |  |
| `iscsi_luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `vm_disks` | Array of [NestedVmDisk](../Nested/NestedVmDisk.md) | No |  |
| `vm_snapshots` | Array of [NestedVmSnapshot](../Nested/NestedVmSnapshot.md) | No |  |
| `vm_templates` | Array of [NestedVmTemplate](../Nested/NestedVmTemplate.md) | No |  |

