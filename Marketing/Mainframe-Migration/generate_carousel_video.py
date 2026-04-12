"""
generate_carousel_video.py
Renders each LinkedIn carousel slide at 1080x1080px using Playwright,
then combines into an MP4 video suitable for LinkedIn feed posts.

Run:
    python Marketing/Mainframe-Migration/generate_carousel_video.py

Output:
    Marketing/Mainframe-Migration/html/LinkedIn_Carousel_AIDAP_Mainframe.mp4

LinkedIn video specs:
  - Format: MP4 (H.264)
  - Square: 1080x1080
  - Duration: ~18s (3s per slide)
  - Max file size: 5GB (ours will be tiny)
"""

import os
import time
from pathlib import Path
import numpy as np
from PIL import Image
import imageio

BASE      = Path(r"C:\Users\TanmayDey\OneDrive - AIDEN AI PRIVATE LIMITED\Documents\Programs")
HTML      = BASE / "Marketing" / "Mainframe-Migration" / "html" / "linkedin-carousel.html"
OUT_DIR   = BASE / "Marketing" / "Mainframe-Migration" / "html"
VIDEO_OUT = OUT_DIR / "LinkedIn_Carousel_AIDAP_Mainframe.mp4"

N_SLIDES   = 8
SLIDE_PX   = 1080
FPS        = 30
HOLD_SECS  = 3.0    # seconds each slide is displayed
FADE_SECS  = 0.5    # seconds for cross-fade transition

HOLD_FRAMES = int(HOLD_SECS * FPS)
FADE_FRAMES = int(FADE_SECS * FPS)


def capture_slides():
    """Use Playwright to screenshot each slide at 1080x1080."""
    from playwright.sync_api import sync_playwright

    screenshots = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page    = browser.new_page(viewport={"width": SLIDE_PX, "height": SLIDE_PX})

        file_url = HTML.as_uri()
        page.goto(file_url, wait_until="networkidle")
        time.sleep(1.5)

        for i in range(N_SLIDES):
            page.evaluate(f"""
                var slides = document.querySelectorAll('.slide');
                slides.forEach(function(s) {{ s.classList.remove('active'); }});
                if (slides[{i}]) slides[{i}].classList.add('active');
            """)
            time.sleep(0.6)

            container = (
                page.query_selector(".carousel-viewport")
                or page.query_selector(".carousel-wrapper")
                or page.query_selector("body")
            )
            img_bytes = container.screenshot(type="png")

            tmp = OUT_DIR / f"_frame_{i+1}.png"
            tmp.write_bytes(img_bytes)
            screenshots.append(tmp)
            print(f"  Slide {i+1} captured")

        browser.close()

    return screenshots


def make_video(slide_paths):
    """Combine slide images into an MP4 with cross-fade transitions."""
    images = [np.array(Image.open(p).convert("RGB").resize((SLIDE_PX, SLIDE_PX))) for p in slide_paths]

    writer = imageio.get_writer(
        str(VIDEO_OUT),
        fps=FPS,
        codec="libx264",
        quality=8,
        macro_block_size=None,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart", "-profile:v", "baseline", "-level", "3.0"],
    )

    for idx, frame in enumerate(images):
        # Hold frames for this slide
        for _ in range(HOLD_FRAMES):
            writer.append_data(frame)

        # Cross-fade to next slide (except after last)
        if idx < len(images) - 1:
            nxt = images[idx + 1]
            for f in range(FADE_FRAMES):
                alpha = f / FADE_FRAMES
                blended = (frame * (1 - alpha) + nxt * alpha).astype(np.uint8)
                writer.append_data(blended)

        print(f"  Slide {idx+1} written  ({HOLD_FRAMES} hold + "
              f"{'0' if idx == len(images)-1 else str(FADE_FRAMES)} fade frames)")

    writer.close()


if __name__ == "__main__":
    print("Generating LinkedIn carousel video...")
    slide_paths = capture_slides()

    print("\nBuilding MP4...")
    make_video(slide_paths)

    # Clean up temp PNGs
    for p in slide_paths:
        p.unlink(missing_ok=True)

    size_mb = VIDEO_OUT.stat().st_size / 1_048_576
    total_secs = N_SLIDES * HOLD_SECS + (N_SLIDES - 1) * FADE_SECS
    print(f"\nVideo saved: {VIDEO_OUT}")
    print(f"Duration   : {total_secs:.1f}s")
    print(f"File size  : {size_mb:.1f} MB")
    print(f"Resolution : {SLIDE_PX}x{SLIDE_PX} @ {FPS}fps (H.264 / yuv420p)")
