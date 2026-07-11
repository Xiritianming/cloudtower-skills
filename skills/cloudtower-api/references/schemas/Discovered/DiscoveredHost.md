# DiscoveredHost

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `all_flash` | boolean | Yes |  |
| `disks` | Array of [NestedDiscoveredHostDisk](../Nested/NestedDiscoveredHostDisk.md) | Yes |  |
| `host_ip` | string | Yes |  |
| `host_uuid` | string | Yes |  |
| `hostname` | string | Yes |  |
| `ifaces` | Array of [NestedDiscoveredHostIface](../Nested/NestedDiscoveredHostIface.md) | Yes |  |
| `serial` | string | Yes |  |
| `sockets` | integer (int32) | Yes |  |
| `version` | string | Yes |  |
| `deployed` | boolean | No |  |
| `dimms` | Array of [NestedDiscoveredHostDimms](../Nested/NestedDiscoveredHostDimms.md) | No |  |
| `ipmi_ip` | string | No |  |
| `is_os_in_raid1` | boolean | No |  |
| `product` | string | No |  |
| `zbs_spec` | string | No |  |

