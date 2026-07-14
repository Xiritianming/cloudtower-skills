# POST /v2/api/get-cluster-pin-in-performance-info

**Resource:** [Cluster](../resources/Cluster.md)
**Operation ID:** `GetClusterPinInPerformanceInfo`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `external-cloudtower-id` | header | string | No |  |

## Request Body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [GetClusterPinInPerformanceInfoRequestBody](../schemas/Get/GetClusterPinInPerformanceInfoRequestBody.md)

> `where` filters use flat suffix syntax (`id_in`, `name_contains`, …) — see the [Query Guide](../querying.md) for filter, counting, and pagination syntax.

## Example

Minimal request body — every required field, optional fields omitted. Copy it, then replace every placeholder with a real value: `<...>` strings, the numbers (`1`) and booleans, and each enum value (one allowed value is shown; the linked schemas list the alternatives). To add an optional field, read its schema link above first.

```json
{
  "where": {}
}
```

Validate the body, then send:

```bash
cd <skill-root>   # the directory containing SKILL.md
python3 scripts/validate.py GetClusterPinInPerformanceInfo /tmp/body.json
bash scripts/call.sh /v2/api/get-cluster-pin-in-performance-info /tmp/body.json
```

## Responses

| Status | Description |
|--------|-------------|
| 200 |  |
| 400 | Bad request |
| 404 | Not found |
| 500 | Server error |

**Success Response Schema:**

Array of [ClusterPinInPerformanceInfo](../schemas/Cluster/ClusterPinInPerformanceInfo.md)

## Security

- **Authorization**
