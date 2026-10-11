"""Static contract checks for the minimal upstream fork."""

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
        self.assertIn("Copyright (c) 2026 Sequester-AG", (ROOT / "LICENSE").read_text())

    def test_upstream_intake_and_six_phase_method(self):
        for phrase in (
            "<bug bounty report, vulnerability description, or target URL + finding>",
            "Extract from the provided report:",
            "PHASE 1: INTAKE", "PHASE 2: LIVE END-TO-END TESTING",
            "PHASE 3: SUBMISSION READINESS", "PHASE 4: ESCALATION",
            "PHASE 5: GENERATE SUBMISSION REPORT", "PHASE 6: TRIAGE DECISION",
            "treat the supplied report as a lead, not proof",
            "independently reproduce the finding end to end",
            "If the PoC fails:", "If the report fails this gate, STOP",
            "Independent end-to-end testing confirms the vulnerability and impact",
            "systematically pursue the maximum defensible impact",
            "test each chain live", "Knowledge-Assumption Audit",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)
        self.assertNotIn("do not use an existing report", self.skill)
        self.assertNotIn("trial draft", self.skill.lower())

    def test_upstream_report_and_decision_gates(self):
        for phrase in (
            "### Summary", "### Reproduction", "### Impact", "### Remediation",
            "Paste test before delivery", "Source-fidelity test before delivery",
            "Never redact supplied evidence", "CVSS:        X.X",
            "Bounty Est:  [$range]", "If GREEN: tell them to submit.",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_only_local_mail_and_chromium_interfaces(self):
        for phrase in ("email-access-policy", "**mail**", "**chromium-test**", "provisioned Chromium browser"):
            self.assertIn(phrase, self.skill)
        for obsolete in ("agent-email", "agent-browser", "in-app browser"):
            self.assertNotIn(obsolete, self.skill)
        for role in ("IDOR/BOLA", "Privilege escalation", "Access control", "Auth bugs"):
            self.assertIn(role, self.skill)

    def test_report_and_optional_poc_in_exact_fid_packet(self):
        path = "reports/<FID>/<target-domain>-<vuln-type>-<FID>.md"
        self.assertIn(path, self.skill)
        self.assertIn("reports/<FID>/", self.skill)
        self.assertIn("If you write a standalone PoC file", self.skill)
        self.assertIn("alongside the report", self.skill)
        self.assertNotIn("_meta/", self.skill)
        self.assertNotIn("REPORT.md", self.skill)

    def test_readme_matches_fork_interfaces(self):
        self.assertIn("$bunny-report-and-triage", self.readme)
        self.assertIn("reports/D15/example-com-idor-D15.md", self.readme)
        self.assertIn("`mail`", self.readme)
        self.assertIn("`chromium-test`", self.readme)
        self.assertNotIn("agent-email-cli", self.readme)
        self.assertNotIn("agent-browser", self.readme)


if __name__ == "__main__":
    unittest.main()
