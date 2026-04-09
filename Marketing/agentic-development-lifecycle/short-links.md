# Short Links — Agentic Development Lifecycle Campaign
## From Builders to Creators | Aiden AI
## Status: PENDING — generate after GitHub Pages deploy

---

## GitHub Pages Setup (one-time)

1. Create a GitHub repo (e.g. `aiden-marketing`) if one doesn't exist
2. In the `Programs/` root, run:
   ```bash
   git init
   git remote add origin https://github.com/<your-username>/aiden-marketing.git
   git add Marketing/agentic-development-lifecycle/
   git commit -m "Deploy ADLC campaign — From Builders to Creators"
   git push -u origin main
   ```
3. Go to repo → **Settings → Pages → Source: Deploy from branch → main → / (root)**
4. Wait ~60 seconds — your site will be live at:
   `https://<your-username>.github.io/aiden-marketing/`

---

## Campaign URLs (fill in after deploy)

Base URL: `https://<your-username>.github.io/aiden-marketing/Marketing/agentic-development-lifecycle/html/`

| Asset | Full URL |
|-------|----------|
| Landing Page | `<base>/index.html` |
| Carousel Preview | `<base>/linkedin-carousel.html` |
| One-Pager | `<base>/one-pager.html` |
| Carousel PDF | `<base>/linkedin-carousel.pdf` |

---

## Generate Short Links (run after deploy)

```python
#!/usr/bin/env python3
# Run: python generate-short-links.py
import urllib.request, urllib.parse, time

BASE = "https://<your-username>.github.io/aiden-marketing/Marketing/agentic-development-lifecycle/html"

urls = {
    "Landing Page":       f"{BASE}/index.html",
    "Carousel Preview":   f"{BASE}/linkedin-carousel.html",
    "One-Pager":          f"{BASE}/one-pager.html",
    "Carousel PDF":       f"{BASE}/linkedin-carousel.pdf",
}

headers = {"User-Agent": "Mozilla/5.0"}
print("Generating short links...\n")
for name, url in urls.items():
    api = "https://tinyurl.com/api-create.php?url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(api, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        short = r.read().decode().strip()
    print(f"  {name:22s}  {short}")
    time.sleep(0.4)
```

---

## Short Links (populate after running script above)

| Asset | Short URL | Status |
|-------|-----------|--------|
| Landing Page | — | ⚠ Pending deploy |
| Carousel Preview | — | ⚠ Pending deploy |
| One-Pager | — | ⚠ Pending deploy |
| Carousel PDF | — | ⚠ Pending deploy |
