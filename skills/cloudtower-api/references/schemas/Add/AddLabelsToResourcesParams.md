# AddLabelsToResourcesParams

**Type:** object

## Fields

Required fields are listed first.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | object | Yes |  |
| `where` | [LabelWhereInput](../Label/LabelWhereInput.md) | Yes |  |

## Nested Fields

### `data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `gpu_devices` | [GpuDeviceWhereInput](../Gpu/GpuDeviceWhereInput.md) | No |  |
| `content_library_vm_templates` | [ContentLibraryVmTemplateWhereInput](../Content/ContentLibraryVmTemplateWhereInput.md) | No |  |
| `content_library_images` | [ContentLibraryImageWhereInput](../Content/ContentLibraryImageWhereInput.md) | No |  |
| `isolation_policies` | [IsolationPolicyWhereInput](../Isolation/IsolationPolicyWhereInput.md) | No |  |
| `security_policies` | [SecurityPolicyWhereInput](../Security/SecurityPolicyWhereInput.md) | No |  |
| `vms` | [VmWhereInput](../Vm/VmWhereInput.md) | No |  |
| `vm_volume_snapshots` | [VmVolumeSnapshotWhereInput](../Vm/VmVolumeSnapshotWhereInput.md) | No |  |
| `vm_volumes` | [VmVolumeWhereInput](../Vm/VmVolumeWhereInput.md) | No |  |
| `vm_templates` | [VmTemplateWhereInput](../Vm/VmTemplateWhereInput.md) | No |  |
| `vm_snapshots` | [VmSnapshotWhereInput](../Vm/VmSnapshotWhereInput.md) | No |  |
| `vlans` | [VlanWhereInput](../Vlan/VlanWhereInput.md) | No |  |
| `vdses` | [VdsWhereInput](../Vds/VdsWhereInput.md) | No |  |
| `nvmf_subsystems` | [NvmfSubsystemWhereInput](../Nvmf/NvmfSubsystemWhereInput.md) | No |  |
| `nvmf_namespace_snapshots` | [NvmfNamespaceSnapshotWhereInput](../Nvmf/NvmfNamespaceSnapshotWhereInput.md) | No |  |
| `nvmf_namespaces` | [NvmfNamespaceWhereInput](../Nvmf/NvmfNamespaceWhereInput.md) | No |  |
| `nics` | [NicWhereInput](../Nic/NicWhereInput.md) | No |  |
| `nfs_inodes` | [NfsInodeWhereInput](../Nfs/NfsInodeWhereInput.md) | No |  |
| `nfs_exports` | [NfsExportWhereInput](../Nfs/NfsExportWhereInput.md) | No |  |
| `namespace_groups` | [NamespaceGroupWhereInput](../Namespace/NamespaceGroupWhereInput.md) | No |  |
| `iscsi_targets` | [IscsiTargetWhereInput](../Iscsi/IscsiTargetWhereInput.md) | No |  |
| `iscsi_lun_snapshots` | [IscsiLunSnapshotWhereInput](../Iscsi/IscsiLunSnapshotWhereInput.md) | No |  |
| `iscsi_luns` | [IscsiLunWhereInput](../Iscsi/IscsiLunWhereInput.md) | No |  |
| `hosts` | [HostWhereInput](../Host/HostWhereInput.md) | No |  |
| `elf_images` | [ElfImageWhereInput](../Elf/ElfImageWhereInput.md) | No |  |
| `disks` | [DiskWhereInput](../Disk/DiskWhereInput.md) | No |  |
| `datacenters` | [DatacenterWhereInput](../Datacenter/DatacenterWhereInput.md) | No |  |
| `consistency_group_snapshots` | [ConsistencyGroupSnapshotWhereInput](../Consistency/ConsistencyGroupSnapshotWhereInput.md) | No |  |
| `consistency_groups` | [ConsistencyGroupWhereInput](../Consistency/ConsistencyGroupWhereInput.md) | No |  |
| `clusters` | [ClusterWhereInput](../Cluster/ClusterWhereInput.md) | No |  |

