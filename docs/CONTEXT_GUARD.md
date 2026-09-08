# Context checkpoint and drift guard

## Purpose

Context rot is declining reliability as a session accumulates tokens, stale assumptions, failed approaches, and irrelevant tool output. Drift is divergence between approved intent and actual work. They overlap but are not identical.

This repository addresses them with a compact external state artifact and deterministic checks around the Git working tree. It does not claim to inspect a model's internal attention.

## State contract

`.agent/context.json` records:

- Intent and invariants.
- Allowed paths and explicit exclusions.
- Acceptance criteria and verification commands.
- Current progress and exactly one next action.
- Failed hypotheses.
- A normalized failure signature and consecutive-attempt count.
- Creation and update timestamps.

The compact checkpoint is the handoff unit. A fresh session should read it before reading broad repository documentation.

## Workflow

1. A human approves the work definition.
2. Run `context_guard.py init` with the approved boundaries.
3. The agent reads the checkpoint and only the files needed for the next action.
4. Before compaction, handoff, or session restart, run `checkpoint`.
5. Record repeat failures with a stable signature using `failure`.
6. When the configured limit is reached, stop editing and begin a fresh diagnostic session.
7. Run `drift` before completion and attach its output to the evidence bundle.
8. Independently verify acceptance criteria.

## Drift semantics

The command detects mechanical scope drift: changed or untracked files outside the approved path patterns. It intentionally does not block writes and does not claim to understand semantic intent.

A change can remain inside allowed paths and still violate the goal. Conversely, a legitimate fix can require an unlisted path. Treat a non-zero drift result as a request to inspect and amend the approved contract—not permission for the agent to rewrite its own scope.

## Context hygiene

Checkpoint when any of these occurs:

- The session is about to compact.
- A worker hands off to another worker.
- A hypothesis is disproven.
- The next action changes.
- The user corrects the agent.
- The session ends.

Do not paste full logs into the checkpoint. Preserve raw evidence elsewhere and record a path or artifact identifier.

## Hook integration

The CLI is deliberately host-neutral and can be called manually, from CI, or from a reviewed host hook. Host adapters are not included until they are tested against a named host and version. Never describe an untested hook as enforcement.