# bunny-report-and-triage

This is a **GitHub fork** of Sequester-AG/bug-bounty-triage (MIT; upstream commit `9684e1bfc876e841f9c789f0b258902b43d461e4`) for a one-report, read-only comparison trial on Hoster. The fork lives at `ghostonbutterbread/bunny-report-and-triage`; it is **not** an integration into BBH's canonical reporting policy. The source report, PoC, evidence, and ledger are never edited by a report-only invocation.

It is designed to help an agent:

- assess existing evidence without live testing by default;
- separate observed evidence from inference;
- reject weak or non-actionable reports before submission;
- pursue the highest defensible impact without overstating severity; and
- preserve upstream's `<target-domain>-<vuln-type>.md` filename and append the exact FID, saving the rewrite in the source `reports/<FID>/` packet with a private triage note under `_meta/`.

## Responsible use

Use this skill only on systems you own or are explicitly authorized to test. Invoking the skill does not grant permission to test a target, exceed a program's scope, access unrelated data, or perform destructive actions.

Do not copy live secrets or unrelated private data into experimental output. A separately authorized live task must use the approved Chromium Test provisioner and owned fixtures; report-only rewriting does not launch it.

## Trial installation on Hoster

Clone this fork as a separate Git checkout on Hoster, then link the skill directory by its unique name `bunny-report-and-triage` into the selected agent's skill root. These links are **manual trial projections**, not Aiskillsync-managed sources. Do not register a new Aiskillsync bridge or alter profile selection until Ryushe reviews an actual rewrite and authorizes integration. Verify the actual link target and `SKILL.md` revision before invoking; do not assume deployment just because this README exists.

## Optional live validation dependencies

None for report-only rewriting. A separately authorized live engagement uses Hoster's existing BBH Chromium Test provisioner and task MITM; approved verification mail uses the existing Composio connection, not agent-email. This standalone report skill does not create accounts or install third-party CLIs.

## Usage

Invoke the skill with the selected report path inside an exact FID packet. If the FID/path is unknown, supply it before drafting:

```text
Use $bunny-report-and-triage in report-only mode to rewrite only <absolute path to reports/<FID>/SUBMISSION.md or REPORT.md>. Preserve the exact FID. Read only its selected evidence; do not change the source report, PoC, ledger, or any other finding, and do not test the live target. Use upstream's <target-domain>-<vuln-type>.md naming with -<FID> appended before .md, in the same packet. Show me the report and triage-note paths.
```

For a separate live-validation assignment, provide the current program scope, account and fixture ownership, and an explicit unresolved proof question. Without that, the skill only evaluates existing evidence and labels unverified steps.

## Output

For an input `.../reports/<FID>/SUBMISSION.md` or `REPORT.md`, a fresh run creates only these two **new** files:

```text
.../reports/<FID>/<target-domain>-<vuln-type>-<FID>.md
.../reports/<FID>/_meta/<target-domain>-<vuln-type>-<FID>-TRIAGE.md
```

For example, a packet `reports/FID-42/` about an IDOR at `api.example.com` yields `reports/FID-42/api-example-com-idor-FID-42.md`. The suffix is the exact FID; this is upstream's filename with only that suffix and destination changed. If the exact filename already exists, stop and ask rather than overwriting or adding a version. Internal triage commentary stays in `_meta/`. Neither file is a platform submission or a change to `SUBMISSION.md`.

## Repository contents

- `SKILL.md` — near-upstream standalone workflow with only environment and safety adaptations
- `LICENSE` — MIT License

## License

MIT
