# NestedContentLibraryVmTemplateNic

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `index` | integer (int32) | Yes |  |
| `egress_rate_limit_burst_in_bit` | number (double) | No |  |
| `egress_rate_limit_enabled` | boolean | No |  |
| `egress_rate_limit_max_rate_in_bitps` | number (double) | No |  |
| `enabled` | boolean | No |  |
| `ingress_rate_limit_burst_in_bit` | number (double) | No |  |
| `ingress_rate_limit_enabled` | boolean | No |  |
| `ingress_rate_limit_max_rate_in_bitps` | number (double) | No |  |
| `mirror` | boolean | No |  |
| `model` | [VmNicModel](../Vm/VmNicModel.md) | No |  |
| `type` | [VmNicType](../Vm/VmNicType.md) | No |  |
| `vlan` | [NestedFrozenVlan](../Nested/NestedFrozenVlan.md) | No |  |
| `vpc_nic` | [NestedTemplateVpcNic](../Nested/NestedTemplateVpcNic.md) | No |  |

