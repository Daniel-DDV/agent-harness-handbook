---
name: drift-audit
description: Compare current Git changes with an approved context contract and report scope drift before completion or handoff. Use when edits may have expanded beyond approved files, dependencies, or acceptance criteria. This skill reports drift and does not authorize scope changes.
---

# Drift audit

1. Read `.agent/context.json` and treat intent, invariants, scope, and acceptance criteria as approved boundaries.
2. Run `python scripts/context_guard.py drift`.
3. Inspect every changed and untracked file, not the agent's summary.
4. For files outside `allowed_paths`, explain whether each is necessary, accidental, generated, or unrelated.
5. Check dependency manifests, migrations, public interfaces, security-sensitive files, tests, and agent configuration explicitly.
6. Do not rewrite the approved contract to make the diff pass.
7. If expansion is justified, stop and request human approval for a revised contract.
8. Attach the drift output and final Git diff summary to the evidence bundle.

A zero exit status proves only path-level conformity, not semantic correctness.