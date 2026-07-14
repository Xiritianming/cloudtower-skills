---
name: observability-insight
description: Base skill for CloudTower observability. Use when 1) Querying metrics for cluster/host/disk/vm etc. through the VictoriaMetrics API. 2) Discovering which observability service (OVM) a cluster is bound to. 3) Performing generic broad-to-narrow metric drill-down. 4) Delegates metric-name discovery to the `metrics-lookup` skill and CloudTower resource inventory to the `cloudtower-api` skill.
---

# Observability Insight

Base skill for talking to CloudTower observability services. It answers three questions:

1. Which OVM hosts the metrics for a given cluster?
2. How do I call that OVM's VictoriaMetrics API?
3. How are metrics labeled, and how do I join across host / VM / disk?

## How to use

Load references progressively:

1. [references/api.md](references/api.md) — auth, endpoints, `query` vs `query_range` selection
2. [references/label-taxonomy.md](references/label-taxonomy.md) — identity labels and join helpers
3. [references/playbook-primitives.md](references/playbook-primitives.md) — generic broad-to-narrow drill-down only when a task needs causal attribution

## Credential gate — check before anything else

Every endpoint in this skill uses HTTP Basic auth via `OBS_USER`/`OBS_PASSWORD`. **CloudTower usernames, passwords, and API tokens do not work here** (they get 401). If `OBS_USER`/`OBS_PASSWORD` are not available, do not probe these endpoints — switch to the `cloudtower-api` skill's Metrics operations (`get-vm-metrics`, `get-top-n-metrics-in-clusters`, …): Tower proxies the observability service with the normal CloudTower token, and the same exporter metric names work there. See its `references/metrics-guide.md`.

## Workflow

1. **Resolve scope.** Call `GET /observability/obs/api/v3/services` and `GET /observability/obs/api/v3/connectedClusters` on the Tower. Build `cluster_name -> OVM_IP` from the response. Narrow by `CLUSTER_NAME` if the caller provided one.
2. **Pick the API shape.** Use `query_range` for anomaly screening, peak detection, and time correlation. Use `query` only for point lookups or identity mapping (e.g. resolving `obs_elf_vm_name`).
3. **Compose queries with label taxonomy.** Aggregate by the identity labels in `label-taxonomy.md`. Join series with `on()` / `group_left()` using the helpers there.
4. **Drill down when needed.** If the caller's task requires causal attribution, follow `playbook-primitives.md`: broad first, then narrow, same direction, same window. The caller is responsible for choosing the concrete metrics.
5. **Report discovery failures loudly.** If a cluster cannot be mapped to an OVM IP, surface it instead of silently skipping.

## Delegate to other skills

- **`metrics-lookup` skill** — use when the caller asks what a metric means, which metric matches a description, or when the environment does not expose the metric name you expected. Pass the keyword or prefix (e.g. `elf_vm_disk`, `host_disk_*`, `port-storage`, `SMART`) and let it return the metric reference.
- **`cloudtower-api` skill** — use when the task needs Tower-side resource inventory: VM / host / disk / cluster properties, task polling for async mutations, or mapping a name to an object ID. Also the fallback route for metric queries when `OBS_USER`/`OBS_PASSWORD` are unavailable (see the credential gate above).
