---
name: detailed-estimation
description: >-
  Granular requirement-level effort estimation skill. Maps each functional and
  non-functional requirement to specific tasks, assigns roles, hours, and
  complexity. Outputs a detailed Excel workbook with requirement-to-effort
  traceability. Use as a standard step in every RFP pipeline alongside the
  high-level estimate.
license: "Internal use"
---

# Detailed Estimation Skill

This skill produces a granular, requirement-level effort estimation as an Excel workbook. Every requirement from the RFP Requirements Register is broken down into discrete tasks with role assignments, complexity ratings, and hour estimates.

---

## Part 1: Inputs Required

| Input | Source | Description |
|-------|--------|-------------|
| **Requirements Register** | `/rfp-requirements` output | Full list of FR, NFR, INT, DM requirements with IDs |
| **High-Level Estimate** | `/rfp-estimate` output | Phase plan, team roles, duration |
| **Deal Type** | Pre-flight | Unqork or AI — affects complexity multipliers |
| **Onshore/Offshore Split** | User-confirmed | % split for blended rate calculation |
| **Reuse Factor** | Deal-specific | 0-70% depending on existing accelerators |

---

## Part 2: Estimation Methodology

### Step 1: Requirement Decomposition
For each requirement (FR-001, NFR-001, INT-001, DM-001), decompose into tasks:

| Requirement Type | Typical Task Breakdown |
|-----------------|----------------------|
| **Functional (FR)** | Analysis → Design → Build → Unit Test → Integration Test → Documentation |
| **Non-Functional (NFR)** | Analysis → Implementation → Testing → Validation |
| **Integration (INT)** | Analysis → API Design → Build Adapter → Stub/Mock → Integration Test → E2E Test |
| **Data Migration (DM)** | Assessment → Mapping → ETL Build → Dry Run → Validation → Cutover |

### Step 2: Complexity Assessment
Rate each requirement's complexity:

| Complexity | Multiplier | Criteria |
|-----------|-----------|---------|
| **Simple** | 1.0x | Standard CRUD, known pattern, no integrations, single data source |
| **Medium** | 1.5x | Business logic, 1-2 integrations, moderate validation rules |
| **Complex** | 2.5x | Multi-system orchestration, complex rules engine, regulatory/compliance logic |
| **Very Complex** | 4.0x | AI/ML components, real-time processing, multi-party workflows, novel architecture |

### Step 3: Base Hours by Task Type

| Task | Simple (hrs) | Medium (hrs) | Complex (hrs) | Very Complex (hrs) |
|------|-------------|-------------|--------------|-------------------|
| Analysis & Design | 4 | 8 | 16 | 24 |
| Build / Development | 8 | 16 | 40 | 80 |
| Unit Testing | 2 | 4 | 8 | 16 |
| Integration Testing | 2 | 6 | 12 | 24 |
| Documentation | 1 | 2 | 4 | 8 |
| **Subtotal per Req** | **17** | **36** | **80** | **152** |

### Step 4: Role Assignment
Map tasks to roles:

| Task | Primary Role | Secondary Role |
|------|-------------|---------------|
| Analysis & Design | Solution Architect | Business Analyst |
| Build / Development | Developer (Unqork/AI) | Sr Developer |
| Unit Testing | Developer | QA Engineer |
| Integration Testing | QA Engineer | Developer |
| Documentation | Business Analyst | Developer |
| Code Review | Sr Developer / Architect | — |

### Step 5: Apply Adjustments

```
Adjusted Hours = Base Hours × Complexity Multiplier × (1 - Reuse Factor)

Additional overlays:
- Integration complexity: +20% for each external system integration
- Compliance requirements: +15% for SOC2/HIPAA/regulatory items
- Data migration: +25% for complex transformations or large volumes
- UAT support: +10% of total build effort
- Hypercare: +5% of total effort (post go-live support)
- Buffer/contingency: +10% of total (not shown to client)
```

---

## Part 3: Effort Roll-Up

### By Phase
Map requirements to project phases and aggregate:

```
Phase 0 (Inception): All Analysis tasks + environment setup
Phase 1 (Pilot/Sprint 1-3): High-priority FRs + core INTs
Phase 2 (Build/Sprint 4-8): Remaining FRs + NFRs + DMs
Phase 3 (Testing): All integration testing + UAT support
Phase 4 (Go-Live): Cutover + hypercare
```

### By Role
Aggregate hours across all requirements per role:

```
Role Total = Σ (hours assigned to role across all requirements)
FTE = Role Total / Available Hours per Phase
```

### Available Hours Reference
```
Hours per FTE per month: 160
Hours per FTE per week: 40
Hours per FTE per year: 1920 (48 working weeks)
```

---

## Part 4: Excel Output Specification

Generate using `openpyxl`. The workbook MUST contain these sheets:

### Sheet 1: Estimation Summary
| Field | Value |
|-------|-------|
| Client | [Name] |
| Deal Type | [Unqork / AI] |
| Total Requirements | [Count] |
| Total Estimated Effort | [X] hours / [Y] person-months |
| Onshore Effort | [X] hours ([Y]%) |
| Offshore Effort | [X] hours ([Y]%) |
| Reuse Factor Applied | [X]% |
| Duration | [X] months |
| Team Size (Peak) | [X] FTEs |

### Sheet 2: Detailed Requirement Estimation
**This is the core sheet** — one row per requirement with full traceability:

| Column | Description |
|--------|-------------|
| Req ID | FR-001, NFR-001, INT-001, DM-001 |
| Category | Functional / Non-Functional / Integration / Data Migration |
| Requirement Description | Full requirement text |
| Priority | Mandatory / Desired / Nice-to-have |
| Complexity | Simple / Medium / Complex / Very Complex |
| Analysis & Design (hrs) | Hours for A&D |
| Build (hrs) | Hours for development |
| Testing (hrs) | Hours for unit + integration testing |
| Documentation (hrs) | Hours for docs |
| Subtotal (hrs) | Sum of task hours |
| Reuse Adjustment | Hours saved from reuse |
| Adjusted Total (hrs) | Final hours after reuse |
| Primary Role | Lead role for this requirement |
| Phase | Which project phase |
| Notes | Assumptions, dependencies, risks |

### Sheet 3: Role-wise Effort Summary
| Role | Phase 0 | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Total Hours | FTEs |
|------|---------|---------|---------|---------|---------|-------------|------|
| Solution Architect | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| Business Analyst | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| Sr Developer | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| Developer | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| QA Engineer | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| **Total** | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** |

### Sheet 4: Phase-wise Breakdown
| Phase | Duration (weeks) | Requirements Covered | Total Hours | Key Deliverables |
|-------|-----------------|---------------------|-------------|-----------------|
| Phase 0: Inception | [X] | [IDs] | [X] | Discovery, env setup |
| Phase 1: [Name] | [X] | [IDs] | [X] | [Deliverables] |
| Phase 2: [Name] | [X] | [IDs] | [X] | [Deliverables] |
| Phase 3: Testing | [X] | All | [X] | SIT, UAT |
| Phase 4: Go-Live | [X] | — | [X] | Cutover, hypercare |

### Sheet 5: Complexity Distribution
| Complexity | Count | % of Total | Total Hours | Avg Hours/Req |
|-----------|-------|-----------|-------------|--------------|
| Simple | [X] | [Y]% | [Z] | [W] |
| Medium | [X] | [Y]% | [Z] | [W] |
| Complex | [X] | [Y]% | [Z] | [W] |
| Very Complex | [X] | [Y]% | [Z] | [W] |
| **Total** | **[X]** | **100%** | **[Z]** | **[W]** |

### Sheet 6: Assumptions & Exclusions
- All estimation assumptions listed
- Reuse factor justification
- Excluded items (infrastructure, licensing, L1 support, etc.)
- Dependencies on client (environments, access, SME availability)
- Risk contingency (internal — not shown to client)

---

## Part 5: Excel Formatting Standards

```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Package: openpyxl

# Formatting rules:
# - Header row: Blue fill (#003781), white bold text, frozen panes
# - Alternating row colors: white / light gray (#F2F2F2)
# - Auto-column-width based on content
# - Number format: #,##0 for hours, #,##0.0 for FTEs, 0% for percentages
# - Conditional formatting: Red for "Very Complex", Orange for "Complex"
# - Filters enabled on all data sheets
# - Summary sheet has bordered summary table with totals
# - Print area and page setup configured for A4 landscape
```

---

## Part 6: When to Use This Skill

**Always run as part of the standard RFP pipeline.** Every RFP response must include a detailed estimation alongside the high-level estimate.

Trigger this skill:
- As part of `/rfp-full` pipeline (always)
- When user runs `/rfp-detailed-estimate`
- When the RFP has granular requirements that need traceable effort mapping
- After `/rfp-requirements` has been completed (depends on requirement IDs)

**Output file**: `<client>_Detailed_Estimate.xlsx`

**Relationship to other deliverables**:
- **Input from**: `/rfp-requirements` (requirement IDs + descriptions) and `/rfp-estimate` (phases + roles)
- **Feeds into**: `/rfp-pricing` (hours by role feed into rate card multiplication)
- **Cross-check**: Total hours from detailed estimate should reconcile (within 10%) with high-level estimate
