---
name: pricing-calculator
description: >-
  Use this skill whenever the user needs to estimate effort, staffing, or pricing
  for a proposal, RFP response, or project estimate. Triggers include: "estimate
  this project", "build a pricing model", "staffing plan", "how much will this
  cost", "create a cost estimate", "pricing for this RFP", "effort breakdown",
  "rate card", "blended rate", "onshore offshore split", or any request to
  calculate project costs and generate staffing grids. This skill uses the
  standard Aiden AI rate card and pricing methodology derived from the Allianz
  and California Claims engagement models. Always use this skill when generating
  Section 16 (Estimate, Staffing & Pricing) of any RFP response.
license: "Internal use — Confidential"
---

# Pricing Calculator Skill

This skill provides the standard rate card, staffing model, and pricing methodology for generating accurate, consistent project estimates across all Aiden AI proposals.

---

## Part 1: Standard Rate Card (with Cost & Margin)

### 1.1 Onshore Roles — Selling Rate, Cost Rate & Margin

| Role | Abbr | Selling Rate ($/hr) | Cost Rate ($/hr) | Margin ($/hr) | Margin % | Daily Sell (8hrs) | Seniority | Typical Allocation |
|------|------|-------------------|-----------------|--------------|----------|-----------------|-----------|-------------------|
| Engagement Manager | EM | $160 | $120 | $40 | 25.0% | $1,280 | Senior | 25-50% all phases |
| Solution Architect | SA | $170 | $120 | $50 | 29.4% | $1,360 | Senior | 40-100% Phase 0-1 |
| AI Architect | AIA | $170 | $120 | $50 | 29.4% | $1,360 | Senior | 40-100% Phase 0-2 |
| Business Analyst | BA | $100 | $70 | $30 | 30.0% | $800 | Mid-Senior | 50-100% all phases |
| AI Engineer | AIE | $100 | $70 | $30 | 30.0% | $800 | Mid-Senior | 100% Build & Test |
| Unqork Developer | UQD | $100 | $70 | $30 | 30.0% | $800 | Mid-Senior | 100% Build & Test |
| QA Engineer | QA | $100 | $70 | $30 | 30.0% | $800 | Mid | 60-100% Test phases |

### 1.2 Offshore Roles — Selling Rate, Cost Rate & Margin

| Role | Abbr | Selling Rate ($/hr) | Cost Rate ($/hr) | Margin ($/hr) | Margin % | Daily Sell (8hrs) | Seniority | Typical Allocation |
|------|------|-------------------|-----------------|--------------|----------|-----------------|-----------|-------------------|
| Scrum Master | SM | $45 | $18 | $27 | 60.0% | $360 | Mid-Senior | 50-100% all phases |
| Solution Architect | SA-O | $55 | $22 | $33 | 60.0% | $440 | Senior | 25-50% support |
| Business Analyst | BA-O | $40 | $18 | $22 | 55.0% | $320 | Mid | 50-100% all phases |
| Developer | DEV-O | $40 | $18 | $22 | 55.0% | $320 | Mid | 100% Build & Test |
| Tester / QA | QA-O | $35 | $18 | $17 | 48.6% | $280 | Mid | 100% Test phases |
| UX Designer | UXD-O | $40 | $18 | $22 | 55.0% | $320 | Mid | 50-100% Phase 0-1 |
| UX Engineer | UXE-O | $35 | $18 | $17 | 48.6% | $280 | Mid | 50-100% Build |
| DevOps Engineer | DVO-O | $40 | $18 | $22 | 55.0% | $320 | Mid | 25-50% all phases |

### 1.3 Rate Card Rules

- **Cost rate** = actual loaded cost to Aiden AI (salary + benefits + overhead)
- **Selling rate** = price billed to the client
- **Margin** = Selling rate - Cost rate
- **Margin %** = Margin / Selling rate × 100
- **Never discount below cost rate** — flag to leadership if client demands rates below cost
- **Discount authority**: Up to 10% discount on selling rate can be approved by Engagement Manager. Above 10% requires VP approval.

### 1.4 Blended Rate & Margin Analysis

The standard blended rate depends on the onshore/offshore mix:

| Mix | Blended Sell Rate | Blended Cost Rate | Blended Margin | Margin % |
|-----|------------------|------------------|----------------|----------|
| 20% on / 80% off | ~$57/hr | ~$38/hr | ~$19/hr | ~33% |
| 30% on / 70% off | ~$67/hr | ~$44/hr | ~$23/hr | ~34% |
| 40% on / 60% off | ~$77/hr | ~$50/hr | ~$27/hr | ~35% |
| 50% on / 50% off | ~$87/hr | ~$56/hr | ~$31/hr | ~36% |

> **Default mix**: 30% onshore / 70% offshore unless client specifies otherwise.
> **Target blended margin by deal type:**
> - **Unqork deals**: 35% standard. Below 25% requires VP sign-off. Below 20% is a no-go unless strategic.
> - **AI deals (AIDAP / Aiden AI Builder)**: 45% standard. Below 35% requires VP sign-off. Below 25% is a no-go unless strategic.

---

## Part 2: Pricing Methodology

### 2.1 Two Supported Pricing Models

**Model A: Monthly FTE Allocation (California Claims method)**
- Best for: Large, multi-month engagements (6+ months)
- Grid: Roles x Months (M1, M2, ... M12+)
- Each cell = number of FTEs allocated that month
- Days = FTE x working days per month (default: 20)
- Hours = Days x 8
- Price = Hours x Hourly Rate

**Model B: Weekly FTE Allocation (Allianz method)**
- Best for: Shorter engagements, sprints, POCs (1-4 months)
- Grid: Roles x Weeks (W1, W2, ... W12+)
- Each cell = number of FTEs allocated that week
- Days = FTE x 5 (working days per week)
- Hours = Days x 8
- Price = Hours x Hourly Rate

> **Rule**: Use Model A for engagements > 3 months. Use Model B for engagements <= 3 months.

### 2.2 Phase-Based Effort Distribution

When total effort is known but phase breakdown is not, use these standard distributions:

| Phase | % of Total Effort | Description |
|-------|------------------|-------------|
| Phase 0: Project Setup & Planning | 10% | Discovery, environment setup, team onboarding, architecture finalization |
| Phase 1: Design | 15% | Detailed design, UX wireframes, data model, integration specs |
| Phase 2: Build & Test | 50% | Core development, unit testing, integration testing |
| Phase 3: UAT & Mock Production | 10% | User acceptance testing, performance testing, defect resolution |
| Phase 4: OCM & Training | 5% | Change management, user training, documentation |
| Phase 5: Go-Live & Hypercare | 10% | Deployment, monitoring, support, knowledge transfer |

### 2.3 Reuse Factors

When estimating offshore effort, apply reuse factors based on platform:

| Platform | Offshore Reuse Factor | Meaning |
|----------|---------------------|---------|
| Unqork | 20% | 20% of Unqork effort can be reused from prior accelerators |
| Custom / AI | 50% | 50% of AI effort can leverage existing AIDAP components |
| Guidewire | 15% | 15% reuse from standard configuration accelerators |
| Greenfield custom | 0% | No reuse — estimate full effort |

> **How to apply**: Effective offshore effort = Raw offshore effort x (1 - Reuse Factor)

---

## Part 3: Staffing Templates

### 3.1 Small Engagement (8-12 weeks, $150K-$300K)

| Location | Role | W1-2 | W3-4 | W5-8 | W9-10 | W11-12 |
|----------|------|------|------|------|-------|--------|
| Onshore | Engagement Manager | 0.25 | 0.25 | 0.25 | 0.25 | 0.5 |
| Onshore | Solution Architect | 0.5 | 0.5 | 0.25 | 0.25 | 0.25 |
| Onshore | Business Analyst | 1 | 0.5 | 0.25 | 0.25 | 0.5 |
| Offshore | Scrum Master | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Offshore | Developer x2 | 0.5 | 1 | 2 | 2 | 1 |
| Offshore | QA | - | - | 0.5 | 1 | 1 |
| Offshore | UX Designer | 1 | 0.5 | 0.25 | - | - |

### 3.2 Medium Engagement (3-6 months, $300K-$800K)

| Location | Role | M1 | M2 | M3 | M4 | M5 | M6 |
|----------|------|----|----|----|----|----|----|
| Onshore | Engagement Manager | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Onshore | Solution Architect | 1 | 1 | 0.5 | 0.5 | 0.5 | 0.5 |
| Onshore | AI Architect | 1 | 1 | 0.5 | 0.5 | 0.25 | 0.25 |
| Onshore | Business Analyst | 1 | 1 | 0.5 | 0.5 | 0.5 | 1 |
| Offshore | Scrum Master | 1 | 1 | 1 | 1 | 1 | 1 |
| Offshore | Developer x3 | 1 | 3 | 3 | 3 | 3 | 2 |
| Offshore | QA x2 | - | 1 | 2 | 2 | 2 | 1 |
| Offshore | UX Designer | 1 | 1 | 0.5 | 0.25 | - | - |
| Offshore | UX Engineer | 0.5 | 1 | 1 | 1 | 0.5 | - |
| Offshore | DevOps | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |

### 3.3 Large Engagement (6-12 months, $800K-$3M+)

| Location | Role | M1 | M2-3 | M4-6 | M7-9 | M10-11 | M12 |
|----------|------|----|----|----|----|----|----|
| Onshore | Engagement Manager | 1 | 1 | 1 | 1 | 1 | 1 |
| Onshore | Solution Architect | 1 | 1 | 1 | 1 | 1 | 1 |
| Onshore | AI Architect | 1 | 1 | 1 | 1 | 1 | 1 |
| Onshore | Business Analyst | 2 | 2 | 2 | 1 | 1 | 1 |
| Onshore | AI Engineer x2 | 1 | 2 | 2 | 2 | 2 | 1 |
| Onshore | Unqork Developer x2 | 1 | 2 | 2 | 2 | 1 | 1 |
| Onshore | QA | 1 | 1 | 1 | 1 | 1 | 1 |
| Offshore | Scrum Master | 1 | 1 | 1 | 1 | 1 | 1 |
| Offshore | Solution Architect | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Offshore | Developer x5+ | 1 | 5 | 6 | 6 | 4 | 2 |
| Offshore | QA x2 | 1 | 2 | 4 | 4 | 2 | 1 |
| Offshore | UX Designer | 1 | 1 | 1 | 0.5 | 0.5 | - |
| Offshore | UX Engineer | 0.5 | 1 | 1 | 1 | 0.5 | - |
| Offshore | DevOps | 1 | 1 | 1 | 1 | 1 | 1 |
| Offshore | BA | 1 | 1 | 1 | 1 | 1 | 1 |

---

## Part 4: Managed Operations / Post-Go-Live Support

### 4.1 Standard Support Staffing

For ongoing managed operations after go-live, use this template:

| Location | Role | Monthly FTE | Hourly Rate | Monthly Cost |
|----------|------|-------------|-------------|-------------|
| Onshore | Support Lead | 1 | $100 | $16,000 |
| Offshore | Support - AI | 1-3 | $40 | $6,400-$19,200 |
| Offshore | Support - Platform | 1-3 | $40 | $6,400-$19,200 |
| Offshore | Support - Infra/DevOps | 1 | $40 | $6,400 |

### 4.2 Support Estimation Rule

> **Standard rule**: Managed Operations effort = **20% of Build phase effort** annualized.
> Includes warranty support (typically 3 months) + on-call support for weekends/non-working hours.

---

## Part 5: How to Generate a Pricing Estimate

### Step 1: Determine Engagement Size

| Indicator | Small | Medium | Large |
|-----------|-------|--------|-------|
| Duration | 8-12 weeks | 3-6 months | 6-12+ months |
| Team size | 4-6 | 8-14 | 15-25+ |
| Budget range | $150K-$300K | $300K-$800K | $800K-$3M+ |
| Integrations | 1-3 | 4-8 | 8+ |
| Functional modules | 3-5 | 6-15 | 15+ |

### Step 2: Select Staffing Template

Pick the appropriate template from Part 3 and adjust based on:
- **Client requirements**: Add/remove roles as needed
- **Platform**: Add platform-specific roles (Unqork Creator, Guidewire configurator, etc.)
- **AI scope**: Scale AI Engineer/Architect count based on model complexity
- **Data migration**: Add Data Migration SME if in scope
- **OCM**: Add OCM Lead if organizational change management is required
- **Compliance**: Add Security Engineer for regulated industries

### Step 3: Build the Staffing Grid

Create a grid with:
- Rows = Roles (grouped by Onshore / Offshore)
- Columns = Time periods (weeks or months)
- Cells = FTE count per period

### Step 4: Calculate Totals (Revenue, Cost & Margin)

For each role:
```
Total Days = Sum of (FTE per period x working days per period)
Total Hours = Total Days x 8
Selling Price = Total Hours x Selling Rate
Internal Cost = Total Hours x Cost Rate
Margin = Selling Price - Internal Cost
Margin % = Margin / Selling Price x 100
```

For the project:
```
Total Onshore Hours = Sum of all onshore role hours
Total Offshore Hours = Sum of all offshore role hours

Revenue (Selling Price):
  Onshore Revenue = Sum of (onshore hours x respective selling rates)
  Offshore Revenue = Sum of (offshore hours x respective selling rates)
  Total Revenue = Onshore Revenue + Offshore Revenue

Cost:
  Onshore Cost = Sum of (onshore hours x respective cost rates)
  Offshore Cost = Sum of (offshore hours x respective cost rates)
  Total Cost = Onshore Cost + Offshore Cost

Margin:
  Total Margin = Total Revenue - Total Cost
  Margin % = Total Margin / Total Revenue x 100
  Blended Sell Rate = Total Revenue / Total Hours
  Blended Cost Rate = Total Cost / Total Hours
```

### Step 5: Apply Reuse Factors (if applicable)

```
Adjusted Offshore Effort = Raw Offshore Effort x (1 - Reuse Factor)
Adjusted Total Cost = Onshore Cost + (Adjusted Offshore Effort x Offshore Rate)
```

### Step 6: Add Infrastructure & Licenses (if applicable)

| Cost Component | Estimate Basis | Notes |
|---------------|---------------|-------|
| Cloud infrastructure | Per-environment monthly cost | Skip for Unqork — included in license |
| Platform licenses | Annual or per-user | Unqork, Guidewire, etc. |
| AI model costs | Per-token or monthly | Claude, OpenAI, etc. |
| Third-party tools | Annual license | Monitoring, CI/CD, etc. |
| Travel & expenses | Per-trip estimate | If onsite required |

### Step 7: Generate Summary Tables

**Table 1: Effort & Revenue by Phase** (Client-facing)

| Phase | Onshore Hours | Offshore Hours | Onshore Revenue | Offshore Revenue | Phase Total |
|-------|--------------|----------------|----------------|-----------------|-------------|
| Phase 0 | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 1 | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 2 | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 3 | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 4 | [X] | [X] | $[X] | $[X] | **$[X]** |
| Phase 5 | [X] | [X] | $[X] | $[X] | **$[X]** |
| **TOTAL** | **[X]** | **[X]** | **$[X]** | **$[X]** | **$[X]** |

**Table 2: Total Cost Summary** (Client-facing)

| Cost Component | Amount |
|---------------|--------|
| Professional Services (Onshore) | $[X] |
| Professional Services (Offshore) | $[X] |
| Infrastructure (if applicable) | $[X] |
| Licenses (if applicable) | $[X] |
| Travel & Expenses (if applicable) | $[X] |
| **TOTAL PROPOSAL VALUE** | **$[X]** |

**Table 3: Key Metrics** (Client-facing)

| Metric | Value |
|--------|-------|
| Total Effort (hours) | [X] |
| Onshore / Offshore Split | [X]% / [X]% |
| Blended Hourly Rate | $[X] |
| Duration | [X] months |
| Peak Team Size | [X] FTEs |
| Average Team Size | [X] FTEs |

**Table 4: Margin Analysis — INTERNAL ONLY (Never share with client)**

| Metric | Onshore | Offshore | Total |
|--------|---------|----------|-------|
| Total Hours | [X] | [X] | [X] |
| Revenue (Selling Price) | $[X] | $[X] | $[X] |
| Internal Cost | $[X] | $[X] | $[X] |
| **Gross Margin** | **$[X]** | **$[X]** | **$[X]** |
| **Margin %** | **[X]%** | **[X]%** | **[X]%** |

**Table 5: Per-Role Margin Breakdown — INTERNAL ONLY**

| Location | Role | Hours | Sell Rate | Revenue | Cost Rate | Cost | Margin | Margin % |
|----------|------|-------|-----------|---------|-----------|------|--------|----------|
| On | Engagement Manager | [X] | $160 | $[X] | $120 | $[X] | $[X] | 25.0% |
| On | Solution Architect | [X] | $170 | $[X] | $120 | $[X] | $[X] | 29.4% |
| On | AI Architect | [X] | $170 | $[X] | $120 | $[X] | $[X] | 29.4% |
| On | Business Analyst | [X] | $100 | $[X] | $70 | $[X] | $[X] | 30.0% |
| On | AI Engineer | [X] | $100 | $[X] | $70 | $[X] | $[X] | 30.0% |
| On | Unqork Developer | [X] | $100 | $[X] | $70 | $[X] | $[X] | 30.0% |
| On | QA Engineer | [X] | $100 | $[X] | $70 | $[X] | $[X] | 30.0% |
| Off | Scrum Master | [X] | $45 | $[X] | $18 | $[X] | $[X] | 60.0% |
| Off | Solution Architect | [X] | $55 | $[X] | $22 | $[X] | $[X] | 60.0% |
| Off | Business Analyst | [X] | $40 | $[X] | $18 | $[X] | $[X] | 55.0% |
| Off | Developer | [X] | $40 | $[X] | $18 | $[X] | $[X] | 55.0% |
| Off | Tester / QA | [X] | $35 | $[X] | $18 | $[X] | $[X] | 48.6% |
| Off | UX Designer | [X] | $40 | $[X] | $18 | $[X] | $[X] | 55.0% |
| Off | UX Engineer | [X] | $35 | $[X] | $18 | $[X] | $[X] | 48.6% |
| Off | DevOps Engineer | [X] | $40 | $[X] | $18 | $[X] | $[X] | 55.0% |
| | **TOTAL** | **[X]** | | **$[X]** | | **$[X]** | **$[X]** | **[X]%** |

**Table 6: Margin Health Check — INTERNAL ONLY**

| Check | Target | Actual | Status |
|-------|--------|--------|--------|
| Overall margin % | 35% (Unqork) / 45% (AI) | [X]% | PASS / WARN / FAIL |
| Onshore margin % | > 25% | [X]% | PASS / WARN / FAIL |
| Offshore margin % | > 45% | [X]% | PASS / WARN / FAIL |
| Blended sell rate | > $55/hr | $[X] | PASS / WARN / FAIL |
| No role below cost | All positive | [Y/N] | PASS / FAIL |
| Discount applied | < 10% | [X]% | PASS / WARN / FAIL |

> **Margin thresholds (Unqork deals):**
> - **PASS**: Margin % >= 35% — healthy deal, proceed
> - **WARN**: Margin % 25-35% — flag to leadership, justify strategically
> - **FAIL**: Margin % < 25% — requires VP approval or re-scope
>
> **Margin thresholds (AI deals):**
> - **PASS**: Margin % >= 45% — healthy deal, proceed
> - **WARN**: Margin % 35-45% — flag to leadership, justify strategically
> - **FAIL**: Margin % < 35% — requires VP approval or re-scope

### Step 8: Payment Terms (Standard)

| Milestone | % Payment | Trigger |
|-----------|-----------|---------|
| Contract Signing | 20% | Signed SOW |
| End of Phase 1 (Design) | 20% | Design sign-off |
| End of Phase 2 (Build) | 20% | Build completion |
| UAT Sign-Off | 20% | UAT acceptance |
| Go-Live Acceptance | 20% | Production deployment |

> **Alternative**: For large engagements, monthly invoicing based on actual effort may be preferred. Discuss with client.

---

## Part 6: Quick Estimation Shortcuts

### 6.1 Per-Feature Estimation

When detailed requirements are available but time is short:

| Feature Complexity | Effort (person-days) | Typical Team |
|-------------------|---------------------|-------------|
| Simple (CRUD, form, basic report) | 5-10 | 1 dev + 0.5 QA |
| Medium (workflow, integration, dashboard) | 15-30 | 2 dev + 1 QA + 0.5 BA |
| Complex (AI model, multi-system integration, rules engine) | 40-80 | 3 dev + 1 AI eng + 1 QA + 1 BA |
| Very Complex (real-time processing, multi-agent AI, large migration) | 80-160 | 5+ dev + 2 AI eng + 2 QA + 1 BA + 1 Arch |

### 6.2 Per-Integration Estimation

| Integration Complexity | Effort (person-days) | Description |
|-----------------------|---------------------|-------------|
| Simple API (REST, well-documented) | 5-8 | Standard CRUD API with good docs |
| Medium API (authentication, mapping) | 10-20 | OAuth, data transformation, error handling |
| Complex (legacy, SOAP, file-based) | 20-40 | Legacy system, poor docs, custom protocols |
| Real-time bidirectional | 30-50 | WebSocket, event-driven, guaranteed delivery |

### 6.3 T-Shirt Sizing to Effort

| T-Shirt Size | Total Effort (hours) | Duration | Budget Range | Team Size |
|-------------|---------------------|----------|-------------|-----------|
| XS | 500-1,000 | 4-6 weeks | $30K-$60K | 2-3 |
| S | 1,000-3,000 | 8-12 weeks | $60K-$200K | 4-6 |
| M | 3,000-8,000 | 3-6 months | $200K-$600K | 8-14 |
| L | 8,000-16,000 | 6-12 months | $600K-$1.5M | 15-20 |
| XL | 16,000-30,000 | 12-18 months | $1.5M-$3M | 20-30 |
| XXL | 30,000+ | 18+ months | $3M+ | 30+ |

---

## Part 7: Output Formats

When generating pricing, always produce:

1. **Staffing Grid** (Markdown table) — roles x time periods with FTE counts
2. **Cost Summary** (Markdown table) — phase-by-phase and total
3. **Key Metrics** — blended rate, split, duration, peak team
4. **Excel Export** (when requested) — generate a Python script using openpyxl to create a formatted `.xlsx` with:
   - Sheet 1: Staffing Grid (with conditional formatting)
   - Sheet 2: Cost Breakdown (with formulas)
   - Sheet 3: Summary Dashboard

---

## Part 8: Discount & Scenario Analysis

### 8.1 Discount Framework

| Discount Level | Approval | When to Use |
|---------------|----------|-------------|
| 0% (standard) | No approval needed | Default for all proposals |
| 1-5% | Engagement Manager | Competitive bid, minor price sensitivity |
| 6-10% | Director / VP Sales | Strategic client, multi-phase pipeline |
| 11-15% | VP + CFO | Enterprise-wide deal, annual commitment |
| 16-20% | CEO | Flagship client, market entry, reference account |
| > 20% | Not recommended | Re-scope instead of discounting |

### 8.2 How to Apply Discounts

```
Discounted Selling Rate = Standard Selling Rate x (1 - Discount %)
New Margin = Discounted Selling Rate - Cost Rate
New Margin % = New Margin / Discounted Selling Rate x 100

CRITICAL: If New Margin % falls below 20%, STOP and escalate.
```

**Example — 10% discount impact on onshore Solution Architect:**
```
Standard:   $170/hr sell - $120/hr cost = $50 margin (29.4%)
After 10%:  $153/hr sell - $120/hr cost = $33 margin (21.6%) ← WARN
After 15%:  $144.50/hr sell - $120/hr cost = $24.50 margin (17.0%) ← FAIL
```

### 8.3 Scenario Modeling

Always generate **three pricing scenarios** for internal review:

**Scenario A: Standard (recommended)**
- Standard rates, no discount
- Target margin: 35% (Unqork) / 45% (AI deals)

**Scenario B: Competitive**
- 5-10% discount on selling rates
- Offset by increasing offshore mix (e.g., 25/75 instead of 30/70)
- Target margin: 25-30% (Unqork) / 35-40% (AI deals)

**Scenario C: Strategic / Market Entry**
- 10-15% discount
- Maximize offshore (20/80 mix)
- Apply reuse factors aggressively
- Target margin: 20-25% (Unqork) / 25-30% (AI deals)
- Requires VP approval

### 8.4 Margin Improvement Levers

When margin is too low, use these levers (in order of preference):

| Lever | Impact | Risk |
|-------|--------|------|
| **Increase offshore ratio** | High — offshore margin is 48-60% vs onshore 25-35% | Client may require onshore presence |
| **Apply reuse factors** | Medium — reduces total effort | Must have reusable accelerators |
| **Reduce scope** | Medium — fewer features = fewer hours | Client may push back |
| **Extend timeline** | Low — same effort, but spread = fewer peak FTEs | Delays client value |
| **Reduce seniority** | Low — mid vs senior rates | Quality risk |
| **Phase the work** | Medium — Phase 1 contract + Phase 2 option | Revenue delay |

> **Never use these levers to improve margin:**
> - Cutting QA below 20% of dev effort (quality risk)
> - Removing discovery/Phase 0 (scope risk)
> - Removing hypercare (relationship risk)
> - Understaffing to hit a budget number (delivery risk)

### 8.5 Revenue & Margin Sensitivity Table

For quick reference — impact of discount on a $1M deal:

| Discount | Revenue | Cost (at 35% margin) | Margin | Margin % |
|----------|---------|---------------------|--------|----------|
| 0% | $1,000,000 | $650,000 | $350,000 | 35.0% |
| 5% | $950,000 | $650,000 | $300,000 | 31.6% |
| 10% | $900,000 | $650,000 | $250,000 | 27.8% |
| 15% | $850,000 | $650,000 | $200,000 | 23.5% |
| 20% | $800,000 | $650,000 | $150,000 | 18.8% |

---

## Part 9: Pricing Checklist

Before delivering any estimate, verify:

**Staffing & Effort:**
- [ ] All roles have correct selling rates AND cost rates from the standard rate card
- [ ] Onshore/offshore split is explicitly stated
- [ ] Engagement Manager is included in every estimate (minimum 25% allocation)
- [ ] Solution Architect is included for the full duration (can reduce allocation after Phase 1)
- [ ] QA effort is at least 20% of development effort
- [ ] Phase 0 (Setup) is included — never skip discovery
- [ ] Hypercare / warranty period is included (minimum 4 weeks)
- [ ] Reuse factors are applied correctly for the platform

**Pricing & Revenue:**
- [ ] Infrastructure costs are included (or explicitly excluded for Unqork)
- [ ] Payment terms are specified
- [ ] Total hours, blended sell rate, and peak team size are calculated
- [ ] Managed Operations is quoted separately if post-go-live support is in scope
- [ ] No role is priced above the standard rate card without explicit approval
- [ ] Travel & expenses are addressed (included, excluded, or at-cost)
- [ ] Any discount is within approval authority

**Margin (INTERNAL — before submission):**
- [ ] Per-role margin breakdown is calculated (Table 5)
- [ ] No role is priced below its cost rate
- [ ] Overall margin % is calculated and within target (30-40%)
- [ ] Onshore margin % is above 25%
- [ ] Offshore margin % is above 45%
- [ ] Margin Health Check table (Table 6) is completed
- [ ] If margin < 30%, justification is documented
- [ ] If margin < 20%, VP approval is obtained
- [ ] Three pricing scenarios are prepared for internal review (standard, competitive, strategic)
- [ ] Discount impact on margin is modeled if any discount is applied

---

> **Final reminder**: Pricing is where proposals are won or lost. Underprice and you lose margin or credibility when you can't deliver. Overprice and you lose the bid. The rate card above represents competitive market rates for Aiden AI's delivery model. Adjust team size, duration, and offshore mix — not rates — to fit the client's budget. Always generate the internal margin analysis (Tables 4-6) before finalizing. If the budget is genuinely too low for the scope, say so honestly rather than cutting corners on staffing. A deal at 15% margin is worse than no deal.
