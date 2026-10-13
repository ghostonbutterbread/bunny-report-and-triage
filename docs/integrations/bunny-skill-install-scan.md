# Bunny skill installation scan repair

- Branch/worktree: `fix/bunny-skill-install-scan`, `/home/ryushe/worktrees/bunny-skill-install-scan`
- Base/intended target: published fork `main` at `5565c8d4cb09d325a149604f393c22349d96939c`
- Finding: `hermes skills install` on immutable `SKILL.md` URL returned DANGEROUS and blocked a community skill because a hypothetical SSRF example names a sensitive system file. The actual report-only route was independently reviewed and smoke-tested; this is installation wording, not authorization to run SSRF probes.
- Repair: replace the incidental file path example with an authorization-bounded scheme-expansion hypothesis. Do not bypass scanner or alter report-only gates.
- Verification gate: fork contract suite, `git diff --check`, fresh install scan of the exact candidate skill, independent review, then fork-main integration/push/readback. Activation is separate.
- Resume: run the scan against the repaired skill before integration. Remove this temporary dossier from main in the integration operation.
