# ReplicationServiceWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ReplicationServiceWhereInput](../Replication/ReplicationServiceWhereInput.md) | No |  |
| `NOT` | Array of [ReplicationServiceWhereInput](../Replication/ReplicationServiceWhereInput.md) | No |  |
| `OR` | Array of [ReplicationServiceWhereInput](../Replication/ReplicationServiceWhereInput.md) | No |  |
| `application` | [CloudTowerApplicationWhereInput](../Cloud/CloudTowerApplicationWhereInput.md) | No |  |
| `createdAt` | string | No |  |
| `createdAt_gt` | string | No |  |
| `createdAt_gte` | string | No |  |
| `createdAt_in` | string[] | No |  |
| `createdAt_lt` | string | No |  |
| `createdAt_lte` | string | No |  |
| `createdAt_not` | string | No |  |
| `createdAt_not_in` | string[] | No |  |
| `description` | string | No |  |
| `description_contains` | string | No |  |
| `description_ends_with` | string | No |  |
| `description_gt` | string | No |  |
| `description_gte` | string | No |  |
| `description_in` | string[] | No |  |
| `description_lt` | string | No |  |
| `description_lte` | string | No |  |
| `description_not` | string | No |  |
| `description_not_contains` | string | No |  |
| `description_not_ends_with` | string | No |  |
| `description_not_in` | string[] | No |  |
| `description_not_starts_with` | string | No |  |
| `description_starts_with` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `failover_executions_every` | [FailoverExecutionWhereInput](../Failover/FailoverExecutionWhereInput.md) | No |  |
| `failover_executions_none` | [FailoverExecutionWhereInput](../Failover/FailoverExecutionWhereInput.md) | No |  |
| `failover_executions_some` | [FailoverExecutionWhereInput](../Failover/FailoverExecutionWhereInput.md) | No |  |
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
| `kube_config` | string | No |  |
| `kube_config_contains` | string | No |  |
| `kube_config_ends_with` | string | No |  |
| `kube_config_gt` | string | No |  |
| `kube_config_gte` | string | No |  |
| `kube_config_in` | string[] | No |  |
| `kube_config_lt` | string | No |  |
| `kube_config_lte` | string | No |  |
| `kube_config_not` | string | No |  |
| `kube_config_not_contains` | string | No |  |
| `kube_config_not_ends_with` | string | No |  |
| `kube_config_not_in` | string[] | No |  |
| `kube_config_not_starts_with` | string | No |  |
| `kube_config_starts_with` | string | No |  |
| `max_failback_jobs` | integer (int32) | No |  |
| `max_failback_jobs_gt` | integer (int32) | No |  |
| `max_failback_jobs_gte` | integer (int32) | No |  |
| `max_failback_jobs_in` | integer[] | No |  |
| `max_failback_jobs_lt` | integer (int32) | No |  |
| `max_failback_jobs_lte` | integer (int32) | No |  |
| `max_failback_jobs_not` | integer (int32) | No |  |
| `max_failback_jobs_not_in` | integer[] | No |  |
| `max_failback_speed_limit` | number (double) | No |  |
| `max_failback_speed_limit_gt` | number (double) | No |  |
| `max_failback_speed_limit_gte` | number (double) | No |  |
| `max_failback_speed_limit_in` | number[] | No |  |
| `max_failback_speed_limit_lt` | number (double) | No |  |
| `max_failback_speed_limit_lte` | number (double) | No |  |
| `max_failback_speed_limit_not` | number (double) | No |  |
| `max_failback_speed_limit_not_in` | number[] | No |  |
| `max_replication_jobs` | integer (int32) | No |  |
| `max_replication_jobs_gt` | integer (int32) | No |  |
| `max_replication_jobs_gte` | integer (int32) | No |  |
| `max_replication_jobs_in` | integer[] | No |  |
| `max_replication_jobs_lt` | integer (int32) | No |  |
| `max_replication_jobs_lte` | integer (int32) | No |  |
| `max_replication_jobs_not` | integer (int32) | No |  |
| `max_replication_jobs_not_in` | integer[] | No |  |
| `max_replication_speed_limit` | number (double) | No |  |
| `max_replication_speed_limit_gt` | number (double) | No |  |
| `max_replication_speed_limit_gte` | number (double) | No |  |
| `max_replication_speed_limit_in` | number[] | No |  |
| `max_replication_speed_limit_lt` | number (double) | No |  |
| `max_replication_speed_limit_lte` | number (double) | No |  |
| `max_replication_speed_limit_not` | number (double) | No |  |
| `max_replication_speed_limit_not_in` | number[] | No |  |
| `max_retry_times` | integer (int32) | No |  |
| `max_retry_times_gt` | integer (int32) | No |  |
| `max_retry_times_gte` | integer (int32) | No |  |
| `max_retry_times_in` | integer[] | No |  |
| `max_retry_times_lt` | integer (int32) | No |  |
| `max_retry_times_lte` | integer (int32) | No |  |
| `max_retry_times_not` | integer (int32) | No |  |
| `max_retry_times_not_in` | integer[] | No |  |
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
| `permanent_failover_execution_every` | [PermanentFailoverExecutionWhereInput](../Permanent/PermanentFailoverExecutionWhereInput.md) | No |  |
| `permanent_failover_execution_none` | [PermanentFailoverExecutionWhereInput](../Permanent/PermanentFailoverExecutionWhereInput.md) | No |  |
| `permanent_failover_execution_some` | [PermanentFailoverExecutionWhereInput](../Permanent/PermanentFailoverExecutionWhereInput.md) | No |  |
| `replication_clusters_every` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `replication_clusters_none` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `replication_clusters_some` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `replication_plans_every` | [ReplicationPlanWhereInput](../Replication/ReplicationPlanWhereInput.md) | No |  |
| `replication_plans_none` | [ReplicationPlanWhereInput](../Replication/ReplicationPlanWhereInput.md) | No |  |
| `replication_plans_some` | [ReplicationPlanWhereInput](../Replication/ReplicationPlanWhereInput.md) | No |  |
| `retry_interval` | integer (int32) | No |  |
| `retry_interval_gt` | integer (int32) | No |  |
| `retry_interval_gte` | integer (int32) | No |  |
| `retry_interval_in` | integer[] | No |  |
| `retry_interval_lt` | integer (int32) | No |  |
| `retry_interval_lte` | integer (int32) | No |  |
| `retry_interval_not` | integer (int32) | No |  |
| `retry_interval_not_in` | integer[] | No |  |
| `updatedAt` | string | No |  |
| `updatedAt_gt` | string | No |  |
| `updatedAt_gte` | string | No |  |
| `updatedAt_in` | string[] | No |  |
| `updatedAt_lt` | string | No |  |
| `updatedAt_lte` | string | No |  |
| `updatedAt_not` | string | No |  |
| `updatedAt_not_in` | string[] | No |  |

