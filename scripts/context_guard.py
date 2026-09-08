from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import subprocess
import sys
from pathlib import Path

STATE_PATH = Path(".agent/context.json")


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def load_state() -> dict:
    if not STATE_PATH.is_file():
        raise SystemExit("No .agent/context.json. Run: python scripts/context_guard.py init ...")
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = now_utc()
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def path_allowed(path: str, patterns: list[str]) -> bool:
    value = path.replace("\\", "/").lstrip("./")
    for pattern in patterns:
        normalized = pattern.replace("\\", "/").lstrip("./").rstrip("/")
        if fnmatch.fnmatch(value, normalized) or value == normalized or value.startswith(normalized + "/"):
            return True
    return False


def changed_files() -> list[str]:
    commands = [
        ["git", "-c", "core.quotepath=false", "diff", "--name-only", "HEAD"],
        ["git", "-c", "core.quotepath=false", "ls-files", "--others", "--exclude-standard"],
    ]
    found: set[str] = set()
    for command in commands:
        result = subprocess.run(command, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(result.stderr.strip() or "Unable to inspect Git working tree")
        found.update(line.strip() for line in result.stdout.splitlines() if line.strip())
    return sorted(found)


def command_init(args: argparse.Namespace) -> int:
    if STATE_PATH.exists() and not args.force:
        raise SystemExit("Context file already exists. Use --force only after human approval.")
    state = {
        "schema_version": 1,
        "intent": args.intent,
        "invariants": args.invariant,
        "allowed_paths": args.allow,
        "out_of_scope": args.out_of_scope,
        "acceptance_criteria": args.acceptance,
        "verification": args.verification,
        "max_same_failure_attempts": args.max_attempts,
        "same_failure_attempts": 0,
        "last_failure_signature": None,
        "failed_hypotheses": [],
        "progress_summary": "Not started",
        "next_action": "Inspect the relevant files and restate the contract",
        "created_at": now_utc(),
    }
    save_state(state)
    print(STATE_PATH)
    return 0


def command_checkpoint(args: argparse.Namespace) -> int:
    state = load_state()
    state["progress_summary"] = args.summary
    state["next_action"] = args.next_action
    if args.failed_hypothesis:
        state["failed_hypotheses"].append(args.failed_hypothesis)
    save_state(state)
    print(json.dumps(state, indent=2, ensure_ascii=False))
    return 0


def command_failure(args: argparse.Namespace) -> int:
    state = load_state()
    if state.get("last_failure_signature") == args.signature:
        state["same_failure_attempts"] = int(state.get("same_failure_attempts", 0)) + 1
    else:
        state["last_failure_signature"] = args.signature
        state["same_failure_attempts"] = 1
    if args.hypothesis:
        state["failed_hypotheses"].append(args.hypothesis)
    save_state(state)
    attempts = state["same_failure_attempts"]
    limit = int(state.get("max_same_failure_attempts", 2))
    print(json.dumps({"signature": args.signature, "attempts": attempts, "limit": limit}))
    if attempts >= limit:
        print("STOP: repeated failure limit reached. Start a fresh diagnostic session.", file=sys.stderr)
        return 2
    return 0


def command_drift(_: argparse.Namespace) -> int:
    state = load_state()
    changed = changed_files()
    outside = [path for path in changed if not path_allowed(path, state.get("allowed_paths", []))]
    report = {
        "intent": state.get("intent"),
        "changed_files": changed,
        "outside_allowed_paths": outside,
        "status": "drift-detected" if outside else "within-declared-scope",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if outside else 0


def command_status(_: argparse.Namespace) -> int:
    print(json.dumps(load_state(), indent=2, ensure_ascii=False))
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Context checkpoint and scope-drift guard")
    sub = root.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="Create the approved context contract")
    init.add_argument("--intent", required=True)
    init.add_argument("--allow", action="append", required=True, help="Allowed path or glob; repeatable")
    init.add_argument("--invariant", action="append", default=[])
    init.add_argument("--out-of-scope", action="append", default=[])
    init.add_argument("--acceptance", action="append", default=[])
    init.add_argument("--verification", action="append", default=[])
    init.add_argument("--max-attempts", type=int, default=2)
    init.add_argument("--force", action="store_true")
    init.set_defaults(run=command_init)

    checkpoint = sub.add_parser("checkpoint", help="Refresh compact working state")
    checkpoint.add_argument("--summary", required=True)
    checkpoint.add_argument("--next-action", required=True)
    checkpoint.add_argument("--failed-hypothesis")
    checkpoint.set_defaults(run=command_checkpoint)

    failure = sub.add_parser("failure", help="Record a normalized failure signature")
    failure.add_argument("--signature", required=True)
    failure.add_argument("--hypothesis")
    failure.set_defaults(run=command_failure)

    drift = sub.add_parser("drift", help="Compare Git changes with allowed paths")
    drift.set_defaults(run=command_drift)

    status = sub.add_parser("status", help="Print the compact context checkpoint")
    status.set_defaults(run=command_status)
    return root


def main() -> int:
    args = parser().parse_args()
    return args.run(args)


if __name__ == "__main__":
    raise SystemExit(main())
