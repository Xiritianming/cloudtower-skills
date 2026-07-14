# BusinessHostGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `business_hosts` | Array of [NestedBusinessHost](../Nested/NestedBusinessHost.md) | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `iscsi_luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `iscsi_targets` | Array of [NestedIscsiTarget](../Nested/NestedIscsiTarget.md) | No |  |
| `nvmf_namespaces` | Array of [NestedNvmfNamespace](../Nested/NestedNvmfNamespace.md) | No |  |
| `nvmf_subsystems` | Array of [NestedNvmfSubsystem](../Nested/NestedNvmfSubsystem.md) | No |  |

