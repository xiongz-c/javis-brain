---
name: task-delegation
description: Use when Jarvis needs to delegate work to another Lark-visible bot or remote development agent, including resolving bot mentions, sending visible Botmux handoffs, drafting outcome-oriented prompts, and reviewing delegated development through pushed Git refs and head commit hashes.
---

# Task Delegation

Use this skill when the owner asks Jarvis to hand work to another Lark-visible
bot or remote development agent.

## Botmux Visibility

A real group-visible delegation must be sent through `botmux send` with a
mention for the target bot. Internal Codex sub-agents are not a substitute for
another Lark bot.

Every `botmux send` must choose one mention mode:

- `--mention <open_id:name>` when delegating to another bot or explicitly
  notifying a person.
- `--mention-back` when the owner needs to see a substantive answer,
  confirmation request, or decision point.
- `--no-mention` for low-priority status notes.

When the CLI cannot infer the current session, pass the current
`--session-id`.

For multi-line messages, use a heredoc:

```sh
botmux send --session-id "$SESSION_ID" --mention-back <<'EOF'
message
EOF
```

## Finding Bots

Prefer direct bot context when available in the incoming prompt. If the target
bot cannot be resolved, inspect group-visible context before asking the owner:

```sh
botmux bots list
botmux history --scope chat --limit 100
botmux history --scope ambient --limit 100
```

Do not say a task was delegated unless a visible `botmux send --mention ...`
message was actually sent.

## Delegation Prompt Shape

Keep delegated prompts outcome-oriented:

- State the owner's goal.
- Provide necessary product or business context.
- Include acceptance criteria and explicit constraints from the owner.
- Specify what artifact should be returned.
- Ask for blockers instead of guessing when environment, credentials, or project
  location cannot be discovered.

Do not include local execution details unless they are part of the owner's
actual requirement.

## Remote Development Agents

When delegating coding work to a development agent running on another machine:

- Ask it to locate the relevant project in its own workspace.
- Ask it to read and follow that project's local instructions, such as its own
  `AGENTS.md`, README, scripts, tests, and contribution conventions.
- Provide the product goal and owner constraints, but do not invent branch
  names, commit style, implementation architecture, or test commands unless the
  owner explicitly requires them.
- Tell it to choose workflow, branch naming, code style, and verification steps
  from the target project's own norms.

Do not direct a remote agent to use paths from this home server as if they
existed on the remote development machine. If a local path is useful only as
context, describe it as local context and ask the remote agent to find the
equivalent project or file in its own environment.

## Review Protocol

When Jarvis reviews work produced by a remote development agent, the
authoritative artifact should be source-control state, not pasted diffs,
screenshots, or narrated changes.

Require the remote development agent to:

- Push its work to a branch or otherwise make the exact Git ref available.
- Report the repository identity, branch or ref name, and head commit hash.
- Summarize the changed scope briefly, including tests or checks it ran.

Then fetch or inspect that exact ref locally or through GitHub and review the
actual diff at the reported commit. If the remote agent amends or force-pushes,
require a new head commit hash before re-reviewing.
