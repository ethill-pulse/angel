#!/bin/bash
# Output merged PRs for a repo over a date range as CSV.
# Usage: pr-csv.sh --repo OWNER/REPO [--since YYYY-MM-DD] [--until YYYY-MM-DD] [--limit N]
# Defaults: --since 7 days ago, --until today, --limit 200

SINCE=""
UNTIL=""
REPO=""
LIMIT=200

while [[ $# -gt 0 ]]; do
    case "$1" in
        --since) SINCE="$2"; shift 2 ;;
        --until) UNTIL="$2"; shift 2 ;;
        --repo)  REPO="$2"; shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

if [[ -z "$REPO" ]]; then
    echo "Error: --repo OWNER/REPO is required" >&2
    exit 1
fi

if [[ -z "$SINCE" ]]; then
    SINCE=$(date -v-7d +%Y-%m-%d 2>/dev/null || date -d '7 days ago' +%Y-%m-%d)
fi

if [[ -z "$UNTIL" ]]; then
    UNTIL=$(date +%Y-%m-%d)
fi

echo "TITLE,PR,DATE,AUTHOR,LINES_ADDED,LINES_REMOVED,DESCRIPTION"

gh pr list --repo "$REPO" --state merged --limit "$LIMIT" \
    --json number,title,author,mergedAt,additions,deletions,body \
    --jq "[.[] | select(.mergedAt >= \"${SINCE}\" and .mergedAt <= \"${UNTIL}T23:59:59Z\")] | sort_by(.mergedAt) | .[] |
        \"\\\"\" + (.title | gsub(\"\\\"\"; \"\") | gsub(\"\n\"; \" \")) + \"\\\",\" +
        (.number | tostring) + \",\" +
        .mergedAt[:10] + \",\" +
        .author.login + \",\" +
        (.additions | tostring) + \",\" +
        (.deletions | tostring) + \",\" +
        \"\\\"\" + ((.body // \"\") | gsub(\"\\\"\"; \"\") | gsub(\"\n\"; \" \") | gsub(\"\r\"; \"\") | .[0:300]) + \"\\\"\""
