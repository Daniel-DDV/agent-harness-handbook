# Limitations and threat model

This toolkit reduces ambiguity, externalizes compact working state, and detects mechanical scope drift. It does not make an AI agent trustworthy or autonomous by itself.

## Non-guarantees

- The toolkit cannot inspect or quantify a model's internal attention degradation.
- Scope-drift detection does not prove semantic alignment with intent.
- A `SKILL.md` file may not trigger implicitly and may be ignored.
- Hooks differ across hosts, versions, tools, and operating systems.
- A hook firing does not prove that its policy covers every write path.
- Timeouts, malformed configuration, missing executables, unsupported events, and host bugs can fail open.
- Allowed path patterns can be too broad, while strict patterns can block legitimate cross-cutting work.
- The agent can propose an invalid checkpoint; human approval remains required for scope changes.
- A passing test proves only what the test checks.
- A fresh reviewer can share the builder's model biases.
- Logs and checkpoints can expose secrets unless deliberately redacted.

## Required boundaries

Use an isolated branch, worktree, container, VM, or ephemeral CI environment appropriate to the risk. Keep production credentials out of the agent environment. Protect configuration that could execute later on the host, including Git hooks, IDE tasks, build scripts, package lifecycle scripts, and agent settings.

## Safe adoption

Start with manual checkpoints and advisory drift reports. Observe false positives and bypasses. Promote a warning to a block only after tests cover the actual host, version, event, shell, edit tools, and recovery path. Keep a documented manual recovery path outside the agent.