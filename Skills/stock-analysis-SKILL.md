---
name: stock-analysis
description: Use when generating a stock analysis report, value picks during market corrections, index performance screening, or fundamental buy/sell recommendations for any stock universe (Nifty 50, Sensex, sector index). Outputs a formatted DOCX report using python-docx.
---

# Stock Analysis Report Skill

## Overview
Generates a professional, formatted DOCX stock analysis report that identifies fundamentally strong stocks that have fallen disproportionately due to market corrections, macro shocks, or sector events. Uses python-docx with Aiden-style NAVY/GREEN/RED color scheme.

## Output Path
`RFP/Stock_Analysis/<Index>_Value_Picks_<Month><Year>.docx`

## Trigger Phrases
"stock report", "value picks", "which stocks to buy", "correction opportunities", "index performance", "market fall analysis", stock screening

---

## Report Structure (8 Sections)

| # | Section | Content |
|---|---------|---------|
| 1 | **Market Context** | Macro/geopolitical triggers for the correction; quantify the fall |
| 2 | **Full Index Performance** | All stocks: Price, 1M Fall%, PE, ROE, Quality Rating |
| 3 | **Screening Methodology** | Table of quality filters applied with rationale |
| 4 | **Shortlisted Stocks** | Stocks passing all filters with deepest falls (10-15 stocks) |
| 5 | **Top 5 Conviction Picks** | Individual detail: metrics table + Bull Case bullets + Risk bullets |
| 6 | **Stocks to Avoid** | Fallen stocks with fundamental concerns (PE too high, low ROE, speculative) |
| 7 | **Summary Decision Matrix** | BUY / ACCUMULATE / HOLD / AVOID verdicts for all shortlisted stocks |
| 8 | **Disclaimer** | Standard SEBI investment risk disclaimer + data sources |

---

## Standard Screening Filters

| Quality Parameter | Filter | Rationale |
|---|---|---|
| 1-Month Price Fall | >10% | Meaningful discount from recent levels |
| Return on Equity (ROE) | >15% | Management efficiency; earnings power |
| PE Ratio | <35 | Reasonable valuation; not overpriced growth |
| Debt-to-Equity | <1.5 (non-banks) | Financial stability under stress |
| Market Leadership | Top 3 in sector | Competitive moat; pricing power |
| Earnings Consistency | Profitable last 5 years | No turnaround stories |
| Institutional Quality | Q or Q+ rating | Validated by quant models (MoneyWorks4Me) |

## Verdict Definitions

| Verdict | Criteria |
|---|---|
| **STRONG BUY** | Deep fall (>12%) + PE <20 + ROE >25% |
| **BUY** | Deep fall + passes all quality filters |
| **ACCUMULATE** | Quality stock at slight premium valuation |
| **HOLD** | Good business — wait for better entry or metric confirmation |
| **AVOID** | High PE post-fall, speculative, structural headwinds |

---

## Python Code Pattern (python-docx)

```python
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

NAVY  = RGBColor(0x0B, 0x2D, 0x5B)
GREEN = RGBColor(0x00, 0x7A, 0x33)
RED   = RGBColor(0xC0, 0x39, 0x2B)

doc = Document()

# Heading styles — all NAVY, Calibri
for lvl in range(1, 4):
    hs = doc.styles[f'Heading {lvl}']
    hs.font.name = 'Calibri'
    hs.font.color.rgb = NAVY
    hs.font.bold = True
    hs.font.size = Pt([0, 18, 14, 12][lvl])

# Page margins
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(2.0)
    s.left_margin = s.right_margin = Cm(2.2)

# Helper: paragraph with run
def p(text, bold=False, italic=False, sz=11, color=None):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = bold; run.italic = italic
    run.font.name = 'Calibri'; run.font.size = Pt(sz)
    if color: run.font.color.rgb = color
    return para

# Helper: bullet
def bullet(text):
    para = doc.add_paragraph(text, style='List Bullet')
    for r in para.runs:
        r.font.name = 'Calibri'; r.font.size = Pt(10)

# Helper: table — use 'Light Grid Accent 1' style
def tbl(headers, rows):
    t = doc.add_table(rows=1+len(rows), cols=len(headers))
    t.style = 'Light Grid Accent 1'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = h
        for pr in c.paragraphs:
            pr.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in pr.runs:
                r.bold = True; r.font.name = 'Calibri'; r.font.size = Pt(9)
    for ri, rd in enumerate(rows):
        for ci, val in enumerate(rd):
            c = t.rows[ri+1].cells[ci]; c.text = str(val)
            for pr in c.paragraphs:
                for r in pr.runs:
                    r.font.name = 'Calibri'; r.font.size = Pt(9)
                    if ci == 2 and str(val).startswith('-'):  # Fall% column
                        r.font.color.rgb = RED
    doc.add_paragraph()
```

## Cover Page Pattern
```python
doc.add_paragraph(); doc.add_paragraph()
p("<INDEX> VALUE ANALYSIS", bold=True, sz=24, color=NAVY).alignment = WD_ALIGN_PARAGRAPH.CENTER
p("<Subtitle>", bold=True, sz=14, color=NAVY).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()
p("<Date>", sz=13).alignment = WD_ALIGN_PARAGRAPH.CENTER
p("Prepared by: Claude AI (Research Only — Not Investment Advice)", sz=11).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_page_break()
```

---

## Data Sources
- **Trendlyne** (trendlyne.com) — Price data, top losers, screeners
- **MoneyWorks4Me** (moneyworks4me.com) — Fundamental data, DeciZen quality ratings (Q, Q+)
- **MarketsMojo** (marketsmojo.com) — Analyst upgrades/downgrades
- **Equitymaster** (equitymaster.com) — Index performance data

---

## Reference Implementation
Full working script: `RFP/Stock_Analysis/generate_stock_report.py`
Sample output: `RFP/Stock_Analysis/Nifty50_Value_Picks_March2026.docx`

---

## Standard Disclaimer (Always Include)
```
IMPORTANT: This document is for informational and educational purposes only. It does NOT 
constitute investment advice, a recommendation to buy or sell any security, or a solicitation 
of any offer to buy or sell securities.

- This analysis was generated by an AI system using publicly available data.
- Stock markets are subject to market risks. Past performance does not guarantee future returns.
- Always consult a SEBI-registered financial advisor before making investment decisions.
- Verify all data independently before acting on any information in this document.
```
