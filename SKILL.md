---
name: bug-bounty-triage-experiment
description: "Experimentally rewrite and triage one bug bounty report without changing its original."
argument-hint: "<existing report path or text + selected evidence; optional separate live-test assignment>"
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit, Agent, WebFetch, WebSearch]
---

# Bug Bounty Report Triage, Validation & Severity Escalation (Experiment)

This is a **standalone, opt-in report experiment** derived from Sequester-AG/bug-bounty-triage (MIT, upstream revision 9684e1bfc876e841f9c789f0b258902b43d461e4). It does not replace BBH's reporting workflow or require its report-writing skills. Read one supplied report and its selected evidence, produce a separately named experimental rewrite, and compare it with the original. Never edit the source report, evidence, PoC, ledger, or other findings. A report rewrite by itself is read-only: do not access the live target, create accounts, or rerun the PoC unless the operator *separately and explicitly* assigns authorized live validation. A skill invocation is not permission to test. Distinguish observed results from inferences and untested possibilities.

Your goals:
1. **Assess the supplied proof** — In report-only mode, identify which steps were previously observed versus independently reproduced; never claim that you tested them yourself. In a separate authorized live-validation assignment, independently check only the unresolved, safe, in-scope boundary.
2. **Assess** — Is the finding reproducible, meaningful, and supported well enough to submit?
3. **Escalate** — Pursue the highest real, defensible impact and severity.
4. **Ship** — Output a clean **experimental** rewrite without changing the canonical packet. Mark readiness separately; only a fully evidenced rewrite may be considered a submission candidate.

## REPORT AUDIENCE AND INFORMATION DENSITY

Write for a technically capable security triager who understands HTTP, curl or Burp, browser developer tools, redirects, JSON, and common vulnerability concepts. Do not teach standard security tooling or narrate routine actions. Assume the triager has no prior knowledge of the target product, its role model, the affected feature, the reporter's lab, or any custom infrastructure used by the PoC.

- Explain only the product-specific and lab-specific facts needed to reproduce the issue.
- Prefer exact commands, requests, short scripts, paths, and expected outputs over explanatory paragraphs.
- Remove repetition, not operational detail. Reproduction completeness takes priority over brevity.
- A capable triager must not need to guess a target-specific step, invent custom infrastructure, or ask where a required value comes from.

$ARGUMENTS

---

## PHASE 1: INTAKE

Extract from the provided report:

- **Target**: domain, app, API
- **Vuln class**: CWE (IDOR, XSS, SSRF, SQLi, Auth Bypass, etc.)
- **Endpoint**: URL, route, parameter
- **Claimed severity**: Critical / High / Medium / Low
- **PoC**: steps, requests, payloads
- **Claimed impact**: what the reporter says happens
- **Program** (if supplied): platform, program name, relevant constraints
- **Target-specific prerequisites**: product version/build, feature location, required role, and how required authentication values are obtained
- **Custom test infrastructure**: network placement, listeners/services, commands or scripts, ports, and replaceable values

If information needed for a live test is missing, continue analyzing the supplied evidence and ask only for the specific missing input.

## SOURCE FIDELITY AND PRIVACY

Preserve the exact technical facts required to understand the boundary: safe endpoint names, owned fixture identifiers, request shape, effect, and negative controls. **Do not copy credentials, cookies, keys, session/CSRF/OAuth tokens, verification codes, reset links, private request bodies, or unrelated personal data** into the experiment or chat, even when present in the input. Use reviewer-supplied placeholders and explain how the reviewer obtains each value from *their own* account. Keep restricted raw evidence in its existing approved location; do not duplicate it in this experiment. Never invent a result or alter a technical identifier to make it look sanitized. If a decisive claim cannot be substantiated without exposing protected content, mark it unverified and name the blocked proof condition rather than writing a false runnable example.

Before delivery, compare the rewrite against the supplied evidence for accurate safe values and supported claims, and check that no secret or unrelated private data migrated into the new file.

---

## PHASE 2: LIVE END-TO-END TESTING (WHEN APPLICABLE AND AUTHORIZED)

**Report-only experiment (default): skip all live actions in this phase.** Treat the supplied report as a lead, distinguish prior recorded observations from new testing, and state precisely which claim links you cannot verify. Only a separate, explicit, authorized live-testing assignment may proceed below. First confirm current program scope/rules, account ownership, rate, and side effects; stop rather than inventing authorization. If end-to-end testing cannot be completed safely, explain why. Do not claim a test occurred when it did not.

### 2a. Set Up Test Infrastructure

Prefer already approved owned test accounts and fixtures; do not create new ones merely because this report skill was invoked. If a separate live test requires a missing owned role or object, use the program's permitted setup flow and record non-secret account metadata. For approved forwarded verification mail, use the existing authorized **Composio** email connection and its discovered read/search schema; never use `agent-email`, assume an inbox exists, create an arbitrary alias, or expose OTPs in a report. If that connection/identity is unavailable, pause for a secure operator handoff. Do not treat Composio as a disposable inbox creator.

For IDOR/BOLA, role, or auth checks, use only the minimum approved owned attacker/second-role fixtures actually needed by the falsifiable test, not automatically generated pairs.

### 2b. Reproduce the Vulnerability

For an explicitly authorized live task, use BBH's isolated **Chromium Test provisioner**, not `agent-browser` or an interchangeable in-app browser. In Hoster's selected lane, preflight `bbh --root` and `bbh --print-command skills/chromium-test/scripts/browser_provisioner.py`, then request `bbh skills/chromium-test/scripts/browser_provisioner.py request <program> <approved-account> --agent-id <agent-id> --run-id <run-id> --purpose 'bounded report validation' --url <in-scope-url>` inside `/bin/bash -lc` in a **task-owned user-systemd service**. From Ghost, dispatch through the existing `hoster-ssh` user-unit helper; never run the provisioner from bare SSH, where `bbh` may not resolve and the workload belongs to `ssh.service`. On Hoster, use the same task-owned user-service boundary. Use the provisioner's recorded CDP control and task-scoped MITM with a trusted CA. Never invoke `chromium_test.py` directly, borrow another profile, or fall back to shared Caido. Release the browser and finish the task proxy after any bounded replay. If provisioner admission or auth fails, record the blocker rather than launching raw Chrome. Establish the starting state, execute only the safe approved step, and independently verify its effect.

- Start with controlled accounts or records and the required attacker/victim roles when applicable
- Execute the complete path from trigger through observable impact, not just the triggering request
- For state changes, compare before and after state; for data exposure, verify unauthorized access to the actual data; for chains, verify each link
- Check a relevant control when feasible so expected behavior is distinguishable from the vulnerability
- Capture screenshots or browser state at the decisive steps using the chosen browser
- Record the HTTP requests/responses that prove exploitation when the PoC depends on them

For an API-level check, use a browser-captured request followed by bounded replay through that same task MITM where authorized; do not put live authentication in commands, logs, or reports.

If the PoC fails, distinguish changed prerequisites, a patched boundary, a transport/auth blocker, and a negative result. A different payload or adjacent endpoint is a **new** scoped test decision, not an automatic retry. Do not label a finding dead until its stated setup and control are understood.

### 2c. Capture Evidence

For explicitly authorized new testing, preserve only sanitized decisive observations in the task-owned evidence lane and cite them in the experiment. For report-only work, reference existing evidence and label it prior evidence; do not recapture it. Include only shareable excerpts and exact attachment filenames that a triager could access.

When the PoC depends on custom infrastructure, also preserve the minimal runnable command or script used to create it, its required network placement, and the log output that proves the target reached it. A description such as "configure a listener" is not reproducible setup.

---

## PHASE 3: SUBMISSION READINESS

**If the report fails this gate, do not label the experimental rewrite submission-ready.** Keep a clearly marked experimental draft if the user wants to compare style, but do not turn missing proof into certainty.

### Common weak-signal examples — assess against the actual program rules and demonstrated effect, not a universal auto-reject policy:

- Informational only (missing headers, version disclosure, verbose errors with no data leak)
- Best practice violation without exploit (missing rate limit, missing CSP with no XSS)
- Self-XSS with no delivery vector
- Clearly outside current program scope
- Requires victim to do unrealistic things (install malware, paste into console)
- Scanner output with no manual validation
- Theoretical — no working PoC, "could potentially" language
- Already patched behavior without a distinct live security impact (a public CVE alone does not determine eligibility)
- DoS via resource exhaustion where prohibited or unsupported; do not perform load testing to establish severity
- Missing SPF/DKIM/DMARC
- Clickjacking on non-state-changing pages
- CSRF on logout or non-sensitive actions
- Open redirect without chain
- Host header injection without cache poisoning PoC
- User enumeration alone (unless program explicitly accepts it)

### Reproduction-Completeness Gate

A supported vulnerability is not yet submission-ready if a capable triager would have to guess any non-standard setup or target-specific step. Mark it YELLOW until the report includes, where applicable:

- the exact affected product version/build and feature location;
- the minimum required role and a compact explanation of any product-specific role name or numeric role ID;
- how to obtain each target-specific token, cookie, identifier, or other required value;
- the placement and reachability requirements for custom test hosts;
- the shortest runnable command or script for custom listeners or services;
- the decisive request, response, service log, and success condition; and
- a clear indication of which addresses and values the triager must replace with their own.

Do not add tutorials for standard tools. Supply the missing operational fact in the smallest useful form: usually one sentence, one command, or one evidence block.

### Verdict

- **GREEN**: The supplied provenance and any independently verified effect support the vulnerability and impact, with a reproducible PoC and program-compliant scope. In report-only mode, explicitly label testing by this run as **NO** even when past proof is sufficient.
- **YELLOW**: Testing is partial, impact is borderline, or an important link remains unverified. Continue testing or strengthen the evidence.
- **RED**: Current evidence does not support submission. Tell the user why and what would need to change.

Read available current program rules before claiming live-test authority or program acceptance. If private rules are inaccessible, analyze existing evidence but label that policy uncertainty; do not assume absent rules grant permission.

---

## PHASE 4: ESCALATION (MAXIMIZE BOUNTY)

For every confirmed finding, **reason about** material adjacent boundaries: broader controlled role or tenant reach, persistent access, or a credible chain. In report-only mode this is a read-only hypothesis audit, not a test plan to execute. Any separate live escalation needs its own current scope, side-effect, ownership, and class-policy decision; never move to internal infrastructure, third-party data, destructive writes, or account takeover merely to maximize payout. Clearly separate confirmed impact, supported inference, and untested possibilities.

### 4a. Escalation Paths by Vuln Class

Use these as *questions*, not automatic tests. If a separately authorized proof requires a browser, use the Chromium Test provisioner described in Phase 2; only use owned fixtures and the narrowest safe observation.

**IDOR / BOLA**
- Read-only → authorized write on a second **owned** fixture, only if the mutation is safe
- Single record → Broader access (use a bounded set of controlled records to assess whether the pattern generalizes)
- User data → privileged role boundary, only with an approved owned higher-role fixture
- Same-tenant → Cross-tenant (try org/tenant ID swaps)
- Check whether the proven fields imply sensitive-data exposure; do not browse third-party records or assert regulatory impact from field names alone

**XSS**
- Reflected → Stored (inject into fields that persist)
- Alert box → Access to session data or privileged actions (demonstrate with a controlled test account)
- Session access → Full ATO (prove with controlled accounts when possible)
- User context → privileged owned context only when an approved account and safe trigger exist
- XSS → CSRF bypass (use XSS to perform privileged actions)

**SSRF**
- External → potentially different trust boundary; internal hosts/metadata/file schemes are **not** default probes and require separate authorization and safe specialist controls
- Internal service → more severe action is an untested chain until safely proven; do not attempt credential exposure or RCE as an automatic follow-up

**SQL Injection**
- Single column → Broader database access (use bounded queries and controlled records)
- Read → potential write, file, or command capability only as hypothesis; do not modify a live database or export private records to chase severity

**Auth Bypass**
- One owned account → another owned role only if both are approved
- Auth bypass → Persistent access (demonstrate with a controlled test account)
- Auth bypass → MFA bypass

**Privilege Escalation**
- User → Admin
- Read-only → Read-write
- Single function → Full admin panel
- Could security settings be affected on an explicitly destructible owned account? Do not change reusable accounts for triage polish.
- Cross-tenant access?

**Open Redirect**
- Standalone → Chain with OAuth token theft (redirect_uri manipulation)
- Chain with SSO flows → ATO
- Test `javascript:` and `data:` URI schemes

**File Upload**
- Image → possible executable content only if a safe isolated proof is authorized; no live web shell by default
- Upload → Path traversal (directory traversal in filename)
- SVG upload → Stored XSS

### 4b. Chaining

Consider chains as **hypotheses**; do not test each chain live just because it is listed:

1. Info disclosure + IDOR → Proven full exploitation with real IDs
2. Open redirect + OAuth → Token theft → ATO
3. XSS + CSRF → Privileged action execution
4. SSRF + Cloud metadata → Cloud infrastructure takeover
5. Race condition + Financial endpoint → Double-spend / balance manipulation
6. Any bug + Admin access → Maximum impact demonstration

### 4c. CVSS Rescoring

When the program requires CVSS 3.1, score only the demonstrated path and its prerequisites. Authentication affects PR, victim interaction generally affects UI, and cross-tenant access alone does not establish changed Scope. Assign high confidentiality, integrity, or availability impact only when demonstrated. Otherwise follow the program rubric and omit an invented vector or payout estimate.

---

## PHASE 5: GENERATE SUBMISSION REPORT

**Never overwrite the report supplied for this experiment.** For an input file inside a finding packet `reports/<FID>/REPORT.md` or `reports/<FID>/SUBMISSION.md`, create one new run capsule at `reports/<FID>/_runs/triage-experiment-<YYYYMMDDThhmmssZ>-<unique-suffix>/` and write `REWRITE.md` there. Put the internal verdict/side-by-side gap notes in the same capsule's `_meta/TRIAGE.md`; do not edit the canonical `EVIDENCE.md`, `REPORT.md`, `SUBMISSION.md`, PoC, ledger, other findings, or prior run capsules. This is inside the normal report directory but visually and operationally separate. Resolve the input file and the approved packet parent first; reject symlinks in the output path components from that parent onward, verify `_runs` resolves inside that same approved parent, and **create the fresh capsule exclusively** (for example with a single `mkdir` that fails if it exists). Fail closed on collision or any unexpected path; never reuse a prior run capsule. If the input is not in a finding packet, use a user-specified separate output directory or task-owned scratch with the same exclusive-new-capsule rule; never guess the canonical destination. Verify that the output path is distinct from the input before writing. No `finding_submission.py` or other BBH report writer is required.

The report must be:
- **Straight to the point** — No filler, no "I discovered", no narrative storytelling
- **Evidence-heavy** — Every claim backed by request/response or screenshot
- **Max impact framing** — Lead with the worst-case proven impact
- **Self-contained** — A triager can understand and reproduce it without access to the researcher's lab or local files; label readiness accurately outside the file

**Experimental rewrite file:** `REWRITE.md` contains only the proposed report text, not internal triage commentary. It is **not** the canonical submission and is not automatically ready to paste or submit. Keep advice, confidence ratings, program-policy discussion, unverified chains, and comparison notes in `_meta/TRIAGE.md`. Do not include hypothetical impact from a different environment as though observed. When a fact limits the finding or severity, state it briefly in the relevant Summary or Impact sentence and adjust the claim. Do not hide a material limitation.

### Report Template

Use this structure as applicable. Keep setup, execution, and proof together so the report does not repeat the same evidence in separate Steps and PoC sections:

```
## [Specific Vulnerability Title Showing Max Impact]

**Severity**: [program-supported tier, when scored]
**CVSS Vector**: [only when required and evidence supports every metric]
**CWE**: CWE-XXX — [Name]
**Asset**: `[affected URL/endpoint]`

### Summary

[2-3 sentences max. What's broken, what an attacker gets. Lead with impact.]

### Reproduction

Prerequisites: [In one compact paragraph or list, identify the affected version/build, required role, feature location, authentication source, network placement, and replaceable values. Omit facts that are obvious to a security triager.]

Setup: [If custom infrastructure is required, provide the shortest runnable commands or script and the expected startup indication. Omit this label when no custom setup is needed.]

1. [Perform one exact target-specific action. Include the request or command at the step where it is used.]
2. [Show the relevant response or log immediately after the action that produces it.]
3. [State the success condition in one sentence, including expected secure behavior versus the observed result.]

` ` `http
[Raw HTTP request or curl command]
` ` `

` ` `http
[Response proving exploitation]
` ` `

### Impact

[Bullet points. What an attacker achieves. Business terms.]

- [Primary impact — the worst thing that happens]
- [Secondary impact — scope, scale, affected users]
- [Regulatory/compliance impact if applicable]

### Remediation

[1-3 bullet points. Specific fix. No essays.]

- [Primary fix]
- [Alternative mitigation if applicable]
```

### Report Rules

1. **Title**: State the strongest demonstrated impact plainly. For example, use "IDOR in invoice API exposes other tenants' invoices" when the evidence shows that access.
2. **Precise claims**: Use direct language for proven behavior. Label plausible but untested consequences as inferences; do not use certainty to disguise missing proof.
3. **No self-references**: No "I found", "I tested", "during my research". Just state the facts.
4. **Assume security competence, not target familiarity**: Do not explain standard tools or concepts. Do explain the target's feature location, product-specific roles, authentication-value source, custom network placement, and any non-obvious prerequisite in the shortest useful form.
5. **Setup must be executable**: "Configure a listener," "set up a server," or similar prose is insufficient when the PoC depends on custom infrastructure. Provide the minimal runnable command or script, or name an exact attachment and show how to run it.
6. **Placeholders must be actionable**: For every value the triager must replace, state what it represents and where to obtain it. Do not explain obvious substitutions repeatedly.
7. **Keep proof beside the action**: Put decisive requests, responses, and logs directly in the numbered reproduction flow. Do not repeat them in a separate PoC section or restate them in prose.
8. **Steps must not hide work**: Use one numbered action per step when combining actions would make the reader infer missing setup or verification. Replace vague directions such as "authenticate," "capture," or "confirm" with the exact target-specific action.
9. **Impact section leads with the strongest supported escalated impact**, not the base finding. Mark an inference as an inference; never present an untested chain as demonstrated.
10. **Be concise without a word limit**: Remove filler, generic transitions, tutorial text, and repeated evidence. Keep every non-obvious detail needed to reproduce and assess the finding. Prefer a command or evidence block to a paragraph.
11. **Make evidence accessible**: Include decisive request/response excerpts and observations in the report. If an attachment is needed, identify it by the exact attached filename and explain what it proves. Do not rely on local file paths, private lab URLs, or unexplained references unavailable to the triager.
12. **Protect private evidence**: Preserve safe technical values accurately, but replace credentials, live authentication, unrelated private data, and sensitive response content with reviewer-owned placeholders whose source is explained. Do not imply a placeholder was the captured value. Keep restricted originals in their existing approved evidence store only.
13. **Request format**: Raw HTTP and curl are equally acceptable. Choose the format that lets the triager reproduce the request most easily; explain how to obtain authentication from their own account, show safe headers/body, and state substitutions. Never paste a live cookie or token.
14. **Paste test before delivery**: Read the entire report file as if selecting all and pasting it into the submission form. Remove template brackets, drafting instructions, internal caveat blocks, status labels, analyst commentary, local file references, escaped Markdown syntax, HTML spacing entities, and any outer code fence around the report. Keep only submission content and code fences needed for commands, requests, responses, or logs.
15. **Fidelity and privacy test before delivery**: Compare the rewrite against supplied evidence for accurate non-secret endpoint, request, observation, and negative-control facts; require explicit value-source instructions for each placeholder. Check that no credential, secret, unrelated PII, or private raw response was copied. Do not silently strengthen the claim or overwrite the original.

### Knowledge-Assumption Audit

Before delivery, read only the submission file as a capable triager unfamiliar with the target and the reporter's lab. Block delivery if any answer is no:

- Can the reader obtain every required product-specific value from the report?
- Can the reader create every custom listener or service without inventing code or configuration?
- Is the required role, feature location, and network placement clear without product research?
- Does each decisive action have an adjacent success signal in a response, log, or state check?
- Can the reader distinguish fixed evidence values from values they must replace?
- Has duplicated explanation been removed while all non-obvious operational detail remains?

If essential information is missing from the supplied evidence and cannot be established during authorized testing, do not invent it or pad the report with prose. Mark the report not ready and request the exact missing detail.

Write the experiment to the new run capsule's `REWRITE.md` using the available file-writing tool. Record the source report path and a non-secret change/readiness summary in `_meta/TRIAGE.md`. Verify that both new files exist and that the input report and PoC were not modified. Give the user both absolute paths and a short comparison summary; never say it was submitted.

---

## PHASE 6: TRIAGE DECISION

After writing the experimental report, put this summary in `_meta/TRIAGE.md` and give a compact version in chat. Never append it to `REWRITE.md`:

```
TRIAGE DECISION
═══════════════
Tested:      [NO — report-only source review / YES or PARTIAL — only if this run performed separately authorized testing]
Validation:  [CONFIRMED / PARTIALLY CONFIRMED / UNVERIFIED / NOT REPRODUCIBLE]
Submission:  [GREEN / YELLOW / RED]
Severity:    [Original] → [Escalated]
CVSS:        [only when required and evidence-supported]
Confidence:  [HIGH / MEDIUM / LOW]
Action:      [REVIEW CANDIDATE / STRENGTHEN / DO NOT SUBMIT]
Report:      <absolute path to the experiment's REWRITE.md>
```

If RED: explain what's wrong and what would fix it.
If YELLOW: explain what's borderline and whether escalation helped.
If GREEN: say the rewrite is a candidate for review; do not imply the original was replaced or a platform submission occurred.

---

## RULES

1. **Read-only by default.** Do not run a target interaction during a rewrite. For a separately authorized live validation task, independently verify the smallest safe boundary and effect; otherwise assess the existing provenance, label unverified links, and say this run did not test. Never label a finding confirmed solely because the draft asserts it.

2. **Do not submit from this skill.** A triage verdict and experimental rewrite are not platform submission or promotion to the canonical report.

3. **Escalation is not fabrication.** Only claim impact you proved or that logically follows from confirmed behavior.

4. **Reuse approved owned fixtures.** Do not create accounts or use email during report-only rewriting. If a separate live task needs verification mail, use the authorized Composio connection only for the approved mailbox.

5. **The experimental file is the deliverable.** For a packet input, output a new `REWRITE.md` under the approved packet's exclusively created `_runs/triage-experiment-.../`; for non-packet input, use the separately specified directory or task-owned scratch from Phase 5. Never touch the source report/PoC. For a finding with missing proof, retain only supported claims and name the gaps in the separate `_meta/TRIAGE.md`; do not call the rewrite submission-ready.

6. **Max impact, honest framing.** Reason about credible escalation paths, but claim only the strongest demonstrated impact. Separate untested chains and material limits in the triage note. Do not launch new probes for severity during a report-only experiment.

7. **Dense reports win.** Triage teams skim. Front-load impact, use executable evidence instead of narration, and remove repetition. Never shorten a report by omitting a non-obvious prerequisite, target-specific action, value source, or success condition.

8. **One vuln per report** unless bugs chain together for compound impact.

9. **If prior proof fails a consistency check, say so.** A report-only rewrite cannot establish that a live finding is patched or dead; label what the evidence can and cannot support.

10. **Use existing shareable evidence.** The rewrite should contain only decisive sanitized proof or exact accessible attachment names; never duplicate restricted raw traffic or secret-bearing screenshots in the new run capsule.
