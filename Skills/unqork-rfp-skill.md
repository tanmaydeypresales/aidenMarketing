---
name: unqork-rfp
description: >-
  Use this skill whenever the user is writing, reviewing, or improving an RFP
  response that involves Unqork as the proposed platform. Triggers include any
  mention of Unqork, no-code enterprise platform, codeless architecture, or
  when an RFP response needs Unqork-specific solution design, architecture
  patterns, honest limitation handling, AI integration strategy, or pricing
  guidance. Combine with the base rfp-response skill for full proposal
  generation. Use this skill BEFORE writing any Unqork solution architecture,
  module design, or technical narrative.
license: "Internal use"
---

# Unqork RFP Response Skill

This skill provides deep, practitioner-level guidance for crafting **winning RFP responses where Unqork is the proposed platform**. It covers Unqork's architecture, strengths, known limitations with honest mitigation strategies, solution design best practices, AI integration patterns, and pricing considerations.

> **Always combine this skill with the base `rfp-response` SKILL.md** for overall proposal structure, section templates, and pricing format. This skill extends and overrides the base skill specifically for Unqork engagements.

---

## Part 1: Unqork Platform — What You Must Know Before Writing

### 1.1 Platform Architecture Overview

Unqork is a **codeless-as-a-service (CaaS) enterprise platform** built on a data-driven architecture that completely separates application logic from underlying code. All application logic is stored as configuration (JSON), not compiled code — making upgrades, maintenance, and portability fundamentally different from traditional or low-code platforms.

**Key architectural facts to cite in proposals:**

- **Single-tenant by default**: Every Unqork customer gets a dedicated, isolated instance. Only the client's products, rules, and data live inside their instance. This is a major differentiator vs. multi-tenant SaaS platforms — critical for regulated industries.
- **Cloud infrastructure**: Runs on AWS or Microsoft Azure using native PaaS offerings. Kubernetes orchestrates the application layer; MongoDB Atlas is the document database layer.
- **Elastic and horizontally scalable**: Kubernetes-based scaling with 99.9% uptime SLA. The platform claims 600x fewer defects than code/low-code approaches.
- **No infrastructure cost in proposals**: Because Unqork is a fully managed PaaS, **do NOT add separate infrastructure line items**. Infrastructure is included in the Unqork license. This is a common mistake in proposals — call it out as a total cost of ownership (TCO) advantage.
- **Zero code = zero tech debt**: Unlike low-code platforms that generate code underneath, Unqork never generates code. All configurations are managed and upgraded by Unqork centrally — the client never inherits legacy code.

### 1.2 Certifications and Compliance (Always Reference in Regulated Industry RFPs)

- **SOC 2 Type II** — annual examination, AICPA standards
- **ISO/IEC 27001:2013** — information security management
- **FedRAMP** — U.S. federal government readiness
- **GDPR** — Unqork processes client data as Data Processor
- **Defense-in-depth security**: WAF, ACLs, IDS/IPS, continuous monitoring, threat detection
- **RBAC at every level**: environment, module, component, field, document level
- **Separate non-production environments** in a VPC isolated from production
- **PII detection**: Automatic detection of PII fields in schema to ensure proper security controls

### 1.3 Core Platform Strengths (Lean Into These in Proposals)

| Strength | What to Say in the RFP |
|----------|----------------------|
| **Rapid UI development** | Complex, enterprise-grade user interfaces built in days, not months. Drag-and-drop component library with dynamic refresh, conditional logic, and RBAC-controlled views. |
| **Visual workflow engine** | 100% visual workflow designer for complex orchestration, routing, rules, and dynamic flows — no BPM coding required. Supports swimlanes, RBAC-based task assignment, and automated workflows. |
| **Rules engine** | Sophisticated business rules configured visually — field-level conditions, cross-module validation, multi-step decision trees, and data-driven logic. |
| **Integration breadth** | 700–800+ pre-built connectors via Integration Gateway. Supports REST, SOAP, GraphQL, legacy file formats, and modern APIs. Visual drag-and-drop integration mapping. |
| **Single-tenant isolation** | Data never co-mingled with other clients. Ideal for financial services, insurance, healthcare, and government. |
| **Composability** | Build once, reuse everywhere. Module reuse across applications drives exponential productivity gains on multi-app programs. |
| **Lifecycle management** | Built-in release management: Dev → UAT → Staging → Production promotion with RBAC-controlled approvals. |
| **Application Performance Monitoring** | Native APM within UDesigner — trace and span telemetry across modules, workflows, and components in near real-time. |
| **Open architecture** | First enterprise platform to open-source its specification. Reduces vendor lock-in concern; customers own their configurations. |
| **Vega runtime** | New high-performance runtime for composability, Embedded UI, and Tables/Operations Builder — addresses historical performance concerns. |

---

## Part 2: Unqork Known Limitations — Handling Them Honestly in RFPs

> **CRITICAL PRINCIPLE**: The best Unqork RFP responses do NOT hide weaknesses. Evaluators are sophisticated. A response that acknowledges limitations and provides credible mitigations scores higher on trust and credibility than one that over-promises. For each limitation below, the skill provides the **honest framing** and the **mitigation strategy** to include.

### 2.1 MongoDB Backend — Reporting and Analytics Challenges

**The honest issue**: Unqork's underlying data store is MongoDB Atlas, a document-oriented NoSQL database. This creates real friction for:
- Traditional SQL-based reporting and BI tools
- Complex relational joins across large datasets
- Enterprise data warehouse integration
- Regulatory reporting that requires structured, tabular data

**What NOT to do**: Do not claim Unqork is a reporting platform or that MongoDB handles complex analytics natively without qualification.

**What TO say in the proposal**:

> "Unqork's MongoDB Atlas backend is optimized for operational, transactional data and application state — not analytics. For enterprise reporting, we recommend a **data extraction and replication strategy** that moves data to an analytics-optimized store. Specifically, our solution will include:
> - A **read replica / data pipeline** (e.g., MongoDB BI Connector, Fivetran, or custom ETL) that exports Unqork data to a SQL-based analytical layer such as Snowflake, Azure Synapse, Amazon Redshift, or PostgreSQL.
> - A **reporting layer** (Power BI, Tableau, Looker) sitting atop the analytical store for dashboards, regulatory reports, and ad-hoc queries.
> - For operational reporting within Unqork, use **Vega runtime's Tables and Operations Builder** for in-application summaries and views.
> This architecture is a best practice for all Unqork engagements and is included in our scope and estimate."

**Architecture pattern to reference**:
```
Unqork (MongoDB Atlas) → MongoDB BI Connector / ETL Pipeline → 
Data Warehouse (Snowflake / Redshift / Synapse) → 
BI Layer (Power BI / Tableau) → Reporting & Analytics
```

### 2.2 Native AI Connectors — Limited Out-of-the-Box

**The honest issue**: Unqork does not have deep, native AI/ML model hosting or a built-in LLM framework. The GenAI Connector (launched mid-2024) provides initial support for OpenAI and Google AI but is not a comprehensive AI platform. AI use cases requiring custom model training, MLOps, vector databases, or fine-tuned LLMs are outside Unqork's native capability.

**What TO say in the proposal**:

> "Unqork is not an AI model platform — it is an application platform that integrates AI models. Our architecture treats Unqork as the **application and workflow orchestration layer** while AI capabilities are delivered by best-of-breed AI services:
> - **GenAI Connector** (GA June 2024): Native integration with OpenAI and Google AI for prompt-driven features directly configurable within Unqork modules.
> - **API-based AI integration**: For AWS Bedrock, Azure OpenAI, Anthropic Claude, Google Vertex AI, and custom ML endpoints — all accessible via Unqork's Integration Gateway using REST connectors. No code required.
> - **Intelligent Document Processing (IDP)**: Integrate third-party IDP services (AWS Textract, Azure Form Recognizer, Google Document AI) via API connectors.
> - **AI governance**: Because Unqork never generates code, AI-augmented applications maintain the same zero-code governance model — all AI integration points are configuration, not code, and are fully auditable.
> 
> This approach gives clients access to the best AI providers in the market, with the flexibility to switch providers without rearchitecting the application."

### 2.3 Performance Under High Concurrent Load / Large Data Sets

**The honest issue**: Unqork performance can degrade when:
- Modules load very large datasets into the browser
- Complex multi-level workflow logic is chained without optimization
- Many simultaneous users trigger heavy server-side execution
- Page rendering involves too many components without lazy loading

**What TO say in the proposal**:

> "Unqork performance is a design consideration, not a platform constraint. Our solution architecture will follow these best practices:
> - **Lazy loading and pagination**: Avoid loading large datasets into a single view; use server-side pagination for all list/grid components.
> - **Server-Side Execution Only (SSE)**: All sensitive and heavy processing modules will be configured for SSE, reducing client-side load and improving security.
> - **Proxy module pattern**: Implement proxy modules to validate, filter, and transform data server-side before sending responses to the browser.
> - **Data filter discipline**: Apply filters before returning data to the client to minimize payload size.
> - **Vega runtime**: All new modules will be built on Vega, Unqork's high-performance runtime, which has materially improved rendering speed and composability.
> - **APM monitoring**: Native Application Performance Monitoring will be configured from Day 1 to detect and resolve bottlenecks before they reach production.
> - **Load testing**: A dedicated performance testing phase is included in our delivery plan to validate performance against agreed SLAs before go-live."

### 2.4 Limited External Documentation and Niche Talent Pool

**The honest issue**: Unqork's documentation is primarily on a closed internal portal (docs.unqork.io). External developer community resources (Stack Overflow, YouTube, GitHub) are sparse compared to platforms like Salesforce or ServiceNow. Certified Unqork practitioners are a smaller talent pool, making staffing a legitimate risk.

**What TO say in the proposal**:

> "We acknowledge that Unqork is a specialist platform with a defined practitioner community. Our team mitigates this in three ways:
> 1. **Certified Unqork Creators**: Our team includes [X] Unqork-certified developers trained through Unqork Academy and live project experience.
> 2. **Accelerator library**: We maintain a proprietary library of reusable Unqork modules, integration templates, and tested patterns that reduce build time and dependency on scarce talent.
> 3. **Knowledge transfer**: Our delivery model includes structured knowledge transfer to client teams, with documentation of all module configurations and Unqork Creator training as a deliverable."

### 2.5 Vendor Dependency / Platform Lock-In

**The honest issue**: Because all application logic lives inside the Unqork platform as JSON configurations, migrating to another platform requires rebuilding the application. However, Unqork has addressed this with its open-source specification.

**What TO say in the proposal**:

> "Unqork has taken a deliberate stance against proprietary lock-in by becoming the **first enterprise no-code platform to open-source its specification**. This means:
> - Customers have full access and ownership of their application specifications
> - Third parties can build tools that interact with Unqork's platform
> - Application configurations can be exported and are not held in a black box
> 
> That said, this is a platform commitment, and clients should plan for Unqork as a long-term strategic platform investment — not a short-term tool. Our proposal includes a **platform governance model** to ensure the client's Unqork investment compounds in value over time."

---

## Part 3: Unqork Solution Architecture Best Practices

### 3.1 Module Design Principles

When describing the solution architecture in Section 6 of the proposal, always reference these Unqork-specific design patterns:

**Core design rules:**
1. **Separation of concerns**: UI modules, workflow modules, integration modules, and schema modules are built separately and composed together. Never mix UI logic with integration logic in the same module.
2. **Reusable module library**: Common functions (validation, lookups, notifications) are built as standalone reusable modules, not duplicated across the application.
3. **RBAC-first design**: Role-based access is designed upfront for every module, swimlane, and field. RBAC cannot be retrofitted effectively.
4. **Server-Side Execution for sensitive operations**: All external API calls, data writes, and PII access must run server-side only. Enforce via SSE module settings.
5. **Schema discipline**: Define data schemas (O modules) before building UI. Schema defines persistence, field types, and per-role security in one place.
6. **Proxy pattern for API security**: External-facing API endpoints use a proxy module layer to validate, sanitize, and authorize before executing backend logic.
7. **Avoid anonymous module access**: Limit modules with anonymous user access to login pages and public landing pages only.

### 3.2 Standard Unqork Application Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│  Express View Modules (UI) — Vega Runtime — RBAC-Controlled  │
├─────────────────────────────────────────────────────────────┤
│                     WORKFLOW LAYER                           │
│  Automated Workflows — Swimlanes — Rules Engine              │
├─────────────────────────────────────────────────────────────┤
│                   INTEGRATION LAYER                          │
│  Integration Gateway — API Plugins — Legacy Connectors       │
├─────────────────────────────────────────────────────────────┤
│                      DATA LAYER                              │
│  Schema Modules — MongoDB Atlas — Data Collections           │
├─────────────────────────────────────────────────────────────┤
│                  REPORTING LAYER (External)                  │
│  ETL / BI Connector → Data Warehouse → BI Tool               │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 AI Integration Architecture Pattern

```
┌──────────────────────────────────────────────────────────────┐
│                    UNQORK APPLICATION                         │
│                                                              │
│  [User Interface] → [Workflow Orchestration]                 │
│         ↓                    ↓                               │
│  [GenAI Connector]    [Integration Gateway]                  │
│         ↓                    ↓                               │
│  [OpenAI / Google AI] [AWS Bedrock / Azure OpenAI]           │
│                              ↓                               │
│              [AI Response Processing Module]                  │
│                              ↓                               │
│              [Audit Log + Governance Module]                  │
└──────────────────────────────────────────────────────────────┘
```

> Always include an AI governance layer — logging all AI calls, inputs, and outputs — as a separate auditable module. This is critical for regulated industries.

### 3.4 Reporting Architecture Pattern (Mandatory for Regulated Industries)

```
┌─────────────────────────────────────────────────────────────┐
│   UNQORK OPERATIONAL DATA (MongoDB Atlas)                    │
│         ↓  (MongoDB BI Connector / Fivetran / API ETL)       │
│   DATA WAREHOUSE LAYER                                       │
│   (Snowflake / Azure Synapse / Amazon Redshift / BigQuery)   │
│         ↓                                                    │
│   BI AND REPORTING LAYER                                     │
│   (Power BI / Tableau / Looker / MicroStrategy)              │
│         ↓                                                    │
│   REGULATORY REPORTING / DASHBOARDS                          │
└─────────────────────────────────────────────────────────────┘
```

**Include this pattern in every proposal involving regulatory reporting, management dashboards, or data analytics.** Do not rely on Unqork's native dashboards for enterprise analytics.

---

## Part 4: Industry-Specific Positioning

### 4.1 Financial Services

**Strongest use cases:**
- Client onboarding and KYC/AML workflows
- Loan origination and servicing portals
- Wealth management advisor portals
- Trade lifecycle management
- NAV oversight and operations

**Key proof points to reference:**
- Goldman Sachs, BlackRock, Marsh are Unqork customers
- Single-tenant architecture meets most data residency requirements
- RBAC controls support maker-checker and 4-eyes approval workflows
- Full ACID transaction support via MongoDB Atlas

**Compliance to lead with**: SOC 2 Type II, ISO 27001, GDPR

### 4.2 Insurance

**Strongest use cases:**
- New business and policy administration portals
- Claims management and adjudication workflows
- Underwriting workbenches
- Broker portals and agent onboarding
- RFQ/RFP processing automation

**Key differentiation**: Unqork can store and process the highest levels of PII (including medical conditions in insurance applications) and has been approved by large insurers for PII data storage within the platform.

**Compliance to lead with**: SOC 2 Type II, ISO 27001, HIPAA-readiness

### 4.3 Government

**Strongest use cases:**
- Benefits administration and case management
- License and permit applications
- Grant management portals
- Constituent services and digital portals

**Key compliance**: FedRAMP authorization, single-tenant government instances

---

## Part 5: Unqork-Specific Sections to Add or Modify in the Base RFP Proposal

### 5.1 Infrastructure Section — OMIT, Replace with TCO Statement

**Do NOT include an infrastructure section in Unqork proposals.**

Instead, include this statement in the Executive Summary and pricing section:

> "Because Unqork is a fully managed, single-tenant PaaS solution, infrastructure costs — including compute, storage, networking, security monitoring, platform maintenance, and upgrades — are included in the Unqork license. There are no separate cloud infrastructure procurement, sizing, or management costs for the client. This represents a significant TCO advantage compared to self-managed or hybrid solutions."

### 5.2 Platform Roles Section (Add to Staffing Plan)

Unqork engagements require specific roles beyond standard project staffing. Add these to Section 16.2:

| Role | Responsibility | Notes |
|------|---------------|-------|
| **Unqork Solution Architect** | Overall platform design, module architecture, integration patterns, performance strategy | Must be Unqork-certified; senior-only |
| **Unqork Creator (Senior)** | Complex module development, workflow design, integration configuration | Certified; 2+ years Unqork experience |
| **Unqork Creator (Mid)** | UI module development, data schema design, testing | Certified; 1+ year Unqork experience |
| **Unqork Security Engineer** | RBAC design, SSE configuration, threat modeling, compliance alignment | Specialized role; critical for regulated industries |
| **Data/Integration Architect** | Reporting pipeline design, ETL strategy, BI layer architecture | Bridges Unqork and analytics ecosystem |

### 5.3 Risks Section — Unqork-Specific Risks to Add

Add these risks to Section 14 (in addition to standard risks from base skill):

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| U1 | Reporting requirements exceed Unqork native capability | High | High | Implement external data pipeline to analytics layer in Phase 1 |
| U2 | Performance degradation under peak load | Medium | High | Performance-first design patterns + load testing sprint before go-live |
| U3 | AI integration requires provider not yet in GenAI Connector | Medium | Medium | Use Integration Gateway REST connector as fallback; all major providers supported |
| U4 | Client team has no prior Unqork experience | High | Medium | Include Unqork Academy training in scope; schedule shadowing sessions during build |
| U5 | Platform upgrade disrupts in-flight development | Low | Medium | Coordinate upgrade windows with Unqork; use non-production environments for testing |
| U6 | MongoDB limitations create regulatory reporting gaps | High | High | Implement dedicated reporting architecture with ETL pipeline in scope |

### 5.4 Assumptions Section — Unqork-Specific Assumptions to Add

Add these to Section 15:

1. The Unqork license has been, or will be, procured by the client prior to the start of Phase 1 development.
2. Unqork's non-production environments (Dev, UAT, Staging) are provisioned and accessible within [X] business days of contract signing.
3. The client's enterprise reporting requirements will be addressed via an external analytics layer (included in scope). Unqork's native MongoDB store will not be used as the primary analytical data source.
4. Any AI/ML capabilities will use API-based integration to external providers (OpenAI, AWS Bedrock, Azure OpenAI, etc.) via Unqork's Integration Gateway, not natively hosted models.
5. The client will provide a dedicated Unqork platform administrator who will be trained and responsible for user provisioning, RBAC management, and environment promotion approvals.

---

## Part 6: Competitive Differentiation — Unqork vs. Alternatives

If the RFP is competitive (Unqork vs. Pega, Appian, Salesforce, ServiceNow, OutSystems), use this positioning:

| Dimension | Unqork Advantage |
|-----------|-----------------|
| **vs. Pega / Appian** | True no-code (zero code generated); single-tenant by default; no BPM licensing complexity |
| **vs. Salesforce** | Not limited to Salesforce data model; more flexible UI; better suited for complex transactional workflows outside CRM |
| **vs. ServiceNow** | Not IT-ops centric; purpose-built for financial services/insurance front-office; better UI flexibility |
| **vs. OutSystems / Mendix** | OutSystems and Mendix generate code and accumulate tech debt; Unqork never generates code |
| **vs. Custom development** | 4x faster build speed; 10x more secure (shared security model); zero ongoing infrastructure management; no tech debt |

---

## Part 7: Win Themes Specific to Unqork Proposals

Use these win themes as narrative anchors throughout the proposal:

1. **"Speed without debt"**: Unqork delivers faster than traditional development without creating technical debt that slows future innovation.

2. **"Regulated-industry ready from Day 1"**: Single-tenant architecture, SOC 2 Type II, ISO 27001, and FedRAMP mean the security and compliance framework is already built. The client inherits it.

3. **"Total cost of ownership, not just day-one cost"**: Infrastructure, maintenance, security patches, and platform upgrades are included in the license. There is no hidden ongoing cost of ownership.

4. **"AI without the liability"**: Because Unqork never generates code, AI-assisted development within Unqork maintains full governance, auditability, and compliance. There is no risk of AI-generated code accumulating as unreviewed tech debt.

5. **"Composable, not monolithic"**: Every component built in Unqork is reusable across applications. A multi-app program compounds in value — each new app is faster to build than the last.

---

## Part 8: Quality Checklist — Unqork-Specific Checks

Before submitting any Unqork RFP response, verify:

- [ ] **No infrastructure line items** — infrastructure included in Unqork license
- [ ] **Reporting architecture explicitly addressed** — MongoDB limitations acknowledged; data pipeline and BI layer in scope
- [ ] **AI integration strategy is honest** — positions Unqork as orchestrator, not AI platform; names specific AI provider APIs
- [ ] **Performance design patterns referenced** — SSE, proxy pattern, pagination, Vega runtime mentioned
- [ ] **Single-tenant security** called out as a competitive differentiator
- [ ] **Unqork-specific roles** included in staffing plan (Solution Architect, Creator, Security Engineer, Data Architect)
- [ ] **Unqork-specific risks** in the risk register with honest mitigation strategies
- [ ] **Unqork-specific assumptions** listed (license procurement, non-prod envs, admin role)
- [ ] **Knowledge transfer** included as a deliverable (client team Unqork training)
- [ ] **Compliance certifications** cited: SOC 2 Type II, ISO 27001, FedRAMP (if gov), GDPR
- [ ] No claim that Unqork natively handles complex relational analytics without an external data layer
- [ ] GenAI Connector limitation acknowledged if AI is in scope; REST-based API fallback documented

---

## Part 9: Unqork Glossary (Reference When Writing Technical Sections)

| Term | Definition |
|------|-----------|
| **Creator** | Unqork's term for a developer/configurator who builds on the platform |
| **Module** | The basic building block of an Unqork application (equivalent to a screen or service) |
| **Express View** | The front-end rendering engine that displays Unqork modules to end users |
| **Vega** | Unqork's new high-performance runtime (as of 2023–2024); prefer over legacy runtime for all new builds |
| **UDesigner** | Unqork's next-generation IDE for collaborative application development (GA 2023) |
| **Integration Gateway** | Unqork's central integration hub connecting 700+ external systems |
| **GenAI Connector** | Unqork's native AI integration feature supporting OpenAI and Google AI (GA June 2024) |
| **SSE** | Server-Side Execution Only — module setting that prevents sensitive logic from running in the browser |
| **RBAC** | Role-Based Access Control — controls access at environment, module, component, and field level |
| **Swimlane** | A workflow lane assigned to a specific role or automated process within Unqork's workflow designer |
| **Schema Module (O Module)** | Defines data structures, field types, persistence settings, and security for a data entity |
| **Data Collection** | Static reference data tables (like lookup lists) used across modules |
| **Workspace** | Organizational container within Unqork for grouping related applications and modules |
| **Submission** | A data record created and stored by an Unqork module (analogous to a database row) |
| **Plugin** | A pre-built integration component (connector) for a specific external system |
| **Proxy Module** | A security design pattern where a front-facing module delegates to a server-side execution module |
| **CaaS** | Codeless as a Service — Unqork's delivery model |
| **UDLC** | Unqork Development Lifecycle — the platform's application lifecycle management toolkit |

---

> **Final reminder**: A great Unqork RFP response tells a story of *confident expertise with honest pragmatism*. Evaluators have seen over-hyped no-code pitches fail in delivery. The winning response acknowledges what Unqork does not do natively (AI models, relational analytics), demonstrates a credible architecture to address those gaps, and shows deep platform knowledge through specific terminology, design patterns, and role definitions. That combination of honesty and depth is what builds trust and wins bids.
