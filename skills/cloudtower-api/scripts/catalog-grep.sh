#!/usr/bin/env bash
# Grep the metrics-lookup skill's metric catalog — the only source of metric
# names for the Metrics operations.
#
# Usage: catalog-grep.sh <keyword> [keyword...]
#   Keywords are OR-combined, case-insensitive. Pass symptom words in both
#   languages (names are English, descriptions Chinese): error 错误 丢包 drop
#
# The catalog is the metrics-lookup skill's references/ directory. This script
# locates it across known install layouts; pin an unusual location with
# METRICS_LOOKUP_DIR=/path/to/metrics-lookup/references.
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: catalog-grep.sh <keyword> [keyword...]" >&2
  exit 2
fi

script_dir=$(cd "$(dirname "$0")" && pwd)
skill_root=$(dirname "$script_dir")

candidates=(
  "${METRICS_LOOKUP_DIR:-}"
  "$skill_root/../metrics-lookup/references"
  /workspace/.claude/skills/metrics-lookup/references
  /workspace/.home/.claude/skills/metrics-lookup/references
  /workspace/.home/.agents/skills/metrics-lookup/references
  "$HOME/.claude/skills/metrics-lookup/references"
  "$HOME/.agents/skills/metrics-lookup/references"
)

catalog=""
for c in "${candidates[@]}"; do
  if [ -n "$c" ] && [ -f "$c/index.md" ]; then
    catalog=$c
    break
  fi
done

if [ -z "$catalog" ]; then
  echo "metrics-lookup catalog not found (searched sibling dir and known skill roots)." >&2
  echo "Fix: set METRICS_LOOKUP_DIR=<path to metrics-lookup/references>, or have the" >&2
  echo "operator install the metrics-lookup skill beside cloudtower-api." >&2
  echo "Metric names only come from the catalog — the live API cannot validate them." >&2
  exit 3
fi

pattern=$(IFS='|'; printf '%s' "$*")
echo "catalog: $catalog" >&2
matches=$(grep -riEn --include='metrics_*.md' "$pattern" "$catalog" || true)

if [ -z "$matches" ]; then
  echo "no match for '$pattern' — retry with broader bilingual symptom words" >&2
  echo "(e.g. latency 延迟 / error 错误 / 丢包 drop), or read $catalog/index.md" >&2
  exit 1
fi

printf '%s\n' "$matches" | head -40
count=$(printf '%s\n' "$matches" | wc -l | tr -d ' ')
if [ "$count" -gt 40 ]; then
  echo "(showing 40 of $count matching lines — narrow the keywords)" >&2
fi
