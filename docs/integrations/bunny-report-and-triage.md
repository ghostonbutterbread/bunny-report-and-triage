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
- Synthetic report-only agent smoke: verified. An agent loaded the feature skill and created only `reports/FID-42/api-fixture-invalid-idor-FID-42.md` from the local-only packet after a first run correctly blocked missing runnable setup. Parent read back the 72-line report, checked the four source SHA-256 hashes against the agent's before/after receipt, verified no `REPORT.md` or `SUBMISSION.md`, and confirmed the report limits its claim to the loopback fixture. The parent separately ran the fixture once to verify A→B and control responses before the report-only invocation; the agent did not run it. No external target action or submission occurred.
- Rereview of `18b7a74` remains pending; publication and runtime projection still gated.
- Origin main descended previous feature tip; `git merge --ff-only origin/main` moved this feature from `6461ee3` to `71df577`, retaining all later fork-main changes rather than restoring obsolete branch content.
- Independent rereview of `bf3a3dd`: REVISE. Its prior symlink and no-report objections were resolved; it found an unconditional ban on private response content inconsistent with specifically approved non-authentication excerpts, and an over-restrictive ledger path rule that excluded BBH's canonical lane-root `ledgers/ledger.json`. The skill now gives one approval-limited, no-live-auth disclosure rule and explicitly permits only the linked canonical ledger lane or synthetic packet-local fixture ledger. Rereview of this correction pending.

## Blockers and deferred work

- **Smoke evidence:** the synthetic report-only agent write succeeded at `reports/FID-42/api-fixture-invalid-idor-FID-42.md`; four source hashes matched before and after. Static tests do not substitute for independent review, installation/provenance, or a real finding proof check.
- **Historical failed CLI attempt:** `codex` was not installed; `claude -p ... --append-system-prompt-file <feature SKILL.md> --allowedTools Read,Write --permission-mode acceptEdits --max-turns 8` failed before any model/tool turn with HTTP 403 `oauth_not_allowed_for_organization`. The later Hermes delegated-agent local-only smoke succeeded; the earlier CLI failure is not an active smoke blocker.
- **Next gate:** independent rereview of `18b7a74`, fresh `origin/main` reconciliation, integration through fork main, then installed-skill provenance/activation validation. No real target needed for these gates.

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
