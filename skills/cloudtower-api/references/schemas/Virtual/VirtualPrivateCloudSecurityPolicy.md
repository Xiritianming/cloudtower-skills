# VirtualPrivateCloudSecurityPolicy

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `apply_to` | Array of [NestedVirtualPrivateCloudSecurityPolicyApply](../Nested/NestedVirtualPrivateCloudSecurityPolicyApply.md) | Yes |  |
| `id` | string | Yes |  |
| `local_id` | string | Yes |  |
| `name` | string | Yes |  |
| `vpc` | [NestedVirtualPrivateCloud](../Nested/NestedVirtualPrivateCloud.md) | Yes |  |
| `description` | string | No |  |
| `egress` | Array of [NestedVirtualPrivateCloudNetworkPolicyRule](../Nested/NestedVirtualPrivateCloudNetworkPolicyRule.md) | No |  |
| `entityAsyncStatus` | any | No |  |
| `ingress` | Array of [NestedVirtualPrivateCloudNetworkPolicyRule](../Nested/NestedVirtualPrivateCloudNetworkPolicyRule.md) | No |  |
| `policy_mode` | any | No |  |

