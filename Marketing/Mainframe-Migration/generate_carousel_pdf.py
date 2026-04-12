"""
generate_carousel_pdf.py
Renders each LinkedIn carousel slide at 1080x1080px using Playwright,
then combines screenshots into a single PDF.

Run:
    python Marketing/Mainframe-Migration/generate_carousel_pdf.py
"""

import os
import sys
import time
from pathlib import Path

BASE    = Path(r"C:\Users\TanmayDey\OneDrive - AIDEN AI PRIVATE LIMITED\Documents\Programs")
HTML    = BASE / "Marketing" / "Mainframe-Migration" / "html" / "linkedin-carousel.html"
OUT_DIR = BASE / "Marketing" / "Mainframe-Migration" / "html"
PDF_OUT = OUT_DIR / "LinkedIn_Carousel_AIDAP_Mainframe.pdf"
N_SLIDES = 8
SLIDE_PX = 1080   # square slide size

# ── Try Playwright approach first ────────────────────────────────────────────
def render_with_playwright():
    from playwright.sync_api import sync_playwright
    from PIL import Image

    screenshots = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page    = browser.new_page(viewport={"width": SLIDE_PX, "height": SLIDE_PX})

        file_url = HTML.as_uri()
        page.goto(file_url, wait_until="networkidle")
        time.sleep(1.5)   # let fonts + animations settle

        for i in range(N_SLIDES):
            # Activate slide i by toggling the 'active' class directly
            page.evaluate(f"""
                var slides = document.querySelectorAll('.slide');
                slides.forEach(function(s) {{ s.classList.remove('active'); }});
                if (slides[{i}]) slides[{i}].classList.add('active');
            """)
            time.sleep(0.5)   # transition + fonts settle

            # Screenshot the carousel container
            container = page.query_selector(".carousel-viewport") or page.query_selector(".carousel-wrapper") or page.query_selector("body")
            img_bytes = container.screenshot(type="png")

            tmp_path = OUT_DIR / f"_slide_{i+1}.png"
            tmp_path.write_bytes(img_bytes)
            screenshots.append(tmp_path)
            print(f"  Slide {i+1} captured")

        browser.close()

    # Combine into PDF with Pillow
    images = [Image.open(p).convert("RGB") for p in screenshots]
    images[0].save(
        PDF_OUT,
        save_all=True,
        append_images=images[1:],
        resolution=150,
        quality=95,
    )
    print(f"\nPDF saved: {PDF_OUT}")

    # Clean up temp PNGs
    for p in screenshots:
        p.unlink(missing_ok=True)


# ── Fallback: ReportLab rebuild ───────────────────────────────────────────────
def render_with_reportlab():
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.lib import colors
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph

    SIZE   = 6 * inch   # 6x6 inch square per slide
    MARGIN = 0.4 * inch

    # Brand colours
    NAVY_DEEP = colors.HexColor("#03091A")
    NAVY      = colors.HexColor("#083663")
    CYAN      = colors.HexColor("#41B5E1")
    TEAL      = colors.HexColor("#2193C2")
    GOLD      = colors.HexColor("#FFC000")
    WHITE     = colors.HexColor("#E8EDF4")
    WHITE_DIM = colors.HexColor("#8FA4BE")
    RED       = colors.HexColor("#E05050")

    c = rl_canvas.Canvas(str(PDF_OUT), pagesize=(SIZE, SIZE))

    def dot_bg(c):
        """Subtle dot grid background."""
        c.setFillColor(NAVY_DEEP)
        c.rect(0, 0, SIZE, SIZE, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#41B5E1"))
        step = 0.30 * inch
        for x in [i * step for i in range(int(SIZE / step) + 1)]:
            for y in [i * step for i in range(int(SIZE / step) + 1)]:
                c.circle(x, y, 0.01 * inch, fill=1, stroke=0)

    def eyebrow(c, text, y, color=CYAN):
        c.setFillColor(color)
        c.setFont("Helvetica", 7)
        c.drawString(MARGIN, y, text.upper())

    def heading(c, text, x, y, size=28, color=WHITE, max_width=SIZE - 2 * MARGIN):
        c.setFillColor(color)
        c.setFont("Times-Bold", size)
        # Simple word wrap
        words = text.split()
        lines = []
        line = ""
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, "Times-Bold", size) <= max_width:
                line = test
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
        for i, ln in enumerate(lines):
            c.drawString(x, y - i * (size + 4), ln)
        return y - len(lines) * (size + 4)

    def body(c, text, x, y, size=10, color=WHITE_DIM, max_width=SIZE - 2 * MARGIN):
        c.setFillColor(color)
        c.setFont("Helvetica", size)
        words = text.split()
        lines = []
        line = ""
        for w in words:
            test = line + (" " if line else "") + w
            if c.stringWidth(test, "Helvetica", size) <= max_width:
                line = test
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
        for i, ln in enumerate(lines):
            c.drawString(x, y - i * (size + 3), ln)
        return y - len(lines) * (size + 3)

    def mono(c, text, x, y, size=8, color=CYAN):
        c.setFillColor(color)
        c.setFont("Courier-Bold", size)
        c.drawString(x, y, text)

    def slide_num(c, n):
        c.setFillColor(WHITE_DIM)
        c.setFont("Courier", 8)
        c.drawRightString(SIZE - MARGIN, MARGIN * 0.5, f"{n} / {N_SLIDES}")
        c.setFillColor(GOLD)
        c.drawString(MARGIN, MARGIN * 0.5, "AIDEN AI")

    def gold_rule(c, y, width=1.0 * inch):
        c.setStrokeColor(GOLD)
        c.setLineWidth(1.5)
        c.line(MARGIN, y, MARGIN + width, y)

    # ── Slide 1: Cover ────────────────────────────────────────────────────────
    dot_bg(c)
    # Gold top accent strip
    c.setFillColor(GOLD)
    c.rect(0, SIZE - 0.08 * inch, SIZE, 0.08 * inch, fill=1, stroke=0)
    # Navy overlay bottom
    c.setFillColor(NAVY)
    c.setFillAlpha(0.3)
    c.rect(0, 0, SIZE, SIZE * 0.35, fill=1, stroke=0)
    c.setFillAlpha(1.0)

    eyebrow(c, "AIDAP  ·  MAINFRAME MODERNISATION", SIZE - MARGIN - 0.32 * inch)
    heading(c, "Why modernisation programmes stall at week 8", MARGIN,
            SIZE - MARGIN - 0.55 * inch, size=32)
    gold_rule(c, SIZE * 0.38)
    mono(c, "AND WHAT ACTUALLY FIXES IT", MARGIN, SIZE * 0.33, size=9, color=CYAN)
    slide_num(c, 1)
    c.showPage()

    # ── Slide 2: The Pattern ──────────────────────────────────────────────────
    dot_bg(c)
    # Ghost WEEK 8 watermark
    c.setFillColor(colors.HexColor("#1A3A5C"))
    c.setFont("Times-Bold", 110)
    c.drawCentredString(SIZE / 2, SIZE * 0.25, "8")
    c.setFillColor(WHITE_DIM)
    c.setFont("Helvetica", 24)
    c.drawCentredString(SIZE / 2, SIZE * 0.44, "WEEK")

    eyebrow(c, "THE PATTERN", SIZE - MARGIN - 0.32 * inch)
    c.setFillColor(WHITE)
    c.setFont("Times-Bold", 22)
    c.drawString(MARGIN, SIZE - MARGIN - 0.55 * inch, "Every bank. Every insurer. Same story.")

    items = [
        ("Business rules — buried and undocumented",   RED),
        ("Dependencies — fragmented across systems",    RED),
        ("SMEs — departed or unavailable",              RED),
        ("Programme decision — deferred, again",        GOLD),
    ]
    y = SIZE * 0.72
    for txt, dot_col in items:
        c.setFillColor(dot_col)
        c.circle(MARGIN + 0.05 * inch, y + 0.04 * inch, 0.045 * inch, fill=1, stroke=0)
        c.setFillColor(WHITE_DIM)
        c.setFont("Courier", 9)
        c.drawString(MARGIN + 0.18 * inch, y, txt)
        y -= 0.28 * inch

    # Gold callout
    c.setFillColor(GOLD)
    c.setFillAlpha(0.08)
    c.rect(MARGIN, 0.18 * inch, SIZE - 2 * MARGIN, 0.28 * inch, fill=1, stroke=0)
    c.setFillAlpha(1.0)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.line(MARGIN, 0.18 * inch, MARGIN, 0.46 * inch)
    mono(c, "THE PROGRAMME STALLS. AGAIN.", MARGIN + 0.14 * inch, 0.28 * inch, size=9, color=GOLD)
    slide_num(c, 2)
    c.showPage()

    # ── Slide 3: The Real Problem ─────────────────────────────────────────────
    dot_bg(c)
    # Right depth panel
    c.setFillColor(NAVY)
    c.setFillAlpha(0.5)
    c.rect(SIZE * 0.55, 0, SIZE * 0.45, SIZE, fill=1, stroke=0)
    c.setFillAlpha(1.0)

    eyebrow(c, "THE ROOT CAUSE", SIZE - MARGIN - 0.32 * inch)
    # Gold left border + pull quote
    c.setStrokeColor(GOLD)
    c.setLineWidth(3)
    c.line(MARGIN, SIZE * 0.35, MARGIN, SIZE * 0.75)
    c.setFillColor(WHITE)
    c.setFont("Times-Italic", 18)
    quote = "Nobody documented it. The people who built it have moved on."
    words = quote.split()
    lines = []; line = ""
    for w in words:
        test = line + (" " if line else "") + w
        if c.stringWidth(test, "Times-Italic", 18) <= SIZE * 0.50:
            line = test
        else:
            lines.append(line); line = w
    if line: lines.append(line)
    for i, ln in enumerate(lines):
        c.drawString(MARGIN + 0.18 * inch, SIZE * 0.72 - i * 0.30 * inch, ln)

    body(c,
         "Decades of pricing logic, eligibility rules, and product controls — "
         "embedded in systems that new teams can't read with confidence.",
         MARGIN + 0.18 * inch, SIZE * 0.42,
         size=9.5, color=WHITE_DIM, max_width=SIZE * 0.50)

    # Gold footer strip
    c.setFillColor(GOLD)
    c.setFillAlpha(0.08)
    c.rect(0, 0.12 * inch, SIZE, 0.36 * inch, fill=1, stroke=0)
    c.setFillAlpha(1.0)
    mono(c, "THIS IS A KNOWLEDGE PROBLEM.", MARGIN, 0.26 * inch, size=10, color=GOLD)
    slide_num(c, 3)
    c.showPage()

    # ── Slide 4: The AIDAP Fix ────────────────────────────────────────────────
    dot_bg(c)
    eyebrow(c, "HOW AIDAP SOLVES IT", SIZE - MARGIN - 0.32 * inch)
    heading(c, "Three steps from opaque to live", MARGIN,
            SIZE - MARGIN - 0.55 * inch, size=22)

    steps = [
        ("01", "7 AI agents read your system landscape",
         "Hours, not months. Every COBOL rule, every JCL dependency,\nevery workflow — extracted into plain English.", True),
        ("02", "A structured knowledge map", "Pricing logic. Eligibility rules. Product controls.\nVisible and governable for the first time.", False),
        ("03", "Migrate layer by layer", "AI intelligence embedded at each layer.\nA smarter system, not a replica.", False),
    ]

    y = SIZE * 0.67
    for num, title, desc, active in steps:
        alpha = 1.0 if active else 0.35
        c.setFillAlpha(alpha)
        if active:
            # Highlighted card
            c.setFillColor(NAVY)
            c.rect(MARGIN - 0.05 * inch, y - 0.42 * inch,
                   SIZE - 2 * MARGIN + 0.10 * inch, 0.52 * inch, fill=1, stroke=0)
            c.setStrokeColor(GOLD)
            c.setLineWidth(2.5)
            c.line(MARGIN - 0.05 * inch, y - 0.42 * inch,
                   MARGIN - 0.05 * inch, y + 0.10 * inch)
        c.setFillColor(GOLD if active else WHITE_DIM)
        c.setFont("Courier-Bold", 20 if active else 16)
        c.drawString(MARGIN, y, num)
        c.setFillColor(WHITE if active else WHITE_DIM)
        c.setFont("Times-Bold", 12 if active else 10)
        c.drawString(MARGIN + 0.45 * inch, y, title)
        if active:
            c.setFillColor(WHITE_DIM)
            c.setFont("Helvetica", 8.5)
            for j, line in enumerate(desc.split("\n")):
                c.drawString(MARGIN + 0.45 * inch, y - 0.18 * inch - j * 0.14 * inch, line)
            if active:
                c.setStrokeColor(CYAN)
                c.setLineWidth(0.5)
                c.rect(MARGIN + 0.45 * inch, y - 0.34 * inch, 1.2 * inch, 0.18 * inch, fill=0, stroke=1)
                mono(c, "HOURS · NOT MONTHS", MARGIN + 0.52 * inch, y - 0.27 * inch, size=6.5, color=CYAN)
        c.setFillAlpha(1.0)
        y -= 0.68 * inch if active else 0.38 * inch

    slide_num(c, 4)
    c.showPage()

    # ── Slide 5: The Output ───────────────────────────────────────────────────
    dot_bg(c)
    eyebrow(c, "THE OUTPUT", SIZE - MARGIN - 0.32 * inch)
    heading(c, "Your system, finally legible", MARGIN,
            SIZE - MARGIN - 0.55 * inch, size=26)

    nodes = [
        ("Pricing Logic",     0.22, 0.62),
        ("Eligibility Rules", 0.50, 0.62),
        ("Product Controls",  0.78, 0.62),
        ("Carrier Rules",     0.22, 0.38),
        ("State DOI",         0.50, 0.38),
        ("System APIs",       0.78, 0.38),
    ]
    connections = [(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5),(0,4),(1,5),(1,3)]
    NW, NH = 0.80 * inch, 0.28 * inch

    # Draw connections first
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.6)
    c.setStrokeAlpha(0.4)
    for a, b in connections:
        ax, ay = nodes[a][1] * SIZE, nodes[a][2] * SIZE
        bx, by = nodes[b][1] * SIZE, nodes[b][2] * SIZE
        c.line(ax, ay, bx, by)
    c.setStrokeAlpha(1.0)

    # Draw node boxes
    for label, nx, ny in nodes:
        cx, cy = nx * SIZE, ny * SIZE
        c.setFillColor(NAVY)
        c.rect(cx - NW/2, cy - NH/2, NW, NH, fill=1, stroke=0)
        c.setStrokeColor(CYAN)
        c.setLineWidth(0.8)
        c.rect(cx - NW/2, cy - NH/2, NW, NH, fill=0, stroke=1)
        c.setFillColor(CYAN)
        c.setFont("Courier-Bold", 8)
        c.drawCentredString(cx, cy - 0.035 * inch, label)

    mono(c, "VISIBLE  ·  STRUCTURED  ·  GOVERNABLE  ·  FOR THE FIRST TIME",
         MARGIN, 0.22 * inch, size=7.5, color=WHITE_DIM)
    slide_num(c, 5)
    c.showPage()

    # ── Slide 6: CTA (full gold) ───────────────────────────────────────────────
    c.setFillColor(GOLD)
    c.rect(0, 0, SIZE, SIZE, fill=1, stroke=0)

    # Navy top strip
    c.setFillColor(NAVY)
    c.rect(0, SIZE - 0.40 * inch, SIZE, 0.40 * inch, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("Courier-Bold", 9)
    c.drawCentredString(SIZE / 2, SIZE - 0.24 * inch, "AIDEN AI  ·  AIDAP")

    c.setFillColor(NAVY)
    c.setFont("Times-Bold", 36)
    c.drawCentredString(SIZE / 2, SIZE * 0.68, "See your system")
    c.drawCentredString(SIZE / 2, SIZE * 0.56, "in 48 hours")

    c.setFont("Helvetica", 12)
    c.drawCentredString(SIZE / 2, SIZE * 0.45, "Discovery session. Your architecture team.")
    c.drawCentredString(SIZE / 2, SIZE * 0.39, "One system domain mapped. No commitment.")

    # CTA button
    btn_w, btn_h = 3.0 * inch, 0.45 * inch
    btn_x, btn_y = (SIZE - btn_w) / 2, SIZE * 0.22
    c.setFillColor(NAVY)
    c.rect(btn_x, btn_y, btn_w, btn_h, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("Courier-Bold", 11)
    c.drawCentredString(SIZE / 2, btn_y + 0.14 * inch, "REQUEST A DISCOVERY SESSION")

    c.setFillColor(NAVY)
    c.setFont("Courier", 8)
    c.drawCentredString(SIZE / 2, 0.18 * inch, "aidenai.com")
    c.showPage()

    c.save()
    print(f"\nPDF saved (ReportLab): {PDF_OUT}")


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating LinkedIn carousel PDF...")
    try:
        from playwright.sync_api import sync_playwright
        from PIL import Image
        print("Using Playwright (pixel-perfect)...")
        render_with_playwright()
    except ImportError:
        print("Playwright not available — using ReportLab...")
        render_with_reportlab()
