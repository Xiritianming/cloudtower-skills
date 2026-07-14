# IscsiConnectionWhereInput

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `AND` | Array of [IscsiConnectionWhereInput](../Iscsi/IscsiConnectionWhereInput.md) | No |  |
| `NOT` | Array of [IscsiConnectionWhereInput](../Iscsi/IscsiConnectionWhereInput.md) | No |  |
| `OR` | Array of [IscsiConnectionWhereInput](../Iscsi/IscsiConnectionWhereInput.md) | No |  |
| `client_port` | integer (int32) | No |  |
| `client_port_gt` | integer (int32) | No |  |
| `client_port_gte` | integer (int32) | No |  |
| `client_port_in` | integer[] | No |  |
| `client_port_lt` | integer (int32) | No |  |
| `client_port_lte` | integer (int32) | No |  |
| `client_port_not` | integer (int32) | No |  |
| `client_port_not_in` | integer[] | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `host` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
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
| `initiator_ip` | string | No |  |
| `initiator_ip_contains` | string | No |  |
| `initiator_ip_ends_with` | string | No |  |
| `initiator_ip_gt` | string | No |  |
| `initiator_ip_gte` | string | No |  |
| `initiator_ip_in` | string[] | No |  |
| `initiator_ip_lt` | string | No |  |
| `initiator_ip_lte` | string | No |  |
| `initiator_ip_not` | string | No |  |
| `initiator_ip_not_contains` | string | No |  |
| `initiator_ip_not_ends_with` | string | No |  |
| `initiator_ip_not_in` | string[] | No |  |
| `initiator_ip_not_starts_with` | string | No |  |
| `initiator_ip_starts_with` | string | No |  |
| `iscsi_target` | [IscsiTargetWhereInput](../Iscsi/IscsiTargetWhereInput.md) | No |  |
| `nvmf_subsystem` | [NvmfSubsystemWhereInput](../Nvmf/NvmfSubsystemWhereInput.md) | No |  |
| `tr_type` | [StoreTransportType](../Store/StoreTransportType.md) | No |  |
| `tr_type_in` | Array of [StoreTransportType](../Store/StoreTransportType.md) | No |  |
| `tr_type_not` | [StoreTransportType](../Store/StoreTransportType.md) | No |  |
| `tr_type_not_in` | Array of [StoreTransportType](../Store/StoreTransportType.md) | No |  |
| `type` | [StoreConnectionType](../Store/StoreConnectionType.md) | No |  |
| `type_in` | Array of [StoreConnectionType](../Store/StoreConnectionType.md) | No |  |
| `type_not` | [StoreConnectionType](../Store/StoreConnectionType.md) | No |  |
| `type_not_in` | Array of [StoreConnectionType](../Store/StoreConnectionType.md) | No |  |

