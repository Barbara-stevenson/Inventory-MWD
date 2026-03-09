# Discovery Call Insights: David Singletary (DJS DIGITAL LLC)

**Date:** January 19, 2026
**Attendees:** John Miranda, David Singletary, Barbara Stevenson, Elaine Chow
**Duration:** ~52 minutes

---

## Executive Summary

This discovery call with David Singletary, an MWD expert with 27+ years of inventory management experience, provided valuable insights into customer pain points, table stakes features, and technical risks. However, **the core order-centric workflow hypothesis was NOT validated** — the examples provided were edge cases (field service, manufacturing) rather than clean wholesale/distribution workflows.

---

## Expert Profile & Credibility

| Attribute | Detail |
|-----------|--------|
| Experience | 27+ years in inventory management (since 1997) |
| Practice | 5 years running DJS DIGITAL LLC |
| Customer Profile | ≤50 users, ≤$50M revenue |
| Implementations | ~450 customers |
| Verticals | Manufacturing & Retail |
| Partner Tools | SOS Inventory, Katana, Inflow, MRP Easy, SIM7 |

**Why this matters:** David is a highly credible source — he's seen hundreds of implementations and knows what works and what doesn't across multiple inventory platforms.

---

## Workflow Validation Assessment

### Status: NOT VALIDATED

The call did **not** validate the order-centric workflow hypothesis (Quote → Order → Ship → Invoice).

### What We Actually Got

**Two customer stories, but neither matched the order-centric hypothesis:**

| Example | What It Actually Was | Fit to Hypothesis |
|---------|---------------------|-------------------|
| Roofing company | Field service / job-centric with mobile trucks | Weak — David himself said "they're unique" |
| Chemical company | Manufacturing with formulas/BOM | Weak — different vertical, different complexity |

David's own words:
> "They do vary a lot."

About the roofing example:
> "I think they're unique because they have the mobile trucks. Most people are not managing inventory in the warehouse and on trucks."

### What We Didn't Get

- No explicit confirmation that Quote → Order → Ship → Invoice is THE workflow for MWD
- No clean wholesale/distribution example (despite that being the stated focus)
- No story from a customer that matches the target persona
- The call shifted to demo mode halfway through — cutting discovery short

### What Was Actually Validated

| Validated | Not Validated |
|-----------|---------------|
| Lack of central inventory system causes friction | The specific order-centric workflow stages |
| Visibility during order entry is critical | How personas move through each stage |
| Paper/spreadsheets are common before intervention | Whether Quote → Order → Ship → Invoice is universal |
| Stock availability check is a critical moment | The handoffs between stages |

---

## Customer Stories (Specific Examples)

### Story 1: Roofing Company

**Context:** Field service company with warehouse + mobile trucks

**Workflow:**
```
Customer needs new roof → Project Manager creates order with materials →
Order placed in Inflow → Warehouse Manager picks (barcode scanner) →
Load truck → Deliver to site → Handle returns/add-ons next day
```

**Unique challenges:**
- Inventory on trucks (not just warehouse)
- Returns handling next day
- Add-ons when more parts needed on-site

**David's assessment:** "I think they're unique because they have the mobile trucks. Most people are not managing inventory in the warehouse and on trucks."

### Story 2: Chemical Company

**Context:** Manufacturing company with formulas/BOM

**Before State:**
- Very old system + paper for everything
- No tracking of ordered, received, or stocked materials
- Single person held all formula knowledge ("If that person got hit by a car, everything's gone")
- Owner had to drive 4 hours to office to see operations

**After State (SOS Inventory + QuickBooks):**
- Orders placed to vendors digitally
- Stock visibility before fulfillment
- All formulas in system
- Paper eliminated
- Owner can monitor remotely

**Key Quote:**
> "They had no idea how much inventory they had at all. They didn't know what their formulas were. They had one person that had all the formulas in their head."

#### Actual Workflow Described (Verbatim from Transcript)

From the transcript (00:12:07):

> "So, now orders are placed to the vendors. Uh well, you know, a customer places an order uh they're they'll able to see if they have stock or they need to create a new formula. If they don't have the proper materials, then they place a purchase order for it. That goes to the vendor uh comes in, they receive it. Uh that invoice for the receipt goes to QuickBooks so that their accountants can then pay it. The materials are received in. They know that they have it. Now they can ship it to the customer."

**Workflow as David Actually Described:**
```
Customer places order → Check stock / need to create formula →
PO to vendor (if materials missing) → Receive materials →
Bill to QuickBooks (to pay vendor) → Ship to customer
```

#### Analysis: What Was Said vs. What Was NOT Said

| Stage | Mentioned by David? | Notes |
|-------|---------------------|-------|
| Quote/Estimate | ❌ No | Not mentioned at all |
| Customer places order | ✅ Yes | Starting point of workflow |
| Check stock | ✅ Yes | "See if they have stock" |
| Create formula | ✅ Yes | Manufacturing-specific step |
| PO to vendor | ✅ Yes | "Place a purchase order for it" |
| Receive materials | ✅ Yes | "They receive it" |
| Bill to QuickBooks | ✅ Yes | "Invoice for the receipt goes to QuickBooks so accountants can pay it" |
| Ship to customer | ✅ Yes | "Now they can ship it to the customer" |
| Sales Invoice to customer | ❌ No | Not mentioned — David stopped at "ship" |
| Payment collection | ❌ No | Not mentioned |

**Important Clarification:** When David said "that invoice for the receipt goes to QuickBooks," he was referring to the **vendor bill** (paying the supplier), NOT a sales invoice to the customer.

#### Why This Matters

This example supports only the **middle portion** of the order-centric hypothesis:

```
Order → Check Stock → (PO if needed) → Receive → Ship
```

It does **NOT** support:
- Quote stage existing
- Sales Invoice as part of the workflow
- Payment collection step

Additionally, this is a **manufacturing** example (formulas/BOM), not wholesale/distribution — the target vertical for the MLP.

---

## Directional Insights for Order-Centric Hypothesis

Even without explicit validation, several signals from David's responses directionally inform the order-centric hypothesis.

### What the Call Directionally Supports

| Hypothesis Element | Signal from David | Strength |
|--------------------|-------------------|----------|
| Order is the anchor stage | "If they're placing orders, they need to know if they have stock" | Strong |
| Order → Ship sequence exists | Chemical company: order → receive → ship | Moderate |
| Stock visibility at Order is critical | Explicitly called out as table stakes | Strong |
| PO subprocess when stock insufficient | Both examples included this | Strong |
| Stage transitions have triggers | "Alert when product arrives" | Moderate |

### What the Call Does NOT Support

| Hypothesis Element | Status |
|--------------------|--------|
| Quote stage as part of workflow | Not mentioned in either example |
| Sales Invoice stage | Not mentioned — David stopped at "ship" |
| Payment collection step | Not mentioned |
| Clean wholesale/distribution flow | No example provided |

### Directional Summary

The chemical company example supports:
```
Order → Check Stock → (PO if needed) → Receive → Ship
```

It does **not** support the full hypothesis:
```
Quote → Order → Ship → Invoice
```

The Quote and Invoice stages remain **unvalidated** from this call.

---

## Critical Sales Workflow Steps (David's Expert View)

David identified these as **the most critical steps** in the sales workflow:

1. **Know if stock exists** to fill the order
2. **Create PO** if stock is insufficient
3. **Alert customer** when product arrives
4. **Confirm payment status** before delivery

**Key Quote:**
> "If they're placing orders, they need to know if they have stock to fill the order. And if they don't have enough stock, they need to be able to create a purchase order to order it from the vendor. And they need to be alerted when that product comes in so they can let the customer know."

---

## Table Stakes vs. Differentiators

### Table Stakes (Must-Haves)

| Capability | David's Words |
|------------|---------------|
| Ease of use / Intuitiveness | "Shouldn't have to click multiple times to get an order through" |
| Add customer/vendor on the fly | "If the customer is not there, they should be able to add on the fly" |
| Stock lookup during order entry | "Easily look up quantity on hand as they're entering an order" |
| Multi-location with bin locations | "Multiple locations and have bin location within those locations" |
| Serial number tracking | "Track the product by serial number and where it's gone" |
| Email orders (PO, SO) | "Emailing orders, purchase orders, sales orders to customers" |
| Quantity available vs. on hand distinction | "That's what I was just going to ask — the distinction between on hand and available" |

### Differentiators (Would Win Deals)

| Capability | David's Words |
|------------|---------------|
| Customer portal for order status | "Maybe the ability to have a portal so a customer can log in and see the status of their order instead of having to call" |
| Mobile salesperson access | "Remote salespeople or mobile salespeople be able to enter an order from wherever they are" |
| Automated workflows | "Automating workflows, updating fields automatically when XYZ happens" |
| Dashboards & reporting | "Good reporting, dashboards, min/max levels, reorder points" |
| Automated low stock alerts | "They need to be alerted when they're low in stock" |
| Lead time tracking | "They need to know lead times, how long it takes to get that product from that vendor" |

### Future Needs (Manufacturing)

- Batch numbers
- Expiration dates
- Bill of Materials (BOM)

David noted: "When you talk about manufacturing, you're adding a whole other complexity with bill of materials and things of that nature."

---

## Reporting Requirements

David listed these reports as **very important to manufacturers and retailers:**

- Min/max levels
- Reorder points
- Gross margins on orders
- Commission reports
- Sales by customer
- Sales by location
- Sales by product
- Lead times

**Key Quote:**
> "These type of reports are very important to manufacturers and retailers."

**Current Gap:** Reporting was flagged as needing more discovery. John acknowledged: "Reporting in general at Method needs a lot more love and attention."

---

## QuickBooks Integration Risk (Technical Concern)

David raised a **critical technical concern** about QBO integration based on his implementation experience:

### The Problem

> "Most other inventory systems require that tracking quantity on hand in QuickBooks be turned off because they can't handle both. QuickBooks gets confused and ends up overstating cost of goods sold."

### Specific Concerns Raised

| Concern | Details |
|---------|---------|
| Stock adjustments sync | Adjustments in Method are Method-only, won't sync to QBO |
| COGS tracking conflicts | Other systems often disable QBO tracking to avoid issues |
| Costing methods | FIFO/LIFO not currently supported |
| System of record confusion | "This should be their system of record for what's on hand and the total value" |

### Current Design Decision

Method's inventory quantity tracking is **Method-only**:
- Method tracks physical stock movements (from SO/PO)
- QBO tracks accounting movements (from Invoice/Bill)
- Numbers may differ
- Customer responsible for reconciliation

**Risk:** This may cause confusion for sophisticated MWD customers who expect a single source of truth.

---

## Why David Reconnected with Method

> "I reconnected at the beginning of the year. I just wanted to see how the product has changed, what other capabilities there are... particularly the improving CRM features and the upcoming inventory functionality."

### What He's Comparing To

David mentioned other CRMs have:
- Sales funnels
- Sequence emails
- Stage-based lead progression
- Automated alerts

**Implication:** Partners like David actively evaluate Method against competitors. He's essentially saying: *"If you build this right, I'll recommend you. But I have alternatives."*

---

## Demo Feedback

### Positive Signals

- "It's a good start"
- "You have some of the basics down"
- Interested in beta testing
- Offered to provide ongoing feedback

### Concerns/Gaps Identified

- No quantity available/on hand/committed columns yet (in development)
- No costing method (FIFO/LIFO)
- Reporting not defined
- QBO sync complexity
- No ETA for GA

---

## Key Quotes for Stakeholder Communication

| Theme | Quote |
|-------|-------|
| Pain before solution | "They had no idea how much inventory they had at all. They didn't know what their formulas were. They had one person that had all the formulas in their head. If that person got hit by a car, everything's gone." |
| Critical workflow step | "If they're placing orders, they need to know if they have stock to fill the order." |
| Ease of use imperative | "It has to be intuitive for the customer. They shouldn't have to click multiple times to get an order through." |
| Visibility value | "Communication and visibility are very important." |
| Reporting requirement | "These type of reports are very important to manufacturers and retailers." |
| Integration risk | "Most other inventory systems require that tracking quantity on hand in QuickBooks be turned off because they can't handle both." |
| Workflow variance | "They do vary a lot." |

---

## Action Items

- [ ] Elaine Chow to send follow-up email if more questions arise
- [ ] John Miranda to send 2025 inventory roadmap survey to David
- [ ] Keep David in loop for future beta testing opportunities

---

## Follow-Up Research Needed

To actually validate the order-centric workflow, the team needs:

1. **A story from a wholesale/distribution customer** — not field service, not manufacturing
2. **Explicit walk-through of their order process** — "Tell me about the last order you processed, start to finish"
3. **Confirmation of stages and handoffs** — who does what, when, and how they know it's done
4. **Multiple data points** — one call is not validation

### Recommended Next Steps

| Action | Purpose |
|--------|---------|
| Schedule call with wholesale/distribution customer | Get workflow story from target persona |
| Ask for specific recent order example | Anchor to real behavior, not generalizations |
| Map personas to stages | Understand who does what at each step |
| Validate handoff points | Identify where friction occurs |

---

## Summary Assessment

### What This Call Provided

- Expert perspective on what MWD customers need (features, capabilities)
- Good signal on table stakes vs. differentiators
- Technical risk awareness (QBO integration, COGS)
- Potential beta tester and partner channel opportunity
- Two specific customer stories (though edge cases)
- Directional support for **Order → Check Stock → (PO if needed) → Ship** sequence

### What This Call Did NOT Provide

- Workflow validation for the order-centric hypothesis
- Confirmation that Quote → Order → Ship → Invoice is how MWD operates
- Evidence that Quote stage exists in MWD workflows
- Evidence that Sales Invoice stage is part of the workflow (David stopped at "ship")
- Persona clarity at each stage
- Clean wholesale/distribution example

### Workflow Validation Status

| Stage | Validated? | Evidence |
|-------|------------|----------|
| Quote | ❌ No | Not mentioned in either example |
| Order | ✅ Directionally | "Customer places order" — starting point in both examples |
| Check Stock | ✅ Directionally | Explicitly called critical by David |
| PO Subprocess | ✅ Directionally | Mentioned in both examples |
| Ship | ✅ Directionally | End point in chemical company example |
| Invoice | ❌ No | Not mentioned — David stopped at "ship to customer" |
| Payment | ❌ No | Not mentioned |

### Bottom Line

This was a valuable discovery call that surfaced pain points, feature requirements, and technical risks. However, **the core workflow hypothesis remains partially untested**:

- The **middle of the workflow** (Order → Ship) has directional support
- The **bookends** (Quote stage, Invoice/Payment stages) have **no evidence** from this call

David's expertise is in inventory management systems broadly — his examples were field service and manufacturing, not the wholesale/distribution focus of the MLP. Additionally, he described workflows ending at "ship to customer" without mentioning invoicing or payment collection.

A world-class PM would note this as *useful directional signal for the Order → Ship sequence* but flag that:
1. The Quote stage remains unvalidated
2. The Invoice/Payment stages remain unvalidated
3. No wholesale/distribution example was obtained
4. Additional research is needed with target-persona customers

---

*Document created: January 19, 2026*
*Analysis by: Claude Code*
