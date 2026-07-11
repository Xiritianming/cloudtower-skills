# VmPlacementGroup

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `description` | string | Yes |  |
| `enabled` | boolean | Yes |  |
| `id` | string | Yes |  |
| `local_created_at` | string | Yes |  |
| `local_id` | string | Yes |  |
| `local_updated_at` | string | Yes |  |
| `name` | string | Yes |  |
| `vm_host_must_enabled` | boolean | Yes |  |
| `vm_host_must_policy` | boolean | Yes |  |
| `vm_host_prefer_enabled` | boolean | Yes |  |
| `vm_host_prefer_policy` | boolean | Yes |  |
| `vm_vm_policy` | [VmVmPolicy](../Vm/VmVmPolicy.md) | Yes |  |
| `vm_vm_policy_enabled` | boolean | Yes |  |
| `entityAsyncStatus` | any | No |  |
| `usage` | any | No |  |
| `vm_host_must_host_uuids` | Array of [NestedHost](../Nested/NestedHost.md) | No |  |
| `vm_host_prefer_host_uuids` | Array of [NestedHost](../Nested/NestedHost.md) | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |

