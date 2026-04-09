---
name: pptx-design-system
description: >-
  Use this skill whenever generating PowerPoint (.pptx) presentations using
  python-pptx. Contains the standard Aiden AI design system extracted from
  the Bonitasoft to Camunda production deck — the canonical template.
  Includes color palette, typography, layout patterns, card styles, table
  formatting, section dividers, and reusable helper functions. Always use
  this skill when creating PPTs to ensure consistent, professional output.
license: "Internal use"
---

# PPTX Design System — Aiden AI Standard

This design system is extracted from the **Bonitasoft to Camunda** production deck and defines the canonical visual language for all PowerPoint outputs.

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
| **Cyan Blue (Primary)** | `#41B5E1` | (65, 181, 225) | Primary brand, title text accents, section header BG, accent shapes, triangles, divider lines, tags |
| **Deep Teal** | `#2193C2` | (33, 147, 194) | Subheadings, card titles, phase labels, column fills, secondary brand |
| **Vivid Sky Blue** | `#00B0F0` | (0, 176, 240) | Slide titles (Tungsten), product names ("AidenAI"), feature headers, deliverable labels |
| **Navy Dark** | `#083663` | (8, 54, 99) | Primary body text, description text, table body text — most used text color |
| **Dark Navy** | `#092750` | (9, 39, 80) | Theme dk2, metric text, dark headings |
| **Midnight** | `#073663` | (7, 54, 99) | Layout fills (section divider layouts), alternate navy |
| **Theme Dark** | `#242E3B` | (36, 46, 59) | Theme dk1, section headers background |

### 2.2 Text Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Navy Body** | `#083663` | Main body text (most used — Franklin Gothic Book) |
| **Dark Body** | `#092750` | Metric text, dark emphasis |
| **Dark Alt** | `#0E2841` | Phase bullet text, detail descriptions |
| **Gray Body** | `#414042` | Secondary body text, challenge lists |
| **White** | `#FFFFFF` | Text on blue/dark backgrounds, table headers, tags |
| **Blue Link** | `#0070C0` | Hyperlinks, diagram labels (INPUT/OUTPUT) |
| **Label Blue** | `#215381` | Source/Target labels, subtle blue text |

### 2.3 Surface Colors (Backgrounds & Fills)

| Name | Hex | Usage |
|------|-----|-------|
| **White** | `#FFFFFF` | Primary slide background (inherited from master) |
| **Light Blue Card** | `#CCEDFF` | Card fills, rounded rectangle backgrounds, info areas |
| **Light Blue Border** | `#37CBFF` | Border on light blue cards |
| **Cyan Blue Fill** | `#40B6E2` / `#42B3DF` | Full-width header bars, column fills, solution approach BG |
| **Light Purple** | `#F8F0FF` | Lifecycle header bar (Discover/Design/Build/Test/Maintain) |
| **Teal Button** | `#41B4E0` | Tag/button fills ("ATTACHMENT"), pill shapes |
| **Theme Light** | `#E6ECF1` | Theme lt2, subtle backgrounds |
| **Theme Accent4** | `#F4F8FA` | Very light wash backgrounds |

### 2.4 Accent & Indicator Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Gold / Amber** | `#FFC000` | Accent underline (below titles), section accent line — 2pt wide |
| **Orange** | `#ED7D31` | Secondary accent, callout borders |
| **Automated Blue** | `#0070C0` | Automated step circles (A), diagram labels |
| **Purple Accent** | `#7438F3` | Vertical connector lines in platform diagrams |
| **Silver Gray** | `#C8C8C8` | Brace shapes, lighter dividers |
| **Dark Blue Outline** | `#002060` | Box outlines for source/target containers |
| **Teal Link** | `#1C75BB` | "Aiden AI offers" emphasis, solution callouts |
| **Green Text** | `#166534` | Success indicators |

### 2.5 Section Divider Background

Section divider slides use the **13_Custom Layout** which has a dark navy/gradient background with:
- Large section number (80pt Tungsten, white/inherited)
- Section title (Tungsten Book, white, ~24pt)
- Background inherited from slide master (dark navy gradient)
- Slide number in bottom-right

```
SECTION DIVIDER:
  Background:  Dark navy (inherited from 13_Custom Layout master)
  Number:      80pt, centered-left
  Title:       Tungsten Book, white, right of number
  Slide #:     Bottom-right, centered
```

### 2.6 Color Usage Rules

```
CONTENT SLIDE (default, white background):
  Background:  #FFFFFF (inherited)
  Slide Title: Tungsten-Book, #00B0F0, 28-32pt, bold
  Gold accent:  #FFC000 line below title (0.68in wide, 2.25pt)
  Body text:   Franklin Gothic Book, #083663, 12-16pt
  Subheadings: Tungsten Book, #2193C2, 24-26pt
  Cards:       #CCEDFF fill, #37CBFF border
  Muted text:  #414042

HEADER BAR SLIDE (blue header top):
  Header bar:  #42B3DF or #40B6E2, full width, ~2in tall
  Header text: Tungsten-Book, white, 32pt bold, centered
  Sub-text:    Franklin Gothic Book, white, 16pt
  Content:     Below bar on white background

SECTION DIVIDER SLIDE:
  Background:  Dark navy gradient (from layout master)
  Number:      80pt, default inherited color
  Title:       Tungsten Book, white
```

---

## Part 3: Typography

### 3.1 Font Family

| Priority | Font | Usage |
|----------|------|-------|
| **Display / Headings** | **Tungsten Book** | Slide titles, section headers, subheadings, phase labels, product names |
| **Display Bold** | **Tungsten-Book** (bold=True) | Slide title text, emphasis headings |
| **Body Primary** | **Franklin Gothic Book** | All body text, descriptions, bullet points, card content |
| **Body Medium** | **Franklin Gothic Medium** | Section subheadings on content slides ("Challenges", "AidenAI offers") |
| **Body Bold** | **Franklin Gothic Demi** | Legend labels, bold callouts |
| **Accent Body** | **Aptos Narrow** | Product names within platform diagrams ("Aiden Discover", "Aiden Test Workbench") |
| **Theme Default** | **Arial** | Theme major/minor font, legend, fallback |

> **Rule**: Use **Tungsten Book** for all headings/titles and **Franklin Gothic Book** for all body text. Fall back to **Arial** / **Calibri** if fonts unavailable.

### 3.2 Font Size Scale

| Element | Size (Pt) | Font | Weight | Color |
|---------|----------|------|--------|-------|
| **Hero title (cover slide)** | 60 | Tungsten Book | Bold | `#41B5E1` |
| **Section divider number** | 80 | Inherited | Regular | Inherited (white) |
| **Section divider title** | 24-36 | Tungsten Book | Regular | White |
| **Slide title** | 28-32 | Tungsten-Book | Bold | `#00B0F0` |
| **Header bar title** | 32 | Tungsten-Book | Bold | White |
| **Subheading / Phase label** | 24-28 | Tungsten Book | Regular | `#2193C2` |
| **Card title** | 24-26 | Tungsten Book | Regular | `#2193C2` |
| **Capabilities label** | 24 | Tungsten Book | Bold | White (on blue pill) |
| **Body large** | 16 | Franklin Gothic Book | Regular | `#083663` |
| **Body default** | 14 | Franklin Gothic Book | Regular | `#083663` |
| **Body small** | 12 | Franklin Gothic Book | Regular | `#083663` or `#414042` |
| **Bullet / detail** | 10.5 | Franklin Gothic Book | Regular | `#0E2841` |
| **Caption / label** | 10 | Franklin Gothic Book | Regular | `#083663` |
| **Table header** | 14 | Franklin Gothic Book | Bold | White (on blue bg) |
| **Table body** | 12 | Franklin Gothic Book | Regular | `#083663` |
| **Product sub-name** | 14 | Aptos Narrow | Bold | `#00B0F0` |
| **Diagram label** | 16 | +mj-lt / Arial | Regular | `#0070C0` or `#215381` |
| **Phase step title** | 28 | Tungsten Book | Regular | `#2193C1` |
| **Numbered item** | 24 | Tungsten Book | Regular | `#3FB7E3` |
| **Tag text** | 14 | Franklin Gothic Book | Bold | White |

### 3.3 Typography Rules

- **Never use font size below 10pt** — maintain readability at projection distance
- **Tungsten Book only for**: slide titles, section headers, subheadings, phase labels, numbered items
- **Franklin Gothic Book for**: all body text, bullets, descriptions, card content
- **Franklin Gothic Medium for**: sub-section headings on content slides
- **Aptos Narrow for**: product/platform component names (within architecture diagrams)
- **Bold usage**: headings, card titles, key metrics, tag text, table headers — never for body text
- **ALL CAPS**: tags ("ATTACHMENT", "DELIVERABLES"), lifecycle phases ("DISCOVER AND DESIGN"), category headers
- **No Roboto** — this template does not use Roboto

---

## Part 4: Layout Patterns

### 4.1 Slide Margins

```python
MARGIN_LEFT = Inches(0.45)   # Content starts ~0.35-0.58 from left
MARGIN_TOP = Inches(0.40)    # Title starts ~0.39-0.45 from top
MARGIN_RIGHT = Inches(0.45)
CONTENT_WIDTH = Inches(12.4)  # 13.333 - margins
CONTENT_HEIGHT = Inches(6.5)
```

### 4.2 Standard Slide Layouts

**Layout 1: Title / Cover Slide**

> **IMPORTANT**: The title slide uses `aiden title slide.png` (in `Programs/`) as a **full-bleed background image**. This image contains the "aiden ai" logo (top-left) and the flowing cyan wave mesh design (right side). These graphic elements CANNOT be replicated with python-pptx shapes — always use the image as background.

```
┌─────────────────────────────────────────────────────┐
│  [aiden title slide.png — full bleed background]    │
│  (contains: "aiden ai" logo top-left + wave mesh)  │
│                                                     │
│  TITLE TEXT (3 lines max)                          │
│  L=0.58  T=1.86  W=7.55  H=2.78                   │
│  Tungsten Book, 60pt, Bold, #41B5E1                │
│  line_spacing = Pt(65)                              │
│                                                     │
│  ─── gold line ─── L=0.70 T=5.22 W=0.85           │
│  #FFC000, 2.25pt (28575 EMU)                       │
│                                                     │
│  Subtitle text                                      │
│  L=0.59  T=5.32  W=5.47  H=0.74                   │
│  Franklin Gothic Book, 24pt, #073663               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

```python
def add_title_slide(prs, title_lines, subtitle):
    """Add standard Aiden AI title slide with background image."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

    # Full-bleed background image (wave + logo)
    BG_PATH = os.path.join(PROGRAMS_DIR, "aiden title slide.png")
    slide.shapes.add_picture(BG_PATH, 0, 0, Inches(13.333), Inches(7.5))

    # Title text — multi-line, left-aligned
    title_box = slide.shapes.add_textbox(
        Inches(0.58), Inches(1.86), Inches(7.55), Inches(2.78))
    tf = title_box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(title_lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = Pt(65)
        r = p.add_run()
        r.text = line
        r.font.size = Pt(60)
        r.font.color.rgb = RGBColor(0x41, 0xB5, 0xE1)  # #41B5E1
        r.font.bold = True
        r.font.name = 'Tungsten Book'

    # Gold accent line
    gold = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.70), Inches(5.22), Inches(0.85), Pt(2.25))
    gold.fill.solid()
    gold.fill.fore_color.rgb = RGBColor(0xFF, 0xC0, 0x00)
    gold.line.fill.background()

    # Subtitle
    sub_box = slide.shapes.add_textbox(
        Inches(0.59), Inches(5.32), Inches(5.47), Inches(0.74))
    stf = sub_box.text_frame
    stf.word_wrap = True
    p = stf.paragraphs[0]
    r = p.add_run()
    r.text = subtitle
    r.font.size = Pt(24)
    r.font.color.rgb = RGBColor(0x07, 0x36, 0x63)  # #073663
    r.font.name = 'Franklin Gothic Book'

    return slide
```

**Layout 2: Section Divider**

> **IMPORTANT**: The section divider uses `divider.png` (in `Programs/`) as a **full-bleed background image**. This image contains: left ~40% meeting-room photo with blue tint overlay, right ~60% cyan-to-teal gradient, yellow+green accent squares (top-left and bottom-right corners), and small copyright footer. These elements CANNOT be replicated with python-pptx — always use the image as background.

```
┌─────────────────────────────────────────────────────┐
│  [divider.png — full bleed background]              │
│  (photo left, gradient right, accent squares)       │
│                                                     │
│                     01                              │
│              L=5.69  T=1.91  W=1.41  H=1.75        │
│              80pt (1016000 EMU), white, inherited    │
│                                                     │
│                     Section Title Here              │
│              L=6.08  T=3.49  W=5.76  H=1.82        │
│              Tungsten Book, white                   │
│                                                     │
│                                          [slide #]  │
│              L=12.72  T=7.02 (centered)            │
└─────────────────────────────────────────────────────┘
```

For dividers with a subtitle, shift title up:
- Title at L=6.96, T=2.12 (with subtitle below at T=3.49)

```python
def add_divider_slide(prs, number, title, subtitle=None):
    """Add section divider slide with background image."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

    # Full-bleed background image
    BG_PATH = os.path.join(PROGRAMS_DIR, "divider.png")
    slide.shapes.add_picture(BG_PATH, 0, 0, Inches(13.333), Inches(7.5))

    # Section number
    num_box = slide.shapes.add_textbox(
        Inches(5.69), Inches(1.91), Inches(1.41), Inches(1.75))
    ntf = num_box.text_frame
    p = ntf.paragraphs[0]
    r = p.add_run()
    r.text = f'{number:02d}'
    r.font.size = Pt(80)
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    r.font.name = 'Tungsten Book'

    # Section title
    if subtitle:
        title_top = Inches(2.12)
        title_left = Inches(6.96)
    else:
        title_top = Inches(3.49)
        title_left = Inches(6.08)

    title_box = slide.shapes.add_textbox(
        title_left, title_top, Inches(5.76), Inches(1.82))
    ttf = title_box.text_frame
    ttf.word_wrap = True
    p = ttf.paragraphs[0]
    r = p.add_run()
    r.text = title
    r.font.size = Pt(28)
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    r.font.name = 'Tungsten Book'

    if subtitle:
        sub_box = slide.shapes.add_textbox(
            Inches(6.96), Inches(3.49), Inches(5.76), Inches(1.00))
        stf = sub_box.text_frame
        stf.word_wrap = True
        p = stf.paragraphs[0]
        r = p.add_run()
        r.text = subtitle
        r.font.size = Pt(24)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.name = 'Tungsten Book'

    return slide
```

**Layout 3: Content — Title + Gold Accent**
```
┌─────────────────────────────────────────────────────┐
│  SLIDE TITLE (Tungsten-Book, 28-32pt, #00B0F0, bold│
│  ─── (#FFC000, 0.68in, 2.25pt) ───                │
│                                                     │
│  [Content area]                                     │
│  Body: Franklin Gothic Book, 14pt, #083663          │
│                                                     │
└─────────────────────────────────────────────────────┘
```
- Title at L=0.35-0.75, T=0.40-0.45
- Gold accent line at L=0.47, T=1.09, W=0.68, H=0

**Layout 4: Content — Blue Header Bar**
```
┌─────────────────────────────────────────────────────┐
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (#42B3DF)  2.1in │
│  [Header text: Tungsten-Book, 32pt, white, bold]    │
│  [Sub-text: Franklin Gothic Book, 16pt, white]      │
│  ───────────────────────────────────────────         │
│                                                     │
│  [Content columns / cards below]                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```
- Header rect: L=0, T=0, W=13.333, H=2.1-2.73 with #42B3DF or #40B6E2
- Used for: "Solution Approach", "WE ARE HELPING CLIENTS..."

**Layout 5: Content — Two-Column with Left Blue Panel**
```
┌─────────────────────────────────────────────────────┐
│  TITLE (Tungsten Book, #00B0F0)                    │
│  ─── gold line ───                                 │
│                                                     │
│  ┌──── #41B5E1 ────┐                               │
│  │  Left panel      │  [Right content area]        │
│  │  4.5in wide      │  Cards, text, diagrams       │
│  │  Rounded corner  │                               │
│  │  White text      │                               │
│  └──────────────────┘                               │
│                                                     │
└─────────────────────────────────────────────────────┘
```
- Blue panel: Round Single Corner Rectangle, L=-0.01, T=1.14, W=4.50, H=4.42, #41B5E1
- Content: Franklin Gothic Book, 15pt, white

**Layout 6: Content — Three Vertical Columns**
```
┌─────────────────────────────────────────────────────┐
│  [Left image / text area]                          │
│                                                     │
│  ┌─ #2193C1 ──┐  ┌─ #42B3DF ──┐  ┌─ solid ──┐    │
│  │  Column 1   │  │  Column 2  │  │ Column 3 │    │
│  │  (3.0in)    │  │  (3.0in)   │  │ (3.0in)  │    │
│  │  Full height│  │  Full ht   │  │ Full ht  │    │
│  └─────────────┘  └────────────┘  └──────────┘    │
│                                                     │
└─────────────────────────────────────────────────────┘
```
- Column rectangles: L=4.37/7.35/10.34, T=0, W=2.99, H=7.5
- Large numbers: Tungsten Book, 66pt, white (01, 02, 03)

**Layout 7: Content — Info Cards (2x2 or 1x4)**
```
┌─────────────────────────────────────────────────────┐
│  SLIDE TITLE (#00B0F0 Tungsten-Book)               │
│  ─── gold line ───                                 │
│                                                     │
│  ┌── #CCEDFF ──┐   ┌── #CCEDFF ──┐                │
│  │ border:     │   │ border:     │                │
│  │ #37CBFF     │   │ #37CBFF     │                │
│  │ Card 1      │   │ Card 2      │                │
│  └─────────────┘   └─────────────┘                │
│  ┌── #CCEDFF ──┐   ┌── #CCEDFF ──┐                │
│  │ Card 3      │   │ Card 4      │                │
│  └─────────────┘   └─────────────┘                │
└─────────────────────────────────────────────────────┘
```

**Layout 8: Case Study / Before-After**
```
┌─────────────────────────────────────────────────────┐
│  [Large text left:                                 │
│   Tungsten Book, 33pt, #00B0F0]                    │
│                                                     │
│  ┌─ Case 01 ─────────┐  ┌─ Case 02 ─────────┐    │
│  │ #41B5E1 triangle   │  │ #41B5E1 triangle  │    │
│  │ Title: Tungsten    │  │ Title: Tungsten   │    │
│  │  24pt #2193C1      │  │  24pt #2193C1     │    │
│  │ ─── #FFC000 ───── │  │ ─── #FFC000 ──── │    │
│  │ Traditional:       │  │ Traditional:      │    │
│  │ } brace #C8C8C8   │  │ } brace #C8C8C8  │    │
│  │ AiDAP Benefits:    │  │ AiDAP Benefits:   │    │
│  │ } brace #C8C8C8   │  │ } brace #C8C8C8  │    │
│  └────────────────────┘  └───────────────────┘    │
└─────────────────────────────────────────────────────┘
```

---

## Part 5: Component Styles

### 5.1 Cards (Light Blue Rounded Rectangle)

```python
def add_card(slide, left, top, width, height,
             fill_color=None, border_color=None):
    """Add Aiden AI standard card — light blue rounded rectangle."""
    if fill_color is None:
        fill_color = RGBColor(0xCC, 0xED, 0xFF)  # #CCEDFF
    if border_color is None:
        border_color = RGBColor(0x37, 0xCB, 0xFF)  # #37CBFF
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(0.75)  # 9525 EMU
    shape.shadow.inherit = False
    return shape
```

**Card variants:**
- **Default info card**: Fill `#CCEDFF`, border `#37CBFF` (most used)
- **Button/Tag card**: Fill `#41B4E0`, border `#37CBFF`, white bold text centered
- **Outline card**: No fill (background), border `#002060`, used for source/target containers
- **Pill shape**: Fill `#41B5E1`, no border, white bold text, used for capability labels

### 5.2 Gold Accent Line (Title Underline)

```python
def add_gold_accent(slide, left=None, top=None, width=None):
    """Add the gold accent line below slide titles."""
    if left is None:
        left = Inches(0.47)
    if top is None:
        top = Inches(1.09)
    if width is None:
        width = Inches(0.68)
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, Pt(2.25)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0xFF, 0xC0, 0x00)  # #FFC000
    shape.line.fill.background()
    shape.rotation = 0
    return shape
```

> The gold accent line appears on most content slides, positioned directly below the title. Width is 0.68in (short accent), weight is 2.25pt (#FFC000).

### 5.3 Cyan Divider Line

```python
def add_cyan_divider(slide, left, top, width, weight=Pt(1)):
    """Add a cyan horizontal divider line."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, weight
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x21, 0x93, 0xC2)  # #2193C2
    shape.line.fill.background()
    return shape
```

Cyan lines (`#2193C2` or `#41B5E1`) are used as horizontal dividers within content areas (12700 EMU = 1pt width).

### 5.4 Triangle Pointer

```python
def add_triangle(slide, left, top, width=Inches(0.16), height=Inches(0.14),
                 color=None):
    """Add a small downward-pointing triangle indicator."""
    if color is None:
        color = RGBColor(0x41, 0xB5, 0xE1)  # #41B5E1
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ISOSCELES_TRIANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape
```

Small cyan triangles are used as bullet indicators and directional pointers throughout the deck.

### 5.5 Blue Header Bar

```python
def add_header_bar(slide, height=Inches(2.1), color=None):
    """Add full-width cyan header bar at top of slide."""
    if color is None:
        color = RGBColor(0x42, 0xB3, 0xDF)  # #42B3DF
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape
```

### 5.6 Tag / Button Pill

```python
def add_tag(slide, left, top, text, width=Inches(1.84), height=Inches(0.44),
            bg_color=None, text_color=None):
    """Add a tag/button pill — used for 'ATTACHMENT', 'CAPABILITIES', etc."""
    if bg_color is None:
        bg_color = RGBColor(0x41, 0xB4, 0xE0)  # #41B4E0
    if text_color is None:
        text_color = RGBColor(0xFF, 0xFF, 0xFF)
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = RGBColor(0x37, 0xCB, 0xFF)
    shape.line.width = Pt(0.75)
    shape.shadow.inherit = False
    tf = shape.text_frame
    tf.paragraphs[0].text = text.upper()
    tf.paragraphs[0].font.size = Pt(14)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = text_color
    tf.paragraphs[0].font.name = 'Franklin Gothic Book'
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape
```

### 5.7 Tables

```python
def style_table_standard(table):
    """Apply standard Aiden AI table styling."""
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            cell.fill.solid()
            if i == 0:
                # Header row — cyan blue background
                cell.fill.fore_color.rgb = RGBColor(0x41, 0xB5, 0xE1)  # #41B5E1
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                        run.font.bold = True
                        run.font.size = Pt(14)
                        run.font.name = 'Franklin Gothic Book'
            else:
                # Body rows — white / light alternating
                cell.fill.fore_color.rgb = (
                    RGBColor(0xF4, 0xF8, 0xFA) if i % 2 == 1
                    else RGBColor(0xFF, 0xFF, 0xFF)
                )
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = RGBColor(0x08, 0x36, 0x63)
                        run.font.size = Pt(12)
                        run.font.name = 'Franklin Gothic Book'
```

**Table rules:**
- Header: Cyan blue `#41B5E1` background, white bold text, 14pt Franklin Gothic Book
- Body: Alternating `#FFFFFF` / `#F4F8FA`, text `#083663`, 12pt
- No heavy borders — use `#37CBFF` thin lines or no borders
- Never use full black borders

### 5.8 Outline Box (Source/Target Container)

```python
def add_outline_box(slide, left, top, width, height, label=None):
    """Add a dark-blue outlined container (for source/target diagrams)."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.background()
    shape.line.color.rgb = RGBColor(0x00, 0x20, 0x60)  # #002060
    shape.line.width = Pt(0.75)
    if label:
        add_text_box(slide, left, top - Inches(0.25), Inches(1.5), Inches(0.37),
                     label, font_size=16, color=RGBColor(0x21, 0x53, 0x81),
                     alignment=PP_ALIGN.CENTER)
    return shape
```

### 5.9 Rounded Pill Item (Inside Outline Box)

```python
def add_pill_item(slide, left, top, text, width=Inches(1.90), height=Inches(0.33)):
    """Add a rounded pill with cyan border — used for list items inside containers."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.background()
    shape.line.color.rgb = RGBColor(0x3F, 0xB7, 0xE3)  # #3FB7E3
    shape.line.width = Pt(0.75)
    tf = shape.text_frame
    tf.paragraphs[0].text = text
    tf.paragraphs[0].font.size = Pt(12)
    tf.paragraphs[0].font.name = 'Arial'
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape
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
    """Standard Aiden AI color palette — from Bonitasoft to Camunda template."""
    # Primary brand
    CYAN = RGBColor(0x41, 0xB5, 0xE1)       # #41B5E1 — primary brand, fills, triangles
    TEAL = RGBColor(0x21, 0x93, 0xC2)        # #2193C2 — subheadings, card titles, dividers
    SKY_BLUE = RGBColor(0x00, 0xB0, 0xF0)    # #00B0F0 — slide titles (Tungsten)
    CYAN_ALT = RGBColor(0x42, 0xB3, 0xDF)    # #42B3DF — header bars, column fills
    CYAN_LIGHT = RGBColor(0x40, 0xB6, 0xE2)  # #40B6E2 — header bars alt
    TEAL_BTN = RGBColor(0x41, 0xB4, 0xE0)    # #41B4E0 — tag/button fills
    LIGHT_CYAN = RGBColor(0x3F, 0xB7, 0xE3)  # #3FB7E3 — pill borders, numbered items

    # Navy / Dark
    NAVY = RGBColor(0x08, 0x36, 0x63)        # #083663 — primary body text
    DARK_NAVY = RGBColor(0x09, 0x27, 0x50)   # #092750 — dark headings, metrics
    MIDNIGHT = RGBColor(0x07, 0x36, 0x63)     # #073663 — layout fills
    THEME_DK = RGBColor(0x24, 0x2E, 0x3B)    # #242E3B — theme dk1
    DARK_BODY = RGBColor(0x0E, 0x28, 0x41)   # #0E2841 — bullet detail text
    OUTLINE = RGBColor(0x00, 0x20, 0x60)      # #002060 — box outlines

    # Text colors
    BODY = RGBColor(0x08, 0x36, 0x63)         # Same as NAVY — most used text
    BODY_SEC = RGBColor(0x41, 0x40, 0x42)     # #414042 — secondary body
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)
    LINK = RGBColor(0x00, 0x70, 0xC0)         # #0070C0 — links, diagram labels
    LABEL_BLUE = RGBColor(0x21, 0x53, 0x81)   # #215381 — source/target labels
    TEAL_LINK = RGBColor(0x1C, 0x75, 0xBB)    # #1C75BB — emphasis links
    PHASE_LABEL = RGBColor(0xE8, 0xE8, 0xE8)  # #E8E8E8 — phase labels (on purple bar)

    # Surfaces / fills
    CARD_BG = RGBColor(0xCC, 0xED, 0xFF)      # #CCEDFF — card fills
    CARD_BORDER = RGBColor(0x37, 0xCB, 0xFF)  # #37CBFF — card borders
    LIGHT_PURPLE = RGBColor(0xF8, 0xF0, 0xFF) # #F8F0FF — lifecycle header bar
    THEME_LT = RGBColor(0xE6, 0xEC, 0xF1)     # #E6ECF1 — theme lt2
    WASH = RGBColor(0xF4, 0xF8, 0xFA)         # #F4F8FA — table alt row

    # Accents
    GOLD = RGBColor(0xFF, 0xC0, 0x00)         # #FFC000 — accent underline
    ORANGE = RGBColor(0xED, 0x7D, 0x31)       # #ED7D31 — secondary accent
    PURPLE = RGBColor(0x74, 0x38, 0xF3)       # #7438F3 — connector lines
    SILVER = RGBColor(0xC8, 0xC8, 0xC8)       # #C8C8C8 — braces, light dividers
    GREEN = RGBColor(0x16, 0x65, 0x34)         # #166534 — success


# ─── FONT CONSTANTS ───────────────────────────────────
FONT_DISPLAY = 'Tungsten Book'         # Headings, titles, phase labels
FONT_DISPLAY_ALT = 'Tungsten-Book'     # Some shapes use hyphenated name
FONT_BODY = 'Franklin Gothic Book'     # All body text
FONT_BODY_MEDIUM = 'Franklin Gothic Medium'  # Sub-section headings
FONT_BODY_BOLD = 'Franklin Gothic Demi'      # Legend labels
FONT_ACCENT = 'Aptos Narrow'           # Product component names
FONT_FALLBACK = 'Arial'                # Theme default / fallback


# ─── LAYOUT CONSTANTS ────────────────────────────────
MARGIN_L = Inches(0.45)
MARGIN_T = Inches(0.40)
MARGIN_R = Inches(0.45)
CONTENT_W = Inches(12.4)
CARD_GAP = Inches(0.25)


# ─── HELPER FUNCTIONS ────────────────────────────────

def set_slide_bg(slide, color):
    """Set solid background color for a slide."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text_box(slide, left, top, width, height, text,
                 font_size=14, color=None, bold=False,
                 alignment=PP_ALIGN.LEFT, font_name=None):
    """Add a text box with standard formatting."""
    if color is None:
        color = C.BODY
    if font_name is None:
        font_name = FONT_BODY
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


def add_slide_title(slide, title, subtitle=None):
    """Add standard slide title (Tungsten-Book, #00B0F0, bold) with gold accent."""
    # Title text
    add_text_box(slide, Inches(0.35), Inches(0.42), Inches(12.5), Inches(0.57),
                 title, font_size=28, color=C.SKY_BLUE, bold=True,
                 font_name=FONT_DISPLAY)

    # Gold accent line below title
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.47), Inches(1.09), Inches(0.68), Pt(2.25)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = C.GOLD
    line.line.fill.background()

    if subtitle:
        add_text_box(slide, Inches(0.45), Inches(1.28), Inches(12.0), Inches(0.73),
                     subtitle, font_size=24, color=C.NAVY,
                     font_name=FONT_BODY)

    return Inches(1.6) if subtitle else Inches(1.2)


def add_section_divider(prs, number, title, subtitle=None):
    """Add a section divider slide matching 13_Custom Layout pattern."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank layout
    # Dark navy background
    set_slide_bg(slide, C.THEME_DK)

    # Section number — large, centered-left
    add_text_box(slide, Inches(5.69), Inches(1.91), Inches(1.41), Inches(1.75),
                 f'{number:02d}', font_size=80, color=C.WHITE,
                 font_name=FONT_FALLBACK)

    # Section title
    title_top = Inches(3.49) if not subtitle else Inches(2.12)
    title_left = Inches(6.08) if not subtitle else Inches(6.96)
    add_text_box(slide, title_left, title_top, Inches(5.76), Inches(1.82),
                 title, font_size=28, color=C.WHITE,
                 font_name=FONT_DISPLAY)

    if subtitle:
        add_text_box(slide, Inches(6.96), Inches(3.60), Inches(5.76), Inches(0.80),
                     subtitle, font_size=24, color=C.WHITE,
                     font_name=FONT_DISPLAY)

    return slide


def add_header_bar(slide, text=None, sub_text=None, height=Inches(2.1)):
    """Add full-width cyan header bar with optional title text."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = C.CYAN_ALT
    shape.line.fill.background()

    content_top = height
    if text:
        add_text_box(slide, Inches(1.21), Inches(0.57), Inches(10.92), Inches(0.64),
                     text, font_size=32, color=C.WHITE, bold=True,
                     alignment=PP_ALIGN.CENTER, font_name=FONT_DISPLAY)

    if sub_text:
        add_text_box(slide, Inches(1.26), Inches(1.32), Inches(10.63), Inches(0.64),
                     sub_text, font_size=16, color=C.WHITE,
                     alignment=PP_ALIGN.CENTER, font_name=FONT_BODY)

    return content_top


def add_card(slide, left, top, width, height,
             fill_color=None, border_color=None):
    """Add standard light blue info card."""
    if fill_color is None:
        fill_color = C.CARD_BG
    if border_color is None:
        border_color = C.CARD_BORDER
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(0.75)
    shape.shadow.inherit = False
    return shape


def add_gold_accent(slide, left=None, top=None, width=None):
    """Add the gold accent line below titles."""
    if left is None: left = Inches(0.47)
    if top is None: top = Inches(1.09)
    if width is None: width = Inches(0.68)
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, Pt(2.25)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = C.GOLD
    shape.line.fill.background()
    return shape


def add_cyan_divider(slide, left, top, width, weight=Pt(1)):
    """Add horizontal cyan divider line."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, weight
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = C.TEAL
    shape.line.fill.background()
    return shape


def add_triangle(slide, left, top, width=Inches(0.16), height=Inches(0.14),
                 color=None):
    """Add small downward triangle pointer."""
    if color is None: color = C.CYAN
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ISOSCELES_TRIANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_tag(slide, left, top, text, width=Inches(1.84), height=Inches(0.44),
            bg_color=None, text_color=None):
    """Add tag/button pill."""
    if bg_color is None: bg_color = C.TEAL_BTN
    if text_color is None: text_color = C.WHITE
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = C.CARD_BORDER
    shape.line.width = Pt(0.75)
    shape.shadow.inherit = False
    tf = shape.text_frame
    tf.paragraphs[0].text = text.upper()
    tf.paragraphs[0].font.size = Pt(14)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = text_color
    tf.paragraphs[0].font.name = FONT_BODY
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape


def add_outline_box(slide, left, top, width, height):
    """Add dark-blue outlined container (source/target)."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.background()
    shape.line.color.rgb = C.OUTLINE
    shape.line.width = Pt(0.75)
    return shape


def add_pill_item(slide, left, top, text, width=Inches(1.90), height=Inches(0.33)):
    """Add cyan-bordered pill item inside containers."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.background()
    shape.line.color.rgb = C.LIGHT_CYAN
    shape.line.width = Pt(0.75)
    tf = shape.text_frame
    tf.paragraphs[0].text = text
    tf.paragraphs[0].font.size = Pt(12)
    tf.paragraphs[0].font.name = FONT_FALLBACK
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape


def add_phase_step(slide, left, top, number, label, bullets,
                   icon_shape=None):
    """Add a phase step column (number + label + bullet list)."""
    # Phase label
    add_text_box(slide, left, top, Inches(1.81), Inches(0.47),
                 label, font_size=28, color=C.TEAL,
                 alignment=PP_ALIGN.CENTER, font_name=FONT_DISPLAY)
    # Bullet items
    y = top + Inches(0.50)
    for bullet in bullets:
        add_text_box(slide, left + Inches(0.10), y, Inches(1.80), Inches(0.20),
                     bullet, font_size=10.5, color=C.DARK_BODY,
                     font_name=FONT_BODY)
        y += Inches(0.22)
    return y


def add_footer(slide, text='AidenAI | Confidential'):
    """Add standard footer."""
    add_text_box(slide, Inches(0.45), Inches(7.1), CONTENT_W, Inches(0.3),
                 text, font_size=8, color=C.SILVER,
                 alignment=PP_ALIGN.RIGHT, font_name=FONT_BODY)


def style_table_standard(table):
    """Apply standard Aiden AI table styling."""
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            cell.fill.solid()
            if i == 0:
                cell.fill.fore_color.rgb = C.CYAN
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = C.WHITE
                        run.font.bold = True
                        run.font.size = Pt(14)
                        run.font.name = FONT_BODY
            else:
                cell.fill.fore_color.rgb = C.WASH if i % 2 == 1 else C.WHITE
                for para in cell.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = C.BODY
                        run.font.size = Pt(12)
                        run.font.name = FONT_BODY
```

---

## Part 7: Slide Type Quick Reference

| Slide Type | Background | Title Font | Title Color | Title Size | Key Elements |
|------------|-----------|------------|-------------|------------|--------------|
| **Cover / Title** | `aiden title slide.png` (full-bleed image: wave mesh + logo) | Tungsten Book | `#41B5E1` | 60pt bold | Title at L=0.58/T=1.86, Gold line at L=0.70/T=5.22, Subtitle at L=0.59/T=5.32 FG Book 24pt |
| **Section Divider** | `divider.png` (full-bleed image: photo + gradient + accent squares) | Tungsten Book | White | 80pt number + 28pt title | Number at L=5.69/T=1.91, Title at L=6.08/T=3.49 |
| **Content (standard)** | White | Tungsten-Book | `#00B0F0` | 28-32pt bold | Gold accent, body in FG Book |
| **Content (header bar)** | White + `#42B3DF` top bar | Tungsten-Book | White | 32pt bold | Full-width blue bar top |
| **Content (blue panel)** | White + `#41B5E1` left | Tungsten Book | `#00B0F0` | 28pt | Left blue rounded panel |
| **Content (3 columns)** | `#2193C1`/`#42B3DF`/solid | Tungsten Book | White | 66pt number | Full-height colored columns |
| **Agenda** | White | Tungsten Book | Inherited | Inherited | Groups with agenda items |
| **Team / People** | White | Tungsten Book | Inherited | Inherited | Photo + name + role + table |

---

## Part 8: Design Checklist

Before delivering any PPT, verify:

- [ ] Slide dimensions are 13.333 x 7.5 inches (16:9)
- [ ] Display font is **Tungsten Book** for all headings/titles
- [ ] Body font is **Franklin Gothic Book** throughout
- [ ] No font smaller than 10pt
- [ ] Slide title is Tungsten-Book, `#00B0F0`, 28-32pt, bold
- [ ] Gold accent line (`#FFC000`, 0.68in, 2.25pt) appears below content slide titles
- [ ] Section dividers use dark navy background with large number + white title
- [ ] Cards use `#CCEDFF` fill with `#37CBFF` border
- [ ] Tags/buttons use `#41B4E0` fill with white bold text
- [ ] Horizontal dividers use `#2193C2` or `#41B5E1`
- [ ] Tables have `#41B5E1` header with white bold text
- [ ] Table body has alternating `#FFFFFF` / `#F4F8FA`
- [ ] Body text color is `#083663` (not black)
- [ ] No pure black (`#000000`) for text (except rare diagram fills)
- [ ] No heavy black borders on any shape or table
- [ ] Small triangles (`#41B5E1`) used as bullet indicators where appropriate
- [ ] Subheadings use Tungsten Book, `#2193C2`
- [ ] Outline containers use `#002060` border with no fill
- [ ] No Roboto — this template uses Tungsten + Franklin Gothic families

---

> **Final reminder**: This template's visual identity is defined by the **Tungsten Book + Franklin Gothic Book** font pairing, the **cyan-blue (#41B5E1) + gold (#FFC000) + navy (#083663)** color triad, and the distinctive **gold accent underline** below slide titles. Every slide must feel like it belongs to this system. When in doubt, use Tungsten Book for headings, Franklin Gothic Book 14pt `#083663` for body, and `#CCEDFF` cards with `#37CBFF` borders.
