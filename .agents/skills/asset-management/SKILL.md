---
name: asset-management
description: Use for Vaultfolio and portfolio operations from the Botmux home workspace, including read-only asset inspection, research queues, analysis tasks, import or sync status, deployment health checks, and carefully scoped data fixes with backup/confirmation guardrails.
---

# Asset Management

Use this skill for Vaultfolio-related operational work. Keep routine inspection
cheap and read-only. Prefer the application API or documented local CLIs before
direct database access or source-code changes.

## Service Discovery

This Botmux/Codex session usually runs in a container attached to the same
Docker network as local services. Do not assume `127.0.0.1` points at another
application container or at the NAS host; it points at the current session
container.

Known reachable services:

- Vaultfolio API: `http://api:18087`
- Vaultfolio web: `http://web` inside the Docker network
- External NAS web port is usually `http://192.168.5.215:14173`

Low-cost checks:

```sh
getent hosts api web vaultfolio
curl -fsS --max-time 5 http://api:18087/api/health
```

## Read-Only Inspection

Prefer API endpoints for inspection:

```sh
curl -fsS http://api:18087/api/health
curl -fsS http://api:18087/api/market/research-candidates
curl -fsS http://api:18087/api/analysis/tasks
curl -fsS http://api:18087/api/analysis/scheduler-sync/status
```

Vaultfolio's SQLite database is mounted inside the backend runtime and should
normally be accessed through the API rather than directly from this workspace.

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
