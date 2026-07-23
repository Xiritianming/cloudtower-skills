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

# Contract: ranking is owned by scripts/metrics-rank.sh, RUN here (not grepped) so
# a real break is caught by execution. The fixture anti-correlates name with value
# (highest value = lexically-first "aaa"), uses a fractional %.6g mantissa, and
# multi-point streams, so a lexical sort, wrong key column, `-rn`/`-nr` (misreads
# the exponent), or a comma locale all produce a wrong order.
rank_script = os.path.join(SKILL, "scripts", "metrics-rank.sh")
rank_fixture = "/tmp/verify_rank_resp.json"
open(rank_fixture, "w").write(json.dumps([
    {"task_id": None, "data": {"dropped": False, "unit": "TIME", "sample_streams": [
        {"labels": {"_vm": "aaa-hi", "metric_name": "lat"}, "points": [{"t": 1, "v": 20_000_000}, {"t": 2, "v": 81_234_567}]},
        {"labels": {"_vm": "mmm-mid", "metric_name": "lat"}, "points": [{"t": 1, "v": 10_000_000}, {"t": 2, "v": 30_111_222}]},
        {"labels": {"_vm": "zzz-lo", "metric_name": "lat"}, "points": [{"t": 1, "v": 940_000}, {"t": 2, "v": 955_000}]},
        {"labels": {"_vm": "sgl-1pt", "metric_name": "lat"}, "points": [{"t": 1, "v": 999_000_000}]},  # single point: no growth
        {"labels": {"_vm": "nnn-nd", "metric_name": "lat"}, "points": [{"t": 1, "v": None}]}]}},         # no data
]))
open("/tmp/verify_rank_inv.json", "w").write(json.dumps([
    {"name": n, "local_id": n} for n in ("aaa-hi", "mmm-mid", "zzz-lo", "sgl-1pt", "nnn-nd")]))
body = "/tmp/verify_rank_body.tsv"
subprocess.run(["bash", "-c",
    f"{sys.executable} {flatten} {rank_fixture} /tmp/verify_rank_inv.json | tail -n +2 > {body}"], check=True)

# max: by the aggregated value; single-point 999M ranks #1, no-data sinks last.
max_order = subprocess.run(["bash", rank_script, body, "max"], capture_output=True, text=True).stdout.split("\n")
max_names = [ln.split("\t")[0] for ln in max_order if ln.strip()]
# growth: last-first; needs >=2 points, so single-point and no-data are EXCLUDED.
grow_out = subprocess.run(["bash", rank_script, body, "growth"], capture_output=True, text=True).stdout
grow_names = [ln.split("\t")[1] for ln in grow_out.splitlines() if ln.strip()]
if (
    max_names[0] != "sgl-1pt"                                # 999M single point is the largest max
    or [n for n in max_names if n in ("aaa-hi", "mmm-mid", "zzz-lo")] != ["aaa-hi", "mmm-mid", "zzz-lo"]
    or max_names[-1] != "nnn-nd"                             # no-data sinks last under -rg
    or grow_names != ["aaa-hi", "mmm-mid", "zzz-lo"]         # growth order; sgl-1pt & nnn-nd excluded ($4>1)
):
    print(f"  CONTRACT metrics-rank.sh wrong: max={max_names} growth={grow_names}")
    flat_fail = 1

# Contract: the recipes must DELEGATE ranking to metrics-rank.sh — a robust,
# spelling-independent check (unlike grepping sort flags). Reverting to an inline
# sort would drop these references and fail here; the execution test above proves
# the script itself ranks correctly.
gtext = open(os.path.join(SKILL, "references", "metrics-guide.md")).read()
if gtext.count("metrics-rank.sh") < 2:   # top-N recipe + fleet recipe
    print("  CONTRACT metrics-guide.md recipes no longer delegate ranking to metrics-rank.sh")
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
