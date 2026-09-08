import argparse
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts/context_guard.py"
SPEC = importlib.util.spec_from_file_location("context_guard", MODULE_PATH)
context_guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(context_guard)


class ContextGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.previous_state_path = context_guard.STATE_PATH
        context_guard.STATE_PATH = Path(self.temp.name) / ".agent/context.json"

    def tearDown(self):
        context_guard.STATE_PATH = self.previous_state_path
        self.temp.cleanup()

    def test_path_allowlist_supports_directories_and_globs(self):
        self.assertTrue(context_guard.path_allowed("src/auth/login.py", ["src/auth"]))
        self.assertTrue(context_guard.path_allowed("tests/test_auth.py", ["tests/test_auth*.py"]))
        self.assertFalse(context_guard.path_allowed("infra/prod.yml", ["src/auth", "tests/*.py"]))

    def test_init_and_checkpoint_persist_compact_state(self):
        args = argparse.Namespace(
            intent="Fix auth redirect",
            invariant=["Keep authorization behavior"],
            allow=["src/auth"],
            out_of_scope=["Dependencies"],
            acceptance=["Expired sessions redirect"],
            verification=["pytest tests/test_auth.py"],
            max_attempts=2,
            force=False,
        )
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(context_guard.command_init(args), 0)
            self.assertEqual(
                context_guard.command_checkpoint(
                    argparse.Namespace(summary="Failure reproduced", next_action="Patch branch", failed_hypothesis="Cookie parsing")
                ),
                0,
            )
        state = context_guard.load_state()
        self.assertEqual(state["intent"], "Fix auth redirect")
        self.assertEqual(state["next_action"], "Patch branch")
        self.assertEqual(state["failed_hypotheses"], ["Cookie parsing"])

    def test_repeated_failure_returns_stop_code(self):
        init_args = argparse.Namespace(
            intent="Fix auth redirect",
            invariant=[],
            allow=["src/auth"],
            out_of_scope=[],
            acceptance=[],
            verification=[],
            max_attempts=2,
            force=False,
        )
        with contextlib.redirect_stdout(io.StringIO()):
            context_guard.command_init(init_args)
            first = context_guard.command_failure(argparse.Namespace(signature="same", hypothesis=None))
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            second = context_guard.command_failure(argparse.Namespace(signature="same", hypothesis="First patch failed"))
        self.assertEqual(first, 0)
        self.assertEqual(second, 2)


if __name__ == "__main__":
    unittest.main()
