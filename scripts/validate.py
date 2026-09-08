from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "AGENTS.md",
    "CITATION.cff",
    "docs/HANDBOOK.md",
    "docs/CONTEXT_GUARD.md",
    "docs/LIMITATIONS.md",
    "docs/SOURCES.md",
    "templates/work-definition.md",
    "templates/session-card.md",
    "templates/context-state.example.json",
    "templates/evidence-bundle.md",
    "templates/autonomy-decision.md",
    "templates/setup-audit.md",
    "skills/agent-run-contract/SKILL.md",
    "skills/agent-setup-audit/SKILL.md",
    "skills/context-checkpoint/SKILL.md",
    "skills/drift-audit/SKILL.md",
    "scripts/context_guard.py",
    "tests/test_context_guard.py",
]


def fail(message):
    print(f"ERROR: {message}")
    return 1


errors = 0
for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file():
        errors += fail(f"missing {relative}")
    elif not path.read_text(encoding="utf-8").strip():
        errors += fail(f"empty {relative}")

for path in ROOT.rglob("SKILL.md"):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors += fail(f"missing frontmatter in {path.relative_to(ROOT)}")
    if not re.search(r"^name:\s*[-a-z0-9]+\s*$", text, re.MULTILINE):
        errors += fail(f"invalid or missing skill name in {path.relative_to(ROOT)}")
    if not re.search(r"^description:\s*\S.+$", text, re.MULTILINE):
        errors += fail(f"missing skill description in {path.relative_to(ROOT)}")

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)", text):
        clean = target.split("#", 1)[0]
        if clean and not (path.parent / clean).resolve().exists():
            errors += fail(f"broken link in {path.relative_to(ROOT)}: {target}")

if errors:
    sys.exit(1)
print(f"Validated {len(REQUIRED)} required files and all local Markdown links.")