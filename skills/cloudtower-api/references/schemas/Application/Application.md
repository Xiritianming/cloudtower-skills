# Application

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `state` | [ApplicationState](../Application/ApplicationState.md) | Yes |  |
| `storage_ip` | string | Yes |  |
| `type` | [ApplicationType](../Application/ApplicationType.md) | Yes |  |
| `vcpu` | integer (int32) | Yes |  |
| `version` | string | Yes |  |
| `volume_size` | integer (int64) | Yes |  |
| `error_message` | string | No |  |
| `image_name` | string | No |  |
| `update_time` | string | No |  |
| `vm` | any | No |  |

