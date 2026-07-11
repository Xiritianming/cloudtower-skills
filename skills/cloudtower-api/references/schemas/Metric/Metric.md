# Metric

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `unit` | [MetricUnit](../Metric/MetricUnit.md) | Yes |  |
| `step` | integer (int32) | Yes |  |
| `dropped` | boolean | Yes |  |
| `samples` | Array of [MetricSample](../Metric/MetricSample.md) | No |  |
| `sample_streams` | Array of [MetricStream](../Metric/MetricStream.md) | No |  |
| `__typename` | enum: Metric | No |  |

