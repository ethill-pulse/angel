#!/bin/bash
# Read-only calendar reader. Wraps cal-read.swift (EventKit via Swift).
# Usage: cal-read.sh [start: YYYY-MM-DD] [end: YYYY-MM-DD]
# Defaults to today through today+7.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec swift "$SCRIPT_DIR/cal-read.swift" "$@"
