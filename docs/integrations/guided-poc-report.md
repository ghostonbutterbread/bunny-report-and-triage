# Guided PoC report integration dossier

- **Status:** review-ready
- **Owner:** Hermes, Kanban `t_886f4f96`
- **Branch:** `feat/guided-poc-report`
- **Base commit:** `be69e55d009d96c9fbf7c205b0c8eb20e2dd1a24`
- **Intended integration target:** standalone fork `main`; Hoster opt-in trial only after review
- **Last updated:** 2026-10-11
- **Owning feature branch/ref:** `feat/guided-poc-report`
- **Latest immutable recovery checkpoint:** `e9e5f35193a3afa9b17fde28d14de1a000892d10`
- **Feature implementation commit(s):** `58b76123a4e9af38ec455e64e33f31bdacc3ca8b`, `e9e5f35193a3afa9b17fde28d14de1a000892d10`
- **Inspiration / canonical references:** Ryu's Discord request `1558984140207030394`; existing `triager-first-poc-authoring` and `poc-tooling-policy` for reviewer-facing artifacts.

## Intent

Keep Bunny's upstream six-phase triage and validation pipeline, but change the fork's reviewer PoC packaging: simple one-request, cookie-only replay is inline curl; dependent IDs, multiple requests, or nontrivial setup require a guided standalone PoC and manual replay beneath its minimal invocation. Keep FID output, mail/Chromium adapters, and trial-only deployment. Do not edit canonical BBH policy, existing finding reports/PoCs, or live targets.

## Implemented contract

- The report's `Proof of Concept` subsection is always executable. Inline curl has no extra Manual Reproduction heading. A complex PoC is `reports/<FID>/poc.<ext>` with only required flags in the report and chronological manual alternative below.
- A standalone PoC discovers owned fixture IDs, sequences requests, verifies the actual effect, handles controlled cleanup/manual handoffs, requests runtime auth, and supports an optional proxy. Its claims align with the manual replay and the report.
- A narrow reviewer-input exception keeps reporter credentials and owned-fixture IDs out of reviewer-run commands while preserving material source proof, including negative controls. Unlike upstream's absolute verbatim treatment, required secret-bearing excerpts stop for explicit disclosure/redaction or a new authorized secret-free observation; they are not silently published or omitted. The readiness STOP remains.
- Artifact creation/inspection is not blanket permission for new live target testing; existing authorization and scope still govern it. No pipeline auto-integration or external submission.

## Evidence and review

- Test-first RED: new format and reviewer-secret/fidelity contract assertions failed against the prior skill as expected.
- GREEN: `python3 -m unittest discover -s tests -q` passed 12 tests; `git diff --check` passed, in the isolated feature worktree.
- Independent review: initial verdict REVISE at `8d5e65e` for selective-quote fidelity, secret-bearing evidence handoff, and non-Cookie runtime authentication. These three points were corrected at `e9e5f35193a3afa9b17fde28d14de1a000892d10`; fresh independent re-review of `710a2b3` returned PASS with no file:line blocker.
- Live target testing: not run; a future approved finding-specific trial must exercise the full workflow separately.

## Blockers and deferred work

- **Missing test or evidence:** Real end-to-end generated guided PoC on an authorized finding.
- **Command / fixture / environment needed:** Task-specific approved account/owned fixture and finding packet; no such live assignment is part of this skill-edit request.
- **Trigger to run it:** Ryu selects a finding for an opt-in trial with scope and authorization.
- **Why it blocks integration, activation, or promotion:** It does not block the instruction-only standalone fork update, but prevents claiming actual end-to-end PoC generation was proven.
- **Next completion step / successor reference:** Run an opt-in finding trial; preserve existing report files unless rewrite explicitly requested.

## Interruption / resume handoff

- **Owning feature branch/ref:** `feat/guided-poc-report`
- **Latest immutable recovery checkpoint:** `e9e5f35193a3afa9b17fde28d14de1a000892d10`
- **Feature implementation commit(s):** `58b76123a4e9af38ec455e64e33f31bdacc3ca8b`, `e9e5f35193a3afa9b17fde28d14de1a000892d10`
- **Exact resume point:** Independent review of feature and dossier; publish standalone fork main and refresh Hoster trial only after accepted verdict.
- **Working-tree state at handoff:** clean after dossier checkpoint.

## Decision gates

- **Integration gate:** Focused tests and source diff, independent reviewer PASS, clean main, no conflicting edits; remove this dossier from integrated main.
- **Activation / cohort gate:** Source remote push, clean Hoster fast-forward, link/skill-load readback; no BBH canonical pipeline changes.
- **Promotion gate:** This is a standalone fork feature, not BBH beta/main promotion.

## Decision record

- 2026-10-11 — Feature prepared test-first; initial independent reviewer returned REVISE on source-fidelity scope, secret-bearing evidence, and non-Cookie authentication. Focused correction committed at `e9e5f35193a3afa9b17fde28d14de1a000892d10`. Fresh re-review of tip `710a2b3182c985280382108e8471de18d34e3772` returned PASS; accepted for standalone main integration, excluding this temporary dossier. Real finding trial remains deferred.
