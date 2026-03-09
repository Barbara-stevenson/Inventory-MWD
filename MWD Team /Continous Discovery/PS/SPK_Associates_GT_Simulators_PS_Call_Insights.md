# PS Discovery Call Insights: SPK Associates & GT Simulators (with Matt Shade)

**Date:** January 29, 2026
**Attendees:** John Miranda, Matt Shade Silver (PS), Elaine Chow, Barbara Stevenson
**Duration:** ~53 minutes

---

## Executive Summary

This PS discovery call with Matt Shade reviewed two MWD customer accounts — SPK Associates (manufacturing broker/middleman) and GT Simulators (medical device manufacturing) — plus brief mentions of CYC (thrift store distributor) and Central Auction Group. SPK Associates is the most complex workflow Matt manages across his 22 accounts, featuring a **multi-step process with custom RFQS, vendor management, and a strict vendor-customer separation requirement**. GT Simulators is a simpler medical manufacturing operation with prepayment and Net 30 invoicing models. A key cross-cutting insight is that **Sales Orders are the most customized application across all of Matt's accounts**, functioning as the de facto project management tool for shipments. The call also surfaced that only 4 out of 22 accounts use Purchase Orders, but all 4 require customization on the PO creation screen.

---

## Interviewee Profile

| Attribute | Detail |
|-----------|--------|
| Name | Matt Shade Silver |
| Role | Professional Services (PS) at Method |
| Total MWD Accounts | ~22 |
| Accounts Using POs | 4 out of 22 |
| Notable Clients | SPK Associates, GT Simulators, CYC (distributor), Central Auction Group |
| Previous PS on SPK | Cole and Ryan (Matt inherited the account ~2 months ago) |

**Important Context:** Matt is an internal PS team member with hands-on experience customizing Method for ~22 MWD accounts. Like Yasar, his observations are **proxy evidence** — observed patterns across multiple customers, not a single customer's firsthand story. He inherited SPK Associates recently but built GT Simulators from scratch, so his depth varies by account.

---

## Customer 1: SPK Associates

### Company Profile

| Attribute | Detail |
|-----------|--------|
| Industry | Manufacturing broker/middleman (custom goods: artwork, tapestries, furniture, etc.) |
| Business Model | Bridges customers and vendors/wholesalers; commission-based |
| Primary Contact | Don (runs the company) |
| Users | 7 total, 5-6 active |
| Method Usage | Opportunities, RFQS (custom), Quote Worksheets (custom), POs, Sales Orders, Invoices, Vendor Portal |
| Inventory Model | Non-inventory items — "comes in and goes out immediately" (00:16:55) |
| Shipping | Outsourced to third party; manual tracking number input |
| Payment | Collected through portal |

### Critical Business Rule

**Vendors and customers cannot communicate directly.** This is the foundational business constraint — SPK Associates exists as the middleman, and if customers discovered vendors directly, they'd bypass SPK for better deals.

**Matt (00:02:31):**
> "That was like the first thing he said whenever we do anything they cannot talk to each other, see each other, know each other, who they are. Like that was the thing that he really hammered home."

### Compensation Structure

SPK Associates uses a commission-based system where sales reps start with a salary they must "pay off" through sales. As reps improve, they transition to pure commission. Commission tiers are based on products sold (different multipliers per product), but calculated manually — no pricing levels set up in Method. Matt has recommended implementing pricing levels (00:11:14).

### Workflow

```
Opportunity (sales pipeline entry) →
    RFQS (Request for Quotes — gather specs from customer) →
        Design breakdown (materials, packing, specifications) →
    Convert RFQS to Purchase Order(s) →
        POs sent to vendor(s) via Vendor Portal →
        Vendor returns pricing information →
    Quote Worksheet generated (finalized estimate for customer) →
        Customer approves →
    Sales Order created →
    Build/manufacture →
    Ship (outsourced, manual tracking number) →
    Invoice (issued from Opportunity) →
    Payment (collected via portal)
```

### Key Details

**Opportunities as Pipeline Hub:**
- All new business enters through Opportunities — not Estimates (00:03:26)
- Opportunities are preferred because SPK manages multiple document types per deal (POs, SOs, estimates, invoices, RFQS)
- Opportunities hold vendor lists, scope of work, dates, and all related transactions
- A "successful opportunity" is defined as one that has a Sales Order (00:06:32)
- Matt explains why Opportunities work here but not for simpler businesses: "with them they have vendor list and options... they have to manage all the dates but also have to manage it in the PO sense" (00:05:29)

**RFQS (Request for Quotes) — Custom App:**
- Custom app critical for manufacturing workflows (00:07:27)
- Different from an estimate — focuses on materials, packing, and design specifications rather than pricing
- Customer provides specs: "Hey, I want a chair. This is what I want in my chair" (00:09:26)
- Once RFQS is built, it converts to a Purchase Order to send to vendors
- Can have multiple RFQS per Opportunity

**Quote Worksheet — Custom App:**
- Functions as a finalized estimate for the customer, generated after vendors return pricing (00:13:01)
- Can have multiple quote worksheets per RFQS (for revisions or additional orders)
- Includes design breakdown with build instructions (00:13:52)

**Multi-Vendor Purchase Orders:**
- When converting RFQS to PO, the system loops through all vendors assigned to items (00:14:57)
- 5 items with 4 vendors = 4 separate POs, each with the correct items
- This multi-vendor PO creation is custom — out of box requires manually creating POs one vendor at a time

**Vendor Portal:**
- Different experience from customer portal — more of a business relationship (00:17:54)
- Features a messaging board replacing email back-and-forth
- Vendors fill in pallet details for shipping
- Accept/deny workflow: vendors save pallet details → email sent → SPK accepts or denies → deny triggers request for more info
- Recurring activities send automated follow-up emails to unresponsive vendors
- "The vendor communication saves a lot of time" (00:22:01)

**Shipping:**
- Outsourced to third party
- Manual tracking number input (not API-connected yet)
- Matt's philosophy: start manual to build confidence, then automate (00:20:12)
- ShipStation recommended as next step but "they're not ready for that yet" (00:25:02)

**ChatGPT Integration (In Progress):**
- Matt is building a ChatGPT → Google Sheets → Zapier → Method integration (00:31:40)
- Sales reps verbally describe deals to ChatGPT on their phone
- ChatGPT fills out an importable Google Sheet template
- Zapier creates an Opportunity in Method from the sheet
- Eliminates manual data entry (reps were entering same info ~5 times)
- Matt calls it a "game changer" (00:32:31)

### Workflow Validation (Order-Centric Hypothesis)

| Stage | Present? | Notes |
|-------|----------|-------|
| Quote/Estimate | Yes (custom) | RFQS (spec gathering) → Quote Worksheet (pricing/finalization) |
| Sales Order | Yes | Created after customer approves quote worksheet |
| Purchase Order | Yes | Multiple POs per deal, per vendor — critical part of workflow |
| Ship | Yes, outsourced | Third-party shipping, manual tracking |
| Invoice | Yes | Issued from Opportunity, summarizes all SOs and POs |
| Payment | Yes | Collected through portal |

**Notable:** SPK Associates validates a longer, more complex variant of the order-centric hypothesis. The Quote stage is split into two custom apps (RFQS for specs, Quote Worksheet for pricing). Purchase Orders play a central role — they're sent TO vendors, not placed BY customers. The Opportunity serves as the overarching project hub.

---

## Customer 2: GT Simulators

### Company Profile

| Attribute | Detail |
|-----------|--------|
| Industry | Medical device manufacturing (compression dummies, CPR training equipment) |
| Business Model | Direct manufacturing and sales — mostly in-house production |
| Sales Channel | Website (Shopify integration) + direct requests |
| Shipping | Worldwide (including Africa, Asia) — ships internationally |
| Key Contact | Technical director (builds customizations with Matt) |
| Users | One person manages everything (account management model) |
| Vendor Usage | Minimal — mostly in-house; some vendors for particular items |

### Workflow

```
Estimate (info gathering) →
    Estimate accepted →
Sales Order (main management hub) →
    [If prepayment]:
        Invoice created with single "prepayment" line for full amount →
        As items ship, invoice updated: item lines added, prepayment line adjusted →
        Total stays constant, inventory updates live
    [If Net 30]:
        Invoice updates automatically →
    Ship (partial shipping common) →
        Yellow = partially shipped, Green = fulfilled (HTML customization) →
        Pack checkbox for "packed and ready to go" →
    Payment
```

### Key Details

**Sales Order as Project Hub:**
- Everything is managed from the Sales Order (00:23:04)
- "The sales order is kind of like where the magic is because this is kind of like the project manager thing" (00:41:11)
- Sales Orders are the most customized app across all of Matt's accounts (00:43:37)

**Prepayment Inventory Tracking:**
- Complex invoicing method to keep inventory accurate with prepayments (00:40:07)
- Initial invoice = one line "prepayment sales order amount" for full total
- As items ship, individual item lines are added to the invoice
- Prepayment line adjusts so total stays constant
- This ensures inventory updates only when items actually ship

**Partial Shipping:**
- "Biggest thing with this is partial shipping. Got to think about that. It happens all the time" (00:42:48)
- "Like Amazon. You order 10 things, they don't all come together. They're coming from different places" (00:42:48)
- HTML color-coding tracks status: yellow (partially shipped), green (fulfilled)

**Invoice Column Bug/Limitation:**
- Invoice quantity doesn't update live when additional invoices are created (00:41:59)
- Matt filed a ticket: "it should be like the live current amount how that product is invoiced for the specific line item"
- Workaround: manual ship column tracking until invoice column gets fixed

**Shopify Integration:**
- Orders come in via Shopify website
- International addresses cause issues (e.g., Asian postal codes = 11 digits, no region code field) (00:34:23)

### Workflow Validation (Order-Centric Hypothesis)

| Stage | Present? | Notes |
|-------|----------|-------|
| Estimate | Yes | Starting point for capturing requirements |
| Sales Order | Yes | Core management hub — prepayment or Net 30 |
| Ship | Yes | Partial shipping common, worldwide |
| Invoice | Yes | Complex prepayment model or Net 30 |
| Payment | Yes | Prepayment upfront or Net 30 terms |
| Purchase Order | Limited | Some vendor purchases, not central to workflow |

**Notable:** GT Simulators validates a cleaner Estimate → Sales Order → Ship → Invoice flow. The Estimate stage is explicitly confirmed. Partial shipping is the dominant pattern, not the exception.

---

## Other Accounts Referenced

Matt briefly mentioned two additional MWD accounts during the call. Neither was explored in depth, but both add useful context.

### CYC (Distributor — Thrift Stores)

| Attribute | Detail |
|-----------|--------|
| Industry | Distribution (thrift stores) |
| Transaction Types | Freight orders, purchase orders, sales orders, proforma invoices, estimates |
| Packing Slips | Yes — the **only** account of Matt's 22 that uses packing slips (00:25:02) |
| Shipping | Handles all shipping in-house; no API integration yet ("still low budget") |
| Team Structure | One person does everything (00:50:17) |

**Why this matters:** CYC is the only distributor in Matt's portfolio that does packing slips and manages their own shipping end-to-end. This makes them a potential reference for validating pick/pack/ship workflows within Method. Their use of proforma invoices also suggests a more complex transaction flow than most distributors.

### Central Auction Group

| Attribute | Detail |
|-----------|--------|
| Industry | Auction brokerage (middleman between auctioneers and sellers) |
| Business Model | Similar to SPK Associates — bridges two sides of a marketplace |
| Team Structure | One person does everything (00:50:17) |

**Why this matters:** Central Auction Group is another middleman/broker business like SPK Associates, but with a simpler one-person operation. Matt provided almost no workflow detail, so this account is noted for reference only. The middleman pattern (connecting buyers and sellers while managing the process in between) appears across multiple account types — not just manufacturing.

---

## Cross-Cutting Patterns Across Matt's Accounts

### Pattern 1: Sales Orders Are the Most Customized App

**Matt (00:43:37):**
> "What app do you see yourself customizing a lot? Sales orders. Sales orders. Well, more more people again... they need a way to man... this manages all the shipments where we don't have a place to manage it."

Sales Orders have become the de facto project management tool for shipments because Method doesn't have a dedicated shipment management area.

### Pattern 2: Purchase Order Creation Needs Customization for Every Account That Uses It

**Matt (00:48:17):**
> "I think four I'm probably at four out of 22 that are using purchase orders. And they all I've customized like so this screen for everyone."

Common customization requests:
- Multiple vendors per PO creation (loop through distinct vendors)
- Drop-down to specify vendor per line item
- Use preferred vendor and auto-create separate POs
- Ability to change quantity on the PO creation screen

### Pattern 3: Color-Coding / Visual Status Indicators Are Highly Requested

**Matt (00:45:32):**
> "Do you know the amount of people that request coloring? ... this is all HTML... this took us like a year just like literally just the HTML stuff took us like six months."

Grid-level visual status (color-coding rows by status) is a common request but requires extensive HTML customization — not available out of the box.

### Pattern 4: Partial Shipping Is the Norm, Not the Exception

Manufacturing and distribution customers consistently deal with partial shipments. Items come from different vendors at different times. The workflow must accommodate tracking what's shipped vs. what's outstanding.

### Pattern 5: Opportunities vs. Estimates — Depends on Complexity

**Matt (00:04:28–00:06:32):**
- **Simple workflows** (construction, single-track estimate → invoice): Estimates preferred, Opportunities feel like an extra step
- **Complex workflows** (manufacturing, multiple document types, vendor management): Opportunities preferred because they manage the sales pipeline and hold all related information
- SPK Associates uses Opportunities; GT Simulators uses Estimates as entry point

### Pattern 6: Distributors vs. Manufacturers Have Different Team Structures

**Matt (00:50:17):**
- **Distributors** (CYC, Central Auction Group, GT Simulators): One person does everything — sales, order, fulfillment, shipping
- **Manufacturers** (SPK Associates): Multiple people involved — sales reps handle accounts end-to-end, but fulfillment/shipping may be separate

---

## Common Customizations for MWD Clients (Matt's Accounts)

| Customization | Frequency | Details |
|---------------|-----------|---------|
| Sales Order as shipment tracker | Very common | Most customized app; manages partial shipping, fulfillment status |
| Multi-vendor PO creation | All PO users (4/22) | Custom loop to create separate POs per vendor from one screen |
| Color-coded grid views (HTML) | Very common | Status visualization (shipped/partial/unfulfilled) requires extensive HTML |
| Vendor Portal with messaging | SPK-specific | Replaces email back-and-forth with in-app communication |
| RFQS / Quote Worksheet apps | SPK-specific | Custom spec-gathering and pricing workflow for manufacturing brokers |
| Commissions tracking app | SPK-specific | Commission-based sales rep management |
| Prepayment invoice management | GT Simulators | Complex invoice restructuring for inventory accuracy with prepayments |
| ShipStation API integration | Multiple accounts | Pre-built catalog integration for automated shipping tracking |

---

## Workflow Comparison: SPK Associates vs. GT Simulators

| Element | SPK Associates | GT Simulators |
|---------|---------------|---------------|
| Starting point | Opportunity | Estimate |
| Quoting process | RFQS (specs) → Quote Worksheet (pricing) | Estimate only |
| Sales Order | Yes, after customer approval | Yes, from accepted estimate |
| Purchase Orders | Central to workflow (multi-vendor) | Minimal |
| Vendor management | Critical — Vendor Portal, messaging, separation | One wholesaler, mostly in-house |
| Manufacturing | Outsourced to vendors | Mostly in-house |
| Shipping | Outsourced, manual tracking | In-house, partial shipping common |
| Invoicing | From Opportunity (summarizes all) | Prepayment or Net 30 |
| Payment | Portal | Prepayment or Net 30 |
| Users involved | 5-6 (multi-role) | 1 (does everything) |
| Complexity level | Most complex of Matt's 22 accounts | Simpler, more linear |

---

## Key Quotes for Stakeholder Communication

| Theme | Quote | Source |
|-------|-------|--------|
| Vendor-customer separation | "Whenever we do anything they cannot talk to each other, see each other, know each other, who they are. Like that was the thing that he really hammered home." | Matt (00:02:31) |
| Why Opportunities over Estimates | "They have the purchase orders, they have the sales orders, they have estimates, they have invoices, and sometimes it's multiple because one chair to five chairs." | Matt (00:04:28) |
| RFQS vs. Estimate | "It's more like getting all the details they need for more of like the design process side of things rather than like actual pricing aspect which kind of comes in later." | Matt (00:08:32) |
| Sales Orders most customized | "Sales orders. Well, more people again... they need a way to manage... this manages all the shipments where we don't have a place to manage it." | Matt (00:43:37) |
| Partial shipping reality | "Biggest thing with this is partial shipping. Got to think about that. It happens all the time... Like Amazon. You order 10 things, they don't all come together." | Matt (00:42:48) |
| Color-coding demand | "Do you know the amount of people that request coloring?... this is all HTML... this took us like a year." | Matt (00:45:32) |
| PO customization universal | "Four out of 22 that are using purchase orders. And they all I've customized like so this screen for everyone." | Matt (00:48:17) |
| Invoice column limitation | "It should be like the live current amount how that product is invoiced for the specific line item. So like you actually know what's invoiced and what's shipped." | Matt (00:41:59) |
| Manual-first philosophy | "There's certain stuff that just has to be manual to make like these people confident at the start and it's meant to be customized to be automated." | Matt (00:20:12) |
| ChatGPT integration | "Game changer for them because now they don't have to repeat stuff three times... they don't have to type anything anymore." | Matt (00:32:31) |

---

## Action Items

- [ ] Matt Shade to ask Ryan about why SPK Associates uses the Quote Worksheet specifically and report back
- [ ] Matt Shade to confirm whether SPK Associates salespeople also handle invoicing, and the exact number of people involved in the process
- [ ] Matt Shade to confirm role breakdown for SPK Associates (who handles what in the workflow)

---

## Relevance to MLP Scope

### What This Call Validates for MLP Priorities

| MLP Feature | Validation | Notes |
|-------------|------------|-------|
| **Available Inventory Visibility** (P1) | Weak | SPK Associates uses non-inventory items; GT Simulators needs live inventory updates with prepayment model |
| **Multi-Warehouse Management** (P1) | Not validated | Neither customer discussed multi-warehouse needs |
| **Third-Party Integration** (P1) | Moderate | ShipStation is pre-connected across many accounts; ChatGPT/Zapier integration shows demand for external tool connections |
| **Dynamic Item Management** (P2) | Moderate | GT Simulators' prepayment model requires dynamic invoice line management as items ship |
| **Backorder Awareness** (P2) | Weak | GT Simulators handles back orders by adding to the sales order and comparing against original estimate (00:43:37) |

### What This Call Reveals About MWD Workflow Patterns

1. **The Estimate stage continues to validate across calls** — GT Simulators starts with an Estimate, SPK Associates uses Opportunities as the entry point instead
2. **Sales Orders are the de facto shipment management tool** — the most customized app across 22 accounts, used because Method has no native shipment management area
3. **Partial shipping is standard practice** — not an edge case. Any shipment tracking feature must handle partial fulfillment
4. **Complex manufacturing workflows need Opportunities as a project hub** — validating the same pattern Yasar identified (SPK Associates = another "opportunities on steroids" case)
5. **Purchase Order creation from Sales Orders needs multi-vendor support** — every account that uses POs requires customization on this screen
6. **Vendor communication management is critical for broker/middleman businesses** — a pattern not yet seen in previous interviews

---

## Summary Assessment

### What This Call Provided

- A **complex manufacturing broker workflow** (SPK Associates) showing how middleman businesses use Method — a new business pattern not seen in previous interviews
- A **simpler medical manufacturing workflow** (GT Simulators) that validates Estimate → Sales Order → Ship → Invoice
- Strong signal that **Sales Orders are Method's de facto shipment management tool** — the most customized app across 22 accounts
- Evidence that **partial shipping is the norm**, not the exception, for MWD customers
- Insight into **Purchase Order creation pain points** — 100% of PO-using accounts require customization
- A clear illustration of **when Opportunities work vs. Estimates** for different complexity levels
- Evidence of **vendor communication management** as a significant workflow need for middleman businesses

### What This Call Did NOT Provide

- Direct customer voice (this is PS perspective, not end-customer interviews)
- Multi-warehouse validation
- Deep inventory management requirements (SPK Associates uses non-inventory items)
- Reorder points or low stock alerts discussion
- Detailed role breakdown for SPK Associates (to be confirmed by Matt)

### Bottom Line

This call is most valuable for its insight into **workflow complexity tiers** and the revelation that **Sales Orders have become the shipment management hub** across MWD accounts. The SPK Associates workflow demonstrates that manufacturing middlemen have fundamentally different needs than direct manufacturers or distributors — they need vendor-customer separation, multi-vendor PO creation, and a custom quoting process that Method doesn't support natively. For the inventory MLP specifically, the key takeaway is that **partial shipping tracking and live invoice updates are critical needs** — GT Simulators' complex prepayment workaround exists solely because inventory quantities need to update in real-time as items ship, not when the invoice is first created.

---

*Document created: January 29, 2026*
*Analysis by: Claude Code*
