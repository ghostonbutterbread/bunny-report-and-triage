# bug-bounty-triage-experiment

This is an **isolated local fork** of Sequester-AG/bug-bounty-triage (MIT; upstream commit `9684e1bfc876e841f9c789f0b258902b43d461e4`) for a one-report, read-only comparison trial on Hoster. It is **not** a GitHub-hosted fork or an integration into BBH's canonical reporting policy. The source report, PoC, evidence, and ledger are never edited by a report-only invocation.

It is designed to help an agent:

- assess existing evidence without live testing by default;
- separate observed evidence from inference;
- reject weak or non-actionable reports before submission;
- pursue the highest defensible impact without overstating severity; and
- produce a separate experimental rewrite and private triage note in the source report packet's `_runs/triage-experiment-<UTC>/` capsule.

## Responsible use

Use this skill only on systems you own or are explicitly authorized to test. Invoking the skill does not grant permission to test a target, exceed a program's scope, access unrelated data, or perform destructive actions.

Do not copy live secrets or unrelated private data into experimental output. A separately authorized live task must use the approved Chromium Test provisioner and owned fixtures; report-only rewriting does not launch it.

## Trial installation on Hoster

Install this local fork as a separate Git checkout on Hoster, then link the skill directory by its unique name `bug-bounty-triage-experiment` into the selected agent's skill root. These links are **manual trial projections**, not Aiskillsync-managed sources. Do not register a new Aiskillsync bridge or alter profile selection until Ryushe reviews an actual rewrite and authorizes integration. Verify the actual link target and `SKILL.md` revision before invoking; do not assume deployment just because this README exists.

## Optional live validation dependencies

None for report-only rewriting. A separately authorized live engagement uses Hoster's existing BBH Chromium Test provisioner and task MITM; approved verification mail uses the existing Composio connection, not agent-email. This standalone report skill does not create accounts or install third-party CLIs.

## Usage

Invoke the skill with the selected report path (or pasted report and an explicit separate output directory):

```text
Use $bug-bounty-triage-experiment in report-only mode to rewrite this one existing report: <absolute path>. Read only the selected evidence. Do not change the source report, PoC, ledger, or any other finding; do not test the live target. Show me the experimental rewrite and triage note paths.
```

For a separate live-validation assignment, provide the current program scope, account and fixture ownership, and an explicit unresolved proof question. Without that, the skill only evaluates existing evidence and labels unverified steps.

## Output

For an input `.../reports/<FID>/SUBMISSION.md` or `REPORT.md`, a fresh run writes only:

```text
.../reports/<FID>/_runs/triage-experiment-<UTC>/REWRITE.md
.../reports/<FID>/_runs/triage-experiment-<UTC>/_meta/TRIAGE.md
```

Internal triage commentary stays outside `REWRITE.md`. Neither file is a platform submission or a change to canonical reporting.

## Repository contents

- `SKILL.md` — near-upstream standalone workflow with only environment and safety adaptations
- `LICENSE` — MIT License

## License

MIT
