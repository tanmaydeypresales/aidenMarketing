---
name: aiden-ai-branding-guidelines
description: >-
  Use this skill whenever producing or directing visual marketing content for
  Aiden AI. Triggers include: LinkedIn image posts, LinkedIn carousels, email
  sharables, client-facing sharables, graphics, infographics, slide decks,
  banners, social media visuals, or any request involving color, font, layout,
  logo, or design decisions for Aiden AI branded content. Always load alongside
  aiden-ai-marketing-SKILL for messaging context and linkedin-visual-content-SKILL
  for LinkedIn-specific copy rules. This skill governs HOW content looks;
  the other skills govern WHAT it says.
license: "Internal use — Confidential"
---

# Aiden AI — Visual Brand Guidelines Skill

This skill defines the complete visual identity system for **Aiden AI** marketing content. It covers color, typography, logo, layout, and channel-specific design specifications for LinkedIn posts, email sharables, and client-facing documents.


---

## Part 1: Color System

### 1.1 Primary Palette

These are the core brand colors. Use them in every piece of content.

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| **Primary Navy** | Deep Navy | `#073663` | Primary text, headings, dark panels, logo color |
| **Electric Blue** | Brand Blue | `#103EE0` | CTAs, buttons, links, key accent, headline highlights |
| **Cyan** | Brand Cyan | `#12DBD5` | Secondary accent, highlight bars, gradient endpoint |
| **Dark Blue (hover)** | Navy Dark | `#093B81` | Button hover states, dark accents |
| **Deep Dark Navy** | Midnight | `#08244B` | Dark slide backgrounds, hero panels, full-bleed dark sections |

### 1.2 Secondary / Support Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| **Light Blue** | Lavender Blue | `#E0E4FC` | Card backgrounds, light section fills, tag/pill backgrounds |
| **Periwinkle** | Soft Blue | `#BCC9FF` | Secondary panel fills, supporting graphic elements |
| **Blue-Violet** | Mid Blue | `#575AC5` | Supporting accents, secondary cards in dark mode |
| **Off-White** | Soft White | `#F8F8F8` | Alternating section backgrounds, light content areas |
| **Light Gray** | Neutral Gray | `#DFE1E2` | Dividers, borders, subtle separators |
| **Teal** | Teal Green | `#1AB9A5` | Tertiary accent, data visualization, success states |

### 1.3 Neutral Palette

| Role | Hex | Usage |
|------|-----|-------|
| **White** | `#FFFFFF` | Primary background, card surfaces, text on dark |
| **Near-Black** | `#0F172A` | Body text on white when maximum contrast needed |
| **Headline Text** | `#08244B` | Default color for all headlines and display text — deeper and heavier than `#073663` |
| **Body / Support Text** | `#64748B` | Supporting copy, descriptions, sub-points — cool medium gray, not navy |
| **Muted Text** | `#D0D8E3` | Captions, labels, secondary text on dark backgrounds |

### 1.4 The Brand Gradient

The signature gradient is a key brand element — use it for hero bars, CTA buttons, accent lines, and highlight elements.

```
Direction: 89deg (left to right)
Start:  #103EE0  (Electric Blue)  at 27%
End:    #12DBD5  (Cyan)           at 83%

CSS: linear-gradient(89deg, #103EE0 27.33%, #12DBD5 83.11%)
```

**Use the gradient for:**
- **Key words or phrases within display headlines** — the primary use (see §1.4a below)
- Illustration and decorative graphic elements — lines, shapes, node diagrams
- CTA button backgrounds on light slides
- Divider lines / section separators as thin accent bars
- Slide number badges or eyebrow labels (sparingly)

**Do NOT use the gradient for:**
- Body text or supporting copy (unreadable at small sizes)
- Full slide/image backgrounds (too intense, overwhelms content)
- More than one element per visual — one gradient element per slide maximum
- Eyebrow labels AND a headline word simultaneously — pick one

### 1.4a Gradient Text on Key Words — The Signature Technique

This is the **primary visual brand technique** for LinkedIn carousels and single image posts. It selectively applies the brand gradient to the single most important word or short phrase in a headline — the word that carries the most meaning, tension, or surprise.

**How it works:**
The headline is set in `#08244B` (dark navy), and one key word or 2–4 word phrase is rendered in the gradient (`#103EE0` → `#12DBD5` left to right). The eye goes directly to the gradient word first.

**Examples from live content:**
```
"The cloud used to host your business.
 Now it [participates] in it."
           ↑ gradient

"Three layers. One outcome:
 infrastructure that [thinks with you.]"
                      ↑ gradient
```

**Rules for using this technique:**
- **One gradient phrase per slide** — if everything is highlighted, nothing is
- The gradient word should be the **verb or payoff** — the word that changes the meaning of the sentence
- Minimum size: 32px — gradient text below this size loses its visual impact
- Works on ExtraBold (800) weight only — thinner weights don't carry gradient well
- Do not apply to more than 4 consecutive words — a whole sentence in gradient loses contrast and punch
- Do not use on eyebrow labels or supporting copy — headlines only

### 1.5 WCAG Contrast Compliance

Enterprise content must meet **WCAG 2.1 AA** minimum contrast standards. Use these pre-verified pairings — do not invent new combinations without checking contrast first.

| Text Color | Background | Contrast Ratio | WCAG Rating | Use For |
|-----------|-----------|---------------|------------|---------|
| `#073663` on `#FFFFFF` | White | **9.8 : 1** | AAA | Primary body text, headings |
| `#073663` on `#F8F8F8` | Off-white | **9.5 : 1** | AAA | Body on section backgrounds |
| `#073663` on `#E0E4FC` | Lavender | **7.2 : 1** | AAA | Text on card fills |
| `#103EE0` on `#FFFFFF` | White | **5.9 : 1** | AA | Links, labels, accent text |
| `#FFFFFF` on `#073663` | Navy | **9.8 : 1** | AAA | Reversed/dark panels |
| `#FFFFFF` on `#08244B` | Dark Navy | **13.4 : 1** | AAA | Dark slide text |
| `#FFFFFF` on `#103EE0` | Electric Blue | **4.6 : 1** | AA | CTA button text |
| `#073663` on `#BCC9FF` | Periwinkle | **5.1 : 1** | AA | Labels on soft blue |

**Failing combinations — never use:**
- `#12DBD5` (cyan) as text on white — fails AA (2.4:1)
- `#BCC9FF` (periwinkle) as text on white — fails AA (2.6:1)
- `#575AC5` on `#E0E4FC` — marginal, avoid for body text
- White text on `#E0E4FC` — fails (1.9:1)
- Any text on the gradient — gradient shifts ratio across the element; use only for decorative elements, never text containers

**Minimum font size for AA compliance:** 14px regular weight, 11px bold weight (digital).

---

### 1.6 Print Color Standards (CMYK)

When producing print assets (client leave-behinds, conference materials, printed one-pagers), use these CMYK equivalents. Do not send RGB hex to a print vendor.

| Color Name | Hex | CMYK | Pantone (closest) |
|-----------|-----|------|--------------------|
| Primary Navy | `#073663` | C:98 M:77 Y:19 K:56 | PMS 281 C |
| Electric Blue | `#103EE0` | C:93 M:72 Y:0 K:12 | PMS 2728 C |
| Cyan | `#12DBD5` | C:72 M:0 Y:10 K:14 | PMS 3255 C |
| Dark Navy | `#08244B` | C:99 M:80 Y:35 K:70 | PMS 539 C |
| Light Blue | `#E0E4FC` | C:12 M:9 Y:0 K:1 | PMS 2717 C |
| White | `#FFFFFF` | C:0 M:0 Y:0 K:0 | — |

> **Note:** Always request a color proof before bulk printing. Cyan `#12DBD5` is a vivid screen color that may shift in CMYK print — verify against a physical proof.

---

### 1.7 Color Mode Rules

**Light Mode (DEFAULT choice for LinkedIn, email sharables, client docs):**
- Background: `#FFFFFF` (pure white) or `#EDEEF4` (cool light gray — see note below)
- Card fill: `#E0E4FC` or `#EDEEF4`
- Primary text: `#08244B` (headlines) / `#64748B` (supporting body text)
- Accent: `#103EE0`
- Pop/highlight: `#12DBD5`

> **Background alternation rule:** When producing multi-slide carousels or multi-section email graphics, alternate between `#FFFFFF` and `#EDEEF4` to create rhythm without introducing new colors. Use white for odd slides/sections, cool gray for even slides/sections. **Do not use the warm `#F8F8F8`** — it reads beige on screen and breaks the cool, crisp brand palette. `#EDEEF4` is the correct brand neutral.

**Dark Mode (for high-impact hero slides, full-bleed carousels, event graphics):**
- Background: `#08244B` or `#073663`
- Primary text: `#FFFFFF`
- Secondary text: `#BCC9FF` or `#E0E4FC`
- Accent: `#103EE0` or `#12DBD5`
- Cards: `#0E2841` or semi-transparent white overlay

**Mixing modes:**
- A single LinkedIn carousel can mix — dark cover slide, light content slides — but must feel intentional, not random
- Never alternate dark/light every slide — dark should only appear on slide 1 (hook) and optionally the final CTA slide

---

## Part 2: Typography

### 2.1 Primary Typeface — Poppins

**Poppins** is the sole brand font for all digital and marketing content. It is the font used across the website and is the consistent voice of Aiden AI.

```
Font family: Poppins
Source: Google Fonts (free, web-safe)
Fallback: Arial, sans-serif
```

**Weight system:**

| Weight | Value | Use For |
|--------|-------|---------|
| **Light** | 300 | Long body text, descriptions, supporting copy |
| **Regular** | 400 | Standard body, paragraph text |
| **Medium** | 500 | Navigation labels, small caps, pill/tag text |
| **SemiBold** | 600 | Subheadings, card titles, emphasized body |
| **Bold** | 700 | Section headings, H2, stat callouts |
| **ExtraBold** | 800 | Hero headlines, H1, display text |

### 2.2 Display Font — Tungsten Book (presentations only)

For large-format presentations and slide decks (not LinkedIn or email), **Tungsten Book** may be used for oversized stat callouts (e.g., "10x" as a standalone number). Do not use in digital/social content.

### 2.3 Typography Scale

**For LinkedIn image/carousel slides:**

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Hero headline | 48–60px | ExtraBold (800) | `#08244B` or `#FFFFFF` |
| Section headline | 32–40px | Bold (700) | `#08244B` or `#FFFFFF` |
| Card/slide title | 24–32px | SemiBold (600) | `#08244B` |
| Supporting line | 16–20px | Regular (400) or Light (300) | `#64748B` (cool gray) |
| Eyebrow / label | 11–14px | Medium (500), ALL CAPS | `#103EE0` |
| Stat / number | 60–80px | ExtraBold (800) | `#103EE0` or gradient |
| CTA text | 14–16px | SemiBold (600) | `#103EE0` or `#FFFFFF` |
| Caption | 10–12px | Light (300) | `#D0D8E3` or muted navy |

**For email sharables:**

| Element | Size | Weight |
|---------|------|--------|
| Email header text | 28–36px | Bold (700) |
| Subheading | 18–22px | SemiBold (600) |
| Body | 14–16px | Regular (400) |
| CTA button | 14–16px | SemiBold (600) |

**For client-facing documents / one-pagers:**

| Element | Size | Weight |
|---------|------|--------|
| Cover title | 36–48px | Bold or ExtraBold |
| Section heading | 24–28px | Bold (700) |
| Body | 10–12px | Regular (400) |
| Callout / stat | 28–40px | ExtraBold (800) |
| Caption / footnote | 8–9px | Light (300) |

### 2.4 Typography Rules

- **Never use more than 2 font weights on a single visual.** Pair ExtraBold headline with Light or Regular body.
- **Letter spacing on labels:** ALL CAPS eyebrow text should have `0.08–0.12em` letter spacing
- **Line height:** Headlines 1.1–1.2x. Body text 1.5–1.6x.
- **Alignment:** Left-align body text. Headlines can be centered on full-width hero slides only.
- **No italic in brand content** — Poppins italic exists but is not part of the Aiden AI brand voice
- **No decorative fonts** — do not substitute Poppins with anything else in marketing output

### 2.5 Accessibility — Typography Requirements (Enterprise Standard)

- **Minimum body text size:** 14px digital / 9pt print — below this, fail WCAG and readability
- **Minimum CTA / button text:** 14px, Medium (500) weight minimum
- **Touch target size:** Any clickable element in digital assets must be at least 44×44px (Apple HIG / WCAG 2.5.5)
- **Line length:** 50–75 characters per line for body text — wider than this degrades readability
- **Text over images:** Only place text on images if there is a solid color overlay with sufficient contrast — never rely on the image providing contrast
- **Never use color alone** to convey meaning — always pair with a text label, icon, or shape difference (e.g., don't signal "required" with red only)
- **Screen reader order:** In email templates, ensure logical reading order matches visual order — do not use layout tables that reorder content visually

---

## Part 3: Logo Usage

### 3.1 Logo Description

The Aiden AI logo is a **lowercase typographic wordmark**: `aiden ai`

- Custom geometric rounded letterforms — the 'a' has a distinctive open circular form
- No separate icon or symbol — the wordmark IS the logo
- The logo reads as two words: `aiden` + `ai`

### 3.2 Logo Color Versions

| Version | When to Use | Logo Color | Background |
|---------|------------|------------|------------|
| **Primary (Dark)** | Light backgrounds, white slides, email, client docs | `#073663` Deep Navy | White / `#F8F8F8` / `#E0E4FC` |
| **Reversed (Light)** | Dark backgrounds, navy slides, dark sections | `#FFFFFF` White | `#08244B` / `#073663` / dark panels |
| **Blue accent** | Light backgrounds where brand blue emphasis needed | `#103EE0` Electric Blue | White only |

### 3.3 Logo Placement Rules

**On LinkedIn single image posts:**
- Logo is **required** on every single image post — no exceptions
- Position: **bottom-right corner** (primary) or **top-right corner** (when illustration occupies bottom-right)
- Minimum size: no smaller than 100px wide in a 1080px canvas
- Clear space: 48px from right edge, 48px from bottom or top edge

**On LinkedIn carousels:**
- Logo is **required on the cover slide (slide 1)** — bottom-right corner or top-right corner
- Logo is **required on the final CTA slide**
- Logo is **optional on interior content slides** — include only if the slide design allows without crowding
- Position: **bottom-right corner** as the default. Use **top-right corner** when an illustration or other element occupies the bottom-right
- The logo position should remain consistent across all slides it appears on — do not switch corners mid-carousel
- Minimum size: no smaller than 100px wide in a 1080px canvas
- Clear space: 48px from edge on all sides — this IS the clear space zone

**On email sharables:**
- Top-left header area OR centered in header band
- Use dark version on white/light backgrounds
- Use reversed version on navy header bands

**On client-facing documents:**
- Cover page: centered or top-left, large (at least 120px wide)
- Running footer: small, bottom-right, light or dark version matching page background
- Never place on a busy background or image without a clean clear zone

### 3.3b Logo Sizing — Minimum Clear Space Rule

Clear space = the height of the lowercase 'a' in the wordmark. Nothing — text, imagery, or other logos — enters this zone.

```
[— clear space —]
    aiden ai
[— clear space —]
```

This applies in all directions. On a 1080px LinkedIn canvas, the logo bottom-right corner should sit 48px from the right edge and 48px from the bottom edge — the 48px padding IS the clear space.

### 3.4 Logo Don'ts

- Do NOT stretch, squash, or rotate the logo
- Do NOT apply drop shadows or outlines to the logo
- Do NOT place on a gradient background (use solid color only)
- Do NOT recolor the logo in any color except the three approved versions above
- Do NOT add "AI" tagline text separately — the wordmark already contains "ai"
- Do NOT use old capitalized version ("AidenAI") — the brand is lowercase `aiden ai`

---

## Part 4: Layout & Composition Principles

### 4.1 Grid & Spacing

**LinkedIn posts (1080 × 1080px square or 1080 × 1350px portrait):**
- Outer margin: 64–80px on all sides (never content in the edge 6%)
- Content safe zone: center 85% of canvas
- Internal padding for cards: 32–48px
- Gutter between elements: 16–24px minimum

**Email sharables (600px wide standard):**
- Outer padding: 40px sides
- Section padding: 32px top/bottom
- Card internal padding: 24px

**Client one-pagers (A4 or US Letter):**
- Margins: 20mm (standard document margins)
- Column gutter: 8mm
- Use 2-column or 3-column grid for content sections

### 4.2 Shape & Geometry Language

Aiden AI's visual language uses **rounded and flowing geometry** — not sharp corners.

**Primary shapes:**
- **Rounded rectangles** — primary container for cards, panels, callout boxes
  - Border radius: 8px (small), 16px (standard card), 24px+ (hero panel)
- **Circles / ovals** — used for accent dots, number badges, icon containers
- **Custom freeform organic shapes** — flowing, asymmetric background elements (used in the deck; recreate in the same spirit — soft, not rigid)
- **Horizontal lines / thin rules** — single-pixel or 2px separators in `#E0E4FC` or gradient

**Avoid:**
- Sharp 0px corners on content boxes
- Heavy thick borders (use fill color, not stroke, to define cards)
- Boxy or rigid geometric compositions
- Overly symmetric layouts that feel static

### 4.3 Card / Panel Patterns

| Pattern | Background | Text | Use When |
|---------|-----------|------|---------|
| **Light card** | `#E0E4FC` | `#073663` | Grouping content on white backgrounds |
| **White card** | `#FFFFFF` with subtle shadow | `#073663` | Primary content cards |
| **Dark card** | `#08244B` | `#FFFFFF` | Feature callouts, dark mode panels |
| **Accent card** | `#103EE0` | `#FFFFFF` | CTA panels, highlighted stats |
| **Ghost card** | Transparent + 1px `#E0E4FC` border | `#073663` | Secondary/supporting items |

### 4.4 Visual Hierarchy Rules

1. **One dominant element per slide/section** — one thing should command attention first
2. **Size = importance** — the most important message is the largest
3. **Color draws the eye** — electric blue `#103EE0` or the gradient should appear on the single most important element only
4. **White space is not empty** — generous padding makes content feel premium, not cramped
5. **Dark anchors light** — a deep navy panel or bar grounds a layout; use it to create structure, not decoration

### 4.5 Visual Storytelling Techniques

Use these techniques to make slides feel like a narrative unfolding — not a static list of facts. Each technique makes the viewer work slightly to connect the dots, which drives engagement.

---

**Technique A — Temporal Weight Progression**

When showing an evolution, timeline, or before/after, communicate time through typography weight and size — not just words. Past or lesser items appear smaller and lighter; the present or key point appears large, bold, and dark.

```
An Example of VISUAL STRUCTURE:

Cloud 1.0 gave you infrastructure.        ← small, #64748B (gray), Regular weight
Cloud 2.0 gave you platforms.             ← medium, #64748B, with key word in SemiBold
Cloud 3.0 gives you a cloud that thinks.  ← large, #08244B, ExtraBold
```

**Rules:**
- Never make all three items the same size — the hierarchy IS the message
- The final item should be at least 2× the font size of the first
- Gray text signals "this is history" — dark navy signals "this is now"
- The key word on the final item can take the gradient for additional emphasis

---

**Technique B — The Gradient Reveal**

Set the headline in dark navy, then apply the gradient to the word that reframes the entire sentence. The viewer reads the setup in dark, and the gradient word lands as the payoff.

```
"The cloud used to HOST your business.
 Now it PARTICIPATES in it."
         ↑ gradient — this word changes everything
```

The gradient draws the eye to the resolution. The dark text provides the context. Together they create a mini narrative on a single slide.

---

**Technique C — Contrast Framing (Not / Now)**

Use structural contrast to create before/after tension without needing two slides.

```
NOT:  [old reality in gray or smaller text]
NOW:  [new reality in dark navy, larger, bolder]
```

Variants: "Before / After", "Then / Now", "Problem / Shift", "Most / Aiden"

---

**Technique D — Progressive Bullet Build**

On a list slide, alternate bold and light to signal which items are the key ones vs. supporting details.

```
• Structured data.                 ← Regular, #64748B
• Unstructured content.            ← key word "Unstructured" in Bold #08244B
• Live signals.                    ← Regular, #64748B
• One intelligence layer.          ← full phrase Bold #08244B — the payoff
• Continuous.                      ← Regular, #64748B — the conclusion
```

Not every bullet deserves equal weight. Bold the claim; light the context.

---

**When to use which technique:**

| Message type | Technique |
|-------------|-----------|
| Showing evolution or before/after | A — Temporal Weight Progression |
| Delivering a reframe or surprising conclusion | B — Gradient Reveal |
| Positioning against a competitor or old way | C — Contrast Framing |
| Walking through a list with a clear winner | D — Progressive Bullet Build |

---

## Part 5: Channel-Specific Specifications

### 5.1 LinkedIn — Image Post

**Canvas:** 1080 × 1080px (square) — preferred
**Alternative:** 1200 × 628px (landscape) for link preview style

**Background options (in order of preference):**
1. White `#FFFFFF` — cleanest, highest contrast in feed
2. Off-white `#F8F8F8` — softer, editorial feel
3. Light blue `#E0E4FC` — brand-tinted, slightly more visual
4. Dark navy `#08244B` — high-impact, use sparingly (max 1 in 5 posts)

**Required elements:**
- Headline text (always)
- Logo — bottom right, minimum 80px wide
- Brand color accent (at minimum: one element in `#103EE0` or gradient)

**Optional elements:**
- Eyebrow label above headline
- Supporting line below headline
- Stat callout
- Thin gradient bar along top or left edge

**Typography on single image:**
- Headline: 48–64px, Poppins ExtraBold or Bold
- Support: 18–22px, Poppins Light or Regular
- Logo: sized proportionally, clear zone respected

---

### 5.2 LinkedIn — Carousel

**Canvas:** 1080 × 1080px per slide (square is most universal)
**Slide count:** 6–8 is optimal for engagement

**Slide background system for a carousel series:**

| Slide | Background | Notes |
|-------|-----------|-------|
| **Cover (Slide 1)** | White `#FFFFFF` — default | Light-first is the brand standard; creates clean, premium impression |
| **Content slides — odd** | White `#FFFFFF` | |
| **Content slides — even** | Cool gray `#EDEEF4` | Alternating backgrounds create rhythm without introducing new colors |
| **CTA (Last slide)** | `#103EE0` (Electric Blue) OR navy `#08244B` | Drive action — make it stand out from content slides |

**Continuity rule:** The logo position, eyebrow label style, and illustration position should remain consistent across all slides. This creates visual flow as the viewer swipes.

**Standard slide template:**
```
┌──────────────────────────────────────┐
│                          [logo] ■    │  ← top-right OR...
│                                      │
│  EYEBROW LABEL          (optional)   │  ← 64px from top, left-aligned
│                                      │
│  HEADLINE TEXT                       │  ← dominant, #08244B ExtraBold
│  with [gradient key word]            │  ← one word/phrase in gradient
│                                      │
│  Supporting line                     │  ← #64748B, Regular/Light
│                                      │
│         [illustration — bottom half] │  ← brand gradient illustration
│                          [logo] ■    │  ← ...OR bottom-right
└──────────────────────────────────────┘
```

> Logo sits in **bottom-right** when illustration is bottom-center or left. Logo moves to **top-right** when illustration occupies the bottom-right corner. Never both corners simultaneously.

**Slide number — required on every carousel slide:**
```
Format:   "Slide X of Y"
Font:     Poppins Regular, 12–13px
Color:    #64748B (cool gray — same as body text)
Position: Bottom edge, opposite corner to logo
          (logo bottom-right → slide number bottom-left, and vice versa)
```
This is a standard carousel navigation element. It appears on every slide including cover and CTA.

---

### 5.3 Email Sharables

**Canvas width:** 600px (standard email width, renders well everywhere)
**Canvas height:** Variable — aim for 300–500px for header graphics; 800–1200px for full email graphics

**Email graphic zones:**

```
┌─────────────────────────────────┐
│  HEADER BAND (80–120px tall)     │  ← navy #073663 or gradient fill
│  [logo left]        [tagline right if needed] │
├─────────────────────────────────┤
│  HERO SECTION (200–280px)        │  ← white or #F8F8F8 background
│  Large headline                  │
│  1–2 lines supporting copy       │
├─────────────────────────────────┤
│  CONTENT SECTION(S)              │  ← alternating white / #F8F8F8 / #E0E4FC
│  Card grid or key points         │
├─────────────────────────────────┤
│  CTA SECTION (80–120px)          │  ← #103EE0 or gradient background
│  Button: white text, rounded 8px │
├─────────────────────────────────┤
│  FOOTER (60–80px)                │  ← #073663 background
│  Logo (white) + contact info     │
└─────────────────────────────────┘
```

**Email color application:**
- Header band: `#073663` (dark navy) — white reversed logo
- Body sections: `#FFFFFF` primary, `#F8F8F8` alternating
- Card fills: `#E0E4FC`
- CTA button: `#103EE0`, white text, 8px border radius, 48px height minimum
- CTA hover: `#093B81`
- Footer: `#073663`, `#FFFFFF` text

**Email dark mode handling (enterprise standard):**
Approximately 35% of email opens are in dark mode (Apple Mail, Outlook on iOS). Design defensively:
- Use `background-color` inline on all sections — do not rely on default white
- Set `color` inline on all text elements — do not rely on inherited black
- For the navy header band: dark mode will likely invert it — test or add a `@media (prefers-color-scheme: dark)` override keeping the header dark
- Export CTA buttons as solid-color HTML buttons (not image-based) — image buttons break in dark mode and get clipped by spam filters
- If producing a graphic-only email image (not HTML), add a thin `#073663` 1px border on the image container so it doesn't bleed into dark-mode white backgrounds
- Always include plain-text fallback for every email — required by CAN-SPAM and good deliverability practice

**Email production standards:**
- Subject line: 40–50 characters (prevents truncation on mobile)
- Preheader text: 85–100 characters
- Total image file size: under 200KB for good deliverability
- Alt text: required on every image — describe the content, not "image"
- Unsubscribe link: must be present and functional (CAN-SPAM / GDPR requirement)
- Sender name: use "Aiden AI" — not a personal name unless from a named person

---

### 5.4 Client Sharables (One-Pagers, Leave-Behinds, Solution Sheets)

**Format:** A4 (210×297mm) or US Letter (8.5×11in) — produce both
**Orientation:** Portrait for documents; Landscape for executive summaries

**Cover page:**
- Full-bleed background: `#08244B` dark navy OR brand gradient (89deg)
- Logo: White reversed, centered or top-left, large (minimum 140px)
- Title: Poppins ExtraBold, 40–48px, white
- Subtitle: Poppins Light, 18–20px, `#BCC9FF` or `#E0E4FC`
- Thin gradient line (3–4px) as a horizontal accent element

**Interior pages:**
- Background: `#FFFFFF`
- Body text: `#073663`, Poppins Regular 10–11px
- Section headings: `#073663`, Poppins Bold 16–20px
- Left accent bar on key sections: 4px solid `#103EE0`
- Stat callouts: `#103EE0` or gradient text, Poppins ExtraBold 32–40px
- Cards / highlighted boxes: `#E0E4FC` fill, 8px border radius
- Running header: thin `#E0E4FC` top border + logo (32px) top right
- Running footer: page number + `aidenai.com` in `#D0D8E3`, 8px

---

## Part 6: Design Patterns & Recurring Motifs

### 6.1 Brand Illustration System — Preferred Visual Pattern

> **This is the primary decorative language for Aiden AI LinkedIn and client content.** Abstract gradient illustrations are preferred over gradient bars (see §6.1b). Use illustrations to occupy the visual weight in the lower or corner portions of a slide — they create brand recognition, add depth, and keep text clean.

**The illustration vocabulary — all styles use brand blue→cyan gradient only:**

| Style | Description | Visual character | Best used on |
|-------|-------------|-----------------|-------------|
| **Crossing arc lines** | Thin curved lines that intersect at angles, with a glow effect at the crossing point — signals converging | Elegant, directional, kinetic | Cover slides, "connection", "convergence", "integration" messaging |
| **3D layered geometry** | Stacked diamond or chevron shapes with glass-like transparency and gradient fills — floating, architectural | Bold, structural, premium | "Platform", "layers", "infrastructure", "stack" messaging |
| **Wireframe grid structure** | Flat perspective grid or layered plane structure in thin lines — technical, precise | Precise, technical, foundational | "Foundation", "data architecture", "enterprise structure" messaging |
| **Network node diagram** | Small spherical nodes connected by flowing curved paths — nodes glow, paths carry gradient color | Organic, intelligent, connected | "Agents", "multi-model", "intelligence", "connectivity" messaging |
| **Flowing wave mesh** | Layered sinusoidal wave lines forming a continuous fabric pattern — like data in motion | Fluid, continuous, dynamic | "Data fabric", "real-time", "flow", "continuous learning" messaging |
| **Concentric ripple rings** | Expanding circles radiating outward from a single origin point — like a signal or impact wave | Expansive, radiating, high-impact | "Scale", "reach", "deployment", "signal", "transformation" messaging |
| **Radial spoke burst** | Thin lines emanating outward from a central point in all directions — like a hub distributing intelligence | Decisive, central, authoritative | "Distribution", "automation", "hub-and-spoke", "orchestration" messaging |
| **Circuit trace pathway** | Right-angle line paths with small node dots at junctions — printed circuit board aesthetic | Technical, precise, systematic | "Automation", "workflow", "processing pipeline", "underwriting" messaging |
| **Helix spiral** | Twin intertwined spiral paths rising upward — like a double helix, gradient transitioning along the curve | Evolutionary, continuous, upward | "Learning", "improvement over time", "AI evolution", "feedback loops" messaging |
| **Topographic contour** | Organic concentric closed curves — like elevation lines on a map, irregular and layered | Complex, landscape, nuanced | "Risk terrain", "complexity mapping", "knowledge graph", "enterprise landscape" messaging |
| **Geometric tessellation** | Interlocking hexagons or triangles in wireframe, gradient applied edge-by-edge | Modular, structured, scalable | "Composable architecture", "modular AI", "enterprise platform", "ecosystem" messaging |
| **Funnel / pipeline flow** | Converging lines that narrow toward a single point or exit — like a submission funnel or processing pipeline | Directed, efficient, process-driven | "Underwriting pipeline", "submission processing", "STP", "workflow automation" messaging |
| **Shield outline** | Geometric shield silhouette rendered in thin gradient lines with inner detail — structured, protective | Secure, trustworthy, enterprise-grade | "Security", "compliance", "governance", "AI guardrails", "audit" messaging |
| **Data stream cascade** | Vertical lines of varying lengths falling downward — like a data waterfall or live feed | Live, real-time, volumetric | "Real-time data", "streaming", "ingestion", "volume", "live signals" messaging |
| **Vortex spiral** | Curved lines that spiral inward to a vanishing point — creates a sense of acceleration and convergence | Transformative, accelerating, magnetic | "Transformation", "speed to production", "from POC to production", "acceleration" messaging |

**Illustration placement rules:**
- Position: bottom-center, bottom-right, or top-right corner — never center-canvas, never overlapping headline text
- Size: occupy 35–50% of the canvas height — large enough to anchor the slide visually, not so large it competes with type
- Opacity: illustrations may be rendered at 70–100% opacity — they should feel present, not ghosted
- Color: **brand gradient only** (`#103EE0` → `#12DBD5`) — no fills, no solid shapes, no other palette colors in illustrations
- Linework: thin (1–2px stroke) — elegant, not heavy. Glow/luminous effect adds depth.
- One illustration style per slide — do not mix styles on the same slide
- One illustration style per carousel — consistency creates a cohesive series

**What illustrations are NOT:**
- Not stock photography
- Not icon sets or clipart
- Not infographics or labeled diagrams
- Not full-bleed backgrounds

### 6.1b The Gradient Bar — Secondary/Alternative Pattern

A thin horizontal bar using the brand gradient (`#103EE0` → `#12DBD5`) is a **secondary option** when an illustration is not available or practical. Prefer illustrations (§6.1) for any visual that will be publicly posted.

- As a **left-edge vertical bar** on cards: draws the eye to the card hierarchy
- As a **text underline** on a key headline section separator
- As a **bottom rule** on email headers

**Spec:** 4–8px thick. Full width of the element it decorates. Do not use at the top of LinkedIn carousel slides — illustrations serve this role.

### 6.2 The Circular Accent

Small filled circles in `#103EE0` or `#12DBD5` used as:
- List bullet replacements
- Number badge backgrounds
- Decorative corner elements
- Step indicators in numbered carousels

**Spec:** 24–48px diameter for badges; 6–8px for bullets.

### 6.3 Pill / Tag Labels

Short all-caps labels in a pill/rounded rectangle container.

```
Background: #E0E4FC
Text color:  #103EE0
Font:        Poppins Medium, 11–13px, ALL CAPS, letter-spacing 0.08em
Padding:     6px 12px
Radius:      99px (fully rounded)
```

Use for: eyebrow labels above headlines, category tags, feature callouts.

### 6.4 Stat Callout Block

Large number + short label beneath, used to highlight proof points.

```
Number:  Poppins ExtraBold, 48–80px, color #103EE0 or gradient text
Label:   Poppins Light, 14–16px, color #073663
Divider: 2px solid #12DBD5 between number and label (optional)
```

### 6.5 Quote / Testimonial Treatment

```
Left border:   4px solid gradient (#103EE0 → #12DBD5)
Quote text:    Poppins Light Italic (exception to no-italic rule), 16–18px, #073663
Attribution:   Poppins Medium, 12–14px, #103EE0
Background:    #F8F8F8 or #E0E4FC card
Padding:       24px left, 20px top/bottom
```

---

## Part 7: What to Avoid

### 7.1 Color Don'ts

| Don't | Why |
|-------|-----|
| Use more than 3 colors per visual | Creates visual noise, dilutes brand |
| Use the gradient as a full background | Overwhelms content, hard to read text on |
| Use orange, red, or yellow as accent | Not part of the brand palette |
| Use warm gray or beige (`#F8F8F8`) as background | Off-brand; use cool gray `#EDEEF4` instead |
| Use gray for headlines | Headlines must be `#08244B` dark navy — `#64748B` gray is for supporting copy only |
| Place navy text on dark navy background | No contrast, unreadable |
| Use white text on light blue `#E0E4FC` | Insufficient contrast |

### 7.2 Typography Don'ts

| Don't | Why |
|-------|-----|
| Mix Poppins with other sans-serif fonts | Inconsistent brand voice |
| Use more than 2 weights on one visual | Cluttered hierarchy |
| Use font size below 10px on print, 12px digital | Accessibility and legibility |
| Set body text in ExtraBold | Reserved for display/headlines only |
| Use ALL CAPS for body paragraphs | Hard to read at length |

### 7.3 Layout Don'ts

| Don't | Why |
|-------|-----|
| Crowd the edges — respect the safe zone | Content gets clipped on different platforms |
| Use more than 4 distinct layout zones per slide | Cognitive overload |
| Center-align everything | Feels generic; left-align body text |
| Use stock photography with obvious watermarks or generic visuals | Undermines enterprise credibility |
| Use clip art or low-resolution icons | Amateur appearance |
| Mix portrait and landscape orientations in a carousel | Breaks the swipe flow |

---

## Part 8: File Format & Asset Standards

### 8.1 File Format by Use Case

| Use Case | Format | Why |
|----------|--------|-----|
| Logo (digital) | **SVG** | Scales infinitely, no pixelation — always preferred |
| Logo (when SVG not supported) | **PNG** with transparent background | Retina-ready, no white box behind logo |
| LinkedIn post / carousel slides | **PNG** at 72–96 DPI, sRGB | LinkedIn compresses JPG — PNG retains quality |
| Email header graphic | **PNG** or **JPG** under 200KB | Balance quality vs deliverability |
| Client one-pager delivery | **PDF** (print-ready, embedded fonts) | Prevents font substitution on recipient's machine |
| Client one-pager edit source | **PPTX or Figma** | Editable by team |
| Presentation deck | **PPTX** + **PDF export** | PPTX for editing, PDF for sending |
| Print materials | **PDF/X-1a** (CMYK, embedded fonts, with bleed) | Print-vendor standard |
| Icons | **SVG** | Always vector for icons |
| Social media sharables | **PNG** | Never JPG for text-heavy graphics |

### 8.2 Resolution Standards

| Context | Resolution | Notes |
|---------|-----------|-------|
| **LinkedIn posts** | 72–96 DPI at 1080×1080px | LinkedIn resamples — export at exact pixel size |
| **Email graphics** | 72 DPI | Retina: export at 2× (e.g., 1200px wide for 600px display) |
| **Print one-pagers** | 300 DPI minimum | 600 DPI for fine detail / small text |
| **Presentations (screen)** | 96 DPI / 1920×1080px | Standard widescreen |

### 8.3 File Naming Convention

Use consistent naming so assets are findable and version-trackable:

```
[dd/mmm]-[content-type]-[descriptor]-[version].[ext]

Examples:
02/mar-linkedin-cloud30-carousel-v1.png
11/feb-email-header-q2campaign-v2.png
27/sep-onepager-aidap-platform-v3.pdf
04/nov-logo-dark-primary.svg
16/dec-logo-white-reversed.svg
```

**Rules:**
- Lowercase, hyphens only (no spaces, no underscores)
- Always include version number (`v1`, `v2`)
- Final approved file: append `-FINAL` before the extension
- Never overwrite a previous version — keep all versions

### 8.4 Asset Library Structure (recommended)

```
/Brand Assets
  /Logos
    aidenai-logo-dark-primary.svg
    aidenai-logo-white-reversed.svg
    aidenai-logo-blue-accent.svg
  /Colors
    aidenai-brand-swatches.ase     ← Adobe Swatch Exchange
    aidenai-brand-swatches.png     ← Reference image
  /Templates
    /LinkedIn
    /Email
    /Client Docs
  /Fonts
    Poppins/ (all weights)
  /Published
    /LinkedIn
    /Email
    /Client
```

---

## Part 9: Co-Branding & Partner Logo Guidelines

When Aiden AI content appears alongside partner or client logos (Unqork, Boomi, InsureMO, Avantos, hyperscalers, etc.):

### 9.1 Logo Lockup Rules

- **Size parity:** Partner logo should be approximately equal in visual weight to the Aiden AI wordmark — not larger
- **Separation:** Use a thin vertical rule (`1px`, `#DFE1E2`) or a clear gap (minimum 40px) between logos — never let logos touch
- **Background:** Both logos on the same solid background — white preferred. Avoid placing partner logos on gradient or textured backgrounds
- **Clear space:** Each logo retains its own required clear space — the lockup gap is in addition to each logo's individual clear space

```
[aiden ai]   |   [Partner Logo]
             ↑
       1px #DFE1E2 rule
       or 40px gap
```

### 9.2 Hierarchy

- On Aiden-produced content: Aiden AI logo appears **first** (left or top position)
- On joint/co-produced content: negotiate position with partner; if no agreement, alphabetical order
- On client case study content: client logo may appear prominently if agreed — Aiden AI logo in footer

### 9.3 Third-Party Logo Standards

- Always use the **official logo file** provided by the partner — never recreate or approximate
- Always use logos on **approved backgrounds** per the partner's own brand guidelines
- Never recolor, crop, or modify partner logos
- If unsure of a partner's logo usage rules, default to their logo on white background at standard weight

### 9.4 Hyperscaler & Platform Partner Badges

AWS, Azure, Google Cloud, Unqork, and similar partners have certified partner badge programs. When using these badges:
- Use only the official badge artwork provided through the partner portal
- Do not resize badges below their specified minimum size
- Display alongside (not above) the Aiden AI logo — partner badges are credentials, not co-equal branding

---

## Part 10: Legal & Compliance Elements

### 10.1 Trademark Usage

- The company name in text is: **Aiden AI** (two words, capital A on each)
- The logo wordmark is: **aiden ai** (lowercase — this is the visual form only)
- Do not add ™ or ® symbols to the logo itself — these are handled at the legal team's direction
- When referencing third-party product names (Claude, GPT-4o, Unqork, etc.) in client-facing content, use their correct capitalization and do not imply ownership

### 10.2 Required Elements by Content Type

| Content Type | Required Elements |
|-------------|------------------|
| **LinkedIn image post** | Logo (every post) |
| **LinkedIn carousel** | Logo on last slide (minimum), optional on cover |
| **Email shareable** | Logo in header, unsubscribe link, company address in footer (CAN-SPAM) |
| **Client one-pager** | Logo on cover and footer, `© [Year] Aiden AI. All rights reserved.` in footer |
| **Case study / reference doc** | Client approval confirmation on file before publishing; client name/logo only with written permission |
| **Press / media content** | Legal review before external distribution |

### 10.3 Copyright Notice

Use this format in footers of client-facing documents:

```
© 2025 Aiden AI. All rights reserved. | aidenai.com
```

For documents spanning calendar years or under active revision, use:

```
© 2024–2025 Aiden AI. All rights reserved.
```

### 10.4 Confidentiality Marking

Client-specific documents (proposals, case studies, solution designs) should carry:

```
CONFIDENTIAL — Prepared for [Client Name]. Not for distribution.
```

Place in the document footer, Poppins Light, 8pt, `#D0D8E3` color. Visible but not dominant.

### 10.5 Disclaimer for AI-Generated Content

If any content was produced with AI assistance and is being shared externally with clients, check whether a disclosure is appropriate under the engagement terms. When in doubt, include:

```
This document was prepared with the assistance of AI tools and reviewed by Aiden AI professionals.
```

---

## Part 11: Brand Governance


### 11.2 Version Control for Templates

- All master templates live in the shared Asset Library (see Part 8.4)
- Templates are versioned (e.g., `linkedin-carousel-template-v3.pptx`)
- When a template is updated, the old version is moved to `/Archive` — never deleted
- Notify the team when a template is updated — do not silently replace the master

### 11.3 Brand Consistency Checklist

Before publishing any marketing visual, verify:

- [ ] Correct logo version used (dark on light / white on dark)
- [ ] Logo clear space respected
- [ ] Only approved brand colors used (no off-palette choices)
- [ ] Poppins font family throughout — no substitutions
- [ ] WCAG AA contrast satisfied for all body text
- [ ] Gradient used on max one element per visual
- [ ] Company name written correctly ("Aiden AI" in text, "aiden ai" in logo only)
- [ ] Copyright or confidentiality notice present where required
- [ ] File saved in correct format and named to convention


---
Part 12: Quick Reference — Design Spec Card

Copy these values directly into design tools (Figma, Canva, PowerPoint, Adobe):

```
=== AIDEN AI BRAND QUICK SPEC ===

COLORS (RGB / HEX)
Primary Navy:     #073663       CMYK: C98 M77 Y19 K56    PMS 281 C
Electric Blue:    #103EE0       CMYK: C93 M72 Y0  K12    PMS 2728 C
Cyan Accent:      #12DBD5       CMYK: C72 M0  Y10 K14    PMS 3255 C
Dark Navy:        #08244B       CMYK: C99 M80 Y35 K70    PMS 539 C
Dark Hover:       #093B81
Light Blue:       #E0E4FC       CMYK: C12 M9  Y0  K1     PMS 2717 C
Periwinkle:       #BCC9FF
Off-white:        #F8F8F8
White:            #FFFFFF       CMYK: C0 M0 Y0 K0
Gradient:         linear-gradient(89deg, #103EE0 27.33%, #12DBD5 83.11%)

WCAG AA VERIFIED PAIRINGS
#073663 on #FFFFFF:   9.8:1 AAA
#103EE0 on #FFFFFF:   5.9:1 AA
#FFFFFF on #103EE0:   4.6:1 AA
#FFFFFF on #08244B:  13.4:1 AAA
#12DBD5 as text:      FAIL -- decorative use only

FONTS
Primary:          Poppins (Google Fonts -- free)
Weights used:     300 / 400 / 500 / 600 / 700 / 800
Fallback:         Arial, sans-serif
Min body size:    14px digital  |  9pt print

BORDER RADIUS
Small:            8px
Standard card:    16px
Pill/badge:       99px

LOGO
Wordmark:         aiden ai (lowercase -- visual form only)
Text form:        Aiden AI (two words, both capitals -- written form)
Dark version:     #073663 on white/light
Light version:    #FFFFFF on dark/navy
Min width:        80px digital  |  25mm print
Clear space:      = height of lowercase a on all sides

CANVAS SIZES
LinkedIn square:   1080 x 1080px  |  72 DPI  |  PNG
LinkedIn portrait: 1080 x 1350px  |  72 DPI  |  PNG
Email width:       600px (export at 1200px for retina)
Client one-pager:  A4 210x297mm or US Letter 8.5x11in
Print resolution:  300 DPI minimum

FILE FORMATS
Digital logo:     SVG (preferred) / PNG transparent
LinkedIn:         PNG
Email graphics:   PNG or JPG under 200KB
Client docs:      PDF (delivery) + PPTX/Figma (source)
Print:            PDF/X-1a, CMYK, embedded fonts

COPYRIGHT
(c) [Year] Aiden AI. All rights reserved. | aidenai.com
```
> **Brand principle**: Aiden AI's visual identity is confident, clean, and enterprise-grade — not flashy. The deep navy grounds everything in credibility. The electric blue and cyan gradient signal forward momentum and intelligence. Poppins Light gives the brand a modern, approachable feel that doesn't sacrifice professionalism. Every visual decision should ask: *does this look like it belongs to a company that ships production AI to the world's top financial institutions and insurers?* If the answer is yes — ship it.
