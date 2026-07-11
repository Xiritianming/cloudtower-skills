# SnmpTransportUpdationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [SnmpTransportWhereInput](../Snmp/SnmpTransportWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disabled` | boolean | No |  |
| `privacy_protocol` | [SnmpPrivacyProtocol](../Snmp/SnmpPrivacyProtocol.md) | No |  |
| `privacy_pass_phrase` | string | No |  |
| `auth_protocol` | [SnmpAuthProtocol](../Snmp/SnmpAuthProtocol.md) | No |  |
| `auth_pass_phrase` | string | No |  |
| `username` | string | No |  |
| `community` | string | No |  |
| `port` | integer (int32) | No |  |
| `protocol` | [SnmpProtocol](../Snmp/SnmpProtocol.md) | No |  |
| `version` | [SnmpVersion](../Snmp/SnmpVersion.md) | No |  |
| `name` | string | No |  |

