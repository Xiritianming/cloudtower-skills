#!/usr/bin/env bash
# Send a CloudTower API request and write the response to a file.
#
# Usage: call.sh [-X METHOD] <path> [body-file]
#   path       full API path from the operation file title, e.g. /v2/api/get-vms
#   body-file  JSON request body file (omit for operations without a body)
#
# Env: CLOUDTOWER_ENDPOINT  base URL, e.g. https://tower.example.com (required)
#      CLOUDTOWER_TOKEN     API token (required except for /v2/api/login)
#      CLOUDTOWER_CURL_OPTS extra curl options, e.g. "--cacert /path/ca.pem"
set -euo pipefail

method=POST
if [ "${1:-}" = "-X" ]; then
  method=${2:?-X needs a method}
  shift 2
fi
path=${1:?usage: call.sh [-X METHOD] <path> [body-file]}
body_file=${2:-}

: "${CLOUDTOWER_ENDPOINT:?set CLOUDTOWER_ENDPOINT, e.g. https://tower.example.com}"
if [ -n "$body_file" ] && [ ! -f "$body_file" ]; then
  echo "body file not found: $body_file" >&2
  exit 2
fi

out="/tmp/tower_$(date +%Y%m%d_%H%M%S)_$RANDOM.json"

# -k: CloudTower appliances commonly use self-signed certificates; pass a CA
# via CLOUDTOWER_CURL_OPTS to verify instead.
args=(-sS -k -X "$method" -o "$out" -w '%{http_code}' -H 'content-type: application/json')
case "$path" in
*/login) ;;
*)
  : "${CLOUDTOWER_TOKEN:?set CLOUDTOWER_TOKEN or log in first (see references/authentication.md)}"
  args+=(-H "Authorization: $CLOUDTOWER_TOKEN")
  ;;
esac
[ -n "$body_file" ] && args+=(--data-binary "@$body_file")
[ -n "${CLOUDTOWER_CURL_OPTS:-}" ] && args+=(${CLOUDTOWER_CURL_OPTS})

status=$(curl "${args[@]}" "${CLOUDTOWER_ENDPOINT}${path}")
size=$(wc -c <"$out" | tr -d ' ')

echo "HTTP $status  response: $out ($size bytes)"
echo "preview: $(head -c 300 "$out")"
if [ "$status" -ge 400 ]; then
  exit 1
fi
