# PS Discovery Call Insights: Fire Station Furniture & Fuji Mats

**Source:** Fujimats & Firestationfurniture Workflows/Customization Review — February 2, 2026
**PS Team Member:** Eric Tran (Professional Services, Method)
**Interviewer(s):** John Miranda
**Duration:** ~35 minutes

---

## Call Context

This was a discovery call with Eric Tran from the PS team to understand MWD customer workflows and customizations. Eric confirmed that the majority of his accounts fall under the MWD vertical. The call focused primarily on Fire Station Furniture (in depth) and Fuji Mats (high-level overview due to time constraints). A brief mention of SCS Automations was included as an example of manufacturing tracking within Method.

**Note:** USA Fleet Solutions was originally included in the call agenda but was excluded as Eric clarified it's a services account, not MWD.

---

## Customer 1: Fire Station Furniture

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Industry** | Fireproof furniture manufacturing |
| **Business Model** | B2B — sells to fire stations |
| **Target Market** | Fire stations, especially in states prone to wildfires |
| **Products** | Beds, dining room furniture, lockers, storage — plus custom embroidered logo furniture |
| **Team Size** | 4 people (1 sales rep, 1 operations, 2 customer support) |
| **Method Tenure** | Longtime customer |

### Core Problem Solved

> "It was really organizing all the steps into one central location where it could be managed, right? It was really an organizational issue, not really the manufacturing just because it's just fire station furniture has so many moving parts and method was kind of their central database to keep everything together in one place and track them." (00:21:11)

### Workflow Summary

```
Opportunity (project tracker)
    ↓
Estimate → Send to customer → Customer accepts
    ↓
[Optional: Proofs app for logo sign-off]
    ↓
Purchase Order (auto-created with preferred vendors)
    ↓
Activities (vendor follow-up reminders)
    ↓
Manufacturing (outside Method, tracked via activities)
    ↓
Ship to customer (tracking via memos/activities)
    ↓
Invoice → Sync to QBO → Payment collected via QBO
```

**Opportunity Stages (Customized):**
- Estimate sent
- Accepted/Approved
- Shipped
- Ordered
- Paid
- "Purchase in the future" (for delayed orders)

> "I think what we're what we're lacking a lot in the opportunities for the specific customer was that there was nothing after the deal was won right there's nothing that tracks the deal was one, right? After the deal is won, it's like what else is next, right?" (00:09:15)

### Key Customizations

| Customization | Description |
|---------------|-------------|
| **Opportunities as project tracker** | Stages extended beyond "deal won" to track post-acceptance steps (vendor contact, payment, invoicing) |
| **Proofs app** | Custom app for logo sign-off — customers approve embroidered logo designs via the portal before production |
| **Auto PO creation** | When estimate is accepted, purchase orders auto-create with preferred vendors |
| **Vendor activities** | Button creates reminders for team to follow up with vendors on parts/completion status |
| **Customer-level file storage** | Attachments saved to opportunity also save to customer level for future reference |
| **Estimate data carryover** | Customer order notes from accepted estimates automatically populate the opportunity |

### Apps Used

| App | Usage |
|-----|-------|
| **Opportunities** | Primary project tracker — highly customized |
| **Estimates** | Quote creation and customer acceptance |
| **Purchase Orders** | Auto-created from estimates with preferred vendors |
| **Invoices** | Final billing, syncs to QBO |
| **Activities** | Manufacturing/vendor follow-up tracking |
| **Proofs (custom)** | Logo design approval workflow |

### What They Don't Use

- **Sales Orders** — Eric noted sales orders are typically used as packing lists or check-and-balance documents in this industry, but Fire Station doesn't find use for them
- **Method Payment Portal** — Stopped using due to historical issues with the payment processor (pre-platform update); now collects via QBO
- **Inventory tracking in Method** — Not used
- **Shipping API** — No integration; tracking numbers manually entered in memos

### Key Quotes

On the small team enabled by automation:
> "They it's really basically method allowed them to have such a small team just because it's so much automation." (00:19:33)

On activities for manufacturing tracking:
> "The only part it's really tracked is through the activities, right? That's how they're tracking it. Like, hey, uh, headrest completed, headrest shipped, right? Sunbelt delivery, stitch pallet approved, right? That's their current way." (00:11:06)

### Workflow Validation (Order-Centric Hypothesis)

| Stage | Present? | Notes |
|-------|----------|-------|
| Quote/Estimate | Yes | Estimate created and sent from within the Opportunity |
| Sales Order | No | Not used — Eric noted they're typically packing lists in this industry, Fire Station skips them |
| Purchase Order | Yes | Auto-created with preferred vendors when estimate is accepted |
| Ship | Yes, manual | Tracked via activities and memo notes — no shipping API or native tracking |
| Invoice | Yes | Created after shipping, synced to QBO |
| Payment | Yes, via QBO | Stopped using Method portal due to historical issues; now collects through QuickBooks |

**Notable:** Fire Station Furniture is the first account across PS interviews that **skips Sales Orders entirely**. Their workflow goes Estimate → PO → Ship → Invoice with Opportunities serving as the project hub. This challenges the assumption that Sales Orders are always part of the MWD workflow — for simpler manufacturing operations with a strong Opportunity-based tracker, Sales Orders may be redundant. The Opportunity acts as both pipeline tool AND fulfillment tracker through extended custom stages.

---

## Customer 2: Fuji Mats

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Industry** | Martial arts mat manufacturing |
| **Business Model** | B2B — sells to gyms, studios, high-profile clients |
| **Scale** | Very large, famous company in the fighting world |
| **Products** | Mats for jiu-jitsu, karate, and other martial arts |
| **Notable Clients** | Joe Rogan, various high-profile fighters |
| **Shipping** | International via shipping containers |

### Workflow Summary (High-Level)

> "Their work process is hyper complicated." (00:23:40)

```
Estimate (extensive details + micro revenue dashboard)
    ↓
Customer accepts → Convert to Sales Order
    ↓
Sales Order (acts as opportunity/project tracker)
    ↓
Sales team validates → Hand off to Operations
    ↓
Operations creates PO, manages manufacturing/packing
    ↓
PO received → Ship to customer (via containers)
    ↓
Operations hands off to Invoicing
    ↓
Convert Sales Order to Invoice → Sync to QBO
```

### Key Customizations

| Customization | Description |
|---------------|-------------|
| **Sales Order as project tracker** | Functions like an opportunity — tracks handoffs between sales, operations, and invoicing |
| **Deposits on Sales Orders** | Accept payments toward sales orders BEFORE conversion to invoice (unusual practice) |
| **Estimate micro-dashboard** | Shows expected revenue for the specific customer within the estimate |
| **Containers app** | Tracks international shipping via shipping containers |
| **Inventory dashboard** | Displays QuickBooks inventory data (quantity on hand, committed, expected) — no automation, display only |
| **Multiple email templates** | Different options for showing/hiding discounts, displaying as "order" vs "estimate" |

### Unique Practices

**Deposits on Sales Orders:**
> "They take payments towards sales orders which is not a that's not that's that's not normal in the in the industry in my opinion but basically instead of paying the invoice they pay the sales they pay the deposit or they pay the sales order first then when that when that sales order gets converted invoice the payment is applied." (00:27:34)

**Container Shipping Tracking:**
> "Containers is that these are these are ships. All these are big ships. They ship these mats right from like with these like with you know with these POS with these sales orders to their country so they can pick it up." (00:31:51)

### What They Use vs. Don't Use

| Uses | Doesn't Use |
|------|-------------|
| Estimates with heavy customization | Opportunities app |
| Sales Orders as project tracker | Full manufacturing tracking in Method |
| Inventory dashboard (display from QBO) | Automated inventory management |
| Container shipping tracking (manual entry) | Shipping API integration |
| Multiple print/email templates | — |

### Workflow Validation (Order-Centric Hypothesis)

| Stage | Present? | Notes |
|-------|----------|-------|
| Quote/Estimate | Yes | Heavy customization — parent/child estimates, micro revenue dashboard, multiple email templates |
| Sales Order | Yes (central) | Core project tracker — replaces Opportunities; manages handoffs between sales → operations → invoicing |
| Purchase Order | Yes | Created during operations phase for materials procurement |
| Ship | Yes | International container shipping tracked via custom app; manual entry, no API |
| Invoice | Yes | Converted from Sales Order; deposits applied at conversion; synced to QBO |
| Payment | Yes (deposits) | Unusual practice — deposits accepted toward Sales Order BEFORE invoice conversion |

**Notable:** Fuji Mats validates the full order-centric hypothesis (Estimate → Sales Order → PO → Ship → Invoice) but with a critical twist: **payments happen before the invoice exists**. Deposits are accepted against the Sales Order (a non-posting transaction), then applied when it converts to an invoice. This is the first account to show a prepayment workflow where the financial transaction precedes the accounting transaction. Also notable: Fuji Mats bypasses the Opportunities app entirely — using Sales Orders as the project tracker instead, the inverse of Fire Station Furniture's approach.

---

## Other Account Referenced: SCS Automations

Eric briefly mentioned SCS Automations as an example of manufacturing/repair tracking within Method.

**Business:** Sign making and die making machine sales and repairs

**Custom App — "Sharpening App":**
- Takes in tool modules (cutting components) from customers for repair/sharpening
- Records: original factory length, actual length, repair results
- Emails results report to customer

> "But like it's like a custom app where they're recording if we were to generalize it to record the results of that manufacturing or of that repair so to speak, right? And that that's kind of what they use method for sometimes." (00:30:06)

**Note:** Eric emphasized this is very niche and industry-specific, not generalizable.

---

## Common Customization Requests (MWD Customers)

Eric identified the following as most common across MWD accounts:

| Request | Details |
|---------|---------|
| **Estimates app customization** | Most customized app for MWD customers |
| **Terms and conditions** | "Massive feature request" — displayed on customer portal or as separate document |
| **Tracking numbers** | Very commonly requested — visible to customer via email, portal, or print templates |

On terms and conditions:
> "That's really really they're really big on that... It's like these are your terms of accepting. Yes, right. That's huge." (00:33:33)

---

## Patterns and Insights

### 1. Project Tracking Hub — Different Apps, Same Need

Both customers need a central place to track deals through the entire lifecycle, but they use different apps:
- **Fire Station Furniture:** Opportunities (customized stages beyond "won")
- **Fuji Mats:** Sales Orders (functions like opportunities)

This mirrors patterns seen in other PS interviews (Yasar's "opportunities on steroids" concept).

### 2. Manufacturing Happens Outside Method

Neither customer tracks actual manufacturing details within Method:
- Fire Station: Activities track completion status, but no production details
- Fuji Mats: Operations handles manufacturing externally, Method tracks handoffs

> "We haven't built that way just because it's kind of been separate from their system." (00:12:21)

### 3. Small Teams Enabled by Automation

Fire Station Furniture operates with just 4 people due to heavy automation:
> "It's really basically method allowed them to have such a small team just because it's so much automation. They were able to because like otherwise we'd take several people, right?" (00:19:33)

### 4. Sales Orders Have Multiple Purposes

Eric noted sales orders serve different purposes across MWD customers:
- Packing list
- Check-and-balance document
- Internal tracking tool
- Project tracker (Fuji Mats)

> "I've seen other customers do use it though as a packing list and as an internal tool where it's like has this shipped, has that, you know, has that not shipped, right?" (00:17:22)

### 5. Inventory — QuickBooks as Source of Truth

When inventory is tracked, QuickBooks is the source:
> "If we go to Fuji Mats, we don't have an inventory system, so to speak... But it's not but it's not like no no automation. It's on ClickBook side. We're just displaying it in a way where it's more palpitable." (00:32:45)

### 6. Payment Portal Trust Issues

Fire Station stopped using Method's payment portal due to historical issues:
> "It was way back when before the new update. Like like credit cards wouldn't wouldn't apply, fees kept like things kept dropping, right? Like like payments wouldn't be recorded properly." (00:15:39)

This resulted in permanent behavior change despite the portal being fixed.

---

## Relevance to Inventory MLP

| MLP Feature | Relevance from This Call |
|-------------|--------------------------|
| **Available Inventory Visibility** | Fuji Mats has an inventory dashboard displaying QBO data — validates need for easy visibility |
| **Multi-Warehouse Management** | Not discussed — neither customer appears to have multi-location needs |
| **Stock at Order Entry** | Not explicitly mentioned, but Fire Station's auto-PO from estimates suggests need for streamlined procurement |
| **Tracking Numbers** | Commonly requested customization — currently no native field |

### Gaps Identified

| Gap | Evidence |
|-----|----------|
| **Terms and conditions** | Massive feature request — needed on portal and/or as separate document |
| **Native tracking number field** | Very commonly requested, currently handled via custom fields or memos |
| **Post-deal-won opportunity stages** | Opportunities app lacks stages for fulfillment tracking |
| **Sales Order as project tracker** | Fuji Mats uses it this way, but requires heavy customization |
| **Deposits on non-posting transactions** | Fuji Mats accepts deposits on sales orders before invoice creation |

---

## Follow-Up Actions

- [ ] Book another session with Eric Tran to go over Fuji Mats in more depth
- [ ] Explore terms and conditions feature request in more detail
- [ ] Consider how tracking numbers could be natively supported

---

*Document created: February 2, 2026*
*Analysis by: Claude Code*
