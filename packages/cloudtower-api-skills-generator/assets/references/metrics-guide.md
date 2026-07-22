# Metric Names Guide

Operations under [Metrics](resources/Metrics.md) (`get-vm-metrics`, `get-vm-volume-metrics`, `get-top-n-metrics-in-clusters`, …) take a `metrics: string[]` field. **Valid metric names are not listed in the OpenAPI spec**, so `scripts/validate.py` cannot check them: a request with a wrong name still validates, and the API responds `200` with empty results instead of an error.

## Which names work

The `metrics` field accepts **underlying exporter metric names** (`elf_*`, `zbs_*`, `host_*`, …). Tower proxies the query to the cluster's observability service; the normal CloudTower token is the only credential needed. Pick the operation whose subject matches the metric's — VM disk metrics via [GetVmMetrics](operations/GetVmMetrics.md), host NIC metrics via [GetHostNetworkMetrics](operations/GetHostNetworkMetrics.md), the full list under [Metrics](resources/Metrics.md).

Deployment note (CloudTower 4.8, live-verified): the `elf_*` family returns data, while the `iostat_*` family (`iostat_latency`, …) resolves into streams but returns **no data points** — if a probe returns streams whose points are null/empty, switch families instead of retrying name variants.

## Finding a metric name: grep the catalog, then probe once

Metric names come from the **metrics-lookup catalog** (~1400 metrics), never from guessing against the live API. `scripts/catalog-grep.sh` locates the catalog across install layouts and greps it — pass symptom words in both languages (names are English, descriptions Chinese):

```bash
cd <skill-root>
bash scripts/catalog-grep.sh error 错误 丢包
```

A name absent from the catalog is not worth probing; if the script reports the catalog missing, follow its error message rather than improvising names. The live API's only discovery job is the probe below: confirming that a cataloged name has data on this deployment. For what a metric *means*, invoke the metrics-lookup skill itself.

## Mapping results back to resources

The `_vm` / `_host` labels carry a resource identity, but **which field it matches depends on the metric family** — for `elf_*` and `host_*` metrics it is the resource's `local_id` (verified live for both VMs and hosts; it is NOT `bios_uuid`). `scripts/metrics-flatten.py` implements the join as a multi-key lookup (`local_id`/`bios_uuid`/`id`) — pass your `get-vms` / `get-hosts` response files as extra arguments instead of writing a parser.

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

# 3. Flatten and rank (flattener resolves _vm/_host to names via the inventory file)
python3 scripts/metrics-flatten.py <topn-response-file> <vms-response-file> \
  | sort -t$'\t' -k6 -rn | head -4    # rank by max; for counters rank by growth:
                                       #   awk -F'\t' '{print $9-$8, $0}' | sort -rn
```

**Report the measurement basis with the answer**: metric name, time window, ranking criterion (here: the top-n endpoint's aggregated value — NOT the peak of the raw time series; peak ranking favors spiky VMs and produces a different list), and coverage limits. Without a declared basis, results from different runs cannot be compared.

## Handling `dropped: true`

- On `get-top-n-metrics-in-clusters` responses `dropped: true` is common and the returned samples are still ordered highest-first. Verify the top entries are stable by re-querying with a larger `n` (e.g. 10) and comparing — do not spiral into batch-splitting.
- On `get-vm-metrics`, a 24h range across many VMs always truncates: splitting to 20-VM and even 10-VM batches still returned `dropped: true` (verified). The working lever is a shorter `range`, or switching to the top-n endpoint.
- **Never fall back to one-VM-per-request loops** — measured ~14s per call; a 129-VM fleet is half an hour of serial requests.

## Probing a cataloged metric name

Probe one resource with a short range and a bounded timeout before building a large query — `CLOUDTOWER_TIMEOUT` caps a hung request instead of letting it stall for minutes:

```bash
cd <skill-root>
cat > /tmp/probe.json <<'EOF'
{"range": "1h", "metrics": ["<candidate_name>"], "vms": {"id": "<vm_id>"}}
EOF
python3 scripts/validate.py GetVmMetrics /tmp/probe.json
CLOUDTOWER_TIMEOUT=120 bash scripts/call.sh /v2/api/get-vm-metrics /tmp/probe.json
```

## Processing any metrics response — use the flattener, don't hand-write a parser

**`scripts/metrics-flatten.py` IS the parser for every Metrics response** (`get-*-metrics` and `get-top-n-metrics-in-clusters` alike). Run it before writing any Python of your own — it already handles the multi-task envelope (one task per metric), the `metric_name` labels, both point shapes, and the identity join; a hand-rolled parser re-derives all of that and is where time is lost.

```bash
cd <skill-root>
python3 scripts/metrics-flatten.py <response-file> [get-hosts-or-get-vms-response...]
```

Output is one TSV row per stream: `resource  device  metric  points  min  max  avg  first  last  unit  dropped`. Pass the raw `get-hosts`/`get-vms` response file(s) as extra args to resolve `_host`/`_vm` to names. Then slice with `awk`/`sort` (e.g. per host, per metric, growth `last-first` for counters); `points 0` means no data. The flattener output is the input to a report — read it, don't re-parse the JSON.

Envelope details, only if you need them beyond what the flattener gives:

- `get-*-metrics`: `[{task_id, data: {sample_streams: [{labels, points}], unit, step, dropped}}]` — `points` is a list of `{"t": <epoch_ms>, "v": <value>}` objects
- `get-top-n-metrics-in-clusters`: `data.samples` is a list of `{labels, point}` with a single aggregated `{"t", "v"}` point per entry
- **a stream's presence proves nothing about the name** — endpoints echo one stream per device even for nonexistent metrics (verified on `get-host-network-metrics`). Only `points` with values validate a name; on empty points recheck the name against the catalog, then the range unit, then the family (`iostat_*` note above)
- `sample_streams: null` and `samples: []` → the endpoint did not recognize the request at all
- **range units**: `24h` and `7d` return data; `72h` and `168h` silently return empty (verified) — use day units for multi-day windows, and on empty results suspect the range unit before the metric name

## Routing between skills (metrics tasks)

- **Only CloudTower credentials available** (the usual case): stay on these Metrics operations — Tower proxies the observability service, no extra auth. Get metric names from the metrics-lookup skill.
- **Direct OVM VictoriaMetrics access** (the observability-insight skill's route) requires separate HTTP Basic credentials (`OBS_USER`/`OBS_PASSWORD`). CloudTower usernames, passwords, and tokens do **not** work there (verified 401). Take that route only when those credentials actually exist in the environment.
