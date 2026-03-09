# PS Discovery Call Insights: Brown Safe & Kier Fabrication (with Yasar Zaman)

**Date:** January 28, 2026
**Attendees:** John Miranda, Yasar Zaman (PS), Elaine Chow, Barbara Stevenson
**Duration:** ~51 minutes

---

## Executive Summary

This PS discovery call with Yasar Zaman reviewed two MWD customer accounts — Brown Safe (safe manufacturing) and Kier Fabrication (fabric/equipment manufacturing) — to understand their workflows, customizations, and pain points. Both companies are **manufacturers who manage production outside of Method**, using Method primarily for transaction logging (estimates, invoicing) and custom project/job tracking apps. The call also surfaced **cross-cutting patterns across Yasar's 10-30 MWD accounts**, including the universal need for a simplified project hub ("opportunities on steroids"), custom pricing levels, multi-location inventory management, and automation/reminders. A key finding is that **both companies built custom apps to replace the Opportunities app**, which MWD customers find too bloated for their needs.

---

## Interviewee Profile

| Attribute | Detail |
|-----------|--------|
| Name | Yasar Zaman |
| Role | Professional Services (PS) at Method |
| MWD Accounts Customized | Estimated 10-30 |
| Notable Clients | Brown Safe, Kier Fabrication, Parkmark Badges, Tripid Rocks |
| Key Partner Collaboration | John Sandy (job costing module) |

**Important Context:** Yasar is an internal PS team member, not a partner or customer. His observations are based on hands-on customization work across multiple MWD accounts. This gives him direct visibility into what customers actually need vs. what Method provides out of the box.

---

## Customer 1: Brown Safe

### Company Profile

| Attribute | Detail |
|-----------|--------|
| Industry | Manufacturing (safes, locks, security deposit boxes) |
| Customer Type | B2B and B2C |
| Method Usage | Estimates, invoicing, installation project tracking, customer/vendor communication |
| Production Management | Base 44 (external AI-based tool) |
| Tax Integration | Avalara (not QuickBooks) |
| Account Age | 5-6 years on Method |

### Workflow

```
Create Estimate → Email to customer → Customer reviews on portal →
Customer accepts & signs off → Invoice auto-generated (posted to Avalara) →
    [If installation needed]:
        Installation project auto-created → Vendor/installer assigned →
        Communication hub (portal) between customer, installer, Brown Safe →
        Installer completes work → Payment collected
    [If no installation]:
        Ship safe → Wait for payment
```

**Production (outside Method):**
```
Invoice approved → Information sent to Base 44 →
Base 44 parses dimensions/specs → Determines materials needed →
Checks stock → Orders missing materials → Production schedule runs
```

### Key Details

**Estimate Stage:**
- Workflow begins with an estimate — this is the starting point (00:02:30)
- Uses predefined templates for safe configurations
- Avalara handles tax calculation, not QuickBooks (00:08:48)
- Estimate is for finished goods (the whole safe), not raw materials/components (00:12:22)

**Installation Project (Custom App):**
- Created automatically when installation is required (00:02:30)
- Functions as a communication hub / work order between customer and installer (vendor) (00:04:29)
- Installers are external subcontractors, not Brown Safe employees (00:05:38)
- Uses Method's portal for communication — customer and installer can see status, reschedule, log complaints (00:11:25)
- Built as a custom app because the standard work orders app wasn't sufficient — subcontractors don't warrant dedicated Method user seats (00:16:27)
- App predates the work orders feature in Method (00:17:24)

**Production Gap:**
- Brown Safe tried to use Method for production management but the person on that project left the company (00:06:33)
- They replaced that portion with Base 44, an AI-based app builder
- Yasar is now trying to integrate Method → Base 44 by sending invoice data to trigger the production schedule (00:07:42)

**Shipping:**
- No shipment tracking in Method — "no record of a shipment being sent out from Method that's captured other than an activity" (00:12:22)
- They handle shipping externally

### Workflow Validation (Order-Centric Hypothesis)

| Stage | Present? | Notes |
|-------|----------|-------|
| Estimate/Quote | Yes | Starting point of workflow — explicitly confirmed |
| Customer Approval | Yes | Via portal — accept and pay deposit or just accept |
| Invoice (auto from estimate) | Yes | Auto-generated on customer acceptance |
| Production | Yes, but external | Handled in Base 44, not Method |
| Installation/Shipping | Yes | Either installation project or ship directly |
| Payment | Yes | Collected after installation or after shipping |
| Sales Order | No | Not used — goes directly from estimate to invoice |
| Purchase Order | Yes, but external | Created by accounting person in QuickBooks, not Method (00:13:17) |

**Notable:** Brown Safe skips the Sales Order stage entirely. Their flow is Estimate → Invoice (auto) → Production → Ship/Install → Payment. This is a different pattern from the standard order-centric hypothesis.

---

## Customer 2: Kier Fabrication

### Company Profile

| Attribute | Detail |
|-----------|--------|
| Industry | Manufacturing (fabrics, equipment, various materials) |
| Customer Type | Primarily B2B, some B2C via website |
| Method Usage | Estimates (with approval flow), sales orders, jobs app, invoicing |
| Production Management | External (not in Method) |
| Inventory Tracking | Not tracked in Method (00:22:29) |

### Workflow

```
Create Estimate → Internal approval → Customer approval →
Sales Order auto-created from approved estimate →
Job created per item on the sales order →
    [Each job = a to-do task: production, assembly, or installation] →
    Jobs managed with timestamped notes and task tracking →
Job completed → Refer back to Sales Order →
Invoice (full or partial) → Payment
```

### Key Details

**Estimate + Approval Flow:**
- Two-stage approval: internal first, then customer (00:17:24)
- Once approved, estimate auto-converts to a sales order

**Jobs App (Custom):**
- One job per line item on the sales order (00:18:25)
- Jobs are to-do tasks — could be installation, production, or assembly
- Each job pulls information from the sales order
- Timestamped notes for tracking progress
- Related jobs for the same sales order are visible from each job
- Invoicing only happens after job completion (00:21:20)

**Production Tracking Workaround:**
- "Weeks in production" and "ship date" fields are calculated by a daily routine that runs once per morning (00:22:29)
- To get real-time numbers, admin must click an "update" button that recalculates all 280+ jobs — which is slow
- This is the closest they get to production tracking in Method

**Purchase Orders:**
- Kier Fabrication uses purchase orders created from scratch in Method, but how they fit into the overall process is not fully explored (00:21:20)

**Website Orders (Future):**
- Customers can order on their website, but it's not connected to Method yet (00:20:24)
- Future goal: have website orders flow into Method

### Workflow Validation (Order-Centric Hypothesis)

| Stage | Present? | Notes |
|-------|----------|-------|
| Estimate/Quote | Yes | Starting point, with two-stage approval |
| Sales Order | Yes | Auto-created from approved estimate |
| Job/Production | Yes (tracking only) | Per-item jobs as to-do tasks, actual production external |
| Invoice | Yes | Only after job completion — full or partial |
| Payment | Implied | End of workflow |
| Purchase Order | Yes | Used somewhere in process, details not explored |

**Notable:** Unlike Brown Safe, Kier Fabrication DOES use the Sales Order stage. Their flow includes the Estimate → Sales Order → Job → Invoice sequence, which is closer to the order-centric hypothesis. The Estimate stage is validated here with a clear approval workflow.

---

## Cross-Cutting Patterns Across MWD Accounts (Yasar's Observations)

### Pattern 1: The "Opportunities on Steroids" Need

The strongest signal from this call. MWD customers consistently need a **central hub for all project-related information** — transactions, to-do lists, inventory, custom fields — but the Opportunities app is too bloated.

**Yasar (00:25:39):**
> "At the end of the day they need a place to manage everything. A central place... it's kind of like an opportunity but it's more open than an opportunity. It's not just housing the transactions and the interactions, but also here's all the custom stuff. Here's all the inventory that's related, all the things that we need to do, the to-do list, everything like that all in one place. It's kind of like opportunities on steroids."

### Pattern 2: Opportunities App Has Too Much Bloat

MWD customers consistently reject the Opportunities app because of mandatory fields they don't need.

**Yasar (00:38:14):**
> "The problem with opportunities is you need a close date. Like why do you need a close date? We don't know when this opportunity is going to close. Or having stages, probabilities... there's a lot of bloat in an opportunity that prevents a user from going into it and finding it appealing for them."

> "A lot of the common customizations revolve around can we just have a separate app that just gives us what we want."

Both Brown Safe (installation project app) and Kier Fabrication (jobs app) built custom apps to replace Opportunities.

### Pattern 3: Sales Orders Are the Common Transaction Type

**Yasar (00:27:42):**
> "I would say so. Whenever I get that kind of distinction of someone made an order, I always push for a sales order."

Distinction between estimate and sales order:
- **Estimate:** You reach out to the customer — "Here's what I can offer you"
- **Sales Order:** Customer reaches out to you — "Hey, I want 100 boxes of these"

### Pattern 4: Production Happens Outside Method

Both Brown Safe and Kier Fabrication manage production externally. This is a pattern, not an exception.

### Pattern 5: Shipping Happens Outside Method

Customers typically handle shipping outside of Method, using Method only to generate documents (release labels, packing slips) (00:40:08).

**Yasar:** "I don't think people ask... like I've never heard about shipping to be honest. It's more so like can Method create the things that I need to then ship it out." (00:40:59)

### Pattern 6: Barcode Scanning Is a Blocker

Pick and pack processes are difficult because Method doesn't support barcode scanning (00:40:59).

**Yasar:** "I promise you I tried everything. I promise you." (00:41:52)

---

## Common Customizations for MWD Clients

| Customization | Frequency | Details |
|---------------|-----------|---------|
| Custom project/job apps | Very common | Replaces bloated Opportunities app with focused project hub |
| Custom price levels (QBO/QBDT) | Frequent request | Customer-level or item-level pricing rules with automatic discount application |
| Advanced inventory management | Common | Multi-location item tracking with quantity on hand calculations |
| Automation / reminders | #1 request across all industries | Estimate reminders, invoice reminders, order date alerts |
| Release labels / packing slips | Occasional | Generating shipping documents from sales orders |

### PS Customization Catalog

Yasar revealed that the PS team maintains a **customization catalog** — a list of pre-built, reusable customizations that can be deployed to customer accounts. Examples:
- Add subtotal on invoices (0.5 hours)
- Custom price levels for QBO/QBDT
- Advanced inventory management
- Estimate reminders (3 hours)

**Limitation:** The catalog doesn't show which industry/account type each customization is for, making it hard to identify MWD-specific patterns without manual lookup (00:37:03).

---

## Yasar's "Wish on a Star" for Developers

**Yasar (00:46:18):**
> "If you can allow the user to make the app really easily in a sense of customizing it to fit their industry... Hey, what do you need to house a project? Do you need purchase orders? Do you need estimates? All that and then it just adds it to the screen for you... In a perfect world, I would want the customers to be able to select this is what I need, these are the apps I need, and then it just plops everything on the screen."

This is essentially a **configurable project hub** — a modular app where customers choose which components they need (POs, estimates, dates, to-do lists) and it assembles a custom view. It directly addresses the "opportunities on steroids" pattern.

---

## Workflow Comparison: Brown Safe vs. Kier Fabrication

| Element | Brown Safe | Kier Fabrication |
|---------|------------|------------------|
| Starting point | Estimate | Estimate (with two-stage approval) |
| Sales Order | Not used | Auto-created from approved estimate |
| Project tracking | Custom installation project app | Custom jobs app (per line item) |
| Production | Base 44 (external) | External (not tracked) |
| Invoicing | Auto from estimate acceptance | After job completion |
| Shipping | External, no Method record | External, "weeks in production" + "ship date" calculated daily |
| POs | In QuickBooks, not Method | Created in Method, integration unclear |
| Custom app purpose | Communication hub (customer ↔ installer) | To-do/task management per order item |

---

## Key Quotes for Stakeholder Communication

| Theme | Quote | Source |
|-------|-------|--------|
| Central project hub need | "At the end of the day they need a place to manage everything... it's kind of like opportunities on steroids." | Yasar (00:25:39) |
| Opportunities bloat | "Why do you need a close date? We don't know when this opportunity is going to close... there's a lot of bloat in an opportunity that prevents a user from going into it." | Yasar (00:38:14) |
| #1 feature request | "That's probably like the number one thing that I've always been asked for is automations." | Yasar (00:42:46) |
| Barcode scanning frustration | "I promise you I tried everything. I promise you." | Yasar (00:41:52) |
| Configurable app wish | "In a perfect world, I would want the customers to be able to select this is what I need, these are the apps I need, and then it just plops everything on the screen." | Yasar (00:47:30) |
| Production outside Method | "That entire production schedule happens outside of Method." | Yasar (00:13:17) |
| Inventory ask from MFG | "This is something that a lot of customers that are in that business kind of ask for is like managing your inventory in different locations." | Yasar (00:36:06) |

---

## Action Items

- [ ] Yasar Zaman to review older MWD accounts for workflow similarities and share findings with John Miranda
- [ ] Explore John Sandy's job costing module progress (uses jobs app + upcoming invoice summaries)
- [ ] Evaluate configurable project hub concept against current Opportunities app limitations

---

## Relevance to MLP Scope

### What This Call Validates for MLP Priorities

| MLP Feature | Validation | Notes |
|-------------|------------|-------|
| **Available Inventory Visibility** (P1) | Moderate | Yasar built multi-location inventory customization; manufacturing customers ask for it frequently |
| **Multi-Warehouse Management** (P1) | Moderate | PS catalog includes multi-location inventory management as a common customization |
| **Third-Party Integration** (P1) | Weak | Brown Safe uses Base 44 for production; integration is being attempted but not inventory-specific |
| **Dynamic Item Management** (P2) | Moderate | Custom price levels is a frequent customization — relates to how items behave in transactions |

### What This Call Reveals About MWD Workflow Patterns

1. **The Estimate stage IS part of MWD workflows** — both companies start there. This is the first call that clearly validates the Quote/Estimate stage.
2. **Sales Orders are used when the customer initiates** — Kier Fabrication uses them; Brown Safe skips them. The distinction depends on who initiates the transaction.
3. **Production is consistently outside Method** — this is a pattern, not an exception. Method's role in MWD is pre-production (estimating, ordering) and post-production (invoicing, payment).
4. **The Opportunities app is actively rejected by MWD customers** — they build custom apps instead. This has implications for how any project/job tracking feature is designed.

---

## Summary Assessment

### What This Call Provided

- Two detailed manufacturing workflows showing how MWD customers actually use Method
- First clear validation of the **Estimate stage** in MWD workflows (absent from Singletary and Europena calls)
- A strong pattern signal: **MWD customers need a simplified, configurable project hub** — not the Opportunities app
- Confirmation that **production and shipping happen outside Method** for manufacturers
- PS team perspective on **the most common MWD customizations** (price levels, inventory, automation)
- Insight into the PS **customization catalog** as a data source for common needs

### What This Call Did NOT Provide

- Direct customer voice (this is PS perspective, not end-customer interviews)
- Distribution/wholesale workflow (both companies are manufacturers)
- Deep inventory management requirements (inventory tracking not used by either customer)
- Detailed purchase order workflows

### Bottom Line

This call is most valuable for its **cross-cutting patterns** rather than the individual customer stories. The consistent finding that MWD customers build custom apps to replace Opportunities, combined with Yasar's "wish on a star" for a configurable project hub, points to a significant product gap. For the inventory MLP specifically, the key takeaway is that **manufacturing customers manage production and materials outside Method** — the MLP's inventory features will serve them at the transaction boundary (knowing what's in stock when creating estimates/orders) rather than during the production process itself.

---

*Document created: January 28, 2026*
*Analysis by: Claude Code*
