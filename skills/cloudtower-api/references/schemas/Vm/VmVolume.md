# VmVolume

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | Yes |  |
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `mounting` | boolean | Yes |  |
| `name` | string | Yes |  |
| `path` | string | Yes |  |
| `sharing` | boolean | Yes |  |
| `size` | integer (int64) | Yes |  |
| `description` | string | No |  |
| `elf_storage_policy_ec_k` | integer (int32) | No |  |
| `elf_storage_policy_ec_m` | integer (int32) | No |  |
| `elf_storage_policy_replica_num` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num` | integer (int32) | No |  |
| `elf_storage_policy_thin_provision` | boolean | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `guest_size_usage` | number (double) | No |  |
| `guest_used_size` | integer (int64) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `lun` | [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `resident_in_cache` | boolean | No |  |
| `type` | [VmVolumeType](../Vm/VmVolumeType.md) | No |  |
| `unique_logical_size` | number (double) | No |  |
| `unique_size` | integer (int64) | No |  |
| `used_size` | integer (int64) | No |  |
| `used_size_usage` | number (double) | No |  |
| `vm_disks` | Array of [NestedVmDisk](../Nested/NestedVmDisk.md) | No |  |

