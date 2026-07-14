# ReplicationPlan

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `compression` | boolean | Yes |  |
| `createdAt` | string | Yes |  |
| `enable_window` | boolean | Yes |  |
| `id` | string | Yes |  |
| `interval` | integer (int32) | Yes |  |
| `ip_mapping` | Array of [NestedReplicationIPAddressMapping](../Nested/NestedReplicationIPAddressMapping.md) | Yes |  |
| `last_execute_status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | Yes |  |
| `last_manual_execute_status` | [BackupPlanExecutionStatus](../Backup/BackupPlanExecutionStatus.md) | Yes |  |
| `name` | string | Yes |  |
| `network_mapping` | Array of [NestedReplicationPlanNetworkMapping](../Nested/NestedReplicationPlanNetworkMapping.md) | Yes |  |
| `objects_descriptor` | Array of [NestedReplicationObjectDescriptor](../Nested/NestedReplicationObjectDescriptor.md) | Yes |  |
| `period` | [ReplicationPlanPeriod](../Replication/ReplicationPlanPeriod.md) | Yes |  |
| `replica_name_rule` | [ReplicaNameRule](../Replica/ReplicaNameRule.md) | Yes |  |
| `status` | [BackupPlanStatus](../Backup/BackupPlanStatus.md) | Yes |  |
| `storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | Yes |  |
| `target_cluster_descriptor` | [NestedReplicationClusterDescriptor](../Nested/NestedReplicationClusterDescriptor.md) | Yes |  |
| `target_replication_service` | [NestedReplicationService](../Nested/NestedReplicationService.md) | Yes |  |
| `time_points` | Array of [NestedBackupPlanTimePoint](../Nested/NestedBackupPlanTimePoint.md) | Yes |  |
| `type` | [ReplicationPlanType](../Replication/ReplicationPlanType.md) | Yes |  |
| `updatedAt` | string | Yes |  |
| `abort_window_unfinished` | boolean | No |  |
| `activation_timestamp` | string | No |  |
| `delete_strategy` | [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `description` | string | No |  |
| `ec_k` | integer (int32) | No |  |
| `ec_m` | integer (int32) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `external_cloudtower` | [NestedExternalCloudTower](../Nested/NestedExternalCloudTower.md) | No |  |
| `inbound` | boolean | No |  |
| `iscsi_luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `keep_mac_address` | boolean | No |  |
| `keep_policy` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_value` | integer (int32) | No |  |
| `last_execute_status_message` | string | No |  |
| `last_execute_success_job_count` | integer (int32) | No |  |
| `last_execute_total_job_count` | integer (int32) | No |  |
| `last_executed_at` | string | No |  |
| `last_manual_execute_status_message` | string | No |  |
| `last_manual_execute_success_job_count` | integer (int32) | No |  |
| `last_manual_execute_total_job_count` | integer (int32) | No |  |
| `last_manual_executed_at` | string | No |  |
| `next_execution_time` | string | No |  |
| `phase` | [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `replica_name_setting` | string | No |  |
| `replica_num` | integer (int32) | No |  |
| `replica_vms` | Array of [NestedReplicaVm](../Nested/NestedReplicaVm.md) | No |  |
| `replication_plan_executions` | Array of [NestedReplicationPlanExecution](../Nested/NestedReplicationPlanExecution.md) | No |  |
| `replication_restore_points` | Array of [NestedReplicationRestorePoint](../Nested/NestedReplicationRestorePoint.md) | No |  |
| `replication_target_executions` | Array of [NestedReplicationTargetExecution](../Nested/NestedReplicationTargetExecution.md) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `snapshot_consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `target_cluster` | [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `thin_provision` | boolean | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |
| `weekdays` | Array of [WeekdayTypeEnum](../Weekday/WeekdayTypeEnum.md) | No |  |
| `window_end` | string | No |  |
| `window_start` | string | No |  |

