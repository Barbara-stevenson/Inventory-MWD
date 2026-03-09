# Customer Feedback Call Insights: Europena (Food Distribution)

**Date:** January 23, 2026
**Attendees:** Noor Shamji, Evelin Hodges (Eve), John Miranda, Thomas Darlington
**Duration:** ~27 minutes

---

## Executive Summary

This customer feedback call with Evelin Hodges from Europena, a food distribution company transitioning into manufacturing, provided direct customer perspective on Method CRM usage, inventory tool pain points, and workflow friction. **Europena is a heavily customized Method user** who relies on the platform primarily as a CRM for sales reps — not for accounting. The call revealed a **concrete third-party inventory integration pain point** (Fishbowl data loss) and **validated the need for a streamlined, native inventory solution**. Eve agreed to participate in future beta testing.

---

## Customer Profile

| Attribute | Detail |
|-----------|--------|
| Company | Europena |
| Industry | Food Distribution (transitioning to Food Manufacturing) |
| Structure | Two separate companies, each with its own distribution center |
| QuickBooks Version | Desktop (not QBO) |
| Inventory Tool (Current) | Fishbowl (migrating to Marov for Company 2) |
| Method Usage | CRM for sales reps — reporting, activities, opportunities, audits, web-to-lead |
| Customization Level | Very high — Noor described it as "intense" |
| Key Contact | Evelin Hodges (manages Method internally) |
| PS Contact | Thomas Darlington (assisted with customization and cleanup) |

**Why this matters:** Europena represents the exact MWD customer profile that experiences friction from disconnected inventory tools. They are actively migrating between third-party inventory systems, which signals openness to a native Method solution.

---

## How Europena Uses Method

### Primary Use Cases

| Use Case | Details |
|----------|---------|
| CRM for Sales Reps | View sales numbers, log activities, manage opportunities |
| Custom Reporting | Trend analysis, seasonality analysis — heavily customized |
| Contact Management | Data cleanup, duplicate detection (parent-child data structure) |
| Audits App | Store-level auditing with pictures and notes |
| Web-to-Lead | Lead capture at trade shows via iPad/phone |
| User Permissions | Granular access control — sales reps cannot see each other's numbers or accounting data |
| Rolling Data App | Custom app for rolling data analysis |

### What They Do NOT Use Method For

- Accounting (kept in QuickBooks)
- Invoicing (done in QuickBooks, synced into Method)
- Purchase Orders (handled at head office in QuickBooks)
- Two-way sync (they pull FROM QuickBooks, not push back)

**Key Insight:** Europena's value proposition from Method is **one-directional data flow** — pulling QuickBooks data into a customized CRM layer for sales reps. This is a different usage pattern than the typical two-way sync customer.

---

## Inventory Workflow (Current State)

### Company 2 (Fishbowl → QuickBooks Desktop → Method)

Eve walked through the workflow explicitly (00:10:19):

```
Receive PO → Enter Sales Order in Fishbowl →
Pull inventory from Fishbowl → Ship product →
Sync to QuickBooks → Create Invoice in QuickBooks →
Adjust invoice if needed → Finalize invoice →
Integrate invoice into Method
```

### Company 1 (QuickBooks Direct → Method)

```
Enter Sales Order in QuickBooks → Turn into Invoice →
Integrate into Method
```

### Workflow Confirmed by Eve (00:12:35)

John summarized and Eve confirmed:
> "You get an order, you ensure you have the right amount of inventory, you would pick, pack it, ship it, and then sync the sales order, sync the invoice into accounting and get paid."

Eve: "Yes. Yes. Yes."

**This is significant:** Eve explicitly confirmed the **Order → Check Stock → Pick/Pack → Ship → Invoice → Payment** workflow — a closer match to the order-centric hypothesis than what was obtained from the David Singletary call.

---

## Workflow Validation Assessment

### Status: PARTIALLY VALIDATED (Distribution Flow)

| Stage | Validated? | Evidence |
|-------|------------|----------|
| Quote | Not mentioned | Not part of Europena's described workflow |
| Order (Sales Order) | Yes | "We enter the sales order in Fishbowl" / "We have our sales order in there" |
| Check Stock | Yes | "We check with the inventory and then if it's missing..." |
| Pick/Pack/Ship | Yes | Confirmed when John summarized "pick, pack, ship" |
| Invoice | Yes | "We have to create the invoice" / "We turn it into an invoice" |
| Payment | Implied | Confirmed John's summary ending with "get paid" |
| PO Subprocess | Yes | "The invoice in the PO" — POs handled at head office |

### Comparison to David Singletary Call

| Element | Singletary Call | Europena Call |
|---------|----------------|---------------|
| Quote stage | Not validated | Not validated |
| Order → Ship | Directionally supported | Explicitly confirmed |
| Invoice stage | Not mentioned | Explicitly confirmed |
| Payment stage | Not mentioned | Confirmed (via summary agreement) |
| Clean distribution example | Not obtained | Obtained |
| Target vertical match | Weak (field service, manufacturing) | Strong (food distribution) |

**The Europena call fills gaps left by the Singletary call.** The Invoice and Payment stages that were missing from Singletary's examples are now confirmed by a real distribution customer. The Quote stage remains unvalidated across both calls.

---

## Third-Party Inventory Integration Pain Point (Fishbowl)

### The Core Problem

All items from Fishbowl entered QuickBooks as generic "Fishbowl items" regardless of what the actual product was.

**Eve's description (00:05:22):**
> "Everything just became like a Fishbowl item. So it doesn't... it didn't matter like what kind of... if it's the actual product or if it's credits or if it's disbursements, everything just came in as like a Fishbowl item."

### Impact Chain

```
Fishbowl → QuickBooks: All items labeled "Fishbowl item" (description in memo field, not description field)
QuickBooks → Method: Items synced as "Fishbowl item" under description
Result: Cannot search for specific products (e.g., "citrus and lemon")
Workaround: Manual data cleanup — download everything, sort, re-enter descriptions
```

**Eve (00:08:17):**
> "If I wanted to search like for example one of our products citrus and lemon, I'm not able to pull it out as citrus and lemon, but I have to go in and pull it out under the memo under Fishbowl item and then just kind of download everything and then start sorting it out from there."

**John's assessment (00:09:21):**
> "It's almost triple the amount of work when it should just have been once."

### Why This Matters for Method's Native Inventory Solution

This is a **real-world example of the integration friction** that the Hybrid approach is designed to solve. If Method's native inventory solution handles item descriptions properly during sync, it eliminates this entire class of pain point. It also validates why data structure alignment between inventory and accounting systems is critical.

### Migration to Marov

Europena is migrating Company 2 from Fishbowl to Marov because:
- Marov's data structure aligns with QuickBooks' data structure
- Items will sync with correct descriptions (not generic labels)
- Should require less customization in Method

Eve has not started using Marov yet — they are still in the data input stage.

---

## Why Europena Chose (and Keeps) Method

### Initial Decision

| Factor | Weight |
|--------|--------|
| QuickBooks integration | Primary reason for initial adoption |

### Retention Factors

| Factor | Eve's Words |
|--------|-------------|
| Customization | "The biggest thing that we have now is the fact that we're able to customize it and get like reports and stuff. That's what has really made us keep it." |
| Sunk investment | "We've already put a lot of invested a lot of time into it" |
| Reporting | Trend analysis, seasonality analysis — Noor noted "the reports look stunning" |
| User permissions | "We're able to just tweak them around and customize them to what we want" |
| Mobile views | iPad and phone views important for audits and trade show lead capture |

### Churn Risk Signal

Eve disclosed that keeping Method was a **50/50 decision**:

> "I know it was 50/50 in terms of like should we keep it, should we not, but I think the biggest thing that we have now is the fact that we're able to customize it."

**Risk Assessment:** Europena stayed because of customization investment and reporting. If a competitor offered comparable customization with better inventory integration, the switching cost argument weakens. A native inventory solution strengthens the retention case.

---

## Challenges and Friction Points

### 1. Sync Conflicts (Method ↔ QuickBooks)

**Eve (00:20:30):**
> "Sometimes when you wake up and the numbers are not correct, but then if you do another sync... and then all of a sudden the numbers are correct."

Eve noted improvement in the last few months, likely due to the sync widget.

### 2. Too Many Steps in the Workflow (Biggest Friction Point)

**Eve (00:23:20):**
> "I think we have a lot of steps. It would be nice to cut them down honestly."

**Eve's described workflow pain (00:24:47):**
> "It's the invoice in the PO, then we get the sales order, then we have to create the invoice, and then we have to go back and then we check with the inventory, and then if it's missing, and then after that we have to then change that invoice around and make it a final invoice, and then before it's sent out — and we don't send out our invoices from QuickBooks as well."

**Eve's ask:**
> "If Method would be able to streamline our processes to make them shorter but more accurate... just make them shorter, that would really help."

### 3. Initial Adoption Resistance

Before customization work (with Thomas), users didn't want to use Method due to glitches and data not syncing properly. Adoption improved after investment in customization.

---

## Personas and Role Separation

Europena has a clear separation of responsibilities:

| Persona | Tools Used | Responsibilities |
|---------|------------|------------------|
| Sales Reps | Method (CRM only) | View numbers, log activities, manage opportunities, send sales order copies, web-to-lead at trade shows |
| Logistics/Admin (Head Office) | QuickBooks + Fishbowl | POs, sales orders, invoicing, inventory processing |
| Buyers | Fishbowl + QuickBooks | Inventory purchasing and management |
| Eve (Admin/Champion) | Method + QuickBooks | Customization, reporting, data cleanup, system management |

**Key Insight:** Sales reps have **no access to QuickBooks or accounting data**. Method is their window into the business. This means any inventory visibility surfaced in Method needs to be tailored for a sales rep audience — showing stock availability without exposing accounting details.

---

## Multi-Location Context

- Two separate companies, each with **one distribution center**
- Company 1: one distribution center
- Company 2: one distribution center
- **Not a multi-warehouse scenario** within a single company

**Implication:** Europena is not a strong candidate for validating multi-warehouse features within the MLP. Their multi-location complexity is at the company/entity level, not the warehouse level.

---

## Future Direction: Manufacturing Transition

Eve mentioned Europena is transitioning from food distribution into food manufacturing (00:15:23, 00:22:23). This would change their inventory needs:
- Manufacturing requires BOM/formula management
- Marov is being brought in to support this transition
- Eve envisions eventually invoicing directly out of Method

**Eve (00:16:14):**
> "I'm looking at a future where we'll be able to invoice out of Method directly, like from the customer out into Method."

**Implication:** Europena could become a more complex use case over time. Their current distribution workflow validates the MLP scope, but their manufacturing transition would push into Priority 3+ territory.

---

## Key Quotes for Stakeholder Communication

| Theme | Quote |
|-------|-------|
| Workflow friction | "I think we have a lot of steps. It would be nice to cut them down honestly." |
| Streamlining ask | "If Method would be able to streamline our processes to make them shorter but more accurate... just make them shorter, that would really help." |
| Fishbowl data loss | "Everything just became like a Fishbowl item. So it doesn't matter if it's the actual product or credits or disbursements, everything just came in as like a Fishbowl item." |
| Manual workaround | "We have had to then manually go in and put in the description. We actually need to put in the actual item because we're dealing item by items." |
| Why they stay | "The biggest thing that we have now is the fact that we're able to customize it and get like reports and stuff. That's what has really made us keep it." |
| Churn risk signal | "It was 50/50 in terms of should we keep it, should we not." |
| Love for Method | "I love Method. It's like my baby." |
| Role separation | "Our sales reps don't get to use QuickBooks. There's a department that does all of that processing." |
| User permissions value | "We customized them seeing what they need to see." |

---

## Action Items

- [ ] Noor Shamji to send inventory-related survey questions from John Miranda to Eve via existing email thread
- [ ] John Miranda to reach out to Eve in the future for inventory testing / beta release
- [ ] Eve to answer the inventory-related survey questions
- [ ] Thomas Darlington to review Marov data structure samples Eve sent over

---

## Relevance to MLP Scope

### What This Call Validates for MLP Priorities

| MLP Feature | Validation from This Call |
|-------------|--------------------------|
| **Available Inventory Visibility** (P1) | Eve's workflow includes "check with the inventory and then if it's missing" — visibility at order entry is critical |
| **Third-Party Integration** (P1) | Fishbowl integration failure is a concrete pain point; Marov migration shows customers actively switch between inventory tools |
| **Multi-Warehouse Management** (P1) | Not validated — single distribution center per company |
| **Dynamic Item Management** (P2) | "Fishbowl item" data loss shows why proper item-level data integrity matters |
| **Backorder Awareness** (P2) | Implied — Eve mentions checking inventory and adjusting invoices "if it's missing" |

### What This Call Does NOT Validate

- Multi-warehouse workflows within a single company
- Reorder points / low stock alerts
- Quote stage in the workflow
- Serial number tracking
- BOM/formula requirements (future state only)

---

## Summary Assessment

### What This Call Provided

- A **real food distribution customer workflow** that confirms the Order → Check Stock → Ship → Invoice → Payment sequence
- A **concrete third-party integration pain point** with data loss between Fishbowl → QuickBooks → Method
- Evidence that **workflow streamlining** is the #1 customer ask
- Insight into **role-based access patterns** — sales reps use Method as a read-only CRM window
- Confirmation that **customization and reporting** are the primary retention drivers
- A **churn risk signal** (50/50 decision to stay) that underscores the importance of adding inventory value
- A willing **beta tester** for the native inventory solution

### What This Call Did NOT Provide

- Multi-warehouse validation
- Quote stage in the workflow
- Deep inventory feature requirements (serial numbers, lot tracking, reorder points)
- Marov integration details (not yet in use)
- Manufacturing workflow specifics (still in planning)

### Bottom Line

Europena is a valuable data point because they represent a **real distribution customer** experiencing friction from disconnected inventory tools. Their confirmed workflow (Order → Stock Check → Ship → Invoice) fills critical gaps from the Singletary call — particularly the Invoice and Payment stages. However, this is a **relatively simple distribution setup** (single warehouse per company, basic inventory needs) that validates the MLP's floor, not its ceiling. The 50/50 retention signal and Eve's explicit ask for workflow streamlining reinforce that inventory improvements are directly tied to retention for MWD customers.

---

*Document created: January 23, 2026*
*Analysis by: Claude Code*
