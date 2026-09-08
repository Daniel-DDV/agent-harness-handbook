# Autonomy decision

Evaluate agency and orchestration separately.

## Questions

1. How quickly will we know the agent is wrong?
2. How cleanly can we undo its actions?
3. What independently proves success?
4. Does it handle sensitive data or irreversible actions?
5. Are parallel tasks isolated and independently mergeable?

## Selection

Agency level: 0 | 1 | 2 | 3

Orchestration level: single | parallel | managed-by-exception

## Required controls

- Workspace isolation:
- Permissions:
- Verification:
- Rollback:
- Human approval points:
- Time, spend, and retry budgets:

If any required control is unavailable, lower the autonomy level.