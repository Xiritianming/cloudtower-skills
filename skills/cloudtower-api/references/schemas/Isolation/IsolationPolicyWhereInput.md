# IsolationPolicyWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `NOT` | Array of [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `OR` | Array of [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `everoute_cluster` | [EverouteClusterWhereInput](../Everoute/EverouteClusterWhereInput.md) | No |  |
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
| `mode` | [IsolationMode](../Isolation/IsolationMode.md) | No |  |
| `mode_in` | Array of [IsolationMode](../Isolation/IsolationMode.md) | No |  |
| `mode_not` | [IsolationMode](../Isolation/IsolationMode.md) | No |  |
| `mode_not_in` | Array of [IsolationMode](../Isolation/IsolationMode.md) | No |  |
| `statistics` | [SecurityPolicyStatisticsWhereInput](../Security/SecurityPolicyStatisticsWhereInput.md) | No |  |
| `vm` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |

