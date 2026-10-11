# Guided PoC report integration dossier

- **Status:** review-ready
- **Owner:** Hermes, Kanban `t_886f4f96`
- **Branch:** `feat/guided-poc-report`
- **Base commit:** `be69e55d009d96c9fbf7c205b0c8eb20e2dd1a24`
- **Intended integration target:** standalone fork `main`; Hoster opt-in trial only after review
- **Last updated:** 2026-10-11
- **Owning feature branch/ref:** `feat/guided-poc-report`
- **Latest immutable recovery checkpoint:** `58b76123a4e9af38ec455e64e33f31bdacc3ca8b`
- **Feature implementation commit(s):** `58b76123a4e9af38ec455e64e33f31bdacc3ca8b`
- **Inspiration / canonical references:** Ryu's Discord request `1558984140207030394`; existing `triager-first-poc-authoring` and `poc-tooling-policy` for reviewer-facing artifacts.

## Intent

Keep Bunny's upstream six-phase triage and validation pipeline, but change the fork's reviewer PoC packaging: simple one-request, cookie-only replay is inline curl; dependent IDs, multiple requests, or nontrivial setup require a guided standalone PoC and manual replay beneath its minimal invocation. Keep FID output, mail/Chromium adapters, and trial-only deployment. Do not edit canonical BBH policy, existing finding reports/PoCs, or live targets.

## Implemented contract

- The report's `Proof of Concept` subsection is always executable. Inline curl has no extra Manual Reproduction heading. A complex PoC is `reports/<FID>/poc.<ext>` with only required flags in the report and chronological manual alternative below.
- A standalone PoC discovers owned fixture IDs, sequences requests, verifies the actual effect, handles controlled cleanup/manual handoffs, requests runtime auth, and supports an optional proxy. Its claims align with the manual replay and the report.
- A narrow reviewer-input exception keeps reporter session Cookie and fixture IDs out of reviewer-run commands without changing factual exploit evidence. Other upstream source-fidelity behavior and the readiness STOP remain.
- Artifact creation/inspection is not blanket permission for new live target testing; existing authorization and scope still govern it. No pipeline auto-integration or external submission.

## Evidence and review

- Test-first RED: new format contract assertions failed against the base skill as expected.
- GREEN: `python3 -m unittest discover -s tests -q` passed 10 tests; `git diff --check` passed, in the isolated feature worktree.
- Independent review: pending fresh reviewer verdict on committed branch.
- Live target testing: not run; a future approved finding-specific trial must exercise the full workflow separately.

## Blockers and deferred work

- **Missing test or evidence:** Real end-to-end generated guided PoC on an authorized finding.
- **Command / fixture / environment needed:** Task-specific approved account/owned fixture and finding packet; no such live assignment is part of this skill-edit request.
- **Trigger to run it:** Ryu selects a finding for an opt-in trial with scope and authorization.
- **Why it blocks integration, activation, or promotion:** It does not block the instruction-only standalone fork update, but prevents claiming actual end-to-end PoC generation was proven.
- **Next completion step / successor reference:** Run an opt-in finding trial; preserve existing report files unless rewrite explicitly requested.

## Interruption / resume handoff

- **Owning feature branch/ref:** `feat/guided-poc-report`
- **Latest immutable recovery checkpoint:** `58b76123a4e9af38ec455e64e33f31bdacc3ca8b`
- **Feature implementation commit(s):** `58b76123a4e9af38ec455e64e33f31bdacc3ca8b`
- **Exact resume point:** Independent review of feature and dossier; publish standalone fork main and refresh Hoster trial only after accepted verdict.
- **Working-tree state at handoff:** clean after dossier checkpoint.

## Decision gates

- **Integration gate:** Focused tests and source diff, independent reviewer PASS, clean main, no conflicting edits; remove this dossier from integrated main.
- **Activation / cohort gate:** Source remote push, clean Hoster fast-forward, link/skill-load readback; no BBH canonical pipeline changes.
- **Promotion gate:** This is a standalone fork feature, not BBH beta/main promotion.

## Decision record

- 2026-10-11 — Feature prepared test-first; reviewer gate pending.
