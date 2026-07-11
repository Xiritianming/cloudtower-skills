# LogCollectionCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `log_ended_at` | string (date-time) | Yes |  |
| `log_started_at` | string (date-time) | Yes |  |
| `cluster_id` | string | Yes |  |
| `hosts` | [HostWhereInput](../Host/HostWhereInput.md) | Yes |  |
| `witness_id` | string | No |  |
| `service_groups` | Array of [LogCollectionServiceGroupParams](../Log/LogCollectionServiceGroupParams.md) | No |  |

