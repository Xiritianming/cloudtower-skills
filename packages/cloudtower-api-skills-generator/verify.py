#!/usr/bin/env python3
"""Regression gate for the generated skill — run after every regeneration.

Usage: python3 verify.py [skill-dir]   (default: ../../skills/cloudtower-api)

1. Round-trips every generated `## Example` body through scripts/validate.py —
   each example must validate against the operation's own schema.
2. Case-sensitively checks every relative markdown link (macOS's filesystem is
   case-insensitive, so a plain existence check would miss links that break on
   Linux checkouts).

Exit 0 = clean; non-zero = failures printed.
"""
import json
import os
import re
import subprocess
import sys

PKG_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PKG_DIR, "..", "..", "skills", "cloudtower-api")
OPS = os.path.join(SKILL, "references", "operations")
VALIDATE = os.path.join(SKILL, "scripts", "validate.py")
TMP_BODY = "/tmp/verify_example_body.json"

fail, passed, no_example = [], 0, 0
for fname in sorted(os.listdir(OPS)):
    text = open(os.path.join(OPS, fname)).read()
    op_id = re.search(r"\*\*Operation ID:\*\* `([^`]+)`", text)
    example = re.search(r"## Example.*?```json\n(.*?)\n```", text, re.S)
    if not example:
        no_example += 1
        continue
    body = example.group(1)
    json.loads(body)
    open(TMP_BODY, "w").write(body)
    r = subprocess.run(
        [sys.executable, VALIDATE, op_id.group(1), TMP_BODY],
        capture_output=True, text=True,
    )
    if r.returncode == 0:
        passed += 1
    else:
        fail.append((fname, (r.stdout + r.stderr).strip()[:300]))

print(f"examples: {passed} passed, {len(fail)} failed, {no_example} ops without example")
for fname, err in fail[:10]:
    print(f"  FAIL {fname}: {err}")


# Contract: catalog-grep.sh must exist, be executable, and — in this repo's
# sibling layout — locate the metrics-lookup catalog and surface the
# host_network error metrics with the guide's own example keywords.
grep_script = os.path.join(SKILL, "scripts", "catalog-grep.sh")
contract_fail = 0
if not os.access(grep_script, os.X_OK):
    print(f"  CONTRACT scripts/catalog-grep.sh missing or not executable")
    contract_fail = 1
else:
    r = subprocess.run(
        ["bash", grep_script, "error", "错误", "丢包"],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or "host_network_receive_errors" not in r.stdout:
        print(f"  CONTRACT catalog-grep.sh failed to find host_network_receive_errors: {(r.stderr or r.stdout)[:200]}")
        contract_fail = 1
print(f"catalog-grep contract: {'FAIL' if contract_fail else 'ok'}")

# Contract: metrics-flatten.py must summarize both envelope shapes and join
# identities via the multi-key lookup.
flatten = os.path.join(SKILL, "scripts", "metrics-flatten.py")
fixture = "/tmp/verify_flatten_resp.json"
inventory = "/tmp/verify_flatten_inv.json"
open(fixture, "w").write(json.dumps([
    {"task_id": None, "data": {"dropped": False, "unit": "COUNT", "sample_streams": [
        {"labels": {"_host": "uuid-1", "_device": "eth0", "metric_name": "m1"},
         "points": [{"t": 1, "v": 5}, {"t": 2, "v": 7}]},
        {"labels": {"_host": "uuid-stranger", "_device": "eth1", "metric_name": "m1"},
         "points": [{"t": 1, "v": 1}]},
        {"labels": {"_host": "uuid-1", "_device": "eth9", "metric_name": "m1"},
         "points": [{"t": 1, "v": None}, {"t": 2, "v": float("inf")}]}]}},  # no-data + non-finite -> empty
    {"task_id": None, "data": {"dropped": True, "unit": "TIME", "samples": [
        {"labels": {"_vm": "uuid-2", "metric_name": "m2"}, "point": {"t": 3, "v": 9}}]}},
]))
open(inventory, "w").write(json.dumps([
    {"name": "host-A", "local_id": "uuid-1", "id": "cm1"},
    {"name": "vm-B", "local_id": "uuid-2", "id": "cm2"},
]))
r = subprocess.run([sys.executable, flatten, fixture, inventory], capture_output=True, text=True)
flat_fail = 0
HEADER = "resource\tdevice\tmetric\tpoints\tmin\tmax\tavg\tfirst\tlast\tunit\tdropped"
import csv as _csv
# Output parses via csv.DictReader with ALL fieldnames; no-data cells are EMPTY
# (fail-fast — raw float() raises, only a points-guarded read succeeds); and no
# stat cell is ever a live nan/inf even when the API sends one.
dict_ok = False
try:
    rows = list(_csv.DictReader(r.stdout.splitlines(), delimiter="\t"))
    nodata = [x for x in rows if x["points"] == "0"]
    guarded = [float(x["max"]) for x in rows if int(x["points"]) > 0]
    raw_raises = False
    try:
        [float(x["max"]) for x in rows]          # unguarded MUST raise on empty (fail-fast)
    except ValueError:
        raw_raises = True
    dict_ok = (
        len(nodata) == 1                         # empty-points + non-finite stream flattened
        and nodata[0]["max"] == "" and nodata[0]["min"] == ""   # empty sentinel, not nan/-/0
        and raw_raises                           # unguarded float() fails fast
        and 7.0 in guarded and 9.0 in guarded    # points-guarded read works
    )
except Exception:
    dict_ok = False
if (
    r.returncode != 0
    or r.stdout.splitlines()[0] != HEADER      # full plain header, every column named
    or not dict_ok
    or "host-A\teth0\tm1\t2\t5\t7\t6\t5\t7" not in r.stdout
    or "vm-B\t\tm2\t1\t9" not in r.stdout
    or "host-A\teth9\tm1\t0\t\t\t\t\t\tCOUNT" not in r.stdout   # empty stat cells, no nan/inf
    or "uuid-stranger\teth1" not in r.stdout
    or "1 unresolved (e.g. uuid-stranger)" not in r.stderr
):
    print(f"  CONTRACT metrics-flatten.py wrong output: {(r.stderr or r.stdout)[:300]}")
    flat_fail = 1

# Contract: the ranking pipeline must order values correctly even at >1e6 (printed
# %.6g -> scientific notation with a fractional mantissa) with a no-data row present.
# Names ANTI-correlate with value (highest value = lexically-first "aaa") and the
# mantissa is fractional, so a lexical sort, a wrong key column, `-rn` (misreads the
# exponent), or a comma locale all produce a different order and fail the gate.
rank_fixture = "/tmp/verify_rank_resp.json"
open(rank_fixture, "w").write(json.dumps([
    {"task_id": None, "data": {"dropped": False, "unit": "TIME", "sample_streams": [
        {"labels": {"_vm": "aaa-hi", "metric_name": "lat"}, "points": [{"t": 1, "v": 1_000_000}, {"t": 2, "v": 81_234_567}]},
        {"labels": {"_vm": "mmm-mid", "metric_name": "lat"}, "points": [{"t": 1, "v": 30_111_222}, {"t": 2, "v": 5_000_000}]},
        {"labels": {"_vm": "zzz-lo", "metric_name": "lat"}, "points": [{"t": 1, "v": 955_000}, {"t": 2, "v": 940_000}]},
        {"labels": {"_vm": "nnn-nd", "metric_name": "lat"}, "points": [{"t": 1, "v": None}]}]}},
]))
open("/tmp/verify_rank_inv.json", "w").write(json.dumps([
    {"name": n, "local_id": n} for n in ("aaa-hi", "mmm-mid", "zzz-lo", "nnn-nd")]))
# top-N recipe verbatim: flatten | tail -n +2 | LC_ALL=C sort -k6 -rg
pipe = (
    f"{sys.executable} {flatten} {rank_fixture} /tmp/verify_rank_inv.json "
    "| tail -n +2 | LC_ALL=C sort -t$'\\t' -k6 -rg | cut -f1"
)
order = subprocess.run(["bash", "-c", pipe], capture_output=True, text=True).stdout.split()
if order[:3] != ["aaa-hi", "mmm-mid", "zzz-lo"] or "nnn-nd" in order[:3]:
    print(f"  CONTRACT recipe ranking order was {order}, expected [aaa-hi, mmm-mid, zzz-lo, nnn-nd]")
    flat_fail = 1

# Contract: the guide must actually USE the safe ranking form — grep it so a drift
# back to `-rn` or a dropped `LC_ALL=C`/`tail -n +2` fails the gate (the pipeline
# test above runs a hardcoded copy and can't catch guide drift on its own).
guide = os.path.join(SKILL, "references", "metrics-guide.md")
gtext = open(guide).read()
import re as _re
if (
    _re.search(r"sort\b[^\n]*-rn", gtext)              # no numeric-sort ranking anywhere
    or "-k6 -rg" not in gtext                          # top-N max-sort present and correct
    or gtext.count("LC_ALL=C sort") < 3                # all three sort pipelines locale-pinned
    or "tail -n +2" not in gtext                       # header stripped before ranking
    or "$4>0{print $9-$8" not in gtext                 # growth variant guards no-data
):
    print("  CONTRACT metrics-guide.md ranking drifted (need -rg, LC_ALL=C, tail -n +2, $4>0 growth guard)")
    flat_fail = 1

contract_fail = contract_fail or flat_fail
print(f"metrics-flatten contract: {'FAIL' if flat_fail else 'ok'}")


def real_case_exists(path):
    directory, name = os.path.split(path)
    if not os.path.isdir(directory):
        return False
    return name in os.listdir(directory)


broken = 0
checked = 0
for root, _dirs, files in os.walk(os.path.join(SKILL, "references")):
    for f in files:
        if not f.endswith(".md"):
            continue
        src = os.path.join(root, f)
        for m in re.finditer(r"\]\((\.{0,2}[\w./-]+\.md)(#[\w-]*)?\)", open(src).read()):
            target = os.path.normpath(os.path.join(root, m.group(1)))
            checked += 1
            if not real_case_exists(target):
                broken += 1
                if broken <= 10:
                    print(f"  BROKEN {os.path.relpath(src, SKILL)} -> {m.group(1)}")
print(f"links: {checked} checked, {broken} broken")
sys.exit(1 if (fail or broken or contract_fail) else 0)
