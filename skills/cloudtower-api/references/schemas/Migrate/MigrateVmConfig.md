# MigrateVmConfig

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `network_mapping` | Array of [VlanMapping](../Vlan/VlanMapping.md) | Yes |  |
| `migrate_type` | [MigrateType](../Migrate/MigrateType.md) | Yes |  |
| `remove_unmovable_devices` | boolean | No |  |
| `new_name` | string | No |  |
| `elf_ec_storage_policy` | object | No |  |
| `elf_replica_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `delete_src_vm` | boolean | No |  |

## Nested Fields

### `elf_ec_storage_policy`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `thin_provision` | boolean | No |  |
| `ec_m` | integer (int32) | No |  |
| `ec_k` | integer (int32) | No |  |

