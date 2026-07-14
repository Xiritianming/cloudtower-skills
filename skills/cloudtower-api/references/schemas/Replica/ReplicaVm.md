# ReplicaVm

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `createdAt` | string | Yes |  |
| `id` | string | Yes |  |
| `origin_object_descriptor` | [NestedReplicationObjectDescriptor](../Nested/NestedReplicationObjectDescriptor.md) | Yes |  |
| `replication_service` | [NestedReplicationService](../Nested/NestedReplicationService.md) | Yes |  |
| `state` | [ReplicaVmState](../Replica/ReplicaVmState.md) | Yes |  |
| `type` | [ReplicationObjectType](../Replication/ReplicationObjectType.md) | Yes |  |
| `updatedAt` | string | Yes |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `external_cloudtower` | [NestedExternalCloudTower](../Nested/NestedExternalCloudTower.md) | No |  |
| `failover_test_object_descriptor` | [NestedReplicationObjectDescriptor](../Nested/NestedReplicationObjectDescriptor.md) | No |  |
| `failover_test_replica_group` | string | No |  |
| `failover_test_vm` | [NestedVm](../Nested/NestedVm.md) | No |  |
| `inbound` | boolean | No |  |
| `iscsi_lun` | [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `object_descriptor` | [NestedReplicationObjectDescriptor](../Nested/NestedReplicationObjectDescriptor.md) | No |  |
| `origin_iscsi_lun` | [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `origin_vm` | [NestedVm](../Nested/NestedVm.md) | No |  |
| `origin_vm_cluster_local_id` | string | No |  |
| `origin_vm_cluster_name` | string | No |  |
| `origin_vm_local_id` | string | No |  |
| `origin_vm_name` | string | No |  |
| `replica_group` | string | No |  |
| `replication_group` | string | No |  |
| `replication_plan` | [NestedReplicationPlan](../Nested/NestedReplicationPlan.md) | No |  |
| `replication_target_executions` | Array of [NestedReplicationTargetExecution](../Nested/NestedReplicationTargetExecution.md) | No |  |
| `restore_points` | Array of [NestedReplicationRestorePoint](../Nested/NestedReplicationRestorePoint.md) | No |  |
| `targets_deletable` | boolean | No |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | No |  |

