# URL Shortener Skill

## When to Use

Run this skill after deploying any marketing campaign to GitHub Pages (or any public URL). Produces short, shareable links for each asset and saves them alongside the campaign files.

Triggers:
- "shorten the URLs"
- "create short links"
- "make links for external sharing"
- Any time a GitHub Pages site is published for a campaign

---

## How It Works

Uses the **TinyURL public API** — no authentication required, no rate limit for reasonable use.

```
GET https://tinyurl.com/api-create.php?url=<encoded-url>
Returns: the short URL as plain text
```

---

## Step-by-Step Process

### 1. Collect the URLs to shorten

For a standard marketing campaign deployment, shorten:
- Hub page (`/hub.html`)
- Landing page (`/` or `/index.html`)
- Blog article (`/blog.html`)
- Email sequence (`/emails.html`)
- LinkedIn carousel (`/carousel.html`)
- Carousel PDF (`/carousel.pdf`)

Add any additional assets that were deployed.

### 2. Run the shortener

Use this Python snippet (works without any external packages):

```python
import urllib.request, urllib.parse, time

urls = {
    "Hub":      "https://...",
    "Landing":  "https://...",
    # etc.
}

headers = {"User-Agent": "Mozilla/5.0"}

results = {}
for name, url in urls.items():
    api = "https://tinyurl.com/api-create.php?url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(api, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        results[name] = r.read().decode().strip()
    time.sleep(0.4)   # be polite

for name, short in results.items():
    print(f"{name}: {short}")
```

### 3. Save results to the campaign folder

Write a `short-links.md` file to `Marketing/<campaign-name>/` in this format:

```markdown
# Short Links — <Campaign Name>
Generated: <date>

| Asset | Short URL | Full URL |
|-------|-----------|----------|
| Hub | https://tinyurl.com/xxxxx | https://... |
| Landing Page | https://tinyurl.com/xxxxx | https://... |
| Blog | https://tinyurl.com/xxxxx | https://... |
| Email Sequence | https://tinyurl.com/xxxxx | https://... |
| LinkedIn Carousel | https://tinyurl.com/xxxxx | https://... |
| Carousel PDF | https://tinyurl.com/xxxxx | https://... |
```

### 4. Commit the short-links file

```bash
git add short-links.md
git commit -m "Add short links for external sharing"
git push
```

---

## Output to User

After running, present the links in a clean table:

| Asset | Short Link |
|-------|------------|
| Campaign Hub | tinyurl.com/xxxxx |
| Landing Page | tinyurl.com/xxxxx |
| Blog Article | tinyurl.com/xxxxx |
| Email Preview | tinyurl.com/xxxxx |
| LinkedIn Carousel | tinyurl.com/xxxxx |
| Carousel PDF | tinyurl.com/xxxxx |

---

## Notes

- TinyURL links are permanent and free — no expiry
- If TinyURL is down, fallback: `https://ulvis.net/API/write/get?url=<encoded>&private=0`
- Do NOT use is.gd — it blocks non-browser User-Agents
- Short links are **public** — only run on content already deployed publicly
- For private/internal campaigns, use a branded shortener (Rebrandly, Bitly with account) instead
