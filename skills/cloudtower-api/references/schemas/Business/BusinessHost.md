# BusinessHost

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `initiators` | Array of [NestedInitiator](../Nested/NestedInitiator.md) | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `business_host_group` | [NestedBusinessHostGroup](../Nested/NestedBusinessHostGroup.md) | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `iscsi_luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `iscsi_targets` | Array of [NestedIscsiTarget](../Nested/NestedIscsiTarget.md) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `nvmf_namespaces` | Array of [NestedNvmfNamespace](../Nested/NestedNvmfNamespace.md) | No |  |
| `nvmf_subsystems` | Array of [NestedNvmfSubsystem](../Nested/NestedNvmfSubsystem.md) | No |  |

