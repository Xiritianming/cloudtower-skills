# Metric Names Guide

Operations under [Metrics](resources/Metrics.md) (`get-vm-metrics`, `get-vm-volume-metrics`, `get-top-n-metrics-in-clusters`, …) take a `metrics: string[]` field. **Valid metric names are not listed in the OpenAPI spec**, so `scripts/validate.py` cannot check them: a request with a wrong name still validates, and the API responds `200` with empty results instead of an error.

## Which names work

The `metrics` field accepts **underlying exporter metric names** (`elf_*`, `zbs_*`, …) — the same names the **metrics-lookup skill** documents (~1400 metrics; use it to find names beyond the table below). Tower proxies the query to the cluster's observability service; the normal CloudTower token is the only credential needed.

Verified live on CloudTower 4.8:

| Purpose | Metric | Notes |
|---|---|---|
| VM storage latency (read+write avg) | `elf_vm_disk_overall_avg_readwrite_latency_ns` | unit ns; `_read_`/`_write_` variants exist |
| Other VM disk metrics (IOPS, bandwidth, …) | `elf_vm_disk_*` prefix family | look up exact names in metrics-lookup |

The `iostat_*` family (`iostat_latency`, `iostat_read_latency`, …) resolves into streams but returns **no data points** on some deployments — do not start there; if a probe returns streams whose points are null/empty, switch to the exporter names above instead of retrying variants.

## Mapping results back to VMs

The `_vm` label carries a VM identity, but **which field it matches depends on the metric family** — for `elf_*` metrics it is the VM's `local_id` (verified live; it is NOT `bios_uuid`). Always build a multi-key lookup instead of betting on one field:

```python
lookup = {}
for v in vms:                       # from a get-vms response
    for k in ("local_id", "bios_uuid", "id"):
        if v.get(k):
            lookup[v[k]] = v
```

## Dead end — do not retry

`zbs_volume_*` names work with `get-top-n-metrics-in-clusters`, but the `_volume` label in the results is a ZBS-internal UUID that matches **nothing** in the CloudTower API (verified: 0 of 58 metric volume UUIDs matched any `VmVolume.local_id` across 264 volumes), and there is no `_vm` label. Volume-level rankings cannot be mapped back to VMs. For "top VMs by …" questions use VM-level `elf_*` metrics.

## Recipe: top-N VMs by a metric

The canonical shape of every rank-by-metric task — adapt the metric name and window, keep the skeleton:

```bash
cd <skill-root>   # the directory containing SKILL.md

# 1. VM inventory (identity -> name/cluster mapping)
echo '{}' > /tmp/vms.json
bash scripts/call.sh /v2/api/get-vms /tmp/vms.json           # note the response file path

# 2. Top-N via the ranking endpoint; ask for more than you need (stability check below)
cat > /tmp/topn.json <<'EOF'
{"metrics": ["elf_vm_disk_overall_avg_readwrite_latency_ns"], "clusters": {}, "type": "top", "n": 10, "range": "24h"}
EOF
python3 scripts/validate.py GetTopNVmVolumeMetrics /tmp/topn.json
bash scripts/call.sh /v2/api/get-top-n-metrics-in-clusters /tmp/topn.json

# 3. Map identities and rank; print only the final table
python3 - <<'PY'
import json
vms = json.load(open("<vms-response-file>"))
lookup = {}
for v in vms:
    for k in ("local_id", "bios_uuid", "id"):
        if v.get(k):
            lookup[v[k]] = v
rows = []
for item in json.load(open("<topn-response-file>")):
    d = item.get("data") or {}
    for s in d.get("samples") or []:
        vm = lookup.get(s["labels"].get("_vm"), {})
        cluster = (vm.get("cluster") or {}).get("name", "?")
        rows.append((s["point"]["v"], vm.get("name", s["labels"].get("_vm")), cluster, d.get("dropped")))
for v, name, cluster, dropped in sorted(rows, reverse=True)[:3]:
    print(f"{name}\t{cluster}\t{v/1e6:.2f} ms\tdropped={dropped}")
PY
```

**Report the measurement basis with the answer**: metric name, time window, ranking criterion (here: the top-n endpoint's aggregated value — NOT the peak of the raw time series; peak ranking favors spiky VMs and produces a different list), and coverage limits. Without a declared basis, results from different runs cannot be compared.

## Handling `dropped: true`

- On `get-top-n-metrics-in-clusters` responses `dropped: true` is common and the returned samples are still ordered highest-first. Verify the top entries are stable by re-querying with a larger `n` (e.g. 10) and comparing — do not spiral into batch-splitting.
- On `get-vm-metrics`, a 24h range across many VMs always truncates: splitting to 20-VM and even 10-VM batches still returned `dropped: true` (verified). The working lever is a shorter `range`, or switching to the top-n endpoint.
- **Never fall back to one-VM-per-request loops** — measured ~14s per call; a 129-VM fleet is half an hour of serial requests.

## Probing an unknown metric name

Probe one resource with a short range before building a large query:

```bash
cd <skill-root>
cat > /tmp/probe.json <<'EOF'
{"range": "1h", "metrics": ["<candidate_name>"], "vms": {"id": "<vm_id>"}}
EOF
python3 scripts/validate.py GetVmMetrics /tmp/probe.json
bash scripts/call.sh /v2/api/get-vm-metrics /tmp/probe.json
```

## Reading the response

Inspect one element with `jq '.[0]'` before writing an aggregation script:

- `get-*-metrics`: `[{task_id, data: {sample_streams: [{labels, points}], unit, step, dropped}}]` — `points` is a list of `{"t": <epoch_ms>, "v": <value>}` objects
- `get-top-n-metrics-in-clusters`: `data.samples` is a list of `{labels, point}` with a single aggregated `{"t", "v"}` point per entry
- streams present but points null/empty → the name resolved but this family has no data here (see `iostat_*` note above)
- `sample_streams: null` and `samples: []` → the endpoint did not recognize the name at all

## Routing between skills (metrics tasks)

- **Only CloudTower credentials available** (the usual case): stay on these Metrics operations — Tower proxies the observability service, no extra auth. Get metric names from the metrics-lookup skill.
- **Direct OVM VictoriaMetrics access** (the observability-insight skill's route) requires separate HTTP Basic credentials (`OBS_USER`/`OBS_PASSWORD`). CloudTower usernames, passwords, and tokens do **not** work there (verified 401). Take that route only when those credentials actually exist in the environment.
