# VmUpdateDiskParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VmWhereInput](../Vm/VmWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_disk_id` | string | Yes |  |
| `content_library_image_id` | string | No |  |
| `elf_image_id` | string | No |  |
| `vm_volume_id` | string | No |  |
| `bus` | [Bus](../Bus/Bus.md) | No |  |

