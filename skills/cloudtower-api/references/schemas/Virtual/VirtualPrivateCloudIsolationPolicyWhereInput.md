# VirtualPrivateCloudIsolationPolicyWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [VirtualPrivateCloudIsolationPolicyWhereInput](../Virtual/VirtualPrivateCloudIsolationPolicyWhereInput.md) | No |  |
| `NOT` | Array of [VirtualPrivateCloudIsolationPolicyWhereInput](../Virtual/VirtualPrivateCloudIsolationPolicyWhereInput.md) | No |  |
| `OR` | Array of [VirtualPrivateCloudIsolationPolicyWhereInput](../Virtual/VirtualPrivateCloudIsolationPolicyWhereInput.md) | No |  |
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
| `mode` | [VirtualPrivateCloudIsolationPolicyMode](../Virtual/VirtualPrivateCloudIsolationPolicyMode.md) | No |  |
| `mode_in` | Array of [VirtualPrivateCloudIsolationPolicyMode](../Virtual/VirtualPrivateCloudIsolationPolicyMode.md) | No |  |
| `mode_not` | [VirtualPrivateCloudIsolationPolicyMode](../Virtual/VirtualPrivateCloudIsolationPolicyMode.md) | No |  |
| `mode_not_in` | Array of [VirtualPrivateCloudIsolationPolicyMode](../Virtual/VirtualPrivateCloudIsolationPolicyMode.md) | No |  |
| `security_groups_every` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | No |  |
| `security_groups_none` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | No |  |
| `security_groups_some` | [VirtualPrivateCloudSecurityGroupWhereInput](../Virtual/VirtualPrivateCloudSecurityGroupWhereInput.md) | No |  |
| `vm` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vpc` | [VirtualPrivateCloudWhereInput](../Virtual/VirtualPrivateCloudWhereInput.md) | No |  |

