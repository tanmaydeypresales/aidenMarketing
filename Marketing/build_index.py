#!/usr/bin/env python3
"""Build Marketing/index.html from every Marketing/*/short-links.md.

Re-run this script any time a new campaign or asset is added.
Usage:  python Marketing/build_index.py
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "index.html"

CAMPAIGN_BLURBS = {
    "AIDAP-TX": "AI-powered testing platform — intelligent test generation, execution, and quality analytics for enterprise transformation.",
    "aiden-discover": "Agentic discovery accelerator — automated requirements, process, and system intelligence extraction.",
    "agentic-development-lifecycle": "Agentic Development Lifecycle — end-to-end AI-assisted SDLC from discovery through deployment.",
    "ai-data-migration": "AI-driven data migration — schema mapping, transformation, reconciliation, and quality at scale.",
    "Mainframe-Migration": "Mainframe modernization — COBOL/AS400 to cloud-native with AI-accelerated refactoring.",
    "agentshub": "AgentsHub — pre-built industry agents for financial services, insurance, and more.",
    "Aiden-AI-Recruiter": "Enterprise-grade, multi-tenant AI recruitment platform for intelligent talent operations from requisition to offer.",
    "Onboard-Agent": "AI-driven onboarding specialist designed to automate the employee and customer lifecycle with proactive orchestration.",
    "Aiden-Tech-Operations": "Enterprise AI for B2B tech operations — automating service desk, infrastructure management, and technical support.",
    "Autonomous-Partner-Onboarding": "Streamlined partner and vendor onboarding with agentic AI — reducing friction and accelerating time-to-value.",
    "AiDAP-Operations": "Agentic operating model for enterprise operations — orchestrating hierarchical agents and semantic memory to scale business functions.",
}


def parse_short_links(md: Path) -> list[tuple[str, str, str]]:
    """Return list of (asset_name, short_url, full_url) rows."""
    rows: list[tuple[str, str, str]] = []
    table_row = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(https?://\S+)\s*\|\s*(https?://\S+)\s*\|")
    for line in md.read_text(encoding="utf-8").splitlines():
        m = table_row.match(line.strip())
        if not m:
            continue
        name = m.group(1).strip()
        if name.lower() in {"asset", "-------"} or set(name) <= {"-", " "}:
            continue
        rows.append((name, m.group(2).strip(), m.group(3).strip()))
    return rows


def discover_campaigns() -> list[dict]:
    campaigns: list[dict] = []
    for sl in sorted(ROOT.glob("*/short-links.md")):
        slug = sl.parent.name
        rows = parse_short_links(sl)
        if not rows:
            continue
        # Prefer a "landing page" row as the primary link.
        primary = next((r for r in rows if "landing" in r[0].lower()), rows[0])
        campaigns.append({
            "slug": slug,
            "title": slug.replace("-", " ").replace("_", " ").title(),
            "blurb": CAMPAIGN_BLURBS.get(slug, ""),
            "primary": primary,
            "assets": rows,
        })
    return campaigns


EXTRA_CARDS: list[dict] = []


def render(campaigns: list[dict]) -> str:
    cards = []
    for extra in EXTRA_CARDS:
        cards.append(f"""
      <article class="card">
        <header>
          <h2>{extra['title']}</h2>
          <p class="blurb">{extra['blurb']}</p>
        </header>
        <a class="cta" href="{extra['href']}" target="_blank" rel="noopener">{extra['cta']} &rarr;</a>
      </article>""")
    for c in campaigns:
        asset_items = "\n".join(
            f'            <li><a href="{full}" target="_blank" rel="noopener">{name}</a> '
            f'<span class="short">{short}</span></li>'
            for name, short, full in c["assets"]
        )
        primary_name, primary_short, primary_full = c["primary"]
        cards.append(f"""
      <article class="card">
        <header>
          <h2>{c['title']}</h2>
          <p class="blurb">{c['blurb']}</p>
        </header>
        <a class="cta" href="{primary_full}" target="_blank" rel="noopener">Open {primary_name} &rarr;</a>
        <details>
          <summary>All assets ({len(c['assets'])})</summary>
          <ul>
{asset_items}
          </ul>
        </details>
      </article>""")

    today = date.today().isoformat()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aiden AI — Marketing Assets</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    :root{{
      --navy:#073663;--dark-navy:#08244B;--electric:#103EE0;--cyan:#12DBD5;
      --light-blue:#E0E4FC;--white:#fff;--text:#1a2744;--muted:#4a5a7a;
      --grad:linear-gradient(89deg,#103EE0 27.33%,#12DBD5 83.11%);
    }}
    body{{font-family:'Poppins',sans-serif;background:#edf1f7;color:var(--text);line-height:1.55}}
    header.hero{{
      background:linear-gradient(135deg,var(--dark-navy) 0%,var(--navy) 60%,var(--electric) 100%);
      color:#fff;padding:72px 32px 88px;text-align:center;position:relative;overflow:hidden
    }}
    header.hero::after{{
      content:"";position:absolute;inset:auto 0 -1px 0;height:40px;
      background:radial-gradient(ellipse at top,rgba(18,219,213,.35),transparent 70%)
    }}
    header.hero h1{{font-size:44px;font-weight:800;letter-spacing:-.5px;margin-bottom:14px}}
    header.hero p{{font-size:18px;opacity:.85;max-width:720px;margin:0 auto}}
    header.hero .tag{{
      display:inline-block;padding:6px 14px;border-radius:999px;
      background:rgba(255,255,255,.12);font-size:12px;letter-spacing:2px;
      text-transform:uppercase;margin-bottom:20px
    }}
    main{{max-width:1200px;margin:-56px auto 0;padding:0 24px 72px;position:relative;z-index:2}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:24px}}
    .card{{
      background:#fff;border-radius:18px;padding:28px 26px;
      box-shadow:0 14px 40px rgba(8,36,75,.08);border:1px solid #e4ebf5;
      display:flex;flex-direction:column;gap:16px;transition:transform .2s,box-shadow .2s
    }}
    .card:hover{{transform:translateY(-4px);box-shadow:0 22px 50px rgba(8,36,75,.14)}}
    .card h2{{font-size:22px;font-weight:700;color:var(--dark-navy)}}
    .card .blurb{{color:var(--muted);font-size:14px}}
    .cta{{
      align-self:flex-start;background:var(--grad);color:#fff;text-decoration:none;
      padding:10px 18px;border-radius:10px;font-weight:600;font-size:14px
    }}
    details{{border-top:1px solid #eef2f8;padding-top:12px;font-size:13px}}
    details summary{{cursor:pointer;font-weight:600;color:var(--electric)}}
    details ul{{list-style:none;margin-top:10px;display:flex;flex-direction:column;gap:6px}}
    details a{{color:var(--text);text-decoration:none;font-weight:500}}
    details a:hover{{color:var(--electric)}}
    .short{{color:var(--muted);font-size:11px;margin-left:6px}}
    footer{{text-align:center;color:var(--muted);font-size:12px;padding:32px 16px}}
    footer a{{color:var(--electric);text-decoration:none}}
  </style>
</head>
<body>
  <header class="hero">
    <span class="tag">Aiden AI</span>
    <h1>Marketing Assets</h1>
    <p>Campaigns, landing pages, carousels, one-pagers, and email copy — all published assets in one place.</p>
  </header>
  <main>
    <section class="grid">{''.join(cards)}
    </section>
  </main>
  <footer>
    Generated {today} &middot; {len(campaigns)} campaigns &middot;
    <a href="https://tanmaydeypresales.github.io/aidenMarketing/">aidenMarketing</a>
  </footer>
</body>
</html>
"""


def main() -> None:
    campaigns = discover_campaigns()
    OUTPUT.write_text(render(campaigns), encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(campaigns)} campaigns.")
    for c in campaigns:
        print(f"  - {c['slug']}: {len(c['assets'])} assets")


if __name__ == "__main__":
    main()
