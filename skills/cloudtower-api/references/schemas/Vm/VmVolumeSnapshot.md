# VmVolumeSnapshot

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | Yes |  |
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `type` | [VmVolumeSnapshotType](../Vm/VmVolumeSnapshotType.md) | Yes |  |
| `createAt` | string | No |  |
| `elf_storage_policy_ec_k` | integer (int32) | No |  |
| `elf_storage_policy_ec_m` | integer (int32) | No |  |
| `elf_storage_policy_replica_num` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num` | integer (int32) | No |  |
| `elf_storage_policy_thin_provision` | boolean | No |  |
| `entityAsyncStatus` | any | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `resident_in_cache` | boolean | No |  |
| `shared_size` | number (double) | No |  |
| `size` | number (double) | No |  |
| `unique_size` | number (double) | No |  |
| `vm_volume` | any | No |  |
| `volume_sharing` | boolean | No |  |
| `volume_size` | number (double) | No |  |
| `zbs_snapshot_uuid` | string | No |  |

