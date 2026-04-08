# Working Model

## How Eric wants to work with Angel

- **Write everything locally** — agent/ is Angel's workspace to organize freely. Refactor structure as needed to stay efficient.
- **NEVER write to Notion** unless Eric explicitly says to. Notion is read-only unless directed.
- **TODOs** live in `agent/todos.md` or `agent/todos/{project}.md`.
- **Task plans** for subagents written as files (e.g., `agent/plans/`) so a Claude Code instance can pick them up.
- **Efficiency is critical** — bedrock token spend is real. Eric will notice if costs spike.

## Heartbeat efficiency rules

- Track last-consolidated date in `agent/heartbeat.md` — only process journal entries dated after that watermark.
- Never re-scan already-consolidated journals.
- Keep memories concise so re-reading them at session start is cheap.
- Spawn subagents for heavy research/work, not the main context.

## Subagent pattern

Common flow:
1. Eric brings a problem
2. Angel generates a task plan doc
3. Eric spins up a Claude Code instance or subagent to execute it
4. Angel tracks status and updates memories/todos accordingly

## Data sources

- **Meeting notes**: Gemini (Google AI) emails high-level meeting notes to Eric from `gemini-notes@google.com` after each meeting. Use `scripts/mail-read.sh --days N --sender gemini-notes@google.com --body` to retrieve them. This is the primary meeting-note source until Google Drive/Docs MCP is available.
- **Google Drive**: Mounted at `~/Library/CloudStorage/GoogleDrive-ethill@clearstreet.io/`. Angel-export CSVs in `My Drive/angel-exports/` — read via `Glob` + `Read`. GDoc/GSheet stubs not readable directly.
- **Notion**: Read via MCP. Never write unless explicitly directed.

## Heartbeat trigger

Eric runs `make heartbeat` manually for now. Will set up a cron later.

## Notes

`notes/` is Eric's primary note-taking location — he is committing to keeping notes there.
- Slim now, will grow over time
- Sort by modification time to find recent activity
- Patterns will emerge as volume increases — watch for topics, people, recurring themes
- Read freely when relevant to current work
- Do not write to `notes/`. It is read-only for Angel.

## Delegation style

Eric delegates based on the person's ability to handle ambiguity. Goal is to grow everyone toward more abstract work over time.
- Good manager = never a single point of failure, team not complaining about ambiguity
- Angel should help draft delegation artifacts (tickets, plans, task docs) calibrated to the person
- Track what's delegated and to whom so nothing falls through
- As team members' working styles become clear from notes/journals, factor that into how plans are written for them
