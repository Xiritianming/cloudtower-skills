# Vds

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `bond_mode` | string | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `ovsbr_name` | string | Yes |  |
| `type` | [NetworkType](../Network/NetworkType.md) | Yes |  |
| `vlans_num` | integer (int32) | Yes |  |
| `entityAsyncStatus` | any | No |  |
| `everoute_cluster` | any | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `nics` | Array of [NestedNic](../Nested/NestedNic.md) | No |  |
| `vlans` | Array of [NestedVlan](../Nested/NestedVlan.md) | No |  |
| `work_mode` | string | No |  |

