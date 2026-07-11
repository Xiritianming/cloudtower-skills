# TableReporterParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `filter` | object | Yes |  |
| `columns` | Array of [ColumnConfig](../Column/ColumnConfig.md) | Yes |  |
| `name` | string | Yes |  |

## Nested Fields

### `filter`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `nvmfSubsystems` | [GetNvmfSubsystemsRequestBody](../Get/GetNvmfSubsystemsRequestBody.md) | No |  |
| `contentLibraryVmTemplates` | [GetContentLibraryVmTemplatesRequestBody](../Get/GetContentLibraryVmTemplatesRequestBody.md) | No |  |
| `nvmfNamespaceSnapshots` | [GetNvmfNamespaceSnapshotsRequestBody](../Get/GetNvmfNamespaceSnapshotsRequestBody.md) | No |  |
| `contentLibraryImages` | [GetContentLibraryImagesRequestBody](../Get/GetContentLibraryImagesRequestBody.md) | No |  |
| `nvmfNamespaces` | [GetNvmfNamespacesRequestBody](../Get/GetNvmfNamespacesRequestBody.md) | No |  |
| `namespaceGroups` | [GetNamespaceGroupsRequestBody](../Get/GetNamespaceGroupsRequestBody.md) | No |  |
| `iscsiLuns` | [GetIscsiLunsRequestBody](../Get/GetIscsiLunsRequestBody.md) | No |  |
| `tasks` | [GetTasksRequestBody](../Get/GetTasksRequestBody.md) | No |  |
| `userAuditLogs` | [GetUserAuditLogsRequestBody](../Get/GetUserAuditLogsRequestBody.md) | No |  |
| `systemAuditLogs` | [GetSystemAuditLogsRequestBody](../Get/GetSystemAuditLogsRequestBody.md) | No |  |
| `iscsiLunSnapshots` | [GetIscsiLunSnapshotsRequestBody](../Get/GetIscsiLunSnapshotsRequestBody.md) | No |  |
| `iscsiConnections` | [GetIscsiConnectionsRequestBody](../Get/GetIscsiConnectionsRequestBody.md) | No |  |
| `consistencyGroups` | [GetConsistencyGroupsRequestBody](../Get/GetConsistencyGroupsRequestBody.md) | No |  |
| `users` | [GetUsersRequestBody](../Get/GetUsersRequestBody.md) | No |  |
| `vmEntityFilters` | [GetEntityFiltersRequestBody](../Get/GetEntityFiltersRequestBody.md) | No |  |
| `snapshotPlans` | [GetSnapshotPlansRequestBody](../Get/GetSnapshotPlansRequestBody.md) | No |  |
| `globalAlertRules` | [GetGlobalAlertRulesRequestBody](../Get/GetGlobalAlertRulesRequestBody.md) | No |  |
| `alerts` | [GetAlertsRequestBody](../Get/GetAlertsRequestBody.md) | No |  |
| `vmPlacementGroups` | [GetVmPlacementGroupsRequestBody](../Get/GetVmPlacementGroupsRequestBody.md) | No |  |
| `vmTemplates` | [GetVmTemplatesRequestBody](../Get/GetVmTemplatesRequestBody.md) | No |  |
| `elfImages` | [GetElfImagesRequestBody](../Get/GetElfImagesRequestBody.md) | No |  |
| `vmVolumes` | [GetVmVolumesRequestBody](../Get/GetVmVolumesRequestBody.md) | No |  |
| `vlans` | [GetVlansRequestBody](../Get/GetVlansRequestBody.md) | No |  |
| `disks` | [GetDisksRequestBody](../Get/GetDisksRequestBody.md) | No |  |
| `vdses` | [GetVdsesRequestBody](../Get/GetVdsesRequestBody.md) | No |  |
| `elfDataStores` | [GetElfDataStoresRequestBody](../Get/GetElfDataStoresRequestBody.md) | No |  |
| `vms` | [GetVmsRequestBody](../Get/GetVmsRequestBody.md) | No |  |
| `nfsExports` | [GetNfsExportsRequestBody](../Get/GetNfsExportsRequestBody.md) | No |  |
| `iscsiTargets` | [GetIscsiTargetsRequestBody](../Get/GetIscsiTargetsRequestBody.md) | No |  |
| `usbDevices` | [GetUsbDevicesRequestBody](../Get/GetUsbDevicesRequestBody.md) | No |  |
| `nics` | [GetNicsRequestBody](../Get/GetNicsRequestBody.md) | No |  |
| `clusters` | [GetClustersRequestBody](../Get/GetClustersRequestBody.md) | No |  |
| `datacenters` | [GetDatacentersRequestBody](../Get/GetDatacentersRequestBody.md) | No |  |
| `hosts` | [GetHostsRequestBody](../Get/GetHostsRequestBody.md) | No |  |

