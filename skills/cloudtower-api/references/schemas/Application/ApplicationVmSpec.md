# ApplicationVmSpec

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `vmUsage` | [VmUsage](../Vm/VmUsage.md) | No |  |
| `storages` | Array of [ApplicationVmSpecStorage](../Application/ApplicationVmSpecStorage.md) | No |  |
| `status` | [ApplicationVmSpecStatus](../Application/ApplicationVmSpecStatus.md) | No |  |
| `publicKeys` | string[] | No |  |
| `network` | [ApplicationVmSpecNetwork](../Application/ApplicationVmSpecNetwork.md) | No |  |
| `name` | string | No |  |
| `memory_unit` | [ByteUnit](../Byte/ByteUnit.md) | No |  |
| `memory` | integer (int64) | No |  |
| `internal` | boolean | No |  |
| `image` | string | No |  |
| `host` | string | No |  |
| `env` | Array of [ApplicationVmSpecEnv](../Application/ApplicationVmSpecEnv.md) | No |  |
| `cpu` | integer (int32) | No |  |
| `cluster` | string | No |  |
| `cloudInitUserData` | string | No |  |

