# POST /v2/api/create-backup-plan

**Resource:** [BackupPlan](../resources/BackupPlan.md)
**Operation ID:** `CreateBackupPlan`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [BackupPlanCreationParams](../schemas/Backup/BackupPlanCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "keep_policy_value": 1,
    "keep_policy": "COUNT",
    "enable_window": false,
    "full_time_point": {
      "minute": 1,
      "hour": 1
    },
    "full_period": "DAILY",
    "full_interval": 1,
    "incremental_interval": 1,
    "incremental_period": "DAILY",
    "snapshot_consistent_type": "CRASH_CONSISTENT",
    "compression": false,
    "vms": {},
    "backup_store_repository_id": "<backup_store_repository_id>",
    "backup_service_id": "<backup_service_id>",
    "name": "<name>"
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateBackupPlan /tmp/body.json
bash scripts/call.sh /v2/api/create-backup-plan /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_BackupPlan_](../schemas/With/WithTask-BackupPlan.md)

## Security

- **Authorization**
