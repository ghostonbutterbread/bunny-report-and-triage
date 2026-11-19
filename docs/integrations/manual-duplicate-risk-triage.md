# Manual duplicate-risk triage integration

- Objective: consult the program's manually maintained duplicate intelligence in the chat-only triage decision, independently of proof and submission readiness.
- Base: `origin/beta` at `1711f029aecdc5feec8242600e8b93d2da2f34e6`; branch `feat/manual-duplicate-risk-triage`; target `beta`.
- Contract: read the local optional `duplicate-intelligence.md`; preserve source/date, scope granularity and root-cause limits; use UNKNOWN for absent, stale or inadequate information; never put internal triage in the submission or contact the target in report-only mode. The bugfix profile already has a risk line and must retain its independent local changes.
- Verification: focused contract test was red before the feature; `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` passed 25 tests.
- Blockers / next: run all skill contract checks, obtain independent cross-repository review, integrate reviewed beta only, then verify actual provider links and reconcile the active bugfix profile copy without overwriting unrelated changes.
- Activation: feature only; no stable promotion or remote publication.
