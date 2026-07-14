# CloudTowerApplication

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes |  |
| `instanceStatuses` | object | Yes |  |
| `name` | string | Yes |  |
| `resourceVersion` | integer (int32) | Yes |  |
| `targetPackage` | string | Yes |  |
| `vmSpec` | object | Yes |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `package` | [NestedCloudTowerApplicationPackage](../Nested/NestedCloudTowerApplicationPackage.md) | No |  |
| `placementSituation` | string | No |  |
| `placementVerb` | string | No |  |
| `state` | [CloudTowerApplicationState](../Cloud/CloudTowerApplicationState.md) | No |  |
| `user` | [NestedUser](../Nested/NestedUser.md) | No |  |

## Nested Fields

### `instanceStatuses`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


### `vmSpec`

| Field | Type | Required | Description |
|-------|------|----------|-------------|


