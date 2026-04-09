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

### Marketing Copy Studio Skill
- **File**: `Skills/marketing-copy-SKILL.md`
- **When to use**: Any marketing, brand, or content creation task. Triggers: website copy, landing pages, email campaigns, LinkedIn posts, white papers, executive briefs, one-pagers, sales sheets, case studies, brand messaging, product descriptions, or any request tagged "marketing", "copy", "brand", or "campaign". Follows a 9-step workflow (brief → copy → quality scoring → improvement → content plan → HTML → repo package). Quality gate: auto-improves any dimension scoring <4; only marks "Publish Ready" at 4.3+ overall. Command: `/marketing` or `/marketing-copy`.

### Aiden AI Brand Guidelines
- **File**: `Skills/aiden-ai-branding-guidelines.md`
- **When to use**: Every time you produce or direct visual marketing content — LinkedIn carousels, email sharables, client-facing graphics, infographics, slide decks, banners, or any design involving color, font, layout, or logo decisions. Governs HOW content looks. Always load alongside the Marketing Copy Studio skill.

### LinkedIn Visual Text Skill
- **File**: `Skills/linkedin-visual-text-SKILL.md`
- **When to use**: Whenever writing text that appears ON a LinkedIn image or carousel slide (not the caption). Governs the 5 Laws, word limits per element, carousel arc structure (Hook → Problem → Content → CTA), and Aiden AI-specific content patterns. Always combine with the Marketing Copy Studio and Brand Guidelines skills.

## File Organization

- `RFP/` — All RFP-related files organized by client name
- `Cloud API Payload Examples/` — Guidewire Cloud API payloads and docs
- `Skills/` — Skill definition files (referenced above)
- `Design/` — Design documents and scripts

### Output Rule
**All generated documents** (PPTX, DOCX, XLSX, PDF, HTML, diagrams, prototypes, analysis outputs) **MUST be saved into `RFP/<client-or-request-name>/`** — never directly in the `Programs/` root folder. If a client folder doesn't exist yet, create it before saving. Ask the user for the client/request name if not obvious from context.
