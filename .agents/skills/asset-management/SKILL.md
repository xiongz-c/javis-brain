---
name: asset-management
description: Use for Vaultfolio and personal asset operations from the Botmux home workspace, including portfolio holdings, accounts, cash, positions, allocation, P/L, exposure, risk, watchlists, prior AI analysis, import or sync status, deployment health checks, and carefully scoped data fixes with backup/confirmation guardrails. For current asset facts, always use the Vaultfolio HTTP API before local development databases or source-code fixtures.
---

# Asset Management

Use this skill for Vaultfolio-related operational and portfolio work. Keep
routine inspection cheap and read-only. Prefer the application API or documented
local CLIs before direct database access or source-code changes.

## Service Discovery

This Botmux/Codex session may run in a container attached to a service network,
or in a separate CLI container that can only reach the NAS host. Do not assume
`127.0.0.1` points at another application container or at the NAS host; it
points at the current session container.

Try API bases in this order:

1. `http://api:18087`
2. `http://vaultfolio-api:18087`
3. `http://192.168.5.215:18087`
4. `http://127.0.0.1:18087`
5. `http://127.0.0.1:18088`

Confirm the selected base with `/api/health` before relying on data.

Low-cost checks:

```sh
getent hosts api vaultfolio-api vaultfolio web
curl -fsS --max-time 5 http://api:18087/api/health
curl -fsS --max-time 5 http://192.168.5.215:18087/api/health
```

## Read-Only Inspection

For personal asset facts, Vaultfolio production API is the source of truth.
Do not infer current holdings from `data/vaultfolio-dev.db`, copied NAS
backups, or fixtures unless the user explicitly asks for local/debug database
work.

Prefer API endpoints for inspection:

```sh
curl -fsS "$VAULTFOLIO_API_BASE/api/health"
curl -fsS "$VAULTFOLIO_API_BASE/api/positions"
curl -fsS "$VAULTFOLIO_API_BASE/api/market/positions"
curl -fsS "$VAULTFOLIO_API_BASE/api/dashboard"
curl -fsS "$VAULTFOLIO_API_BASE/api/cash-balances"
curl -fsS "$VAULTFOLIO_API_BASE/api/analysis/reports"
curl -fsS "$VAULTFOLIO_API_BASE/api/market/research-candidates?status=all"
curl -fsS "$VAULTFOLIO_API_BASE/api/analysis/scheduler-sync/status"
```

Common uses:

- Current holdings and cost basis: `/api/positions`
- Stored quote-enriched position state: `/api/market/positions`
- Portfolio value, allocation, cash, performance, data warnings: `/api/dashboard`
- Cash balances: `/api/cash-balances`
- Prior AI analysis and recommendations: `/api/analysis/reports`
- Current-position lookup for a symbol/name: `/api/analysis/parameter-options?source=current_positions&q=<query>`
- Watchlist/research universe context: `/api/market/research-candidates?status=all`

Vaultfolio's SQLite database is mounted inside the backend runtime and should
normally be accessed through the API rather than directly from this workspace.

## Portfolio/Risk Workflow

When the user asks about a holding, exposure, drawdown, or risk:

1. Resolve the Vaultfolio API base and confirm `/api/health`.
2. Read `/api/positions`, `/api/market/positions`, and `/api/dashboard`.
3. If historical analysis matters, read `/api/analysis/reports` and filter by
   ticker, name, task key, or category.
4. Use Vaultfolio for account, quantity, cost, stored value, portfolio weight,
   cash, and historical report facts.
5. Use public market/news sources only as supporting evidence for same-day
   price action, commodity moves, or event attribution.
6. State data freshness: Vaultfolio quote/trading date, public quote timestamp
   when used, and dashboard data warnings.
7. Do not output trade execution instructions; frame any action as manual review
   unless the user explicitly asks for an operational step and confirms risk.

## Helper

Use the bundled helper for quick read-only calls:

```sh
python3 /workspaces/.agents/skills/asset-management/scripts/vaultfolio_api.py health
python3 /workspaces/.agents/skills/asset-management/scripts/vaultfolio_api.py positions --query 000807
python3 /workspaces/.agents/skills/asset-management/scripts/vaultfolio_api.py market-positions --query 云铝
python3 /workspaces/.agents/skills/asset-management/scripts/vaultfolio_api.py dashboard-summary
python3 /workspaces/.agents/skills/asset-management/scripts/vaultfolio_api.py reports --query '000807|云铝' --compact
```

The helper only performs GET requests against read endpoints and prints JSON.

## Deployment Checks

Vaultfolio production deployment has a normal delay after `main` is updated.
The Docker publish workflow builds and promotes images first, then the NAS
auto-deployer polls and pulls the new `:main` image on its own schedule.

After a merge or push to `main`, wait 10-15 minutes before treating a stale
`/api/health` commit as a deployment problem. Verify deployment by checking
that `/api/health` reports the expected commit SHA before validating new API
fields.

## Data Changes

For data-changing operations:

1. Prefer documented application workflows.
2. If a direct database write is unavoidable, create a backup first.
3. Make the smallest targeted change.
4. Verify through the API after the change.
5. Report exactly what changed and how it was verified.

Ask for explicit confirmation immediately before asset-moving, payment,
credential, destructive, or irreversible actions.
