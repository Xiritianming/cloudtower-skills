# POST /v2/api/update-global-recycle-bin-setting

**Resource:** [GlobalSettings](../resources/GlobalSettings.md)
**Operation ID:** `UpdateGlobalRecycleBinSetting`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content-language` | header | ContentLanguage | No |  |
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [GlobalRecycleBinUpdationParams](../schemas/Global/GlobalRecycleBinUpdationParams.md)

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "retain": 1,
  "enabled": false
}
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py UpdateGlobalRecycleBinSetting /tmp/body.json
bash scripts/call.sh /v2/api/update-global-recycle-bin-setting /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

[WithTask_GlobalSettings_](../schemas/With/WithTask-GlobalSettings.md)

## Security

- **Authorization**
