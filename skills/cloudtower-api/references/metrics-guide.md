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

# 3. Flatten (resolves _vm/_host to names via the inventory) and rank by the
#    aggregated value. metrics-rank.sh owns the correct sort (general-numeric +
#    locale-pinned; a raw `sort -n` misreads the %.6g scientific notation of
#    values >=1e6, e.g. 8e+07 -> 8). The top-n endpoint returns ONE point per
#    entry, so rank it by `max`; growth ranking needs a time series (see the
#    fleet recipe) and is a no-op here.
python3 scripts/metrics-flatten.py <topn-response-file> <vms-response-file> | tail -n +2 > /tmp/flat.tsv
bash scripts/metrics-rank.sh /tmp/flat.tsv max 4
```

**Report the measurement basis with the answer**: metric name, time window, ranking criterion (here: the top-n endpoint's aggregated value — NOT the peak of the raw time series; peak ranking favors spiky VMs and produces a different list), and coverage limits. Without a declared basis, results from different runs cannot be compared.

## Recipe: fleet inspection (scan every resource for anomalies)

The other canonical shape: not "rank by one metric" but "summarize many metrics across a whole fleet and surface the outliers" (e.g. inspect all host NICs over 7 days). **The whole report assembles from the flattener's TSV with `awk`/`jq` — do not hand-write a JSON parser** (that path re-derives the envelope and loses time on the `metric_name`-is-in-labels trap the flattener already handles). Adapt the metric list and the anomaly test; keep the skeleton:

```bash
cd <skill-root>

# 1. Inventory (identity -> name, and any grouping field like cluster)
echo '{}' > /tmp/hosts.json
bash scripts/call.sh /v2/api/get-hosts /tmp/hosts.json          # -> /tmp/tower_<ts>.json

# 2. One query per batch if the fleet is large (dropped:true → shrink range or split hosts)
cat > /tmp/net.json <<'EOF'
{"hosts": {}, "range": "7d", "metrics": ["host_network_receive_errors", "host_network_transmit_errors", "host_network_receive_dropped_packets", "host_network_receive_speed_bitps"]}
EOF
python3 scripts/validate.py GetHostNetworkMetrics /tmp/net.json
bash scripts/call.sh /v2/api/get-host-network-metrics /tmp/net.json  # -> a response file per batch

# 3. Flatten every batch into one TSV, resolving names via inventory. tail -n +2 drops each
#    batch's header positionally (matching the header by content would erase a resource named "resource").
for f in <net-response-files>; do
  python3 scripts/metrics-flatten.py "$f" <hosts-response-file> | tail -n +2
done > /tmp/flat.tsv

# 4. Report = filter/group the TSV. Anomaly scan for counters = growth over the
#    window (last-first), since these are cumulative (max>0 only means "ever
#    errored"). Filter to the error/drop metrics with awk, then let
#    metrics-rank.sh compute growth and sort correctly (it excludes no-data and
#    single-point rows; resets show as negative growth at the bottom):
awk -F'\t' '$3 ~ /errors|dropped/' /tmp/flat.tsv | bash scripts/metrics-rank.sh - growth 20

# 5. Group by cluster without touching the metrics JSON — join the small inventory file:
jq -r '.[] | [.name, .cluster.name] | @tsv' <hosts-response-file> > /tmp/host_cluster.tsv
awk -F'\t' 'NR==FNR{cl[$1]=$2; next} {print cl[$1]"\t"$0}' /tmp/host_cluster.tsv /tmp/flat.tsv
```

Report the basis (metrics, window, that errors are cumulative counters so growth is the signal) and the coverage (hosts/NICs with no data). Derived figures like bandwidth-utilization % are the caller's own analysis — the flattener gives throughput; a link-capacity reference is not part of it.

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

Output is a plain-header TSV, one row per stream: `resource  device  metric  points  min  max  avg  first  last  unit  dropped`. Pass the raw `get-hosts`/`get-vms` response file(s) as extra args to resolve `_host`/`_vm` to names. Then slice with `awk`/`sort` (e.g. per host, per metric, growth `last-first` for counters). The flattener output is the input to a report — read it, don't re-parse the JSON.

**No-data rows**: when a metric has no values for a device, its `points` column is `0` and the five stat columns are **empty**. Handle them before doing math: `pandas.read_csv` reads them as `NaN`, `awk` sums add `0`, and `sort` sinks them — but raw `float("")` **raises**, on purpose: an unguarded consumer fails fast rather than reporting a silently wrong number. So **filter on `points > 0`** before treating the stat columns as numbers (`csv.DictReader` + `float`, `sorted(key=float)`, `max`/`min`, sums — all need the guard). `awk -F'\t'` positional (`$1` resource … `$11` dropped) needs no header.

Envelope details, only if you need them beyond what the flattener gives:

- `get-*-metrics`: `[{task_id, data: {sample_streams: [{labels, points}], unit, step, dropped}}]` — `points` is a list of `{"t": <epoch_ms>, "v": <value>}` objects
- `get-top-n-metrics-in-clusters`: `data.samples` is a list of `{labels, point}` with a single aggregated `{"t", "v"}` point per entry
- **a stream's presence proves nothing about the name** — endpoints echo one stream per device even for nonexistent metrics (verified on `get-host-network-metrics`). Only `points` with values validate a name; on empty points recheck the name against the catalog, then the range unit, then the family (`iostat_*` note above)
- `sample_streams: null` and `samples: []` → the endpoint did not recognize the request at all
- **range units**: `24h` and `7d` return data; `72h` and `168h` silently return empty (verified) — use day units for multi-day windows, and on empty results suspect the range unit before the metric name

## Routing between skills (metrics tasks)

- **Only CloudTower credentials available** (the usual case): stay on these Metrics operations — Tower proxies the observability service, no extra auth. Get metric names from the metrics-lookup skill.
- **Direct OVM VictoriaMetrics access** (the observability-insight skill's route) requires separate HTTP Basic credentials (`OBS_USER`/`OBS_PASSWORD`). CloudTower usernames, passwords, and tokens do **not** work there (verified 401). Take that route only when those credentials actually exist in the environment.
