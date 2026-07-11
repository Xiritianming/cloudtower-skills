# Datacenter

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `name` | string | Yes |  |
| `organization` | [NestedOrganization](../Nested/NestedOrganization.md) | Yes |  |
| `cluster_num` | integer (int32) | No |  |
| `clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `failure_data_space` | integer (int64) | No |  |
| `host_num` | integer (int32) | No |  |
| `labels` | Array of [NestedLabel](../Nested/NestedLabel.md) | No |  |
| `total_cpu_hz` | integer (int64) | No |  |
| `total_data_capacity` | integer (int64) | No |  |
| `total_memory_bytes` | integer (int64) | No |  |
| `used_cpu_hz` | number (double) | No |  |
| `used_data_space` | integer (int64) | No |  |
| `used_memory_bytes` | number (double) | No |  |
| `vm_num` | integer (int32) | No |  |

