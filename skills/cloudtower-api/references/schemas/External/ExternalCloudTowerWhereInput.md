# ExternalCloudTowerWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [ExternalCloudTowerWhereInput](../External/ExternalCloudTowerWhereInput.md) | No |  |
| `NOT` | Array of [ExternalCloudTowerWhereInput](../External/ExternalCloudTowerWhereInput.md) | No |  |
| `OR` | Array of [ExternalCloudTowerWhereInput](../External/ExternalCloudTowerWhereInput.md) | No |  |
| `api_key` | string | No |  |
| `api_key_contains` | string | No |  |
| `api_key_ends_with` | string | No |  |
| `api_key_gt` | string | No |  |
| `api_key_gte` | string | No |  |
| `api_key_in` | string[] | No |  |
| `api_key_lt` | string | No |  |
| `api_key_lte` | string | No |  |
| `api_key_not` | string | No |  |
| `api_key_not_contains` | string | No |  |
| `api_key_not_ends_with` | string | No |  |
| `api_key_not_in` | string[] | No |  |
| `api_key_not_starts_with` | string | No |  |
| `api_key_starts_with` | string | No |  |
| `createdAt` | string | No |  |
| `createdAt_gt` | string | No |  |
| `createdAt_gte` | string | No |  |
| `createdAt_in` | string[] | No |  |
| `createdAt_lt` | string | No |  |
| `createdAt_lte` | string | No |  |
| `createdAt_not` | string | No |  |
| `createdAt_not_in` | string[] | No |  |
| `deploy_id` | string | No |  |
| `deploy_id_contains` | string | No |  |
| `deploy_id_ends_with` | string | No |  |
| `deploy_id_gt` | string | No |  |
| `deploy_id_gte` | string | No |  |
| `deploy_id_in` | string[] | No |  |
| `deploy_id_lt` | string | No |  |
| `deploy_id_lte` | string | No |  |
| `deploy_id_not` | string | No |  |
| `deploy_id_not_contains` | string | No |  |
| `deploy_id_not_ends_with` | string | No |  |
| `deploy_id_not_in` | string[] | No |  |
| `deploy_id_not_starts_with` | string | No |  |
| `deploy_id_starts_with` | string | No |  |
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
| `endpoint` | string | No |  |
| `endpoint_contains` | string | No |  |
| `endpoint_ends_with` | string | No |  |
| `endpoint_gt` | string | No |  |
| `endpoint_gte` | string | No |  |
| `endpoint_in` | string[] | No |  |
| `endpoint_lt` | string | No |  |
| `endpoint_lte` | string | No |  |
| `endpoint_not` | string | No |  |
| `endpoint_not_contains` | string | No |  |
| `endpoint_not_ends_with` | string | No |  |
| `endpoint_not_in` | string[] | No |  |
| `endpoint_not_starts_with` | string | No |  |
| `endpoint_starts_with` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `failback_executions_every` | [FailbackExecutionWhereInput](../Failback/FailbackExecutionWhereInput.md) | No |  |
| `failback_executions_none` | [FailbackExecutionWhereInput](../Failback/FailbackExecutionWhereInput.md) | No |  |
| `failback_executions_some` | [FailbackExecutionWhereInput](../Failback/FailbackExecutionWhereInput.md) | No |  |
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
| `permanent_failover_executions_every` | [PermanentFailoverExecutionWhereInput](../Permanent/PermanentFailoverExecutionWhereInput.md) | No |  |
| `permanent_failover_executions_none` | [PermanentFailoverExecutionWhereInput](../Permanent/PermanentFailoverExecutionWhereInput.md) | No |  |
| `permanent_failover_executions_some` | [PermanentFailoverExecutionWhereInput](../Permanent/PermanentFailoverExecutionWhereInput.md) | No |  |
| `replica_vms_every` | [ReplicaVmWhereInput](../Replica/ReplicaVmWhereInput.md) | No |  |
| `replica_vms_none` | [ReplicaVmWhereInput](../Replica/ReplicaVmWhereInput.md) | No |  |
| `replica_vms_some` | [ReplicaVmWhereInput](../Replica/ReplicaVmWhereInput.md) | No |  |
| `replication_plans_every` | [ReplicationPlanWhereInput](../Replication/ReplicationPlanWhereInput.md) | No |  |
| `replication_plans_none` | [ReplicationPlanWhereInput](../Replication/ReplicationPlanWhereInput.md) | No |  |
| `replication_plans_some` | [ReplicationPlanWhereInput](../Replication/ReplicationPlanWhereInput.md) | No |  |
| `status` | [ExternalCloudTowerStatus](../External/ExternalCloudTowerStatus.md) | No |  |
| `status_in` | Array of [ExternalCloudTowerStatus](../External/ExternalCloudTowerStatus.md) | No |  |
| `status_not` | [ExternalCloudTowerStatus](../External/ExternalCloudTowerStatus.md) | No |  |
| `status_not_in` | Array of [ExternalCloudTowerStatus](../External/ExternalCloudTowerStatus.md) | No |  |
| `sync_replication_plans_every` | [SyncReplicationPlanWhereInput](../Sync/SyncReplicationPlanWhereInput.md) | No |  |
| `sync_replication_plans_none` | [SyncReplicationPlanWhereInput](../Sync/SyncReplicationPlanWhereInput.md) | No |  |
| `sync_replication_plans_some` | [SyncReplicationPlanWhereInput](../Sync/SyncReplicationPlanWhereInput.md) | No |  |
| `updatedAt` | string | No |  |
| `updatedAt_gt` | string | No |  |
| `updatedAt_gte` | string | No |  |
| `updatedAt_in` | string[] | No |  |
| `updatedAt_lt` | string | No |  |
| `updatedAt_lte` | string | No |  |
| `updatedAt_not` | string | No |  |
| `updatedAt_not_in` | string[] | No |  |
| `use_api_key` | [ApiKeyWhereInput](../Api/ApiKeyWhereInput.md) | No |  |

