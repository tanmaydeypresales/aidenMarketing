#!/usr/bin/env python3
"""
Export LinkedIn carousel (1080x1080) and one-pager (A4) to PDF.

Requirements:
    pip install playwright
    python -m playwright install chromium

Usage:
    python export-pdf.py
"""
import asyncio
import sys
from pathlib import Path

SCRIPT_DIR     = Path(__file__).parent.resolve()
CAROUSEL_HTML  = SCRIPT_DIR / "html" / "linkedin-carousel-print.html"
CAROUSEL_PDF   = SCRIPT_DIR / "html" / "linkedin-carousel.pdf"
ONE_PAGER_HTML = SCRIPT_DIR / "html" / "one-pager.html"
ONE_PAGER_PDF  = SCRIPT_DIR / "html" / "one-pager.pdf"


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: Playwright not installed.")
        print("  Run:  pip install playwright && python -m playwright install chromium")
        sys.exit(1)

    for f in [CAROUSEL_HTML, ONE_PAGER_HTML]:
        if not f.exists():
            print(f"ERROR: File not found: {f}")
            sys.exit(1)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()

        # 1. Carousel — 1080x1080 px per page
        print(f">> Carousel: {CAROUSEL_HTML.name}")
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})
        await page.goto(f"file://{CAROUSEL_HTML}", wait_until="networkidle")
        await page.wait_for_timeout(800)
        await page.pdf(
            path=str(CAROUSEL_PDF),
            width="1080px", height="1080px",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        kb = CAROUSEL_PDF.stat().st_size // 1024
        print(f"OK Carousel PDF saved — 10 pages, {kb} KB")

        # 2. One-pager — A4
        print(f">> One-pager: {ONE_PAGER_HTML.name}")
        page = await browser.new_page(viewport={"width": 794, "height": 1123})
        await page.goto(f"file://{ONE_PAGER_HTML}", wait_until="networkidle")
        await page.wait_for_timeout(800)
        await page.pdf(
            path=str(ONE_PAGER_PDF),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        kb = ONE_PAGER_PDF.stat().st_size // 1024
        print(f"OK One-pager PDF saved — 1 page, {kb} KB")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
