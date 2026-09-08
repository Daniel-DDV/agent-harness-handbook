---
name: agent-setup-audit
description: Perform a read-only audit of AI coding-agent instructions, skills, hooks, permissions, and context loading. Use when a setup has duplicated rules, unknown hook behavior, stale files, excessive context, or unexplained agent drift. Do not modify the setup during the audit.
---

# Agent setup audit

1. Inventory all global instructions, repository instructions, skills, hooks, wrappers, MCP servers, and relevant CI gates.
2. Group instructions and skills by job rather than file name.
3. For every hook, record the host, version, event, matcher, executable path, timeout, exit behavior, and recovery path.
4. Verify file existence and configuration syntax without executing untrusted code.
5. Measure loaded instruction bytes against the host's current documented limit.
6. Identify overlaps, contradictions, dead references, broad matchers, expensive always-on events, and fail-open paths.
7. Label each claimed control `measured`, `enforced`, or `advisory`.
8. Produce the table in `templates/setup-audit.md`.
9. Change nothing. Wait for human approval of a separate remediation plan.