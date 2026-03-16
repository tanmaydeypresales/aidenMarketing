# Project Instructions

## Skills

Always load and apply the following skills when relevant:

### RFP Response Skill
- **File**: `Skills/RFP_SKILL.md`
- **When to use**: Any RFP analysis, proposal writing, or bid response task. Provides full proposal structure, pricing templates, and quality checklists.

### Aiden AI / AIDAP Skill
- **File**: `Skills/aiden-ai-rfp-SKILL.md`
- **When to use**: Any proposal involving Aiden AI Builder or AIDAP as the platform. Covers AI architecture, agentic design, MCP 2.0, multi-model strategy, and win themes. Combine with the base RFP skill.

### Unqork Skill
- **File**: `Skills/unqork-rfp-skill.md`
- **When to use**: Any proposal involving Unqork as the platform. Covers no-code architecture, MongoDB limitations, AI integration patterns, and Unqork-specific design. Combine with the base RFP skill.

### RFP Analyzer Skill
- **File**: `Skills/rfp-analyzer-SKILL.md`
- **When to use**: FIRST skill to run when a new RFP arrives. Use whenever the user uploads, shares, or references an RFP document and wants to extract requirements, deadlines, evaluation criteria, user counts, compliance gaps, or scope details. Covers: document inventory, timeline extraction, client intelligence, functional & non-functional requirements extraction, user/volume metrics, integration mapping, evaluation criteria analysis, risk/gap analysis, and go/no-go assessment. Always run this BEFORE the RFP Response skill.

### Pricing Calculator Skill
- **File**: `Skills/pricing-calculator-SKILL.md`
- **When to use**: Any time the user needs effort estimation, staffing plans, or pricing for a proposal. Contains the standard Aiden AI rate card (onshore & offshore roles with rates), two pricing models (weekly for short engagements, monthly for long), phase-based effort distribution, reuse factors, staffing templates by engagement size (S/M/L), managed operations pricing, T-shirt sizing shortcuts, and Excel export guidance. Always use when generating Section 16 of any RFP response.

### Support Estimator Skill
- **File**: `Skills/support-estimator-SKILL.md`
- **When to use**: When the RFP includes application support, managed services, production support, L1/L2/L3 tiers, 24x7/16x5/8x5 coverage, SLA requirements, or hypercare/warranty support. Calculates staffing, effort, and pricing for support models with on-call coverage for P1/P2, weekends, and holidays. Outputs a 6-sheet Excel workbook.

### Detailed Estimation Skill
- **File**: `Skills/detailed-estimation-SKILL.md`
- **When to use**: Always run as part of the standard RFP pipeline. Maps every requirement (FR, NFR, INT, DM) to granular tasks with complexity ratings, role assignments, and hour estimates. Produces a traceable requirement-to-effort Excel workbook. Run after `/rfp-requirements`.

### Animated Diagram Skill
- **File**: `Skills/animated-diagram-SKILL.md`
- **When to use**: When generating animated architecture/flow diagrams as GIF files with moving dashed arrows. Uses Pillow + imageio. Dark theme with Aiden AI branding. Invoked by `/rfp-animated-diagram` command.

### RFP Command Set
- **File**: `Skills/rfp-commands-SKILL.md`
- **When to use**: Whenever the user wants to respond to an RFP end-to-end or run any `/rfp-*` command. Defines 13 sequential commands (`/rfp-analyze`, `/rfp-requirements`, `/rfp-instructions`, `/rfp-estimate`, `/rfp-detailed-estimate`, `/rfp-pricing`, `/rfp-respond`, `/rfp-deck`, `/rfp-clarifications`, `/rfp-architecture`, `/rfp-support-estimate`, `/rfp-prototype`, `/rfp-animated-diagram`) plus `/rfp-full` shortcut. All outputs go to `RFP/<client-name>/`.

### PPTX Design System Skill
- **File**: `Skills/pptx-design-system-SKILL.md`
- **When to use**: Every time you generate a PowerPoint using python-pptx. Contains the standard Aiden AI color palette, typography scale, layout patterns, card/table styles, and reusable helper functions extracted from production proposals. Ensures consistent, professional output across all decks.

## File Organization

- `RFP/` — All RFP-related files organized by client name
- `Cloud API Payload Examples/` — Guidewire Cloud API payloads and docs
- `Skills/` — Skill definition files (referenced above)
- `Design/` — Design documents and scripts

### Output Rule
**All generated documents** (PPTX, DOCX, XLSX, PDF, HTML, diagrams, prototypes, analysis outputs) **MUST be saved into `RFP/<client-or-request-name>/`** — never directly in the `Programs/` root folder. If a client folder doesn't exist yet, create it before saving. Ask the user for the client/request name if not obvious from context.
