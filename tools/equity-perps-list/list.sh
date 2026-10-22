#!/usr/bin/env bash
# List Binance UM + Hyperliquid equity perps with market data and historical candles enabled.
#
# Usage:
#   ADMIN_JWT=... ./list.sh <cs-dev|dev|staging|clearstreet> [--apply]   (dry run unless --apply)
#
# ADMIN_JWT is sessionStorage 'adminjwt' from the admin UI. Run with no args for full
# instructions.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

USAGE="Usage: ADMIN_JWT=... $0 <cs-dev|dev|staging|clearstreet> [--apply]"

if [[ $# -eq 0 ]]; then
  python3 "$SCRIPT_DIR/list_equity_perps.py"
  echo "$USAGE"
  exit 1
fi

ENV="$1"
shift
case "$ENV" in
  cs-dev|dev|staging|clearstreet) ADMIN_URL="https://admin.${ENV}.tokyo.pulseprime.systems" ;;
  *) echo "$USAGE" >&2; exit 1 ;;
esac

if [[ -z "${ADMIN_JWT:-}" ]]; then
  echo "ADMIN_JWT not set (sessionStorage 'adminjwt' from the ${ENV} admin UI)" >&2
  exit 1
fi

echo "=== ${ENV}: ${ADMIN_URL} ==="
python3 "$SCRIPT_DIR/list_equity_perps.py" --admin-url "$ADMIN_URL" "$@"
