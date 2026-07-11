# IscsiTargetCommonParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `business_host_groups` | [BusinessHostGroupWhereInput](../Business/BusinessHostGroupWhereInput.md) | No |  |
| `business_hosts` | [BusinessHostWhereInput](../Business/BusinessHostWhereInput.md) | No |  |
| `configuration_adaptive` | boolean | No |  |
| `configuration_method` | [ConfigurationMethod](../Configuration/ConfigurationMethod.md) | No |  |
| `encrypt_method` | [EncryptMethod](../Encrypt/EncryptMethod.md) | No |  |
| `prioritized` | boolean | No |  |
| `ec_m` | number (double) | No |  |
| `ec_k` | number (double) | No |  |
| `resiliency_type` | [ResiliencyType](../Resiliency/ResiliencyType.md) | No |  |
| `bps_wr_max_length` | integer (int64) | No |  |
| `bps_wr_max_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps_wr_max_size` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps_wr_max` | integer (int64) | No |  |
| `bps_rd_max_length` | integer (int64) | No |  |
| `bps_rd_max_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps_rd_max` | integer (int64) | No |  |
| `bps_max_length` | integer (int64) | No |  |
| `bps_max_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps_max` | integer (int64) | No |  |
| `iops_wr_max_length` | integer (int64) | No |  |
| `iops_wr_max` | integer (int64) | No |  |
| `iops_rd_max_length` | integer (int64) | No |  |
| `iops_rd_max` | integer (int64) | No |  |
| `iops_max_length` | integer (int64) | No |  |
| `iops_max` | integer (int64) | No |  |
| `bps_wr_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps_wr` | integer (int64) | No |  |
| `bps_rd_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps_rd` | integer (int64) | No |  |
| `bps_unit` | [BPSUnit](../BPSUnit/BPSUnit.md) | No |  |
| `bps` | integer (int64) | No |  |
| `iops_wr` | integer (int64) | No |  |
| `iops_rd` | integer (int64) | No |  |
| `iops` | integer (int64) | No |  |
| `initiator_chaps` | Array of [IscsiTargetCommonParamsInitiatorChaps](../Iscsi/IscsiTargetCommonParamsInitiatorChaps.md) | No |  |
| `chap_secret` | string | No |  |
| `chap_name` | string | No |  |
| `chap_enabled` | boolean | No |  |
| `description` | string | No |  |
| `iqn_whitelist` | string | No |  |
| `ip_whitelist` | string | No |  |

