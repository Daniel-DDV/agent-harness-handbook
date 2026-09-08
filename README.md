# Agent Harness Handbook

An evidence-first operating handbook and reusable toolkit for reliable AI coding agents.

Created and maintained by Daniel (@Daniel-DDV).

## Status

Version 1.0.0. The handbook, templates, two portable Agent Skills, validation script, CI workflow, contribution guide, security policy, and limitations are included.

## What this is

This repository helps teams define bounded work, control permissions and budgets, preserve useful context, collect evidence, choose an autonomy level, run independent review loops, learn from failures, and audit their agent setup.

It is deliberately not a universal enforcement layer. Skills are advisory. Hook behavior differs by host and can fail open. Security boundaries belong in sandboxes, permissions, CI, and branch protection.

## Quick start

1. Copy `templates/work-definition.md` into your project and complete it before implementation.
2. Copy `templates/session-card.md` into the prompt for any delegated run.
3. Select an autonomy level using `templates/autonomy-decision.md`.
4. Require `templates/evidence-bundle.md` before accepting the result.
5. Run `python scripts/validate.py` after changing this repository.

Portable skills live in `skills/`. Install them in a directory supported by your agent host, or invoke their procedures manually.

## Contents

- `docs/HANDBOOK.md` — the complete nine-part operating model.
- `docs/LIMITATIONS.md` — explicit non-guarantees and failure modes.
- `docs/SOURCES.md` — primary and clearly labelled secondary sources.
- `templates/` — ready-to-use work, session, evidence, autonomy, and audit forms.
- `skills/` — focused Agent Skills for run contracts and setup audits.
- `scripts/validate.py` — dependency-free repository validation.

## Core rule

Never accept a model's confidence, summary, or self-assessment as evidence. Prefer executable checks and independently inspectable artifacts.

## License

MIT License. Copyright 2026 Daniel (@Daniel-DDV).