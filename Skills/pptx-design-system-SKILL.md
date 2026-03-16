---
name: pptx-design-system
description: >-
  Use this skill whenever generating PowerPoint (.pptx) presentations using
  python-pptx. Contains the standard Aiden AI design system extracted from
  production proposals (Allianz Technical Proposal, Allianz RFP Response).
  Includes color palette, typography, layout patterns, card styles, table
  formatting, and reusable helper functions. Always use this skill when
  creating PPTs to ensure consistent, professional output.
license: "Internal use"
---

# PPTX Design System — Aiden AI Standard

This design system is extracted from production Aiden AI proposals and defines the standard visual language for all PowerPoint outputs.

---

## Part 1: Slide Dimensions

```python
prs = Presentation()
prs.slide_width = Inches(13.333)  # Widescreen 16:9
prs.slide_height = Inches(7.5)
```

Always use **13.333 x 7.5 inches** (widescreen 16:9). Never use 4:3.

---

## Part 2: Color Palette

### 2.1 Primary Brand Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Allianz Blue** | `#003781` | (0, 55, 129) | Primary brand, headers, accent shapes, section dividers |
| **Dark Navy** | `#1A1A2E` | (26, 26, 46) | Dark backgrounds, dark mode slides |
| **Deep Blue** | `#003366` | (0, 51, 102) | Secondary brand, subheadings |
| **Indigo** | `#232465` | (35, 36, 101) | Accent headers, feature callouts |

### 2.2 Text Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Heading Dark** | `#1E293B` | Primary headings on light backgrounds |
| **Body Primary** | `#334155` | Main body text (most used) |
| **Body Secondary** | `#475569` | Secondary body text |
| **Body Tertiary** | `#64748B` | Descriptions, captions |
| **Muted** | `#6B7280` | Labels, footnotes |
| **Light Muted** | `#94A3B8` | Watermarks, de-emphasized text |
| **White** | `#FFFFFF` | Text on dark/blue backgrounds |
| **Dark Text** | `#333333` | Alternative body text |

### 2.3 Surface Colors (Backgrounds & Fills)

| Name | Hex | Usage |
|------|-----|-------|
| **White** | `#FFFFFF` | Primary slide background, card fills |
| **Slate 50** | `#F8FAFC` | Card backgrounds, table even rows, subtle fills |
| **Slate 100** | `#F1F5F9` | Section backgrounds, alternate row fills |
| **Slate 200** | `#E2E8F0` | Borders, dividers, shape outlines (most used border) |
| **Slate 300** | `#E5E7EB` | Heavier borders, separators |
| **Blue 50** | `#EFF6FF` | Blue-tinted cards, info callouts |
| **Blue 100** | `#E0F2FE` | Lighter blue accent areas |
| **Blue 50 Alt** | `#F0F9FF` | Very light blue wash |
| **Gray BG** | `#F5F7FA` | Neutral card backgrounds |

### 2.4 Accent Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Orange** | `#ED7D31` | Accent shapes, callout borders, highlights |
| **Green Text** | `#166534` | Success indicators, positive metrics |
| **Green Alt** | `#15803D` | Green badges, status indicators |
| **Link Blue** | `#0369A1` | Hyperlinks, clickable text |
| **Royal Blue** | `#1E40AF` | Feature highlights, key metrics |

### 2.5 Color Usage Rules

```
LIGHT SLIDE (default):
  Background:  #FFFFFF
  Cards:       #F8FAFC or #F1F5F9
  Borders:     #E2E8F0
  Headings:    #003781 or #1E293B
  Body text:   #334155
  Muted text:  #64748B

DARK SLIDE (title, section dividers):
  Background:  #003781 or #1A1A2E
  Cards:       rgba(255,255,255,0.08)
  Borders:     rgba(255,255,255,0.15)
  Headings:    #FFFFFF
  Body text:   #FFFFFF (opacity 0.85)
  Muted text:  #94A3B8

ACCENT SLIDE (key messages, CTAs):
  Background:  #003781
  Accent bar:  #ED7D31
  Text:        #FFFFFF
```

---

## Part 3: Typography

### 3.1 Font Family

| Priority | Font | Fallback |
|----------|------|----------|
| **Primary** | Roboto | Arial, Calibri |
| **Secondary** | Franklin Gothic Book | Calibri |
| **Headings** | Franklin Gothic Demi | Calibri Bold |
| **Monospace** | Consolas | Courier New |

> **Rule**: Use **Roboto** as the default for all new presentations. Fall back to **Calibri** if Roboto is not available on the target machine.

### 3.2 Font Size Scale

| Element | Size (Pt) | Weight | Color |
|---------|----------|--------|-------|
| **Slide title (hero)** | 36-45 | Bold | `#003781` or `#FFFFFF` |
| **Section header** | 22 | Bold | `#003781` |
| **Slide title** | 18 | Bold | `#1E293B` or `#003781` |
| **Subheading** | 15 | Bold | `#1E293B` |
| **Card title** | 13 | Bold | `#003781` or `#1E293B` |
| **Body large** | 12 | Regular | `#334155` |
| **Body default** | 10 | Regular | `#334155` |
| **Body small** | 9 | Regular | `#475569` |
| **Caption / label** | 8 | Regular | `#64748B` |
| **Table header** | 10-11 | Bold | `#FFFFFF` (on blue bg) |
| **Table body** | 9-10 | Regular | `#334155` |
| **Footnote** | 8 | Regular | `#94A3B8` |

### 3.3 Typography Rules

- **Never use font size below 8pt** — unreadable in presentations
- **Maximum 3 font sizes per slide** — title + body + caption
- **Bold only for**: headings, card titles, key metrics, table headers
- **Italic only for**: quotes, citations, emphasis (sparingly)
- **ALL CAPS only for**: tags, labels, small category headers (always with letter-spacing)

---

## Part 4: Layout Patterns

### 4.1 Slide Margins

```python
MARGIN_LEFT = Inches(0.7)
MARGIN_TOP = Inches(0.5)
MARGIN_RIGHT = Inches(0.7)
CONTENT_WIDTH = Inches(11.9)  # 13.333 - 0.7 - 0.7
CONTENT_HEIGHT = Inches(6.3)  # 7.5 - 0.5 - 0.7
```

### 4.2 Standard Slide Layouts

**Layout 1: Title Slide**
```
┌─────────────────────────────────────────────────┐
│  [Full bleed blue background #003781]           │
│                                                 │
│           [Logo / Brand mark]                   │
│                                                 │
│        SLIDE TITLE (36-45pt, white, bold)        │
│        Subtitle (18pt, white, regular)          │
│                                                 │
│        [Date / Confidential tag]                │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Layout 2: Section Divider**
```
┌─────────────────────────────────────────────────┐
│  [Blue background #003781]                      │
│                                                 │
│     Section Number (45pt, white/orange)         │
│     Section Title (36pt, white, bold)           │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Layout 3: Content — Full Width**
```
┌─────────────────────────────────────────────────┐
│  SLIDE TITLE (18pt, blue)                       │
│  ─────────────────────────── (thin line #E2E8F0)│
│                                                 │
│  [Content area - full width]                    │
│  Body text, tables, diagrams                    │
│                                                 │
│  [Footer / page number]                         │
└─────────────────────────────────────────────────┘
```

**Layout 4: Content — Two Column**
```
┌─────────────────────────────────────────────────┐
│  SLIDE TITLE (18pt, blue)                       │
│  ───────────────────────────                    │
│                                                 │
│  ┌──────────────┐  ┌──────────────┐             │
│  │  Left Column │  │ Right Column │             │
│  │  (5.7in)     │  │ (5.7in)      │             │
│  └──────────────┘  └──────────────┘             │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Layout 5: Content — Three Cards**
```
┌─────────────────────────────────────────────────┐
│  SLIDE TITLE (18pt, blue)                       │
│  ───────────────────────────                    │
│                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  Card 1  │  │  Card 2  │  │  Card 3  │      │
│  │ (3.7in)  │  │ (3.7in)  │  │ (3.7in)  │      │
│  └──────────┘  └──────────┘  └──────────┘      │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Layout 6: Comparison (Before/After)**
```
┌─────────────────────────────────────────────────┐
│  SLIDE TITLE (18pt, blue)                       │
│  ───────────────────────────                    │
│                                                 │
│  ┌─── RED BORDER ───┐  ┌─── GREEN BORDER ──┐   │
│  │  BEFORE          │  │  AFTER            │   │
│  │  (5.8in)         │  │  (5.8in)          │   │
│  └──────────────────┘  └──────────────────┘   │
│                                                 │
│  [Impact bar — full width, green tinted]        │
└─────────────────────────────────────────────────┘
```

---

## Part 5: Component Styles

### 5.1 Cards

```python
def add_card(slide, left, top, width, height,
             fill='#F8FAFC', border_color='#E2E8F0', border_width=Pt(1),
             accent_color=None, corner_radius=Inches(0.1)):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor.from_string(fill)
    shape.line.color.rgb = RGBColor.from_string(border_color)
    shape.line.width = border_width
    shape.shadow.inherit = False
    return shape
```

**Card variants:**
- **Default card**: Fill `#F8FAFC`, border `#E2E8F0`
- **Blue card**: Fill `#EFF6FF`, border `#E0F2FE`
- **Accent card**: Fill `#F8FAFC`, left border `#003781` (4pt)
- **Dark card**: Fill `#1A1A2E`, border `rgba(255,255,255,0.1)`
- **Metric card**: Fill `#FFFFFF`, border `#E2E8F0`, large number centered

### 5.2 Tables

```python
def style_table(table):
    # Header row
    for cell in table.rows[0].cells:
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0x00, 0x37, 0x81)  # Allianz Blue
        for para in cell.text_frame.paragraphs:
            for run in para.runs:
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                run.font.bold = True
                run.font.size = Pt(10)
                run.font.name = 'Roboto'

    # Body rows — alternating
    for i, row in enumerate(table.rows):
        if i == 0: continue  # skip header
        for cell in row.cells:
            cell.fill.solid()
            if i % 2 == 1:
                cell.fill.fore_color.rgb = RGBColor(0xF8, 0xFA, 0xFC)
            else:
                cell.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            for para in cell.text_frame.paragraphs:
                for run in para.runs:
                    run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
                    run.font.size = Pt(9)
                    run.font.name = 'Roboto'
```

**Table rules:**
- Header: Blue background `#003781`, white bold text, 10-11pt
- Body: Alternating `#FFFFFF` / `#F8FAFC`, text `#334155`, 9-10pt
- Cell padding: 10-12px vertical, 16px horizontal
- No heavy borders — use `#E2E8F0` thin lines or no borders at all
- Never use full black borders

### 5.3 Metric/KPI Callouts

```python
def add_metric(slide, left, top, number, label,
               number_color='#003781', number_size=36):
    # Large number
    add_text_box(slide, left, top, Inches(2), Inches(0.8),
                 number, font_size=number_size,
                 color=number_color, bold=True,
                 alignment=PP_ALIGN.CENTER)
    # Label below
    add_text_box(slide, left, top + Inches(0.75), Inches(2), Inches(0.4),
                 label, font_size=8,
                 color='#64748B', bold=False,
                 alignment=PP_ALIGN.CENTER)
```

### 5.4 Section Divider Bar

```python
def add_divider(slide, left, top, width):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, Pt(2)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0xE2, 0xE8, 0xF0)
    shape.line.fill.background()
```

### 5.5 Tag / Badge

```python
def add_tag(slide, left, top, text, bg_color='#EFF6FF', text_color='#003781'):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(1.8), Inches(0.3)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor.from_string(bg_color)
    shape.line.fill.background()
    tf = shape.text_frame
    tf.paragraphs[0].text = text.upper()
    tf.paragraphs[0].font.size = Pt(8)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = RGBColor.from_string(text_color)
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
```

---

## Part 6: Reusable Helper Functions

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


# ─── COLOR CONSTANTS ──────────────────────────────────
class C:
    """Standard color palette"""
    BRAND_BLUE = RGBColor(0x00, 0x37, 0x81)
    DARK_NAVY = RGBColor(0x1A, 0x1A, 0x2E)
    DEEP_BLUE = RGBColor(0x00, 0x33, 0x66)
    INDIGO = RGBColor(0x23, 0x24, 0x65)

    HEADING = RGBColor(0x1E, 0x29, 0x3B)
    BODY = RGBColor(0x33, 0x41, 0x55)
    BODY_SEC = RGBColor(0x47, 0x55, 0x69)
    MUTED = RGBColor(0x64, 0x74, 0x8B)
    LIGHT_MUTED = RGBColor(0x94, 0xA3, 0xB8)
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)

    SURFACE = RGBColor(0xFF, 0xFF, 0xFF)
    CARD_BG = RGBColor(0xF8, 0xFA, 0xFC)
    SECTION_BG = RGBColor(0xF1, 0xF5, 0xF9)
    BORDER = RGBColor(0xE2, 0xE8, 0xF0)
    BLUE_WASH = RGBColor(0xEF, 0xF6, 0xFF)
    BLUE_LIGHT = RGBColor(0xE0, 0xF2, 0xFE)

    ORANGE = RGBColor(0xED, 0x7D, 0x31)
    GREEN = RGBColor(0x16, 0x65, 0x34)
    GREEN_ALT = RGBColor(0x15, 0x80, 0x3D)
    LINK_BLUE = RGBColor(0x03, 0x69, 0xA1)
    ROYAL_BLUE = RGBColor(0x1E, 0x40, 0xAF)
    RED = RGBColor(0xFF, 0x44, 0x44)

    # Dark theme
    ACCENT = RGBColor(0x00, 0xD4, 0xAA)
    ACCENT2 = RGBColor(0x6C, 0x63, 0xFF)


# ─── FONT CONSTANTS ───────────────────────────────────
FONT_PRIMARY = 'Roboto'
FONT_FALLBACK = 'Calibri'


# ─── LAYOUT CONSTANTS ────────────────────────────────
MARGIN_L = Inches(0.7)
MARGIN_T = Inches(0.5)
MARGIN_R = Inches(0.7)
CONTENT_W = Inches(11.9)
CARD_GAP = Inches(0.3)


# ─── HELPER FUNCTIONS ────────────────────────────────

def set_slide_bg(slide, color):
    """Set solid background color for a slide."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text_box(slide, left, top, width, height, text,
                 font_size=10, color=None, bold=False,
                 alignment=PP_ALIGN.LEFT, font_name=None):
    """Add a text box with standard formatting."""
    if color is None:
        color = C.BODY
    if font_name is None:
        font_name = FONT_PRIMARY
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return tf


def add_card(slide, left, top, width, height,
             fill_color=None, border_color=None,
             accent_side=None, accent_width=Pt(4)):
    """Add a card shape with optional left accent border."""
    if fill_color is None:
        fill_color = C.CARD_BG
    if border_color is None:
        border_color = C.BORDER
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1)
    shape.shadow.inherit = False

    # Add accent bar on left side if specified
    if accent_side:
        bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, left, top + Inches(0.1),
            accent_width, height - Inches(0.2)
        )
        bar.fill.solid()
        bar.fill.fore_color.rgb = accent_side
        bar.line.fill.background()

    return shape


def add_slide_title(slide, title, subtitle=None):
    """Add standard slide title with optional subtitle and divider."""
    add_text_box(slide, MARGIN_L, MARGIN_T, CONTENT_W, Inches(0.5),
                 title, font_size=18, color=C.BRAND_BLUE, bold=True)

    # Divider line
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, MARGIN_L, Inches(1.05), CONTENT_W, Pt(1.5)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = C.BORDER
    line.line.fill.background()

    if subtitle:
        add_text_box(slide, MARGIN_L, Inches(1.15), CONTENT_W, Inches(0.4),
                     subtitle, font_size=10, color=C.MUTED)

    return Inches(1.6) if subtitle else Inches(1.2)


def add_metric_box(slide, left, top, number, label,
                   number_color=None, width=Inches(2.2)):
    """Add a large metric number with label below."""
    if number_color is None:
        number_color = C.BRAND_BLUE
    card = add_card(slide, left, top, width, Inches(1.4))
    add_text_box(slide, left, top + Inches(0.1), width, Inches(0.7),
                 str(number), font_size=36, color=number_color,
                 bold=True, alignment=PP_ALIGN.CENTER)
    add_text_box(slide, left, top + Inches(0.8), width, Inches(0.4),
                 label.upper(), font_size=8, color=C.MUTED,
                 alignment=PP_ALIGN.CENTER)


def add_tag(slide, left, top, text, bg_color=None, text_color=None,
            width=Inches(1.8)):
    """Add a small tag/badge."""
    if bg_color is None:
        bg_color = C.BLUE_WASH
    if text_color is None:
        text_color = C.BRAND_BLUE
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.28)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.fill.background()
    shape.shadow.inherit = False
    tf = shape.text_frame
    tf.paragraphs[0].text = text.upper()
    tf.paragraphs[0].font.size = Pt(8)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = text_color
    tf.paragraphs[0].font.name = FONT_PRIMARY
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE


def style_table_standard(table):
    """Apply standard Aiden AI table styling."""
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            cell.fill.solid()
            if i == 0:
                # Header
                cell.fill.fore_color.rgb = C.BRAND_BLUE
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = C.WHITE
                        run.font.bold = True
                        run.font.size = Pt(10)
                        run.font.name = FONT_PRIMARY
            else:
                # Body — alternating rows
                cell.fill.fore_color.rgb = C.CARD_BG if i % 2 == 1 else C.SURFACE
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = C.BODY
                        run.font.size = Pt(9)
                        run.font.name = FONT_PRIMARY


def add_footer(slide, text='AidenAI | Confidential'):
    """Add standard footer bar."""
    add_text_box(slide, MARGIN_L, Inches(7.1), CONTENT_W, Inches(0.3),
                 text, font_size=7, color=C.LIGHT_MUTED,
                 alignment=PP_ALIGN.RIGHT)
```

---

## Part 7: Dark Theme Variant

For product launches, keynotes, and AdiOS-specific presentations, use the dark theme:

```python
class CDark:
    """Dark theme colors (AdiOS style)"""
    BG = RGBColor(0x0A, 0x0A, 0x1A)
    CARD = RGBColor(0x1A, 0x1A, 0x2E)
    BORDER = RGBColor(0x2A, 0x2A, 0x3E)
    ACCENT = RGBColor(0x00, 0xD4, 0xAA)
    ACCENT2 = RGBColor(0x6C, 0x63, 0xFF)
    ORANGE = RGBColor(0xFF, 0x8C, 0x00)
    RED = RGBColor(0xFF, 0x44, 0x44)
    PINK = RGBColor(0xE0, 0x55, 0xA0)
    BLUE = RGBColor(0x4A, 0x90, 0xD9)
    TEXT = RGBColor(0xFF, 0xFF, 0xFF)
    TEXT_SEC = RGBColor(0x99, 0xA0, 0xB4)
    TEXT_MUTED = RGBColor(0x5A, 0x60, 0x78)
```

**When to use dark theme**: Product launches, AdiOS presentations, keynotes, internal demos.

**When to use light theme**: RFP responses, client proposals, technical documents, formal submissions.

---

## Part 8: Design Checklist

Before delivering any PPT, verify:

- [ ] Slide dimensions are 13.333 x 7.5 inches (16:9)
- [ ] Font is Roboto (or Calibri fallback) throughout
- [ ] No font smaller than 8pt
- [ ] Maximum 3 font sizes per slide
- [ ] Colors are from the standard palette only
- [ ] Cards use `#F8FAFC` fill with `#E2E8F0` border (light) or `#1A1A2E` (dark)
- [ ] Tables have blue header row with white text
- [ ] Table body has alternating row colors
- [ ] Margins are consistent (0.7in left/right, 0.5in top)
- [ ] Every slide has a title at the top
- [ ] Slide title uses 18pt bold blue
- [ ] Section dividers use full-bleed blue background
- [ ] Footer is present on content slides
- [ ] No pure black (#000000) used anywhere
- [ ] No heavy black borders on any shape or table

---

> **Final reminder**: Consistency is what separates professional from amateur presentations. Every slide should look like it belongs to the same deck. When in doubt, use the default card style, the standard blue, and Roboto 10pt. Simplicity with consistency always beats complexity with inconsistency.
