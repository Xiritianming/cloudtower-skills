# POST /v2/api/backup-rebuild-vm

**Resource:** [BackupPlan](../resources/BackupPlan.md)
**Operation ID:** `BackupRebuildVm`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [BackupRestorePointRebuildParams](../schemas/Backup/BackupRestorePointRebuildParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "data": {
    "rebuild_network_mapping": [
      {
        "src_vlan_id": "<src_vlan_id>",
        "dst_vlan_id": "<dst_vlan_id>"
      }
    ],
    "rebuild_target_host_id": "<rebuild_target_host_id>",
    "rebuild_target_cluster_id": "<rebuild_target_cluster_id>",
    "rebuild_name": "<rebuild_name>",
    "startup_after_restore": false
  },
  "where": {}
}
```

Validate the body, then send (paths relative to the skill root):

```bash
python3 scripts/validate.py BackupRebuildVm /tmp/body.json
bash scripts/call.sh /v2/api/backup-rebuild-vm /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_BackupRestoreExecution_](../schemas/With/WithTask-BackupRestoreExecution.md)

## Security

- **Authorization**
