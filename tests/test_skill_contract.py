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
            "Preserve material source evidence", "CVSS:        X.X",
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
        self.assertIn("Choose the smallest reviewer-facing PoC", self.skill)
        self.assertIn("alongside the report under `reports/<FID>/`", self.skill)
        self.assertNotIn("_meta/", self.skill)
        self.assertNotIn("REPORT.md", self.skill)

    def test_simple_replay_prefers_inline_curl_without_duplicate_manual_section(self):
        for phrase in (
            "#### Proof of Concept", "only a reviewer-supplied Cookie header",
            "omit the Manual Reproduction heading", "no discovered IDs or dependent setup",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_dependent_setup_requires_standalone_guided_poc_and_manual_replay(self):
        for phrase in (
            "triager-first-poc-authoring", "poc.<ext>",
            "discover target-specific IDs", "send the dependent requests",
            "verify the claimed effect", "#### Manual Reproduction",
            "only required flags", "same finding and observed effect",
            "supports `--proxy URL`", "Cookie header for a session-based target",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")
        self.assertIn("reports/<FID>/", self.skill)

    def test_reviewer_runtime_inputs_do_not_embed_reporter_session(self):
        for phrase in (
            "reviewer-run input exception", "reviewer's Cookie header",
            "reporter's live session Cookie", "reviewer-owned fixture IDs",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_source_fidelity_checks_all_material_proof_and_stops_for_secrets(self):
        for phrase in (
            "including negative controls", "not merely the excerpts you chose to quote",
            "stop before placing secret-bearing evidence in the paste-ready report",
            "ask for an explicit disclosure or redaction decision",
            "scan the whole finished report for live credentials",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_non_cookie_auth_is_provided_at_runtime_for_guided_poc(self):
        for phrase in (
            "Bearer token or API key when the target uses one",
            "rather than embedding the reporter's credential",
        ):
            self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_readiness_checks_final_reviewer_artifact(self):
        for phrase in (
            "inspect the finished PoC's setup, requests, output, and failure paths",
            "do not claim an unrun artifact was live-tested",
        ):
            self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_delegates_poc_authoring_and_requires_final_e2e_run(self):
        for phrase in (
            "MUST load `triager-first-poc-authoring`", "including inline `curl`",
            "standalone `poc.<ext>`", "MUST execute the final reviewer-facing PoC end to end",
            "not ready", "JSON Cookie", "If the skill is unavailable",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_submission_format_has_bullet_prerequisites_and_command_flag_bullets(self):
        report_template = self.skill.split("### Report Template", 1)[1].split("### Report Rules", 1)[0]
        self.assertIn("**Prerequisites**\n- ", report_template)
        self.assertIn("```bash\npython3 poc.py\n```", report_template)
        self.assertIn("- `--proxy URL`", report_template)
        self.assertIn("implemented flags", report_template)
        self.assertIn("one command line", report_template)
        self.assertIn("#### Manual Reproduction", report_template)

    def test_readme_matches_fork_interfaces(self):
        self.assertIn("$bunny-report-and-triage", self.readme)
        self.assertIn("reports/D15/example-com-idor-D15.md", self.readme)
        self.assertIn("`mail`", self.readme)
        self.assertIn("`chromium-test`", self.readme)
        self.assertNotIn("agent-email-cli", self.readme)
        self.assertNotIn("agent-browser", self.readme)


if __name__ == "__main__":
    unittest.main()
