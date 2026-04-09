#!/usr/bin/env python3
"""
Export LinkedIn carousel to a 10-page, 1080×1080 PDF.

Requirements:
    pip install playwright
    python -m playwright install chromium

Usage:
    python export-pdf.py
"""
import asyncio
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
HTML_FILE  = SCRIPT_DIR / "html" / "linkedin-carousel-print.html"
PDF_OUT    = SCRIPT_DIR / "html" / "linkedin-carousel.pdf"


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: Playwright not installed.")
        print("  Run:  pip install playwright && python -m playwright install chromium")
        sys.exit(1)

    if not HTML_FILE.exists():
        print(f"ERROR: Print HTML not found: {HTML_FILE}")
        sys.exit(1)

    print(f">> Rendering: {HTML_FILE}")

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1080, "height": 1080},
            device_scale_factor=1,
        )
        page = await context.new_page()

        # Load the file and wait for fonts + wave SVGs to render
        await page.goto(f"file://{HTML_FILE}", wait_until="networkidle")
        await page.wait_for_timeout(800)   # extra buffer for Google Fonts

        await page.pdf(
            path=str(PDF_OUT),
            width="1080px",
            height="1080px",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        await browser.close()

    size_kb = PDF_OUT.stat().st_size // 1024
    print(f"OK PDF saved:  {PDF_OUT}")
    print(f"   Pages: 10   Size: {size_kb} KB")


if __name__ == "__main__":
    asyncio.run(main())
