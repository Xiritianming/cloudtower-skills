#!/usr/bin/env python3
"""Flatten a CloudTower metrics response into a neutral TSV summary.

Usage: metrics-flatten.py <metrics-response.json> [resources.json ...]

Prints one row per stream/sample:
  resource  device  metric  points  min  max  avg  first  last  unit  dropped

`resources.json` files are get-vms / get-hosts response files; identity
labels (`_vm` / `_host`) are resolved to resource names via a multi-key
lookup (local_id, bios_uuid, id). Unresolved identities print as the raw
label value.

Output is a plain-header TSV (csv.DictReader / pandas.read_csv parse it
directly). No-data rows (the `points` column is 0 — the count of finite
values) leave the five stat columns empty: pandas reads them as NaN, awk
sums add 0, and sort sinks them, while raw `float()` raises so an
unguarded consumer fails fast instead of reporting a silent wrong number
— filter on `points > 0` before treating the stat columns as numbers.
Resource names are printed raw — a name containing a tab or newline would
shift columns.

Filtering is the caller's job (awk on any column). For ranking, pipe to
`scripts/metrics-rank.sh <flat.tsv|-> [max|growth]` — it owns the correct
sort (general-numeric, locale-pinned; growth needs >=2 points), which a
hand-written `sort -n` gets wrong on %.6g scientific notation.
"""
import json
import math
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

    dropped_vals = 0

    def finite(v):
        # Keep only real numbers so `points` counts finite values and no stat
        # cell is ever a live nan/inf. null is expected (not counted); anything
        # else present-but-unusable (JSON NaN/Infinity, a huge int, a string) is
        # counted so an all-dropped stream isn't silently reported as no-data.
        nonlocal dropped_vals
        if v is None:
            return False
        try:
            ok = isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
        except OverflowError:  # int too large to test finiteness
            ok = False
        if not ok:
            dropped_vals += 1
        return ok

    def rows(data, dropped, unit):
        for s in data.get("sample_streams") or []:
            pts = s.get("points") or []
            yield s.get("labels") or {}, [p["v"] for p in pts if finite(p.get("v"))], dropped, unit
        for s in data.get("samples") or []:
            p = s.get("point") or {}
            vals = [p["v"]] if finite(p.get("v")) else []
            yield s.get("labels") or {}, vals, dropped, unit

    idents, unresolved = set(), set()
    print("resource\tdevice\tmetric\tpoints\tmin\tmax\tavg\tfirst\tlast\tunit\tdropped")
    for item in json.load(open(sys.argv[1])):
        data = (item or {}).get("data") or {}
        for labels, vals, dropped, unit in rows(data, data.get("dropped"), data.get("unit")):
            ident = labels.get("_vm") or labels.get("_host") or ""
            resource = lookup.get(ident, ident)
            if ident:
                idents.add(ident)
                if ident not in lookup:
                    unresolved.add(ident)
            device = labels.get("_device") or ""
            metric = labels.get("metric_name") or ""
            if vals:
                stats = [min(vals), max(vals), sum(vals) / len(vals), vals[0], vals[-1]]
                cells = [f"{v:.6g}" for v in stats]
            else:
                cells = [""] * 5   # no data — empty is the standard TSV null: pandas -> NaN,
                                   # awk sums add 0, sort sinks it, and raw float() raises (fail-fast)
            print("\t".join([resource, device, metric, str(len(vals)), *cells, str(unit), str(dropped)]))

    if len(sys.argv) > 2 and unresolved:
        print(
            f"joined {len(idents) - len(unresolved)}/{len(idents)} identities; "
            f"{len(unresolved)} unresolved (e.g. {sorted(unresolved)[0]}) — pass the RAW "
            f"get-hosts/get-vms response file (projected/filtered files lose local_id); "
            f"unresolved rows keep the raw UUID",
            file=sys.stderr,
        )
    if dropped_vals:
        print(
            f"dropped {dropped_vals} non-finite/non-numeric point value(s) (NaN/Infinity/"
            f"overflow) from the stats; a row whose values were all dropped shows as "
            f"no-data (points 0)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    # Behave like a standard Unix filter: if a downstream reader closes the pipe
    # early (e.g. `... | head` to preview), die on SIGPIPE instead of raising a
    # BrokenPipeError traceback that reads as a failure. The rows already taken
    # are correct; the normal (unpiped / fully-read) case is unaffected.
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    sys.exit(main())
