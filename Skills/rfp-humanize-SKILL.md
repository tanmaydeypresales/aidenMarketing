---
name: rfp-humanize
description: >-
  Rewrites RFP response text to pass AI-generated content detectors.
  Removes robotic patterns, cliches, filler, and over-structured prose.
  Makes content read like it was written by an experienced solutions
  architect or proposal manager — not a language model.
  Invoke with /rfp-humanize or apply automatically as a post-processing
  step after /rfp-respond.
license: "Internal use"
---

# RFP Humanizer Skill

## Purpose

AI-generated content detectors (GPTZero, Originality.ai, Turnitin, Copyleaks) flag text based on predictable patterns: uniform sentence length, hedge phrases, passive voice clusters, repetitive transitions, and "too-perfect" structure. This skill rewrites RFP text to defeat those detectors while preserving accuracy and professionalism.

## When to Use

- After `/rfp-respond` generates a narrative response
- Before any client-facing document submission
- When the user says "humanize", "make it sound natural", "pass AI detection", "remove AI feel", or "make it not sound like AI"
- Apply to: narrative sections, cover letters, executive summaries, approach descriptions, staffing narratives, and any free-text response

## What NOT to Touch

- Requirement IDs, compliance tables, pricing, technical specifications
- Quoted RFP language or regulatory text
- Data tables, matrices, formulas, or structured data
- Headings and section numbers (formatting only)

---

## AI Detection Patterns to Eliminate

### Pattern 1: Filler Openers & Transitions
These phrases score highest on AI detectors. **Delete or replace every instance.**

| Kill This | Why It Flags | Replace With |
|-----------|-------------|--------------|
| "In today's rapidly evolving..." | Cliche opener, 95% AI-generated | Cut entirely. Start with the point. |
| "It is important to note that..." | Hedge filler | Delete. State the fact directly. |
| "Furthermore," / "Moreover," | Overused AI transitions | Use "Also," or restructure to drop it |
| "In order to" | Verbose | "To" |
| "It is worth mentioning that" | Filler | Delete |
| "This ensures that" | Robotic cause-effect | Rewrite as direct statement |
| "Leveraging" / "Harnessing" | AI buzzword | "Using" or specific verb |
| "Comprehensive" / "Robust" | Overused qualifiers | Cut or use specific descriptor |
| "Seamless" / "Seamlessly" | AI favorite | Cut. Describe what actually happens. |
| "Cutting-edge" / "State-of-the-art" | Marketing fluff | Name the specific technology |
| "Plays a crucial role" | Vague importance claim | Say what it actually does |
| "A wide range of" | Filler | Specific count or list |
| "At its core" | AI structure cliche | Delete |
| "This approach enables" | Passive connector | Name the subject: "Teams can..." |
| "Stakeholders" (overused) | Once is fine, 10 times flags | Use specific names: "DIR staff", "DWC analysts", "claims adjusters" |
| "Best practices" | Vague authority claim | Name the specific practice |
| "World-class" | Unprovable superlative | Delete or cite specific ranking |
| "Empower" / "Empowering" | AI buzzword | "Let", "Allow", "Enable" (sparingly) |
| "Utilize" | Pretentious synonym | "Use" |
| "Facilitate" | Vague | Specific verb: "run", "manage", "coordinate" |
| "Streamline" | Overused | Describe the actual improvement |
| "Holistic" | AI favorite | "Complete", "Full", or cut |
| "Ecosystem" (non-technical) | Overused metaphor | "System", "environment", or specific name |
| "Paradigm" / "Synergy" | Corporate AI cliche | Delete |
| "Moving forward" / "Going forward" | Filler | Delete |
| "It should be noted" | Passive filler | Delete. Just state it. |
| "Key" (as adjective, overused) | Once per page max | "Main", "Primary", or cut |

### Pattern 2: Uniform Sentence Structure
AI detectors measure **perplexity** (word predictability) and **burstiness** (sentence length variation). AI text has low perplexity and low burstiness — every sentence is 15-25 words, medium complexity, predictable.

**Fix:** Vary sentence length deliberately.

```
BAD (AI pattern — every sentence ~20 words):
"The system provides comprehensive audit logging. All user actions are recorded
with timestamps. The audit trail supports compliance requirements. Reports can
be generated on demand."

GOOD (human pattern — mix short and long):
"Every action is logged. The audit trail captures who did what, when, from which
IP, and why — down to field-level changes on claims records. DIR compliance
teams can pull any report on demand, or schedule automated weekly exports to
Cloud Logging."
```

**Rules:**
- Mix sentence lengths: some 5-8 words, some 30-40 words
- Start 20% of sentences with a short fragment or dependent clause
- Use dashes, colons, and parenthetical asides — humans do this naturally
- Occasionally start with "And" or "But" (AI almost never does)
- Use contractions in cover letters and less formal sections ("doesn't" not "does not")
- One rhetorical question per major section is fine

### Pattern 3: Parallel Structure Overuse
AI loves lists where every item starts the same way. Detectors flag this.

```
BAD (AI pattern):
- The system provides real-time monitoring
- The system provides automated alerts
- The system provides self-healing capabilities
- The system provides comprehensive dashboards

GOOD (human pattern):
- Real-time monitoring across all services
- Automated alerts when thresholds breach — no manual watchlists
- Self-healing: failed pods restart in <30 seconds
- Dashboards that DIR ops teams actually use daily, not just at audit time
```

**Rules:**
- Vary list item structure — don't start every bullet the same way
- Mix lengths within lists (some terse, some detailed)
- Add a specific detail or example to 30% of bullets
- Occasionally break a list item into a sub-point

### Pattern 4: Perfect Topic-Sentence Paragraphs
AI writes textbook paragraphs: topic sentence, three supporting points, concluding sentence. Every time.

**Fix:** Break the pattern.

- Start some paragraphs with context or an example, not the main point
- Merge related short paragraphs into one longer one
- Use a one-sentence paragraph for emphasis (humans do this; AI doesn't)
- Let some paragraphs end without a tidy summary — just stop when the point is made
- Occasionally reference something from a previous section ("As described in Section 3.1...")

### Pattern 5: Passive Voice Clusters
AI defaults to passive voice. Three or more passive sentences in a row is a strong AI signal.

```
BAD: "The data is encrypted. The keys are managed by Cloud KMS. The access is
controlled by IAM policies."

GOOD: "Cloud KMS manages all encryption keys. IAM policies control who touches
what. Every byte at rest uses AES-256 — no exceptions."
```

**Rules:**
- Active voice for 70%+ of sentences
- Name the actor: "Cloud Spanner handles..." not "Data is handled by..."
- Passive is fine for emphasis: "No claims data is ever stored outside the US." (deliberate)

### Pattern 6: Hedge Language
AI hedges constantly to avoid being wrong. Humans in proposals are assertive.

| AI Hedge | Human Version |
|----------|--------------|
| "This can potentially help reduce..." | "This cuts processing time by 30%." |
| "It is generally recommended..." | "We do this on every engagement." |
| "This may contribute to improved..." | "This improves throughput." |
| "The solution is designed to support..." | "The solution supports..." |
| "We believe this approach will..." | "This approach delivers..." |

### Pattern 7: Emotional Flatness
AI text is emotionally neutral — no conviction, no confidence, no edge. Proposals need conviction.

**Add (sparingly):**
- Confidence: "We've done this before. The pattern works."
- Specificity over generality: "We ran this at Allianz across 3 regions" not "We have extensive experience"
- Mild informality in appropriate places: "The short answer: yes, it scales."
- Direct address: "Your team will have..." not "The client team will have..."
- Occasional first-person: "We chose Cloud Spanner because..." not "Cloud Spanner was selected because..."

---

## Rewrite Process

When `/rfp-humanize` is invoked on a document or text block:

### Step 1: Scan & Flag
Read the entire text. Identify every instance of:
- Filler openers and transitions (Pattern 1 kill list)
- Uniform sentence runs of 3+ sentences within 5 words of each other (Pattern 2)
- Parallel list items starting with the same words (Pattern 3)
- Perfect topic-sentence paragraphs (Pattern 4)
- Passive voice clusters of 3+ (Pattern 5)
- Hedge phrases (Pattern 6)
- Emotionally flat sections with no conviction (Pattern 7)

### Step 2: Rewrite
Apply fixes section by section:
1. **Delete** all filler phrases from Pattern 1 kill list. Do not replace with synonyms — just cut them.
2. **Vary** sentence length: insert 2-3 short sentences (5-8 words) per page. Extend 1-2 sentences to 30+ words with specifics.
3. **Break** parallel list structures. Vary at least 40% of list items.
4. **Restructure** 30% of paragraphs to not start with a topic sentence.
5. **Flip** passive to active voice where the actor is known.
6. **Sharpen** hedges to direct claims backed by evidence.
7. **Inject** 1-2 conviction statements per major section.

### Step 3: Verify
After rewriting, check:
- [ ] No sentence starts with "It is important to note" or similar filler
- [ ] No paragraph uses "comprehensive" AND "robust" AND "seamless"
- [ ] Sentence lengths vary: check that at least 20% are under 10 words and 10% are over 30
- [ ] No list has 4+ items starting with the same word
- [ ] Active voice is dominant (>70%)
- [ ] Specific numbers, names, or examples appear every 2-3 paragraphs
- [ ] The text reads like a human solutions architect wrote it under deadline — confident, direct, occasionally imperfect

### Step 4: Preserve Accuracy
- Never change technical facts, numbers, requirement IDs, or compliance claims
- Never invent case studies or metrics
- Never add humor, slang, or casual language to formal compliance sections
- Keep all RFP requirement references intact
- Maintain section numbering and heading hierarchy

---

## Integration with RFP Pipeline

### Automatic Application
When integrated into the `/rfp-respond` pipeline, apply humanization as the final pass before document generation:

```
/rfp-respond → generate narrative → /rfp-humanize (auto) → format document → save
```

### Manual Invocation
```
/rfp-humanize                    — humanize the last generated narrative
/rfp-humanize <file.docx>       — humanize a specific document
/rfp-humanize --section 2.1     — humanize a specific section only
/rfp-humanize --check-only      — scan and report issues without rewriting
```

---

## Quick Reference Card

### Always Delete
- "In today's rapidly evolving"
- "It is important to note"
- "Furthermore" / "Moreover"
- "In order to"
- "It is worth mentioning"
- "Plays a crucial role"
- "At its core"
- "Moving forward"

### Always Replace
| From | To |
|------|----|
| Utilize | Use |
| Facilitate | (specific verb) |
| Leverage | Use |
| Comprehensive | (cut or specific) |
| Robust | (cut or specific) |
| Seamless | (cut — describe the mechanism) |
| Stakeholders | (name the actual group) |
| Best practices | (name the practice) |
| Streamline | (describe the improvement) |
| Holistic | Complete / Full / (cut) |

### Always Vary
- Sentence length (5-40 words, mixed)
- List item structure (don't repeat openers)
- Paragraph openers (not always topic sentence)
- Voice (70% active, 30% passive for emphasis)

### Always Add
- Specific numbers over vague claims
- Named technologies over generic categories
- Client-specific references over generic "stakeholders"
- 1-2 conviction statements per section
- At least one short punchy sentence per page
