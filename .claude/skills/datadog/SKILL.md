---
name: datadog
description: Use when querying Datadog for Pulse Prime services — metrics, logs, monitors, dashboards, events — or doing on-call investigation ("is anything alerting", "check the error logs for X", "what was memory doing at 3am", latency/error-rate questions). Encodes credentials handling, working curl patterns, and this org's tag conventions.
---

# Datadog (Clear Street Digital)

## Credentials & invocation

`DD_API_KEY`, `DD_APPLICATION_KEY`, `DD_APPLICATION_KEY_ID` are exported in `~/.zshrc`. In Bash tool calls, `source ~/.zshrc >/dev/null 2>&1` first. **Never echo the values** — always reference `$DD_API_KEY` / `$DD_APPLICATION_KEY`.

Site: `api.datadoghq.com`.

**RTK gotcha:** the rtk hook compresses curl JSON responses into a type schema, which destroys the actual data. Always write responses to a file with `-o /tmp/dd.json`, then read values with `jq '...' /tmp/dd.json` in a separate command (or use `rtk proxy curl ...` for raw output).

## Tag conventions

- `kube_cluster_name:` **the Datadog tag value is NOT the kubectl context name** — it's the `cs-digital-*` form below. Querying with the kubectl context name returns `status:ok` with zero series (silent empty), which looks like "no data" but is really a wrong tag. Mapping (kubectl context → `kube_cluster_name` tag):
  - `dev-prime-tokyo` → `cs-digital-tokyo-dev-rengen`
  - `staging-prime-tokyo` → `cs-digital-tokyo-staging-rengen`
  - `mktdata-prime-tokyo` → `cs-digital-tokyo-mktdata-rengen`
  - `clearstreet-dev-prime-tokyo` → `cs-digital-tokyo-dev-clearstreet`
  - `clearstreet-prime-tokyo` (prod) → `cs-digital-tokyo-prod-clearstreet`
  - `infra-systems` → `cs-digital-infra-systems`
  - If unsure, discover it: query your metric `by {kube_cluster_name}` with no cluster filter and read the scopes back.
- Node-level host metrics (`system.load.1`, `system.cpu.*`, `system.io.*`) tag by `host` = the node's private DNS (`ip-10-…-….<region>.compute.internal`); group `by {host}` (the `host:<dns>` filter form sometimes returns nothing — `by {host}` then grep is more reliable). `system.load.1` is the trustworthy node-saturation signal when a node's kubelet/agent is starved (per-pod `kubernetes.cpu.usage.total` undercounts then) — see node-resilience skill.
- `kube_namespace:` see the `k8s-debug` skill for the namespace map (`publicapi`, `datapipe`, `questdb`, ...)
- `service:` matches the app name (e.g. `account-server`, `questdb-ts-publisher`)
- `team:digital` — all of the Digital team's dashboards carry this tag; full list at app.datadoghq.com/dashboard/lists (see Notion: "Datadog Dashboards for Pulse Apps")

## Working query patterns

Metrics (v1 timeseries query — epoch seconds, macOS `date -v` syntax):

```bash
source ~/.zshrc >/dev/null 2>&1
curl -s -G "https://api.datadoghq.com/api/v1/query" \
  -H "DD-API-KEY: $DD_API_KEY" -H "DD-APPLICATION-KEY: $DD_APPLICATION_KEY" \
  --data-urlencode "from=$(date -v-1H +%s)" --data-urlencode "to=$(date +%s)" \
  --data-urlencode "query=avg:kubernetes.memory.usage{kube_cluster_name:staging-prime-tokyo,kube_namespace:publicapi} by {pod_name}" \
  -o /tmp/dd.json
jq -r '.series[] | "\(.scope) last=\(.pointlist[-1][1])"' /tmp/dd.json
```

Logs search (v2, POST):

```bash
curl -s -X POST "https://api.datadoghq.com/api/v2/logs/events/search" \
  -H "DD-API-KEY: $DD_API_KEY" -H "DD-APPLICATION-KEY: $DD_APPLICATION_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filter":{"query":"service:account-server kube_cluster_name:staging-prime-tokyo status:error","from":"now-1h","to":"now"},"page":{"limit":25},"sort":"-timestamp"}' \
  -o /tmp/dd_logs.json
jq -r '.data[].attributes | "\(.timestamp) \(.message[0:160])"' /tmp/dd_logs.json
```

Monitors — what's alerting right now:

```bash
curl -s -G "https://api.datadoghq.com/api/v1/monitor" \
  -H "DD-API-KEY: $DD_API_KEY" -H "DD-APPLICATION-KEY: $DD_APPLICATION_KEY" \
  --data-urlencode "group_states=alert" -o /tmp/dd_mon.json
jq -r '.[] | "\(.id) [\(.overall_state)] \(.name)"' /tmp/dd_mon.json
```

Monitor search by name/tag: `GET /api/v1/monitor/search?query=<terms>`. Events: `GET /api/v1/events?start=<epoch>&end=<epoch>`.

## App-emitted metrics worth knowing

- Pulse apps publish stats via `kafka-influx-stats-publisher`; QuestDB write/read latency histograms appear as `questdb.execute_write`, `questdb.execute_read`, `questdb.last_offset`.
- For Kafka consumer lag and pipeline throughput, combine with the `data-pipeline-debug` skill.

## When a session teaches something new

Found a metric name, log facet, or query that took effort to discover? Append it here so next time is one command.
- `kubernetes.containers.restarts` (and most k8s state metrics) tag the container as `kube_container_name`, NOT `container` — grouping by `container` returns zero series, which makes a monitor sit in permanent "No Data" without erroring (bit the App/Infra Pod Restarting monitor pair for months). Sanity-check any monitor stuck in No Data by re-running its query grouped by each tag.
- Pod-crash alert routing (2026-07): four monitors, all routed by QUERY-LEVEL namespace filters (never message-template conditionals - `{{#is_match}}` is SUBSTRING match, not regex; an anchored regex alternation silently never matches and everything falls to the else branch, which misrouted infra alerts to eng for a day). `Kubernetes App Pod Restarting` (264189250) + `[CS-DIGITAL] Pod CrashLoopBackOff` (245939913) -> #digital-eng-alerts with `!kube_namespace:` blocklists; `Kubernetes Infra/System Pod Restarting` (264189251) + `[CS-DIGITAL] Infra Pod CrashLoopBackOff` (304323135) -> #digital-infra-alerts with `kube_namespace IN (...)` allowlists. Keep the namespace sets in sync across all four when adding infra namespaces.
- Slack handle gotcha: `@slack-Clear_Street-digital-infra` and `@slack-Clear_Street-digital-infra-alerts` are DIFFERENT channels - the team watches #digital-infra-alerts (the `-alerts` handle). Verify the handle suffix when routing.
- Dev/prod Slack split (2026-07-11): all five pod-crash/PVC monitors route by `{{#is_match "kube_cluster_name.name" "-dev-"}}` substring conditionals - dev clusters post to #digital-eng-alerts-dev / #digital-infra-alerts-dev, everything else to the prod channels. Single-substring is_match is RELIABLE (unlike regex alternations, which silently never match). The PVC monitor's PD conditional uses nested negations (`{{^is_match ... "-dev-"}}{{^is_match ... "infra-systems"}}`) for the same reason - the original anchored-regex version never matched and PVC criticals silently didn't page for ~a day.
- Pulse log status mapping (2026-07-14): pulse apps log plain text (`<rfc3339ns>Z [LEVEL] ("thread" file:line): msg`, from `pulse/libs/core/crates/sys/src/logger.rs`), so log `status` defaulted to info until pipeline `Pulse Prime rust apps` (id `OxvufK_9TTCa9vJ_n8GCSA`, filter `kube_cluster_name:cs-digital-*`) was added: grok-parses `level` (+ `logger.thread`, `msg` attrs) then a status remapper. Non-matching lines (multiline continuations, other formats) stay info by design; pipelines apply at INGEST only, so historical logs keep their old status. Edit via `PUT /api/v1/logs/config/pipelines/<id>` if the log format changes.
- kafka_consumer cluster check (DIG-149, staging+clearstreet): configured via DatadogAgent `override.clusterAgent.extraConfd`, targets kafka-cluster.confluent-cluster.svc:9071 (plaintext in-cluster). THREE gotchas cost a day: (1) `max_partition_contexts` is an **init_config** option - instance-level placement (and made-up keys like max_returned_metrics) are silently ignored; (2) when the context cap trips, the check SKIPS HIGHWATER COLLECTION entirely, so `kafka.consumer_lag` never exists while `kafka.consumer_offset` flows fine - lag missing but offsets present = cap tripped (staging needs ~4k contexts, cap set 8000); (3) the operator does NOT restart the cluster-agent on extraConfd changes - `rollout restart deploy datadog-cluster-agent` after every merge. Money-path monitors exclude `topic:refdata` (idle consumers carry stale committed offsets, e.g. talos-fills-publisher shows 24k fake lag there). `change()`-based monitors on fresh metrics need `new_group_delay` or every new cluster/topic misfires on first appearance. Dashboard: /dashboard/by8-zh4-urt.
