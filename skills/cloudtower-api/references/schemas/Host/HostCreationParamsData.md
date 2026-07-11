# HostCreationParamsData

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ifaces` | Array of [HostBatchCreateIfaceInput](../Host/HostBatchCreateIfaceInput.md) | Yes |  |
| `disks` | Array of [HostBatchCreateDiskInput](../Host/HostBatchCreateDiskInput.md) | Yes |  |
| `hostname` | string | Yes |  |
| `host_uuid` | string | Yes |  |
| `host_ip` | string | Yes |  |
| `vdses` | Array of [HostVdsConfig](../Host/HostVdsConfig.md) | No |  |
| `zbs_spec` | [ZbsSpec](../Zbs/ZbsSpec.md) | No |  |
| `platform_password` | string | No |  |
| `platform_username` | string | No |  |
| `platform_ip` | string | No |  |
| `ipmi` | [HostBatchCreateIpmiInput](../Host/HostBatchCreateIpmiInput.md) | No |  |

