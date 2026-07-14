# ClusterSettings

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `default_ha` | boolean | No |  |
| `default_storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `default_storage_policy_ec_k` | integer (int32) | No |  |
| `default_storage_policy_ec_m` | integer (int32) | No |  |
| `default_storage_policy_replica_num` | integer (int32) | No |  |
| `default_storage_policy_stripe_num` | integer (int32) | No |  |
| `default_storage_policy_thin_provision` | boolean | No |  |
| `enabled_iscsi` | boolean | No |  |
| `vm_recycle_bin` | [NestedVmRecycleBin](../Nested/NestedVmRecycleBin.md) | No |  |

