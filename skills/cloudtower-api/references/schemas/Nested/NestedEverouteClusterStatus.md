# NestedEverouteClusterStatus

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `agents` | [NestedEverouteClusterAgentStatus](../Nested/NestedEverouteClusterAgentStatus.md) | No |  |
| `conditions` | Array of [NestedEverouteClusterCondition](../Nested/NestedEverouteClusterCondition.md) | No |  |
| `controllers` | [NestedEverouteClusterControllerStatus](../Nested/NestedEverouteClusterControllerStatus.md) | No |  |
| `message` | string | No |  |
| `phase` | [EverouteClusterPhase](../Everoute/EverouteClusterPhase.md) | No |  |
| `reason` | string | No |  |
| `retryCount` | integer (int32) | No |  |
| `version` | string | No |  |

