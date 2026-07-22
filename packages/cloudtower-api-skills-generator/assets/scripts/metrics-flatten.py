#!/usr/bin/env python3
"""Flatten a CloudTower metrics response into a neutral TSV summary.

Usage: metrics-flatten.py <metrics-response.json> [resources.json ...]

Prints one row per stream/sample:
  resource  device  metric  points  min  max  avg  first  last  unit  dropped

`resources.json` files are get-vms / get-hosts response files; identity
labels (`_vm` / `_host`) are resolved to resource names via a multi-key
lookup (local_id, bios_uuid, id). Unresolved identities print as the raw
label value. Rows with `points 0` mean the metric returned no data.

Ranking and filtering are the caller's job — pick your own criterion:
  sort -t$'\\t' -k6 -rn            # by max (gauges, peaks)
  awk -F'\\t' '{print $9-$8, $0}'  # by growth last-first (counters)
"""
import json
import sys


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    lookup = {}
    for path in sys.argv[2:]:
        for r in json.load(open(path)):
            for k in ("local_id", "bios_uuid", "id"):
                if isinstance(r, dict) and r.get(k):
                    lookup[r[k]] = r.get("name") or r[k]

    def rows(data, dropped, unit):
        for s in data.get("sample_streams") or []:
            pts = s.get("points") or []
            yield s.get("labels") or {}, [p.get("v") for p in pts if p.get("v") is not None], dropped, unit
        for s in data.get("samples") or []:
            p = s.get("point") or {}
            vals = [p["v"]] if p.get("v") is not None else []
            yield s.get("labels") or {}, vals, dropped, unit

    print("#resource\tdevice\tmetric\tpoints\tmin\tmax\tavg\tfirst\tlast\tunit\tdropped")
    for item in json.load(open(sys.argv[1])):
        data = (item or {}).get("data") or {}
        for labels, vals, dropped, unit in rows(data, data.get("dropped"), data.get("unit")):
            ident = labels.get("_vm") or labels.get("_host") or ""
            resource = lookup.get(ident, ident)
            device = labels.get("_device") or ""
            metric = labels.get("metric_name") or ""
            if vals:
                stats = [min(vals), max(vals), sum(vals) / len(vals), vals[0], vals[-1]]
                cells = [f"{v:.6g}" for v in stats]
            else:
                cells = ["-"] * 5
            print("\t".join([resource, device, metric, str(len(vals)), *cells, str(unit), str(dropped)]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
