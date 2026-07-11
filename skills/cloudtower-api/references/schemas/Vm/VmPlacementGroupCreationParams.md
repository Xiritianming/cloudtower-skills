# VmPlacementGroupCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes |  |
| `enabled` | boolean | Yes |  |
| `cluster_id` | string | Yes |  |
| `vm_vm_policy` | [VmVmPolicy](../Vm/VmVmPolicy.md) | No |  |
| `vm_host_prefer_enabled` | boolean | No |  |
| `vm_host_must_policy` | boolean | No |  |
| `vm_host_must_enabled` | boolean | No |  |
| `vm_host_prefer_policy` | boolean | No |  |
| `vm_vm_policy_enabled` | boolean | No |  |
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `prefer_hosts` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `must_hosts` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `description` | string | No |  |

