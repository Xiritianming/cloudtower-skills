---
name: cloudtower-api
description: cloudtower operation API and SDK. Use when the user wants to query or manage CloudTower resources (VMs, clusters, hosts, storage, networks, snapshots, backups) or otherwise interact with the cloudtower-api.
metadata:
  api-version: "4.8.0"
  openapi-version: "3.0.0"
---

# cloudtower-api

cloudtower operation API and SDK

## How to Use This Skill

This API documentation is split into multiple files for on-demand loading.

**Directory structure:**
```
references/
├── resources/        # 130 resource index files
├── operations/       # 575 operation detail files
├── schemas/          # 163 schema groups, 1894 schema files
├── querying.md       # where-filter, counting, and pagination syntax
├── metrics-guide.md  # metric names for the Metrics operations
└── openapi.json      # full spec, used by scripts/validate.py (large — grep with -o and head, never cat)
scripts/
├── call.sh           # sends requests (auth, endpoint, response-to-file); `call.sh login` caches a token
├── validate.py       # validates a request body against the API schema
├── catalog-grep.sh   # finds metric names in the metrics-lookup catalog (locates it across install layouts)
└── metrics-flatten.py # flattens a metrics response into a TSV summary (joins _vm/_host to names)
```

**Calling flow — follow all five steps for every API call:**

1. Find the resource in the list below and read `references/resources/<resource>.md` to pick the operation
2. Read `references/operations/<operation>.md` — it has the full request path, parameters, and an `## Example` request body
3. Write the example body to a file (e.g. `/tmp/body.json`) and edit it. **Copy, don't compose**: every field name must come from the example or from a schema file you have read this session. To add an optional field, read its schema link first; for `where` filters, counting, and pagination see `references/querying.md`
4. Validate (from the skill root — `cd` there first): `python3 scripts/validate.py <OperationId> /tmp/body.json` — it checks required fields, types, enums, and unknown fields. Fix every reported error and re-run until it prints `OK`
5. Send: `bash scripts/call.sh <path> /tmp/body.json` — the path comes from the operation file title

## Endpoint and Authentication

`scripts/call.sh` needs `CLOUDTOWER_ENDPOINT` (base URL, e.g. `https://tower.example.com`; paths in operation files already include the `/v2/api` prefix) plus a token:

- Token known: `export CLOUDTOWER_TOKEN=<token>`
- Username/password: export `CLOUDTOWER_ENDPOINT`, `CLOUDTOWER_USERNAME`, `CLOUDTOWER_PASSWORD`, then run `bash scripts/call.sh login` **once** — the token is cached in `/tmp/cloudtower.env` and every later `call.sh` reads it automatically, so it survives shells that reset environment variables between commands

See [Authentication](./references/authentication.md) for details.

## Async Operations and Tasks

Most mutation operations are asynchronous. Instead of blocking, the API returns immediately with a placeholder resource and a task reference. As a result, a successful response does **not** guarantee that the operation has finished; the returned `data` (except for the resource `id`) should be treated as temporary.

Mutation responses are typically `WithTask<T>` or `Array<WithTask<T>>`. See the schema index at [With schemas](references/schemas/With/_index.md) for concrete types.

Use the task ID to track completion via [GetTasks](references/operations/GetTasks.md):

```bash
echo '{"where": {"id": "<task_id>"}, "first": 1}' > /tmp/task-query.json
bash scripts/call.sh /v2/api/get-tasks /tmp/task-query.json
```

Poll until `status` is `SUCCESSED` or `FAILED`, then fetch the latest resource state by ID. If `task_id` is `null`, the operation is synchronous and no polling is required.

## Response handling

`scripts/call.sh` writes every response to a file under `/tmp/` and prints the HTTP status, the file path, and a short preview — responses can be large, so this keeps them out of context. Read small portions of the file with `jq`, `grep`, or `head`, and load only the fields you need.

The same rule applies to derived data: keep intermediate results (ID→name maps, per-batch samples, merged lists) in files, aggregate them with a script, and print only the final, small answer.

## Resources

Each resource's operation index is at `references/resources/<Name>.md`. Operation count in parentheses:

`Vm` (58) · `Metrics` (17) · `Cluster` (15) · `BackupPlan` (13) · `Host` (11) · `ContentLibraryVmTemplate` (10) · `VmVolume` (10) · `GlobalSettings` (9) · `ContentLibraryImage` (8) · `IscsiLun` (8) · `SnapshotPlan` (8) · `User` (8) · `CloudTowerApplication` (7) · `Datacenter` (7) · `Label` (7) · `NvmfNamespace` (7) · `Vds` (7) · `Vlan` (7) · `BrickTopo` (6) · `GpuDevice` (6) · `ReportTemplate` (6) · `SnapshotGroup` (6) · `VmTemplate` (6) · `AlertNotifier` (6) · `ConsistencyGroupSnapshot` (5) · `ConsistencyGroup` (5) · `EntityFilter` (5) · `Graph` (5) · `IscsiTarget` (5) · `ElfImage` (5) · `IsolationPolicy` (5) · `LogCollection` (5) · `NamespaceGroup` (5) · `NetworkPolicyRuleService` (5) · `NfsExport` (5) · `NvmfSubsystem` (5) · `Organization` (5) · `RackTopo` (5) · `UserRoleNext` (5) · `SecurityGroup` (5) · `SecurityPolicy` (5) · `SnmpTransport` (5) · `SnmpTrapReceiver` (5) · `UsbDevice` (5) · `View` (5) · `VirtualPrivateCloudFloatingIp` (5) · `VirtualPrivateCloudNatGateway` (5) · `VirtualPrivateCloudRouteTable` (5) · `VirtualPrivateCloudRouterGateway` (5) · `VirtualPrivateCloudSecurityGroup` (5) · `VirtualPrivateCloudSecurityPolicy` (5) · `VirtualPrivateCloudSubnet` (5) · `VirtualPrivateCloud` (5) · `VmFolder` (5) · `VmPlacementGroup` (5) · `GlobalAlertRule` (4) · `Disk` (4) · `IscsiLunSnapshot` (4) · `NvmfNamespaceSnapshot` (4) · `Task` (4) · `VcenterAccount` (4) · `VmSnapshot` (4) · `VmVolumeSnapshot` (4) · `Alert` (3) · `UserAuditLog` (3) · `Ovf` (3) · `License` (3) · `NfsInode` (3) · `Nic` (3) · `NodeTopo` (3) · `ReplicationPlan` (3) · `SvtImage` (3) · `UploadTask` (3) · `VsphereEsxiAccount` (3) · `Observability` (2) · `AlertRule` (2) · `Application` (2) · `BackupPlanExecution` (2) · `BackupRestoreExecution` (2) · `BackupRestorePoint` (2) · `BackupService` (2) · `BackupStoreRepository` (2) · `BackupTargetExecution` (2) · `BusinessHostGroup` (2) · `BusinessHost` (2) · `CloudTowerApplicationPackage` (2) · `ClusterImage` (2) · `ClusterSettings` (2) · `ClusterTopo` (2) · `ClusterUpgradeHistory` (2) · `Deploy` (2) · `DiskPool` (2) · `EcpLicense` (2) · `ElfDataStore` (2) · `ElfStoragePolicy` (2) · `EverouteCluster` (2) · `EverouteLicense` (2) · `EveroutePackage` (2) · `IscsiConnection` (2) · `PmemDimm` (2) · `RegistryService` (2) · `ReplicaVm` (2) · `ReplicationService` (2) · `ReportTask` (2) · `SmtpServer` (2) · `SnapshotPlanTask` (2) · `SystemAuditLog` (2) · `V2EverouteLicense` (2) · `VirtualPrivateCloudClusterBinding` (2) · `VirtualPrivateCloudEdgeGatewayGroup` (2) · `VirtualPrivateCloudEdgeGateway` (2) · `VirtualPrivateCloudExternalSubnetGroup` (2) · `VirtualPrivateCloudExternalSubnet` (2) · `VmDisk` (2) · `VmEntityFilterResult` (2) · `VmExportFile` (2) · `VmNic` (2) · `Witness` (2) · `ZoneTopo` (2) · `Zone` (2) · `Ntp` (1) · `ResourceChange` (1) · `Internal` (1) · `TableReporter` (1) · `ApiInfo` (1) · `DiscoveredHost` (1) · `Ipmi` (1) · `LogServiceConfig` (1) · `PciDevice` (1) · `WitnessService` (1)