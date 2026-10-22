#!/usr/bin/env bash
# Validate funding rate coverage for the trailing 24 hours.
#
# Usage:
#   ./validate.sh [prod|cs-dev] [--hours N] [--grace-minutes M] [--all]   (default: prod)
#
# Captures mktdata.fundingrate from the target environment, then checks
# that every target CLST symbol has a settlement for each slot its funding
# interval (any divisor of 24h) implies. Extra args pass through to the validator.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PULSE_DIR="$(cd "$SCRIPT_DIR/../../repos/pulse" && pwd)"
TOOLS_DIR="$PULSE_DIR/tools"

ENV="${1:-prod}"
case "$ENV" in
  prod)   KAFKA_CFG="$SCRIPT_DIR/kafka-prod.yml" ;;
  cs-dev) KAFKA_CFG="$SCRIPT_DIR/kafka-cs-dev.yml" ;;
  *)      echo "Usage: $0 [prod|cs-dev]" >&2; exit 1 ;;
esac

RAW="$SCRIPT_DIR/fundingrate-${ENV}-raw.yml"

echo "=== Capturing mktdata.fundingrate from ${ENV} ==="
cd "$TOOLS_DIR"
cargo run -q -p kafka-capture -- \
  --config "$KAFKA_CFG" \
  --topic mktdata.fundingrate \
  --partition 0 \
  --start beginning \
  --end end \
  2>/dev/null > "$RAW"
echo "Captured $(wc -l < "$RAW") lines"
echo ""

echo "=== Validating ==="
python3 "$SCRIPT_DIR/validate_funding_rates.py" "$RAW" "${@:2}"
