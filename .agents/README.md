# Agent Configuration

This directory is reserved for Jarvis-specific configuration that is safe to
version.

Suggested structure:

- `skills/`: local skill instructions or references.
- `assets/`: stable visual assets such as the Javis Bear avatar.
- `identity.md`: the agent's local Git author and avatar notes.
- `prompts/`: reusable prompt fragments.
- `notes/`: durable operational notes that do not contain secrets.

Do not store API keys, access tokens, private SSH keys, Home Assistant raw state
dumps, local databases, or personal account data here.
