# Label Taxonomy

Identity labels and join helpers used across CloudTower observability metrics. Use these to aggregate series and to enrich results with human-readable names.

## Identity labels

Refer to metrics-lookup skill for detailed labels description.

Rule of thumb: aggregate by internal ids (`_cluster_uuid`, `_host`, `_vm`), then join display names through the helpers below.

## Join helpers

These are identity metrics. Query with `query` (point lookup) unless you specifically need history.

| Purpose | PromQL |
| --- | --- |
| Cluster display name | `max by (cluster_name, _tenant_id, _cluster_uuid) (obs_cluster_info{platform!="VMWare"})` |
| Host display name | `max(obs_host_name) without(source)` |
| VM display name | `max(obs_elf_vm_name) without(source)` or `max by (_vm, name) (obs_elf_vm_name)` |
| VM → host mapping | `max(obs_elf_vm_hostname) without(source)` or `max by (_vm, hostname) (obs_elf_vm_hostname)` |

## Join pattern

Enrich a value series with a name label using `on(...) group_left(...)`:

```promql
sum by (_cluster_uuid, _vm, _tenant_id) (elf_vm_disk_overall_read_speed_bps)
  * on(_vm) group_left(name)     max by (_vm, name)     (obs_elf_vm_name)
  * on(_vm) group_left(hostname) max by (_vm, hostname) (obs_elf_vm_hostname)
```

## Fallbacks

- If `obs_elf_vm_hostname` is missing or stale, fall back from host-level attribution to same-cluster + same-time-window correlation, and state that the host mapping is weaker evidence.
- If a cluster has no `obs_cluster_info` series on the target OVM, the cluster is probably not bound to that OVM — re-run Tower discovery before continuing.

## When the label you need is not listed

Invoke the `metrics-lookup` skill with the prefix or keyword (e.g. `obs_`, `elf_vm_`, `host_disk_`) to discover the correct metric. Do not guess label names.
