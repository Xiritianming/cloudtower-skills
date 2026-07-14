# AlertNotifier

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disabled` | boolean | Yes |  |
| `email_tos` | string[] | Yes |  |
| `id` | string | Yes |  |
| `notice_severities` | string[] | Yes |  |
| `clusters` | Array of [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `email_from` | string | No |  |
| `entityAsyncStatus` | [EntityAsyncStatus](../Entity/EntityAsyncStatus.md) | No |  |
| `language_code` | [NotifierLanguageCode](../Notifier/NotifierLanguageCode.md) | No |  |
| `name` | string | No |  |
| `security_mode` | [NotifierSecurityMode](../Notifier/NotifierSecurityMode.md) | No |  |
| `smtp_server_config` | [NestedSmtpServer](../Nested/NestedSmtpServer.md) | No |  |
| `smtp_server_host` | string | No |  |
| `smtp_server_port` | integer (int32) | No |  |
| `username` | string | No |  |

