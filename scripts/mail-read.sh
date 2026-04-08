#!/bin/bash
# Read-only mail reader via AppleScript.
# Usage: mail-read.sh [--days N] [--mailbox NAME] [--sender PAT] [--subject PAT] [--body]
#
# Options:
#   --days N        Messages received in the last N days (default: 1)
#   --mailbox NAME  Mailbox to read (default: inbox)
#   --sender PAT    Filter to senders containing PAT (case-insensitive)
#   --subject PAT   Filter to subjects containing PAT (case-insensitive)
#   --body          Include message body (first 500 chars)
#
# Output: date | from | subject [| body]

DAYS=1
MAILBOX="INBOX"
SENDER_FILTER=""
SUBJECT_FILTER=""
INCLUDE_BODY=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --days)    DAYS="$2";           shift 2 ;;
        --mailbox) MAILBOX="$2";        shift 2 ;;
        --sender)  SENDER_FILTER="$2";  shift 2 ;;
        --subject) SUBJECT_FILTER="$2"; shift 2 ;;
        --body)    INCLUDE_BODY=true;   shift 1 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

# Convert filters to lowercase in bash for comparison in AppleScript
SENDER_LOW=$(echo "$SENDER_FILTER" | tr '[:upper:]' '[:lower:]')
SUBJECT_LOW=$(echo "$SUBJECT_FILTER" | tr '[:upper:]' '[:lower:]')

osascript <<EOF
tell application "Mail"
    set cutoff to (current date) - ($DAYS * days)
    set targetBox to mailbox "$MAILBOX" of first account
    set allMsgs to (messages of targetBox whose date received >= cutoff)
    set output to ""
    repeat with m in allMsgs
        set fromAddr to sender of m
        set subj to subject of m
        set dateStr to (date received of m) as string

        set fromLow to do shell script "echo " & quoted form of fromAddr & " | tr '[:upper:]' '[:lower:]'"
        set subjLow to do shell script "echo " & quoted form of subj & " | tr '[:upper:]' '[:lower:]'"

        set senderOk to ("$SENDER_LOW" is "" or fromLow contains "$SENDER_LOW")
        set subjectOk to ("$SUBJECT_LOW" is "" or subjLow contains "$SUBJECT_LOW")

        if senderOk and subjectOk then
            set msgLine to dateStr & " | " & fromAddr & " | " & subj
            if $INCLUDE_BODY then
                set bodyText to content of m
                if (length of bodyText) > 500 then
                    set bodyText to (text 1 thru 500 of bodyText) & "..."
                end if
                set msgLine to msgLine & " | " & bodyText
            end if
            set output to output & msgLine & linefeed
        end if
    end repeat
    return output
end tell
EOF
