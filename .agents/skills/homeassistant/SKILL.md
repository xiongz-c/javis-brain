---
name: homeassistant
description: Operate and diagnose the user's Home Assistant setup from this Botmux home workspace. Use when Codex needs to inspect HA entities, read states/history/logbook, reason about home device semantics, troubleshoot automations or device behavior, or perform explicitly requested low-risk controls such as lights, air conditioners, ordinary plugs, and non-sensitive settings with confirmation guardrails for locks, security, gas, heaters, high-power appliances, and ambiguous safety-sensitive actions.
---

# Home Assistant

## Quick Start

Use `HOME_ASSISTANT_URL` when set; otherwise use `http://homeassistant:8123`.
API calls require `HOME_ASSISTANT_TOKEN`.

Read state without changing anything:

```sh
curl -H "Authorization: Bearer $HOME_ASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  "$HOME_ASSISTANT_URL/api/states"
```

Prefer Python or `curl` API calls over Home Assistant UI assumptions. Never print
tokens or secrets.

## Safety Rules

- Execute low-risk controls only when the user explicitly asks for that action:
  lights, air conditioners, ordinary plugs, and ordinary non-safety settings.
- Require explicit immediate confirmation before controlling or changing door
  locks, alarms/security devices, gas-related devices, heaters, high-power
  appliances, cooking devices, destructive automations, or ambiguous actions.
- For troubleshooting, start read-only: current states, semantic map, history,
  logbook, and error log.
- After any write, verify final state with `/api/states/<entity_id>` and report
  the exact entities changed.

## Home Reference Files

Use the private reference directory at `/workspaces/homeassistant-optimization`
before interpreting home entities:

- `home_semantics_core.yaml`: preferred curated map for daily-control entities,
  auxiliary settings, switch-backed lights, and diagnostic entities.
- `entity_audit.md` and `entity_audit.json`: generated audit for broader entity
  discovery and classification.
- `raw_states.json`, `raw_entity_registry.json`, `raw_device_registry.json`,
  `raw_area_registry.json`: historical snapshots for deeper debugging.

Do not assume every HA entity is user-facing. Prefer entities marked daily
control in the semantic map. Treat diagnostic lights and auxiliary switches as
implementation details unless the task specifically targets them.

## Common Workflows

### Entity Discovery

1. Search `home_semantics_core.yaml` for the room/device name.
2. If not found, search `entity_audit.md` or current `/api/states`.
3. Distinguish group lights from individual diagnostic lights.
4. Confirm current state before proposing or executing control.

### Logs and Automation Diagnosis

1. Identify relevant entity ids.
2. Query `/api/history/period/<start>` for state transitions.
3. Query `/api/logbook/<start>` with `entity=<entity_id>` for human-readable
   events.
4. Inspect `context.id`, `parent_id`, and `user_id` when history includes them:
   an empty context often indicates device/integration state reporting rather
   than a Home Assistant service call.
5. Search automation/script/scene states by friendly name and `last_triggered`.

### Control Execution

Use service endpoints:

```sh
curl -X POST \
  -H "Authorization: Bearer $HOME_ASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id":"light.example"}' \
  "$HOME_ASSISTANT_URL/api/services/light/turn_off"
```

Then verify:

```sh
curl -H "Authorization: Bearer $HOME_ASSISTANT_TOKEN" \
  "$HOME_ASSISTANT_URL/api/states/light.example"
```

