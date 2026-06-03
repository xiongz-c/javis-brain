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

## Local service discovery

This Botmux/Codex session usually runs in a container attached to the same
Docker network as local services. Do not assume `127.0.0.1` points at another
application container or at the NAS host; it points at the current session
container. Prefer Docker service names and verify them with `getent hosts` or a
small health request before deciding a system is down.

Known reachable services from this workspace:

- Vaultfolio API: `http://api:18087`
- Vaultfolio web: `http://web` inside the Docker network; externally the NAS
  web port is usually `http://192.168.5.215:14173`
- Home Assistant: `http://homeassistant:8123`

Useful low-cost checks:

```sh
getent hosts api web homeassistant vaultfolio
curl -fsS --max-time 5 http://api:18087/api/health
curl -fsS --max-time 5 http://homeassistant:8123/api/
```

Vaultfolio's SQLite database is mounted inside the Vaultfolio backend runtime
and should normally be accessed through the API rather than directly from this
workspace. For read-only Vaultfolio inspection, prefer API endpoints such as:

```sh
curl -fsS http://api:18087/api/health
curl -fsS http://api:18087/api/market/research-candidates
curl -fsS http://api:18087/api/analysis/tasks
curl -fsS http://api:18087/api/analysis/scheduler-sync/status
```

## Botmux / Lark delegation notes

When a user asks Jarvis to delegate work to another Lark bot in the same group,
do not treat Codex internal sub-agents as that bot. A real group-visible
delegation must be sent through `botmux send --mention <id:name>`.

Prefer direct Lark group lookup before scanning history. If the current bot has
usable Lark app credentials and `im:chat.members:read`, call the chat detail /
members APIs for the target `chat_id` first. Chat detail may expose `bot_count`
even when the members endpoint only returns human users. If the API confirms
bots are present but does not expose their mentionable IDs, then use broader
group context as a fallback:

```sh
botmux history --scope chat --limit 100
botmux history --scope ambient --limit 100
```

`botmux bots list` may only show bots visible to the current session/thread or
this machine's configured bot context. Other group bots may run on different
machines. Use history fallback only to find prior bot messages, app sender IDs,
or mention text when direct member lookup is insufficient. If the target bot
still cannot be resolved, ask the user for the bot's open_id or ask them to
mention the bot once in the current thread. Do not say a task was delegated to
another Lark bot unless a visible `botmux send --mention ...` message was
actually sent.

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
