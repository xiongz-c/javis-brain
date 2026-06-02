# Botmux Home Workspace

This workspace runs on a low-power home server. Treat it primarily as an
operations, research, and data-query environment, not as a development machine.

Code repositories under `/workspaces` may be read to understand local systems,
APIs, schemas, and data flows, but do not edit repository code, run frontend or
backend builds, compile large projects, reinstall dependencies, or start heavy
development servers unless the user explicitly asks for that specific coding or
build action.

For application data tasks, prefer existing low-cost interfaces, database reads,
small targeted database writes after backup, or documented local CLIs. Avoid
changing source code as the default way to operate local systems.

Home Assistant is reachable from this container at:

```sh
http://homeassistant:8123
```

Use `HOME_ASSISTANT_URL` when available. Home Assistant API calls require a long-lived access token supplied by the user.

Read-only state check:

```sh
curl -H "Authorization: Bearer $HOME_ASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  "$HOME_ASSISTANT_URL/api/states"
```

Low-risk controls such as lights, air conditioners, and ordinary plugs may be executed when the user explicitly asks for that action.

Door locks, security/alarm devices, gas-related devices, heaters, high-power appliances, and any ambiguous or safety-sensitive action require explicit user confirmation immediately before the API call.

When interpreting Home Assistant entities for the user's home, prefer the curated semantic map at:

```sh
/workspaces/homeassistant-optimization/home_semantics_core.yaml
```

Use it to distinguish daily control entities from auxiliary configuration entities, indicator lights, and switch-backed non-smart lights. The full generated audit is in `/workspaces/homeassistant-optimization/entity_audit.md` and `/workspaces/homeassistant-optimization/entity_audit.json`.
