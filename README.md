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

The full live-validation workflow uses the `chromium-test` skill for the provisioned Chromium browser and the `mail` skill for verification messages in approved owned mailboxes. Select account identities under `email-access-policy`; `mail` does not create disposable inboxes.

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
If the agent writes a separate PoC file, it goes beside the report under `reports/<FID>/`; the report itself includes reproduction steps even when no separate PoC is needed.

## Repository contents

- `SKILL.md` — skill metadata, workflow, validation gates, escalation guidance, and report format
- `LICENSE` — MIT License

## License

MIT
