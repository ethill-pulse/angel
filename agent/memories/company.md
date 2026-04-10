# Clear Street

**Website**: clearstreet.io  
**Type**: Financial services / prime brokerage  

## Digital Asset Team

The digital asset team (formerly Pulse Prime Technologies) was acquired by Clear Street in **December 2025**. Eric Thill was CTO of Pulse Prime and is now Principal Engineer of Digital Engineering at Clear Street. The team and codebase carried over through the acquisition.

The core product is **Pulse Prime** — a multi-venue crypto/trad-fi trading platform (Rust monorepo at `repos/pulse/`). See `repos/pulse/CLAUDE.md` for full architecture.

## RenGen Relationship

**RenGen** (Suley Duyar's firm) was Pulse Prime's primary customer, and Pulse and RenGen shared the same parent company. This is why RenGen is the first and primary liquidity provider in the CS Digital trading setup — the relationship predates the Clear Street acquisition. Suley is now at CS Digital focused on big-picture business strategy.

## Tech Stack Relationship

Pulse and Clear Street are staying **separate stacks** for now. Jon Daplyn (Clear Street COO) is pushing for an eventual merger, but Eric has communicated this requires proper staffing and compliance work before it's viable. Current priority is delivery.

## Infrastructure

- Clear Street's main AWS environment is called **"fleet"** — Star Trek naming throughout
- Pulse team lives in a **child AWS account** under fleet, with its own spend tracking
- Matt Gow owns Pulse infra

### Repos

| Repo | Purpose |
|------|---------|
| `repos/kustomize` | 90+ microservice K8s configs (Kustomize + ArgoCD GitOps). EKS in ap-northeast-1 (Tokyo), ECR in us-east-2 (Ohio). 5 envs: dev, staging, mktdata, clearstreet, clearstreet-dev |
| `repos/terraform` | Terragrunt AWS infra definitions. Regions: ap-northeast-1, eu-central-1, us-east-1, us-east-2. Covers EKS, VPC, IAM, S3, Lambda, EC2, Route53, CloudFront |
| `repos/infrastructure` | Supporting scripts, Dockerfiles, Lambda functions, Packer AMI builds |
| `repos/polaris` | Clear Street Digital's algo trading platform — sequencer architecture, low-latency, connects upstream to Standalone |

### infrastructure/ Docker services

- **alfred-assistant** — Slack bot (Bedrock/Claude) that creates PRs for infra changes in kustomize/terraform repos. GitHub user: `Alfred-Pulse`
- **claude-api** — HTTP API wrapping Claude Code CLI; alfred delegates code changes to this
- **kafka-ingestor** — JSON stats → Kafka `stats` topic (Flask)
- **chronograph-ingestor** — Binary payloads → S3 under `chronograph/` prefix (Flask)
- **canalstreet-web** — (web service container)

### AWS Regions in use

- `ap-northeast-1` (Tokyo) — primary production cluster
- `us-east-2` (Ohio) — ECR, staging, infra-systems
- `eu-central-1`, `us-east-1` — infra-systems only

## Tools & Infrastructure

- **Notion**: Company knowledge base, accessible via MCP (`claude mcp add --transport http notion https://mcp.notion.com/mcp`)
- **AWS**: Cloud infrastructure (Bedrock setup documented in `notes/claude_bedrock.md`)
- **AWS SSO**: `aws sso login` to authenticate

## AI Tooling (as of Apr 8)

CS has an **AI Coding Working Group** (recurring, Eric attends). Key context:
- CS spending ~**$100k/month** on AI tools, mostly Claude via AWS Bedrock
- License rationalization underway: ChatGPT, Claude, Juni, Copilot, Codex all in use; team is rationalizing to avoid duplicate spend
- **Eric's team action item (Apr 8)**: Prepare and showcase dev workflow at Lunch & Learn presentation scheduled **Apr 24**. Eric's team is considered a good AI use case example.
- Notable CS-wide AI use case: security vulnerability fixing agent (Michal's team) scanning 5-6 languages, fixing 600 critical vulns, creating PRs autonomously
- RTK tool (Rust binary): filters command output before sending to AI — reduces tokens dramatically (988k → 142k in testing)
- Cost optimization: sub-agent architecture (cheap Sonnet first for filtering, then expensive model for analysis); per-user quota investigation underway

## Notes

- `notes/suley_token_list.md` — token tier/discount system notes (risk team, Binance listings)
- Interview notes in `notes/interviews/`
