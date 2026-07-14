# SnmpTransport

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | Yes |  |
| `disabled` | boolean | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `port` | integer (int32) | Yes |  |
| `protocol` | [SnmpProtocol](../Snmp/SnmpProtocol.md) | Yes |  |
| `version` | [SnmpVersion](../Snmp/SnmpVersion.md) | Yes |  |
| `auth_pass_phrase` | string | No |  |
| `auth_protocol` | [SnmpAuthProtocol](../Snmp/SnmpAuthProtocol.md) | No |  |
| `community` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `privacy_pass_phrase` | string | No |  |
| `privacy_protocol` | [SnmpPrivacyProtocol](../Snmp/SnmpPrivacyProtocol.md) | No |  |
| `username` | string | No |  |

