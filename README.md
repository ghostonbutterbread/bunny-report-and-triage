# bunny-report-and-triage

`bunny-report-and-triage` is a fork of Sequester-AG/bug-bounty-triage for rigorous bug bounty report triage, independent validation, impact escalation, and submission-ready reporting.

It is designed to help an agent:

- reproduce findings end to end when testing is authorized;
- separate observed evidence from inference;
- reject weak or non-actionable reports before submission;
- pursue the highest defensible impact without overstating severity; and
- produce concise, evidence-heavy Markdown reports for bug bounty platforms.

## Responsible use

Use this skill only on systems you own or are explicitly authorized to test. Invoking the skill does not grant permission to test a target, exceed a program's scope, access unrelated data, or perform destructive actions.

The skill may preserve sensitive evidence in generated reports when the user supplies it. Review generated files before sharing or committing them, and follow the applicable bug bounty program's rules.

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

Invoke the skill with a report, vulnerability description, or target and finding:

```text
Use $bunny-report-and-triage to validate this report and determine whether it is ready to submit: <report>. FID: <exact finding ID>
```

For live validation, provide the relevant authorization and scope. The complete workflow can use Chromium browser automation, direct HTTP requests, and owned test accounts with authorized mail access when those capabilities are available in the host environment. If live testing is unavailable, the skill should state what remains unverified.

## Output

For a supported, submission-ready finding, the skill writes a Markdown report named from the target and vulnerability class, such as:

```text
reports/D15/example-com-idor-D15.md
```

Internal triage commentary stays outside the submission file.
The report's **Prerequisites** are short bullet points. **Proof of Concept** contains a runnable curl when one fixed request needs at most the reviewer's own Cookie header; it has no separate PoC file or Manual Reproduction heading. If replay requires project IDs, dependent requests, or stateful setup, `triager-first-poc-authoring` guides a `poc.<ext>` beside the report under `reports/<FID>/`. The report shows one exact invocation (usually `python3 poc.py`) and bullet points for supported flags below it; **Manual Reproduction** follows with chronological steps and decisive evidence. The script should discover owned-fixture IDs, accept raw or JSON Cookie input privately, and verify the effect rather than merely sending requests. Its final artifact must have an authorized end-to-end run before the PoC or package is called ready. Reviewer authentication is supplied at runtime, not embedded in the shareable PoC or report command. This trial fork is not automatically integrated into the canonical BBH reporting pipeline.

## Repository contents

- `SKILL.md` — skill metadata, workflow, validation gates, escalation guidance, and report format
- `LICENSE` — MIT License

## License

MIT
