# Digital Engineering Team

Eric's direct reports, carried over from Pulse Prime through the Clear Street acquisition (Dec 2025).

| Name | Title | Location | Notes |
|------|-------|----------|-------|
| Aksel Hakim | Consultant | Amsterdam | |
| Anton Ronis | Head of Quant, CS Digital | Israel | Eric's peer — reports to Bob/Suley. RenGen-connected; worked with Eric to retire RenGen legacy systems in favor of Pulse. Prior military — can be unavailable for weeks at a time. GitHub: `ant0wn` |
| Atakan Kupeli | Consultant | Turkey | |
| Chris Davidson | Staff Software Engineer | Chicago | Owns options instrument creation end-to-end: deal entry endpoint, FACT instrument ID flow, custom instrument setup in Talos/Pulse. |
| Emre Ekici | Consultant | Turkey | Led the QuestDB migration effort. Strong on venue integrations (Kalshi, Haruko) and streaming/mktdata pipelines. Now working on Deribit index price collector (options settlement). |
| Erick Arce | Senior Staff Software Engineer | New York City | |
| Estiven Salazar | Software Engineer | New York City | |
| Matt Gow | Senior Staff Software Engineer | Chicago | Was head of infrastructure at Pulse Prime Technologies |
| Ömer Yılmaz | RenGen FTE / CS Consultant | Turkey (RenGen) | Still employed by RenGen; CS consultant role gives him CS laptop + access. Technically reports to Eric. GitHub: `litityum` |
| Selman | RenGen / CS Consultant | — | Same consultant arrangement as Ömer. GitHub: `SelmanB`. Surfaced Aug 4 heartbeat doing venue-integration work (Coinbase, Ibkr, Coinbase National, Bitso) — confirm scope/reporting line if he becomes a regular contributor. |
| Talgat Taskhozhayev | Senior Software Engineer | New York City | |
| Amit Kirdatt (akirdatt) | Software Engineer | — | Transferred to Eric's org May 20, 2026 (from Rama/BK). Owns Haruko integration. CaaS (custody/BitGo) moving to Ankit Singh (BK/CSC team). |

## Mid-year peer feedback cycle (June 2026) — DELIVERED

Eric delivered reviews to direct reports Jun 11–15. Content/draft in `notes/20260610_peer_feedback.md` (personnel-sensitive — handle discreetly). Summary per person:

- **Talgat** — the substantive/critical one, framed as "thin ice." Themes: (1) **collaboration** — combative about decisions then reverses, doesn't "disagree and commit," should take a "patient educator" approach (start at the other person's understanding, prioritize faster back-and-forth, stop more often for others to participate); (2) **AI self-sufficiency** — multiple people report he asks them questions whose answers are verbatim what Claude Code would give; ask Claude first ("other people's time is more important than your aversion to AI"); (3) **don't treat everything as an emergency / choose battles** — "if everything is an emergency, nothing is." Also flagged poor ownership ("works as designed" deflection on integration bugs). Universal feedback across the team; **Suley, Bob, and Eric aligned and watching.** Long-term gauge: are people asking him for feedback vs. him having to jump in. **Talgat will ask for follow-up peer feedback in 3–4 weeks and report to Suley.** Note: **Amit didn't submit any peer reviews (too new); Eric working with him now is a chance to leave a good impression — Eric plans to check with Amit in a couple weeks on how it's going with Talgat.**
- **Erick** — strong (avg ≥3.5 all questions). Recognized as a strong eng leader, scalable architectural decisions, pushes back on off-mission asks. Growth areas: **soften abrasive/impatient approach with juniors** (tiered tone), and **qualify urgency on after-hours requests** (people treat off-hours asks as emergencies — summarize impact/urgency). Eric + Erick need to do better getting **Emre** more involved with the team (Erick was the only one to respond to Emre's reviews).
- **Estiven** — strong (all 4s except "knowledgeable about the space for his level" = 3.5 avg). Tremendous growth: FE SME → senior full-stack, proactive, takes backend ownership, operating above title. Suggestion: get into the weeds on **business requirements** (Trade/Account/Entity modeling, options trading) — the "why."
- **Chris** — strong (all ≥3.6; "knowledgeable for level" = 4). Multiple unsolicited org compliments. **Eric plans to tell Suley & Bob that Chris is probably the only person who can fully cover for Eric when out.** Main suggestion: once he has breathing room on Spot/Options, make a **public effort to do cleanup** (avoid "Claude duct tape" fixes that bury problems) — Eric will give him time for it; low-touch projects should shift some of his dev-stress load to others.

For Erick, Estiven, and Chris, Eric relayed the Talgat themes and asked each to flag if they see improvement (or the same challenges) with Talgat.

## Status check-ins needed (as of Aug 4 heartbeat, from 5-week PR-activity gap)

- **Atakan** — only 3 PRs in 5 weeks (Jun 30–Aug 4), lowest of anyone on the team. Not idle — owns Haruko/Talos reconciliation dev work per the Aug 4 Dev Sync (action item: notify team when it lands in dev) — but worth confirming he's not blocked or under-scoped. One of his PRs (testnet integration, #2917) was reverted by Eric and later relanded by **Aksel** under the same title — possible quiet ownership handoff of that workstream from Atakan to Aksel.
- **Talgat** — went quiet Jul 30 → Aug 4 after an otherwise-daily PR cadence (Trade-Engine-Bots iteration, then Trade-Engine persistence/Redb work). Worth a check-in — OOO, reassigned, or just between milestones is unclear from PR history alone.
- **Estiven** — gap Jul 27–Aug 2 (~1 week), then reappeared Aug 3 with a brand-new "loans-widget" thread (#3310) — a new initiative, not yet reflected in projects.md milestone tracker; probably worth asking about scope/priority.
- **SelmanB** (GitHub handle) — **identified: Selman, a Clear Street consultant via RenGen** (same arrangement as Ömer). 6 PRs Jul 21–31, venue-integration work (Coinbase, new `Venue::Ibkr` skeleton, Coinbase National, Bitso). Add to the team roster table above if he becomes a recurring contributor.

## Org leveling (Jun 30, 2026)

HR is running a project to align internal roles/titles with external industry benchmarks — functional leveling + title standardization (discussed in the Jun 30 Eric/Brian 1:1). Likely to touch how Eric's reports are titled/leveled. Watch for follow-through; relevant context for any leveling/promotion conversations.

## Structure

- Eric reports into Clear Street as Principal Engineer, Digital Engineering
- 9 direct reports distributed (Amsterdam, Turkey, Chicago, NYC, + Amit)
- Four consultants (Aksel, Atakan, Emre, Ömer), six FTEs
- Anton Ronis (peer, Head of Quant) collaborates closely but is not a direct report
