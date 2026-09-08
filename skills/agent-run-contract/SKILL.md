---
name: agent-run-contract
description: Create a bounded, verifiable run contract before an AI coding agent implements a non-trivial change. Use when scope, permissions, stop conditions, budgets, or acceptance evidence are unclear. Do not use for simple explanations or read-only questions.
---

# Agent run contract

1. Read `templates/work-definition.md` and `templates/session-card.md` from this repository.
2. Restate the requested outcome and invariants without proposing implementation.
3. Identify unresolved assumptions and ask only questions that block measurable acceptance criteria.
4. Fill the work definition with in-scope and out-of-scope work, permissions, budgets, stop rules, and verification.
5. Select the lowest autonomy level that fits the available rollback and evidence.
6. Do not implement until the contract is approved.
7. During execution, stop after two attempts at the same failure unless a materially new diagnosis exists.
8. Finish with `templates/evidence-bundle.md`.

Never describe advisory text as enforcement.