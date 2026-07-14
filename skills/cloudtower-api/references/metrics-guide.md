# Metric Names Guide

Operations under [Metrics](resources/Metrics.md) (`get-vm-metrics`, `get-vm-volume-metrics`, `get-top-n-metrics-in-clusters`, …) take a `metrics: string[]` field. **Valid metric names are not listed in the OpenAPI spec**, so `scripts/validate.py` cannot check them: a request with a wrong name still validates, and the API responds `200` with empty results instead of an error.

## Which names work

The `metrics` field accepts **underlying exporter metric names** (`elf_*`, `zbs_*`, …) — the same names the **metrics-lookup skill** documents (~1400 metrics; use it to find names when installed). Tower proxies the query to the cluster's observability service; the normal CloudTower token is the only credential needed.

Verified on CloudTower 4.8:

- **VM storage latency**: `elf_vm_disk_overall_avg_readwrite_latency_ns` (also `_read_`/`_write_` variants) via `get-vm-metrics` — returns per-VM streams with data points; the `_vm` label is the VM's `bios_uuid`, which joins back to the `get-vms` inventory.
- The `iostat_*` family (`iostat_latency`, `iostat_read_latency`, …) resolves into streams but returns **no data points** on some deployments. Do not start there; if a probe returns streams whose `points` is null/empty, switch to the exporter names above instead of retrying variants.

## Dead end — do not retry

`zbs_volume_*` names work with `get-top-n-metrics-in-clusters`, but the `_volume` label in the results is a ZBS-internal UUID that matches **nothing** in the CloudTower API (verified: 0 of 58 metric volume UUIDs matched any `VmVolume.local_id` across 264 volumes), and there is no `_vm` label. Volume-level rankings cannot be mapped back to VMs. For "top VMs by …" questions use VM-level `elf_*` metrics via `get-vm-metrics`.

## Recipe: top-N VMs by storage latency

```bash
# 1. VM inventory (bios_uuid -> name/cluster mapping)
echo '{}' > /tmp/vms.json
python3 scripts/validate.py GetVms /tmp/vms.json
bash scripts/call.sh /v2/api/get-vms /tmp/vms.json          # note the response file path

# 2. Latency for all VMs in one call ({} in `vms` = no filter)
cat > /tmp/lat.json <<'EOF'
{"range": "24h", "metrics": ["elf_vm_disk_overall_avg_readwrite_latency_ns"], "vms": {}}
EOF
python3 scripts/validate.py GetVmMetrics /tmp/lat.json
bash scripts/call.sh /v2/api/get-vm-metrics /tmp/lat.json   # note the response file path

# 3. Aggregate in a script; print only the ranked table
python3 - <<'PY'
import json
vms = {v["bios_uuid"]: v for v in json.load(open("<vms-response-file>"))}

def val(p):  # a point is a [ts, value] pair or an object — handle both
    return float(p[1] if isinstance(p, (list, tuple)) else p.get("value", p.get("v", 0)))

best = {}
for item in json.load(open("<latency-response-file>")):
    for s in (item.get("data") or {}).get("sample_streams") or []:
        uuid, pts = s["labels"].get("_vm"), s.get("points") or []
        if pts:
            best[uuid] = max(best.get(uuid, 0), max(val(p) for p in pts))
for uuid, ns in sorted(best.items(), key=lambda kv: -kv[1])[:3]:
    vm = vms.get(uuid, {})
    print(f'{vm.get("name", uuid)}  {vm.get("cluster", {}).get("name", "?")}  {ns/1e6:.2f} ms')
PY
```

If the response reports `dropped: true`, the server truncated the result — split the query (filter `vms` by cluster or batch `bios_uuid_in` groups) or shorten `range`.

## Probing an unknown metric name

Probe one resource with a short range before building a large query:

```bash
cat > /tmp/probe.json <<'EOF'
{"range": "1h", "metrics": ["<candidate_name>"], "vms": {"id": "<vm_id>"}}
EOF
python3 scripts/validate.py GetVmMetrics /tmp/probe.json
bash scripts/call.sh /v2/api/get-vm-metrics /tmp/probe.json
```

## Reading the response

Inspect one element with `jq '.[0]'` before writing an aggregation script — the shape varies by endpoint:

- `get-*-metrics`: `[{task_id, data: {sample_streams: [{labels, points}], unit, step, dropped}}]` — timestamped values live in `points`
- `get-top-n-metrics-in-clusters`: `data.samples` is a list of `{labels, point}` (one value per entry)
- streams present but `points`/values null or empty → the name resolved but this family has no data here (see `iostat_*` note above)
- `sample_streams: null` and `samples: []` → the endpoint did not recognize the name at all
- `dropped: true` → result truncated; narrow the query

## Routing between skills (metrics tasks)

- **Only CloudTower credentials available** (the usual case): stay on these Metrics operations — Tower proxies the observability service, no extra auth. Get metric names from the metrics-lookup skill.
- **Direct OVM VictoriaMetrics access** (the observability-insight skill's route) requires separate HTTP Basic credentials (`OBS_USER`/`OBS_PASSWORD`). CloudTower usernames, passwords, and tokens do **not** work there (verified 401). Take that route only when those credentials actually exist in the environment.
