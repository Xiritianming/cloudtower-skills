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
| `auth_protocol` | any | No |  |
| `community` | string | No |  |
| `entityAsyncStatus` | any | No |  |
| `privacy_pass_phrase` | string | No |  |
| `privacy_protocol` | any | No |  |
| `username` | string | No |  |

