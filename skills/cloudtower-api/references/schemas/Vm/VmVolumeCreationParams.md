# VmVolumeCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `size` | integer (int64) | Yes |  |
| `sharing` | boolean | Yes |  |
| `cluster_id` | string | Yes |  |
| `name` | string | Yes |  |
| `resident_in_cache` | boolean | No |  |
| `elf_ec_storage_policy` | object | No |  |
| `elf_replica_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `size_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |

## Nested Fields

### `elf_ec_storage_policy`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `thin_provision` | boolean | No |  |
| `ec_m` | integer (int32) | No |  |
| `ec_k` | integer (int32) | No |  |

