# Metric Names Guide

Operations under [Metrics](resources/Metrics.md) (`get-vm-metrics`, `get-vm-volume-metrics`, `get-top-n-metrics-in-clusters`, …) take a `metrics: string[]` field. **Valid metric names are not listed in the OpenAPI spec**, so `scripts/validate.py` cannot check them: a request with a wrong name still validates, and the API responds `200` with empty `samples`/`sample_streams` instead of an error.

**Empty samples almost always mean a wrong metric name — not "no data in this range".** (The strings `iostat_latency`/`iostat_latency_ms` that appear in the spec are boolean settings fields, not metric names — do not treat spec grep hits as metric names.)

## Discovery recipe

Probe one resource with a candidate name; the `metric_name` labels in the response streams carry the true names:

```bash
cat > /tmp/probe.json <<'EOF'
{"range": "1h", "metrics": ["iostat_latency"], "vms": {"id": "<vm_id>"}}
EOF
python3 scripts/validate.py GetVmMetrics /tmp/probe.json
bash scripts/call.sh /v2/api/get-vm-metrics /tmp/probe.json
jq '[.[].data.sample_streams[]?.labels.metric_name] | unique' <response-file>
```

If the API rejects the `range` value, its error message states the accepted duration format.

## Known-good starting points (observed on CloudTower 4.8, VM level)

- `iostat_latency` — returns read/write latency streams (labels show `metric_name`: `iostat_read_latency`, `iostat_write_latency`)

Verify anything beyond this list with the discovery recipe before building a large query.

## Working with metric responses

- Batch large fleets: query VMs in groups (e.g. 30 `bios_uuid`s per request via the `vms` where-filter) rather than one call per VM.
- Aggregate response files with a script (`jq`/`python3`) and print only the final ranked result — never dump per-batch samples or ID→name maps into the conversation.
