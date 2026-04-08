#!/bin/bash
# Read-only GitHub PR reader. Lists merged PRs across pulseprime repos since a given date.
# Usage: pr-read.sh [--since YYYY-MM-DD] [--repo OWNER/REPO] [--limit N]
# Defaults: --since 7 days ago, both pulseprime/pulse and pulseprime/polaris, --limit 100
#
# Output per PR: #<num> [<date>] <author>: <title> (+<add>/-<del>, <files> files)

SINCE=""
REPOS=()
LIMIT=100

while [[ $# -gt 0 ]]; do
    case "$1" in
        --since) SINCE="$2"; shift 2 ;;
        --repo)  REPOS+=("$2"); shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

if [[ ${#REPOS[@]} -eq 0 ]]; then
    REPOS=("pulseprime/pulse" "pulseprime/polaris")
fi

if [[ -z "$SINCE" ]]; then
    SINCE=$(date -v-7d +%Y-%m-%d 2>/dev/null || date -d '7 days ago' +%Y-%m-%d)
fi

for REPO in "${REPOS[@]}"; do
    echo "=== $REPO (merged since $SINCE) ==="
    gh pr list --repo "$REPO" --state merged --limit "$LIMIT" \
        --json number,title,author,mergedAt,additions,deletions,changedFiles \
        --jq "[.[] | select(.mergedAt >= \"${SINCE}\")] | sort_by(.mergedAt) | reverse | .[] | \"#\(.number) [\(.mergedAt[:10])] \(.author.login): \(.title) (+\(.additions)/-\(.deletions), \(.changedFiles) files)\""
    echo ""
done
