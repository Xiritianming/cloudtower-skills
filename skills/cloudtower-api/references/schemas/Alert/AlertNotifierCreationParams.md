# AlertNotifierCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `notice_severities` | string[] | Yes |  |
| `language_code` | [NotifierLanguageCode](../Notifier/NotifierLanguageCode.md) | Yes |  |
| `email_tos` | string[] | Yes |  |
| `email_from` | string | Yes |  |
| `disabled` | boolean | Yes |  |
| `smtp_server_id` | string | Yes |  |
| `name` | string | Yes |  |
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | Yes |  |

