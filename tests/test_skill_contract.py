"""Static contract checks for the upstream-style, evidence-first trial skill."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_identity_and_license(self):
        self.assertTrue(self.skill.startswith("---\nname: bunny-report-and-triage\n"))
        self.assertIn("9684e1bfc876e841f9c789f0b258902b43d461e4", self.skill)
        self.assertIn("Copyright (c) 2026 Sequester-AG", (ROOT / "LICENSE").read_text())

    def test_upstream_pipeline_preserved(self):
        for heading in ("PHASE 1: INTAKE", "PHASE 2: LIVE END-TO-END TESTING", "PHASE 3: SUBMISSION READINESS", "PHASE 4: ESCALATION", "PHASE 5: GENERATE SUBMISSION REPORT", "PHASE 6: TRIAGE DECISION", "Knowledge-Assumption Audit"):
            with self.subTest(heading=heading):
                self.assertIn(heading, self.skill)
        self.assertIn("### Summary", self.skill)
        self.assertIn("### Reproduction", self.skill)
        self.assertIn("### Impact", self.skill)
        self.assertIn("### Remediation", self.skill)

    def test_evidence_only_intake_no_old_stage_files(self):
        for text in ("`EVIDENCE.md`", "No prior report, submission draft, or standalone PoC is required", "Writing a report from evidence does not authorize target contact", "do not import an earlier report or PoC", "Distinguish prior evidence from testing by this run"):
            self.assertIn(text.lower(), (self.skill + self.readme).lower())
        self.assertNotIn("`REPORT.md` or `SUBMISSION.md`", self.skill)
        self.assertNotIn("finding_submission.py", self.skill)

    def test_environment_adapters_and_privacy(self):
        for text in ("`chromium-test`", "Chromium Test provisioner", "task-scoped MITM", "`hoster-ssh`", "`email-access-policy`", "`mail`", "Composio", "never paste a live cookie or token", "no live web shell by default"):
            with self.subTest(text=text):
                self.assertIn(text.lower(), self.skill.lower())
        self.assertNotIn("agent-email create", self.skill)
        self.assertNotIn("SOURCE FIDELITY — NEVER REDACT", self.skill)

    def test_single_exclusive_report_in_exact_fid_packet(self):
        for text in ("reports/<FID>/<target-domain>-<vuln-type>-<FID>.md", "reports/FID-42/api-example-com-idor-FID-42.md", "Use exclusive creation", "If the exact file exists, stop", "Reject symlinked packet/output components", "triage commentary and the GREEN/YELLOW/RED verdict stay in chat"):
            self.assertIn(text.lower(), (self.skill + self.readme).lower())
        self.assertNotIn("_meta/<target-domain>", self.skill)
        self.assertNotIn("current working directory.**", self.skill)

    def test_not_canonical_or_auto_submission(self):
        for text in ("opt-in trial", "not a change to the standing BBH report pipeline", "No second report-writing stage", "do not claim it was submitted", "Do not register a new Aiskillsync bridge"):
            self.assertIn(text.lower(), (self.skill + self.readme).lower())


if __name__ == "__main__":
    unittest.main()
