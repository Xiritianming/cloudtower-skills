# VmNic

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `guest_info_ip_addresses` | string[] | Yes |  |
| `guest_info_ip_addresses_v6` | string[] | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `vm` | [NestedVm](../Nested/NestedVm.md) | Yes |  |
| `dpi_enabled` | boolean | No |  |
| `egress_rate_limit_burst_in_bit` | number (double) | No |  |
| `egress_rate_limit_enabled` | boolean | No |  |
| `egress_rate_limit_max_rate_in_bitps` | number (double) | No |  |
| `enabled` | boolean | No |  |
| `gateway` | string | No |  |
| `ingress_rate_limit_burst_in_bit` | number (double) | No |  |
| `ingress_rate_limit_enabled` | boolean | No |  |
| `ingress_rate_limit_max_rate_in_bitps` | number (double) | No |  |
| `interface_id` | string | No |  |
| `ip_address` | string | No |  |
| `mac_address` | string | No |  |
| `mirror` | boolean | No |  |
| `model` | any | No |  |
| `nic` | any | No |  |
| `order` | integer (int32) | No |  |
| `subnet_mask` | string | No |  |
| `type` | any | No |  |
| `vlan` | any | No |  |
| `vpc_nic` | any | No |  |

