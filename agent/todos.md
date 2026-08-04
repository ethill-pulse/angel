# TODOs

## Engineering

- **[x]** **Websocket / JSON API** for client direct-connect — Eric's codegen (`json-ws-gen-digital.py` #2587) landed and shipped as part of the Parataxis low-touch launch. *(added 2026-06-01; done: 2026-08-04)*

## Management

- **[x]** Drive the security/access-provisioning conversation for July-15 low-touch client access — resolved by the fact of launch: the Parataxis low-touch client went live (tracker shows "Parataxis Go Live" = Complete). No explicit written security sign-off seen, but treating as closed. *(added 2026-06-25; done: 2026-08-04)*
- **[ ]** **Update the team on Thursday's (Aug 6) CaaS meeting status** — action item from the Aug 4 Digital Dev Sync. *(added 2026-08-04)*
- **[ ]** **Check in with Atakan** — only 3 PRs in the last 5 weeks, lowest of any report; owns Haruko/Talos recon work per the Aug 4 Dev Sync, but worth confirming he's not blocked. One of his PRs was reverted and later relanded by Aksel under the same title — possible ownership handoff worth clarifying. **Natural opening: Wed Aug 5, 9:30am — recurring "Eric, Atakan, Aksel" meeting already on calendar.** *(added 2026-08-04)*
- **[ ]** **Check in with Talgat** — went quiet on PRs Jul 30 → Aug 4 after an otherwise-daily cadence; unclear if OOO, reassigned, or between milestones. *(added 2026-08-04)*
- **[ ]** **Decide the position-recovery system end state** — open group action item from the Aug 4 Digital Dev Sync (disk-backed queue / async persistence approach for order-status recovery). *(added 2026-08-04)*
- **[ ]** Perp instrument type config in FACT/pulse — **NOT YET on Eric's plate**. Collin Zoll still needs to finalize documentation and get buy-in first. Revisit once Collin follows up. *(added 2026-06-01)*

## Engineering — backlog / forward-looking (from Jun 26 team sync)

- **[ ]** **Hyperliquid equity perp support** — forward-looking; ties to the perp-instrument-type-config item above (Collin Zoll). *(added 2026-06-30)*

## Awareness (not action items, but worth knowing)

- The `polaris` repo has been fully merged into `pulse` (as of Jul 30) — it's now `libs/polaris` inside pulse. Any docs/onboarding material that still describes `polaris` as a separate repo (including the top-level workspace `CLAUDE.md`) is stale.
- Calendar access (`scripts/cal-read.sh`) is now working again (confirmed in a same-day re-run) — the earlier denial was session/terminal-specific, not a lasting break. Notion MCP still needs re-authentication (OAuth flow requires Eric in the browser) — no Notion search performed yet either heartbeat pass today.

