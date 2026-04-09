---
name: rfp-response
description: >-
  Use this skill whenever the user wants to analyze an RFP (Request for
  Proposal) document and generate a structured professional proposal response.
  Triggers include any mention of RFP, Request for Proposal, proposal response,
  bid response, tender response, or when the user uploads a document and asks
  for a proposal or bid to be drafted. Also use when extracting key metadata
  from an RFP such as deadlines, submission details, and evaluation criteria,
  or when the user asks to respond to a client opportunity. Do NOT use for
  general document summarization, SOW creation without an RFP, or internal
  project plans.
license: "Internal use"
---

This skill guides the complete end-to-end process of reading an RFP document, extracting all critical metadata, and producing a structured, winning proposal response in Markdown format.

---

## Phase 1: RFP Intelligence Extraction

Before writing a single word of the response, thoroughly read the entire RFP and extract the following critical metadata. Present this as a structured **RFP Brief** to the user before proceeding to drafting.

### 1.1 Submission & Logistics
- **Submission destination**: Where exactly does the response get sent? (email address, portal URL, physical address)
- **Submission format**: PDF, Word, portal upload, physical copies, page limits, font/margin requirements
- **Response due date & time**: Exact deadline including timezone
- **Client name & full legal entity**: Who is issuing this RFP?
- **Internal point of contact (client-side)**: Name, title, email, phone of the person managing the RFP process
- **Our internal point of contact**: Who on our side owns this response?

### 1.2 Key Dates & Milestones
Extract and present ALL dates mentioned in the RFP as a timeline table:

| Date | Event |
|------|-------|
| [date] | RFP issued |
| [date] | Intent to bid deadline |
| [date] | Q&A / Clarification submission deadline |
| [date] | Q&A responses published |
| [date] | Proposal due date |
| [date] | Shortlist/down-select notification |
| [date] | Oral presentations / demos |
| [date] | Contract award |
| [date] | Project kickoff |

### 1.3 Evaluation & Win Themes
- **Evaluation criteria**: List all scoring dimensions and their weights (e.g., Technical 40%, Price 30%, Past Experience 20%, Team 10%)
- **Key win themes**: Identify 3–5 explicit or implied success factors the client values most (e.g., time-to-value, regulatory compliance, scalability, local presence, proven methodology)
- **Mandatory requirements**: Any pass/fail or must-have requirements that disqualify non-compliant responses
- **Incumbent or competitors**: Any clues about incumbent vendors or known competitors in the space

### 1.4 Platform & Context Detection
- **Is this an Unqork RFP?** Look for mentions of Unqork, no-code platform, visual configuration, or Unqork-specific terminology
  - If YES: Infrastructure costs are included in the Unqork license — do NOT add separate infrastructure line items
  - If NO: Include an infrastructure requirements section with relevant sizing and cost assumptions
- **Key AI capabilities requested**: Identify any mentions of AI, ML, generative AI, LLM, automation, intelligent document processing, chatbots, predictive analytics, etc.

---

## Phase 2: Proposal Response Structure

Generate the full proposal response using the following Table of Contents. Each section must be substantive, tailored to the specific RFP, and avoid generic filler language.

---

# [Client Name] — Proposal Response
**RFP Reference:** [RFP ID / Title]
**Submitted by:** [Our Company Name]
**Submission Date:** [Date]
**Version:** 1.0 | CONFIDENTIAL

---

## Table of Contents

1. Executive Summary
2. Why Our Solution Is a Great Fit
3. Our Understanding of the Problem Statement
4. Scope of Work
5. What Is Out of Scope
6. Solution Architecture (Detailed)
7. Solution Components (Detailed Descriptions)
8. Infrastructure Requirements *(omit for Unqork RFPs — included in license)*
9. Key AI Capabilities
10. Requirements Traceability Matrix
11. As-Is to To-Be State View
12. Delivery Approach
13. Project Plan
14. Risks and Mitigation
15. Assumptions
16. Estimate, Staffing & Pricing

---

### Section 1: Executive Summary

Write a compelling 1–2 page executive summary that:
- Opens with a powerful statement of the client's core challenge
- Articulates the proposed solution in plain, confident language (no jargon)
- States 3–5 headline differentiators of the proposed approach
- Confirms understanding of the timeline and commitment to deliver
- Ends with a clear call to action or expression of partnership intent

> **Tone**: Confident, client-centric, strategic. Avoid passive voice. Write as if the client is reading this first (because they are).

---

### Section 2: Why Our Solution Is a Great Fit

Map the client's stated goals and pain points directly to your firm's strengths. Use a combination of:
- A **3–5 bullet narrative** of fit statements ("You need X; we bring Y because Z")
- A **fit matrix table** if the RFP has explicit evaluation criteria:

| Client Priority | Our Relevant Strength | Evidence / Reference |
|----------------|----------------------|----------------------|
| [Priority 1] | [Our capability] | [Case study / credential] |
| [Priority 2] | [Our capability] | [Case study / credential] |

---

### Section 3: Our Understanding of the Problem Statement

- Restate the client's problem in your own words — demonstrate that you have truly understood it, not just read it
- Identify the root causes behind the stated problem
- Call out any secondary or implied challenges not explicitly stated (shows depth of understanding)
- Acknowledge any constraints the client is operating under (budget, timeline, regulatory, organizational)

> **CRITICAL**: Do NOT simply paraphrase the RFP. Reframe the problem from your point of view as a knowledgeable partner.

---

### Section 4: Scope of Work

Define clearly what is included in this engagement. Structure as:

**In Scope:**
- [Workstream 1]: Description of deliverables and boundaries
- [Workstream 2]: Description of deliverables and boundaries
- [Workstream N]: ...

Use a scope table where applicable:

| Workstream | Description | Deliverable | Owner |
|-----------|-------------|-------------|-------|
| [Name] | [What we will do] | [Output] | [Us/Client/Shared] |

---

### Section 5: What Is Out of Scope

Be explicit and specific. Do NOT use vague language like "anything not mentioned above."

List specific exclusions such as:
- Data migration from legacy systems (unless explicitly stated)
- Third-party vendor license procurement
- Ongoing post-go-live support beyond [X] days
- Custom integrations not listed in Section 4
- Training beyond [X] sessions / [X] users
- Change management and organizational readiness

> **Why this matters**: Explicit out-of-scope items protect against scope creep and set clear client expectations.

---

### Section 6: Solution Architecture (Detailed)

Provide a detailed description of the proposed solution architecture. Include:

- **Architecture overview**: Describe the overall structure in narrative form
- **Architecture diagram**: If generating as a document, describe the diagram with clear component labels. If creating programmatically, render a Mermaid or ASCII diagram.
- **Technology stack**: List all technologies, platforms, and tools with their roles
- **Integration landscape**: How the solution connects to existing client systems
- **Security & compliance architecture**: Authentication, authorization, data residency, relevant regulations
- **Scalability & performance**: How the architecture handles growth and load

**For Unqork RFPs specifically:**
- Describe the Unqork module design approach
- Reference relevant Unqork-native capabilities (workflows, policies, connectors)
- Note that infrastructure is bundled with the Unqork license

---

### Section 7: Solution Components (Detailed Descriptions)

For each major component of the solution, provide a dedicated sub-section:

#### 7.X [Component Name]
- **Purpose**: What this component does and why it's needed
- **Key features**: Bullet list of capabilities
- **Technology**: What it's built on
- **Integration points**: What it connects to
- **User personas served**: Who uses this component

Repeat for every significant component in the proposed solution.

---

### Section 8: Infrastructure Requirements

> ⚠️ **SKIP THIS SECTION FOR UNQORK RFPs.** Infrastructure is included in the Unqork license. Replace with a note: *"Infrastructure provisioning, hosting, and scaling are included as part of the Unqork platform license. No separate infrastructure costs apply."*

For non-Unqork RFPs, include:

| Component | Specification | Environment | Sizing Basis |
|-----------|--------------|-------------|--------------|
| Application servers | [Spec] | Dev / UAT / Prod | [# concurrent users] |
| Database | [Type, size] | Dev / UAT / Prod | [Data volume estimate] |
| Storage | [Type, GB/TB] | Dev / UAT / Prod | [Asset types] |
| Network / CDN | [Spec] | Prod | [Traffic estimate] |
| CI/CD pipeline | [Tools] | All | [Deployment frequency] |
| Monitoring & alerting | [Tools] | Prod | [SLA target] |

Include cloud platform recommendation (AWS / Azure / GCP / on-prem) with justification.

---

### Section 9: Key AI Capabilities

List every AI/ML capability proposed in the solution. For each:

| AI Capability | Description | Use Case in This Solution | Underlying Technology |
|--------------|-------------|--------------------------|----------------------|
| [e.g., Document Intelligence] | [What it does] | [How it applies here] | [e.g., Azure Form Recognizer, Claude API] |
| [e.g., Conversational AI] | [What it does] | [How it applies here] | [e.g., Claude, GPT-4o] |
| [e.g., Predictive Analytics] | [What it does] | [How it applies here] | [e.g., custom ML model] |

If no AI capabilities are in scope or requested, state: *"No AI capabilities are in scope for this engagement based on the RFP requirements."*

---

### Section 10: Requirements Traceability Matrix

Map every explicit RFP requirement to the solution component that addresses it. This is often the most scrutinized section by evaluators.

| RFP Ref # | Requirement Description | Our Solution Component | Compliance | Notes |
|-----------|------------------------|----------------------|------------|-------|
| [RFP §3.1] | [Exact or paraphrased requirement] | [Section 7.X / Component name] | ✅ Full / ⚠️ Partial / ❌ Not addressed | [Any caveats] |

> **CRITICAL**: Every mandatory/must-have requirement must appear here. Flag any partial compliance proactively with a clear explanation and workaround.

---

### Section 11: As-Is to To-Be State View

Describe the transformation the client will experience. Use a two-column format:

| Dimension | As-Is State (Today) | To-Be State (Post-Implementation) |
|-----------|--------------------|------------------------------------|
| Process | [Current pain point] | [Future optimized state] |
| Technology | [Current legacy stack] | [New solution] |
| Data | [Siloed / manual] | [Unified / automated] |
| User experience | [Current friction] | [Future streamlined UX] |
| Compliance/Risk | [Current exposure] | [Mitigated / automated] |
| Metrics | [Current KPI baseline] | [Target KPI improvement] |

Include a narrative paragraph for each major transformation theme.

---

### Section 12: Delivery Approach

Describe the delivery methodology in detail:

- **Methodology**: Agile, Waterfall, or hybrid — justify the choice based on the project nature
- **Sprint/phase cadence**: Sprint length, ceremony structure (if Agile)
- **Governance model**: Steering committee, project sponsor, working team structure
- **Client involvement expectations**: What we need from the client and when
- **Quality assurance approach**: Code reviews, testing strategy (unit, integration, UAT, performance)
- **Change management process**: How scope changes are handled
- **Environment strategy**: Dev → UAT → Staging → Production promotion process
- **Hypercare / warranty period**: Post-go-live support window and SLA

---

### Section 13: Project Plan

Present a high-level project plan as a phased timeline. If generating a document, use a Markdown table. If generating a presentation, describe each phase.

| Phase | Key Activities | Milestone | Start | End | Duration |
|-------|--------------|-----------|-------|-----|----------|
| Phase 0: Inception | Discovery, environment setup, team onboarding | Kickoff complete | [Wk 1] | [Wk 2] | 2 weeks |
| Phase 1: [Name] | [Activities] | [Milestone] | [Wk X] | [Wk Y] | [N weeks] |
| Phase 2: [Name] | [Activities] | [Milestone] | [Wk X] | [Wk Y] | [N weeks] |
| Phase N: UAT & Go-Live | UAT execution, defect resolution, go-live | System live | [Wk X] | [Wk Y] | [N weeks] |
| Hypercare | Monitoring, support, knowledge transfer | Handover complete | [Wk X] | [Wk Y] | [N weeks] |

State total project duration and go-live date clearly.

---

### Section 14: Risks and Mitigation

| # | Risk | Probability | Impact | Mitigation Strategy | Owner |
|---|------|-------------|--------|---------------------|-------|
| R1 | [Risk description] | High/Med/Low | High/Med/Low | [Mitigation] | [Us/Client] |
| R2 | [Risk description] | High/Med/Low | High/Med/Low | [Mitigation] | [Us/Client] |

Include at minimum:
- Scope creep risk
- Data availability / quality risk
- Client resource availability risk
- Third-party dependency risk
- Technology integration risk
- Timeline compression risk

---

### Section 15: Assumptions

List all assumptions the proposal is based on. These protect scope and pricing.

1. Client will provide access to all relevant systems, data, and subject matter experts within [X] business days of kickoff.
2. All required licenses (platform, third-party tools) will be procured by [party] prior to [phase].
3. A dedicated client product owner will be available for [X] hours per week.
4. Existing data is in [format/quality] and does not require significant cleansing beyond [defined scope].
5. Infrastructure will be provisioned on [cloud platform] with [access level].
6. [Add any RFP-specific assumptions here]

> **Note**: Assumptions that turn out to be incorrect may result in scope or cost adjustments via the change management process.

---

### Section 16: Estimate, Staffing & Pricing

#### 16.1 Staffing Model

**Standard Blended Rate Model:**
- **Onshore**: 20% of total effort — **$100/hour**
- **Offshore**: 80% of total effort — **$40/hour**
- **Blended effective rate**: (0.20 × $100) + (0.80 × $40) = **$52/hour**

#### 16.2 Staffing Plan

| Role | Seniority | Location | % Allocation | Hours/Sprint | Phase(s) |
|------|----------|----------|-------------|-------------|---------|
| Engagement Manager | Senior | Onshore | 25% | [X hrs] | All |
| Solution Architect | Senior | Onshore | 50% | [X hrs] | Ph 0–2 |
| Tech Lead | Senior | Offshore | 100% | [X hrs] | All |
| Senior Developer | Mid | Offshore | 100% | [X hrs] | Ph 1–3 |
| Developer | Junior | Offshore | 100% | [X hrs] | Ph 1–3 |
| QA Engineer | Mid | Offshore | 100% | [X hrs] | Ph 2–4 |
| Business Analyst | Mid | Offshore | 75% | [X hrs] | All |
| UX Designer | Mid | Offshore | 50% | [X hrs] | Ph 0–2 |

#### 16.3 Effort & Cost Breakdown by Phase

| Phase | Onshore Hours | Offshore Hours | Onshore Cost | Offshore Cost | Phase Total |
|-------|--------------|----------------|-------------|---------------|-------------|
| Phase 0: Inception | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 1: [Name] | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 2: [Name] | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 3: [Name] | [X] | [X] | $[X] | $[X] | **$[X]** |
| Hypercare | [X] | [X] | $[X] | $[X] | **$[X]** |
| **TOTAL** | **[X]** | **[X]** | **$[X]** | **$[X]** | **$[X]** |

#### 16.4 Total Cost Summary

| Cost Component | Amount |
|---------------|--------|
| Professional Services (Labor) | $[X] |
| Infrastructure (if applicable) | $[X] |
| Third-party licenses (if applicable) | $[X] |
| Travel & expenses (if applicable) | $[X] |
| **TOTAL PROPOSAL VALUE** | **$[X]** |

> **Note**: All estimates are based on the assumptions in Section 15. Final pricing may be adjusted following a detailed discovery engagement.

#### 16.5 Payment Terms (suggested)
- 20% upon contract signing
- 20% at end of Phase 1 milestone
- 20% at end of Phase 2 milestone
- 20% at UAT sign-off
- 20% at go-live acceptance

---

## Phase 3: Quality Checklist Before Finalizing

Before delivering the response, verify:

- [ ] All RFP mandatory requirements appear in the Requirements Traceability Matrix (Section 10)
- [ ] Submission destination, format, and deadline are confirmed
- [ ] All key dates from the RFP calendar are captured
- [ ] Pricing uses exactly 20% onshore at $100/hr and 80% offshore at $40/hr
- [ ] Infrastructure section is present (non-Unqork) OR explicitly excluded (Unqork RFP)
- [ ] AI capabilities section reflects only what is actually in scope
- [ ] Assumptions cover all major dependencies on the client
- [ ] Risks include at minimum the 6 standard risk categories
- [ ] Executive summary can stand alone as a 1-page pitch

---

## Output Format

The proposal response must be delivered as a **single, well-structured Markdown (.md) file** with:
- A cover page header (client name, RFP title, submission date, our firm name)
- Numbered sections matching the TOC above
- Tables used for structured data (matrices, plans, pricing)
- Clear section breaks (`---`) between major sections
- No placeholder text left unreplaced — every `[bracket]` must be filled with actual content derived from the RFP

> **Final note**: A great proposal doesn't just answer the RFP — it tells a story. The story is: *"We understand your world better than anyone else, we have solved this before, and we are the lowest-risk path to success."* Every section should reinforce this narrative.
