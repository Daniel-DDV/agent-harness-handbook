# Session card

## Intent

## Context

Only the files, decisions, and failed hypotheses needed for this run.

## Read budget

## Loop budget

Maximum attempts on the same failure: 2.

## Check budget

## Stop when

- Scope expansion is required.
- A dependency, migration, public API, infrastructure, auth, security, payment, or privacy change is needed.
- The same check fails twice without a materially new diagnosis.
- Production data, secrets, or destructive commands are required.
- Acceptance criteria conflict.

## Output

Return:
- Diagnosis.
- Changed files.
- Checks with commands and exit codes.
- Remaining risks.
- Stop reason, if any.