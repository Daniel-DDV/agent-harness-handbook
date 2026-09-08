# Handbook

## 1. Work definition

Define work before an agent builds. Record the intended outcome, invariants, in-scope and out-of-scope work, observable acceptance criteria, edge cases, stop rules, and required evidence. If the work cannot fit into one reviewable change, split it.

Use behavior rather than implementation detail. A useful boundary is as important as the goal: state what must not change. Large tasks should begin with a short interview and end with an independently executable verification step.

## 2. Context engineering

Context is finite and degrades before the advertised window is full. Keep persistent instructions limited to facts that are both non-obvious from the repository and relevant to nearly every task. Put task-specific state in the work definition.

Use progressive disclosure: load names and descriptions first, procedures only when selected, and references only when needed. Prefer isolated, fresh-context workers over repeatedly compressing a polluted session. Store each durable decision at its natural owner: product decision in a spec, architecture decision in an ADR, repository rule in AGENTS.md, and operating lesson in a runbook.

## 3. Harness and permissions

Classify actions as allowed, ask first, or never. Allow bounded local edits and checks. Ask before dependencies, migrations, public API changes, security-sensitive work, deployment, or destructive commands. Never expose production data or secrets, weaken tests, silently alter acceptance criteria, or disable security checks.

Prompt text is not a security boundary. Use isolated and recoverable environments, least privilege, branch protection, CI, and reviewed configuration. Skills do not grant permissions. Hooks are host-specific and may fail open; validate their actual event and exit behavior.

## 4. Execution budgets

Every delegated run needs a read budget, loop budget, check budget, and output budget. Stop after two attempts at the same failure unless a materially new diagnosis exists. Permit at most one scope-expansion request before rewriting the work definition.

Track task type, model, elapsed time, tool calls, retries, checks, changed files, stop reason, and outcome. Optimize the environment rather than rewarding raw activity.

## 5. Verification and evidence

Output is not evidence. Require an evidence bundle containing intent, approach, changed files, exact commands, exit codes, CI or artifact links, commit identifier, known risks, review focus, and out-of-scope items.

Escalate verification from a prompt-level check to an executable goal, deterministic gate, and fresh-context reviewer as risk rises. A reviewer should report only defects affecting correctness or stated requirements; unrestricted gap hunting encourages overengineering.

Use only three maturity labels:

- `measured`: a reproducible task produced recorded results.
- `enforced`: a deterministic mechanism was tested on the relevant path.
- `advisory`: written guidance without proven enforcement.

## 6. Autonomy

Select autonomy from risk, reversibility, and available evidence—not prestige or task complexity.

- Level 0: suggestions only.
- Level 1: supervised actions.
- Level 2: bounded task delegation with review.
- Level 3: goal-driven looping against measurable criteria and budgets.
- Level 4: parallel delegation with isolated workspaces and ownership.
- Level 5: managed by exception with observability and independent verification.

Treat agency and orchestration as separate dimensions even when using this shorthand. Higher autonomy requires faster detection, cleaner rollback, and stronger proof.

## 7. Review loops

Use a gauntlet only when quality is repeatedly and cheaply measurable. A valid reference bar must be named, retrievable, and comparable. Give each unit to a builder and its artifact—not the builder's summary—to a fresh-context critic. The critic identifies the single largest requirement-relevant gap, then the builder revises.

Stop when the bar is met, no material gap remains, marginal improvement costs more than it returns, a budget is exhausted, or a human stops the run. Without tests, screenshots, benchmarks, or references, a critic is a second opinion—not an independent verifier.

## 8. Improvement loop

After a correction, capture the failure pattern, root cause, prevention rule, and destination. Promote repeated controls to the narrowest durable mechanism: deterministic control to a script or hook, situational procedure to a skill, and short universal fact to AGENTS.md.

After two failed corrections without a new diagnosis, stop the session. Start a clean session with a prompt that includes the evidence and failed hypotheses. Compare harness changes on a fixed reference task before declaring improvement.

## 9. Setup audit

Every instruction needs one home: global instruction, repository instruction, skill, or deterministic mechanism. Audit by job rather than file name. Identify overlap, dead paths, controls that never trigger, broad matchers, collisions, and expensive events.

Separate audit from modification. Produce the table first; change nothing until a human reviews it. Apply a pruning test to every persistent rule: if removing it does not cause a demonstrated failure, remove or relocate it.

## Operating sequence

1. Establish one reference task and baseline.
2. Audit existing hooks and permissions read-only.
3. Prune persistent context and overlapping skills.
4. Introduce the work definition and session card.
5. Require an evidence bundle.
6. Add deterministic controls only for repeated, measurable failures.
7. Increase autonomy only after rollback and verification are proven.
8. Re-run the reference task and record the delta.