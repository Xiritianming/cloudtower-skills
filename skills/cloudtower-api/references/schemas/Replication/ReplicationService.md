# ReplicationService

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `createdAt` | string | Yes |  |
| `id` | string | Yes |  |
| `kube_config` | string | Yes |  |
| `management_network` | [NestedReplicationServiceNetwork](../Nested/NestedReplicationServiceNetwork.md) | Yes |  |
| `name` | string | Yes |  |
| `replication_clusters_descriptor` | Array of [NestedReplicationClusterDescriptor](../Nested/NestedReplicationClusterDescriptor.md) | Yes |  |
| `replication_network` | [NestedReplicationServiceNetwork](../Nested/NestedReplicationServiceNetwork.md) | Yes |  |
| `storage_network` | [NestedReplicationServiceNetwork](../Nested/NestedReplicationServiceNetwork.md) | Yes |  |
| `updatedAt` | string | Yes |  |
| `application` | any | No |  |
| `description` | string | No |  |
| `entityAsyncStatus` | any | No |  |
| `failover_executions` | Array of [NestedFailoverExecution](../Nested/NestedFailoverExecution.md) | No |  |
| `max_failback_jobs` | integer (int32) | No |  |
| `max_failback_speed_limit` | number (double) | No |  |
| `max_replication_jobs` | integer (int32) | No |  |
| `max_replication_speed_limit` | number (double) | No |  |
| `max_retry_times` | integer (int32) | No |  |
| `permanent_failover_execution` | Array of [NestedPermanentFailoverExecution](../Nested/NestedPermanentFailoverExecution.md) | No |  |
| `replication_clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `replication_plans` | Array of [NestedReplicationPlan](../Nested/NestedReplicationPlan.md) | No |  |
| `retry_interval` | integer (int32) | No |  |

