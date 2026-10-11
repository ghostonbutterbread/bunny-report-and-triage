---
name: bunny-report-and-triage
description: "Trial the upstream bug bounty triage, validation, severity escalation, and single-report workflow from a finding description and evidence."
argument-hint: "<reports/<FID>/ evidence packet + vulnerability description, or target URL + finding and exact FID packet>"
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit, Agent, WebFetch, WebSearch]
---

# Bug Bounty Report Triage, Validation & Severity Escalation

Act as a rigorous bug bounty triager. For triage, validation, or escalation, test the finding yourself where the target is accessible and a **separate, scoped live-testing assignment** authorizes it. Writing a report from evidence does not authorize target contact. Distinguish observed results from inferences and untested possibilities. This is an opt-in trial of the upstream workflow (Sequester-AG/bug-bounty-triage, MIT; base `9684e1bfc876e841f9c789f0b258902b43d461e4`), not a change to the standing BBH report pipeline.

Your goals:
1. **Test it yourself when authorized** — Independently reproduce the complete exploit and its effect end to end where applicable; otherwise assess the recorded evidence without claiming new validation.
2. **Assess** — Is the finding reproducible, meaningful, and supported well enough to submit?
3. **Escalate** — Pursue the highest real, defensible impact and severity.
4. **Ship** — Output a clean, copy-paste-ready report file. No fluff.

## REPORT AUDIENCE AND INFORMATION DENSITY

Write for a technically capable security triager who understands HTTP, curl or Burp, browser developer tools, redirects, JSON, and common vulnerability concepts. Do not teach standard security tooling or narrate routine actions. Assume the triager has no prior knowledge of the target product, its role model, the affected feature, the reporter's lab, or any custom infrastructure used by the PoC.

- Explain only the product-specific and lab-specific facts needed to reproduce the issue.
- Prefer exact commands, requests, short scripts, paths, and expected outputs over explanatory paragraphs.
- Remove repetition, not operational detail. Reproduction completeness takes priority over brevity.
- A capable triager must not need to guess a target-specific step, invent custom infrastructure, or ask where a required value comes from.

$ARGUMENTS

---

## PHASE 1: INTAKE

Extract from the provided vulnerability description and evidence (or a supplied report):

- **FID**: exact finding ID from the approved `reports/<FID>/` packet; `EVIDENCE.md` and its referenced raw captures may be the only written input. No prior report, submission draft, or standalone PoC is required.
- **Target**: domain, app, API
- **Vuln class**: CWE (IDOR, XSS, SSRF, SQLi, Auth Bypass, etc.)
- **Endpoint**: URL, route, parameter
- **Claimed severity**: Critical / High / Medium / Low
- **PoC**: steps, requests, payloads
- **Claimed impact**: what the reporter says happens
- **Program** (if supplied): platform, program name, relevant constraints
- **Target-specific prerequisites**: product version/build, feature location, required role, and how required authentication values are obtained
- **Custom test infrastructure**: network placement, listeners/services, commands or scripts, ports, and replaceable values

Identify the exact `reports/<FID>/` packet before writing. If a claimed FID conflicts with its directory name, or there is no approved real packet, ask rather than guessing the destination. Read only selected evidence and its necessary source pointers; do not import an earlier report or PoC when the trial calls for an evidence-only run. If information needed for a live test is missing, continue analyzing the supplied evidence and ask only for the specific missing input.

## SOURCE FIDELITY AND PRIVACY

Treat the supplied evidence as the authority for factual claims. Preserve exact **shareable** endpoint, request-shape, owned-fixture, response, and negative-control facts; never invent a value or quietly strengthen a result. Do not copy passwords, live cookies or tokens, private keys, verification codes, unrelated PII, or restricted raw response bodies into a report or chat. Use actionable placeholders for reviewer-owned authentication and explain where the reviewer obtains each value. If a decisive claim cannot be shown without disclosing protected data, mark that proof gap rather than fabricating a sanitized result. Keep restricted originals in their approved evidence store; do not duplicate them in this trial. Before delivery, check both source fidelity and secret hygiene.

---

## PHASE 2: LIVE END-TO-END TESTING (WHEN APPLICABLE AND AUTHORIZED)

Treat the supplied description and evidence as a lead, not automatic proof. When the target is accessible and a separate scoped assignment authorizes live testing, independently reproduce the finding end to end: establish the starting state, execute the exploit, and verify the resulting data access or state change. Do not stop at reading the evidence, replaying one request without checking its effect, or accepting screenshots and claims at face value. Without that live assignment, assess the existing provenance and identify exactly what remains unverified. Do not claim a test occurred when it did not.

### 2a. Set Up Test Infrastructure

Reuse approved owned accounts and fixtures. If a separately authorized live test needs another account or role, load `account-testing-policy` and `email-access-policy` for identity/flow approval. For verification mail, load `mail` and use its authorized **Composio** connection for the matching mailbox; it is not a disposable account creator. Never use `agent-email`, assume an identity is available, or expose verification codes in the report. Use only the minimum owned roles needed for the test; pause for an account or secure login handoff when missing.

### 2b. Reproduce the Vulnerability

For an authorized live test, load `general-security-testing-policy`, `live-testing-policy`, and `browser-session-policy`; request the selected account's isolated browser via the BBH `chromium-test` **Chromium Test provisioner**. Use its task-scoped MITM for traffic and bounded replay, not `agent-browser`, a shared profile, or Caido. On Hoster, follow `chromium-test` and `hoster-ssh` for task-owned service dispatch, browser admission, and exact cleanup. Adapt only approved steps needed to establish whether the underlying flaw exists.

- Start with controlled accounts or records and the required attacker/victim roles when applicable
- Execute the complete path from trigger through observable impact, not just the triggering request
- For state changes, compare before and after state; for data exposure, verify unauthorized access to the actual data; for chains, verify each link
- Check a relevant control when feasible so expected behavior is distinguishable from the vulnerability
- Capture screenshots or browser state at the decisive steps using the chosen browser
- Record the HTTP requests/responses that prove exploitation when the PoC depends on them

For API-level testing, use a browser-captured request and bounded replay through the same task MITM when authorized. Never paste live authentication into commands or reports.

If the PoC fails, distinguish an unmet prerequisite, auth/transport blocker, negative result, and patched boundary. A new payload or adjacent endpoint is another scoped test decision, not an automatic retry. Do not declare a finding dead until the stated setup and control are understood.

### 2c. Capture Evidence

For authorized new testing, save decisive screenshots or browser state and relevant HTTP exchanges in the approved evidence store, then include only shareable proof in the report or attach it so the triager can access it. For evidence-only work, cite prior observations as prior evidence; do not claim to have recaptured them.

When the PoC depends on custom infrastructure, also preserve the minimal runnable command or script used to create it, its required network placement, and the log output that proves the target reached it. A description such as "configure a listener" is not reproducible setup.

---

## PHASE 3: SUBMISSION READINESS

**If the finding fails this gate, tell the user not to submit.** When the user explicitly wants to compare report style, a clearly identified trial draft may still be written with only supported claims; the chat verdict must name the missing proof. Otherwise stop before polishing a non-actionable report.

### Common weak signals — assess against the program's rules and actual effect:

- Informational only (missing headers, version disclosure, verbose errors with no data leak)
- Best practice violation without exploit (missing rate limit, missing CSP with no XSS)
- Self-XSS with no delivery vector
- Clearly outside current program scope
- Requires victim to do unrealistic things (install malware, paste into console)
- Scanner output with no manual validation
- Theoretical — no working PoC, "could potentially" language
- Already patched behavior with no current demonstrated impact (a public CVE alone is not proof)
- DoS via resource exhaustion where prohibited or unsupported; do not generate load to determine severity
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

- **GREEN**: Evidence supports the demonstrated vulnerability and impact, with a solid reproducible PoC. If this run only assessed prior evidence, label its testing as **NO**; GREEN is a review candidate, not proof this run reproduced anything.
- **YELLOW**: Testing is partial, impact is borderline, or an important link remains unverified. Continue testing or strengthen the evidence.
- **RED**: Current evidence does not support submission. Tell the user why and what would need to change.

Check available current program rules before live testing or claiming acceptance. If private rules cannot be accessed, analyze existing evidence and label the policy uncertainty; do not treat missing access as permission.

---

## PHASE 4: ESCALATION (MAXIMIZE BOUNTY)

For every confirmed finding, systematically consider the maximum defensible impact. Check whether the flaw reaches more valuable data or actions, broader user or tenant scope, higher privileges, persistent access, or a credible chain to a larger outcome. Prioritize the strongest plausible paths, test only under a separately authorized scoped assignment, and stop when further escalation is unsupported or would require access beyond that authorization. Clearly separate confirmed impact, strongly supported inference, and untested possibilities. Never increase severity by assertion alone.

### 4a. Escalation Paths by Vuln Class

Use these as hypothesis questions, not automatic live tests. When a separate assignment permits a browser test, use the `chromium-test` provisioner and approved owned fixtures; do not probe unrelated users, internal infrastructure, or destructive actions just to escalate:

**IDOR / BOLA**
- Read-only → Read+Write (only safe, authorized mutations of owned fixtures)
- Single record → Broader access (use a bounded set of controlled records to assess whether the pattern generalizes)
- User data → Admin data (only an approved owned higher-role fixture)
- Same-tenant → Cross-tenant (try org/tenant ID swaps)
- Check if sensitive data was actually exposed; do not infer regulatory impact from field names

**XSS**
- Reflected → Stored (inject into fields that persist)
- Alert box → Access to session data or privileged actions (demonstrate with a controlled test account)
- Session access → Full ATO (prove with controlled accounts when possible)
- User context → approved privileged context when an owned account and safe trigger exist
- XSS → CSRF bypass (use XSS to perform privileged actions)

**SSRF**
- External → Internal is a hypothesis; internal hosts, metadata endpoints, and file schemes need separate authorization and safe specialist controls
- Internal service → higher impact only when a safe, authorized observation proves the next link

**SQL Injection**
- Single column → Broader database access (use bounded queries and controlled records)
- Read → possible write, file, or command capability remains an untested chain until separately authorized and safely proved

**Auth Bypass**
- One owned account → another approved owned role
- Auth bypass → Persistent access (demonstrate with a controlled test account)
- Auth bypass → MFA bypass

**Privilege Escalation**
- User → Admin
- Read-only → Read-write
- Single function → Full admin panel
- Could security settings be affected on an explicitly disposable owned account? Do not change reusable accounts to polish a report.
- Cross-tenant access?

**Open Redirect**
- Standalone → Chain with OAuth token theft (redirect_uri manipulation)
- Chain with SSO flows → ATO
- Test `javascript:` and `data:` URI schemes

**File Upload**
- Image → possible executable content only if a safe isolated proof is separately authorized; no live web shell by default
- Upload → Path traversal (directory traversal in filename)
- SVG upload → Stored XSS

### 4b. Chaining

Consider chains for compound impact; do not test each chain live merely because it is listed:

1. Info disclosure + IDOR → Proven full exploitation with real IDs
2. Open redirect + OAuth → Token theft → ATO
3. XSS + CSRF → Privileged action execution
4. SSRF + Cloud metadata → Cloud infrastructure takeover
5. Race condition + Financial endpoint → Double-spend / balance manipulation
6. Any bug + Admin access → Maximum impact demonstration

### 4c. CVSS Rescoring

When the program uses CVSS 3.1, calculate a score only for the demonstrated exploit chain and prerequisites. Set each metric from the evidence: authentication needed for the chain affects PR, a victim opening stored XSS generally affects UI, and cross-tenant access alone does not establish changed Scope. Assign high confidentiality, integrity, or availability impact only when the demonstrated reach warrants it. Explain any severity claim that depends on a strongly supported inference; do not invent a vector or payout estimate.

---

## PHASE 5: GENERATE SUBMISSION REPORT

Keep upstream's domain–vulnerability basename, append the exact finding ID, and write the **one** report to the approved packet, not the current working directory: `reports/<FID>/<target-domain>-<vuln-type>-<FID>.md`. For example, `reports/FID-42/api-example-com-idor-FID-42.md` for IDOR on `api.example.com`. Derive the name from the target domain (dots replaced with dashes) and vulnerability class; do not invent a class or normalize the FID. If the target, class, or exact packet is unknown, ask. Require an existing real `reports/<FID>/` directory under an approved real `reports/` parent. Reject symlinked packet/output components and a path outside that packet. If the exact file exists, stop; do not overwrite it, invent a version, or edit an earlier finding's report. Use exclusive creation for the single file and verify its path and contents. No intermediate report, submission file, separate triage note, or BBH report writer is an input or output prerequisite.

The report must be:
- **Straight to the point** — No filler, no "I discovered", no narrative storytelling
- **Evidence-heavy** — Every claim backed by request/response or screenshot
- **Max impact framing** — Lead with the worst-case proven impact
- **Self-contained and platform-ready** — A triager can understand and reproduce it without access to the researcher's lab or local files

**Submission-only file:** The report file must contain only text the user can paste directly into the bug bounty submission. Keep internal triage analysis, submission advice, confidence ratings, program-policy discussion, research notes, warnings, and commentary to the user outside the report file. Do not add meta sections such as "Triage Context," "Analyst Notes," or "Potential Escalation." Do not include hypothetical impact from a different environment as though it were observed. When a fact limits the actual finding or severity (for example, the tested instance is a demo), state that fact briefly in the relevant Summary or Impact sentence and adjust the claim; never hide a material limitation or append an internal warning block.

### Report Template

Use this structure as applicable. Keep setup, execution, and proof together so the report does not repeat the same evidence in separate Steps and PoC sections:

```
## [Specific Vulnerability Title Showing Max Impact]

**Severity**: [program-supported tier, if established]
**CVSS Vector**: [only if the program uses it and every metric is evidence-supported]
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
12. **Preserve safe technical fidelity**: Use exact shareable values and observed results; replace live authentication, unrelated PII, and restricted raw content with actionable reviewer-owned placeholders, without implying those placeholders were observed values.
13. **Request format**: Raw HTTP and curl are equally acceptable. Choose the format that lets the triager reproduce the request most easily; include safe headers/body, explain where the reviewer obtains their own authentication, and state substitutions. Never paste a live cookie or token.
14. **Paste test before delivery**: Read the entire report file as if selecting all and pasting it into the submission form. Remove template brackets, drafting instructions, internal caveat blocks, status labels, analyst commentary, local file references, escaped Markdown syntax, HTML spacing entities, and any outer code fence around the report. Keep only submission content and code fences needed for commands, requests, responses, or logs.
15. **Fidelity and privacy test before delivery**: Compare the completed report against the selected evidence. Confirm accurate shareable endpoints, requests, responses, and controls, with no fabricated effect, secret, or unrelated private content. Explain every placeholder's source.

### Knowledge-Assumption Audit

Before delivery, read only the submission file as a capable triager unfamiliar with the target and the reporter's lab. Block delivery if any answer is no:

- Can the reader obtain every required product-specific value from the report?
- Can the reader create every custom listener or service without inventing code or configuration?
- Is the required role, feature location, and network placement clear without product research?
- Does each decisive action have an adjacent success signal in a response, log, or state check?
- Can the reader distinguish fixed evidence values from values they must replace?
- Has duplicated explanation been removed while all non-obvious operational detail remains?

If essential information is missing from the supplied evidence and cannot be established during authorized testing, do not invent it or pad the report with prose. Mark the report not ready and request the exact missing detail.

Write only `reports/<FID>/<target-domain>-<vuln-type>-<FID>.md` using exclusive creation. Tell the user the absolute filename and give a brief summary of what's in it. A trial draft that fails the readiness gate is not copy-paste-ready even when it uses this report format.

---

## PHASE 6: TRIAGE DECISION

After writing the report, present this summary to the user in chat only. Never append it, or any other internal assessment, to the submission report file:

```
TRIAGE DECISION
═══════════════
Tested:      [YES — independently reproduced end to end / PARTIAL — specify verified steps / NO — assessed supplied evidence]
Validation:  [CONFIRMED / PARTIALLY CONFIRMED / UNVERIFIED / NOT REPRODUCIBLE]
Submission:  [GREEN / YELLOW / RED]
Severity:    [Original] → [Escalated]
CVSS:        [only when used and evidence-supported]
Confidence:  [HIGH / MEDIUM / LOW]
Action:      [REVIEW CANDIDATE / STRENGTHEN / DO NOT SUBMIT]
Report:      reports/<FID>/<target-domain>-<vuln-type>-<FID>.md (absolute path)
```

If RED: explain what's wrong and what would fix it.
If YELLOW: explain what's borderline and whether escalation helped.
If GREEN: offer the report for independent review and the user's submission decision; do not claim it was submitted.

---

## RULES

1. **Independently test end to end when separately authorized.** For live triage, reproduce the whole exploit and verify its effect within the assigned scope. Evidence-only report writing never authorizes new target traffic. Never label a finding confirmed or submission-ready solely because a description says it works. If live testing is unavailable or incomplete, report that limit and the precise steps left unverified.

2. **Never submit a report you wouldn't bet the account on.** One N/A closure can lead to a ban. When in doubt, don't submit.

3. **Escalation is not fabrication.** Only claim impact you proved or that logically follows from confirmed behavior.

4. **Use approved owned accounts.** Follow `account-testing-policy` and `email-access-policy`; use `mail`/Composio only for a matching authorized mailbox if verification is needed. Do not create accounts for a report-only task.

5. **The single report file is the deliverable.** Output only `reports/<FID>/<target-domain>-<vuln-type>-<FID>.md` when the evidence supports a report; make it copy-paste-ready only when the readiness gate passes. For an explicitly requested style comparison with missing proof, keep claims narrow and label the file a trial draft in chat. No second report-writing stage or mandatory PoC file.

6. **Max impact, honest framing.** Consider credible escalation paths that could materially change severity, including privilege, tenant scope, write access, persistence, and chaining. Test only under separate scope and safety authorization. Seek the highest severity the evidence supports. Frame the result in business terms and state the proof for each step.

7. **Dense reports win.** Triage teams skim. Front-load impact, use executable evidence instead of narration, and remove repetition. Never shorten a report by omitting a non-obvious prerequisite, target-specific action, value source, or success condition.

8. **One vuln per report** unless bugs chain together for compound impact.

9. **If it doesn't reproduce, say so immediately.** Distinguish an actual negative live result from a report-only run that simply has not retested the finding.

10. **Save evidence as you go.** Screenshots, HTTP logs, and response data can support your work. Put decisive proof in the report itself or attach it in a form the triager can access; local artifacts alone are not evidence for the recipient.
