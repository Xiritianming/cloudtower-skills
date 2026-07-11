# SnmpTransportCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `port` | integer (int32) | Yes |  |
| `protocol` | [SnmpProtocol](../Snmp/SnmpProtocol.md) | Yes |  |
| `version` | [SnmpVersion](../Snmp/SnmpVersion.md) | Yes |  |
| `name` | string | Yes |  |
| `cluster_id` | string | Yes |  |
| `disabled` | boolean | No |  |
| `privacy_protocol` | [SnmpPrivacyProtocol](../Snmp/SnmpPrivacyProtocol.md) | No |  |
| `privacy_pass_phrase` | string | No |  |
| `auth_protocol` | [SnmpAuthProtocol](../Snmp/SnmpAuthProtocol.md) | No |  |
| `auth_pass_phrase` | string | No |  |
| `username` | string | No |  |
| `community` | string | No |  |

