#!/usr/bin/env python3
"""
Export AIDAP-TX marketing assets to PDF.
Requires: pip install playwright
First run: python -m playwright install chromium

Outputs:
  html/one-pager.pdf          — A4 (794 x 1123px)
  html/linkedin-carousel.pdf  — 1080x1080 per slide (7 slides)
"""
import asyncio
from pathlib import Path

SCRIPT_DIR            = Path(__file__).parent
HTML_DIR              = SCRIPT_DIR / "html"

ONE_PAGER_HTML        = HTML_DIR / "one-pager.html"
ONE_PAGER_PDF         = HTML_DIR / "one-pager.pdf"

CAROUSEL_PRINT_HTML   = HTML_DIR / "linkedin-carousel-print.html"
CAROUSEL_PDF          = HTML_DIR / "linkedin-carousel.pdf"


async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # ── One-pager (A4) ────────────────────────────────────────────
        page = await browser.new_page(viewport={"width": 794, "height": 1123})
        await page.goto(f"file://{ONE_PAGER_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(1500)
        await page.pdf(
            path=str(ONE_PAGER_PDF),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        print(f"OK  One-pager PDF:  {ONE_PAGER_PDF}")

        # ── LinkedIn carousel (1080x1080 per slide, 7 slides) ─────────
        if CAROUSEL_PRINT_HTML.exists():
            page2 = await browser.new_page(viewport={"width": 1080, "height": 1080})
            await page2.goto(
                f"file://{CAROUSEL_PRINT_HTML.resolve()}", wait_until="networkidle"
            )
            await page2.wait_for_timeout(1500)
            await page2.pdf(
                path=str(CAROUSEL_PDF),
                width="1080px",
                height="1080px",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
            print(f"OK  Carousel PDF:   {CAROUSEL_PDF}")
        else:
            print(f"SKIP Carousel print HTML not found: {CAROUSEL_PRINT_HTML}")

        await browser.close()


asyncio.run(main())
