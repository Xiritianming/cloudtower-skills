# MountNewCreateDisksParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_volume` | object | Yes |  |
| `bus` | [Bus](../Bus/Bus.md) | Yes |  |
| `boot` | integer (int32) | Yes |  |
| `max_bandwidth_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_bandwidth_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `max_bandwidth` | integer (int64) | No |  |
| `max_iops_policy` | [VmDiskIoRestrictType](../Vm/VmDiskIoRestrictType.md) | No |  |
| `max_iops` | integer (int64) | No |  |
| `index` | integer (int32) | No |  |
| `key` | integer (int32) | No |  |

## Nested Fields

### `vm_volume`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `size` | integer (int64) | Yes |  |
| `name` | string | Yes |  |
| `resident_in_cache` | boolean | No |  |
| `elf_ec_storage_policy` | object | No |  |
| `elf_replica_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `path` | string | No |  |
| `size_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |

#### `vm_volume.elf_ec_storage_policy`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `thin_provision` | boolean | No |  |
| `ec_m` | integer (int32) | No |  |
| `ec_k` | integer (int32) | No |  |

