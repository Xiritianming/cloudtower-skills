# Playbook Primitives

Generic drill-down method for any observability investigation on CloudTower. No specific metrics, no thresholds, no severity colors — those are the custom skill's responsibility.

## Core method

1. **Broad first.** Screen the whole lookback window with an aggregation that hides individual series (e.g. `sum by (...)`). Record peak value, peak timestamp, and the identity labels at the peak.
2. **Narrow next.** Shrink to the peak window (typically `±15m`). Only now pull per-object detail.
3. **Same direction.** Read explains read, write explains write. Do not mix `read_*` evidence to explain a `write_*` symptom.
4. **Same window.** Causal evidence must overlap in time with the symptom. "Both were high somewhere today" is not evidence.
5. **Stop when explained.** If one branch already explains the symptom, skip the others. Do not collect evidence you will not use.
6. **Unresolved is a valid conclusion.** If no branch aligns, say so and recommend a tighter follow-up window rather than invent a cause.

## Direction hints

The typical drill-down directions in CloudTower. Treat them as naming hints, not mandatory paths. The custom skill decides which metrics to query.

| Direction | When to take it |
| --- | --- |
| `cluster -> host` | A cluster-level symptom needs to be attributed to a specific host, or multiple hosts need to be compared. |
| `host -> VM` | A host-level anomaly needs per-VM attribution on the same host and window. |
| `host -> physical disk` | Host latency is abnormal but VM-side throughput/IOPS does not explain it. Check disk latency on the same host, then disk health companion metrics. |
| `cluster-wide -> port-storage` | Several hosts in one cluster spike at similar timestamps. Prefer storage-path / network contention over per-host causes. |

## Evidence chain

For any non-trivial conclusion, the caller's report should contain four elements in order:

1. Symptom — what was observed broadly.
2. Chosen next query — why this branch, not another.
3. Decisive evidence — the narrow-window data that confirmed or rejected the hypothesis.
4. Final attribution — a specific cause, or `原因未完全确认` / `unresolved`.

## When metrics are unfamiliar

If the environment does not expose the metric the caller expected, or if a direction requires a metric not yet known, invoke the `metrics-lookup` skill with a keyword (e.g. `read_latency`, `port-storage`, `smart`) and adapt. Do not stop and do not fabricate metric names.

## When object identity is needed

If the report needs a VM or host name that is not in the VictoriaMetrics labels (e.g. business tags, cluster role), invoke the `cloudtower-api` skill to resolve the object from the Tower side.
