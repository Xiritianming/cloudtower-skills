# SecurityGroupWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vms_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `security_policies_some` | [SecurityPolicyWhereInput](../Security/SecurityPolicyWhereInput.md) | No |  |
| `security_policies_none` | [SecurityPolicyWhereInput](../Security/SecurityPolicyWhereInput.md) | No |  |
| `security_policies_every` | [SecurityPolicyWhereInput](../Security/SecurityPolicyWhereInput.md) | No |  |
| `name_starts_with` | string | No |  |
| `name_not_starts_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not` | string | No |  |
| `name_lte` | string | No |  |
| `name_lt` | string | No |  |
| `name_in` | string[] | No |  |
| `name_gte` | string | No |  |
| `name_gt` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_contains` | string | No |  |
| `name` | string | No |  |
| `member_type_not_in` | Array of [SecurityGroupMemberType](../Security/SecurityGroupMemberType.md) | No |  |
| `member_type_not` | [SecurityGroupMemberType](../Security/SecurityGroupMemberType.md) | No |  |
| `member_type_in` | Array of [SecurityGroupMemberType](../Security/SecurityGroupMemberType.md) | No |  |
| `member_type` | [SecurityGroupMemberType](../Security/SecurityGroupMemberType.md) | No |  |
| `isolation_policies_some` | [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `isolation_policies_none` | [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `isolation_policies_every` | [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `ips_starts_with` | string | No |  |
| `ips_not_starts_with` | string | No |  |
| `ips_not_in` | string[] | No |  |
| `ips_not_ends_with` | string | No |  |
| `ips_not_contains` | string | No |  |
| `ips_not` | string | No |  |
| `ips_lte` | string | No |  |
| `ips_lt` | string | No |  |
| `ips_in` | string[] | No |  |
| `ips_gte` | string | No |  |
| `ips_gt` | string | No |  |
| `ips_ends_with` | string | No |  |
| `ips_contains` | string | No |  |
| `ips` | string | No |  |
| `id_starts_with` | string | No |  |
| `id_not_starts_with` | string | No |  |
| `id_not_in` | string[] | No |  |
| `id_not_ends_with` | string | No |  |
| `id_not_contains` | string | No |  |
| `id_not` | string | No |  |
| `id_lte` | string | No |  |
| `id_lt` | string | No |  |
| `id_in` | string[] | No |  |
| `id_gte` | string | No |  |
| `id_gt` | string | No |  |
| `id_ends_with` | string | No |  |
| `id_contains` | string | No |  |
| `id` | string | No |  |
| `exclude_ips_starts_with` | string | No |  |
| `exclude_ips_not_starts_with` | string | No |  |
| `exclude_ips_not_in` | string[] | No |  |
| `exclude_ips_not_ends_with` | string | No |  |
| `exclude_ips_not_contains` | string | No |  |
| `exclude_ips_not` | string | No |  |
| `exclude_ips_lte` | string | No |  |
| `exclude_ips_lt` | string | No |  |
| `exclude_ips_in` | string[] | No |  |
| `exclude_ips_gte` | string | No |  |
| `exclude_ips_gt` | string | No |  |
| `exclude_ips_ends_with` | string | No |  |
| `exclude_ips_contains` | string | No |  |
| `exclude_ips` | string | No |  |
| `everoute_cluster` | [EverouteClusterWhereInput](../Everoute/EverouteClusterWhereInput.md) | No |  |
| `description_starts_with` | string | No |  |
| `description_not_starts_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not` | string | No |  |
| `description_lte` | string | No |  |
| `description_lt` | string | No |  |
| `description_in` | string[] | No |  |
| `description_gte` | string | No |  |
| `description_gt` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_contains` | string | No |  |
| `description` | string | No |  |
| `OR` | Array of [SecurityGroupWhereInput](../Security/SecurityGroupWhereInput.md) | No |  |
| `NOT` | Array of [SecurityGroupWhereInput](../Security/SecurityGroupWhereInput.md) | No |  |
| `AND` | Array of [SecurityGroupWhereInput](../Security/SecurityGroupWhereInput.md) | No |  |

