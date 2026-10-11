# Bunny report-and-triage fork trial

- **Status:** review-ready experimental fork
- **Owner:** Hermes / Ryushe
- **Branch:** `feat/bunny-fid-naming`
- **Base commit:** `9684e1bfc876e841f9c789f0b258902b43d461e4` (upstream main and fork `origin/main` at feature creation)
- **Intended integration target:** `ghostonbutterbread/bunny-report-and-triage` fork `main`, **not** BBH beta/main
- **Last updated:** 2026-10-11
- **Owning feature branch/ref:** `feat/bunny-fid-naming`
- **Latest immutable recovery checkpoint:** `4c291216ca30466f96976eaf67c7df15335ce6ca`
- **Feature implementation commits:** `eec100fd4a347569b8da4858b719e6a8f48b7a5e` (prior standalone adaptation cherry-picked), `4c291216ca30466f96976eaf67c7df15335ce6ca` (name and FID output)
- **Inspiration/canonical references:** Sequester-AG/bug-bounty-triage MIT upstream, BBH `security-reporting` FID packet identity and `bounty-directory-structure-policy` for `_meta` notes.

## Intent

Publish an actual named GitHub fork for an opt-in Hoster report rewrite trial. Keep the upstream triage/report method recognizable, adapt only host browser/mail/privacy boundaries and the experiment's output naming. Do not integrate with BBH reporting policies, Aiskillsync, canonical `SUBMISSION.md`, PoCs, or live testing by default.

## Implemented contract

`$bunny-report-and-triage` takes one absolute `reports/<FID>/REPORT.md` or `SUBMISSION.md` path plus selected evidence. The exact FID is the directory name. It creates one separate, front-door `<FID>-<domain-slug>-<class-slug>-bunny-<UTC>-<unique>.md` in that packet and a matching `_meta/*-TRIAGE.md`; both exclusive-new, never overwriting existing artifacts. FID conflict or absent packet path blocks writing. Report-only mode does not contact a target. A separately authorized live task uses Hoster BBH Chromium Test and Composio mail, not upstream's agent-browser/agent-email.

## Evidence and review

- Tests: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` from the feature worktree: **6 passed** at implementation commit `4c291216ca30466f96976eaf67c7df15335ce6ca`; `git diff --cached --check` passed before commit.
- Independent review: pending. The earlier standalone implementation `5bb4550` had a PASS review and synthetic Codex smoke on Hoster, but the renamed FID output needs fresh review and fresh smoke before deployment.
- GitHub fork creation: GitHub API returned 202 for `ghostonbutterbread/bunny-report-and-triage`; readback returned 200, `fork=true`, parent `Sequester-AG/bug-bounty-triage`, public, main at `9684e1b` before any adaptation push.
- Real report/target: none read, rewritten, or contacted in this task.

## Blockers and deferred work

- **Missing evidence:** independently reviewed naming/path safety and a synthetic output smoke under the selected Hoster skill root.
- **Command/fixture:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`; use a task-owned synthetic `reports/FID-42/REPORT.md` fixture for a Codex report-only invocation after deployment.
- **Trigger:** after reviewer PASS, integration into fork main, remote readback, and Hoster fast-forward or fresh clone.
- **Why:** static text tests cannot prove an agent writes an exclusive FID-prefixed file while preserving original report/PoC.
- **Next:** review, integrate/push fork main, deploy Hoster, run synthetic smoke, verify source hash and only two new files.

## Interruption / resume handoff

- **Owning feature branch/ref:** `feat/bunny-fid-naming`
- **Latest immutable recovery checkpoint:** `4c291216ca30466f96976eaf67c7df15335ce6ca`
- **Feature implementation commits:** `eec100fd4a347569b8da4858b719e6a8f48b7a5e`, `4c291216ca30466f96976eaf67c7df15335ce6ca`
- **Exact resume point:** request fresh independent read-only review of the committed implementation; if accepted, stage merge into fork main and exclude this dossier from the integration tree.
- **Working-tree state:** clean after this dossier is committed.

## Decision gates

- **Integration:** reviewer PASS and tests on the staged fork-main tree; no push to Sequester-AG.
- **Activation:** Hoster checkout verifies fork main SHA, new skill link resolves, synthetic write smoke preserves originals.
- **Promotion:** no BBH/Aiskillsync integration without later explicit Ryushe approval after real report comparison.

## Decision record

- 2026-10-11 — fork created under requested name; FID-prefixed experimental artifact chosen to improve packet-level discoverability without touching canonical stages.
