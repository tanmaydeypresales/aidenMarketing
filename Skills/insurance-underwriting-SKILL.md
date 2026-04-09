---
name: insurance-underwriting-rfp
description: >-
  Use this skill whenever writing, reviewing, or responding to an RFP that
  involves insurance underwriting, policy administration, risk assessment,
  rating engines, submission intake, quote-bind-issue, underwriting workbench,
  loss ratio optimization, reinsurance, or related insurance operations.
  Triggers include any mention of underwriting, P&C insurance, commercial lines,
  specialty lines, life/health underwriting, submission clearance, risk appetite,
  pricing/rating, policy issuance, bordereaux, Lloyd's, MGA/MGU, carrier,
  ACORD, Guidewire, Duck Creek, Majesco, Insurity, or insurance-specific
  compliance (state filings, NAIC, Solvency II, IFRS 17). Covers full domain
  knowledge (LOBs, workflows, regulations, data models, integrations) plus
  Aiden AI / AIDAP solution patterns (AI underwriting agents, risk scoring,
  submission triage, portfolio optimization, compliance bots). Combine with
  the base rfp-response skill and aiden-ai-rfp skill for full proposal
  structure. Use this skill BEFORE writing any insurance underwriting solution
  architecture, module design, or technical narrative.
license: "Internal use — Confidential"
---

# Insurance Underwriting RFP Response Skill

This skill provides **deep domain expertise and Aiden AI solution patterns** for crafting winning RFP responses in the **insurance underwriting, policy administration, and risk assessment** space.

> **Always combine with:**
> - `rfp-response` SKILL.md — overall proposal structure, section templates, pricing format
> - `aiden-ai-rfp` SKILL.md — deep Aiden AI Builder / AIDAP platform details
> - `pricing-calculator` SKILL.md — effort estimation and rate cards
> - `unqork-rfp-skill.md` — if the platform is Unqork (common in insurance)

---

## Part 1: Insurance Underwriting Domain Knowledge

### 1.1 Market Segments & Entity Types

| Entity Type | Role | Key Characteristics | Technology Needs |
|-------------|------|--------------------|--------------------|
| **Carrier** | Risk-bearing insurer | Balance sheet risk, regulatory capital, filed rates | Full-stack policy admin, rating, claims |
| **MGA/MGU** | Managing General Agent/Underwriter | Delegated authority from carrier, own UW guidelines | Submission intake, UW workbench, binding authority |
| **Lloyd's Syndicate** | Specialty market participant | Unique Lloyd's infrastructure, coverholder model | Lloyd's market integration, bordereaux, ACORD |
| **Reinsurer** | Risk transfer from primary carrier | Treaty & facultative, catastrophe modeling | Accumulation tracking, treaty management, ceded premium |
| **Insurtech** | Technology-driven insurer/MGA | Speed, embedded insurance, API-first | Modern tech stack, real-time quoting, digital distribution |
| **Program Administrator** | Manages niche insurance programs | Specialized LOBs, defined authority | Program-specific rating, reporting to carrier |
| **Wholesale Broker** | Places surplus/specialty risks | E&S market access, complex submissions | Submission management, market access, placement |
| **Retail Broker/Agent** | Client-facing distribution | Quote comparison, client advisory | Multi-carrier quoting, CRM, client portal |

**Always ask in RFP analysis:** What entity type is the client? This determines the scope — a carrier needs policy admin + rating + claims; an MGA needs submission intake + UW workbench + bordereaux reporting.

### 1.2 Lines of Business (LOB)

#### Property & Casualty — Commercial Lines

| LOB | Key UW Factors | Complexity | Data Sources |
|-----|---------------|-----------|--------------|
| **Commercial Property** | Building construction, occupancy, protection, exposure (COPE), TIV, CAT exposure | Medium | COPE data, CAT models, loss history, inspections |
| **General Liability** | Operations, revenue, employee count, claims history, contractual obligations | Medium | Applications, loss runs, financial data |
| **Commercial Auto** | Fleet size, radius, driver records, vehicle types, cargo | Medium | MVR reports, fleet data, telematics |
| **Workers' Compensation** | Payroll, class codes (NCCI), experience mod, safety programs | Medium–High | Payroll data, NCCI, loss history, OSHA |
| **Professional Liability (E&O)** | Revenue, practice area, claims history, credentials | High | Applications, regulatory filings, claims |
| **D&O (Directors & Officers)** | Financial health, governance, litigation history, industry risk | High | SEC filings, financial statements, litigation search |
| **Cyber Liability** | IT infrastructure, security posture, revenue, data volume | High | Security scans, questionnaires, breach history |
| **Umbrella/Excess** | Underlying coverage, limits, attachment points | Medium | Underlying policies, loss history |
| **Marine/Cargo** | Vessel type, route, cargo value, loss history | High | Vessel registries, port data, claims |
| **Construction/Builders Risk** | Project type, value, duration, subcontractor quality | High | Project docs, contractor prequalification |
| **Environmental** | Site history, contamination, remediation, regulatory status | Very High | Phase I/II reports, EPA data, regulatory filings |

#### Property & Casualty — Personal Lines

| LOB | Key UW Factors | Automation Potential |
|-----|---------------|---------------------|
| **Homeowners** | Location, construction, protection class, claims history, credit | High — rule-based + AI |
| **Personal Auto** | Driving record, vehicle, credit, usage, territory | Very High — telematics + ML |
| **Renters** | Location, coverage amount, liability | Very High — straight-through |
| **Personal Umbrella** | Underlying limits, assets, risk profile | High |

#### Specialty Lines

| LOB | Unique Challenges | AI Opportunity |
|-----|------------------|---------------|
| **Aviation** | Aircraft type, pilot experience, use category | Document extraction from fleet records |
| **Marine (Hull & P&I)** | Vessel age, flag state, crew, route risk | AIS data analysis, port risk scoring |
| **Energy** | Asset type, location, operational history, CAT | Satellite imagery analysis, IoT data |
| **Political Risk/Trade Credit** | Country risk, counterparty financial health | NLP on geopolitical intelligence |
| **Surety** | Financial strength, work-in-progress, backlog | Financial statement analysis agent |
| **Transactional (M&A)** | Deal structure, target company risk, representations | Data room document analysis |
| **Parametric** | Trigger definition, basis risk, data quality | Real-time parametric trigger monitoring |

#### Life & Health

| LOB | Key UW Factors | AI Opportunity |
|-----|---------------|---------------|
| **Term Life** | Age, health, occupation, lifestyle, family history | Accelerated UW with predictive models |
| **Whole/Universal Life** | Same + investment component, persistency | Illustration optimization |
| **Group Life/Health** | Census data, industry, plan design, experience | Automated group quoting |
| **Disability (STD/LTD)** | Occupation class, income, plan design | Claims prediction models |
| **Long-Term Care** | Age, health, cognitive function, ADL capability | Risk selection with NLP on medical records |

### 1.3 Core Underwriting Workflow

```
Submission Intake → Clearance → Triage/Assignment → Data Gathering →
Risk Assessment → Rating/Pricing → Terms & Conditions → Quote →
Negotiation → Bind → Policy Issuance → Endorsements → Renewal
```

#### Detailed Process Breakdown

**1. Submission Intake**
- Receive submissions via email (60–70% of commercial), portal, API, broker system
- Extract data from ACORD forms (125, 126, 130, 140), applications, SOVs, loss runs
- Identify LOB, classify submission type (new, renewal, endorsement)
- Pain point: Underwriters spend 30–40% of time on data entry from unstructured submissions

**2. Submission Clearance**
- Check for duplicate/existing accounts
- Sanctions/OFAC screening
- Validate within risk appetite (geography, industry, size, LOB)
- Preliminary decline or proceed decision
- Pain point: 40–60% of submissions are outside appetite — fast decline saves UW capacity

**3. Triage & Assignment**
- Score submission complexity (simple/moderate/complex)
- Route to appropriate underwriter based on expertise, authority level, workload
- SLA clock starts (typical: 24–48 hours for initial response)
- Pain point: Uneven workload distribution, SLA breaches on complex submissions

**4. Data Gathering & Enrichment**
- Pull third-party data: D&B, LexisNexis, credit scores, MVRs, property data (CoreLogic, CAPE)
- Request additional information (subjectivities) from broker
- Retrieve prior policy and claims history
- CAT modeling for property (RMS, AIR, CoreLogic)
- Pain point: Manual data collection from 5–15 sources per submission

**5. Risk Assessment**
- Evaluate hazards (physical, moral, morale, legal)
- Analyze loss history (frequency, severity, trends, development)
- Benchmark against portfolio and industry peers
- Apply UW guidelines and risk appetite framework
- Identify risk mitigation opportunities
- Pain point: Subjective, inconsistent risk assessment across underwriters

**6. Rating & Pricing**
- Apply filed or proprietary rating algorithms
- Loss cost development and trending
- Expense loading, profit margin, contingency
- Experience rating, schedule rating, judgment rating
- Layer pricing for excess/umbrella (ILFs, exposure curves)
- Reinsurance cost allocation
- Pain point: Manual spreadsheet-based pricing for complex/specialty risks

**7. Quote & Negotiation**
- Generate quote document with terms, conditions, exclusions, subjectivities
- Compare against competitor quotes (market intelligence)
- Negotiate terms, pricing, and coverage with broker
- Manage quote validity period
- Pain point: Slow turnaround loses business; lack of market intelligence

**8. Bind & Issuance**
- Confirm binding authority and referral thresholds
- Generate binder, policy document, certificates
- Set up billing (direct, agency, installment)
- Establish reinsurance cessions
- File with bureau/state where required
- Pain point: Manual policy document assembly, state-specific form management

**9. Renewal Management**
- 90–120 day renewal pipeline monitoring
- Automated renewal scoring (retention priority)
- Rate change recommendation based on loss experience and market conditions
- Streamlined renewal processing for clean accounts
- Pain point: High-value renewals get lost in volume; retention below target

### 1.4 Regulatory & Compliance Landscape

#### U.S. Insurance Regulation

| Regulation/Body | Scope | Key Requirements | Solution Implication |
|----------------|-------|-----------------|---------------------|
| **State DOI (Dept. of Insurance)** | Rate, form, and market conduct | Rate filings, form approvals, market conduct exams | State-specific form library, filing tracking |
| **NAIC** | Model laws & standards | ORSA, RBC, statutory reporting, MCAS | Reporting engine, capital adequacy monitoring |
| **SERFF** | System for Electronic Rate & Form Filing | Electronic filing for rates and forms | Integration with SERFF for automated filing |
| **OFAC** | Sanctions screening | Screen all insureds, beneficiaries, claimants | Real-time sanctions check in submission intake |
| **State Surplus Lines** | Non-admitted market | Diligent search, surplus lines tax, stamping office | E&S eligibility check, tax calculation |
| **TRIA** | Terrorism Risk Insurance Act | Terrorism risk disclosure, make-available | TRIA premium calculation, disclosure generation |
| **Flood (NFIP/WYO)** | Federal flood insurance | NFIP rating, community rating system | NFIP integration, flood zone lookup |
| **Workers' Comp Bureaus** | NCCI, state bureaus | Class codes, experience mods, residual market | Bureau integration, mod calculation |

#### International Regulations

| Regulation | Jurisdiction | Key Impact on Underwriting |
|-----------|-------------|--------------------------|
| **Solvency II** | EU | Capital requirements, ORSA, risk-based supervision |
| **IFRS 17** | Global | Insurance contract accounting, measurement models |
| **IDD (Insurance Distribution Directive)** | EU | Product governance, demands & needs, conflicts of interest |
| **Lloyd's Minimum Standards** | Lloyd's Market | Peer review, line guide, coverholder audit |
| **IRDAI** | India | Product filing, reinsurance requirements, appointed actuary |
| **APRA** | Australia | Prudential standards, capital adequacy, risk management |
| **PRA/FCA** | UK | Dual regulation, conduct requirements, senior managers regime |

#### Compliance Requirements for Every Proposal

- **Audit trail**: Every underwriting decision must be documented with rationale
- **Authority limits**: Role-based binding authority with referral workflows
- **Rate adequacy**: Demonstrate pricing methodology meets regulatory requirements
- **Fair dealing**: Anti-discrimination in pricing (protected classes), disparate impact testing
- **Data privacy**: Handling of personal/medical information (HIPAA for health, state privacy laws)
- **AI/ML model governance**: Regulatory scrutiny on algorithmic underwriting (Colorado SB21-169, NAIC AI principles)
- **Unfair trade practices**: Compliance with state unfair claims/trade practices acts

### 1.5 Key Data Entities & Standards

#### Core Data Model

```
Submission
  ├── Account (named insured, industry, locations)
  │     ├── Locations / Assets (addresses, buildings, vehicles, operations)
  │     ├── Coverages (LOB, limits, deductibles, endorsements)
  │     ├── Loss History (5–10 years, by occurrence, reserves, payments)
  │     └── Third-Party Data (D&B, credit, MVR, CAT scores, inspections)
  ├── Participants (broker, underwriter, reinsurer, TPA)
  ├── Documents (applications, SOVs, financials, loss runs, engineering)
  └── Workflow State (status, SLA, referrals, approvals)

Policy
  ├── Coverage Structure (per-occurrence, aggregate, sub-limits)
  ├── Forms & Endorsements (ISO, proprietary, manuscript)
  ├── Rating Basis (class codes, exposure base, rate, premium)
  ├── Billing (payment plan, commission, taxes, fees)
  └── Reinsurance (treaty, facultative, cessions)

Claims (for UW reference)
  ├── Loss Detail (date, cause, description, reserves)
  ├── Development (paid, incurred, IBNR)
  └── Subrogation / Recovery
```

#### Industry Standards

| Standard | Purpose | Integration Approach |
|----------|---------|---------------------|
| **ACORD** | Data exchange standard for insurance | ACORD XML/JSON mapping, form recognition |
| **ACORD Forms** | Standard application forms (125, 126, 130, 140) | AI extraction + ACORD field mapping |
| **ISO** | Rating, classification, statistical plans | ISO rate/class integration |
| **NCCI** | Workers' comp classification, experience rating | NCCI API, class code lookup |
| **NAICS/SIC** | Industry classification | Industry risk scoring, appetite matching |
| **COPE** | Property risk characteristics | COPE data capture and validation |
| **RMS/AIR/CoreLogic** | Catastrophe modeling | CAT model integration, accumulation tracking |
| **Verisk** | Rating, analytics, data | ISO/Verisk rating API, loss cost data |
| **CLUE/A-PLUS** | Claims history reporting | LexisNexis CLUE integration |

#### Common Integration Points

| System | Examples | Integration Pattern |
|--------|----------|-------------------|
| **Policy Admin (PAS)** | Guidewire PolicyCenter, Duck Creek, Majesco, Insurity | API, event-driven, batch |
| **Rating Engine** | Guidewire Rating, Earnix, Milliman Arius, proprietary | API call per rate request |
| **Claims** | Guidewire ClaimCenter, Duck Creek Claims, Snapsheet | API for loss history retrieval |
| **Billing** | Guidewire BillingCenter, One Inc, EIS | API for premium/billing setup |
| **Document Management** | OnBase, Alfresco, OpenText, FileNet | API, content services |
| **Broker Portal** | Proprietary, Applied Epic, Vertafore AMS360 | REST API, ACORD messages |
| **Reinsurance** | RMS Risk Intelligence, Guy Carpenter GC Capital | API, file-based |
| **CAT Modeling** | RMS RiskLink, AIR Touchstone, CoreLogic | API or batch, model import |
| **Third-Party Data** | LexisNexis, D&B, CoreLogic, Verisk, Moody's | API, real-time enrichment |
| **Actuarial** | Arius, ResQ, Excel-based models | File import, API where available |
| **Bureau** | NCCI, ISO, state bureaus, SERFF | API, EDI, file-based |
| **Geospatial** | Google Maps, Precisely, Pitney Bowes | API for geocoding, hazard lookup |
| **IoT/Telematics** | Sensor data, wearables, fleet trackers | Streaming ingestion, API |

---

## Part 2: Aiden AI Solution Patterns for Insurance Underwriting

### 2.1 Solution Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────┐
│                      DISTRIBUTION LAYER                              │
│  Broker Portal │ Agent Portal │ Self-Service │ Embedded Insurance     │
├──────────────────────────────────────────────────────────────────────┤
│                      UW EXPERIENCE LAYER                             │
│  UW Workbench │ Submission Dashboard │ Portfolio View │ Renewal Mgr  │
├──────────────────────────────────────────────────────────────────────┤
│                      AIDEN AI AGENT LAYER                            │
│  Submission Triage │ Risk Scoring │ Pricing Agent │ Compliance Agent │
│  Document Intelligence │ Portfolio Optimizer │ Renewal Agent │       │
│  Referral Agent │ Market Intelligence │ Appetite Matching Agent      │
├──────────────────────────────────────────────────────────────────────┤
│                      AIDAP ORCHESTRATION LAYER                       │
│  Agent Orchestrator │ MCP 2.0 Tools │ Memory │ Context Engine        │
├──────────────────────────────────────────────────────────────────────┤
│                      DATA & INTEGRATION LAYER                        │
│  Submission Store │ Policy Admin │ Claims │ Third-Party Data         │
│  Vector DB │ Knowledge Graph │ CAT Models │ Rating Engine            │
├──────────────────────────────────────────────────────────────────────┤
│                      INFRASTRUCTURE LAYER                            │
│  Cloud (AWS/Azure/GCP) │ Security │ Monitoring │ CI/CD              │
└──────────────────────────────────────────────────────────────────────┘
```

### 2.2 AI Agent Catalog — Insurance Underwriting

#### Agent 1: Submission Intake & Triage Agent

**Purpose:** Automate submission intake, extraction, clearance, and intelligent routing.

**Capabilities:**
- Ingest submissions from email, portal, API, and broker feeds
- AI-powered document classification (application vs. SOV vs. loss run vs. financial statement vs. engineering report)
- ACORD form recognition and field extraction (125, 126, 130, 140 series)
- SOV (Schedule of Values) extraction — parse complex multi-sheet Excel/PDF SOVs into structured location data
- Named insured matching and duplicate detection
- OFAC/sanctions screening on all parties
- Risk appetite pre-screening (geography, industry, size, LOB vs. appetite rules)
- Automatic decline with reason for out-of-appetite submissions
- Complexity scoring and intelligent routing to appropriate underwriter
- SLA tracking from first touch

**MCP Tools:** Email connector, ACORD parser, OCR/document extractor, sanctions screener, appetite rules engine, CRM lookup, routing engine, SLA tracker

**Estimated Effort:** 12–16 weeks

#### Agent 2: Data Enrichment & Risk Scoring Agent

**Purpose:** Automatically gather third-party data and produce a preliminary risk score.

**Capabilities:**
- Automated third-party data pulls (D&B, LexisNexis, MVR, CoreLogic, credit, FEMA flood zone)
- COPE data assembly for property risks
- Industry risk benchmarking using NAICS/SIC classification
- Loss history analysis — frequency/severity trending, development factor application, peer comparison
- CAT exposure scoring (hurricane, earthquake, flood, wildfire, convective storm)
- Financial strength assessment from public filings and D&B data
- Litigation and regulatory action search
- Preliminary risk score generation (1–100) with explainable factor breakdown
- Gap identification — flag missing data needed for complete assessment

**MCP Tools:** D&B connector, LexisNexis API, CoreLogic API, FEMA flood tool, CAT model connector, financial data tool, litigation search, risk scoring model

**Estimated Effort:** 10–14 weeks

#### Agent 3: Intelligent Pricing Agent

**Purpose:** AI-augmented pricing that combines actuarial methods with market intelligence.

**Capabilities:**
- Automated rate calculation using filed or proprietary rating algorithms
- Experience rating with loss development and trending
- Schedule rating recommendations with documented rationale
- Layer pricing for excess/umbrella using ILF curves and exposure rating
- Reinsurance cost allocation and net pricing
- Competitive positioning analysis (where does this price sit vs. market?)
- Price optimization within regulatory constraints (avoid unfair discrimination)
- What-if scenarios (impact of deductible changes, limit changes, coverage modifications)
- Minimum premium and rate adequacy validation
- Quote document generation with terms, conditions, and subjectivities

**MCP Tools:** Rating engine connector, loss cost database, ILF tables, market intelligence feed, reinsurance calculator, document generator, compliance checker

**Estimated Effort:** 14–18 weeks

#### Agent 4: Underwriter Copilot

**Purpose:** AI assistant embedded in the UW workbench that augments underwriter decision-making.

**Capabilities:**
- Submission summary generation (one-page brief of key risk factors, concerns, and opportunities)
- Natural language queries on portfolio data ("What's my loss ratio on habitational risks in Florida?")
- Guideline and appetite lookup ("Are we writing restaurants with liquor exposure in TX?")
- Similar risk comparison — find comparable accounts in the book with their outcomes
- Referral preparation — auto-populate referral forms with risk analysis and recommendation
- Endorsement impact analysis — premium, coverage, and exposure implications
- Renewal recommendation engine — rate change, retention priority, terms modification
- Draft broker communications (declinations, quote letters, subjectivity requests)
- Authority limit monitoring and referral triggers

**MCP Tools:** Portfolio data tool, guideline knowledge base, similar risk search (vector), communication drafter, referral workflow, endorsement calculator

**Estimated Effort:** 10–14 weeks

#### Agent 5: Document Intelligence Agent

**Purpose:** Extract, classify, and analyze all underwriting documents using AI.

**Capabilities:**
- Multi-format document ingestion (PDF, Excel, Word, email, scanned images)
- Document classification (application, SOV, loss run, financial statement, inspection report, engineering report, legal filing)
- Intelligent data extraction:
  - **ACORD forms**: Field-level extraction mapped to data model
  - **SOVs**: Multi-sheet Schedule of Values with location/building/coverage parsing
  - **Loss runs**: Carrier-format loss run parsing (every carrier has different format)
  - **Financial statements**: Revenue, assets, liabilities, ratios extraction
  - **Inspection/engineering reports**: Risk recommendations, deficiency extraction
- Cross-document validation (does the SOV match the application? Do loss runs match reported history?)
- NIGO detection with automated correction requests
- Confidence scoring on all extractions with human review routing for low-confidence items
- Document summarization for underwriter review

**MCP Tools:** OCR engine, document classifier, ACORD field mapper, SOV parser, loss run parser, financial extractor, validation engine, confidence scorer

**Estimated Effort:** 14–20 weeks (high variability based on document diversity)

#### Agent 6: Portfolio Optimization Agent

**Purpose:** Continuous portfolio monitoring and strategic optimization recommendations.

**Capabilities:**
- Real-time portfolio dashboards (GWP, NWP, loss ratio, combined ratio by LOB/geography/industry)
- Concentration risk monitoring (geographic, industry, insured-level)
- Aggregation tracking for CAT exposure (PML, AAL by peril and zone)
- Rate adequacy monitoring by segment with trend analysis
- Mix-of-business optimization recommendations
- Underwriter performance analytics (hit ratio, quote-to-bind, loss ratio by UW)
- Emerging risk detection (new loss trends, frequency shifts, severity inflation)
- Reinsurance optimization (treaty vs. facultative, retention analysis)
- What-if modeling for appetite changes (impact on portfolio metrics)

**MCP Tools:** Portfolio data warehouse, CAT accumulation engine, actuarial model connector, market data feed, visualization engine, scenario modeler

**Estimated Effort:** 12–16 weeks

#### Agent 7: Compliance & Regulatory Agent

**Purpose:** Embedded compliance monitoring across all underwriting activities.

**Capabilities:**
- Pre-bind compliance checking (authority limits, referral triggers, restricted classes)
- Rate filing compliance (ensure quoted rates match filed/approved rates)
- Form compliance (correct forms for state/LOB, required endorsements)
- Surplus lines eligibility checking and stamping office requirements
- TRIA disclosure and premium calculation
- Anti-discrimination monitoring (algorithmic fairness testing for AI models)
- State-specific regulatory requirement enforcement
- Market conduct exam readiness (documentation, file completeness scoring)
- Regulatory change monitoring and impact analysis
- Audit trail generation for every underwriting decision

**MCP Tools:** Compliance rules engine, state regulation database, filing tracker, authority limit checker, fairness tester, audit logger, regulatory feed

**Estimated Effort:** 12–16 weeks

#### Agent 8: Renewal Management Agent

**Purpose:** Proactive renewal pipeline management to maximize retention and profitability.

**Capabilities:**
- 120-day renewal pipeline monitoring and prioritization
- Automated renewal scoring: retention value (premium, profitability, relationship) vs. risk (loss deterioration, market pressure)
- Rate change recommendation based on loss experience, rate adequacy, and market conditions
- Streamlined processing for "clean" renewals (no claims, no exposure changes)
- Broker/agent outreach automation with renewal terms preview
- Policy comparison (expiring vs. proposed terms, coverage changes, exclusion modifications)
- Non-renewal identification with documented rationale
- Win-back campaign triggers for lost renewals
- Renewal hit ratio tracking and optimization

**MCP Tools:** Renewal pipeline data, loss analysis tool, rate adequacy calculator, communication drafter, policy comparison engine, CRM connector

**Estimated Effort:** 8–12 weeks

#### Agent 9: Market Intelligence Agent

**Purpose:** Provide underwriters with competitive and market intelligence to improve win rates.

**Capabilities:**
- Market rate monitoring by LOB, geography, and segment
- Competitor appetite changes and market capacity shifts
- Catastrophe event impact analysis (how does this event affect our book and the market?)
- Regulatory change tracking and impact assessment
- Industry trend analysis from trade publications, earnings calls, and AM Best reports
- Broker relationship intelligence (submission patterns, win/loss by broker)
- Emerging risk briefings (cyber trends, social inflation, climate risk, litigation funding)
- Market cycle positioning recommendations

**MCP Tools:** Market data feeds, news aggregator, AM Best connector, regulatory tracker, broker analytics, NLP summarizer

**Estimated Effort:** 8–10 weeks

### 2.3 Underwriting Workbench — The Core UX

Every underwriting proposal must include an **UW Workbench** design. This is the underwriter's daily operating system.

**Workbench Components:**

| Component | Description | AI Enhancement |
|-----------|------------|----------------|
| **Submission Queue** | Prioritized list of submissions with SLA status | AI triage scoring, smart prioritization |
| **Account 360** | Single view of account: risk, coverage, claims, documents, contacts | Auto-assembled from all data sources |
| **Risk Assessment Panel** | Structured risk analysis with scoring | Pre-populated risk score with explainable factors |
| **Pricing Worksheet** | Rating, experience mod, schedule credits, layered pricing | AI-suggested pricing with market context |
| **Document Viewer** | Side-by-side document review with extraction highlights | AI extraction overlay, cross-doc validation |
| **Referral Manager** | Authority tracking, referral submission, approval workflow | Auto-populated referral with AI risk summary |
| **Communication Center** | Broker/agent correspondence, templates, tracking | AI-drafted communications, sentiment analysis |
| **Portfolio Dashboard** | Book of business metrics, drill-down analytics | AI-driven insights, anomaly detection |
| **Guideline Assistant** | Searchable UW guidelines, appetite rules, authority limits | Natural language guideline queries |
| **Renewal Pipeline** | 120-day renewal view with retention scoring | AI renewal prioritization, rate recommendations |

**UX Design Principles for UW Workbench:**
- **One-screen underwriting**: Minimize tab-switching; bring data to the underwriter
- **Progressive disclosure**: Show summary first, drill into detail on demand
- **Keyboard-first**: Power users navigate and act without mouse
- **Exception-based**: Highlight what needs attention, not what's fine
- **Configurable**: Underwriters customize their view by LOB and preference

### 2.4 Key Differentiators vs. Competition

| Traditional Platform | Aiden AI Advantage |
|---------------------|-------------------|
| Manual submission data entry | AI extraction from any document format in seconds |
| Rule-based triage (LOB + state) | ML-driven triage scoring on 50+ factors |
| Underwriter pulls data from 10+ systems | Agent auto-enriches submission before UW sees it |
| Spreadsheet-based pricing | AI pricing with market context and optimization |
| Static guidelines in PDF/wiki | Natural language guideline assistant with reasoning |
| Batch portfolio reports | Real-time portfolio intelligence with anomaly detection |
| Calendar-based renewal reminders | AI-scored renewal prioritization by value and risk |
| Manual compliance checking | Embedded compliance agents in every workflow step |
| Generic document management | AI document intelligence with extraction and validation |
| Siloed data, no institutional memory | Knowledge graph captures and recalls every UW decision |

### 2.5 Straight-Through Processing (STP) Tiers

A key value proposition for underwriting proposals — define STP tiers:

| Tier | Description | Criteria | Target % of Submissions |
|------|------------|----------|------------------------|
| **Tier 1: Full STP** | Auto-quote, auto-bind, no human touch | Clean data, within appetite, low complexity, good loss history, within STP authority | 15–25% (personal) / 5–10% (commercial) |
| **Tier 2: Assisted STP** | AI pre-populates, UW reviews and approves | Moderate complexity, minor data gaps, within appetite but needs judgment | 30–40% |
| **Tier 3: UW-Led** | AI assists, UW drives assessment and pricing | Complex risk, large account, referral required, outside standard appetite | 30–40% |
| **Tier 4: Manual/Specialty** | Full manual underwriting with AI support | Manuscript policies, unique risks, treaty-level, high authority | 10–20% |

**Value narrative:** "Even moving 10% of submissions from Tier 3 to Tier 2 saves an underwriter 15+ hours per week — equivalent to adding 30% capacity without headcount."

### 2.6 Implementation Approach

**Recommended phased approach for underwriting proposals:**

#### Phase 1: Foundation & Intake (Weeks 1–10)
- Submission data model and integration framework
- Submission Intake & Triage Agent (email + portal ingestion)
- Document Intelligence Agent (ACORD forms + SOV extraction)
- Core UW Workbench shell with submission queue
- Authentication, RBAC, authority limits, audit logging
- **Deliverable:** AI-powered submission intake with intelligent routing

#### Phase 2: Underwriting Intelligence (Weeks 11–22)
- Data Enrichment & Risk Scoring Agent
- Underwriter Copilot Agent
- Third-party data integrations (D&B, LexisNexis, CoreLogic)
- UW Workbench: Account 360, risk assessment panel, guideline assistant
- **Deliverable:** AI-augmented underwriting with auto-enrichment and risk scoring

#### Phase 3: Pricing & Quoting (Weeks 23–32)
- Intelligent Pricing Agent
- Rating engine integration
- Quote generation and document assembly
- Broker portal (submission status, quote review, bind request)
- **Deliverable:** End-to-end quote-to-bind with AI pricing

#### Phase 4: Portfolio & Compliance (Weeks 33–42)
- Portfolio Optimization Agent
- Compliance & Regulatory Agent
- Renewal Management Agent
- Portfolio dashboards and analytics
- **Deliverable:** AI-driven portfolio management with embedded compliance

#### Phase 5: Advanced & Optimization (Weeks 43–50)
- Market Intelligence Agent
- Advanced STP rules and auto-bind authority
- Model fine-tuning based on UW feedback and loss emergence
- Performance tuning, load testing, operational readiness
- Training program with UW champions network
- **Deliverable:** Production-ready, optimized underwriting platform

### 2.7 Non-Functional Requirements — Insurance Underwriting Specifics

| NFR | Requirement | Aiden AI Approach |
|-----|------------|------------------|
| **Data Encryption** | AES-256 at rest, TLS 1.3 in transit, PII tokenization | AIDAP native encryption + field-level tokenization |
| **Data Residency** | Comply with state/country data residency laws | Cloud region pinning, data sovereignty controls |
| **Audit Trail** | Every UW decision logged with rationale, immutable, 7+ year retention | Event sourcing with append-only store, tamper-evident |
| **Availability** | 99.95% during business hours (critical for binding) | Multi-AZ, active-active, failover < 30s |
| **RTO/RPO** | RTO < 30 min, RPO < 5 min (binding transactions cannot be lost) | Cross-region replication, WAL shipping |
| **Performance** | Submission intake < 30s, risk score < 5s, rate calc < 3s, quote gen < 10s | Async processing, caching, optimized ML inference |
| **Scalability** | Handle renewal surge (2–3x volume in Q4/Q1), catastrophe event spikes | Auto-scaling, queue-based processing, burst capacity |
| **Document Processing** | Handle 10K+ pages/day, 50+ document formats | Distributed OCR, GPU-accelerated extraction |
| **SOC 2 Type II** | Required by carriers and reinsurers | AIDAP inherits cloud SOC 2; app-level controls |
| **AI Model Governance** | Regulatory scrutiny on algorithmic UW (state DOI, NAIC) | Model inventory, explainability, bias testing, version control |
| **Business Continuity** | Must maintain binding capability during outage | Offline binding capability, sync on recovery |

### 2.8 Pricing Considerations — Underwriting Engagements

When estimating underwriting engagements, account for:

- **Document AI is the #1 differentiator but hardest to get right** — every carrier, every broker, every state has different forms and formats. Budget significant effort for training extraction models. Plan for iterative improvement.
- **Rating engine integration is complex** — proprietary rating algorithms often live in legacy systems (mainframe, Access, Excel). Modernization or wrapping adds 6–10 weeks per LOB.
- **LOB count is the primary scope multiplier** — each LOB has unique data models, rating, forms, and workflows. Budget 60–70% of base effort per additional LOB after the first.
- **State/jurisdiction count matters** — each state has filing requirements, rate variations, and form differences. Group states by regulatory similarity to manage scope.
- **UW guideline digitization takes time** — converting 200-page PDF guidelines into executable rules requires SME collaboration. Budget 4–6 weeks per LOB.
- **Change management is critical** — underwriters are experts resistant to AI encroachment. Position AI as augmentation, not replacement. Budget for UW advisory council and champion program.

**Typical engagement sizes:**

| Scope | Duration | Team Size | Typical Client |
|-------|----------|-----------|---------------|
| **Submission Intake MVP** | 12–16 weeks | 6–8 | MGA wanting digital intake |
| **Single-LOB UW Workbench** | 20–28 weeks | 10–14 | Carrier modernizing one LOB |
| **Multi-LOB UW Platform** | 36–48 weeks | 16–22 | Carrier/MGA, 3–5 LOBs |
| **Enterprise UW Transformation** | 48–60+ weeks | 20–30+ | Large carrier, full commercial lines |

---

## Part 3: Proposal Writing Guidance

### 3.1 Win Themes for Insurance Underwriting RFPs

Use 3–4 of these win themes based on the specific RFP:

1. **AI That Thinks Like an Underwriter**: Our agents don't just automate data entry — they assess risk, score submissions, and recommend pricing using the same factors experienced underwriters consider, with full explainability and audit trails.

2. **From 40% Data Entry to 80% Decision-Making**: By automating submission intake, data enrichment, and document extraction, we shift underwriters from data wranglers to risk experts — handling 2x the submissions with better outcomes.

3. **Institutional Memory, Not Institutional Amnesia**: Every underwriting decision, every market insight, every loss outcome is captured in the knowledge graph — so your best underwriter's judgment scales across the organization and survives turnover.

4. **Speed Wins Business**: Brokers send business to underwriters who respond fast. Our AI-powered triage and enrichment cut first-response time from 48 hours to 4 hours for 60% of submissions.

5. **Compliance by Design, Not by Audit**: Regulatory compliance is embedded in every workflow — authority limits, rate filing checks, form compliance, and full audit trails are automatic, not afterthoughts.

6. **Portfolio Intelligence, Not Just Portfolio Reporting**: Real-time portfolio optimization with AI-driven insights on concentration, rate adequacy, and emerging risks — moving from backward-looking reports to forward-looking strategy.

### 3.2 Common RFP Questions — Insurance Underwriting

| Question | Key Points to Cover |
|----------|-------------------|
| How does your AI handle complex/specialty risks? | Tiered STP model — AI handles simple risks end-to-end, augments underwriters on complex risks; human always in the loop for specialty |
| What document formats can you process? | Any format — PDF, scanned image, Excel, Word, email. Trained on ACORD forms, carrier-specific loss runs, SOVs, engineering reports |
| How do you integrate with our existing PAS? | API-first architecture; pre-built connectors for Guidewire, Duck Creek, Majesco, Insurity; custom adapters for legacy systems |
| How do you handle state-specific requirements? | Configurable rules engine with state-by-state regulatory profiles; form library management; filing tracking |
| What about AI model explainability? | Every AI recommendation includes factor-level explanation; model cards document training data, performance, and limitations; bias testing per NAIC guidelines |
| How do you handle catastrophe events? | CAT model integration (RMS/AIR), accumulation tracking, event-triggered portfolio impact analysis, capacity management |
| Can the system support Lloyd's? | Yes — Lloyd's-specific workflows including slip, MRC, endorsement, bordereaux, and coverholder management |
| What's your approach to UW guidelines? | Digitize guidelines into executable rules in knowledge graph; natural language guideline queries; auto-update from guideline changes |
| How do you measure UW effectiveness? | Hit ratio, quote-to-bind, cycle time, loss ratio by UW, STP rates, SLA compliance — all tracked with AI-driven benchmarking |

### 3.3 Competitor Positioning

| Competitor | Their Strength | Our Counter |
|-----------|---------------|-------------|
| **Guidewire** | Market leader PAS, large install base | We complement Guidewire with AI UW layer; or replace with modern alternative for greenfield |
| **Duck Creek** | Cloud-native PAS, configurable | Our AI agents are a generation ahead; we integrate with or extend Duck Creek |
| **Majesco** | Speed to market, digital platform | We match speed and add deeper AI — document intelligence, risk scoring, portfolio optimization |
| **Insurity** | Specialty lines strength | Our agentic AI handles specialty complexity better than rules-based systems |
| **Unqork** | No-code, rapid UI development | We complement Unqork (common combo); add AI agents that Unqork cannot build natively |
| **Earnix** | Rating/pricing optimization | We go beyond pricing — full submission-to-bind AI, not just the rating step |
| **Shift Technology** | AI for claims/fraud | We cover the UW side; complementary for carriers who also want claims AI |
| **Hyperscience** | Document extraction | Our extraction is purpose-built for insurance (ACORD, SOV, loss runs) not generic OCR |
| **EIS** | Modern core platform | We provide the AI intelligence layer that EIS doesn't have natively |
| **Novidea** | Insurance-specific CRM/mgmt | Our AI UW capabilities far exceed CRM-based workflow automation |

---

## Part 4: Technical Deep Dives (Use When RFP Requires Detail)

### 4.1 Submission Triage Scoring Model

```
Triage Score = f(Complexity Score, Appetite Score, Value Score, Urgency Score)

Complexity Score (30%):
  - LOB complexity (GL=low, D&O=high, environmental=very high)
  - Multi-state/multi-location
  - Manuscript endorsement requirements
  - Reinsurance involvement
  - Historical litigation

Appetite Score (25%):
  - Industry class vs. appetite (green/yellow/red)
  - Geography vs. appetite
  - Account size vs. target range
  - Loss history vs. acceptable benchmarks
  - Concentration impact

Value Score (25%):
  - Premium size (larger = higher priority)
  - Cross-sell potential (multi-LOB account)
  - Broker relationship tier
  - Renewal vs. new business
  - Strategic account flag

Urgency Score (20%):
  - Days until effective date
  - Broker-indicated urgency
  - Competitive situation (incumbent, multi-market)
  - SLA status

Output: 1–100 score → Route to:
  1–25:   Auto-decline (outside appetite) or Tier 1 STP
  26–50:  Tier 2 — Junior UW with AI assistance
  51–75:  Tier 3 — Senior UW
  76–100: Tier 4 — Specialist/referral
```

### 4.2 Loss Development & Experience Rating

```
Experience Rating Process:

1. Collect 5-year loss history (claims, reserves, payments)
2. Apply loss development factors (LDFs) by LOB and maturity
   - Year 1 (most recent): LDF = 2.5–3.0 (most immature)
   - Year 2: LDF = 1.8–2.2
   - Year 3: LDF = 1.3–1.5
   - Year 4: LDF = 1.1–1.2
   - Year 5: LDF = 1.02–1.05
3. Develop each year to ultimate
   Ultimate Loss = Incurred Loss × LDF
4. Apply trend factor for loss cost inflation
   Trended Ultimate = Ultimate × (1 + trend)^years
5. Calculate experience loss ratio
   Exp. Loss Ratio = Total Trended Ultimate / Total Earned Premium
6. Compare to expected loss ratio (class/industry benchmark)
7. Apply credibility weighting
   Modified Loss Ratio = (Z × Experience) + (1-Z × Expected)
   where Z = credibility factor based on premium volume
8. Calculate experience modification factor
   Ex Mod = Modified Loss Ratio / Expected Loss Ratio

AI Enhancement:
- Auto-extract loss data from carrier-format loss runs (every carrier different)
- Detect large loss vs. attritional split automatically
- Flag development anomalies (reserve strengthening, late-reported claims)
- Suggest appropriate LDFs from actuarial tables
- Compare experience to AI-derived industry benchmarks
```

### 4.3 CAT Accumulation Tracking

```
CAT Accumulation Monitoring:

Input: All in-force locations with TIV, construction, occupancy
Process:
  1. Geocode all locations (lat/long)
  2. Map to CAT zones (hurricane, earthquake, flood, wildfire, tornado)
  3. Calculate gross PML by zone and peril (return periods: 100yr, 250yr, 500yr)
  4. Apply policy terms (deductibles, sub-limits, coverage triggers)
  5. Net down for reinsurance (treaty, facultative)
  6. Monitor against capacity limits and risk tolerance
  7. Alert when new submission pushes accumulation beyond threshold

Real-Time Monitoring:
  - Every new policy/endorsement triggers accumulation recalculation
  - Dashboard shows heat map of exposure by geography and peril
  - Pre-bind check: "If we write this account, what's the impact on our FL wind PML?"
  - Event response: "A CAT 4 hurricane is approaching FL — show all exposed accounts
    with estimated gross and net loss by return period"

Integration: RMS RiskLink API, AIR Touchstone API, or CoreLogic for model-based PML
Alternative: Simplified accumulation using Aiden AI's geospatial agent with TIV-based
estimation for clients without CAT model licenses
```

### 4.4 SOV (Schedule of Values) Extraction Pipeline

```
SOV Processing Pipeline:

1. Document Classification
   - Detect SOV vs. other documents (AI classifier, 95%+ accuracy)
   - Identify format: Excel (multi-sheet), PDF (table-based), CSV

2. Structure Detection
   - Identify header row(s) — often non-standard, merged cells, multi-row headers
   - Map columns to standard fields: Location #, Address, City, State, ZIP,
     Construction, Occupancy, Year Built, # Stories, Square Footage,
     Building Value, Contents Value, BI Value, Total Insured Value (TIV)

3. Data Extraction
   - Parse cell values with type inference (currency, integer, date, text)
   - Handle merged cells, hidden columns, formula-dependent cells
   - Extract across multiple sheets (some SOVs split by state/division)

4. Normalization
   - Standardize addresses (geocode, validate, normalize)
   - Map construction codes (ISO, carrier-specific → standard)
   - Map occupancy codes to industry classification
   - Convert currencies, resolve units

5. Validation
   - TIV = Building + Contents + BI (flag mismatches)
   - Address geocoding validation
   - Duplicate location detection
   - Completeness check (required fields populated)
   - Outlier detection (unusual TIV for building type)

6. Output
   - Structured JSON/DB records per location
   - Confidence score per field
   - Validation exceptions for UW review
   - CAT-ready format for model import

Complexity: SOVs are the single hardest document to extract in insurance.
A large account may have 500–5,000 locations across 50 Excel tabs.
Budget training time and expect iterative accuracy improvement.
```

---

## Appendix A: Glossary of Insurance Underwriting Terms

| Term | Definition |
|------|-----------|
| **GWP** | Gross Written Premium — total premium written before reinsurance |
| **NWP** | Net Written Premium — GWP minus ceded reinsurance premium |
| **NEP** | Net Earned Premium — portion of NWP earned in the period |
| **Loss Ratio** | Incurred losses / earned premium |
| **Combined Ratio** | Loss ratio + expense ratio (< 100% = underwriting profit) |
| **IBNR** | Incurred But Not Reported — reserve for unknown claims |
| **LDF** | Loss Development Factor — multiplier to develop immature losses to ultimate |
| **PML** | Probable Maximum Loss — estimated maximum loss from a single event |
| **AAL** | Average Annual Loss — expected loss per year from catastrophe models |
| **TIV** | Total Insured Value — sum of building + contents + business interruption values |
| **COPE** | Construction, Occupancy, Protection, Exposure — property risk factors |
| **SOV** | Schedule of Values — list of insured locations with values |
| **ILF** | Increased Limits Factor — multiplier for excess layer pricing |
| **Ex Mod** | Experience Modification Factor — adjusts premium based on loss history |
| **ACORD** | Association for Cooperative Operations Research and Development — data standards |
| **STP** | Straight-Through Processing — full automation without human intervention |
| **NIGO** | Not In Good Order — submission/document with errors or missing data |
| **Binder** | Temporary evidence of insurance before policy issuance |
| **Bordereaux** | Detailed listing of premiums and/or claims reported to reinsurer |
| **Subjectivity** | Condition that must be met for coverage to remain in force |
| **Manuscript** | Custom policy language drafted for a specific risk |
| **Surplus Lines (E&S)** | Excess & Surplus — non-admitted market for risks standard market won't write |
| **Facultative** | Case-by-case reinsurance for individual risks |
| **Treaty** | Automatic reinsurance covering a defined book of business |
| **Retention** | Amount of risk/loss retained by the insurer before reinsurance |
| **Cession** | Portion of risk/premium transferred to reinsurer |
| **MGA/MGU** | Managing General Agent/Underwriter — delegated underwriting authority |
| **Coverholder** | Lloyd's term for entity with delegated binding authority |
| **ORSA** | Own Risk and Solvency Assessment — enterprise risk management requirement |
| **RBC** | Risk-Based Capital — regulatory minimum capital requirement |

## Appendix B: ACORD Form Reference

| Form | Name | Use |
|------|------|-----|
| **ACORD 125** | Commercial Insurance Application | Base application for all commercial lines |
| **ACORD 126** | Commercial General Liability Section | GL-specific supplement |
| **ACORD 127** | Commercial Business Auto Section | Auto-specific supplement |
| **ACORD 130** | Workers Compensation Application | WC-specific application |
| **ACORD 140** | Property Section | Property-specific supplement |
| **ACORD 131** | Umbrella/Excess Section | Umbrella supplement |
| **ACORD 133** | Contractors Supplement | Construction-specific |
| **ACORD 137** | Inland Marine Section | Inland marine supplement |
| **ACORD 160** | Professional Liability Application | E&O/PL application |
| **ACORD 25** | Certificate of Insurance | Evidence of coverage |
| **ACORD 35** | Cancellation Request | Policy cancellation |
| **ACORD 75** | Insurance Binder | Temporary evidence of insurance |
