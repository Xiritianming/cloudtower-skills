#!/usr/bin/env bash
# Rank a flattened metrics TSV (from metrics-flatten.py) correctly. This owns the
# fragile sort so recipes don't hand-write it: general-numeric + locale-pinned
# (%.6g prints values >=1e6 as 8e+07, which `sort -n` and a comma locale misread),
# and growth needs two points so single-point / no-data rows are excluded.
#
# Usage: metrics-rank.sh <flat.tsv | -> [max|growth] [N]
#   max    (default): rank by the `max` column (col 6), highest first
#   growth: rank by last-first over the window (counters); prepends the growth
#           value; excludes rows with <2 points (single-point top-N responses and
#           no-data rows cannot express growth)
#   N      (default 20): how many rows to print
#
# Input is the flattener's TSV body (the recipes strip the header with tail -n +2).
# A stray header row is still handled: it sinks under max (its `max` cell is
# non-numeric -> 0) and is excluded under growth (`$4+0 > 1`). Read a file, or `-`
# for stdin (e.g. after an awk metric filter).
set -euo pipefail

src=${1:-}
mode=${2:-max}
n=${3:-20}
if [ -z "$src" ]; then
  echo "usage: metrics-rank.sh <flat.tsv | -> [max|growth] [N]" >&2
  exit 2
fi
[ "$src" = "-" ] && src=/dev/stdin

# Top-N is `awk 'NR<=n'`, not `head`: head closes the pipe after N lines, which
# would SIGPIPE the still-writing sort and, under `pipefail`, fail the script
# (exit 141) on any fleet large enough to overflow the pipe buffer. `$4+0 > 1`
# forces a numeric compare so a stray header row ("points") is excluded, not
# string-compared as > "1".
case "$mode" in
  max)
    LC_ALL=C sort -t$'\t' -k6 -rg "$src" | awk -v n="$n" 'NR <= n'
    ;;
  growth)
    awk -F'\t' '$4 + 0 > 1 { print ($9 - $8) "\t" $0 }' "$src" | LC_ALL=C sort -rg | awk -v n="$n" 'NR <= n'
    ;;
  *)
    echo "mode must be 'max' or 'growth', got '$mode'" >&2
    exit 2
    ;;
esac
