#!/usr/bin/env bash
# Send a CloudTower API request and write the response to a file.
#
# Usage: call.sh [-X METHOD] <path> [body-file]   send a request
#        call.sh login                            obtain a token and cache it
#
#   path       full API path from the operation file title, e.g. /v2/api/get-vms
#   body-file  JSON request body file (omit for operations without a body)
#
# Environment (explicit env always beats the cached env file):
#   CLOUDTOWER_ENDPOINT   base URL, e.g. https://tower.example.com (required)
#   CLOUDTOWER_TOKEN      API token; `call.sh login` obtains and caches one
#   CLOUDTOWER_USERNAME   used only by `call.sh login`; CLOUDTOWER_USER also
#   CLOUDTOWER_PASSWORD   accepted. Credentials are never printed.
#   CLOUDTOWER_SOURCE     login source enum, default LOCAL
#   CLOUDTOWER_ENV_FILE   cached state file (default /tmp/cloudtower.env),
#                         written by `call.sh login` and sourced on every call
#                         so the token survives shells that reset environment
#   CLOUDTOWER_CURL_OPTS  extra curl options, e.g. "--cacert /path/ca.pem"
set -euo pipefail

env_file=${CLOUDTOWER_ENV_FILE:-/tmp/cloudtower.env}

# Fill missing vars from the cached env file; explicit env wins.
_endpoint=${CLOUDTOWER_ENDPOINT:-}
_token=${CLOUDTOWER_TOKEN:-}
if [ -f "$env_file" ]; then
  # shellcheck disable=SC1090
  . "$env_file"
fi
CLOUDTOWER_ENDPOINT=${_endpoint:-${CLOUDTOWER_ENDPOINT:-}}
CLOUDTOWER_TOKEN=${_token:-${CLOUDTOWER_TOKEN:-}}

: "${CLOUDTOWER_ENDPOINT:?set CLOUDTOWER_ENDPOINT, e.g. https://tower.example.com}"

# -k: CloudTower appliances commonly use self-signed certificates; pass a CA
# via CLOUDTOWER_CURL_OPTS to verify instead.
curl_base=(-sS -k -H 'content-type: application/json')
[ -n "${CLOUDTOWER_CURL_OPTS:-}" ] && curl_base+=(${CLOUDTOWER_CURL_OPTS})

if [ "${1:-}" = "login" ]; then
  username=${CLOUDTOWER_USERNAME:-${CLOUDTOWER_USER:-}}
  : "${username:?set CLOUDTOWER_USERNAME (or CLOUDTOWER_USER) to log in}"
  : "${CLOUDTOWER_PASSWORD:?set CLOUDTOWER_PASSWORD to log in}"
  body=$(LOGIN_USERNAME="$username" python3 -c 'import json, os
print(json.dumps({"username": os.environ["LOGIN_USERNAME"],
                  "password": os.environ["CLOUDTOWER_PASSWORD"],
                  "source": os.environ.get("CLOUDTOWER_SOURCE", "LOCAL")}))')
  resp=$(printf '%s' "$body" | curl "${curl_base[@]}" -X POST --data-binary @- \
    "${CLOUDTOWER_ENDPOINT}/v2/api/login")
  if ! token=$(printf '%s' "$resp" | python3 -c 'import json,sys
print(json.load(sys.stdin)["data"]["token"])' 2>/dev/null); then
    echo "login failed: $(printf '%s' "$resp" | head -c 300)" >&2
    exit 1
  fi
  umask 077
  printf 'export CLOUDTOWER_ENDPOINT=%q\nexport CLOUDTOWER_TOKEN=%q\n' \
    "$CLOUDTOWER_ENDPOINT" "$token" >"$env_file"
  echo "login OK — token cached in $env_file (call.sh loads it automatically)"
  exit 0
fi

method=POST
if [ "${1:-}" = "-X" ]; then
  method=${2:?-X needs a method}
  shift 2
fi
path=${1:?usage: call.sh [-X METHOD] <path> [body-file] | call.sh login}
body_file=${2:-}

if [ -n "$body_file" ] && [ ! -f "$body_file" ]; then
  echo "body file not found: $body_file" >&2
  exit 2
fi

out="/tmp/tower_$(date +%Y%m%d_%H%M%S)_$RANDOM.json"

args=("${curl_base[@]}" -X "$method" -o "$out" -w '%{http_code}')
case "$path" in
*/login) ;;
*)
  : "${CLOUDTOWER_TOKEN:?set CLOUDTOWER_TOKEN or run 'call.sh login' first (see references/authentication.md)}"
  args+=(-H "Authorization: $CLOUDTOWER_TOKEN")
  ;;
esac
[ -n "$body_file" ] && args+=(--data-binary "@$body_file")

status=$(curl "${args[@]}" "${CLOUDTOWER_ENDPOINT}${path}")
size=$(wc -c <"$out" | tr -d ' ')

echo "HTTP $status  response: $out ($size bytes)"
echo "preview: $(head -c 300 "$out")"
if [ "$status" -ge 400 ]; then
  exit 1
fi
