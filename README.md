# Agent Harness Handbook

An evidence-first operating handbook and working toolkit for reducing context rot and implementation drift in AI coding agents.

Created and maintained by Daniel (@Daniel-DDV).

## Status

Version 1.1.0. The repository includes a nine-part handbook, reusable templates, four portable Agent Skills, a tested context checkpoint and scope-drift guard, repository validation, and CI.

## Context rot and drift

The core runtime is `scripts/context_guard.py`. It creates a compact task contract outside chat, preserves progress between sessions, compares the Git working tree with approved paths, and stops repeated attempts at the same failure.

```bash
python scripts/context_guard.py init \
  --intent "Fix expired-session redirects" \
  --allow "src/auth" \
  --allow "tests/test_auth*.py" \
  --invariant "Existing authorization errors remain unchanged" \
  --acceptance "Expired sessions redirect to login" \
  --verification "pytest tests/test_auth.py"

python scripts/context_guard.py checkpoint \
  --summary "Reproduced the redirect failure" \
  --next-action "Patch the session-expiry branch"

python scripts/context_guard.py drift
python scripts/context_guard.py failure --signature "test_auth_redirect:AssertionError"
python scripts/context_guard.py status
```

The state is stored in `.agent/context.json`. Commit it when the task contract should be shared; keep it local when it contains sensitive task details.

## What is enforced

- `drift` returns a failing exit status when changed or untracked files fall outside `allowed_paths`.
- `failure` returns exit code 2 when the same normalized failure reaches the configured attempt limit.
- Repository CI validates required files, skill metadata, links, and unit tests.

Semantic intent drift cannot be proven from file paths alone. The evidence bundle and independent review remain necessary.

## Quick start

1. Complete `templates/work-definition.md`.
2. Initialize `.agent/context.json` with the command above.
3. Use `templates/session-card.md` for delegated runs.
4. Refresh the checkpoint before compaction, handoff, or a new session.
5. Run `python scripts/context_guard.py drift` before completion.
6. Require `templates/evidence-bundle.md` before accepting the result.
7. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.

## Contents

- `docs/HANDBOOK.md` — complete operating model.
- `docs/CONTEXT_GUARD.md` — context-rot and drift workflow.
- `docs/LIMITATIONS.md` — explicit non-guarantees and threat model.
- `docs/SOURCES.md` — sources and evidence labels.
- `templates/` — work, session, state, evidence, autonomy, and audit forms.
- `skills/` — focused Agent Skills.
- `scripts/context_guard.py` — context checkpoint and drift CLI.
- `scripts/validate.py` — repository validator.

## Safety

This is not a sandbox or universal security boundary. Review executable code before use. Host hooks differ and can fail open; this repository does not silently install them.

## License

MIT License. Copyright 2026 Daniel (@Daniel-DDV).