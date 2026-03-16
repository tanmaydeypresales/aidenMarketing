# Aiden AI — RFP Pipeline Skills for Claude Code

A library of Claude Code skills that power the end-to-end RFP response pipeline. Drop these into any Claude Code project to get a 13-command workflow that produces all proposal deliverables automatically.

## Quick Start

1. Clone this repo into your project:
   ```bash
   git clone https://github.com/enterprise/aidenai/aiden-rfp-skills.git
   ```
2. Copy `Skills/` folder and `CLAUDE.md` into your working directory
3. Open Claude Code in that directory — skills are loaded automatically

## Skills Inventory

| # | Skill File | Purpose | Invoked By |
|---|-----------|---------|------------|
| 1 | `RFP_SKILL.md` | 16-section proposal structure, quality checklists | `/rfp-respond` |
| 2 | `rfp-analyzer-SKILL.md` | 7-phase RFP deep analysis, go/no-go assessment | `/rfp-analyze` |
| 3 | `aiden-ai-rfp-SKILL.md` | AIDAP/Aiden AI Builder platform content, agentic AI, MCP 2.0 | AI deals |
| 4 | `unqork-rfp-skill.md` | Unqork no-code platform content, MongoDB, integrations | Unqork deals |
| 5 | `pricing-calculator-SKILL.md` | Rate card, effort models, staffing templates, margin analysis | `/rfp-pricing` |
| 6 | `detailed-estimation-SKILL.md` | Requirement-level effort decomposition, complexity scoring | `/rfp-detailed-estimate` |
| 7 | `support-estimator-SKILL.md` | L1/L2/L3 support models, 24x7/16x5/8x5, SLA pricing | `/rfp-support-estimate` |
| 8 | `pptx-design-system-SKILL.md` | Aiden AI visual identity, colors, typography, card styles | `/rfp-deck` |
| 9 | `animated-diagram-SKILL.md` | Animated GIF architecture diagrams (Pillow + imageio) | `/rfp-animated-diagram` |
| 10 | `rfp-commands-SKILL.md` | Master command set defining all 13 `/rfp-*` commands | All commands |

## Pipeline Commands

| Command | Output | Format |
|---------|--------|--------|
| `/rfp-analyze` | RFP intelligence & go/no-go | MD + DOCX |
| `/rfp-requirements` | Structured requirements register | MD + DOCX |
| `/rfp-instructions` | Section-by-section writing guide | MD |
| `/rfp-estimate` | Effort estimate & staffing plan | MD |
| `/rfp-detailed-estimate` | Granular requirement-level estimation | XLSX |
| `/rfp-pricing` | Commercial pricing with margin analysis | XLSX |
| `/rfp-respond` | Full 16-section proposal | MD + DOCX |
| `/rfp-deck` | Executive presentation | HTML + PPTX (Marp) |
| `/rfp-clarifications` | Clarification questions for client | XLSX |
| `/rfp-architecture` | Architecture diagrams | SVG + HTML (svgwrite) |
| `/rfp-support-estimate` | Support model pricing (conditional) | XLSX |
| `/rfp-prototype` | Interactive UI prototypes | Streamlit/Gradio/HTML |
| `/rfp-animated-diagram` | Animated architecture flows | GIF (Pillow) |
| `/rfp-full` | Run all 13 commands end-to-end | All formats |

## How to Use

### For a new RFP response:
```
/rfp-full
```
This runs the entire pipeline and produces all deliverables in `RFP/<client-name>/`.

### For individual steps:
```
/rfp-analyze        # Start here — deep-read the RFP
/rfp-requirements   # Extract and structure all requirements
/rfp-respond        # Generate the full proposal
/rfp-deck           # Create the presentation
```

## Dependencies

These Python packages are used by various output generators:
- `python-docx` — DOCX generation
- `openpyxl` — Excel generation
- `svgwrite` — SVG architecture diagrams
- `Pillow`, `imageio`, `numpy` — Animated GIF diagrams
- `streamlit` — Interactive prototypes
- `gradio` — AI demo interfaces
- Marp CLI (`npx @marp-team/marp-cli`) — Presentations

## File Structure

```
aiden-rfp-skills/
  CLAUDE.md              # Project instructions — loads all skills automatically
  README.md              # This file
  Skills/
    RFP_SKILL.md         # Core proposal structure
    rfp-analyzer-SKILL.md
    rfp-commands-SKILL.md
    aiden-ai-rfp-SKILL.md
    unqork-rfp-skill.md
    pricing-calculator-SKILL.md
    detailed-estimation-SKILL.md
    support-estimator-SKILL.md
    pptx-design-system-SKILL.md
    animated-diagram-SKILL.md
```

## Team

Maintained by Aiden AI Proposal Engineering.

---
*Built for Claude Code by Aiden AI*
