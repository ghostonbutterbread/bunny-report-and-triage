# Submission package handoff

- **Status:** feature
- **Owner:** Hermes bugfix
- **Branch:** feat/submission-package-handoff
- **Base commit:** 2bb716b27ec824fbe732770f136b85374eb15316
- **Intended integration target:** main
- **Last updated:** 2026-10-29
- **Owning feature branch/ref:** feat/submission-package-handoff
- **Latest immutable recovery checkpoint:** none yet
- **Feature implementation commit(s):** none yet
- **Inspiration / canonical references:** finding-to-report miss where the writer was listed as a triager and loaded only after it was named

## Intent

Make `bunny-report-and-triage` discoverable as the submission writer, and tell a loaded writer to finish a required standalone PoC in the same package. Do not grant live testing or PoC execution from this skill alone.

## Implemented contract

- Description starts with writing a finding submission and stays within the 60-character discovery budget.
- A populated evidence packet is the trigger for the FID-named report.
- A standalone PoC loads `triager-first-poc-authoring` and `poc-tooling-policy` and is finished with the report. Inline proof stays in the report.
- Missing proof or authorization remains a named gap.

## Evidence and review

- Tests and commands: description-length check; `git diff --check`
- Independent review: pending
- Replay/cohort/fixture evidence: none; text-only routing change
- Merge/ancestry evidence: pending

## Blockers and deferred work

- **Missing test or evidence:** fresh-agent discovery check that a submission request loads this skill without being told its name
- **Command / fixture / environment needed:** disposable agent with this skill projected
- **Trigger to run it:** after the reviewed text is on the checkout agents actually read
- **Why it blocks integration, activation, or promotion:** it does not block the text change; it blocks claiming agents now select the writer
- **Next completion step / successor reference:** project the merged main checkout through the existing Hoster skill symlink, then run the fresh-agent check

## Interruption / resume handoff

- **Owning feature branch/ref:** feat/submission-package-handoff
- **Latest immutable recovery checkpoint:** none yet
- **Feature implementation commit(s):** none yet
- **Exact resume point:** commit this dossier with the skill edit, then review before merging to main
- **Working-tree state at handoff:** intentionally uncommitted until the implementation commit

## Decision gates

- **Integration gate:** independent review of the skill diff, then merge to main. This repository has no beta lane.
- **Activation / cohort gate:** Hoster `~/.agents/skills/bunny-report-and-triage` resolves to the updated main checkout
- **Promotion gate:** not applicable; main is the only published lane

## Decision record

- 2026-10-29 — created for the submission-writer discovery and same-package PoC handoff.
