#!/usr/bin/env python3
"""
Export AIDAP-TX one-pager to PDF.
Requires: pip install playwright
First run: python -m playwright install chromium
"""
import asyncio
from pathlib import Path

SCRIPT_DIR    = Path(__file__).parent
ONE_PAGER_HTML = SCRIPT_DIR / "html" / "one-pager.html"
ONE_PAGER_PDF  = SCRIPT_DIR / "html" / "one-pager.pdf"


async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # One-pager — A4
        page = await browser.new_page(viewport={"width": 794, "height": 1123})
        await page.goto(f"file://{ONE_PAGER_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(1200)  # allow Google Fonts to load
        await page.pdf(
            path=str(ONE_PAGER_PDF),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        print(f"OK  One-pager PDF: {ONE_PAGER_PDF}")

        await browser.close()


asyncio.run(main())
