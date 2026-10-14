# bunny-report-and-triage

`bunny-report-and-triage` is a fork of Sequester-AG/bug-bounty-triage for evidence-led FID packet report triage and optional separately authorized validation.

It is designed to help an agent:

- draft from populated `EVIDENCE.md` in the ledger-resolved finding packet and linked proof without live testing by default;
- reproduce findings end to end only under a separate authorized live assignment;
- separate observed evidence from inference;
- reject weak or non-actionable reports before submission;
- pursue the highest defensible impact without overstating severity; and
- produce concise, evidence-heavy Markdown reports for bug bounty platforms.

## Responsible use

Use this skill only on systems you own or are explicitly authorized to test. Invoking the skill does not grant permission to test a target, exceed a program's scope, access unrelated data, or perform destructive actions.

Do not copy live secrets or unrelated private evidence into generated reports. Review generated files before sharing or committing them, and follow the applicable bug bounty program's rules.

## Installation

### Skills CLI

```bash
npx skills add ghostonbutterbread/bunny-report-and-triage --skill bunny-report-and-triage
```

### Codex

```bash
git clone https://github.com/ghostonbutterbread/bunny-report-and-triage.git ~/.codex/skills/bunny-report-and-triage
```

### Agent skills directory

```bash
git clone https://github.com/ghostonbutterbread/bunny-report-and-triage.git ~/.agents/skills/bunny-report-and-triage
```

## Supporting skills and CLIs

The full live-validation workflow uses the `chromium-test` skill for the provisioned Chromium browser and the `mail` skill for verification messages in approved owned mailboxes. Select account identities under `email-access-policy`; `mail` does not create disposable inboxes. Inline `curl` needs no PoC-authoring skill; it still needs authorized effect validation and reviewer-supplied authentication. A standalone PoC requires `triager-first-poc-authoring` and `poc-tooling-policy`; the fork does not substitute its own standalone authoring guidance when those skills are unavailable.

## Usage

Invoke the skill with an absolute source path inside the ledger-resolved finding packet and its linked ledger context/proof:

```text
Use $bunny-report-and-triage in report-only mode on <absolute path to ledger-resolved EVIDENCE.md> and its linked ledger proof. Check the populated Verified claim and exact evidence-index pointers before writing. Do not test live. Create only <resolved-packet>/<target-domain>-<vuln-type>-<FID>.md when supported; do not create REPORT.md or SUBMISSION.md.
```

An existing `REPORT.md` or `SUBMISSION.md` in the same packet may instead be selected as a legacy source, provided its proof pointers resolve. Neither file is required or created for new findings. For separate live validation, provide current authorization, scope, and the unresolved proof question; absent that, the skill reads only existing evidence and labels unverified steps.

## Output

For a verified, populated finding with resolvable evidence-index pointers, the skill creates only one new Markdown report named from the target, vulnerability class, and **exact ledger FID**, such as:

```text
reports/D15-api-idor/example-com-idor-D15.md
```

It never overwrites a previous report, edits the source, ledger, PoC, or canonical files, or writes a report from a pending scaffold. Internal triage commentary stays outside the report file. Authored prose in the submission report and triage summary uses plain hyphens, no em dashes; literal commands, payloads, URLs, and quoted evidence stay unchanged.
Keep each authored paragraph on one source line without manually wrapping it; preserve literal evidence line breaks. The report's **Prerequisites** are short bullet points. **Proof of Concept** uses a recorded fixed-request curl when appropriate; a recorded standalone `poc.<ext>` beside `EVIDENCE.md` is referenced with its exact invocation and manual replay only when the existing evidence supports it. Optional screenshots and supporting artifacts belong in `evidence/` and are described in `EVIDENCE.md`. Report-only work neither authors nor executes a PoC. A separately authorized PoC-authoring task follows `triager-first-poc-authoring` and `poc-tooling-policy`, including final-artifact effect verification. Reviewer authentication is supplied at runtime, not embedded in the shareable report. This trial fork is not automatically integrated into the canonical BBH reporting pipeline.

## Repository contents

- `SKILL.md` — skill metadata, workflow, validation gates, escalation guidance, and report format
- `LICENSE` — MIT License

## License

MIT
