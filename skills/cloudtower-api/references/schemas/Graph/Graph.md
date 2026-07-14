# Graph

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `instance_ids` | string[] | Yes |  |
| `local_id` | string | Yes |  |
| `metric_count` | integer (int32) | Yes |  |
| `metric_name` | string | Yes |  |
| `metric_type` | [MetricType](../Metric/MetricType.md) | Yes |  |
| `resource_type` | string | Yes |  |
| `targets` | object | Yes |  |
| `title` | string | Yes |  |
| `type` | [GraphType](../Graph/GraphType.md) | Yes |  |
| `view` | [NestedView](../Nested/NestedView.md) | Yes |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `disks` | Array of [NestedDisk](../Nested/NestedDisk.md) | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `hosts` | Array of [NestedHost](../Nested/NestedHost.md) | No |  |
| `luns` | Array of [NestedIscsiLun](../Nested/NestedIscsiLun.md) | No |  |
| `namespaces` | Array of [NestedNvmfNamespace](../Nested/NestedNvmfNamespace.md) | No |  |
| `network` | [NetworkType](../Network/NetworkType.md) | No |  |
| `nics` | Array of [NestedNic](../Nested/NestedNic.md) | No |  |
| `service` | string | No |  |
| `vmNics` | Array of [NestedVmNic](../Nested/NestedVmNic.md) | No |  |
| `vmVolumes` | Array of [NestedVmVolume](../Nested/NestedVmVolume.md) | No |  |
| `vms` | Array of [NestedVm](../Nested/NestedVm.md) | No |  |
| `witnesses` | Array of [NestedWitness](../Nested/NestedWitness.md) | No |  |
| `zones` | Array of [NestedZone](../Nested/NestedZone.md) | No |  |

## Nested Fields

### `targets`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


