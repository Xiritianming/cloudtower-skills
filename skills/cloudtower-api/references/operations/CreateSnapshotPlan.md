# POST /v2/api/create-snapshot-plan

**Resource:** [SnapshotPlan](../resources/SnapshotPlan.md)
**Operation ID:** `CreateSnapshotPlan`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [SnapshotPlanCreationParams](../schemas/Snapshot/SnapshotPlanCreationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
[
  {
    "vm_ids": [
      "<vm_ids>"
    ],
    "execute_intervals": [
      1
    ],
    "execute_plan_type": "DAY",
    "start_time": "<start_time>",
    "remain_snapshot_num": 1,
    "cluster_id": "<cluster_id>",
    "name": "<name>"
  }
]
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py CreateSnapshotPlan /tmp/body.json
bash scripts/call.sh /v2/api/create-snapshot-plan /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_SnapshotPlan_](../schemas/With/WithTask-SnapshotPlan.md)

## Security

- **Authorization**
