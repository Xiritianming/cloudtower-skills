# VmdkDiskModify

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vmdk_name` | string | Yes |  |
| `elf_ec_storage_policy` | object | No |  |
| `elf_replica_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `bus` | [Bus](../Bus/Bus.md) | No |  |
| `volume_name` | string | No |  |
| `boot` | integer (int32) | No |  |

## Nested Fields

### `elf_ec_storage_policy`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `thin_provision` | boolean | No |  |
| `ec_m` | integer (int32) | No |  |
| `ec_k` | integer (int32) | No |  |

