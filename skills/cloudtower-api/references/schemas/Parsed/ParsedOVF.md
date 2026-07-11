# ParsedOVF

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `firmware` | [VmFirmware](../Vm/VmFirmware.md) | Yes |  |
| `disks` | Array of [OvfDisk](../Ovf/OvfDisk.md) | Yes |  |
| `nics` | Array of [OvfNic](../Ovf/OvfNic.md) | Yes |  |
| `memory` | integer (int64) | Yes |  |
| `cpu` | [OvfCpu](../Ovf/OvfCpu.md) | Yes |  |
| `vcpu` | integer (int32) | Yes |  |
| `name` | string | Yes |  |
| `description` | string | No |  |

