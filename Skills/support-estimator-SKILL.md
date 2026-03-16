---
name: support-estimator
description: >-
  IT Application Support estimation and pricing model. Calculates staffing,
  effort, and pricing for 24x7, 16x5, or 8x5 support models with on-call
  coverage for P1/P2, weekends, and holidays. Use when an RFP includes
  application support, managed services, or production support requirements.
license: "Internal use"
---

# IT Application Support Estimator

This skill generates a comprehensive support estimation and pricing model as an Excel workbook. It supports multiple coverage models (24x7, 16x5, 8x5) with configurable on-call arrangements.

---

## Part 1: Inputs Required

Before estimating, gather the following from the RFP or ask the user:

| Input | Description | Default |
|-------|-------------|---------|
| **Coverage Model** | 24x7 / 16x5 / 8x5 | 8x5 |
| **Number of Applications** | Total apps in support scope | — |
| **Application Names** | List each application by name | — |
| **Number of Users** | Users per year (Y1-Y5) | — |
| **Avg Tickets per User/Year** | Expected ticket volume driver | 5 |
| **Ticket Growth %** | Year-over-year growth in users/tickets | 20% |
| **L1 Ownership** | Client-owned or Aiden-owned | Client-owned |
| **On-Call Required** | P1/P2 after-hours, weekends, holidays | Yes |
| **Contract Duration** | 1-5 years | 3 years |
| **Location** | Onshore / Offshore / Blended | Offshore |
| **Efficiency Factor** | YoY improvement from automation/knowledge | 10% per year |

---

## Part 2: Support Level Definitions

| Level | Description | Avg Hours/Ticket | % of Total Tickets |
|-------|-------------|-----------------|-------------------|
| **L1** | Password resets, basic queries, ticket logging | 0 (if client-owned) | 50% |
| **L2** | Configuration issues, known error fixes, minor changes | 6 hrs | 30% |
| **L3 Simple** | Bug fixes, simple enhancements, data fixes | 10 hrs | 5% |
| **L3 Medium** | Feature changes, integration fixes, performance tuning | 16 hrs | 10% |
| **L3 Complex** | Architecture changes, major bug fixes, security patches | 24 hrs | 5% |

**Additional effort categories**:
- **Monitoring, issues, others**: 10% of L2+L3 effort
- **L4 support (escalation/vendor mgmt)**: 10% of L2+L3 effort
- **Management cover (support lead)**: 25% of total L2+L3+others effort
- **On-call load (P1/P2)**: ~10% additional for after-hours/weekend coverage
- **Config management**: 0.3-0.4 FTE for middleware/platform config (InsureMO, Unqork, etc.)

---

## Part 3: Coverage Models

### Model A: 8x5 (Business Hours)
- **Hours**: 9 AM – 5 PM, Monday–Friday
- **Shifts**: 1 shift
- **Staff per shift**: Based on ticket volume
- **On-call**: P1/P2 only — 1 person on-call after hours and weekends (rotating)
- **Holiday coverage**: On-call only

### Model B: 16x5
- **Hours**: 7 AM – 11 PM, Monday–Friday (2 shifts)
- **Shift A**: 7 AM – 3 PM (9 hrs)
- **Shift B**: 3 PM – 11 PM (8 hrs)
- **Staff per shift**: Based on ticket volume split
- **On-call**: P1/P2 for 11 PM – 7 AM + weekends
- **Holiday coverage**: On-call only

### Model C: 24x7
- **Hours**: Round the clock, 7 days
- **Shift A**: 7 AM – 3 PM
- **Shift B**: 3 PM – 11 PM
- **Shift C**: 11 PM – 7 AM (night)
- **Weekend**: Rotating coverage — 1 person on weekend duty every 2 months
- **Night shift**: 1 person on night duty for 1 week every 2 months (rotating)
- **Holiday coverage**: Full coverage with holiday premium

### Roster Rules
- Support resources work Mon-Fri on regular shifts
- Night shift (Shift C) and weekend duty are **on-call** (not active shift) unless 24x7 active coverage is required
- Manager covers 0.5 FTE across all shifts
- 1 person per 2 months rotates into night on-call
- 1 person per 2 months rotates into weekend on-call

---

## Part 4: Staffing Calculation

### Step 1: Calculate Total Tickets by Category
```
Total Tickets = Number of Users × Avg Tickets per User
L1 Tickets = Total × 50%
L2 Tickets = Total × 30%
L3 Simple = Total × 5%
L3 Medium = Total × 10%
L3 Complex = Total × 5%
```

### Step 2: Calculate Total Effort (Hours)
```
L1 Effort = L1 Tickets × 0 hrs (if client-owned)
L2 Effort = L2 Tickets × 6 hrs
L3 Simple Effort = L3 Simple × 10 hrs
L3 Medium Effort = L3 Medium × 16 hrs
L3 Complex Effort = L3 Complex × 24 hrs
Monitoring/Others = (L2 + L3 total) × 10%
L4 Support = (L2 + L3 total) × 10%
Management = (L2 + L3 + Monitoring + L4) × 25%
```

### Step 3: Calculate FTEs
```
Available hours per FTE per year = 1800 hrs
Raw FTE = Total Effort / 1800

Apply efficiency factor:
Y1: Raw FTE (no efficiency — ramp-up year)
Y2: Raw FTE × 0.90 (10% efficiency)
Y3: Raw FTE × 0.80 (20% cumulative)
Y4: Raw FTE × 0.70 (30% cumulative — capped)
Y5: Raw FTE × 0.70 (maintained)
```

### Step 4: Determine Client-Facing Team Size
Round FTEs to nearest whole number for client-facing staffing:

| Role | Coverage | Rate ($/hr) |
|------|----------|------------|
| Support Engineer (L2/L3) | Per shift requirement | $30 offshore / $85 onshore |
| Manager / Support Lead | 0.5-1 FTE | $35 offshore / $95 onshore |

### Step 5: Add On-Call Premium
```
On-call load = ~10% of base effort
For 24x7: Add night shift and weekend rotation
For 16x5: Add after-hours on-call
For 8x5: Add P1/P2 on-call only
```

---

## Part 5: Pricing Calculation

### Monthly Price per Resource
```
Monthly Rate = Hourly Rate × 160 hrs (standard month)
Annual Rate = Monthly Rate × 12

Support Engineer: $30/hr × 160 = $4,800/month = $57,600/year (offshore)
Manager: $35/hr × 160 = $5,600/month = $67,200/year (offshore)
```

### Total Annual Price
```
Annual Price = Σ (FTEs per role × Annual Rate per role)
```

### Multi-Year Pricing
Apply rate escalation if applicable:
- Y1: Base rate
- Y2: Base rate (or +3% if contractual)
- Y3-Y5: Base rate (or +3% annual escalation)

---

## Part 6: Excel Output Specification

Generate using `openpyxl`. The workbook MUST contain these sheets:

### Sheet 1: Support Summary
| Field | Value |
|-------|-------|
| Client | [Name] |
| Coverage Model | [24x7 / 16x5 / 8x5] |
| Applications in Scope | [Count + Names] |
| Contract Duration | [X years] |
| L1 Ownership | [Client / Aiden] |
| Total Y1 Price | [$X] |
| Total Contract Value | [$X] |

### Sheet 2: Ticket Volume & Effort
- Ticket volume by category (L1-L3) for each year
- Effort hours by category for each year
- FTE calculation with efficiency factor
- Per-application breakdown if multiple apps

### Sheet 3: Staffing Plan
- Roles and headcount by year
- Shift roster (if 16x5 or 24x7)
- On-call rotation schedule
- Ramp-up plan (Y1 typically lower headcount)

### Sheet 4: Pricing
- Annual cost by role
- Total annual price for each year
- Total contract value
- Payment terms

### Sheet 5: Assumptions
- All assumptions listed
- SLA targets (P1: 1hr response, P2: 4hr, P3: 8hr, P4: next business day)
- Exclusions (L1 if client-owned, infrastructure, licensing)

### Sheet 6: Scenarios (INTERNAL)
- Standard pricing
- Competitive pricing (10% discount)
- Strategic pricing (15-20% discount)
- Margin analysis per scenario

---

## Part 7: SLA Framework (Standard)

| Priority | Response Time | Resolution Time | Availability |
|----------|--------------|----------------|-------------|
| P1 (Critical) | 15 min (24x7) / 30 min (8x5) | 4 hrs | 99.9% |
| P2 (High) | 1 hr | 8 hrs | 99.5% |
| P3 (Medium) | 4 hrs | 2 business days | 99.0% |
| P4 (Low) | 8 hrs | 5 business days | — |

---

## Part 8: When to Use This Skill

Trigger this skill when the RFP mentions ANY of:
- Application support / production support / managed services
- L1/L2/L3 support tiers
- 24x7 / 16x5 / 8x5 coverage
- SLA requirements for response/resolution times
- Helpdesk / service desk requirements
- Hypercare / warranty support (post go-live)
- Application maintenance and support (AMS)
- Incident management / problem management

When triggered, generate the support estimate as a **separate Excel file**: `<client>_Support_Estimate.xlsx`

If the RFP includes BOTH project delivery AND support, generate:
1. `<client>_Pricing.xlsx` — Project delivery pricing (from pricing-calculator skill)
2. `<client>_Support_Estimate.xlsx` — Support pricing (from this skill)
3. Combine totals in a summary view within each file
