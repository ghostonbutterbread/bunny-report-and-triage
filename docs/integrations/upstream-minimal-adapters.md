# Upstream-minimal Bunny triage integration dossier

- **Status:** review-ready
- **Owner:** Hermes Agent
- **Branch:** `fix/upstream-minimal-adapters`
- **Base commit:** `cd2a504aad6b344703c184f22716894bf554b20a`
- **Intended integration target:** standalone fork `main` (`ghostonbutterbread/bunny-report-and-triage`), not BBH beta
- **Last updated:** 2026-10-11
- **Owning feature branch/ref:** `fix/upstream-minimal-adapters`
- **Latest immutable recovery checkpoint:** `f92aa79abe0f5fc7c2fd9ea8b9cd4aa0fc203e76`
- **Feature implementation commit(s):** `f92aa79abe0f5fc7c2fd9ea8b9cd4aa0fc203e76`
- **Inspiration / canonical references:** `Sequester-AG/bug-bounty-triage` upstream `main` at `9684e1bfc876e841f9c789f0b258902b43d461e4`; Discord message `1558971123767713803`

## Intent

Restore the full upstream six-phase triage method. Adapt only fork identity, FID report location and optional authored PoC location, and the unavailable agent-email/agent-browser tool interfaces to the approved mail/Chromium skills. Revert the prior fork's evidence-only intake, trial-draft readiness bypass, softened escalation, privacy rewrite, CVSS/verdict redesign, and exclusive-write contract. Do not change the canonical BBH pipeline, real D15 report, target state, or existing PoCs.

## Implemented contract

Retain the original report/description/target intake, live end-to-end validation when authorized, readiness STOP gate, escalation, upstream report template/audits, and chat triage decision. Report to `reports/<FID>/<target-domain>-<vuln-type>-<FID>.md`; optional authored standalone PoC goes in `reports/<FID>/`. Substitute local `mail` and `chromium-test` skills, with `email-access-policy` for selecting an approved identity. No live test or new report is part of this repository change.

## Evidence and review

- Tests and commands: six static contract checks pass with `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`; `git diff --check` passes. Inspect `git diff upstream/main HEAD -- SKILL.md` for the exact upstream-to-fork adapter changes; do not infer substantive changes from the prior fork's commit diff.
- Independent review: REVISE for an ambiguous/mismatched diff-count receipt in this dossier only; skill and README passed the requested upstream-parity review. This receipt was corrected and awaits focused re-review.
- Replay/cohort/fixture evidence: no live target or PoC execution; static contract and direct upstream diff only.
- Merge/ancestry evidence: feature based on clean `origin/main` at `cd2a504`.

## Blockers and deferred work

- **Missing test or evidence:** live end-to-end PoC-validation behavior cannot be demonstrated without a separately authorized scoped finding run.
- **Command / fixture / environment needed:** approved target, owned identities and program rules for such a run.
- **Trigger to run it:** separately requested full-pipeline trial.
- **Why it blocks integration, activation, or promotion:** does not block this textual restoration or standalone fork publication; prevents claiming the live pipeline has run.
- **Next completion step / successor reference:** an owner-selected finding and approved scoped validation assignment if needed.

## Interruption / resume handoff

- **Owning feature branch/ref:** `fix/upstream-minimal-adapters`
- **Latest immutable recovery checkpoint:** `f92aa79abe0f5fc7c2fd9ea8b9cd4aa0fc203e76`
- **Feature implementation commit(s):** `f92aa79abe0f5fc7c2fd9ea8b9cd4aa0fc203e76`
- **Exact resume point:** independently re-review corrected dossier, then merge/push standalone fork main, refresh existing Hoster trial checkout, verify runtime skill links.
- **Working-tree state at handoff:** clean after dossier checkpoint commit.

## Decision gates

- **Integration gate:** exact upstream diff limited to four adapter families; six tests and independent review pass.
- **Activation / cohort gate:** verify Hoster trial checkout and symlinks separately from publication; no canonical BBH integration.
- **Promotion gate:** standalone fork main only; no external upstream PR or BBH beta/main change.

## Decision record

- 2026-10-11 — created from Ryu's narrow-restoration instruction; initial focused static checks pass. Implementation checkpoint `f92aa79abe0f5fc7c2fd9ea8b9cd4aa0fc203e76` is ready for independent review.
- 2026-10-11 — independent review found only the inaccurate/ambiguous line-count receipt in this dossier; removed it without changing the skill, README, or tests. Fresh narrow review pending.
