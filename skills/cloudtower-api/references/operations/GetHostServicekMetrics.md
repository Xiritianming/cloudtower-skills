# POST /v2/api/get-host-service-metrics

**Resource:** [Metrics](../resources/Metrics.md)
**Operation ID:** `GetHostServicekMetrics`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [GetHostServiceMetricInput](../schemas/Get/GetHostServiceMetricInput.md)

> **`metrics` values are free strings the schema cannot validate** — see the [Metric Names Guide](../metrics-guide.md) for known names and a discovery recipe. A `200` response with empty `samples` almost always means a wrong metric name.

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "range": "<range>",
  "hosts": {},
  "services": [
    "<services>"
  ],
  "metrics": [
    "<metrics>"
  ]
}
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py GetHostServicekMetrics /tmp/body.json
bash scripts/call.sh /v2/api/get-host-service-metrics /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [WithTask_Metric_](../schemas/With/WithTask-Metric.md)

## Security

- **Authorization**
