# VirtualPrivateCloudNatGatewayUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [VirtualPrivateCloudNatGatewayWhereInput](../Virtual/VirtualPrivateCloudNatGatewayWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `external_ips` | Array of [VirtualPrivateCloudExternalIpsParams](../Virtual/VirtualPrivateCloudExternalIpsParams.md) | No |  |
| `external_ip` | string | No |  |
| `dnat_rules` | Array of [VirtualPrivateCloudDnatRuleParams](../Virtual/VirtualPrivateCloudDnatRuleParams.md) | No |  |
| `enable_dnat` | boolean | No |  |
| `enable_snat` | boolean | No |  |
| `name` | string | No |  |

