# Bunny FID evidence intake integration dossier

- **Status:** feature committed, review and synthetic smoke pending
- **Owner:** Hermes / Ryushe
- **Branch:** `feat/bunny-fid-naming`
- **Base commit:** `71df577bfa52f46d767032acb2073ca2452b2e0b` (fetched `origin/main`, fast-forwarded from `6461ee3`)
- **Intended integration target:** `ghostonbutterbread/bunny-report-and-triage` fork `main` (`origin/main`), not BBH beta/main
- **Last updated:** 2026-10-13
- **Owning feature branch/ref:** `feat/bunny-fid-naming`
- **Latest immutable recovery checkpoint:** `1ba3f0a4fdfc34469d1f0d62a9a607e56b3e13a5`
- **Feature implementation commit(s):** `1ba3f0a4fdfc34469d1f0d62a9a607e56b3e13a5`
- **References:** prior branch dossier at `6461ee3`, BBH `security-reporting` EVIDENCE packet contract, upstream report filename with exact FID suffix

## Intent and implemented contract

The fork accepts an absolute `reports/<FID>/EVIDENCE.md` as the default report source plus its linked ledger identity and exact proof pointers. It requires a populated `Verified: ...` claim and resolvable evidence index with decisive effect proof; an empty scaffold, conflicting FID, unsupported claim, or missing proof blocks report creation. Existing `REPORT.md` and `SUBMISSION.md` remain selectable legacy inputs, never new outputs. Report-only mode performs no target interaction or PoC execution. The only new report is `reports/<FID>/<target-domain>-<vuln-type>-<FID>.md`, with exact FID case/punctuation, exclusive creation, and no canonical report/ledger/PoC edit. A separate live assignment remains explicitly gated.

## Evidence and review

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`: 17/17 pass on worktree before commit.
- `git diff --check`: pass.
- Origin main descended previous feature tip; `git merge --ff-only origin/main` moved this feature from `6461ee3` to `71df577`, retaining all later fork-main changes rather than restoring obsolete branch content.
- Independent no-edit review: pending. No live target or real finding used.

## Blockers and deferred work

- **Missing evidence:** a synthetic report-only *agent invocation* producing the exact FID-named file while leaving a synthetic source unchanged; static text-contract tests do not exercise agent judgment or writes.
- **Command/fixture:** synthetic `reports/FID-42/EVIDENCE.md`, `proof/observation.md`, and mock `ledger.jsonl` under `/home/ryushe/.hermes/profiles/bugfix/cache/scratch/bunny-fid-smoke/`; invoke the installed fork skill in report-only mode, then compare hashes and file list. A pending-scaffold negative fixture should produce no report. `codex` was not installed; `claude -p ... --append-system-prompt-file <feature SKILL.md> --allowedTools Read,Write --permission-mode acceptEdits --max-turns 8` was attempted on the synthetic fixture but failed before any model/tool turn with HTTP 403 `oauth_not_allowed_for_organization` (zero input/output tokens, no artifact). This is not a successful smoke.
- **Trigger:** once a capable authenticated agent CLI and isolated skill projection are available, before fork-main activation; never use a real target for this smoke.
- **Next:** independent review and synthetic invocation, reconcile a fresh `origin/main`, integrate through fork main only on owner approval, test/read back/publish there, then decide activation separately. Do not merge or push from this subtask.

## Interruption / resume handoff

- **Owning feature branch/ref:** `feat/bunny-fid-naming`
- **Latest immutable recovery checkpoint:** `1ba3f0a4fdfc34469d1f0d62a9a607e56b3e13a5`
- **Feature implementation commit(s):** `1ba3f0a4fdfc34469d1f0d62a9a607e56b3e13a5`
- **Exact resume point:** review committed diff and run synthetic agent invocation when available; no merge/push authorized here.
- **Working-tree state at handoff:** expected clean after commit.

## Decision gates

- **Integration:** independent review and fresh main reconciliation; preserve main's current PoC/report formatting and remove this temporary dossier from target merge tree.
- **Activation:** installed skill provenance and synthetic packet write smoke after integration, separate from code publication.
- **Promotion:** no BBH policy or runtime activation implied.

## Decision record

- 2026-10-13 — resumed prior FID branch at current fork-main tip; added EVIDENCE-led, ledger-backed report-only intake while preserving exact FID output and legacy inputs.
