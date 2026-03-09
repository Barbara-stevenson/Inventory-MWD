# Customer Discovery Call Insights: OSAP (Patrick Kelly & Scott Kohlstrom)

**Date:** February 20, 2026
**Attendees:** John Miranda, Patrick Kelly (Customer Success Manager, OSAP), Scott Kohlstrom (General Manager, OSAP), Scott Leaver (Estimator — joined but audio failed)
**Duration:** ~27 minutes

---

## Executive Summary

This discovery call with OSAP revealed a customer using Method in a highly deliberate but narrow role: exclusively for quoting and sales orders. OSAP manufactures custom shadow boards (foam/plastic tool control boards) for aerospace, defense, and lean manufacturing customers. Their technology ecosystem is unusually sophisticated for an SMB — a proprietary custom app called "Blue Manager" manages all project data, design, and manufacturing; HubSpot handles all CRM, marketing, and service; QuickBooks Desktop Enterprise manages inventory and invoicing; and Method sits in the middle generating quotes and sales orders. **Their #1 pain is the quoting process** — project data must be manually exported from Blue Manager as a CSV and imported into Method, with no preserved customer linkages, requiring manual matching of each quote to the right customer and shipping address before pricing rules are verified. ScottK is actively building a Method API integration to automate this. Patrick's "magic wand" was two buttons instead of hundreds of clicks: one in Blue Manager to create the quote, one in Method to send it via HubSpot. The call surfaces a critical strategic risk: OSAP explicitly sees Blue Manager as their hub and Method as "the widget between the financial side of things" — if the quoting workflow gets absorbed into Blue Manager via API, Method's role could shrink further. Retention here depends on making the quoting and sales order experience indispensable.

---

## Customer Profile

| Attribute | Detail |
|-----------|--------|
| Company | OSAP |
| Industry | Custom Manufacturing (tool control shadow boards — foam and plastic) |
| Business Model | B2B custom manufacturer; sells to aerospace, defense, lean manufacturing via distributors; low-volume, high-customization (qty 1 to several hundred) |
| Parent Company | Blackstone Global — OSAP is one of 5 business units sharing accounting resources |
| QuickBooks Version | QuickBooks Desktop Enterprise |
| CRM | HubSpot (marketing, knowledge base, chatbot, tech support, ticketing, drip campaigns) |
| Core Custom App | "Blue Manager" — proprietary project management, design, and manufacturing software |
| Carrier/Shipping | FedEx and UPS apps on a dedicated shipping computer (external to Method) |
| Method Usage | Quoting and sales orders only |
| Customization Level | Moderate — complex quoting rules, copy/edit quote functionality, API integration setup; ongoing monthly work with PS developer Alex |
| Key Contacts | Patrick Kelly (Customer Success Manager), Scott Kohlstrom (General Manager — handles all software), Scott Leaver (Estimator — primary daily Method user) |
| PS Developer | Alex |

**Why this matters:** OSAP is a "Method as middleware" account — not a typical CRM-centric user. They explicitly chose HubSpot over Method for CRM and are satisfied with QuickBooks Desktop Enterprise for inventory. Their Method footprint is narrow by design, not by ignorance. This makes the quoting and sales order experience the single retention lever.

---

## How OSAP Uses Method

### Primary Use Cases

| Use Case | Details |
|----------|---------|
| Quote Generation | Import project/part data from Blue Manager (via CSV) → build quote in Method with pricing rules and customizations → send to customer |
| Sales Order Creation | Order desk converts accepted quote to sales order in Method → syncs to QuickBooks for financial processing |
| Quote Visibility for Sales Team | Sales reps can view generated quotes in Method (read-only access to track status) |
| Forecasting & Commission Reports (future) | Currently being custom-built with Alex — not yet live |

### What They Do NOT Use Method For

- **CRM** — HubSpot handles all customer relationship management, marketing, and service
- **Inventory** — Managed entirely in QuickBooks Desktop Enterprise; all part numbering and pricing originate there
- **Invoicing** — Accounting team lives in QuickBooks; refuses to migrate invoicing to Method
- **Manufacturing** — Managed in Blue Manager after a sales order is created
- **Shipping** — FedEx and UPS carrier apps used on a dedicated computer; tracking numbers never enter Method

**Key Insight:** OSAP's narrow Method usage is intentional. Method was chosen as a financial buffer — a controlled layer between their team and QuickBooks — not as an operational hub. This is a fundamentally different usage pattern than most accounts and shapes which opportunities are actionable.

---

## End-to-End Workflow (Current State)

### Quote-to-Sales-Order Workflow

```
Customer contacts OSAP with a need →
Design process begins in Blue Manager (OSAP designs the shadow board) →
Design approved → Quote needed →
    Blue Manager exports project + part data as CSV (manual) →
    CSV imported into Method (manual) →
    Estimator (Scott L.) manually links correct customer and shipping address →
    Estimator manually verifies pricing rules →
    Quote reviewed and finalized →
Quote sent to customer [via HubSpot — separate manual step] →
Customer approves and sends Purchase Order →
Order desk generates Sales Order in Method (linked to QuickBooks) →
Manufacturing handed back to Blue Manager →
Order manufactured and shipped →
    [Shipping on separate computer via FedEx/UPS apps — manual tracking numbers] →
Order complete → Invoicing and payments handled in QuickBooks by accounting team
```

### Future State (ScottK's API Integration Vision)

```
Customer approved → Design finalized in Blue Manager →
API call pushes project + part data directly into Method →
Quote auto-generated in Method (no manual CSV step) →
One button in Method confirms and routes quote to HubSpot →
HubSpot sends quote to customer with communication record →
Purchase Order received → Sales Order generated →
[Downstream same as current]
```

### Key Workflow Gaps (Current State)

```
Gap 1: Blue Manager → Method [manual CSV export/import; no customer linkage preserved]
Gap 2: Method → HubSpot [manual; no native quote delivery; no communication record in Method]
Gap 3: Method → Shipping [no carrier integration; tracking numbers never captured]
Gap 4: Method → QuickBooks for invoicing [blocked by accounting team; not in Method at all]
```

---

## Workflow Validation Assessment

### Status: PARTIALLY VALIDATED (Custom Manufacturer — Quote-to-Order Flow Only)

| Stage | Validated? | Evidence |
|-------|------------|----------|
| Design / Estimation (pre-quote) | Yes | Blue Manager handles all design and BOM-equivalent project data before quoting begins |
| Quote Generation | Yes | Core use case — "we do all our estimating there" (00:07:32) |
| Quote Delivery | Partial | Quote created in Method but delivered via HubSpot — no native delivery mechanism |
| Sales Order | Yes | "Our order desk will then go back to Method and generate a sales order from that which again it's connected right to QuickBooks." (00:07:32) |
| Manufacturing | Out of scope | Managed in Blue Manager after SO is created — Method not involved |
| Shipping | No | Entirely external — FedEx/UPS apps on separate computer |
| Invoice | No | Accounting team lives in QuickBooks; refusing to migrate |
| Payment | No | Collected and posted in QuickBooks by shared accounting team |
| Inventory Management | No | Controlled entirely in QuickBooks Desktop Enterprise; OSAP may move to Blue Manager eventually |

### Comparison to Other Customer Calls

| Element | Liquid Medlock (Toby) | OSAP (Pat/Scott) |
|---------|----------------------|------------------|
| Method as operational hub | Yes — full order-to-cash | No — quoting/SO layer only |
| CRM used in Method | No | No (HubSpot) |
| Inventory in Method | Yes (custom QBO sync) | No (QBDE) |
| QuickBooks version | QBO | QBDT Enterprise |
| Invoicing in Method | Yes | No (accounting refuses) |
| Shipping in Method | Manual upload workaround | Entirely external |
| PS developer dependency | High (Safwan) | High (Alex) |
| Churn risk profile | Satisfied but narrow gaps remain | Narrow footprint; Blue Manager could absorb quoting |
| Magic wand request | Automated warehouse shipment upload | Two-button quote creation + delivery |

---

## Key Finding 1: Quoting Is a Painful, Multi-Step Manual Process With Too Many Error Points

### The Core Problem

Every quote at OSAP begins in Blue Manager with project and part data. Getting that data into Method requires a manual CSV export and import — and when it arrives, it's unlinked. The estimator (Scott Leaver) must manually identify the correct customer record and shipping address for each quote, then verify that all pricing rules applied correctly. There are too many steps and too many places for mistakes.

**ScottK (00:18:49):**
> "It's such a tedious task to manually export our data CSV, get it into Method as a little bit of a process. And the customer information is not linked right now. So once it's in the system then Scott comes in, looks at all these new quotes, and now has to figure out the right customer, the right shipping address. That takes time. So this is our first immediate thing to fix."

**Patrick Kelly (00:16:26):**
> "Our focus has been all the things — looking hard at all the things that we do manually that take time and seeing if there's a reasonable way to automate pieces of that... every time we humans touch something there's a risk."

### Why the Workaround Exists

OSAP offloads some quoting to a design team in India to manage the volume. But this adds coordination overhead without solving the root problem — the data still travels through the same error-prone manual path before Scott can finalize and send it.

### Why This Matters for Method

This is not a niche problem. Any custom manufacturer or company using proprietary software alongside Method faces the same structural gap: Method has no native way to receive structured data from an external system and automatically generate a quote. The API enables this, but requires engineering investment most customers can't make.

---

## Key Finding 2: Method Is the "Widget" — Blue Manager Is the Hub

### The Explicit Signal

ScottK offered an unusually clear articulation of how OSAP thinks about Method in their stack:

**ScottK (00:11:56):**
> "I think our software is going to end up being the hub and you're the widget between the financial side of things."

He also noted they may eventually move inventory control into Blue Manager as well — reducing Method's role further.

### Why This Is a Retention Risk

If ScottK successfully builds the API integration to auto-generate quotes in Method from Blue Manager, the daily friction that currently keeps Scott Leaver embedded in Method will decrease. If Blue Manager can also absorb inventory tracking and eventually trigger sales orders directly, Method's role could shrink to a pass-through with minimal user interaction. The retention play is making Method's quoting experience so good — reliable, fast, accurate — that rebuilding it inside Blue Manager creates more work than it's worth.

### The Positive Signal

ScottK is investing real engineering effort to integrate *with* Method, not replace it. He's building via the API because Method offers customization and financial integration that Blue Manager and QuickBooks alone can't replicate. This is a window — not a guarantee.

---

## Key Finding 3: Method CRM Was Evaluated and Rejected — HubSpot Is Deeply Entrenched

### What HubSpot Does That Method Doesn't

Patrick Kelly articulated the specific reasons HubSpot won:

**Patrick Kelly (00:05:37):**
> "We're using it on the marketing side. We're using it to manage some of our web pages. We use it to manage our knowledge base. We have a chatbot on our website connected to our knowledge base... we use it on the service side for tech support and ticketing and tracking our activities around there... marketing uses the database for drip campaigning and things like that."

### The Investment Barrier

OSAP has significant investment in HubSpot — web pages, knowledge base content, chatbot training, ticketing workflows, campaign history. ScottK acknowledged they haven't been keeping up with Method's new features. But HubSpot is entrenched enough that awareness alone won't shift them. A genuine CRM recapture here would require Method to match HubSpot's service/support tooling and marketing automation capabilities.

### Why This Is Broader Than OSAP

This is the first customer call where a direct end customer explicitly walked through *which* CRM capabilities caused them to choose a competitor over Method. It's not vague dissatisfaction — it's knowledge base, chatbot, ticketing, and drip campaigns. These are specific gaps that likely affect other accounts who never mentioned it because they weren't asked.

---

## Key Finding 4: Accounting Teams Are the Invoicing Blocker — Pattern Confirmed Again

### The Specific Barriers at OSAP

**ScottK (00:22:14):**
> "They told me: one is all the payment things, credit card, everything else has all been set up in there. They also said that they live in there. They don't like what's this Method thing? They don't live in Method. So that's where I keep getting all the push back... they're basically saying everything works on my side. I don't know why I need to change."

### The Organizational Complexity

OSAP is owned by Blackstone Global with 5 shared business units. The accounting team is a shared resource across all 5. This means a single BU requesting a system change for invoicing has almost no organizational leverage — the change would need to benefit (or at minimum not disrupt) all 5 units to get approval.

### Pattern Significance

This is the third consecutive customer interview confirming that accounting teams won't migrate invoicing from QuickBooks to Method. Singletary raised it as a systemic implementer problem. Liquid Medlock showed it as an internal org conflict. OSAP shows it amplified by multi-BU shared accounting. This is not a product gap that a single feature will close — it's a trust and change management problem requiring a different strategy (possibly: prove Method invoicing works for operations first, then invite accounting teams to adopt it on their terms).

---

## Key Finding 5: PS Developer Alex Is a Significant Retention Anchor

### The Strength of the Relationship

ScottK was unusually emphatic about Alex's impact:

**ScottK (00:23:17):**
> "I think you solved it by giving us Alex, seriously... We'll ask for something and we're so used to 'we'll get back to you.' No. Bam. He fixes it right in front of you. It's just crazy. I think that changed it from night to day."

Alex has fixed complex quoting rules, built the copy/edit quote feature, helped configure the API, and provides ongoing monthly support. He is described as a "whiz" who understands their customization requirements at a deep level.

### The Risk

OSAP's satisfaction with Method is substantially tied to Alex. If Alex leaves the PS team, becomes unavailable, or the monthly engagement becomes cost-prohibitive, the relationship is at risk. The underlying product experience — without Alex's ongoing customizations — is not where it needs to be.

---

## Personas and Role Separation

| Persona | Tools Used | Responsibilities |
|---------|------------|-----------------|
| Scott Kohlstrom (General Manager) | Blue Manager, Method API, HubSpot, QuickBooks | Software strategy, API integration, overseeing all systems; growth and efficiency initiatives |
| Patrick Kelly (Customer Success Manager) | HubSpot (primary) | Customer success, service/ticketing, marketing, process improvement, systems consolidation |
| Scott Leaver (Estimator) | Method (primary daily user), Blue Manager | Quote creation, sales order generation — the person most affected by quoting friction |
| Order Desk / Production Coordinator | Method | Sales order creation, production coordination |
| Sales Team | Method (view-only) | Viewing generated quotes |
| Accounting Team (shared, Blackstone Global) | QuickBooks Desktop Enterprise | Invoicing, payments, financial reporting |

**Key Insight:** Scott Leaver is the most important Method user at OSAP — he lives in the quoting workflow every day — but he couldn't be heard on this call. Follow-up directly with Scott Leaver would provide the richest operational detail about daily quoting pain.

---

## Key Quotes for Stakeholder Communication

| Theme | Quote | Timestamp |
|-------|-------|-----------|
| Method as middleware, not hub | "I think our software is going to end up being the hub and you're the widget between the financial side of things." | 00:11:56 |
| Quoting pain | "It's such a tedious task to manually export our data CSV, get it into Method... the customer information is not linked right now. So once it's in the system then Scott comes in, looks at all these new quotes, and now has to figure out the right customer, the right shipping address. That takes time." | 00:18:49 |
| Too many error points | "And certainly there's too many points where mistakes happen." | 00:18:49 |
| Human error as the enemy | "Every time we humans touch something there's a risk. So we're looking hard at all those touch points where we're having to do something manually and seeing if there's a reasonable amount of effort to get it to go automatically." | 00:16:26 |
| Magic wand | "The perfect world for me would be... a button gets pushed in Blue Manager which creates the quote and then a button gets pushed in Method to confirm it, which sends it out via HubSpot. So there's a record that it went out with the quote attached to it and all of that is the pressing of two buttons instead of today, which would require a few hundred clicks." | 00:23:17 |
| Accuracy trust barrier | "We would have to trust it... the numbers are important, they impact all kinds of things right, and our quotes need to be right... if we make a mistake it costs money." | 00:24:32 |
| Why accounting won't move | "They don't like what's this Method thing? They don't live in Method. So that's where I keep getting all the push back... they're basically saying everything works on my side. I don't know why I need to change." | 00:22:14 |
| Alex as retention anchor | "I think you solved it by giving us Alex, seriously... Bam. He fixes it right in front of you. It's just crazy. I think that changed it from night to day." | 00:23:17 |
| Quoting identified as top priority | "Quoting is pretty painful for us. It's a time consuming process. So we're looking to get efficient there. And then the next things I think would be better inventory control and then shipping." | 00:13:08 |
| HubSpot capabilities driving decision | "We use it on the marketing side... we use it to manage our knowledge base. We have a chatbot on our website... we use it on the service side for tech support and ticketing and tracking our activities... drip campaigning." | 00:05:37 |

---

## Action Items

- [ ] Follow up with Scott Leaver (Estimator) directly — he's the daily Method user most affected by quoting friction; his voice was missing from this call
- [ ] Document OSAP as a "Method as middleware" case study — this usage pattern may be more common than previously understood
- [ ] Evaluate API-level quote generation as a use case for Method's developer platform — ScottK is building this himself, which signals demand
- [ ] Consider how Method's quoting experience needs to differentiate from Blue Manager + HubSpot to remain indispensable
- [ ] Log HubSpot CRM gap evidence (knowledge base, ticketing, chatbot, drip campaigns) with the Core CRM team — this is specific competitive intelligence
- [ ] Explore whether Method invoicing adoption path can be designed for accounting-resistant accounts — OSAP, Liquid Medlock, and Singletary all point to the same blocker
- [ ] Invite Pat and ScottK to inventory testing as agreed — they expressed openness to participating

---

## Relevance to MLP Scope

### What This Call Validates for MLP Priorities

| MLP Feature | Validation | Notes |
|-------------|------------|-------|
| **Available Inventory Visibility** (P1) | Weak | Inventory managed in QBDT Enterprise, not QBO. Method pulls pricing/part data from QBDT but doesn't display inventory counts to users. |
| **Multi-Warehouse Management** (P1) | Not validated | OSAP has a single manufacturing site; not a multi-warehouse distributor |
| **Third-Party Integration** (P1) | Partial | OSAP uses QBDT Enterprise (not QBO) — integration scope is different from the standard QBO connector |
| **Reorder Points & Low Stock Alerts** (P2) | Not validated | Inventory managed outside Method entirely |
| **Dynamic Item Management** (P2) | Moderate | Part numbers and pricing originate in QBDT and are pulled into Method quotes — this linkage is where the friction lives |
| **Backorder Awareness** (P2) | Not discussed | |

### What This Call Reveals Beyond MLP Scope

| Gap | Evidence | Implication |
|-----|----------|-------------|
| **External data import for quote generation** | CSV export from Blue Manager → manual import into Method | A structured import or API endpoint for quote creation would eliminate OSAP's #1 pain point and likely apply to other manufacturers using proprietary software |
| **Native quote delivery with communication record** | Quote created in Method but delivered via HubSpot separately | No CRM communication record tied to quote in Method; this is a gap that makes HubSpot sticky |
| **CRM: knowledge base, ticketing, marketing automation** | HubSpot chosen specifically for these features | Method CRM is not competitive for service-heavy or marketing-active B2B companies |
| **Invoicing trust / adoption path** | Accounting team refuses to leave QuickBooks despite leadership wanting to consolidate | Product gap isn't features — it's a trust and change management problem requiring a different approach |

### Important Technical Note

OSAP uses **QuickBooks Desktop Enterprise**, not QuickBooks Online. The inventory MLP is being designed around the QBO integration. OSAP's inventory needs (and the QBO connector) may not align. This is worth flagging if OSAP is considered for any inventory testing or rollout.

---

## Summary Assessment

### What This Call Provided

- A **"Method as middleware" use case** — the first customer to explicitly describe Method as a widget in their stack rather than the operational hub
- **Specific quoting workflow pain** — the most detailed description of the manual CSV import problem and the downstream manual matching work it creates
- **Explicit "magic wand" request** that reveals the full desired quote workflow: Blue Manager → auto-create quote in Method → send via HubSpot in two button pushes
- **First-hand CRM competitive intelligence** — specific HubSpot features (knowledge base, chatbot, ticketing, drip campaigns) that caused a customer to choose a competitor over Method CRM
- **Third confirmation** of the accounting team invoicing blocker pattern, with added organizational complexity (Blackstone Global shared accounting across 5 BUs)
- **Clear strategic risk signal** — ScottK directly stated Blue Manager will be the hub; Method is the widget. If quoting friction isn't resolved, this account could reduce or eliminate their Method footprint
- **PS retention dependency** — Alex is the most important retention factor named; satisfaction is substantially relationship-based

### What This Call Did NOT Provide

- Scott Leaver's perspective — the actual daily Method user couldn't be heard; his experience would be the richest operational signal
- Inventory workflow detail — OSAP doesn't use Method for inventory at all, and uses QBDT Enterprise rather than QBO
- Insights on the sales team's day-to-day experience beyond view-only quote access
- Manufacturing workflow detail (all in Blue Manager, out of scope for Method)
- Pricing for their PS engagement or ARR context

### Bottom Line

OSAP is a retention risk that looks like a satisfied customer. They say they're happy with Method for what they use it for — and that's true, with Alex's help. But their footprint is narrow, their hub is Blue Manager, and ScottK is actively building an integration path that could reduce Method's role over time. The lever to prevent this is **making the quoting experience so seamless and trustworthy that displacing it costs more than it's worth**. The CSV import gap is fixable. The customer linkage gap is fixable. The "send quote via HubSpot" problem is harder — it points to a broader need for Method quotes to be deliverable with communication tracking. Solving the quoting flow convincingly could also open the door to invoicing adoption, since the same trust barrier (accuracy, reliability, accounting team buy-in) applies to both.

---

*Document created: February 20, 2026*
*Analysis by: Claude Code*
