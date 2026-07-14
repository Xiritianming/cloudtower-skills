# SyncReplicationPlanWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [SyncReplicationPlanWhereInput](../Sync/SyncReplicationPlanWhereInput.md) | No |  |
| `NOT` | Array of [SyncReplicationPlanWhereInput](../Sync/SyncReplicationPlanWhereInput.md) | No |  |
| `OR` | Array of [SyncReplicationPlanWhereInput](../Sync/SyncReplicationPlanWhereInput.md) | No |  |
| `activation_timestamp` | string | No |  |
| `activation_timestamp_gt` | string | No |  |
| `activation_timestamp_gte` | string | No |  |
| `activation_timestamp_in` | string[] | No |  |
| `activation_timestamp_lt` | string | No |  |
| `activation_timestamp_lte` | string | No |  |
| `activation_timestamp_not` | string | No |  |
| `activation_timestamp_not_in` | string[] | No |  |
| `compression` | boolean | No |  |
| `compression_not` | boolean | No |  |
| `createdAt` | string | No |  |
| `createdAt_gt` | string | No |  |
| `createdAt_gte` | string | No |  |
| `createdAt_in` | string[] | No |  |
| `createdAt_lt` | string | No |  |
| `createdAt_lte` | string | No |  |
| `createdAt_not` | string | No |  |
| `createdAt_not_in` | string[] | No |  |
| `data_version` | integer (int32) | No |  |
| `data_version_gt` | integer (int32) | No |  |
| `data_version_gte` | integer (int32) | No |  |
| `data_version_in` | integer[] | No |  |
| `data_version_lt` | integer (int32) | No |  |
| `data_version_lte` | integer (int32) | No |  |
| `data_version_not` | integer (int32) | No |  |
| `data_version_not_in` | integer[] | No |  |
| `delete_strategy` | [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `delete_strategy_in` | Array of [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `delete_strategy_not` | [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
| `delete_strategy_not_in` | Array of [BackupPlanDeleteStrategy](../Backup/BackupPlanDeleteStrategy.md) | No |  |
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
| `ec_k` | integer (int32) | No |  |
| `ec_k_gt` | integer (int32) | No |  |
| `ec_k_gte` | integer (int32) | No |  |
| `ec_k_in` | integer[] | No |  |
| `ec_k_lt` | integer (int32) | No |  |
| `ec_k_lte` | integer (int32) | No |  |
| `ec_k_not` | integer (int32) | No |  |
| `ec_k_not_in` | integer[] | No |  |
| `ec_m` | integer (int32) | No |  |
| `ec_m_gt` | integer (int32) | No |  |
| `ec_m_gte` | integer (int32) | No |  |
| `ec_m_in` | integer[] | No |  |
| `ec_m_lt` | integer (int32) | No |  |
| `ec_m_lte` | integer (int32) | No |  |
| `ec_m_not` | integer (int32) | No |  |
| `ec_m_not_in` | integer[] | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `entityAsyncStatus_not_in` | Array of [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `external_cloudtower` | [ExternalCloudTowerWhereInput](../External/ExternalCloudTowerWhereInput.md) | No |  |
| `failover_test_keep_mac_address` | boolean | No |  |
| `failover_test_keep_mac_address_not` | boolean | No |  |
| `failover_test_name_rule` | [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `failover_test_name_rule_in` | Array of [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `failover_test_name_rule_not` | [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `failover_test_name_rule_not_in` | Array of [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `failover_test_name_setting` | string | No |  |
| `failover_test_name_setting_contains` | string | No |  |
| `failover_test_name_setting_ends_with` | string | No |  |
| `failover_test_name_setting_gt` | string | No |  |
| `failover_test_name_setting_gte` | string | No |  |
| `failover_test_name_setting_in` | string[] | No |  |
| `failover_test_name_setting_lt` | string | No |  |
| `failover_test_name_setting_lte` | string | No |  |
| `failover_test_name_setting_not` | string | No |  |
| `failover_test_name_setting_not_contains` | string | No |  |
| `failover_test_name_setting_not_ends_with` | string | No |  |
| `failover_test_name_setting_not_in` | string[] | No |  |
| `failover_test_name_setting_not_starts_with` | string | No |  |
| `failover_test_name_setting_starts_with` | string | No |  |
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
| `inbound` | boolean | No |  |
| `inbound_not` | boolean | No |  |
| `initialization_time_point` | string | No |  |
| `initialization_time_point_contains` | string | No |  |
| `initialization_time_point_ends_with` | string | No |  |
| `initialization_time_point_gt` | string | No |  |
| `initialization_time_point_gte` | string | No |  |
| `initialization_time_point_in` | string[] | No |  |
| `initialization_time_point_lt` | string | No |  |
| `initialization_time_point_lte` | string | No |  |
| `initialization_time_point_not` | string | No |  |
| `initialization_time_point_not_contains` | string | No |  |
| `initialization_time_point_not_ends_with` | string | No |  |
| `initialization_time_point_not_in` | string[] | No |  |
| `initialization_time_point_not_starts_with` | string | No |  |
| `initialization_time_point_starts_with` | string | No |  |
| `interval` | integer (int32) | No |  |
| `interval_gt` | integer (int32) | No |  |
| `interval_gte` | integer (int32) | No |  |
| `interval_in` | integer[] | No |  |
| `interval_lt` | integer (int32) | No |  |
| `interval_lte` | integer (int32) | No |  |
| `interval_not` | integer (int32) | No |  |
| `interval_not_in` | integer[] | No |  |
| `keep_mac_address` | boolean | No |  |
| `keep_mac_address_not` | boolean | No |  |
| `keep_policy` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_in` | Array of [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_not` | [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_not_in` | Array of [BackupPlanKeepPolicy](../Backup/BackupPlanKeepPolicy.md) | No |  |
| `keep_policy_value` | integer (int32) | No |  |
| `keep_policy_value_gt` | integer (int32) | No |  |
| `keep_policy_value_gte` | integer (int32) | No |  |
| `keep_policy_value_in` | integer[] | No |  |
| `keep_policy_value_lt` | integer (int32) | No |  |
| `keep_policy_value_lte` | integer (int32) | No |  |
| `keep_policy_value_not` | integer (int32) | No |  |
| `keep_policy_value_not_in` | integer[] | No |  |
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
| `period` | [ReplicationPlanPeriod](../Replication/ReplicationPlanPeriod.md) | No |  |
| `period_in` | Array of [ReplicationPlanPeriod](../Replication/ReplicationPlanPeriod.md) | No |  |
| `period_not` | [ReplicationPlanPeriod](../Replication/ReplicationPlanPeriod.md) | No |  |
| `period_not_in` | Array of [ReplicationPlanPeriod](../Replication/ReplicationPlanPeriod.md) | No |  |
| `phase` | [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `phase_in` | Array of [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `phase_not` | [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `phase_not_in` | Array of [BackupPlanPhase](../Backup/BackupPlanPhase.md) | No |  |
| `replica_name_rule` | [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `replica_name_rule_in` | Array of [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `replica_name_rule_not` | [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `replica_name_rule_not_in` | Array of [ReplicaNameRule](../Replica/ReplicaNameRule.md) | No |  |
| `replica_name_setting` | string | No |  |
| `replica_name_setting_contains` | string | No |  |
| `replica_name_setting_ends_with` | string | No |  |
| `replica_name_setting_gt` | string | No |  |
| `replica_name_setting_gte` | string | No |  |
| `replica_name_setting_in` | string[] | No |  |
| `replica_name_setting_lt` | string | No |  |
| `replica_name_setting_lte` | string | No |  |
| `replica_name_setting_not` | string | No |  |
| `replica_name_setting_not_contains` | string | No |  |
| `replica_name_setting_not_ends_with` | string | No |  |
| `replica_name_setting_not_in` | string[] | No |  |
| `replica_name_setting_not_starts_with` | string | No |  |
| `replica_name_setting_starts_with` | string | No |  |
| `replica_num` | integer (int32) | No |  |
| `replica_num_gt` | integer (int32) | No |  |
| `replica_num_gte` | integer (int32) | No |  |
| `replica_num_in` | integer[] | No |  |
| `replica_num_lt` | integer (int32) | No |  |
| `replica_num_lte` | integer (int32) | No |  |
| `replica_num_not` | integer (int32) | No |  |
| `replica_num_not_in` | integer[] | No |  |
| `replica_vms_every` | [ReplicaVmWhereInput](../Replica/ReplicaVmWhereInput.md) | No |  |
| `replica_vms_none` | [ReplicaVmWhereInput](../Replica/ReplicaVmWhereInput.md) | No |  |
| `replica_vms_some` | [ReplicaVmWhereInput](../Replica/ReplicaVmWhereInput.md) | No |  |
| `replication_restore_points_every` | [ReplicationRestorePointWhereInput](../Replication/ReplicationRestorePointWhereInput.md) | No |  |
| `replication_restore_points_none` | [ReplicationRestorePointWhereInput](../Replication/ReplicationRestorePointWhereInput.md) | No |  |
| `replication_restore_points_some` | [ReplicationRestorePointWhereInput](../Replication/ReplicationRestorePointWhereInput.md) | No |  |
| `replication_target_executions_every` | [ReplicationTargetExecutionWhereInput](../Replication/ReplicationTargetExecutionWhereInput.md) | No |  |
| `replication_target_executions_none` | [ReplicationTargetExecutionWhereInput](../Replication/ReplicationTargetExecutionWhereInput.md) | No |  |
| `replication_target_executions_some` | [ReplicationTargetExecutionWhereInput](../Replication/ReplicationTargetExecutionWhereInput.md) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_in` | Array of [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_not` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resiliency_type_not_in` | Array of [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `resource_version` | integer (int32) | No |  |
| `resource_version_gt` | integer (int32) | No |  |
| `resource_version_gte` | integer (int32) | No |  |
| `resource_version_in` | integer[] | No |  |
| `resource_version_lt` | integer (int32) | No |  |
| `resource_version_lte` | integer (int32) | No |  |
| `resource_version_not` | integer (int32) | No |  |
| `resource_version_not_in` | integer[] | No |  |
| `snapshot_consistent_type` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `snapshot_consistent_type_in` | Array of [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `snapshot_consistent_type_not` | [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `snapshot_consistent_type_not_in` | Array of [ConsistentType](../Consistent/ConsistentType.md) | No |  |
| `status` | [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `status_in` | Array of [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `status_not` | [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `status_not_in` | Array of [BackupPlanStatus](../Backup/BackupPlanStatus.md) | No |  |
| `storage_encrypted` | boolean | No |  |
| `storage_encrypted_not` | boolean | No |  |
| `storage_policy` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `storage_policy_in` | Array of [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `storage_policy_not` | [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `storage_policy_not_in` | Array of [VmVolumeElfStoragePolicyType](../Vm/VmVolumeElfStoragePolicyType.md) | No |  |
| `target_cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `target_replication_service` | [ReplicationServiceWhereInput](../Replication/ReplicationServiceWhereInput.md) | No |  |
| `thin_provision` | boolean | No |  |
| `thin_provision_not` | boolean | No |  |
| `type` | [ReplicationPlanType](../Replication/ReplicationPlanType.md) | No |  |
| `type_in` | Array of [ReplicationPlanType](../Replication/ReplicationPlanType.md) | No |  |
| `type_not` | [ReplicationPlanType](../Replication/ReplicationPlanType.md) | No |  |
| `type_not_in` | Array of [ReplicationPlanType](../Replication/ReplicationPlanType.md) | No |  |
| `updatedAt` | string | No |  |
| `updatedAt_gt` | string | No |  |
| `updatedAt_gte` | string | No |  |
| `updatedAt_in` | string[] | No |  |
| `updatedAt_lt` | string | No |  |
| `updatedAt_lte` | string | No |  |
| `updatedAt_not` | string | No |  |
| `updatedAt_not_in` | string[] | No |  |
| `vms_every` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_none` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vms_some` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |

