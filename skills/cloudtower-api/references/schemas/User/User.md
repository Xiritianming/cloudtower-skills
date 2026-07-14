# User

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `display_username` | string | Yes |  |
| `id` | string | Yes |  |
| `internal` | boolean | Yes |  |
| `name` | string | Yes |  |
| `source` | [UserSource](../User/UserSource.md) | Yes |  |
| `username` | string | Yes |  |
| `auth_config_id` | string | No |  |
| `email_address` | string | No |  |
| `ldap_dn` | string | No |  |
| `mobile_phone` | string | No |  |
| `password_expired` | boolean | No |  |
| `password_recover_qa` | [NestedPasswordRecoverQa](../Nested/NestedPasswordRecoverQa.md) | No |  |
| `password_updated_at` | string | No |  |
| `role` | [UserRole](../User/UserRole.md) | No |  |
| `roles` | Array of [NestedUserRoleNext](../Nested/NestedUserRoleNext.md) | No |  |

