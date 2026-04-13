# AiDAP Operations — Marketing Assets

This folder contains the complete marketing asset package for **AiDAP Operations**, positioned as the agentic operating model for the modern enterprise.

## Contents
- `copy/` — Source marketing copy (Brief, Landing Page, Carousel, Email, One-Pager).
- `html/` — Production-grade HTML assets.
- `qa/` — Quality review and scoring report.
- `content-plan/` — Multi-channel distribution plan.
- `export-pdf.py` — Script to generate PDF versions of the carousel and one-pager.

## Quick Start: Publishing

### 1. Generate PDFs
Ensure `playwright` is installed, then run:
```bash
python export-pdf.py
```

### 2. Deploy Landing Page
Copy `html/landing-page.html` to `html/index.html` (if not already done) and push to your GitHub repo to enable GitHub Pages.

### 3. Share Short Links
Once deployed, use the `short-links.md` file to share assets with clients.

---
*Built with Aiden AI Marketing Copy Studio*
