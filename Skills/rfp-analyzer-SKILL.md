---
name: rfp-analyzer
description: >-
  Use this skill whenever the user uploads, shares, or references an RFP document
  and wants to extract, analyze, or understand its contents BEFORE writing a response.
  Triggers include: "analyze this RFP", "what does this RFP ask for", "extract
  requirements", "summarize this RFP", "what are the deadlines", "how will they
  evaluate us", "what are the mandatory requirements", "read Exhibit B", "break down
  this scope", or any request to understand an RFP document before responding to it.
  This skill is the FIRST step before using the rfp-response skill. Always run this
  skill first when a new RFP arrives. Do NOT use for writing the response — use the
  base rfp-response skill for that.
license: "Internal use"
---

# RFP Analyzer Skill

This skill provides a systematic, thorough framework for **reading, extracting, and analyzing RFP documents** before any response is drafted. It ensures nothing is missed and gives the team a complete intelligence picture of the opportunity.

> **This skill runs BEFORE the rfp-response skill.** Analyze first, respond second. Never draft a proposal without completing this analysis.

---

## Phase 1: Document Inventory

Before reading content, catalog what you're working with.

### 1.1 Document Map

List every document, exhibit, appendix, and attachment in the RFP package:

| # | Document Name | Type | Pages/Size | Key Contents |
|---|--------------|------|------------|--------------|
| 1 | [Main RFP body] | PDF/Word | [X pages] | Scope, evaluation, instructions |
| 2 | [Exhibit A] | [Type] | [Size] | [Contents] |
| 3 | [Exhibit B] | [Type] | [Size] | [Contents] |
| N | [Attachment N] | [Type] | [Size] | [Contents] |

### 1.2 Format Requirements

Extract ALL submission format requirements:

- **Response format**: PDF / Word / Portal upload / Physical
- **Page limit**: [If any]
- **Font/margin requirements**: [If specified]
- **Section ordering**: Must follow RFP structure? Or proposer's choice?
- **Mandatory forms**: Any forms that must be completed and attached?
- **Copies required**: Electronic only? Physical copies?
- **File naming convention**: [If specified]
- **Portal submission details**: URL, account setup, file size limits

---

## Phase 2: Timeline & Logistics Intelligence

### 2.1 Complete Date Extraction

Extract EVERY date mentioned in the RFP. Present as a timeline:

| Date | Time | Timezone | Event | Mandatory? | Action Required |
|------|------|----------|-------|------------|-----------------|
| [date] | [time] | [tz] | RFP issued | - | - |
| [date] | [time] | [tz] | Intent to bid / registration deadline | Yes/No | [What to do] |
| [date] | [time] | [tz] | Questions / clarifications deadline | Yes/No | [What to do] |
| [date] | [time] | [tz] | Q&A responses published | - | Review answers |
| [date] | [time] | [tz] | Proposal due date | YES | Submit by this time |
| [date] | [time] | [tz] | Shortlist notification | - | - |
| [date] | [time] | [tz] | Oral presentations / demos | Likely | Prepare demo |
| [date] | [time] | [tz] | Best & final offer (BAFO) | Maybe | - |
| [date] | [time] | [tz] | Contract award | - | - |
| [date] | [time] | [tz] | Expected project start | - | Staff planning |

### 2.2 Submission Logistics

- **Submit to**: [Email / portal URL / physical address]
- **Point of contact**: [Name, title, email, phone]
- **Questions submitted to**: [Email / portal]
- **Late submission policy**: Accepted? Rejected? Grace period?
- **Amendment process**: How are RFP changes communicated?

---

## Phase 3: Client Intelligence

### 3.1 Client Profile

- **Client name (full legal entity)**:
- **Industry / sector**:
- **Headquarters / geography**:
- **Regulatory environment**: [IRDAI, NAIC, DIFC, state-regulated, federal, etc.]
- **Estimated size**: [Revenue, employees, customers — if available]
- **Current technology landscape**: [What systems do they mention using today?]
- **Pain points stated or implied**: [Why are they issuing this RFP?]

### 3.2 Stakeholder Map

Identify every person or role mentioned:

| Name | Title | Role in RFP Process | Contact Info |
|------|-------|-------------------|-------------|
| [Name] | [Title] | Decision maker / Evaluator / POC / Sponsor | [If provided] |

### 3.3 Incumbent & Competitive Intelligence

- **Current vendor/system**: [What are they replacing or augmenting?]
- **Reason for change**: [Contract expiry? Dissatisfaction? New requirements?]
- **Known competitors**: [Any hints about who else is bidding?]
- **Bias indicators**: [Does the RFP seem written for a specific vendor?]

---

## Phase 4: Scope & Requirements Analysis

### 4.1 Scope Summary

In 3-5 sentences, summarize what the client is asking for in plain language.

### 4.2 Functional Requirements Extraction

Extract ALL functional requirements. For each:

| Req ID | Category | Requirement Description | Priority | Mandatory? | Complexity | Our Capability |
|--------|----------|------------------------|----------|------------|------------|----------------|
| FR-001 | [Category] | [What they need] | High/Med/Low | Yes/No | High/Med/Low | Full/Partial/Gap |
| FR-002 | ... | ... | ... | ... | ... | ... |

**Categorize requirements into domains:**
- User management & authentication
- Core business functionality
- Workflow & process automation
- Reporting & analytics
- Integration requirements
- Data migration
- UI/UX requirements
- Mobile / offline requirements
- AI / automation requirements

### 4.3 Non-Functional Requirements Extraction

| Req ID | Category | Requirement | Specific Target | Our Capability |
|--------|----------|-------------|-----------------|----------------|
| NFR-001 | Performance | [Requirement] | [e.g., < 3 sec response time] | [Can we meet it?] |
| NFR-002 | Scalability | [Requirement] | [e.g., 10,000 concurrent users] | [Can we meet it?] |
| NFR-003 | Availability | [Requirement] | [e.g., 99.9% uptime] | [Can we meet it?] |
| NFR-004 | Security | [Requirement] | [e.g., SOC 2 Type II] | [Can we meet it?] |
| NFR-005 | Compliance | [Requirement] | [e.g., HIPAA, GDPR] | [Can we meet it?] |

**Non-functional categories to check for:**
- Performance (response time, throughput, latency)
- Scalability (users, data volume, concurrent sessions)
- Availability (uptime SLA, disaster recovery, RPO/RTO)
- Security (authentication, encryption, penetration testing)
- Compliance (industry regulations, certifications)
- Accessibility (WCAG, ADA, Section 508)
- Localization (languages, currencies, time zones)
- Data residency (where data must be stored)
- Browser / device support
- Integration SLAs
- Backup & recovery

### 4.4 User & Volume Metrics

Extract every mention of scale, users, and volume:

| Metric | Value | Context |
|--------|-------|---------|
| Total users | [Number] | [Where mentioned] |
| Concurrent users | [Number] | [Where mentioned] |
| Transaction volume | [Number/period] | [Where mentioned] |
| Data volume | [Size] | [Where mentioned] |
| Number of locations / offices | [Number] | [Where mentioned] |
| Number of integrations | [Number] | [Where mentioned] |
| Geographic distribution | [Regions] | [Where mentioned] |
| Growth projection | [Rate] | [Where mentioned] |

> **CRITICAL**: If user counts or volume metrics are NOT stated, flag this explicitly: "User/volume metrics not provided — must clarify before estimating infrastructure and pricing."

### 4.5 Integration Requirements

| # | System / Application | Direction | Protocol | Frequency | Data Exchanged | Mandatory? |
|---|---------------------|-----------|----------|-----------|---------------|------------|
| 1 | [System name] | Inbound/Outbound/Bidirectional | REST/SOAP/File/MQ | Real-time/Batch | [Data types] | Yes/No |

### 4.6 Data Migration Requirements

- **Source systems**: [What data is migrating from where?]
- **Data volume**: [How much?]
- **Data types**: [Structured, unstructured, documents, images?]
- **Historical data**: [How far back?]
- **Data quality**: [Any known issues?]
- **Migration timeline**: [Big bang or phased?]
- **Validation requirements**: [How is migration verified?]

---

## Phase 5: Evaluation Intelligence

### 5.1 Evaluation Criteria & Weights

| # | Criterion | Weight | What They're Really Looking For |
|---|----------|--------|-------------------------------|
| 1 | [Technical approach] | [X%] | [Our interpretation] |
| 2 | [Experience & qualifications] | [X%] | [Our interpretation] |
| 3 | [Price / cost] | [X%] | [Our interpretation] |
| 4 | [Team / staffing] | [X%] | [Our interpretation] |
| 5 | [Demo / presentation] | [X%] | [Our interpretation] |

### 5.2 Mandatory / Pass-Fail Requirements

List every requirement that is explicitly pass/fail or mandatory:

| # | Requirement | Evidence Needed | Can We Meet It? | Risk |
|---|------------|-----------------|-----------------|------|
| 1 | [Requirement] | [What to provide] | Yes/No/Partial | [Risk if partial] |

> **RED FLAG**: Any mandatory requirement we cannot fully meet must be escalated immediately.

### 5.3 Win Theme Identification

Based on the evaluation criteria and client context, identify 3-5 themes that should run through our response:

1. **Theme 1**: [What the client values most] → [How we address it]
2. **Theme 2**: [Second priority] → [How we address it]
3. **Theme 3**: [Third priority] → [How we address it]

---

## Phase 6: Risk & Gap Analysis

### 6.1 Compliance Gaps

| # | Requirement | Gap Description | Severity | Mitigation Option |
|---|------------|-----------------|----------|-------------------|
| 1 | [Requirement we can't fully meet] | [What's missing] | High/Med/Low | [How to address] |

### 6.2 Ambiguity Register

List every requirement that is vague, contradictory, or needs clarification:

| # | Section/Ref | Ambiguity | Recommended Clarification Question | Impact if Unresolved |
|---|------------|-----------|-----------------------------------|---------------------|
| 1 | [Section] | [What's unclear] | [Question to ask] | [Risk] |

### 6.3 Go / No-Go Assessment

Based on the analysis, provide a recommendation:

| Factor | Assessment | Notes |
|--------|-----------|-------|
| Can we meet mandatory requirements? | Yes/No/Partial | |
| Do we have relevant experience? | Strong/Moderate/Weak | |
| Is the timeline realistic? | Yes/Tight/Unrealistic | |
| Is pricing competitive at our rates? | Yes/Marginal/No | |
| Do we have the right team available? | Yes/Partial/No | |
| Is the client a strategic fit? | Yes/Maybe/No | |
| **Overall recommendation** | **GO / CONDITIONAL GO / NO-GO** | |

---

## Phase 7: Response Planning

### 7.1 Response Outline

Map the RFP's required sections to our response structure:

| RFP Section | RFP Ref | Our Response Section | Owner | Status |
|------------|---------|---------------------|-------|--------|
| [Their section 1] | [§X.X] | [Our section Y] | [Who writes it] | Not started |

### 7.2 Clarification Questions

Compile all questions to submit before the Q&A deadline:

1. [Question 1 — reference section]
2. [Question 2 — reference section]
3. [Question N — reference section]

### 7.3 Effort Drivers for Estimation

Summarize the key factors that drive our effort estimate:

- **Number of functional modules/features**: [Count]
- **Number of integrations**: [Count]
- **Data migration complexity**: [High/Med/Low]
- **Customization level**: [Heavy/Moderate/Light]
- **User count / concurrent load**: [Numbers]
- **Compliance requirements**: [List]
- **Timeline pressure**: [Aggressive/Normal/Relaxed]
- **Client readiness**: [High/Low — do they have SMEs available?]

---

## Output Format

The analysis must be delivered as a **structured Markdown document** with:
- Every section above completed (mark "Not found in RFP" if information is absent)
- A clear executive summary at the top (5-7 sentences)
- Color-coded risk indicators where applicable
- All requirement counts tallied at the end

```
ANALYSIS SUMMARY
─────────────────────────────────
Client:              [Name]
RFP Title:           [Title]
Due Date:            [Date]
Functional Reqs:     [X] total ([Y] mandatory)
Non-Functional Reqs: [X] total ([Y] mandatory)
Integrations:        [X]
Compliance Gaps:     [X]
Ambiguities:         [X]
Go/No-Go:            [RECOMMENDATION]
─────────────────────────────────
```

---

> **Final reminder**: A thorough RFP analysis is the foundation of a winning response. Rushing past this step is the #1 reason proposals lose — they miss mandatory requirements, misunderstand evaluation criteria, or price against the wrong scope. Take the time here. It pays back tenfold in the response.
