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
