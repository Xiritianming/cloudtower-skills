# VmPlacementGroupUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VmPlacementGroupWhereInput](../Vm/VmPlacementGroupWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vm_vm_policy` | [VmVmPolicy](../Vm/VmVmPolicy.md) | No |  |
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `prefer_hosts` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `must_hosts` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `vm_host_prefer_enabled` | boolean | No |  |
| `vm_host_must_policy` | boolean | No |  |
| `vm_host_must_enabled` | boolean | No |  |
| `vm_host_prefer_policy` | boolean | No |  |
| `vm_vm_policy_enabled` | boolean | No |  |
| `name` | string | No |  |
| `description` | string | No |  |
| `enabled` | boolean | No |  |

