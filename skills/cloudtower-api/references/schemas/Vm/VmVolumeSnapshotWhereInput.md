# VmVolumeSnapshotWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VmVolumeSnapshotWhereInput](../Vm/VmVolumeSnapshotWhereInput.md) | No |  |
| `NOT` | Array of [VmVolumeSnapshotWhereInput](../Vm/VmVolumeSnapshotWhereInput.md) | No |  |
| `OR` | Array of [VmVolumeSnapshotWhereInput](../Vm/VmVolumeSnapshotWhereInput.md) | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `createAt` | string | No |  |
| `createAt_gt` | string | No |  |
| `createAt_gte` | string | No |  |
| `createAt_in` | string[] | No |  |
| `createAt_lt` | string | No |  |
| `createAt_lte` | string | No |  |
| `createAt_not` | string | No |  |
| `createAt_not_in` | string[] | No |  |
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
| `elf_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy_ec_k` | integer (int32) | No |  |
| `elf_storage_policy_ec_k_gt` | integer (int32) | No |  |
| `elf_storage_policy_ec_k_gte` | integer (int32) | No |  |
| `elf_storage_policy_ec_k_in` | integer[] | No |  |
| `elf_storage_policy_ec_k_lt` | integer (int32) | No |  |
| `elf_storage_policy_ec_k_lte` | integer (int32) | No |  |
| `elf_storage_policy_ec_k_not` | integer (int32) | No |  |
| `elf_storage_policy_ec_k_not_in` | integer[] | No |  |
| `elf_storage_policy_ec_m` | integer (int32) | No |  |
| `elf_storage_policy_ec_m_gt` | integer (int32) | No |  |
| `elf_storage_policy_ec_m_gte` | integer (int32) | No |  |
| `elf_storage_policy_ec_m_in` | integer[] | No |  |
| `elf_storage_policy_ec_m_lt` | integer (int32) | No |  |
| `elf_storage_policy_ec_m_lte` | integer (int32) | No |  |
| `elf_storage_policy_ec_m_not` | integer (int32) | No |  |
| `elf_storage_policy_ec_m_not_in` | integer[] | No |  |
| `elf_storage_policy_in` | Array of [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy_not` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy_not_in` | Array of [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `elf_storage_policy_replica_num` | integer (int32) | No |  |
| `elf_storage_policy_replica_num_gt` | integer (int32) | No |  |
| `elf_storage_policy_replica_num_gte` | integer (int32) | No |  |
| `elf_storage_policy_replica_num_in` | integer[] | No |  |
| `elf_storage_policy_replica_num_lt` | integer (int32) | No |  |
| `elf_storage_policy_replica_num_lte` | integer (int32) | No |  |
| `elf_storage_policy_replica_num_not` | integer (int32) | No |  |
| `elf_storage_policy_replica_num_not_in` | integer[] | No |  |
| `elf_storage_policy_stripe_num` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num_gt` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num_gte` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num_in` | integer[] | No |  |
| `elf_storage_policy_stripe_num_lt` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num_lte` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num_not` | integer (int32) | No |  |
| `elf_storage_policy_stripe_num_not_in` | integer[] | No |  |
| `elf_storage_policy_thin_provision` | boolean | No |  |
| `elf_storage_policy_thin_provision_not` | boolean | No |  |
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
| `labels_every` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_none` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `labels_some` | [LabelWhereInput](../Label/LabelWhereInput.md) | No |  |
| `local_created_at` | string | No |  |
| `local_created_at_gt` | string | No |  |
| `local_created_at_gte` | string | No |  |
| `local_created_at_in` | string[] | No |  |
| `local_created_at_lt` | string | No |  |
| `local_created_at_lte` | string | No |  |
| `local_created_at_not` | string | No |  |
| `local_created_at_not_in` | string[] | No |  |
| `local_id` | string | No |  |
| `local_id_contains` | string | No |  |
| `local_id_ends_with` | string | No |  |
| `local_id_gt` | string | No |  |
| `local_id_gte` | string | No |  |
| `local_id_in` | string[] | No |  |
| `local_id_lt` | string | No |  |
| `local_id_lte` | string | No |  |
| `local_id_not` | string | No |  |
| `local_id_not_contains` | string | No |  |
| `local_id_not_ends_with` | string | No |  |
| `local_id_not_in` | string[] | No |  |
| `local_id_not_starts_with` | string | No |  |
| `local_id_starts_with` | string | No |  |
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
| `resident_in_cache` | boolean | No |  |
| `resident_in_cache_not` | boolean | No |  |
| `shared_size` | number (double) | No |  |
| `shared_size_gt` | number (double) | No |  |
| `shared_size_gte` | number (double) | No |  |
| `shared_size_in` | number[] | No |  |
| `shared_size_lt` | number (double) | No |  |
| `shared_size_lte` | number (double) | No |  |
| `shared_size_not` | number (double) | No |  |
| `shared_size_not_in` | number[] | No |  |
| `size` | number (double) | No |  |
| `size_gt` | number (double) | No |  |
| `size_gte` | number (double) | No |  |
| `size_in` | number[] | No |  |
| `size_lt` | number (double) | No |  |
| `size_lte` | number (double) | No |  |
| `size_not` | number (double) | No |  |
| `size_not_in` | number[] | No |  |
| `type` | [VmVolumeSnapshotType](../Vm/VmVolumeSnapshotType.md) | No |  |
| `type_in` | Array of [VmVolumeSnapshotType](../Vm/VmVolumeSnapshotType.md) | No |  |
| `type_not` | [VmVolumeSnapshotType](../Vm/VmVolumeSnapshotType.md) | No |  |
| `type_not_in` | Array of [VmVolumeSnapshotType](../Vm/VmVolumeSnapshotType.md) | No |  |
| `unique_size` | number (double) | No |  |
| `unique_size_gt` | number (double) | No |  |
| `unique_size_gte` | number (double) | No |  |
| `unique_size_in` | number[] | No |  |
| `unique_size_lt` | number (double) | No |  |
| `unique_size_lte` | number (double) | No |  |
| `unique_size_not` | number (double) | No |  |
| `unique_size_not_in` | number[] | No |  |
| `vm_volume` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | No |  |
| `volume_sharing` | boolean | No |  |
| `volume_sharing_not` | boolean | No |  |
| `volume_size` | number (double) | No |  |
| `volume_size_gt` | number (double) | No |  |
| `volume_size_gte` | number (double) | No |  |
| `volume_size_in` | number[] | No |  |
| `volume_size_lt` | number (double) | No |  |
| `volume_size_lte` | number (double) | No |  |
| `volume_size_not` | number (double) | No |  |
| `volume_size_not_in` | number[] | No |  |
| `zbs_snapshot_uuid` | string | No |  |
| `zbs_snapshot_uuid_contains` | string | No |  |
| `zbs_snapshot_uuid_ends_with` | string | No |  |
| `zbs_snapshot_uuid_gt` | string | No |  |
| `zbs_snapshot_uuid_gte` | string | No |  |
| `zbs_snapshot_uuid_in` | string[] | No |  |
| `zbs_snapshot_uuid_lt` | string | No |  |
| `zbs_snapshot_uuid_lte` | string | No |  |
| `zbs_snapshot_uuid_not` | string | No |  |
| `zbs_snapshot_uuid_not_contains` | string | No |  |
| `zbs_snapshot_uuid_not_ends_with` | string | No |  |
| `zbs_snapshot_uuid_not_in` | string[] | No |  |
| `zbs_snapshot_uuid_not_starts_with` | string | No |  |
| `zbs_snapshot_uuid_starts_with` | string | No |  |

