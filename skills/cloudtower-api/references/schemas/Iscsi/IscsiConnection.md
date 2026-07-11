# IscsiConnection

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `client_port` | integer (int32) | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `host` | [NestedHost](../Nested/NestedHost.md) | Yes |  |
| `id` | string | Yes |  |
| `initiator_ip` | string | Yes |  |
| `type` | [StoreConnectionType](../Store/StoreConnectionType.md) | Yes |  |
| `iscsi_target` | any | No |  |
| `nvmf_subsystem` | any | No |  |
| `tr_type` | any | No |  |

