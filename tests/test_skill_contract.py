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
            "<absolute ledger-resolved EVIDENCE.md path",
            "Extract from the selected FID packet source",
            "PHASE 1: INTAKE", "PHASE 2: LIVE END-TO-END TESTING",
            "PHASE 3: SUBMISSION READINESS", "PHASE 4: ESCALATION",
            "PHASE 5: GENERATE SUBMISSION REPORT", "PHASE 6: TRIAGE DECISION",
            "Skip Phase 2 entirely in report-only mode",
            "separate assignment must explicitly authorize live testing",
            "If the PoC fails:", "STOP before creating the FID-named output",
            "Decisive cited prior proof", "reason about the maximum defensible impact",
            "do not test a chain live", "Knowledge-Assumption Audit",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)
        self.assertNotIn("do not use an existing report", self.skill)
        self.assertNotIn("trial draft", self.skill.lower())

    def test_upstream_report_and_decision_gates(self):
        for phrase in (
            "### Summary", "### Reproduction", "### Impact", "### Remediation",
            "Paste test before delivery", "Source-fidelity and privacy test before delivery",
            "Preserve material shareable evidence", "CVSS:        X.X",
            "Bounty Est:  [$range]", "If GREEN: say the report is a candidate for review",
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

    def test_report_and_optional_poc_in_ledger_packet(self):
        path = "<resolved-packet>/<target-domain>-<vuln-type>-<FID>.md"
        self.assertIn(path, self.skill)
        self.assertIn("stored `report_dir`", self.skill)
        self.assertIn("choose the smallest reviewer-facing PoC", self.skill)
        self.assertIn("alongside the report in the ledger-resolved finding packet", self.skill)
        self.assertIn("Optional screenshots and supporting artifacts belong in `evidence/`", self.readme)
        self.assertNotIn("_meta/", self.skill)
        self.assertIn("Existing `REPORT.md` or `SUBMISSION.md`", self.skill)
        self.assertNotIn("alongside the report under `reports/<FID>/`", self.skill)

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
        self.assertIn("ledger-resolved FID packet destination", self.skill)

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
            "stop before placing the restricted original in the paste-ready report",
            "otherwise obtain an authorized secret-free observation",
            "Scan the entire output for live credentials",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_private_evidence_and_red_gate_do_not_authorize_leaks(self):
        for phrase in (
            "never in BBH `EVIDENCE.md`", "outside shared report packets",
            "approved private evidence location", "never authorizes copying a live credential",
            "symlinks in intermediate directories and leaf files",
            "Report: not created", "whether a report was created",
            "<lane-root>/ledgers/ledger.json", "context/target_profile.json",
            "unapproved** private response content", "specifically approves that excerpt",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.skill.lower())
        self.assertNotIn("unless the user explicitly authorizes a specific redaction", self.skill)
        self.assertNotIn("ask for an explicit disclosure/redaction decision", self.skill)
        self.assertNotIn("After writing the report, present this summary", self.skill)

    def test_non_cookie_auth_is_provided_at_runtime_for_guided_poc(self):
        for phrase in (
            "Bearer token or API key when the target uses one",
            "rather than embedding the reporter's credential",
        ):
            self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_readiness_checks_final_reviewer_artifact(self):
        for phrase in (
            "inspect the finished PoC's setup, requests, output, and failure paths",
            "Do not execute it in report-only mode",
        ):
            self.assertTrue(phrase in self.skill, f"Missing: {phrase}")

    def test_delegates_poc_authoring_and_requires_final_e2e_run(self):
        for phrase in (
            "For a standalone PoC, MUST load `triager-first-poc-authoring`",
            "Inline `curl` does not require `triager-first-poc-authoring`",
            "standalone `poc.<ext>`", "authorized final-artifact effect verification",
            "not ready", "JSON Cookie", "If the standalone authoring skill is unavailable",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in self.skill, f"Missing: {phrase}")
        self.assertNotIn("including inline `curl`, MUST load", self.skill)
        self.assertIn("Inline `curl` needs no PoC-authoring skill", self.readme)

    def test_submission_format_has_bullet_prerequisites_and_command_flag_bullets(self):
        report_template = self.skill.split("### Report Template", 1)[1].split("### Report Rules", 1)[0]
        self.assertIn("**Prerequisites**\n- ", report_template)
        self.assertIn("```bash\npython3 poc.py\n```", report_template)
        self.assertIn("- `--proxy URL`", report_template)
        self.assertIn("implemented flags", report_template)
        self.assertIn("one command line", report_template)
        self.assertIn("#### Manual Reproduction", report_template)

    def test_report_and_triage_output_use_hyphens_not_em_dashes(self):
        report_template = self.skill.split("````text\n", 1)[1].split("\n````", 1)[0]
        decision_template = self.skill.split("```\nTRIAGE DECISION\n", 1)[1].split("\n```", 1)[0]
        self.assertNotIn("—", report_template)
        self.assertNotIn("—", decision_template)
        self.assertIn("use ` - ` instead", self.skill)
        self.assertIn("literal commands, payloads, URLs, or quoted evidence", self.skill)
        self.assertIn("no em dashes", self.readme)

    def test_readme_matches_fork_interfaces(self):
        self.assertIn("$bunny-report-and-triage", self.readme)
        self.assertIn("reports/D15-api-idor/example-com-idor-D15.md", self.readme)
        self.assertIn("`mail`", self.readme)
        self.assertIn("`chromium-test`", self.readme)
        self.assertNotIn("agent-email-cli", self.readme)
        self.assertNotIn("agent-browser", self.readme)

    def test_evidence_first_ledger_source(self):
        for phrase in (
            "ledger-resolved finding packet", "linked ledger context/proof",
            "`## Claim and status`", "`Verified: ...`", "`## Evidence index`",
            "exact, resolvable pointers", "independent effect verification",
            "A `Pending` field", "stop before report creation",
            "For legacy `REPORT.md` or `SUBMISSION.md` intake",
            "do not infer evidence from neighboring findings",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.skill.lower())
        self.assertIn("Neither file is required or created for new findings", self.readme)

    def test_historical_fid_only_packet_is_explicit_fallback(self):
        self.assertIn("or a legacy `reports/<FID>/` packet", self.skill)
        self.assertIn("when the stored path is absent", self.skill)
        self.assertIn("verify that `evidence_path` is in that same packet", self.skill)
        self.assertNotIn("Write exactly one new file at `reports/<FID>/", self.skill)

    def test_exact_fid_report_only_no_canonical_output_or_overwrite(self):
        for phrase in (
            "FID verbatim from the canonical ledger", "exact ledger FID",
            "<resolved-packet>/<target-domain>-<vuln-type>-<FID>.md",
            "every path component", "Do not traverse another FID",
            "create exclusively", "never overwrite or append a timestamp/version suffix",
            "Do not create or edit `EVIDENCE.md`, `REPORT.md`, `SUBMISSION.md`",
            "Read back the new report", "Do not contact a target, run a PoC",
            "Tested:      [NO - report-only source review",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.skill.lower())


    def test_one_line_paragraph_contract(self):
        self.assertIn("Keep paragraphs 1 line, don't manually create the line breaks.", self.skill)
        self.assertIn("Preserve necessary line breaks in code, requests, responses, and other literal evidence.", self.skill)


if __name__ == "__main__":
    unittest.main()
