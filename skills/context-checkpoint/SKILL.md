---
name: context-checkpoint
description: Preserve a compact, durable task state before context compaction, handoff, session restart, or after a disproven hypothesis. Use during non-trivial coding work when conversation history is becoming long or another agent will continue the task.
---

# Context checkpoint

1. Read `.agent/context.json`; if it does not exist, initialize it with `python scripts/context_guard.py init` after the human approves intent and scope.
2. Read only the files required for `next_action` before loading broad history.
3. Before compaction, handoff, or ending the session, run `checkpoint` with:
   - A factual progress summary.
   - Exactly one next action.
   - Any newly disproven hypothesis.
4. Preserve raw logs outside the checkpoint and reference their path; do not paste large logs into state.
5. Never silently change intent, invariants, allowed paths, acceptance criteria, or verification.
6. If those fields must change, stop and request human approval.
7. In a fresh session, restate the compact contract before editing.