---
name: rfp-review
description: >-
  Use this skill whenever the user wants to REVIEW, AUDIT, or QA-check an
  existing RFP response package — not just write one. Triggers include: "review
  my RFP response", "check if our proposal covers everything", "validate our
  bid", "QA the proposal", "does our response match the RFP", "review the deck
  and the doc", "check the language consistency", "are all sections aligned",
  "check for inconsistencies", "is our messaging consistent", "final check
  before submission", or any request to cross-check a completed proposal against
  the source RFP. Also trigger when the user uploads an RFP AND a response doc
  or slide deck and asks for a gap analysis, compliance check, or narrative
  audit. Always produces a standalone Review Report — never edits the original
  proposal. Combine with rfp-response, unqork-rfp, or aiden-ai-rfp skills for
  platform-specific validation.
license: "Internal use"
---

# RFP Review & Validation Skill

This skill guides a structured, end-to-end **audit of an RFP response package** against the source RFP. It reads both documents critically, validates compliance, alignment, pricing, estimates, attachments, and open items — and outputs a clear checklist with pass/fail statuses and a prioritized open questions log.

> **When to combine with other skills:**
> - If the RFP mentions **Unqork**: also read `/mnt/skills/user/unqork-rfp/SKILL.md`
> - If the RFP mentions **Aiden / AIDAP**: also read `/mnt/skills/user/aiden-ai-rfp/SKILL.md`
> - If generating a corrected response: also read `/mnt/skills/user/rfp-response/SKILL.md`

---

## Step 0: Gather All Materials

Before starting the review, identify and confirm you have access to all of the following:

| # | Document / Artifact | Status |
|---|---------------------|--------|
| 1 | **Source RFP** (original client document) | Required |
| 2 | **Proposal Response Document** (.docx / .pdf / .md) | Required |
| 3 | **Proposal Presentation / Deck** (.pptx / slides) | If submitted |
| 4 | **Pricing / Estimate Workbook** (.xlsx / table) | If separate |
| 5 | **Required Attachments** (forms, certifications, CVs, etc.) | If required by RFP |

> If any required document is missing, **stop and ask** before proceeding. A review without the source RFP or the primary response document is not possible.

---

## Step 1: RFP Intelligence Extraction (Read the RFP First)

Read the **entire RFP** before evaluating the response. Extract and document the following. This becomes your audit baseline.

### 1.1 Submission Requirements
- Exact **submission deadline** (date, time, timezone)
- **Submission method** (portal, email, physical)
- **Format requirements** (page limits, font, PDF/Word, binding, copies)
- **Required sections** explicitly mandated by the RFP
- **Required attachments** (forms, templates, certificates, references)
- **Mandatory pass/fail criteria** (any requirement that disqualifies non-compliant bids)

### 1.2 Key Evaluation Criteria
Extract all scoring dimensions and weights:

| Criterion | Weight | Notes |
|-----------|--------|-------|
| [e.g., Technical Approach] | [e.g., 40%] | |
| [e.g., Pricing] | [e.g., 30%] | |
| [e.g., Team / Experience] | [e.g., 20%] | |
| [e.g., Company Qualifications] | [e.g., 10%] | |

### 1.3 Explicit Requirements Inventory
Create a numbered list of **every explicit requirement** stated in the RFP. Tag each as:
- 🔴 **MANDATORY** — disqualifying if missing
- 🟡 **SCORED** — evaluated and weighted
- 🟢 **INFORMATIONAL** — context only, no direct scoring

> **Tip**: Look for requirements in: Statement of Work, Technical Requirements, Vendor Qualifications, Submission Instructions, Evaluation Criteria, and any appendices.

### 1.4 Questions & Clarifications Log (from RFP)
Note anything in the RFP that is **ambiguous, contradictory, or unclear**. These become open questions in the final output.

---

## Step 2: Response Document Review

Read the **proposal response document** in full. For each section, check:

### 2.1 Section Coverage Check

| RFP Section / Requirement | Present in Response? | Quality | Notes |
|---------------------------|---------------------|---------|-------|
| Executive Summary | ✅ / ⚠️ / ❌ | Strong / Adequate / Weak | |
| Problem Understanding | ✅ / ⚠️ / ❌ | | |
| Proposed Solution | ✅ / ⚠️ / ❌ | | |
| Technical Architecture | ✅ / ⚠️ / ❌ | | |
| Requirements Traceability | ✅ / ⚠️ / ❌ | | |
| Delivery Approach | ✅ / ⚠️ / ❌ | | |
| Project Plan / Timeline | ✅ / ⚠️ / ❌ | | |
| Team / Staffing | ✅ / ⚠️ / ❌ | | |
| Past Experience / References | ✅ / ⚠️ / ❌ | | |
| Pricing / Cost Summary | ✅ / ⚠️ / ❌ | | |
| Assumptions | ✅ / ⚠️ / ❌ | | |
| Risks & Mitigation | ✅ / ⚠️ / ❌ | | |
| [Any RFP-specific section] | ✅ / ⚠️ / ❌ | | |

### 2.2 Mandatory Requirements Compliance Check

Map every 🔴 MANDATORY requirement from Step 1.3 to the response:

| Req # | Requirement | Response Location | Compliant? | Gap / Issue |
|-------|-------------|------------------|------------|-------------|
| M-1 | [Requirement] | [Section X.X] | ✅ Full / ⚠️ Partial / ❌ Missing | |
| M-2 | [Requirement] | [Section X.X] | | |

> **CRITICAL**: Any ❌ Missing mandatory requirement is a **disqualifying risk**. Flag immediately and prominently.

### 2.3 Scored Requirements Compliance Check

Map every 🟡 SCORED requirement to the response:

| Req # | Requirement | Weight | Response Location | Coverage | Strength |
|-------|-------------|--------|------------------|----------|----------|
| S-1 | [Requirement] | [X%] | [Section X.X] | ✅ / ⚠️ / ❌ | Strong / Adequate / Weak |

---

## Step 3: Language Consistency & Narrative Alignment Audit

> **IMPORTANT**: Do NOT rewrite or correct any text. This step is purely analytical — identify and document issues for the review report. All findings are reported with exact locations (section, paragraph, slide number) so the author can make corrections.

### 3.1 Terminology Consistency Scan

Read the full response document and presentation together. Flag every instance where the same concept is referred to using **different terminology** across sections or documents. Common inconsistency patterns to scan for:

| Terminology Category | What to Check |
|---------------------|---------------|
| **Product / platform name** | Is the platform spelled and capitalised identically every time? (e.g., "Unqork" vs "UNQORK" vs "UnQork") |
| **Project name** | Is the engagement name consistent? (e.g., "Project Alpha" vs "Alpha Project" vs "the Alpha initiative") |
| **Client name** | Is the client's legal name used consistently? (e.g., "Department of Health" vs "DoH" vs "the Department") |
| **Our company name** | Consistent usage of our own firm name throughout? |
| **Phase names** | Are project phases named identically everywhere? (e.g., "Discovery" vs "Phase 0 Discovery" vs "Inception") |
| **Role titles** | Are roles consistent? (e.g., "Project Manager" vs "Engagement Manager" vs "PM") |
| **Deliverable names** | Are deliverables named consistently? (e.g., "Solution Design Document" vs "SDD" vs "Design Doc") |
| **Acronyms** | Are all acronyms defined on first use and used consistently thereafter? |
| **Currencies / units** | Are monetary values in the same currency and format throughout? |
| **Dates / time formats** | Are date formats consistent? (e.g., DD/MM/YYYY vs MM/DD/YYYY vs "Q1 2025") |

### 3.2 Narrative & Message Alignment Check

Verify that the **strategic narrative is consistent** across the full response package — document and deck must tell the same story:

| Narrative Element | Check |
|------------------|-------|
| **Value proposition** | Is the core "why us" message identical or complementary across executive summary (doc) and opening slides (deck)? |
| **Problem statement** | Is the client's problem framed the same way throughout? |
| **Solution description** | Is the proposed solution described consistently — same features, same scope, same approach? |
| **Key differentiators** | Are the same 3–5 differentiators cited consistently, not different ones in different places? |
| **Timeline / go-live date** | Is the stated project duration and go-live date the same in every section and every slide? |
| **Team composition** | Is the same team described in staffing section, CVs, and deck slides? |
| **Scope boundaries** | Are in-scope and out-of-scope items consistent across all sections? |
| **Risk language** | Are risks framed consistently — not catastrophised in one section, minimised in another? |
| **Pricing narrative** | Is the pricing described with the same context and qualifications throughout? |

### 3.3 Tone & Register Consistency

Flag sections where the **tone shifts** significantly in ways that undermine credibility:

- Sections that are suddenly overly casual when the rest is formal
- Sections that use first person ("I") vs the rest uses "we"
- Sections that shift from confident to hedging or from active to passive voice unexpectedly
- Sections that use marketing language inconsistent with the technical tone elsewhere
- Boilerplate or templated text that hasn't been customised to this RFP (e.g., "[Client Name]" left unreplaced, wrong industry referenced)

### 3.4 Cross-Reference Integrity

Check that internal cross-references within the document are accurate:

- Section references ("see Section 6.3 for details") — does Section 6.3 actually contain the referenced content?
- Figure/table references ("see Table 4") — does Table 4 exist and contain the right data?
- Appendix references — do all referenced appendices exist?
- Any "as described above/below" references — is the referenced content actually above/below?

---

## Step 4: Presentation / Deck Alignment Review

If a slide deck is part of the submission package, verify **alignment between the deck and the response document**:

### 4.1 Narrative Consistency Check
- Does the executive summary in the deck match the document?
- Are pricing figures **identical** in both (no rounding inconsistencies)?
- Is the project timeline/phases consistent across both artifacts?
- Are team member names, roles, and credentials consistent?
- Is the proposed solution described the same way in both?
- Do key differentiators and win themes align?

### 4.2 Deck-Specific Completeness
- Does the deck stand alone if the evaluator only sees it?
- Are all RFP-required topics visually represented?
- Is branding, client name, and RFP reference correct throughout?

Flag any **conflicts or inconsistencies** between deck and document as HIGH PRIORITY issues.

---

## Step 5: Requirements Traceability Matrix Validation

If the response includes a Requirements Traceability Matrix (RTM), audit it:

- [ ] Does the RTM reference **every mandatory requirement** from the RFP?
- [ ] Are all RTM entries mapped to a specific section of the proposal?
- [ ] Are any requirements marked "Partial" — and is there a clear explanation?
- [ ] Are any requirements **missing from the RTM** that appear in the RFP?
- [ ] Does the RTM use consistent requirement numbering that matches the RFP?

If there is no RTM but the RFP requires one — flag as a CRITICAL gap.

---

## Step 6: Estimate & Experience Validation

### 5.1 Estimate Reasonableness Check

Review the effort estimates and validate:

| Check | Pass / Fail | Notes |
|-------|------------|-------|
| Total hours are stated clearly | | |
| Phase-by-phase breakdown provided | | |
| Onshore/offshore split is stated (default: 20/80) | | |
| Onshore rate = $100/hr (or stated rate if different) | | |
| Offshore rate = $40/hr (or stated rate if different) | | |
| Blended rate math is correct: (0.20×100)+(0.80×40) = $52 | | |
| Total cost = (Onshore hrs × $100) + (Offshore hrs × $40) | | |
| No arithmetic errors in pricing tables | | |
| Estimate is defensible given the described scope | | |
| Contingency or assumptions about estimate basis are noted | | |

**Sanity-check the hours**: Cross-reference the staffing plan with the project timeline. If the team is described as 8 people over 6 months (~1,040 hours per person), the total hours should be in the range of 8,320 hours. Significant deviations need explanation.

### 5.2 Experience / Credentials Validation

Check that the response substantiates claimed experience:

| Check | Pass / Fail | Notes |
|-------|------------|-------|
| Past projects cited are relevant to this RFP's domain | | |
| Case studies or references align with claimed capabilities | | |
| Team CVs/bios (if included) match the roles proposed | | |
| Certifications mentioned are real and current | | |
| Client references (if required) are provided and contactable | | |
| Years of experience claims are consistent throughout | | |

---

## Step 7: Pricing Validation

### 6.1 Price Completeness Check

| Pricing Element | Present? | Correct? | Notes |
|----------------|----------|----------|-------|
| Professional services total | ✅ / ❌ | | |
| Infrastructure costs (if non-Unqork) | ✅ / ❌ / N/A | | |
| Unqork license (if Unqork RFP) | ✅ / ❌ / N/A | | |
| Third-party licenses | ✅ / ❌ / N/A | | |
| Travel & expenses | ✅ / ❌ / N/A | | |
| Payment milestones / schedule | ✅ / ❌ | | |
| Grand total is clearly stated | ✅ / ❌ | | |

### 6.2 Pricing Consistency Check
- Does the pricing total match across: document, deck, and any separate pricing forms?
- Are all numbers in the same currency?
- If a pricing template was provided by the client — has it been used?
- Are all optional/alternative pricing scenarios clearly labeled?

### 6.3 Platform-Specific Pricing Rules
- **Unqork RFP**: Infrastructure costs must NOT be included (covered by license). Flag if present.
- **Non-Unqork RFP**: Infrastructure must be included. Flag if absent.
- **Aiden/AIDAP**: Check AI compute cost handling per `aiden-ai-rfp` skill.

---

## Step 8: Attachments & Submission Completeness

Go back to the RFP's submission requirements section. For every required attachment or form:

| Attachment / Form | RFP Reference | Prepared? | Notes |
|-------------------|---------------|-----------|-------|
| [e.g., Vendor qualification form] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Signed cover letter] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Insurance certificates] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Reference contacts form] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Pricing schedule template] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Team CVs / resumes] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Non-disclosure agreement] | [§X.X] | ✅ / ⚠️ / ❌ | |
| [e.g., Conflict of interest declaration] | [§X.X] | ✅ / ⚠️ / ❌ | |

Any ❌ missing required attachment is a **submission risk**. Flag with urgency level.

---

## Step 9: Final Output — Review Report

> **OUTPUT RULE**: Produce the full review as a **standalone Review Report document** (Markdown `.md` file). Do NOT make any changes to the original response documents. The review report identifies, locates, and categorises all issues — the author decides what to fix. Always save the review report as a file and present it to the user.

Produce the complete review output in six parts:

---

### Part A: Compliance Scorecard

```
╔══════════════════════════════════════════════════════╗
║         RFP RESPONSE REVIEW SCORECARD                ║
╠══════════════════════════════════════════════════════╣
║ RFP Title:        [Name]                             ║
║ Client:           [Client name]                      ║
║ Response Date:    [Date reviewed]                    ║
║ Reviewer:         Claude (AI-assisted)               ║
╚══════════════════════════════════════════════════════╝
```

| Review Domain | Status | Critical Issues |
|--------------|--------|----------------|
| Mandatory Requirements | ✅ All covered / ⚠️ Gaps / 🔴 Disqualifying gaps | |
| Scored Requirements | ✅ Strong / ⚠️ Moderate / ❌ Weak | |
| Language & Terminology Consistency | ✅ Consistent / ⚠️ Minor issues / ❌ Major inconsistencies | |
| Narrative & Message Alignment | ✅ Aligned / ⚠️ Minor drift / ❌ Contradictions found | |
| Document ↔ Deck Alignment | ✅ Aligned / ⚠️ Minor conflicts / ❌ Major conflicts | |
| Cross-Reference Integrity | ✅ All valid / ⚠️ Some broken / ❌ Widespread errors | |
| Estimate Validation | ✅ Sound / ⚠️ Review needed / ❌ Errors found | |
| Experience Substantiation | ✅ Strong / ⚠️ Weak / ❌ Missing | |
| Pricing Completeness | ✅ Complete / ⚠️ Gaps / ❌ Errors | |
| Attachments | ✅ All present / ⚠️ Some missing / ❌ Critical missing | |
| **OVERALL** | **🟢 READY / 🟡 NEEDS WORK / 🔴 NOT READY** | |

---

### Part B: Missing RFP Requirements Register

> This section lists every RFP requirement that is **absent or insufficiently addressed** in the response. This is the core compliance gap log — every entry here is a direct miss against what the client asked for.

| # | RFP Section | Requirement | Type | Status in Response | Risk Level |
|---|-------------|-------------|------|--------------------|------------|
| G-1 | [e.g., RFP §3.2] | [Exact requirement text or paraphrase] | 🔴 Mandatory / 🟡 Scored / 🟢 Info | ❌ Missing / ⚠️ Partially addressed | 🔴 Disqualifying / 🟡 Score loss / 🟢 Minor |
| G-2 | [RFP §X.X] | [Requirement] | | | |
| G-3 | [RFP §X.X] | [Requirement] | | | |

**Summary counts:**
- 🔴 Mandatory requirements missing: [N]
- 🟡 Scored requirements insufficiently addressed: [N]
- 🟢 Informational requirements not acknowledged: [N]

> If zero gaps found: state "All identified RFP requirements are addressed in the response."

---

### Part C: Language & Consistency Issues Log

> Do NOT correct any text. Report exact locations so the author can fix them.

#### C.1 Terminology Inconsistencies

| # | Term / Concept | Variant A | Location A | Variant B | Location B | Recommended Standard |
|---|---------------|-----------|------------|-----------|------------|---------------------|
| T-1 | [e.g., Platform name] | "Unqork" | Doc §2, p.4 | "UNQORK" | Deck Slide 7 | "Unqork" (per vendor branding) |
| T-2 | [e.g., Phase name] | "Discovery Phase" | Doc §12 | "Phase 0 Inception" | Doc §13 | Align to single name |
| T-3 | [e.g., Client name] | "Dept. of Health" | Doc §1 | "Department of Health" | Deck Slide 1 | Use full legal name throughout |

#### C.2 Narrative & Message Inconsistencies

| # | Element | Inconsistency Found | Location 1 | Location 2 | Impact |
|---|---------|---------------------|------------|------------|--------|
| N-1 | [e.g., Go-live date] | "Q3 2025" stated in doc vs "Q4 2025" in deck | Doc §13 | Deck Slide 12 | 🔴 High — evaluator will notice |
| N-2 | [e.g., Team size] | "8-person team" in staffing vs "10 resources" in exec summary | Doc §16 | Doc §1 | 🟡 Medium |
| N-3 | [e.g., Differentiator] | Differentiator 3 ("AI-native") cited in deck but absent from doc | Deck Slide 5 | Doc §2 | 🟡 Medium |

#### C.3 Tone & Register Issues

| # | Location | Issue Description | Severity |
|---|----------|-------------------|---------|
| TR-1 | [e.g., Doc §7, para 3] | [e.g., Sudden switch to first-person "I will ensure..." rest of doc uses "we"] | 🟡 Medium |
| TR-2 | [e.g., Deck Slide 9] | [e.g., Unfilled template placeholder: "[Insert client logo]" visible] | 🔴 High |
| TR-3 | [e.g., Doc §14, para 1] | [e.g., References "our previous work for ABC Corp" — wrong client name, likely copy-paste error] | 🔴 High |

#### C.4 Broken Cross-References

| # | Location | Reference Made | Actual Destination | Issue |
|---|----------|---------------|-------------------|-------|
| XR-1 | [e.g., Doc §4, p.8] | "See Section 9.2 for architecture details" | Section 9.2 covers staffing | Wrong section referenced |
| XR-2 | [e.g., Doc §11] | "Refer to Appendix C" | No Appendix C exists | Missing appendix |
| XR-3 | [e.g., Doc §6] | "See Table 3" | Table 3 shows pricing, not architecture | Wrong table referenced |

---

### Part D: Action Checklist

Present a prioritised, actionable checklist. Group by urgency:

#### 🔴 CRITICAL — Must fix before submission
- [ ] [e.g., "Mandatory requirement §3.2 (data residency) is not addressed anywhere in the response — DISQUALIFYING"]
- [ ] [e.g., "Pricing on Deck Slide 14 shows $1.2M; response document §16.4 shows $1.4M — resolve conflict"]
- [ ] [e.g., "Insurance certificate required per RFP §7.1 is not included in the submission package"]
- [ ] [e.g., "Template placeholder '[Client Logo]' is visible on Deck Slide 1 — must be replaced"]

#### 🟡 IMPORTANT — Should fix if time permits
- [ ] [e.g., "Requirements Traceability Matrix is missing RFP requirements §4.5–4.8"]
- [ ] [e.g., "Go-live date is stated as Q3 2025 in the document and Q4 2025 in the deck — align"]
- [ ] [e.g., "'Engagement Manager' in staffing table referred to as 'Project Manager' in three deck slides"]
- [ ] [e.g., "Section 7 references Appendix C which does not exist — update reference or add appendix"]

#### 🟢 NICE TO HAVE — Optional improvements
- [ ] [e.g., "Risk register is thin — consider adding client availability and data quality risks"]
- [ ] [e.g., "Executive summary is reactive — open with client's challenge before proposing solution"]

---

### Part E: Open Questions Log

List everything that is **unclear, ambiguous, or unverifiable** from either the RFP or the response:

| # | Source | Question | Impact | Owner |
|---|--------|----------|--------|-------|
| OQ-1 | RFP §2.3 | [e.g., "'Relevant experience' — does this require exact industry match or adjacent domain acceptable?"] | 🔴 High | Bid Manager → Client |
| OQ-2 | Response §16 | [e.g., "What is the basis for 3,200 offshore hours in Phase 2 — is there a detailed estimate sheet?"] | 🟡 Medium | Delivery Lead |
| OQ-3 | RFP §5.1 | [e.g., "Is the provided pricing template mandatory or a suggested format?"] | 🟡 Medium | Bid Manager → Client |
| OQ-4 | Response §8 | [e.g., "Infrastructure line shows $0 — confirm intentional given this is a non-Unqork RFP"] | 🔴 High | Solution Architect |

---

### Part F: Submission Readiness Summary

Provide a one-paragraph plain-language verdict for the bid team:

> **Example**: *"The response package has [N] critical issues that must be resolved before submission. The most urgent are: [issue 1], [issue 2], [issue 3]. There are also [N] important language/consistency issues that could undermine evaluator confidence. [N] open questions have been raised that require input from either the delivery lead or the client before the response can be finalised. The overall submission is currently rated [🟢 READY / 🟡 NEEDS WORK / 🔴 NOT READY]."*

---

## Review Principles

1. **Read the RFP first, always** — never review a response without the source document.
2. **Never change the source documents** — the review report observes and reports; the author decides and fixes.
3. **Assume nothing is covered unless you can point to it** with an exact location in the response.
4. **Inconsistencies between documents are high risk** — evaluators catch these and lose confidence.
5. **Missing mandatory requirements = disqualification** — these are never minor issues.
6. **Language inconsistency erodes credibility** — a sloppy proposal signals a sloppy delivery team.
7. **Pricing errors are trust-destroyers** — arithmetic must be verified, not assumed.
8. **Open questions are valuable output** — a clear OQ log helps the bid team make fast decisions.
9. **Be specific in every finding** — not "this section is weak" but "§3 claims SOC 2 compliance but no certificate is included per RFP §6.2 requirement."
10. **Report location precisely** — every finding must include the document name, section number, page, or slide number.

---

## Quick Reference: Common Review Failures

| Failure Pattern | Where to Check | Reported In |
|----------------|----------------|-------------|
| Pricing mismatch between doc and deck | Step 7.2 | Part D Checklist — CRITICAL |
| RFP requirement with no response coverage | Step 2.2 | Part B Missing Requirements Register |
| Mandatory form not submitted | Step 8 | Part D Checklist — CRITICAL |
| Terminology used inconsistently | Step 3.1 | Part C.1 Terminology Log |
| Timeline stated differently across documents | Step 3.2 | Part C.2 Narrative Issues |
| Wrong client name (copy-paste from old proposal) | Step 3.3 | Part C.3 Tone Issues — CRITICAL |
| Broken internal section reference | Step 3.4 | Part C.4 Cross-References |
| Missing appendix that is referenced | Step 3.4 | Part C.4 Cross-References |
| Infrastructure included in Unqork RFP | Step 7.3 | Part D Checklist — CRITICAL |
| Infrastructure missing in non-Unqork RFP | Step 7.3 | Part D Checklist — CRITICAL |
| Onshore/offshore rate not stated | Step 6.1 | Part D Checklist — IMPORTANT |
| Experience claims without evidence | Step 6.2 | Part D Checklist — IMPORTANT |
| Team in deck ≠ team in document | Step 4.1 | Part C.2 Narrative Issues |
| RFP Q&A deadline missed | Step 1.1 | Part E Open Questions — escalate immediately |
