# UserAuditLog

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `action` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `id` | string | Yes |  |
| `ip_address` | string | Yes |  |
| `message` | string | Yes |  |
| `auth_type` | string | No |  |
| `cluster` | [NestedCluster](../Nested/NestedCluster.md) | No |  |
| `finished_at` | string | No |  |
| `resource_id` | string | No |  |
| `resource_type` | string | No |  |
| `started_at` | string | No |  |
| `status` | [UserAuditLogStatus](../User/UserAuditLogStatus.md) | No |  |
| `user` | [NestedUser](../Nested/NestedUser.md) | No |  |
| `username` | string | No |  |

