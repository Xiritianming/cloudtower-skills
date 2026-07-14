# DatacenterWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `NOT` | Array of [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `OR` | Array of [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `cluster_num` | integer (int32) | No |  |
| `cluster_num_gt` | integer (int32) | No |  |
| `cluster_num_gte` | integer (int32) | No |  |
| `cluster_num_in` | integer[] | No |  |
| `cluster_num_lt` | integer (int32) | No |  |
| `cluster_num_lte` | integer (int32) | No |  |
| `cluster_num_not` | integer (int32) | No |  |
| `cluster_num_not_in` | integer[] | No |  |
| `clusters_every` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `clusters_none` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `clusters_some` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `failure_data_space` | integer (int64) | No |  |
| `failure_data_space_gt` | integer (int64) | No |  |
| `failure_data_space_gte` | integer (int64) | No |  |
| `failure_data_space_in` | integer[] | No |  |
| `failure_data_space_lt` | integer (int64) | No |  |
| `failure_data_space_lte` | integer (int64) | No |  |
| `failure_data_space_not` | integer (int64) | No |  |
| `failure_data_space_not_in` | integer[] | No |  |
| `host_num` | integer (int32) | No |  |
| `host_num_gt` | integer (int32) | No |  |
| `host_num_gte` | integer (int32) | No |  |
| `host_num_in` | integer[] | No |  |
| `host_num_lt` | integer (int32) | No |  |
| `host_num_lte` | integer (int32) | No |  |
| `host_num_not` | integer (int32) | No |  |
| `host_num_not_in` | integer[] | No |  |
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
| `name` | string | No |  |
| `name_contains` | string | No |  |
| `name_ends_with` | string | No |  |
| `name_gt` | string | No |  |
| `name_gte` | string | No |  |
| `name_in` | string[] | No |  |
| `name_lt` | string | No |  |
| `name_lte` | string | No |  |
| `name_not` | string | No |  |
| `name_not_contains` | string | No |  |
| `name_not_ends_with` | string | No |  |
| `name_not_in` | string[] | No |  |
| `name_not_starts_with` | string | No |  |
| `name_starts_with` | string | No |  |
| `organization` | [OrganizationWhereInput](../Organization/OrganizationWhereInput.md) | No |  |
| `total_cpu_hz` | integer (int64) | No |  |
| `total_cpu_hz_gt` | integer (int64) | No |  |
| `total_cpu_hz_gte` | integer (int64) | No |  |
| `total_cpu_hz_in` | integer[] | No |  |
| `total_cpu_hz_lt` | integer (int64) | No |  |
| `total_cpu_hz_lte` | integer (int64) | No |  |
| `total_cpu_hz_not` | integer (int64) | No |  |
| `total_cpu_hz_not_in` | integer[] | No |  |
| `total_data_capacity` | integer (int64) | No |  |
| `total_data_capacity_gt` | integer (int64) | No |  |
| `total_data_capacity_gte` | integer (int64) | No |  |
| `total_data_capacity_in` | integer[] | No |  |
| `total_data_capacity_lt` | integer (int64) | No |  |
| `total_data_capacity_lte` | integer (int64) | No |  |
| `total_data_capacity_not` | integer (int64) | No |  |
| `total_data_capacity_not_in` | integer[] | No |  |
| `total_memory_bytes` | integer (int64) | No |  |
| `total_memory_bytes_gt` | integer (int64) | No |  |
| `total_memory_bytes_gte` | integer (int64) | No |  |
| `total_memory_bytes_in` | integer[] | No |  |
| `total_memory_bytes_lt` | integer (int64) | No |  |
| `total_memory_bytes_lte` | integer (int64) | No |  |
| `total_memory_bytes_not` | integer (int64) | No |  |
| `total_memory_bytes_not_in` | integer[] | No |  |
| `used_cpu_hz` | number (double) | No |  |
| `used_cpu_hz_gt` | number (double) | No |  |
| `used_cpu_hz_gte` | number (double) | No |  |
| `used_cpu_hz_in` | number[] | No |  |
| `used_cpu_hz_lt` | number (double) | No |  |
| `used_cpu_hz_lte` | number (double) | No |  |
| `used_cpu_hz_not` | number (double) | No |  |
| `used_cpu_hz_not_in` | number[] | No |  |
| `used_data_space` | integer (int64) | No |  |
| `used_data_space_gt` | integer (int64) | No |  |
| `used_data_space_gte` | integer (int64) | No |  |
| `used_data_space_in` | integer[] | No |  |
| `used_data_space_lt` | integer (int64) | No |  |
| `used_data_space_lte` | integer (int64) | No |  |
| `used_data_space_not` | integer (int64) | No |  |
| `used_data_space_not_in` | integer[] | No |  |
| `used_memory_bytes` | number (double) | No |  |
| `used_memory_bytes_gt` | number (double) | No |  |
| `used_memory_bytes_gte` | number (double) | No |  |
| `used_memory_bytes_in` | number[] | No |  |
| `used_memory_bytes_lt` | number (double) | No |  |
| `used_memory_bytes_lte` | number (double) | No |  |
| `used_memory_bytes_not` | number (double) | No |  |
| `used_memory_bytes_not_in` | number[] | No |  |
| `vm_num` | integer (int32) | No |  |
| `vm_num_gt` | integer (int32) | No |  |
| `vm_num_gte` | integer (int32) | No |  |
| `vm_num_in` | integer[] | No |  |
| `vm_num_lt` | integer (int32) | No |  |
| `vm_num_lte` | integer (int32) | No |  |
| `vm_num_not` | integer (int32) | No |  |
| `vm_num_not_in` | integer[] | No |  |

