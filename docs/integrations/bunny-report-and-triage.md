# Bunny report-and-triage fork trial

- **Status:** reviewed experimental fork, integration pending
- **Owner:** Hermes / Ryushe
- **Branch:** `feat/bunny-fid-naming`
- **Base commit:** `9684e1bfc876e841f9c789f0b258902b43d461e4` (upstream main and fork `origin/main` at feature creation)
- **Intended integration target:** `ghostonbutterbread/bunny-report-and-triage` fork `main`, **not** BBH beta/main
- **Last updated:** 2026-10-11
- **Owning feature branch/ref:** `feat/bunny-fid-naming`
- **Latest immutable recovery checkpoint:** `38cd164a0e0d9ceb25b7e2873538805c43a6a80b`
- **Feature implementation commits:** `eec100fd4a347569b8da4858b719e6a8f48b7a5e` (prior standalone adaptation cherry-picked), `4c291216ca30466f96976eaf67c7df15335ce6ca` (name and superseded FID-prefix output), `516c08f917156dd2ae038e6c17f6302650df8b24` (upstream basename + FID suffix), `38cd164a0e0d9ceb25b7e2873538805c43a6a80b` (paired-write failure path)
- **Inspiration/canonical references:** Sequester-AG/bug-bounty-triage MIT upstream, BBH `security-reporting` FID packet identity and `bounty-directory-structure-policy` for `_meta` notes.

## Intent

Publish an actual named GitHub fork for an opt-in Hoster report rewrite trial. Keep the upstream triage/report method and exact domain-class filename convention, changing its destination to the FID packet and appending the exact FID. Do not integrate with BBH reporting policies, Aiskillsync, canonical `SUBMISSION.md`, PoCs, or live testing by default.

## Implemented contract

`$bunny-report-and-triage` takes one absolute `reports/<FID>/REPORT.md` or `SUBMISSION.md` path plus selected evidence. The exact FID is the directory name. It creates one separate, front-door `<target-domain>-<vuln-type>-<FID>.md` in that packet, preserving upstream's filename except for the appended FID, and a matching `_meta/*-TRIAGE.md`; both exclusive-new, never overwriting existing artifacts or silently suffixing a collision. The approved `reports` parent must be real, not a symlink; both filenames are preflighted, the note precedes the report, and partial failure cleans up only identity-proven task-created files. FID conflict or absent packet path blocks writing. Report-only mode does not contact a target. A separately authorized live task uses Hoster BBH Chromium Test and Composio mail, not upstream's agent-browser/agent-email.

## Evidence and review

- Tests: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` from the feature worktree: **6 passed** at corrected implementation commit `38cd164a0e0d9ceb25b7e2873538805c43a6a80b`; `git diff --cached --check` passed before commit.
- Independent review: first review of superseded `4c29121` returned REVISE for partial two-file failure and symlinked `reports` parent; addressed by `38cd164a`. Fresh read-only review of implementation `38cd164a` at dossier tip `9d3cdd2` returned **PASS**, confirming the upstream basename plus exact FID suffix, paired-write safety, no canonical edits, and isolated 6/6 static tests. The earlier standalone implementation `5bb4550` had a synthetic Codex smoke on Hoster; it does not substitute for a fresh FID-suffix write smoke.
- GitHub fork creation: GitHub API returned 202 for `ghostonbutterbread/bunny-report-and-triage`; readback returned 200, `fork=true`, parent `Sequester-AG/bug-bounty-triage`, public, main at `9684e1b` before any adaptation push.
- Real report/target: none read, rewritten, or contacted in this task.

## Blockers and deferred work

- **Missing evidence:** independently reviewed naming/path safety and a synthetic output smoke under the selected Hoster skill root.
- **Command/fixture:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`; use a task-owned synthetic `reports/FID-42/REPORT.md` fixture for a Codex report-only invocation after deployment.
- **Trigger:** after reviewer PASS, integration into fork main, remote readback, and Hoster fast-forward or fresh clone.
- **Why:** static text tests cannot prove an agent writes an exclusive upstream-style filename with exact FID suffix while preserving the original report/PoC.
- **Next:** review, integrate/push fork main, deploy Hoster, run synthetic smoke, verify source hash and only two new files.

## Interruption / resume handoff

- **Owning feature branch/ref:** `feat/bunny-fid-naming`
- **Latest immutable recovery checkpoint:** `38cd164a0e0d9ceb25b7e2873538805c43a6a80b`
- **Feature implementation commits:** `eec100fd4a347569b8da4858b719e6a8f48b7a5e`, `4c291216ca30466f96976eaf67c7df15335ce6ca` (superseded naming), `516c08f917156dd2ae038e6c17f6302650df8b24` (FID suffix), `38cd164a0e0d9ceb25b7e2873538805c43a6a80b` (paired-write safety)
- **Exact resume point:** request fresh independent read-only review of the committed implementation; if accepted, stage merge into fork main and exclude this dossier from the integration tree.
- **Working-tree state:** clean after this dossier is committed.

## Decision gates

- **Integration:** reviewer PASS and tests on the staged fork-main tree; no push to Sequester-AG.
- **Activation:** Hoster checkout verifies fork main SHA, new skill link resolves, synthetic write smoke preserves originals.
- **Promotion:** no BBH/Aiskillsync integration without later explicit Ryushe approval after real report comparison.

## Decision record

- 2026-10-11 — fork created under requested name. Initial FID-prefixed/bunny-timestamp artifact was superseded by Ryushe's correction: preserve the upstream `<target-domain>-<vuln-type>` basename and append the exact FID before `.md` in `reports/<FID>/`.
- 2026-10-11 — independent exact-tree re-review PASS on `38cd164a`; integrate only after staging exclusion of this branch-only dossier and rerunning tests, then activate on Hoster with a synthetic packet smoke.
