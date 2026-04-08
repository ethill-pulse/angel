---
name: notes/ directory is read-only for Angel
description: Angel should never write to notes/ — it's Eric's personal notes directory for ingesting context only
type: feedback
---

Do not write to `notes/`. It is read-only for Angel.

**Why:** notes/ is Eric's personal notes directory. Angel should only read from it to ingest context. Eric writes his own notes there; Angel's job is to consume that data and persist insights into `agent/journals/` and `agent/memories/`.

**How to apply:** When given context from Slack, meetings, or other sources, journal it and update memory files. Never create files under `notes/`.
