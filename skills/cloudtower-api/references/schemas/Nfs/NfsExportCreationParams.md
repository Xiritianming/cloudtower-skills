# NfsExportCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster_id` | string | Yes |  |
| `thin_provision` | boolean | Yes |  |
| `replica_num` | integer (int32) | Yes |  |
| `name` | string | Yes |  |
| `encrypt_method` | [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `ec_m` | number (double) | No |  |
| `ec_k` | number (double) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `ip_whitelist` | string | No |  |

