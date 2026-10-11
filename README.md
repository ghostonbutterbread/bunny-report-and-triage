# bunny-report-and-triage

`bunny-report-and-triage` is an opt-in [GitHub fork](https://github.com/ghostonbutterbread/bunny-report-and-triage) of Sequester-AG/bug-bounty-triage (MIT; upstream revision `9684e1bfc876e841f9c789f0b258902b43d461e4`). It preserves upstream's triage, authorized validation, impact escalation, and single-report method. This trial does not replace BBH's standing reporting workflow.

It is designed to help an agent:

- reproduce findings end to end when testing is authorized;
- separate observed evidence from inference;
- reject weak or non-actionable reports before submission;
- pursue the highest defensible impact without overstating severity; and
- produce concise, evidence-heavy Markdown reports for bug bounty platforms.

## Responsible use

Use this skill only on systems you own or are explicitly authorized to test. Invoking the skill does not grant permission to test a target, exceed a program's scope, access unrelated data, or perform destructive actions.

Review generated files before sharing or committing them. Keep live secrets, unrelated personal data, and restricted raw evidence out of reports. An evidence-only writing request does not authorize live target contact; a separate scoped assignment is required.

## Trial installation

Keep this fork in a separate Git checkout and project its unique skill name `bunny-report-and-triage` to the selected trial agent's skill root. Verify its actual Git revision and resolved skill link. Do not register a new Aiskillsync bridge or assume deployment from this README; wider integration needs the owner's decision after comparing a real report.

## Supporting skills

Evidence-only reporting needs no browser or mailbox. Separately authorized live validation uses BBH's `chromium-test` provisioner and task-scoped MITM; account setup follows `account-testing-policy`/`email-access-policy`, and authorized mailbox retrieval uses `mail` via Composio. This fork does not install upstream's browser or email CLIs or create disposable inboxes.

## Usage

Invoke the skill with an exact FID packet and a vulnerability description or its evidence index; no existing report, submission draft, or standalone PoC file is required:

```text
Use $bunny-report-and-triage on <absolute path to reports/<FID>/EVIDENCE.md> and its necessary raw-evidence pointers to create one upstream-style report for <FID>. This is an evidence-only trial: do not read earlier reports/PoCs, contact the target, or create accounts. Distinguish prior evidence from testing by this run. Give the report path and triage verdict in chat.
```

For live validation, provide a separate scoped assignment with current program rules, approved account/fixture ownership, and the specific proof question. Otherwise the skill evaluates existing evidence and identifies what remains unverified.

## Output

The skill writes one Markdown report named from the target and vulnerability class with the packet's exact FID suffix, such as:

```text
reports/FID-42/api-example-com-idor-FID-42.md
```

If the exact destination exists, stop rather than overwrite or invent a version. Internal triage commentary and the GREEN/YELLOW/RED verdict stay in chat, outside the report. A trial draft with missing proof is not submission-ready; the user reviews the output before any future pipeline adoption or submission decision.

## Repository contents

- `SKILL.md` — skill metadata, workflow, validation gates, escalation guidance, and report format
- `LICENSE` — MIT License

## License

MIT
