# GraphUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `where` | [GraphWhereInput](../Graph/GraphWhereInput.md) | Yes |  |
| `data` | object | No |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `instance_ids` | string[] | No |  |
| `luns` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `vmNics` | [VmNicWhereInput](../Vm/VmNicWhereInput.md) | No |  |
| `nics` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `disks` | [DiskWhereInput](../Disk/DiskWhereInput.md) | No |  |
| `vmVolumes` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | No |  |
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `hosts` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `network` | [NetworkType](../Network/NetworkType.md) | No |  |
| `cluster` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |
| `service` | string | No |  |
| `metric_type` | [MetricType](../Metric/MetricType.md) | No |  |
| `metric_count` | integer (int32) | No |  |
| `type` | [GraphType](../Graph/GraphType.md) | No |  |
| `resource_type` | string | No |  |
| `title` | string | No |  |
| `metric_name` | string | No |  |
| `connect_id` | string[] | No |  |

