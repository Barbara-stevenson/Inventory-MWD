# Customer Discovery Call Insights: Liquid Medlock (Toby Merker)

**Date:** February 5, 2026
**Attendees:** John Miranda, Toby Merker (Supply Chain Manager, Liquid Medlock)
**Duration:** ~31 minutes

---

## Executive Summary

This discovery call with Toby Merker, Supply Chain Manager at Liquid Medlock, revealed one of the most mature and heavily customized inventory implementations in Method CRM. Liquid Medlock is a Canadian-based medical-compliant packaging company (child-resistant packaging for pharmaceutical/cannabis industries) that operates out of **4 separate warehouse locations** and sources product from factories in China. **Method CRM is their operational source of truth** — Toby manages the entire supply chain "birth to death" from a single seat, using custom-built container tracking, purchase order, and inventory apps developed over months with PS developer Safwan. Despite this sophistication, **human error remains the sole remaining pain point**: warehouse code typos, quantity entry mistakes, and the resulting manual reconciliation process. Toby's "magic wand" request was automated warehouse shipment data upload with invoice generation. Notably, **Toby expressed skepticism that any general-purpose inventory solution would match their niche custom setup**, making this a case study in what the ceiling of Method customization looks like — and where it still falls short.

---

## Customer Profile

| Attribute | Detail |
|-----------|--------|
| Company | Liquid Medlock |
| Industry | Medical-Compliant Packaging (pharmaceutical, cannabis, methadone dispersement) |
| Business Model | Distribution — sources from factories in China, sells to B2B customers (pharmacies, addiction treatment centers) |
| Geography | Canadian-based, majority sales from Canada, expanding into US methadone market (12-18 months) |
| Warehouse Locations | 4 separate locations (including G warehouse and Brampton) |
| QuickBooks Version | QuickBooks Online (QBO) |
| WMS | All 4 warehouses use their own WMS software (4 different systems) |
| US Channel | Shopify (self-serve, separate from Method) |
| Method Usage | Full supply chain operations — sales orders, purchase orders, inventory visibility, container tracking, run rates, invoicing |
| Customization Level | Extremely high — months of iterative PS development with Safwan |
| Key Contact | Toby Merker (Supply Chain Manager — manages entire day-to-day operations solo) |
| PS Developer | Safwan |

**Why this matters:** Liquid Medlock represents the most advanced inventory customization we've encountered in Method. Their setup validates the entire inventory MLP thesis — visibility, multi-warehouse, PO tracking, run rates — but achieved through custom development. Their remaining pain points reveal what even the best customization can't solve, pointing to platform-level gaps.

---

## How Liquid Medlock Uses Method

### Primary Use Cases

| Use Case | Details |
|----------|---------|
| Sales Order Processing | Core transaction type — orders entered as sales orders, sent to warehouses via workflows |
| Purchase Order Tracking | Custom PO app tracks quantities ordered from China with real-time updates |
| Container/Shipment Tracking | Custom container app tracks inbound shipments from China — items, quantities, arrival dates, shipping documents |
| Inventory Visibility | QBO syncs daily (~11 AM) to show available quantity per warehouse per product |
| Run Rate Calculations | Custom inventory tab showing 12-month sales velocity, replenishment time, and low-stock email alerts |
| Invoice Generation | Manual process — Toby uploads shipment data into CRM, then generates invoices that sync to QBO |
| Pending Order Management | Sales leads and purchase orders used to hold pending/future orders (e.g., "10,000 units over 6 months") |

### What They Do NOT Use Method For

- Manufacturing/production (factories are external partners in China)
- Pick and pack (they sell full cases, no repackaging)
- Payment collection/posting (handled by accountant in QuickBooks)
- US market orders (handled through Shopify)
- Direct WMS integration (intentionally kept separate from CRM)

**Key Insight:** Liquid Medlock's usage pattern validates the product thesis that MWD merchants want Method to absorb inventory complexity and simplify order-to-cash. They've built exactly this through customization — but it took months of PS effort, and gaps remain.

---

## End-to-End Workflow (Current State)

### Order-to-Cash Workflow

Toby walked through the end-to-end workflow explicitly (00:02:06, 00:03:12):

```
Customer contacts Liquid Medlock →
Sales Order entered in CRM →
    [If pending/future order]:
        Held in pending dropdown → Released when customer confirms →
CRM workflows send order to warehouse →
Warehouse picks and packs order →
Warehouse secures shipping (pre-arranged carrier OR spot rate quote) →
Order ships out →
Warehouse sends end-of-day shipped report (manual) →
Toby uploads shipment data + tracking into CRM (manual, one-by-one) →
Toby verifies items shipped correctly →
Invoice generated through QuickBooks →
Invoice sent to customer →
Accountant collects and posts payment
```

### Supply Chain / Replenishment Workflow

```
Run rate calculations flag low-stock items →
Email notification sent to Toby →
Toby evaluates and creates Purchase Order in CRM →
PO sent to factory in China →
Custom PO app tracks quantities ordered (real-time) →
Factory produces and ships via container →
Custom Container app tracks:
    - Items, quantities, arrival dates
    - Shipping documents
    - Status: active vs. delivered →
Container arrives at warehouse →
Warehouse receives inventory →
QuickBooks updated → Syncs to CRM next morning (~11 AM) →
Inventory page shows: on-hand + on-the-water + open PO quantities
```

### Inventory Reconciliation Workflow (Annual)

```
End of year trigger →
Pull CRM inventory records →
Pull warehouse WMS reports →
Compare quantities across systems →
Identify discrepancies →
    [For each discrepancy]:
        Review original orders, transactions, and codes →
        Trace back to human error (wrong warehouse code, wrong quantity, etc.) →
        Communicate with warehouse for verification →
Manual stock adjustment in system →
Sign off on reconciled counts
```

---

## Workflow Validation Assessment

### Status: STRONGLY VALIDATED (Distribution Flow with Advanced Inventory)

| Stage | Validated? | Evidence |
|-------|------------|----------|
| Order (Sales Order) | Yes | "It will start out as a sales order. Yes." (00:04:22) — core transaction type |
| Check Stock | Yes | "CRM is synced with our QuickBooks and we have active inventory when we're placing the order." (00:04:22) |
| Warehouse Fulfillment | Yes | Orders sent to warehouse via CRM workflows for picking and shipping |
| Ship | Yes | Warehouses ship and send confirmation reports back to Toby |
| Invoice | Yes | "We upload the information that it's shipped out back to CRM, generate an invoice that goes through QuickBooks." (00:03:12) |
| Payment | Yes | Accountant collects and posts payments (00:21:14) |
| PO Subprocess | Yes | Custom PO app with real-time tracking of quantities ordered from China (00:07:09) |
| Inventory Visibility | Yes | Daily QBO sync shows per-warehouse, per-product available quantity (00:06:15) |

### Comparison to Previous Customer Calls

| Element | Europena Call | Liquid Medlock Call |
|---------|-------------|---------------------|
| Full order-to-cash confirmed | Yes | Yes — most complete workflow captured to date |
| Stock check at order entry | Implied | Explicitly confirmed with daily sync |
| Multi-warehouse | No (single DC per company) | Yes — 4 separate locations |
| Purchase order workflow | At head office | Fully integrated custom app in CRM |
| Inbound shipment tracking | Not present | Custom container app for China shipments |
| Run rates / alerts | Not present | Custom-built with email notifications |
| Invoice generation | From QuickBooks | Manual process — shipment upload → invoice |
| Distribution complexity | Low | High — 4 warehouses, international sourcing, 4 WMS systems |

**Liquid Medlock provides the most complete and advanced workflow validation of any customer call to date.** Every stage of the order-to-cash cycle is explicitly confirmed, and the inventory management depth goes well beyond what other calls have surfaced.

---

## Key Finding 1: Human Error as the Sole Remaining Pain Point

### The Core Problem

Despite months of custom development and a mature, streamlined workflow, human error at the point of data entry is the only source of inventory discrepancies.

**Toby (00:09:31):**
> "The only issue that we have found so far is humans. So, every time a human makes a mistake either in a quantity or in a skew code or listing an item incorrectly or ordering the wrong thing, errors happen. And um if I could remove the humans, it would be great."

### Error Types

| Error Type | Example | Impact |
|------------|---------|--------|
| Warehouse code typo | One-letter difference between G and Brampton warehouse codes | Inventory shows at wrong location; QuickBooks says "you don't have this item on hand" during order processing |
| Quantity entry error | Keying 10,000 instead of 100,000 on receipt | Inventory counts off by an order of magnitude; missing stock on paper |
| SKU code error | Listing an item incorrectly | Wrong product attributed to the order |

### Why This Matters for Method

The system has no validation layer to catch these errors at the point of entry. They propagate silently until they surface during order processing or annual reconciliation. This is a **platform-level gap** — no amount of customization can add input validation or anomaly detection to the data entry process.

---

## Key Finding 2: Deliberate Separation of CRM and Warehouse WMS

### The Unexpected Insight

When asked about WMS-CRM integration, Toby's response was definitive — he **doesn't want** direct integration:

**Toby (00:14:50):**
> "No, we don't want it to communicate with the CRM. We want to have our own tracking of our inventory and orders separate from the warehouses for a bunch of reasons. Um we want it to be as accurate as possible, but like we can't rely on a warehouse to say, 'Oh, no, you're not missing anything.'"

### Why This Matters

This challenges the assumption that tighter system integration is always desirable. Toby deliberately maintains **independent tracking** as a check against warehouse accuracy. The CRM serves as the operations source of truth, WMS reports are the backup, and reconciliation between the two is how they verify accuracy. This is a trust architecture, not a technical limitation.

---

## Key Finding 3: The Cost of Custom Inventory in Method

### Investment Required

Toby described the months-long development process in detail:

**Toby (00:26:11):**
> "We spent, you know, weeks and months um, here's a step, here's a step, here's what I need tied in here. And it was, okay, this is broken, this doesn't work, change it. So it really took like months and months to get to the point where we could say this is working and doing what we want."

### What They Built

| Component | Purpose |
|-----------|---------|
| QBO-CRM Inventory Sync | Daily sync showing available quantity per warehouse per product |
| Custom Container App | Track inbound shipments from China — items, quantities, dates, documents |
| Custom Purchase Order App | Real-time tracking of quantities ordered from factories |
| Inventory Dashboard | Consolidated view: on-hand + on-the-water + open PO |
| Run Rate Calculator | 12-month sales velocity and replenishment time estimates |
| Low Stock Email Alerts | Automated email notifications when items need reordering |

### Implications for Native Inventory Solution

Toby was direct about his skepticism:

**Toby (00:25:05):**
> "I don't think that anything you would roll out today would do everything that we're currently doing for our business because I know that we've integrated so many little pieces and codes and track this and track that and upload and we've worked through all of those bugs."

This is a critical insight: **customers who have already invested heavily in custom inventory won't adopt a native solution that covers less ground**. However, the native solution isn't competing for these customers — it's competing for the hundreds of MWD accounts that haven't made this investment and can't afford months of PS development.

---

## Key Finding 4: Source of Truth Tension Between CRM and QuickBooks

### The Internal Conflict

Operations (Toby) and accounting (Rey) disagree on which system is authoritative for inventory.

**Toby (00:23:02):**
> "Our accountant wants to use QuickBooks as our um as our ledger and this is the be-all and end-all and I have learned due to human error and data entry and back and forth invoicing issues... like our accountant wants to use QuickBooks and I don't care about QuickBooks. So, I guess we're always going to bang heads."

**Toby (00:22:07):**
> "Method is the source of truth for day-to-day operations and inventory. Yes. Um, however, uh, as God is a source of truth, my WMS reports from my warehouses are my backup."

### Why This Matters

This mirrors David Singletary's observation about QB and inventory systems fighting over who controls stock quantities. In Liquid Medlock's case, it manifests as an **organizational** conflict: operations trusts CRM + WMS reports, accounting trusts QuickBooks, and when numbers don't match, there's no system to arbitrate.

---

## Personas and Role Separation

| Persona | Tools Used | Responsibilities |
|---------|------------|------------------|
| Toby (Supply Chain Manager) | Method CRM (primary), QuickBooks (reference) | Entire order-to-cash workflow: sales order entry, warehouse coordination, shipment upload, invoice generation, PO management, container tracking, inventory monitoring |
| Sales Team | Method CRM | Order entry, pending order management, inventory visibility (view only) |
| Accountant (Rey) | QuickBooks (primary), Method CRM (reference) | Payment collection, revenue posting, financial reconciliation |
| Jack / Sales VP | Method CRM | Sales follow-ups, leads, marketing initiatives (not supply chain) |
| Safwan (PS Developer) | Method backend | Custom app development, integration maintenance |

**Key Insight:** Toby is essentially a **one-person supply chain department** — "I am the entire company" (00:21:14). This means the workflow is optimized for a single power user, not a team. The sales team uses CRM for inventory visibility but doesn't participate in the operational workflow.

---

## Key Quotes for Stakeholder Communication

| Theme | Quote | Timestamp |
|-------|-------|-----------|
| Human error is the only problem | "The only issue that we have found so far is humans. So, every time a human makes a mistake either in a quantity or in a skew code or listing an item incorrectly or ordering the wrong thing, errors happen. And um if I could remove the humans, it would be great." | 00:09:31 |
| Error cascade example | "When you're inputting the wrong letter code for the warehouse it'll say we have units in G when they're supposed to be and actually in Brampton. And then when you're processing orders, QuickBooks will then say, 'Oh, you don't have this item on hand.' And you're like, 'No, no, I know I do.'" | 00:10:28 |
| Reconciliation pain | "Manual adjustment, make the counts match. I don't want to talk about it anymore." | 00:11:44 |
| Magic wand request | "The end of day shipped out documents from the warehouse, I would like them to automatically upload and if not automatically generate an invoice... that's the only thing." | 00:27:59 |
| Why they built it custom | "We spent, you know, weeks and months... here's a step, here's a step... it really took like months and months to get to the point where we could say this is working and doing what we want." | 00:26:11 |
| Skepticism of general solution | "I don't think that anything you would roll out today would do everything that we're currently doing for our business because I know that we've integrated so many little pieces and codes." | 00:26:11 |
| Deliberate system separation | "We don't want it to communicate with the CRM. We want to have our own tracking of our inventory and orders separate from the warehouses... we can't rely on a warehouse to say, 'Oh, no, you're not missing anything.'" | 00:14:50 |
| Source of truth conflict | "Our accountant wants to use QuickBooks... and I don't care about QuickBooks. So, I guess we're always going to bang heads." | 00:23:02 |
| Delivery instructions need | "I want to be able to go into Shoppers Drug Mart, Shoppers Drug Mart Monton, and say, 'This location needs a tailgate. This location delivers before 2 p.m., this location needs specific items only.'" | 00:28:51 |
| Streamlined workflow satisfaction | "As a supply chain and dealing with the daily ops, I don't have any issues um with the day-to-day. It's streamlined. I like it." | 00:20:09 |

---

## Action Items

- [ ] John Miranda to send Toby the 5-minute inventory management feature priorities survey
- [ ] Evaluate automated warehouse data import (Excel → CRM) as a potential platform feature
- [ ] Document Liquid Medlock as a case study for the "ceiling of customization" — what PS can build vs. what requires platform capabilities
- [ ] Follow up on delivery instructions field request — assess if this is a native feature gap or PS customization scope
- [ ] Consider Toby's "break things" offer for future QA/testing — "If you ever want anything broken, I have a sales rep for you" (Randy)

---

## Relevance to MLP Scope

### What This Call Validates for MLP Priorities

| MLP Feature | Validation | Notes |
|-------------|------------|-------|
| **Available Inventory Visibility** (P1) | Strong | Entire custom QBO-CRM sync was built for this — "sales was coming and going do we have this, do we have that?" |
| **Multi-Warehouse Management** (P1) | Strong | 4 separate warehouse locations, inventory tracked per warehouse per product |
| **Third-Party Integration** (P1) | Moderate | They use WMS but deliberately keep it separate from CRM; Shopify used for US orders |
| **Reorder Points & Low Stock Alerts** (P2) | Strong | Custom-built run rate calculations with email alerts — validates the need and the shape of the feature |
| **Dynamic Item Management** (P2) | Moderate | Items tied to specific warehouses; pending order management via sales lead/PO status dropdowns |
| **Backorder Awareness** (P2) | Weak | Not explicitly discussed — inventory visibility at order entry handles this implicitly |
| **Item Audit Trail** (P3) | Strong | Reconciliation pain directly caused by lack of audit trail — "you have to go and track down the problem" |
| **Detailed Location-Based Tracking** (P3) | Strong | Warehouse code errors (one-letter difference) cause major inventory discrepancies |

### What This Call Reveals Beyond MLP Scope

| Gap | Evidence | Implication |
|-----|----------|-------------|
| **Automated data import from external systems** | Magic wand request — upload Excel shipment reports from 4 warehouses | Not in MLP scope but a critical distribution workflow need |
| **Input validation / error prevention** | Human error is the sole pain point in a mature system | Platform-level gap — no customization can add data validation rules |
| **Ship-to address delivery instructions** | Toby needs notes per destination that pre-populate on sales orders | Not inventory-specific but critical for distribution operations |
| **Inbound shipment / container tracking** | Built entirely as custom apps | Validates PO-to-inventory pipeline but goes beyond current MLP scope |

---

## Summary Assessment

### What This Call Provided

- The **most complete order-to-cash distribution workflow** captured across all discovery calls — every stage explicitly confirmed
- A **case study in the ceiling of Method customization** for inventory — what months of PS development can achieve and where gaps remain
- **First-party customer evidence** (not PS proxy) for multi-warehouse inventory management, run rate calculations, low stock alerts, and PO tracking
- The strongest evidence yet that **human error and data validation** is a platform gap that no amount of customization can solve
- A concrete "magic wand" request for **automated warehouse data import** — a feature that could apply broadly to distribution customers
- An unexpected insight about **deliberate system separation** — not all customers want tighter integration; some maintain independent systems as a trust mechanism
- Evidence of the **CRM vs. QuickBooks source of truth conflict** from the customer's perspective (previously only heard from Partners and PS)
- A **net-new feature request** for delivery instructions on ship-to addresses

### What This Call Did NOT Provide

- Manufacturing or production workflow validation (Liquid Medlock is pure distribution)
- Multi-user workflow patterns (Toby is the sole operational user)
- Estimate/quote stage validation (orders start as sales orders, no estimate step)
- BOM, lot tracking, or serial number requirements
- Willingness to test the native inventory solution (skeptical of general-purpose approach)
- Deep insights into the sales team's experience (Toby manages everything; sales team only views inventory)

### Bottom Line

Liquid Medlock is the most valuable discovery call to date for understanding **what a mature, deeply customized Method inventory implementation looks like in practice**. Their setup — container tracking, PO tracking, per-warehouse QBO sync, run rates with email alerts — is essentially a custom-built version of what the MLP is trying to deliver natively. This validates that the MLP features are the right features. But the call also reveals a crucial insight: **the remaining pain points (human error, no input validation, manual reconciliation, manual shipment upload) exist at the platform level, not the customization level**. These are gaps that PS can't close. For the MLP, this means the native solution doesn't need to compete with Liquid Medlock's custom build — it needs to deliver the 80% solution that the hundreds of MWD accounts *without* months of PS investment desperately need, while also addressing platform-level gaps (validation, audit trail, data import) that even the most sophisticated custom setup can't solve.

---

*Document created: February 5, 2026*
*Analysis by: Claude Code*
