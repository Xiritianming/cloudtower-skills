# ContentLibraryVmTemplateImportParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes |  |
| `upload_tasks` | string[] | Yes |  |
| `parsed_ovf` | [ParsedOVF](../Parsed/ParsedOVF.md) | Yes |  |
| `cluster_id` | string | Yes |  |
| `vm_nics` | Array of [ContentLibraryImportVmNic](../Content/ContentLibraryImportVmNic.md) | No |  |
| `disk_operate` | [ContentLibraryVmTemplateOvfDiskOperate](../Content/ContentLibraryVmTemplateOvfDiskOperate.md) | No |  |
| `ha` | boolean | No |  |
| `memory_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `memory` | integer (int64) | No |  |
| `vcpu` | integer (int32) | No |  |
| `cpu_cores` | integer (int32) | No |  |
| `cpu_sockets` | integer (int32) | No |  |
| `description` | string | No |  |

