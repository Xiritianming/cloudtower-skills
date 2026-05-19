# API

Two endpoints live on the Tower; two live on each OVM.

## Auth and TLS

All Tower and OVM endpoints below use HTTP Basic auth. Resolve
them at the moment of the call from one of these sources, in order:

1. Environment variables `OBS_USER` and `OBS_PASSWORD` (preferred for
   automation, CI, and repeated calls in the same session).
2. A secret manager / `.env` file the caller has already loaded into the
   shell (it should populate the same two variables).
3. As a last resort, ask the user for the username and password through an
   interactive prompt, then export them into the shell for the rest of the
   session.

Other ground rules:

- Ignore TLS verification (self-signed certs are normal): always pass `-k`.

## Tower endpoints (cluster -> OVM discovery)

| Endpoint | Purpose |
| --- | --- |
| `GET https://TOWER_IP/observability/obs/api/v3/services` | List observability services. Extract service id, service name, OVM IP/host. |
| `GET https://TOWER_IP/observability/obs/api/v3/connectedClusters` | List cluster-to-service bindings. Extract cluster name, cluster uuid, linked service id / name. |

Build `cluster_name -> OVM_IP` by joining these two responses on service id:

1. Read `services[].id`, `services[].name`, and `services[].management_ip`. Build a service lookup table keyed by `id`.
2. Read `connected_clusters[].cluster_id`, `connected_clusters[].name`, and `connected_clusters[].service_id`.
3. For each connected cluster, use `connected_clusters[].service_id` to find the matching `services[].id`.
4. The mapping is:

| Mapping field | Source |
| --- | --- |
| Cluster display name | `connected_clusters[].name` |
| CloudTower cluster id | `connected_clusters[].cluster_id` |
| Observability service id | `connected_clusters[].service_id` = `services[].id` |
| Observability service name | `services[].name` |
| OVM API host | `services[].management_ip` |

In code, treat the relationship as `connected_cluster -> service -> OVM`:

```text
connected_clusters[].cluster_id/name
  -- connected_clusters[].service_id == services[].id -->
services[].management_ip
```

Example from real responses: if a connected cluster has
`service_id = "35NE9SsEQCjFffmPn788z9rv5OV"`, match it to the service whose
`id` is the same value, then use that service's `management_ip`
(`172.20.252.20`) as the `OVM_IP` for VictoriaMetrics queries.

Example:

```bash
curl -sk -u "$OBS_USER:$OBS_PASSWORD" \
  "https://${TOWER_IP}/observability/obs/api/v3/services?page_size=1000"
curl -sk -u "$OBS_USER:$OBS_PASSWORD" \
  "https://${TOWER_IP}/observability/obs/api/v3/connectedClusters?page_size=1000"
```

## OVM endpoints (VictoriaMetrics)

| Endpoint | Use |
| --- | --- |
| `GET https://OVM_IP/victoriametrics/api/v1/query` | Point lookups and identity mapping (e.g. `obs_elf_vm_name`) |
| `GET https://OVM_IP/victoriametrics/api/v1/query_range` | Peak screening, time correlation, any window-based check |

### `query_range` parameters

| Param | Required | Note |
| --- | --- | --- |
| `query` | yes | PromQL |
| `start` | yes | RFC3339 or unix seconds |
| `end` | yes | RFC3339 or unix seconds |
| `step` | yes | e.g. `1m`, `5m`, `15m` |

Example:

```bash
curl -sk -u "$OBS_USER:$OBS_PASSWORD" --get \
  "https://${OVM_IP}/victoriametrics/api/v1/query_range" \
  --data-urlencode 'query=sum by (_cluster_uuid, _host) (host_disk_read_speed_bps)' \
  --data-urlencode 'start=2026-04-17T00:00:00Z' \
  --data-urlencode 'end=2026-04-17T06:00:00Z' \
  --data-urlencode 'step=5m'
```

### `query` vs `query_range`

- Anything that needs a peak, a trend, or time correlation → `query_range`.
- Anything that asks "what is this series right now?" or resolves an identity label → `query`.
- Never replay the entire lookback window for every metric up-front. Let the evidence pick the next query.
