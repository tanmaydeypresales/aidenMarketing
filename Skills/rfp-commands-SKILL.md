---
name: rfp-commands
description: >-
  Master command set for end-to-end RFP response workflow. Defines 13 slash
  commands that produce all required deliverables: analysis (MD+DOCX),
  requirements (MD+DOCX), response instructions (MD), estimate (MD), detailed
  estimation (Excel), pricing (Excel), response document (MD+DOCX), deck
  (HTML+PPTX via Marp), clarifications (Excel), architecture diagrams (SVG+HTML),
  support estimation (Excel), interactive prototypes (Streamlit/Gradio/HTML),
  and animated architecture diagrams (GIF via Pillow+imageio).
  Use when the user says "respond to this RFP", "run the full RFP pipeline",
  or invokes any /rfp-* command.
license: "Internal use"
---

# RFP Response Command Set

This skill defines the standard command pipeline for responding to any RFP. Each command produces specific deliverables and must be run in order. All outputs are saved to `RFP/<client-name>/`.

---

## Command Overview

| # | Command | What It Produces | Format | Depends On |
|---|---------|-----------------|--------|------------|
| 1 | `/rfp-analyze` | `<client>_RFP_Analysis` | **.md + .docx** | RFP document |
| 2 | `/rfp-requirements` | `<client>_Requirements` | **.md + .docx** | Step 1 |
| 3 | `/rfp-instructions` | `<client>_Response_Instructions` | .md | Steps 1-2 |
| 4 | `/rfp-estimate` | `<client>_Estimate` | .md | Steps 1-2 |
| 5 | `/rfp-detailed-estimate` | `<client>_Detailed_Estimate` | **.xlsx** (always Excel) | Steps 2, 4 |
| 6 | `/rfp-pricing` | `<client>_Pricing` | **.xlsx** (always Excel) | Steps 4-5 |
| 7 | `/rfp-respond` | `<client>_Response` | **.md + .docx** | Steps 1-6 |
| 8 | `/rfp-deck` | `<client>_Deck` | **.html + .pptx** (Marp) | Step 7 |
| 9 | `/rfp-clarifications` | `<client>_Clarifications` | **.xlsx** | Step 1 |
| 10 | `/rfp-architecture` | `<client>_Architecture_*.svg` | **.svg + .html** (svgwrite) | Step 7 |
| 11 | `/rfp-support-estimate` | `<client>_Support_Estimate` | **.xlsx** (always Excel) | Step 1 (if support in scope) |
| 12 | `/rfp-prototype` | `<client>_Prototype.*` | **.py + .html** (Streamlit/Gradio/HTML) | Step 7 |
| 13 | `/rfp-animated-diagram` | `<client>_Animated_*.gif` | **.gif + .py** (Pillow+imageio) | Step 10 |

**Shortcut:** `/rfp-full` runs all 13 commands in sequence.

---

## Pre-Flight Checklist (runs before ANY command)

Before executing any `/rfp-*` command:

1. **Identify the client name** — ask the user if not obvious from the RFP filename or content
2. **Create the output folder** — `RFP/<client-name>/` (create if it doesn't exist)
3. **Identify deal type** — Is this a **Unqork deal** or an **AI deal (AIDAP/Aiden AI Builder)**? This determines:
   - Margin targets: 35% (Unqork) vs 45% (AI)
   - Infrastructure section: skip for Unqork (included in license)
   - Platform skill to load: `Skills/unqork-rfp-skill.md` or `Skills/aiden-ai-rfp-SKILL.md`
4. **Load all relevant skills from CLAUDE.md** — always load:
   - `Skills/rfp-analyzer-SKILL.md`
   - `Skills/RFP_SKILL.md`
   - `Skills/pricing-calculator-SKILL.md`
   - `Skills/pptx-design-system-SKILL.md`
   - `Skills/detailed-estimation-SKILL.md`
   - `Skills/support-estimator-SKILL.md` (if support/managed services in scope)
   - Platform-specific skill (Unqork or Aiden AI)

---

## Command 1: `/rfp-analyze`

**Purpose**: Deep-read the RFP and produce a comprehensive intelligence document.

**Skill used**: `Skills/rfp-analyzer-SKILL.md` (all 7 phases)

**Input**: RFP document (PDF, DOCX, XLSX, or text)

**Process**:
1. Read every document, exhibit, and attachment in the RFP package
2. Execute all 7 phases from the RFP Analyzer skill:
   - Phase 1: Document Inventory
   - Phase 2: Timeline & Logistics Intelligence
   - Phase 3: Client Intelligence
   - Phase 4: Scope & Requirements Analysis (functional, non-functional, integrations, data migration)
   - Phase 5: Evaluation Intelligence
   - Phase 6: Risk & Gap Analysis (including Go/No-Go)
   - Phase 7: Response Planning
3. Generate the Analysis Summary block

**Output**:
- `RFP/<client-name>/<client>_RFP_Analysis.md`
- `RFP/<client-name>/<client>_RFP_Analysis.docx` (converted via `python-docx`)

**DOCX conversion**: After generating the MD file, convert to DOCX using `python-docx` with formatted headers, styled tables (blue header rows), and proper paragraph styling. Use Python path: `/c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe`.

**Contents**:
```
# <Client Name> — RFP Analysis
Generated: <date>
RFP Title: <title>

ANALYSIS SUMMARY
─────────────────────────────────
Client:              [Name]
RFP Title:           [Title]
Due Date:            [Date]
Deal Type:           [Unqork / AI]
Functional Reqs:     [X] total ([Y] mandatory)
Non-Functional Reqs: [X] total ([Y] mandatory)
Integrations:        [X]
Compliance Gaps:     [X]
Ambiguities:         [X]
Go/No-Go:            [RECOMMENDATION]
─────────────────────────────────

[Full 7-phase analysis follows...]
```

---

## Command 2: `/rfp-requirements`

**Purpose**: Extract and organize every requirement into a structured, traceable format.

**Skills used**: `Skills/rfp-analyzer-SKILL.md` (Phase 4), `Skills/RFP_SKILL.md` (Section 10)

**Input**: RFP document + output from `/rfp-analyze`

**Process**:
1. Pull all functional requirements from the analysis
2. Pull all non-functional requirements
3. Pull all integration requirements
4. Pull all data migration requirements
5. Assign unique IDs (FR-001, NFR-001, INT-001, DM-001)
6. Classify each as: Mandatory / Desired / Nice-to-have
7. Map compliance status: Full / Partial / Gap
8. Flag every gap with severity and mitigation option

**Output**:
- `RFP/<client-name>/<client>_Requirements.md`
- `RFP/<client-name>/<client>_Requirements.docx` (converted via `python-docx`)

**DOCX conversion**: After generating the MD file, convert to DOCX using `python-docx` with formatted headers, styled tables (blue header rows), and proper paragraph styling.

**Contents**:
```markdown
# <Client Name> — Requirements Register

## Summary
| Category | Total | Mandatory | Gaps | Partial |
|----------|-------|-----------|------|---------|
| Functional | [X] | [Y] | [Z] | [W] |
| Non-Functional | [X] | [Y] | [Z] | [W] |
| Integration | [X] | [Y] | [Z] | [W] |
| Data Migration | [X] | [Y] | [Z] | [W] |

## Functional Requirements
| Req ID | Category | Description | Priority | Mandatory | Complexity | Compliance | Gap Mitigation |
|--------|----------|-------------|----------|-----------|------------|------------|----------------|
| FR-001 | ... | ... | ... | ... | ... | Full/Partial/Gap | ... |

## Non-Functional Requirements
| Req ID | Category | Description | Target | Compliance | Gap Mitigation |
|--------|----------|-------------|--------|------------|----------------|
| NFR-001 | ... | ... | ... | Full/Partial/Gap | ... |

## Integration Requirements
| Req ID | System | Direction | Protocol | Frequency | Data | Mandatory | Compliance |
|--------|--------|-----------|----------|-----------|------|-----------|------------|
| INT-001 | ... | ... | ... | ... | ... | ... | ... |

## Data Migration Requirements
| Req ID | Source | Volume | Type | Historical | Compliance |
|--------|--------|--------|------|------------|------------|
| DM-001 | ... | ... | ... | ... | ... |

## Compliance Gap Register
| Req ID | Requirement | Gap | Severity | Mitigation |
|--------|-------------|-----|----------|------------|
| ... | ... | ... | Critical/High/Med/Low | ... |

## Ambiguity Register
| # | Section | Ambiguity | Clarification Question | Impact |
|---|---------|-----------|------------------------|--------|
| 1 | ... | ... | ... | ... |
```

---

## Command 3: `/rfp-instructions`

**Purpose**: Generate a response instruction file that tells the proposal team exactly what to write, in what order, with what emphasis.

**Skills used**: `Skills/RFP_SKILL.md`, `Skills/rfp-analyzer-SKILL.md` (Phase 5 & 7)

**Input**: Outputs from `/rfp-analyze` and `/rfp-requirements`

**Process**:
1. Map RFP sections to response sections (from Phase 7 Response Planning)
2. Extract evaluation criteria and weights
3. Define win themes and how each section reinforces them
4. Specify page/word targets per section based on weight
5. List mandatory inclusions per section (forms, certifications, references)
6. Flag sections that need client-specific case studies
7. Define review/approval workflow

**Output**: `RFP/<client-name>/<client>_Response_Instructions.md`

**Contents**:
```markdown
# <Client Name> — Response Instructions

## Deal Profile
| Field | Value |
|-------|-------|
| Client | [Name] |
| RFP Title | [Title] |
| Due Date | [Date + Time + Timezone] |
| Deal Type | [Unqork / AI] |
| Target Margin | [35% / 45%] |
| Submission Format | [PDF/Word/Portal] |
| Page Limit | [If any] |

## Win Themes
These themes must be woven into EVERY section of the response:

1. **[Theme 1]**: [Description] — Reinforce in Sections: [1, 2, 6, 12]
2. **[Theme 2]**: [Description] — Reinforce in Sections: [1, 3, 9, 11]
3. **[Theme 3]**: [Description] — Reinforce in Sections: [1, 4, 6, 10]

## Section-by-Section Instructions

### Section 1: Executive Summary
- **Weight in evaluation**: [X%]
- **Target length**: [1-2 pages]
- **Must include**: [Client's core challenge, our differentiators, timeline commitment]
- **Tone**: Confident, client-centric, no jargon
- **Win themes to emphasize**: [Theme 1, Theme 3]
- **Mandatory forms/attachments**: [None / List]

### Section 2: Why Our Solution Is a Great Fit
- **Weight in evaluation**: [X%]
- **Target length**: [1 page]
- **Must include**: [Fit matrix mapping client priorities to our strengths]
- **Case studies needed**: [Yes — similar industry/scale/technology]
- **Win themes to emphasize**: [Theme 1, Theme 2]

[... repeat for all 16 sections ...]

## Mandatory Inclusions Checklist
- [ ] [Form A — completed and signed]
- [ ] [Certificate of Insurance]
- [ ] [3 client references with contact details]
- [ ] [Compliance attestation for all mandatory requirements]
- [ ] [Pricing in required format]

## Submission Checklist
- [ ] Response follows RFP section ordering
- [ ] Page limit respected
- [ ] Font/margin requirements met
- [ ] All mandatory forms attached
- [ ] File named per convention: [convention]
- [ ] Submitted to: [destination]
- [ ] Submitted by: [date + time + timezone]

## Review & Approval
| Reviewer | Section(s) | Review By |
|----------|-----------|-----------|
| [Engagement Manager] | All | [Date] |
| [Solution Architect] | 6, 7, 8, 9 | [Date] |
| [Pricing Lead] | 16 | [Date] |
```

---

## Command 4: `/rfp-estimate`

**Purpose**: Generate effort estimate with role-by-role hours, phase breakdown, and staffing plan.

**Skills used**: `Skills/pricing-calculator-SKILL.md` (Parts 2-6)

**Input**: Requirements from `/rfp-requirements`, scope from `/rfp-analyze`

**Process**:
1. Determine engagement size: S / M / L (from pricing calculator Part 5)
2. Select pricing model: Monthly FTE (>3 months) or Weekly FTE (<=3 months)
3. Define phases and map requirements to phases
4. Assign roles per phase with allocation %
5. Calculate hours per role per phase
6. **Determine onshore/offshore split** — check with the user whether onshore involvement is needed and what %. Default is 30/70 onshore/offshore unless the user specifies otherwise (e.g., 0% onshore for cost-optimized deals)
7. Apply reuse factors where applicable (AI reuse factor can range from 30-70% depending on deal)
8. Calculate total effort in person-months and hours
9. Include effort drivers summary

**Output**: `RFP/<client-name>/<client>_Estimate.md`

**Contents**:
```markdown
# <Client Name> — Effort Estimate

## Estimate Summary
| Metric | Value |
|--------|-------|
| Total Duration | [X] months |
| Total Effort | [X] person-months / [Y] hours |
| Onshore Effort | [X] hours ([Y]%) |
| Offshore Effort | [X] hours ([Y]%) |
| Team Size (peak) | [X] FTEs |
| Engagement Size | S / M / L |
| Pricing Model | Monthly FTE / Weekly FTE |

## Effort Drivers
| Factor | Value | Impact |
|--------|-------|--------|
| Functional modules | [X] | [High/Med/Low] |
| Integrations | [X] | [High/Med/Low] |
| Data migration | [Complexity] | [High/Med/Low] |
| Customization level | [Heavy/Moderate/Light] | [High/Med/Low] |
| Compliance requirements | [List] | [High/Med/Low] |

## Phase Plan
| Phase | Duration | Key Deliverables |
|-------|----------|-----------------|
| Phase 0: Inception | [X] weeks | Discovery, env setup, kickoff |
| Phase 1: [Name] | [X] weeks | [Deliverables] |
| ... | ... | ... |

## Staffing Plan — Role x Phase Matrix
| Role | Location | Ph 0 | Ph 1 | Ph 2 | Ph 3 | UAT | Hypercare | Total Hours |
|------|----------|------|------|------|------|-----|-----------|-------------|
| Engagement Manager | Onshore | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| Solution Architect | Onshore | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **Phase Totals** | | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** |

## Reuse & Acceleration Factors
| Component | Standard Effort | Reuse Factor | Adjusted Effort | Savings |
|-----------|----------------|--------------|-----------------|---------|
| [Component] | [X] hrs | [Y]% | [Z] hrs | [W] hrs |

## Assumptions
1. [Estimation assumption 1]
2. [Estimation assumption 2]
3. ...
```

---

## Command 5: `/rfp-detailed-estimate`

**Purpose**: Generate a granular, requirement-level effort estimation as an Excel workbook with full traceability from each requirement to tasks, roles, and hours.

**Skill used**: `Skills/detailed-estimation-SKILL.md`

**Input**: Requirements from `/rfp-requirements`, phases/roles from `/rfp-estimate`

**Process**:
1. Take every requirement (FR-xxx, NFR-xxx, INT-xxx, DM-xxx) from the Requirements Register
2. Assess complexity per requirement: Simple / Medium / Complex / Very Complex
3. Decompose each into tasks: Analysis & Design → Build → Testing → Documentation
4. Assign base hours per task using complexity multipliers (1.0x / 1.5x / 2.5x / 4.0x)
5. Apply reuse factor where applicable
6. Apply overlays: integration complexity (+20%), compliance (+15%), data migration (+25%), UAT (+10%), hypercare (+5%)
7. Map each requirement to a project phase
8. Assign roles per task
9. Roll up by role, by phase, and by complexity
10. Cross-check total against high-level estimate (within 10% tolerance)
11. Generate Excel with 6 sheets

**Output**: `RFP/<client-name>/<client>_Detailed_Estimate.xlsx`

**Excel Sheets**:

| Sheet | Contents | Client-Facing? |
|-------|----------|---------------|
| Estimation Summary | Totals, FTEs, duration, reuse factor | Yes |
| Detailed Requirement Estimation | One row per requirement — full breakdown | Yes |
| Role-wise Effort Summary | Hours by role by phase | Yes |
| Phase-wise Breakdown | Requirements mapped to phases with hours | Yes |
| Complexity Distribution | Count and hours by complexity level | Yes |
| Assumptions & Exclusions | All estimation assumptions | Yes |

**Generation method**: Use `openpyxl` via Python:
```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Formatting: blue header row (#003781), alternating rows, auto-width, filters, conditional formatting for complexity
```

**Cross-check rule**: Total hours from detailed estimate must reconcile (within 10%) with the high-level estimate from `/rfp-estimate`. If divergence > 10%, flag it and explain the delta.

---

## Command 6: `/rfp-pricing`

**Purpose**: Generate the commercial pricing file with rate card, cost breakdown, margin analysis, and scenarios.

**Skills used**: `Skills/pricing-calculator-SKILL.md` (Parts 1, 7, 8)

**Input**: Estimate from `/rfp-estimate`

**Process**:
1. Apply rate card from pricing calculator (Part 1) to estimated hours
2. Calculate per-role revenue: hours x selling rate
3. Calculate per-role cost: hours x cost rate
4. Calculate per-role margin and margin %
5. Generate blended rates for the specific onshore/offshore mix
6. Build 3 pricing scenarios: Standard, Competitive, Strategic
7. Run margin health check (Table 6) against deal-type thresholds
8. Generate Excel file with sheets: Summary, Detail by Phase, Rate Card, Scenarios, Margin Analysis (INTERNAL)
9. Mark Tables 4-6 as INTERNAL ONLY — never include in client-facing documents

**Output**: `RFP/<client-name>/<client>_Pricing.xlsx`

**Excel Sheets**:

| Sheet | Contents | Client-Facing? |
|-------|----------|---------------|
| Summary | Total cost, payment terms, blended rate | Yes |
| Phase Breakdown | Cost by phase, onshore/offshore split | Yes |
| Staffing & Rates | Role, rate, hours, cost per role | Yes |
| Rate Card | Standard selling rates only | Yes |
| Scenario Comparison | Standard / Competitive / Strategic | Internal |
| Margin Analysis | Cost rates, margins, health check | **INTERNAL ONLY** |

**Generation method**: Use `openpyxl` via Python to create formatted Excel:
```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Package: openpyxl (already installed)
```

**Margin thresholds applied**:
- Unqork deals: PASS >= 35%, WARN 25-35%, FAIL < 25%
- AI deals: PASS >= 45%, WARN 35-45%, FAIL < 35%

---

## Command 7: `/rfp-respond`

**Purpose**: Generate the full proposal response document following the 16-section structure.

**Skills used**: `Skills/RFP_SKILL.md` (all sections), platform skill (Unqork or Aiden AI)

**Input**: All outputs from commands 1-5

**Process**:
1. Load response instructions from `/rfp-instructions` output
2. Follow the 16-section structure from the RFP Response skill
3. Fill every section with content derived from the RFP — no placeholders
4. Incorporate win themes throughout
5. Build Requirements Traceability Matrix from `/rfp-requirements` output
6. Insert staffing and pricing from `/rfp-estimate` and `/rfp-pricing`
7. Apply platform-specific content (Unqork or AI)
8. Run the quality checklist from Phase 3 of the RFP Response skill
9. Ensure every mandatory requirement is addressed

**Output**:
- `RFP/<client-name>/<client>_Response.md`
- `RFP/<client-name>/<client>_Response.docx` (converted via `python-docx`)

**DOCX conversion**: After generating the MD file, convert to DOCX using `python-docx` with formatted headers, styled tables (blue header rows), and proper paragraph styling.

**Contents**: Full 16-section proposal response per `Skills/RFP_SKILL.md`:
1. Executive Summary
2. Why Our Solution Is a Great Fit
3. Our Understanding of the Problem Statement
4. Scope of Work
5. What Is Out of Scope
6. Solution Architecture (Detailed)
7. Solution Components (Detailed Descriptions)
8. Infrastructure Requirements (skip for Unqork)
9. Key AI Capabilities
10. Requirements Traceability Matrix
11. As-Is to To-Be State View
12. Delivery Approach
13. Project Plan
14. Risks and Mitigation
15. Assumptions
16. Estimate, Staffing & Pricing

**Quality gate** — response cannot be finalized until all checklist items pass:
- [ ] All mandatory requirements appear in Traceability Matrix
- [ ] Submission format and deadline confirmed
- [ ] All key dates captured
- [ ] Pricing uses correct rate card and margin targets
- [ ] Infrastructure section handled correctly for deal type
- [ ] AI capabilities section matches actual scope
- [ ] Assumptions cover all client dependencies
- [ ] Risks include all 6 standard categories
- [ ] Executive summary works as standalone 1-page pitch
- [ ] No `[bracket]` placeholders remain
- [ ] Win themes are present in at least Sections 1, 2, 3, 6

---

## Command 8: `/rfp-deck`

**Purpose**: Generate a professional presentation summarizing the proposal.

**Skills used**: `Skills/pptx-design-system-SKILL.md` (for color/brand reference)

**Input**: Response document from `/rfp-respond`, architecture diagrams from `/rfp-architecture`

**Process**:
1. Create a Marp markdown file with comprehensive custom CSS design system
2. Structure the deck as 15-20 slides with **detailed content pulled from the response document** (not just summaries):

| Slide # | Title | Content Source |
|---------|-------|---------------|
| 1 | Title Slide | Client name, RFP title, date, Aiden AI branding |
| 2-3 | Executive Summary | Section 1 — full key points with metric cards |
| 4 | Why Aiden AI | Section 2 — fit matrix as visual cards |
| 5 | Understanding Your Challenge | Section 3 — problem reframed with detail |
| 6 | Scope of Work | Section 4 — workstream overview |
| 7-8 | Solution Architecture | Section 6 — **include architecture diagrams** from `/rfp-architecture` |
| 9-10 | AI Pipeline / Components | Section 7+9 — detailed component + capability cards |
| 11 | As-Is → To-Be | Section 11 — transformation visual |
| 12 | Transformation Benefits | Quantified outcomes with metric cards |
| 13-14 | Delivery Approach | Section 12 — methodology + timeline |
| 15 | Risks & Mitigation | Section 14 — top risks table |
| 16 | Team & Staffing | Section 16.1-16.2 — roles + allocation |
| 17 | Investment Summary | Section 16.3-16.4 — pricing summary (client-facing only) |
| 18 | Win Themes | Differentiators and key strengths |
| 19 | Assumptions | Key assumptions that client needs to confirm |
| 20 | Next Steps | Contact info, timeline, call to action |

3. **Must include architecture diagrams as slides** — reference the Mermaid diagrams from `/rfp-architecture`
4. Apply custom CSS design system in the Marp front matter:
   - Brand colors: `--brand-blue: #003781`, `--dark-navy: #1A1A2E`, `--deep-blue: #003366`, `--orange: #ED7D31`
   - CSS classes: `.card`, `.card-orange`, `.card-green`, `.metric`, `.metric-number`, `.columns`, `.tag`
   - Section classes: `.title`, `.section-divider`, `.dark`
5. Export to both HTML and PPTX using Marp CLI

**Output**:
- `RFP/<client-name>/<client>_Deck.html` (best viewing quality)
- `RFP/<client-name>/<client>_Deck.pptx` (for editing/sharing)
- `RFP/<client-name>/<client>_Deck.md` (Marp source)

**Generation method** — use Marp (NOT python-pptx):
```bash
# Generate PPTX from Marp markdown
npx @marp-team/marp-cli <client>_Deck.md -o <client>_Deck.pptx --html true

# Generate HTML from Marp markdown
npx @marp-team/marp-cli <client>_Deck.md -o <client>_Deck.html --html true
```

**Quality rules**:
- Every slide must have substantive content from the response document — no generic filler
- Use CSS card components for key metrics and highlights
- Architecture slides must show the actual system design, not just text
- Minimum 15 slides; more if the response document has sufficient detail
- Include page numbers and Aiden AI branding on every slide

---

## Command 9: `/rfp-clarifications`

**Purpose**: Generate a structured list of clarification questions to send to the client before finalizing the response.

**Skills used**: `Skills/rfp-analyzer-SKILL.md` (Phase 6 — Ambiguity Register)

**Input**: RFP document + output from `/rfp-analyze` (especially ambiguities, gaps, and assumptions)

**Process**:
1. Extract all ambiguities identified in the RFP analysis
2. Extract all compliance gaps that need client confirmation
3. Identify assumptions that carry risk if wrong
4. Categorize questions by topic: Scope, Technical, Commercial, Timeline, Compliance, Data, Integration
5. Prioritize: Critical (blocks response), Important (affects pricing/scope), Nice-to-have (clarifies detail)
6. Generate Excel file with structured question format

**Output**: `RFP/<client-name>/<client>_Clarifications.xlsx`

**Excel structure**:

| Column | Description |
|--------|-------------|
| # | Sequential question number |
| Category | Scope / Technical / Commercial / Timeline / Compliance / Data / Integration |
| Priority | Critical / Important / Nice-to-have |
| RFP Section | Section reference in the original RFP |
| Question | The clarification question |
| Context | Why this question matters / what it impacts |
| Impact if Unresolved | What we'll assume if not answered |
| Status | Open (default — client fills in response) |
| Client Response | Blank (for client to fill) |

**Generation method**: Use `openpyxl` via Python to create formatted Excel:
```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Package: openpyxl (already installed)
# Formatting: blue header row, alternating row colors, auto-column-width, filters enabled
```

---

## Command 10: `/rfp-architecture`

**Purpose**: Generate high-quality technical architecture diagrams using `svgwrite` (Python SVG library), bundled into an HTML viewer.

**Input**: Response document from `/rfp-respond` (Section 6 — Solution Architecture)

**Process**:
1. Identify the key architecture views needed based on the solution:
   - **Architecture Overview** — high-level system context showing all layers and external systems (e.g., AIDAP Five-Layer)
   - **Migration/Processing Pipeline** — data flow or transformation pipeline with AI agents
   - **Target State Architecture** — detailed target architecture with all layers (presentation, application, data, infrastructure)
   - **LLM Gateway / AI Routing** — multi-model intelligent routing diagram (if AI deal)
   - Additional views as needed (integration architecture, data architecture, security architecture)
2. Generate a Python script (`generate_architecture_diagrams.py`) using `svgwrite` that creates all diagrams as SVG files
3. Run the script to produce SVG files + an HTML viewer that displays all diagrams on a single page
4. Architecture diagrams are also referenced/included in the deck (Command 7)

**Output**:
- `RFP/<client-name>/<client>_Architecture_<view>.svg` (one per diagram — scalable vector graphics)
- `RFP/<client-name>/<client>_Architecture_Diagrams.html` (single-page HTML viewer wrapping all SVGs)
- `RFP/<client-name>/generate_architecture_diagrams.py` (source script for regeneration)

**Minimum diagrams** (always generate at least these 3-4):
1. `<client>_Architecture_FiveLayer.svg` — System context / platform architecture layers
2. `<client>_Migration_Pipeline.svg` or `<client>_Processing_Pipeline.svg` — Core processing flow with agents
3. `<client>_Target_Architecture.svg` — Detailed target state with all layers and components
4. `<client>_LLM_Gateway.svg` — Multi-model routing (for AI deals only)

**Generation method** — use `svgwrite` Python library (NOT Mermaid, NOT Plotly, NOT matplotlib):
```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Package: svgwrite (installed)

# Design standards for all architecture SVGs:
# - Dark background gradient (#0F1B2D → #1A365D)
# - Brand colors: BRAND_BLUE=#003781, ORANGE=#ED7D31, GREEN=#27AE60, TEAL=#1ABC9C, PURPLE=#8E44AD
# - Rounded rectangles for layer containers (rx=10-12)
# - Color-coded accent bars on left edge of each layer
# - Component cards inside layers with semi-transparent backgrounds
# - Icon circles for agents/services
# - Connecting arrows between layers (dashed, semi-transparent)
# - Aiden AI branding and confidential footer
# - Minimum size: 1200x700 per diagram
```

**HTML viewer template** — single page showing all SVGs:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title><Client> — Architecture Diagrams</title>
    <style>
        body { background: #0F1B2D; color: white; font-family: 'Segoe UI', sans-serif; }
        .header h1 { color: #5BA4E6; text-align: center; }
        .diagram-section h2 { color: #ED7D31; border-left: 4px solid #ED7D31; padding-left: 15px; }
        .diagram-container { background: #1A1A2E; border-radius: 12px; padding: 20px; border: 1px solid #2C3E50; }
        .diagram-container img { width: 100%; height: auto; }
    </style>
</head>
<body>
    <!-- One section per SVG diagram -->
</body>
</html>
```

**Architecture slide in deck**: The deck (Command 7) MUST include at least one architecture slide showing the system design. Reference the architecture diagrams generated here.

**Quality rules**:
- Every diagram must have substantive detail — not just boxes with labels
- Each layer/phase must show specific components, technologies, and data flows
- Use consistent color coding across all diagrams
- Diagrams must be self-explanatory without additional text

---

## Command 11: `/rfp-support-estimate`

**Purpose**: Generate a comprehensive IT application support estimation and pricing model as an Excel workbook. Covers 24x7, 16x5, or 8x5 coverage models with on-call arrangements.

**Skill used**: `Skills/support-estimator-SKILL.md`

**Input**: RFP document + `/rfp-analyze` output (to identify support requirements)

**When to run**: Only when the RFP includes application support, managed services, production support, L1/L2/L3 tiers, SLA requirements, helpdesk, hypercare, or AMS. The `/rfp-full` pipeline auto-detects this from the analysis.

**Process**:
1. Gather inputs from RFP: coverage model, number of apps, users, ticket volume, contract duration, location
2. Ask the user for any missing inputs (use defaults from the skill if not specified)
3. Calculate ticket volumes by tier (L1 50%, L2 30%, L3 5%/10%/5%)
4. Calculate effort hours by tier using standard hours/ticket
5. Add overlays: monitoring (10%), L4 escalation (10%), management (25%), on-call (10%)
6. Calculate FTEs with efficiency factor (10% YoY improvement)
7. Determine shift roster based on coverage model
8. Calculate pricing using standard rates ($30/hr offshore support, $35/hr offshore manager)
9. Build 3 pricing scenarios: Standard, Competitive (-10%), Strategic (-15-20%)
10. Generate Excel with 6 sheets

**Output**: `RFP/<client-name>/<client>_Support_Estimate.xlsx`

**Excel Sheets**:

| Sheet | Contents | Client-Facing? |
|-------|----------|---------------|
| Support Summary | Coverage model, apps, contract value | Yes |
| Ticket Volume & Effort | Volumes, hours, FTEs by year | Yes |
| Staffing Plan | Roles, shifts, on-call rotation | Yes |
| Pricing | Annual cost by role, total per year | Yes |
| Assumptions | SLAs, exclusions, dependencies | Yes |
| Scenarios | Standard/Competitive/Strategic pricing | **INTERNAL ONLY** |

**Generation method**: Use `openpyxl` via Python:
```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Formatting: blue header row, multi-year columns, conditional formatting for scenarios
```

---

## Command 12: `/rfp-prototype`

**Purpose**: Generate interactive UI prototypes and AI demos that can be shown during client presentations or shared as clickable demos.

**Input**: Response document from `/rfp-respond` (Sections 6, 7, 11 — solution architecture, components, as-is/to-be)

**Process**:
1. Identify key user-facing workflows from the solution scope (e.g., portal, workbench, dashboard, AI chat)
2. Determine the best prototype format for each:
   - **Streamlit** — For data-driven UIs: dashboards, analytics views, form workflows, admin panels
   - **Gradio** — For AI demos: chatbots, document processors, model playgrounds, agent interactions
   - **Single-file HTML** — For static interactive mockups: login screens, multi-step wizards, landing pages
3. Generate prototype files with realistic mock data derived from the RFP
4. Each prototype must be self-contained and runnable without additional setup
5. Take screenshots of key screens for embedding in the deck

**Output**:
- `RFP/<client-name>/<client>_Prototype.py` — Streamlit app (run with: `streamlit run <file>`)
- `RFP/<client-name>/<client>_AI_Demo.py` — Gradio app (run with: `python <file>`) — for AI deals only
- `RFP/<client-name>/<client>_UI_Prototype.html` — Static HTML mockup (open in browser)

**Prototype selection guide**:

| RFP Scope | Prototype Type | Tool |
|-----------|---------------|------|
| Portal / Self-service UI | Multi-page app with forms, tables, status tracking | Streamlit |
| Underwriting workbench | Data grids, filters, decision panels | Streamlit |
| Analytics dashboard | Charts, KPIs, filters | Streamlit |
| AI chatbot / copilot | Conversational interface with mock responses | Gradio |
| Document processing | Upload → extract → review workflow | Gradio |
| AI agent demo | Multi-step agent with tool calls | Gradio |
| Login / landing page | Branded static page | HTML |
| Multi-step wizard | Step-by-step form flow | HTML |
| Mobile-responsive UI | Responsive layout demo | HTML |

**Generation rules**:
- Always generate at least 1 prototype (Streamlit or HTML depending on scope)
- For AI deals, always generate a Gradio AI demo in addition
- Use the client's industry domain for mock data (insurance terms, healthcare, energy, etc.)
- Apply Aiden AI brand colors: `#003781` (blue), `#ED7D31` (orange), `#1A1A2E` (dark navy)
- Include Aiden AI logo reference and "Powered by Aiden AI" footer
- Streamlit apps must use `st.set_page_config(layout="wide")` for professional appearance

**Running prototypes**:
```bash
# Streamlit (interactive web app on localhost:8501)
/c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe -m streamlit run <client>_Prototype.py

# Gradio (interactive web app on localhost:7860)
/c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe <client>_AI_Demo.py

# HTML (just open in browser)
start <client>_UI_Prototype.html
```

---

## Command 13: `/rfp-animated-diagram`

**Purpose**: Generate animated architecture/flow diagrams as GIF files with moving dashed arrows showing data flow between components.

**Skill used**: `Skills/animated-diagram-SKILL.md`

**Input**: Architecture diagrams from `/rfp-architecture`, response document from `/rfp-respond`

**Process**:
1. Identify key architecture flows that benefit from animation:
   - **Migration Pipeline** — data flowing through discovery → analysis → transformation → testing → deployment
   - **Architecture Overview** — requests flowing between layers (presentation → API → business logic → data)
   - **AI Agent Flow** — orchestrator dispatching to specialized agents
   - **Integration Flow** — data exchange between systems
2. Generate a Python script (`generate_animated_diagrams.py`) using Pillow + imageio
3. Define nodes (boxes), layers (containers), and arrows (animated dashed lines)
4. Render 24 frames with incrementing dash offset to create smooth arrow animation
5. Assemble frames into looping GIF
6. Generate one GIF per flow diagram

**Output**:
- `RFP/<client-name>/<client>_Animated_<flow-name>.gif` (one per diagram)
- `RFP/<client-name>/generate_animated_diagrams.py` (source script for regeneration)

**Minimum diagrams** (generate at least 1-2):
1. `<client>_Animated_Pipeline.gif` — Core processing/migration pipeline flow
2. `<client>_Animated_Architecture.gif` — System architecture with data flow

**Generation method** — use Pillow + imageio:
```python
# Python path: /c/Users/TanmayDey/AppData/Local/Microsoft/WindowsApps/python.exe
# Packages: Pillow, imageio, numpy (install if needed)
# Design: dark background (#0F1B2D), brand colors, 1400x900 canvas, 24 frames at 80ms
```

**Quality rules**:
- Minimum canvas: 1400x900
- GIF must loop seamlessly
- All text must be legible (minimum 12px)
- Color-code arrows by flow type (data=teal, control=orange, API=blue)
- Include title and Aiden AI branding
- Maximum file size: ~5MB

---

## Shortcut: `/rfp-full`

**Purpose**: Run the complete pipeline end-to-end.

**Process**:
1. Ask the user for: **Client name**, **Deal type** (Unqork/AI), **RFP document location**, and **Onshore % (or 0%)**
2. Create folder: `RFP/<client-name>/`
3. Run all 13 commands in sequence:
   - `/rfp-analyze` → `<client>_RFP_Analysis.md` + `.docx`
   - `/rfp-requirements` → `<client>_Requirements.md` + `.docx`
   - `/rfp-instructions` → `<client>_Response_Instructions.md`
   - `/rfp-estimate` → `<client>_Estimate.md`
   - `/rfp-detailed-estimate` → `<client>_Detailed_Estimate.xlsx` (always — standard step)
   - `/rfp-pricing` → `<client>_Pricing.xlsx`
   - `/rfp-respond` → `<client>_Response.md` + `.docx`
   - `/rfp-architecture` → `<client>_Architecture_*.svg` + `_Architecture_Diagrams.html` (3-4 SVG diagrams)
   - `/rfp-deck` → `<client>_Deck.md` + `.html` + `.pptx` (Marp, includes architecture slides)
   - `/rfp-clarifications` → `<client>_Clarifications.xlsx`
   - `/rfp-support-estimate` → `<client>_Support_Estimate.xlsx` (only if support/managed services in RFP scope)
   - `/rfp-prototype` → `<client>_Prototype.py` + `<client>_AI_Demo.py` (AI deals) + `<client>_UI_Prototype.html`
   - `/rfp-animated-diagram` → `<client>_Animated_*.gif` (animated architecture flow GIFs)
4. Print final deliverable checklist

**Auto-detection**: After `/rfp-analyze`, check if the RFP mentions application support, managed services, production support, L1/L2/L3, SLAs, hypercare, or AMS. If yes, automatically include `/rfp-support-estimate` in the pipeline.

**Final output**:
```
RFP RESPONSE COMPLETE
─────────────────────────────────────────────
Client:    [Name]
Deal Type: [Unqork / AI]
Folder:    RFP/<client-name>/

Deliverables (MD + DOCX):
  ✅ <client>_RFP_Analysis.md + .docx         — RFP intelligence & go/no-go
  ✅ <client>_Requirements.md + .docx         — Full requirements register
  ✅ <client>_Response.md + .docx             — Full 16-section proposal

Deliverables (MD only):
  ✅ <client>_Response_Instructions.md        — Section-by-section writing guide
  ✅ <client>_Estimate.md                     — Effort estimate & staffing plan

Deliverables (Excel):
  ✅ <client>_Detailed_Estimate.xlsx          — Granular requirement-level estimation
  ✅ <client>_Pricing.xlsx                    — Pricing with margin analysis
  ✅ <client>_Clarifications.xlsx             — Questions for client
  ✅ <client>_Support_Estimate.xlsx           — Support model pricing (if applicable)

Deliverables (Presentation — Marp):
  ✅ <client>_Deck.html                       — Best viewing quality
  ✅ <client>_Deck.pptx                       — Editable presentation
  ✅ <client>_Deck.md                         — Marp source

Deliverables (Architecture — svgwrite SVG):
  ✅ <client>_Architecture_FiveLayer.svg      — Platform architecture layers
  ✅ <client>_Migration_Pipeline.svg          — Agent pipeline flow
  ✅ <client>_Target_Architecture.svg         — Target state diagram
  ✅ <client>_LLM_Gateway.svg                 — Multi-model routing (AI deals)
  ✅ <client>_Architecture_Diagrams.html      — Single-page viewer for all SVGs

Deliverables (Prototypes — Streamlit/Gradio/HTML):
  ✅ <client>_Prototype.py                    — Streamlit interactive app
  ✅ <client>_AI_Demo.py                      — Gradio AI demo (AI deals)
  ✅ <client>_UI_Prototype.html               — Static HTML mockup

Deliverables (Animated Diagrams — Pillow+imageio):
  ✅ <client>_Animated_Pipeline.gif           — Animated pipeline flow
  ✅ <client>_Animated_Architecture.gif       — Animated architecture flow

Internal-only files (DO NOT share with client):
  🔒 Margin Analysis sheet in Pricing.xlsx
  🔒 Scenario Comparison sheet in Pricing.xlsx
  🔒 Scenarios sheet in Support_Estimate.xlsx
  🔒 Tables 4-6 in estimate
─────────────────────────────────────────────
```

---

## Command Reference Card

| Command | One-liner | Output Format | Time |
|---------|-----------|---------------|------|
| `/rfp-analyze` | Deep-read the RFP, extract everything, go/no-go | MD + DOCX | First |
| `/rfp-requirements` | Structure all requirements with IDs and compliance | MD + DOCX | After analyze |
| `/rfp-instructions` | Tell the team what to write and how | MD | After requirements |
| `/rfp-estimate` | Calculate effort, hours, staffing plan | MD | After requirements |
| `/rfp-detailed-estimate` | Granular requirement-level estimation | XLSX | After estimate |
| `/rfp-pricing` | Build pricing Excel with margin analysis | XLSX | After detailed estimate |
| `/rfp-respond` | Write the full 16-section proposal | MD + DOCX | After all above |
| `/rfp-deck` | Generate executive presentation (Marp) | HTML + PPTX | After response |
| `/rfp-clarifications` | Generate clarification questions for client | XLSX | After analyze |
| `/rfp-architecture` | Generate SVG architecture diagrams (svgwrite) | SVG + HTML | After response |
| `/rfp-support-estimate` | Support model staffing & pricing (if applicable) | XLSX | After analyze |
| `/rfp-prototype` | Interactive UI prototypes & AI demos | PY + HTML | After response |
| `/rfp-animated-diagram` | Animated architecture flow GIFs | GIF + PY | After architecture |
| `/rfp-full` | Run all 13 commands end-to-end | All formats | Anytime |

---

## Rules (enforced across all commands)

1. **All outputs go to `RFP/<client-name>/`** — never the root Programs folder
2. **Load all skills from CLAUDE.md** before any command
3. **Detect deal type early** — it affects margins, infrastructure section, and platform content
4. **No placeholders in final outputs** — every `[bracket]` must be filled with real content
5. **Mark internal-only content clearly** — cost rates, margins, and Tables 4-6 never go to clients
6. **Apply correct margin thresholds** — 35% for Unqork, 45% for AI deals
7. **Run quality checklist** before finalizing the response document
8. **Output format rules** (mandatory):
   - **Pricing** → always Excel (`.xlsx`) via `openpyxl` — never MD or PDF
   - **Analysis, Requirements, Response** → always dual output: `.md` + `.docx` via `python-docx`
   - **Deck** → always Marp-based: `.md` (source) + `.html` + `.pptx` — **never use python-pptx** (poor quality)
   - **Clarifications** → always Excel (`.xlsx`) via `openpyxl`
   - **Architecture** → always `svgwrite` Python SVG (`.svg`) + HTML viewer — NOT Mermaid, NOT Plotly, NOT matplotlib
   - **Instructions, Estimate** → `.md` only (internal working documents)
9. **Always check onshore % with the user** — do not assume 30/70 split; ask if onshore is needed and at what %
10. **Architecture diagrams must be included in the deck** — at least one architecture slide in every presentation
11. **Deck quality standards** — every slide must have substantive content from the response document; minimum 15 slides; use CSS card components for metrics; include Aiden AI branding throughout
12. **DOCX styling** — blue header rows on tables, formatted heading hierarchy, proper paragraph spacing
13. **Detailed estimation is mandatory** — every RFP pipeline run must produce `<client>_Detailed_Estimate.xlsx` with requirement-level traceability. Cross-check total hours against high-level estimate (within 10%)
14. **Support estimation is conditional** — auto-detect from `/rfp-analyze` whether the RFP includes support/managed services. If yes, generate `<client>_Support_Estimate.xlsx` automatically. If unclear, ask the user
15. **Estimation Excel formatting** — all estimation Excel files use: blue header row (#003781), alternating row colors, auto-column-width, filters enabled, conditional formatting for complexity/priority
