#!/usr/bin/env python3
"""
Export LinkedIn carousel (1080x1080) and one-pager (A4) to PDF.

Requires:
    pip install playwright
    python -m playwright install chromium
"""
import asyncio
from pathlib import Path

SCRIPT_DIR     = Path(__file__).parent
CAROUSEL_HTML  = SCRIPT_DIR / "html" / "linkedin-carousel-print.html"
CAROUSEL_PDF   = SCRIPT_DIR / "html" / "linkedin-carousel.pdf"
ONE_PAGER_HTML = SCRIPT_DIR / "html" / "one-pager.html"
ONE_PAGER_PDF  = SCRIPT_DIR / "html" / "one-pager.pdf"


async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # 1. Carousel — 1080x1080 px per page
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})
        await page.goto(f"file://{CAROUSEL_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(1200)
        await page.pdf(
            path=str(CAROUSEL_PDF),
            width="1080px", height="1080px",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        print(f"OK Carousel PDF: {CAROUSEL_PDF}")

        # 2. One-pager — A4
        page = await browser.new_page(viewport={"width": 794, "height": 1123})
        await page.goto(f"file://{ONE_PAGER_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.pdf(
            path=str(ONE_PAGER_PDF),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        print(f"OK One-pager PDF: {ONE_PAGER_PDF}")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
