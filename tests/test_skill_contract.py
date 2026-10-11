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
        self.assertTrue(self.skill.startswith("---\nname: bunny-report-and-triage\n"))
        self.assertIn("9684e1bfc876e841f9c789f0b258902b43d461e4", self.skill)
        self.assertIn("Copyright (c) 2026 Sequester-AG", (ROOT / "LICENSE").read_text())

    def test_report_only_mode_never_retests_or_overwrites(self):
        for text in (
            "report-only experiment (default): skip all live actions",
            "do not access the live target",
            "never overwrite the report supplied",
            "reports/<FID>/<target-domain>-<vuln-type>-<FID>.md",
            "_meta/<target-domain>-<vuln-type>-<FID>-TRIAGE.md",
            "do not create or edit any of those canonical files",
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
            "require a real `reports/<FID>/` parent",
            "require its `reports` parent to be a real, approved directory, not a symlink",
            "Reject a symlinked source, packet, `_meta`, or candidate output",
            "Preflight **both** intended filenames for absence",
            "Create the private triage note first, then the visible report",
            "using exclusive creation for each",
            "remove only this run's newly created file(s) after checking their exact path and file identity",
            "if either exact filename already exists, stop and ask",
            "if the source lacks a valid FID packet path, **stop for the packet path**",
        ):
            self.assertIn(text.lower(), self.skill.lower(), text)

    def test_standalone_not_promoted_as_canonical(self):
        self.assertIn("standalone, opt-in report experiment", self.skill)
        self.assertIn("not** the canonical submission", self.skill)
        self.assertIn("GitHub fork", self.readme)
        self.assertIn("ghostonbutterbread/bunny-report-and-triage", self.readme)
        self.assertIn("Do not register a new Aiskillsync bridge", self.readme)
        self.assertIn("do not assume deployment", self.readme)

    def test_upstream_filename_with_fid_suffix_is_visible_and_noncanonical(self):
        self.assertIn("Keep the upstream output convention", self.skill)
        self.assertIn("The final `<FID>` is the **exact packet directory name**", self.skill)
        self.assertIn("A new file at the packet front door is intentional for discoverability", self.skill)
        self.assertIn("reports/FID-42/api-example-com-idor-FID-42.md", self.readme)
        self.assertIn("rather than overwriting or adding a timestamp/version suffix", self.skill)
        self.assertIn("not a new canonical report stage", self.skill)


if __name__ == "__main__":
    unittest.main()
