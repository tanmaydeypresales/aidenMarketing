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

### Insurance Underwriting Skill
- **File**: `Skills/insurance-underwriting-SKILL.md`
- **When to use**: Any RFP or proposal involving insurance underwriting, policy administration, risk assessment, rating engines, submission intake, quote-bind-issue, underwriting workbench, or insurance operations. Covers full domain knowledge (P&C commercial/personal/specialty lines, life/health, LOB-specific UW factors, regulations like state DOI/NAIC/Solvency II/IFRS 17, ACORD standards, data models, integrations with Guidewire/Duck Creek/Majesco) plus 9 Aiden AI agent patterns (Submission Triage, Risk Scoring, Pricing, UW Copilot, Document Intelligence, Portfolio Optimization, Compliance, Renewal Management, Market Intelligence). Includes STP tiers, UW Workbench design, competitor positioning, and insurance-specific pricing guidance. Combine with the base RFP skill and Aiden AI skill.

### Wealth Management Skill
- **File**: `Skills/wealth-management-SKILL.md`
- **When to use**: Any RFP or proposal involving wealth management, asset management, private banking, financial advisory, portfolio management, robo-advisory, trading platforms, or investment operations. Covers full domain knowledge (client tiers, regulations like SEC/FINRA/MiFID, business processes, data models, integrations) plus 7 Aiden AI agent patterns (Advisor Copilot, Onboarding, Portfolio Intelligence, Compliance, Client Insights, Financial Planning, Research). Includes Client 360 architecture, phased implementation approach, competitor positioning, and WM-specific pricing guidance. Combine with the base RFP skill and Aiden AI skill.

### RFP Review Skill
- **File**: `Skills/rfp-review-SKILL.md`
- **When to use**: When the user wants to review, audit, QA-check, or validate an existing RFP response package. Triggers: "review my RFP response", "check our proposal", "validate the bid", "QA the proposal", "does our response match the RFP", "final check before submission", or any gap analysis / compliance check request. Requires: source RFP + response document. Also ask for the presentation deck and pricing workbook if available. Produces a standalone Review Report with compliance scorecard, missing requirements register, language/consistency issues log, action checklist, open questions log, and submission readiness summary. Never edits the original proposal.

### PPTX Design System Skill
- **File**: `Skills/pptx-design-system-SKILL.md`
- **When to use**: Every time you generate a PowerPoint using python-pptx. Contains the standard Aiden AI color palette, typography scale, layout patterns, card/table styles, and reusable helper functions extracted from production proposals. Ensures consistent, professional output across all decks.

### RFP Humanizer Skill
- **File**: `Skills/rfp-humanize-SKILL.md`
- **When to use**: After generating any RFP narrative text, before client submission. Rewrites content to pass AI-generated content detectors (GPTZero, Originality.ai, Turnitin). Eliminates filler phrases, uniform sentence patterns, passive voice clusters, hedge language, and robotic structure. Makes text read like an experienced solutions architect wrote it. Invoke with `/rfp-humanize` or apply automatically as final pass after `/rfp-respond`. Also apply when user says "humanize", "make it sound natural", "pass AI detection", or "remove AI feel".

### Marketing Copy Studio Skill
- **File**: `Skills/marketing-copy-SKILL.md`
- **When to use**: Any marketing, brand, or content creation task. Triggers: website copy, landing pages, email campaigns, LinkedIn posts, white papers, executive briefs, one-pagers, sales sheets, case studies, brand messaging, product descriptions, or any request tagged "marketing", "copy", "brand", or "campaign". Follows a 9-step workflow (brief → copy → quality scoring → improvement → content plan → HTML → repo package). Quality gate: auto-improves any dimension scoring <4; only marks "Publish Ready" at 4.3+ overall. **For HTML generation, invokes the `frontend-design` skill** (installed via superpowers plugin) to produce production-grade, distinctive HTML assets. Command: `/marketing` or `/marketing-copy`.

### URL Shortener Skill
- **File**: `Skills/url-shortener-SKILL.md`
- **When to use**: After deploying any marketing campaign to GitHub Pages or any public URL. Triggers: "shorten the URLs", "create short links", "links for external sharing", or automatically after any GitHub Pages deployment. Uses TinyURL public API (no auth required). Saves results to `Marketing/<campaign-name>/short-links.md` and commits to the repo.

### Stock Analysis Skill
- **File**: `Skills/stock-analysis-SKILL.md`
- **When to use**: When the user wants a stock analysis report, value picks during market corrections, index performance screening (Nifty 50, Sensex, any index), or fundamental buy/sell recommendations. Covers 8-section DOCX report structure, standard screening filters (ROE >15%, PE <35, market leader), verdict definitions (STRONG BUY → AVOID), python-docx code patterns, and data sources. Reference implementation at `RFP/Stock_Analysis/generate_stock_report.py`. Output to `RFP/Stock_Analysis/`.

## File Organization

- `RFP/` — All RFP-related files organized by client name
- `Cloud API Payload Examples/` — Guidewire Cloud API payloads and docs
- `Skills/` — Skill definition files (referenced above)
- `Design/` — Design documents and scripts

### Output Rule
**All generated documents** (PPTX, DOCX, XLSX, PDF, HTML, diagrams, prototypes, analysis outputs) must be saved into the correct subfolder — never directly in the `Programs/` root folder:
- **RFP / proposal work** → `RFP/<client-or-request-name>/`
- **Marketing copy, campaigns, HTML assets** → `Marketing/<campaign-or-client-name>/`
- **PPT project tools and templates** → `PPT/`

If the client or campaign name is not obvious from context, ask the user before creating the folder.
