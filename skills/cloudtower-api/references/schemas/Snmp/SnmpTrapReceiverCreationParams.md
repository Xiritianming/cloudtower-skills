# SnmpTrapReceiverCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `language_code` | [SnmpLanguageCode](../Snmp/SnmpLanguageCode.md) | Yes |  |
| `port` | integer (int32) | Yes |  |
| `host` | string | Yes |  |
| `protocol` | [SnmpProtocol](../Snmp/SnmpProtocol.md) | Yes |  |
| `version` | [SnmpVersion](../Snmp/SnmpVersion.md) | Yes |  |
| `name` | string | Yes |  |
| `cluster_id` | string | Yes |  |
| `disabled` | boolean | No |  |
| `inform` | boolean | No |  |
| `engine_id` | string | No |  |
| `privacy_protocol` | [SnmpPrivacyProtocol](../Snmp/SnmpPrivacyProtocol.md) | No |  |
| `privacy_pass_phrase` | string | No |  |
| `auth_protocol` | [SnmpAuthProtocol](../Snmp/SnmpAuthProtocol.md) | No |  |
| `auth_pass_phrase` | string | No |  |
| `username` | string | No |  |
| `community` | string | No |  |

