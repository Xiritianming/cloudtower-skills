# ContentLibraryVmTemplateCreationParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | Yes |  |
| `vm` | [VmWhereUniqueInput](../Vm/VmWhereUniqueInput.md) | Yes |  |
| `name` | string | Yes |  |
| `cloud_init_supported` | boolean | No |  |
| `description` | string | No |  |

