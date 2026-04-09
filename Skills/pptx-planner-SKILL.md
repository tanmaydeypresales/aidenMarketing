---
name: pptx-planner
description: Must invoke before writing any python-pptx code. Plans every slide as a Python dict with exact layout coordinates, text limits, icon choices, and research data before any code is written.
license: Internal use
---

# PPTX Planner Skill

## 1. When to Invoke

Invoke this skill **before** any of the following:

- Writing ANY new python-pptx presentation script from scratch
- Regenerating or rebuilding an existing slide deck
- Adding new slides to an existing deck
- Fixing layout overflow, text clipping, or element collision issues
- Responding to a `/rfp-deck`, `/rfp-architecture`, or any other command that produces a PPTX file

**Rule:** No python-pptx rendering code is written until all slide plans are defined and validated.

---

## 2. Canvas Constants

These values are fixed for all presentations. Import or reference them from `pptx_planner.py`. Never hardcode different values.

```python
W             = 13.333   # Slide width in inches (widescreen 16:9)
H             = 7.5      # Slide height in inches
MARGIN        = 0.35     # Standard margin from all edges
SAFE_L        = 0.35     # Left safe boundary
SAFE_T        = 0.38     # Top safe boundary
SAFE_R        = 12.983   # Right safe boundary  (W - MARGIN)
SAFE_B        = 7.15     # Bottom safe boundary (H - MARGIN)
CONTENT_W     = 12.633   # Usable content width (SAFE_R - SAFE_L)

BODY_T_NO_SUB  = 1.22   # Body top when no subtitle present
BODY_T_WITH_SUB = 1.48  # Body top when subtitle is present

HEADER_BAR_H  = 2.05    # Standard header bar height
INTER_GAP     = 0.12    # Standard gap between sibling elements
```

---

## 3. Layout Template Catalogue

All layouts are defined in the `LAYOUTS` dict inside `pptx_planner.py`. Reference them by their string key in every slide plan. Use the layout that best fits the content density and hierarchy of the slide.

| Layout Key | Use Case |
|---|---|
| `cover` | Title / opening slide. Large hero text, client logo zone, tagline. |
| `divider` | Section separator. Bold section title, optional subtitle, no data. |
| `header_3stat` | Single statement header + 3 large KPI stats below. Good for impact/outcomes slides. |
| `title_3col` | Title + 3 equal-width content columns. Each column holds a card with title, icon, bullets. |
| `title_4col` | Title + 4 equal-width columns. Tighter than 3col — keep card titles short. |
| `title_5col` | Title + 5 equal-width columns. Use for comparisons, process steps, or capability lists. |
| `title_6card_2x3` | Title + 6 cards in a 2-row × 3-column grid. Best for feature matrices or agent catalogs. |
| `header_5col` | Large header zone (with stat or callout) + 5 columns below. Combines punch with detail. |
| `title_layer5` | Title + 5 horizontal layers/rows. Use for architecture layers, stack views, or tiered models. |
| `title_hero_3panel` | Title + 3 wide hero panels side-by-side. Each panel has image/icon zone + text below. |
| `title_fit_table` | Title + a full-width table that auto-fits to available body height. Use for comparison matrices, SLA tables, pricing rows. |
| `title_3panel_poc` | Title + 3 panels designed for POC/prototype walkthrough (screenshot zone + caption). |
| `title_gantt_pricing` | Title + Gantt chart zone on left + pricing summary on right. Phase timelines + cost. |
| `full_bleed_close` | Full-bleed background image or gradient with centered CTA text. Closing/thank-you slide. |

**The catalogue is open-ended — new layouts are added to the `LAYOUTS` dict freely** when an existing layout does not fit the content requirement. When adding a new layout, define its coordinate spec in `LAYOUTS` before referencing it in any plan dict.

---

## 4. Slide Brief Format

Every slide is planned as a Python dict **before** any rendering code is written. All dicts are collected into a `SLIDE_PLANS` list at the top of the script.

```python
{
    "id": 3,                          # Sequential slide number (1-based)
    "name": "Agentic AI Capabilities",  # Short internal label for this slide
    "layout": "title_4col",           # Key from LAYOUTS dict
    "purpose": (
        "Introduce the 4 core AI agents in the platform. "
        "Each column = one agent. Audience: technical evaluators."
    ),
    "research": [
        # At least 1 cited stat per data slide. Use real market research.
        "Gartner 2024: 80% of enterprises will deploy agentic AI by 2026",
        "McKinsey 2023: Automation of knowledge work saves 40% of FTE time",
    ],
    "content": {
        "slide_title": "Four Agents That Run Your Underwriting End-to-End",
        "subtitle": "From submission intake to bind — zero manual handoffs",  # optional
        "columns": [
            {
                "icon": "robot",
                "icon_variant": "circle_cyan",
                "card_title": "Submission Triage Agent",  # <= 34 chars
                "bullets": [
                    "Parses ACORD 125/126 in <2 sec",  # <= 55 chars, measurable
                    "Routes by LOB, geography, appetite",
                    "Flags incomplete data before queue",
                ],  # max 3 bullets
            },
            {
                "icon": "shield",
                "icon_variant": "circle_teal",
                "card_title": "Risk Scoring Agent",
                "bullets": [
                    "600+ rating variables per submission",
                    "ML model updated weekly from loss data",
                    "Outputs recommended premium band",
                ],
            },
            {
                "icon": "chart_bar",
                "icon_variant": "circle_navy",
                "card_title": "UW Copilot Agent",
                "bullets": [
                    "Surfaces comparable prior decisions",
                    "Drafts referral memo in 30 seconds",
                    "UW reviews, clicks Approve or Revise",
                ],
            },
            {
                "icon": "lightning",
                "icon_variant": "circle_gold",
                "card_title": "Quote & Bind Agent",
                "bullets": [
                    "Generates bindable quote PDF instantly",
                    "API push to broker portal or DTC flow",
                    "Audit trail written to policy system",
                ],
            },
        ],
        "footer": "Source: Gartner 2024 | McKinsey 2023 | Aiden AI Internal Benchmarks",
    },
    "design_notes": (
        "Use gradient card backgrounds (dark navy to dark teal). "
        "Drop shadow on each card. Icon at top-center of each column. "
        "Footer at SAFE_B - 0.22. No decorative bullets — use clean list."
    ),
}
```

### Required Fields

| Field | Required | Notes |
|---|---|---|
| `id` | Yes | Matches position in `SLIDE_PLANS` list |
| `name` | Yes | Internal reference label, not rendered |
| `layout` | Yes | Must be a key in `LAYOUTS` dict |
| `purpose` | Yes | Audience + goal for this slide |
| `research` | Yes for data slides | List of cited stats. Empty list `[]` only for cover/divider/close slides |
| `content` | Yes | All text strings subject to limits in Section 5 |
| `design_notes` | Recommended | Gradient, shadow, icon variant, color callouts |

---

## 5. Text Limit Rules

Enforce these limits in `validate_plan()` and visually during plan review. Violations must be fixed before coding begins.

| Element | Max Lines | Max Characters Per Line | Notes |
|---|---|---|---|
| `slide_title` | 1 | 72 | Assertion statement, not a label |
| `card_title` | 1 | 34 | Proper noun agent/feature name preferred |
| `card_bullet` | 1 per bullet | 55 | Max 3 bullets per card |
| `stat_label` | 2 | 26 per line | Stat value on line 1, label on line 2 |
| `subtitle` / `intro` | 1 | 100 | Amplifies the title — no repetition |
| `table_cell` | 2 | 48 per line | Wrap gracefully, never overflow cell bounds |
| `footer` | 1 | 150 | Source citations only, small font |
| `section_divider_title` | 2 | 38 per line | High-contrast, large type |

**Enforcement:** If any string exceeds its limit, shorten the string in the plan dict — do NOT increase font size or shrink the layout to compensate.

---

## 6. Pre-Flight Checklist

Run `validate_plan()` on every item in `SLIDE_PLANS`. All checks must pass before any rendering code is written.

- [ ] Every element satisfies: `left + width <= 12.983` (SAFE_R)
- [ ] Every element satisfies: `top + height <= 7.15` (SAFE_B)
- [ ] Every `card_title` string is <= 34 characters
- [ ] Every card has <= 3 bullets, each <= 55 characters
- [ ] Every data slide has >= 1 cited research stat in the `research` list
- [ ] No two elements on the same slide overlap (check bounding boxes)
- [ ] All icons sourced from `icon_lib` PNG library via `place_icon()`
- [ ] All primary shape fills use gradient (not flat color)
- [ ] All card elements have drop shadows applied
- [ ] `slide_title` is a declarative assertion, not a noun phrase label
- [ ] No slide repeats information already shown on a prior slide
- [ ] `layout` key exists in `LAYOUTS` dict before referencing

If any check fails, fix the plan dict. Do not skip checks or mark them as acceptable exceptions.

---

## 7. Content Quality Rules

Apply these rules when writing content strings in every `SLIDE_PLANS` dict.

**Bullets must be substantive.** Every bullet must contain at least one of:
- A measurable outcome: "Reduces cycle time by 40%"
- A named capability: "Runs ACORD 125/126 parsing natively"
- A cited statistic: "Gartner: 65% of firms cite data latency as top risk"

**Numbers beat words.** Always prefer a quantified claim over a qualitative one:
- Correct: "Processes 500+ submissions per day unassisted"
- Wrong: "Handles a large volume of submissions efficiently"

**Agent names are proper nouns.** Capitalize agent names consistently across all slides:
- Correct: "Quote & Bind Agent", "Submission Triage Agent", "Risk Scoring Agent"
- Wrong: "the quoting agent", "our triage bot", "AI-powered submission tool"

**Every slide title is an assertion, not a label.** The title must make a claim the slide then supports:
- Correct: "Agentic AI Cuts Underwriting Cycle Time by Half"
- Wrong: "AI Capabilities Overview"

**Each slide introduces new information.** No two slides may repeat the same stat, bullet point, or claim. Review the full `SLIDE_PLANS` list before coding to identify and remove duplicates.

**Minimum 1 research stat per data slide.** Source must be real and recent (Gartner, McKinsey, Forrester, IDC, Celent, Deloitte, company annual report, or Aiden AI internal benchmark). Format: `"Source Name Year: stat text"`. Never fabricate citations.

---

## 8. Planning Process (Step by Step)

Follow this sequence exactly. Do not skip steps or reorder them.

### Step 1 — Write All SLIDE_PLANS Dicts (No Rendering Yet)

At the top of the script, define the complete `SLIDE_PLANS` list. Every slide in the deck gets a plan dict following the format in Section 4. No `add_slide()`, no `add_shape()`, no rendering calls at this stage.

```python
SLIDE_PLANS = [
    { "id": 1, "name": "Cover", "layout": "cover", ... },
    { "id": 2, "name": "Agenda", "layout": "title_3col", ... },
    # ... all slides
]
```

### Step 2 — Run validate_plan() on Every Plan

```python
from pptx_planner import validate_plan

for plan in SLIDE_PLANS:
    errors = validate_plan(plan)
    if errors:
        raise ValueError(f"Slide {plan['id']} ({plan['name']}) failed: {errors}")
```

Fix all violations before proceeding. Do not suppress or ignore errors.

### Step 3 — Write Rendering Code

Only after all plans pass validation, write the rendering loop using generic renderers from `pptx_planner.py`:

```python
from pptx_planner import render_slide

prs = Presentation()
prs.slide_width  = Inches(W)
prs.slide_height = Inches(H)

for plan in SLIDE_PLANS:
    render_slide(prs, plan)

prs.save(OUTPUT_PATH)
```

### Step 4 — Use Generic Renderers — Never Hardcode Coordinates

All layout logic lives in `pptx_planner.py` renderers. The script that calls `render_slide()` must not contain raw `Inches(x)` coordinate values for element positioning. Coordinates belong only inside `LAYOUTS` dict definitions.

Exception: if a layout is being defined for the first time in `LAYOUTS`, coordinate values are permitted there and nowhere else.

---

## 9. Icon Usage

All icons must be placed via the `icon_lib` helper. Never embed PNG files manually or reference icon paths directly from rendering code.

### Import

```python
from icon_lib.icon_lib import place_icon, ICON_PATH
```

### Usage

```python
place_icon(
    slide,
    icon_name="robot",          # Named icon from the 89-icon library
    variant="circle_cyan",      # Background circle color variant
    left=2.15,                  # Position in inches (left edge)
    top=1.85,                   # Position in inches (top edge)
    size=0.52,                  # Diameter in inches
)
```

### Available Variants

| Variant Key | Use For |
|---|---|
| `circle_cyan` | Primary AI agents, core features |
| `circle_teal` | Secondary agents, supporting features |
| `circle_navy` | Analytics, data, intelligence |
| `circle_gold` | Outcomes, results, ROI, value |
| `circle_dark` | Background/neutral elements |
| `circle_green` | Success, compliance, go indicators |
| `circle_red` | Risk, alert, no indicators |
| `circle_orange` | Warning, in-progress, partial |

### Icon Selection Rule

Choose the icon that represents the function, not the technology. Use a consistent variant color scheme per deck — assign variant colors to semantic roles (e.g., cyan = agents, gold = outcomes) and hold that mapping throughout all slides.

The full 89-icon catalog is visible at: `icon_lib/png/_preview.png`. Review it before planning to select accurate icon names for each card.

---

## Summary — Enforcement Order

1. Load this skill before writing any python-pptx code.
2. Write all `SLIDE_PLANS` dicts — layout, content, research, design notes.
3. Validate all plans with `validate_plan()`.
4. Fix all violations.
5. Write rendering code using `render_slide()` and `pptx_planner.py` generics.
6. Never hardcode coordinates in the rendering script.
7. Never write a bullet without a measurable outcome, capability, or citation.
8. Never write a slide title that is a noun phrase label rather than an assertion.
