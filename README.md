# Javis Brain

Home workspace configuration for Jarvis running through Botmux.

This repository intentionally tracks only lightweight operating instructions and
agent configuration. It does not track application source snapshots, local
databases, Home Assistant state dumps, credentials, or generated runtime data.

## Tracked

- `AGENTS.md`: workspace-level operating rules for Jarvis.
- `.agents/`: place for reusable agent configuration, skills, notes, and
  templates that are safe to version.
- `.gitignore`: guardrails for keeping local systems and personal data out of
  Git.

## Ignored

- `vaultfolio/`: deployed source snapshot and local runtime data.
- `homeassistant-optimization/`: Home Assistant semantic maps, audit outputs,
  raw states, and device/entity registry snapshots.
- Database files, archives, logs, secrets, and runtime caches.

## Operating Notes

This workspace runs on a low-power home server. Treat Git operations here as
lightweight configuration maintenance only. Do not build frontend/backend
projects or modify deployed application source trees from this repository unless
explicitly requested.

