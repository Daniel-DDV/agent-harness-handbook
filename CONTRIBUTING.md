# Contributing

Thank you for improving the Agent Harness Handbook.

## Principles

- Prefer primary sources and link them directly.
- Mark vendor claims and unresolved evidence explicitly.
- Keep additions focused on a demonstrated failure mode.
- Do not add a skill when a template, test, or short instruction is sufficient.
- Do not claim cross-host compatibility without testing each named host and version.

## Process

1. Open an issue describing the failure mode and expected evidence.
2. Make the smallest coherent change.
3. Run `python scripts/validate.py`.
4. Include an evidence bundle in the pull request.
5. Update `CHANGELOG.md` for user-visible changes.

By contributing, you agree that your contribution is licensed under the MIT License.