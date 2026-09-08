# Limitations and threat model

This toolkit reduces ambiguity and makes review easier. It does not make an AI agent trustworthy or autonomous by itself.

## Non-guarantees

- A `SKILL.md` file may not trigger implicitly and may be ignored.
- Hooks differ across hosts, versions, tools, and operating systems.
- A hook firing does not prove that its policy covers every write path.
- Timeouts, malformed configuration, missing executables, unsupported events, and host bugs can fail open.
- Scope limits may block legitimate cross-cutting fixes or incentivize duplication.
- A passing test proves only what the test checks.
- A fresh reviewer can share the builder's model biases.
- Logs and traces can expose secrets unless deliberately redacted.

## Required boundaries

Use an isolated branch, worktree, container, VM, or ephemeral CI environment appropriate to the risk. Keep production credentials out of the agent environment. Protect configuration that could execute later on the host, including Git hooks, IDE tasks, build scripts, package lifecycle scripts, and agent settings.

## Safe adoption

Start advisory. Observe false positives and bypasses. Promote a warning to a block only after tests cover the actual host, version, event, shell, edit tools, and recovery path. Keep a documented manual recovery path outside the agent.