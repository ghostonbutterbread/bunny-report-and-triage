"""Static checks for the isolated report experiment's safety and provenance."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"


class SkillContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")

    def test_name_and_upstream_license(self):
        self.assertTrue(self.skill.startswith("---\nname: bug-bounty-triage-experiment\n"))
        self.assertIn("9684e1bfc876e841f9c789f0b258902b43d461e4", self.skill)
        self.assertIn("Copyright (c) 2026 Sequester-AG", (ROOT / "LICENSE").read_text())

    def test_report_only_mode_never_retests_or_overwrites(self):
        for text in (
            "report-only experiment (default): skip all live actions",
            "do not access the live target",
            "never overwrite the report supplied",
            "_runs/triage-experiment-<YYYYMMDDThhmmssZ>-<unique-suffix>/",
            "REWRITE.md",
            "_meta/TRIAGE.md",
            "do not edit the canonical `EVIDENCE.md`, `REPORT.md`, `SUBMISSION.md`, PoC, ledger",
            "No `finding_submission.py` or other BBH report writer is required",
        ):
            self.assertIn(text.lower(), self.skill.lower(), text)

    def test_browser_mail_and_secrets_boundaries(self):
        for text in (
            "Chromium Test provisioner", "browser_provisioner.py request",
            "task-scoped MITM", "Composio", "never use `agent-email`",
            "Do not copy credentials, cookies, keys", "never paste a live cookie or token",
        ):
            self.assertIn(text.lower(), self.skill.lower(), text)
        self.assertNotIn("agent-email create", self.skill)
        self.assertNotIn("Write a file called `<target-domain>", self.skill)
        self.assertNotIn("Never redact supplied evidence", self.skill)

    def test_hoster_dispatch_and_capsule_creation_are_bounded(self):
        for text in (
            "bbh --root", "bbh --print-command", "/bin/bash -lc",
            "hoster-ssh", "never run the provisioner from bare SSH",
            "resolve the input file and the approved packet parent",
            "reject symlinks in the output path components",
            "create the fresh capsule exclusively", "fail closed on collision",
            "for non-packet input, use the separately specified directory or task-owned scratch",
        ):
            self.assertIn(text.lower(), self.skill.lower(), text)

    def test_standalone_not_promoted_as_canonical(self):
        self.assertIn("standalone, opt-in report experiment", self.skill)
        self.assertIn("not** the canonical submission", self.skill)
        self.assertIn("not** a GitHub-hosted fork", self.readme)
        self.assertIn("Do not register a new Aiskillsync bridge", self.readme)
        self.assertIn("do not assume deployment", self.readme)


if __name__ == "__main__":
    unittest.main()
