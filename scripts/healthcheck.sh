#!/usr/bin/env sh
set -eu
curl --fail --silent "${API_URL:-http://localhost:8000}/health" >/dev/null
