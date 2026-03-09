# Opportunity Solution Tree: GT Simulators (Matt Shade, PS)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** SPK Associates Workflow/Customization Review — January 29, 2026
**Interviewee:** Matt Shade Silver (Professional Services, Method)
**Interviewer(s):** John Miranda, Elaine Chow, Barbara Stevenson
**Customer Discussed:** GT Simulators (medical device manufacturing — compression dummies, CPR training equipment)

**Important Context:** Matt is an internal PS team member with hands-on experience customizing Method for ~22 MWD accounts. His opportunities are **proxy evidence** — observed patterns across multiple customers, not a single customer's firsthand story. However, Matt built everything for GT Simulators from scratch, giving him deep firsthand knowledge of this account's specific pain points and workarounds.

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: Invoice quantities don't update in real-time when changes happen

Once an invoice is created, the quantity captured doesn't change — even when additional invoices are created or items ship. This means the "invoiced" column on a Sales Order shows stale data. For GT Simulators, this is a critical problem because their prepayment model requires inventory to update live as items ship.

**Evidence:**
> "How it was originally set up is you create a invoice and then that's what the invoice quantity was. It can't update. So if you change that amount or you invoice another one, it doesn't update." (00:41:59)

> "I said to them it should be like the live current amount how that product is invoiced for the specific line item. So like you actually know what's invoiced and what's shipped." (00:41:59)

**Child opportunities:**
- **1a.** Can't see real-time invoiced quantities per line item on a sales order
- **1b.** Workaround requires custom "ship" column to manually track what's been shipped (00:41:59)
- **1c.** For prepayment models, maintaining total consistency while tracking individual item shipments requires a complex invoicing workaround — the invoice is restructured each time items ship so the total stays constant while inventory updates (00:40:07)

---

## Opportunity 2: No place to manage shipments — Sales Orders have become the workaround

Sales Orders are the most customized app across all of Matt's accounts because Method has no dedicated shipment management area. GT Simulators uses the Sales Order as their project hub for tracking fulfillment.

**Evidence:**
> "Sales orders. Well, more more people again... they need a way to man... this manages all the shipments where we don't have a place to manage it." (00:43:37)

> "The sales order is kind of like where the magic is because this is kind of like the project manager thing because you already have the invoiced part of it but now the invoiced will show yes they paid for it but it doesn't properly like know what progress it is." (00:41:11)

**Child opportunities:**
- **2a.** No native way to track what's been shipped vs. what's outstanding on an order
- **2b.** Fulfillment status (packed, partially shipped, fulfilled) requires HTML customization to visualize (00:40:07)
- **2c.** Sales Orders weren't designed as shipment trackers — they're being forced into a role they weren't built for

---

## Opportunity 3: Partial shipments are the norm but tracking them requires workarounds

GT Simulators regularly ships partial orders — items go out as they're ready, not all at once. This is especially complex with international shipping (they ship worldwide, including Africa and Asia). But Method has no native partial shipment tracking.

**Evidence:**
> "Biggest thing with this is partial shipping. Got to think about that. It happens all the time where it's like when things are ready, that's you ship it. Like that's like think about Amazon. You order 10 things, they don't all come together. They're coming from different places." (00:42:48)

> Yellow = partially shipped, green = fulfilled — "So we know like this is a..." (00:40:07) — all done via HTML customization

**Child opportunities:**
- **3a.** No visual indicator of shipment status (partial vs. complete) without HTML customization
- **3b.** Can't easily see at a glance which items on a sales order have shipped and which haven't
- **3c.** Need to track both what's been shipped AND what's been paid for — two different dimensions of "complete" (00:42:48)
- **3d.** Prepayment orders make this harder — the full amount is paid upfront, so the invoice can't be used to determine shipment progress

---

## Opportunity 4: No native color-coding or visual status indicators in grid views

GT Simulators uses HTML color-coding to track shipment status (yellow for partial, green for fulfilled). This is one of the most commonly requested features across all of Matt's accounts but requires extensive HTML customization.

**Evidence:**
> "Do you know the amount of people that request coloring? ... this is all HTML... this took us like a year just like literally just the HTML stuff took us like six months." (00:45:32)

> "Yellow is partially shipped, green is fulfilled, and then they're unfulfilled." (00:40:07)

**Child opportunities:**
- **4a.** No conditional formatting for grid rows based on field values
- **4b.** HTML customization for visual indicators is expensive (6+ months of work) and fragile
- **4c.** Color-coding is requested for internal views only — report templates already support it, but the working grid doesn't

---

## Opportunity 5: Creating purchase orders for multiple vendors from a single sales order takes too many steps

While GT Simulators uses POs less centrally than SPK Associates, this is a cross-cutting pain point across all of Matt's accounts that use Purchase Orders (4 out of 22). The out-of-box workflow forces users to create POs one vendor at a time.

**Evidence:**
> "If you wanted to create two purchase orders with different vendors for this one, you'd have to go from the sales order, create purchase order, put the drop, select the items, create the purchase order, then you have to go back to the sales order, then hit the drop down, do the other vendor, select the items that you want." (00:47:24)

> "Four out of 22 that are using purchase orders. And they all I've customized like so this screen for everyone." (00:48:17)

**Child opportunities:**
- **5a.** No option to automatically split a purchase order by vendor — requires manual one-at-a-time creation
- **5b.** Each round-trip (create PO → go back → create another) wastes time and increases error risk
- **5c.** PO creation screen behavior depends on where you came from (sales order vs. estimate vs. invoice) — inconsistent experience (00:49:26)

---

## Opportunity 6: International addresses break Method's data model

GT Simulators ships worldwide — including Africa and parts of Asia where postal codes and address structures don't fit Method's fields.

**Evidence:**
> "Addresses in Asia hate method... there's like I think the postal codes are like 11 digits in some places. So it's like awful for us. So we had to like figure out something else because we can't use a state field or postal code field because we need a region and like a region code doesn't exist." (00:34:23)

**Child opportunities:**
- **6a.** Postal code fields can't accommodate international formats (e.g., 11-digit Asian postal codes)
- **6b.** No region/province field for countries that don't use state-based addressing
- **6c.** International Shopify orders that sync into Method break when addresses don't fit the expected format

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| EDI support | Not mentioned for GT Simulators |
| Multi-warehouse management | Not discussed — GT Simulators appears to operate from a single location |
| Reorder points / low stock alerts | Not mentioned |
| Packing slips | GT Simulators uses them but no pain point was described around them |
| Shopify integration issues (beyond addresses) | Shopify orders flow in, but no friction described beyond address formatting |

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Singletary Overlap | Europena Overlap | Yasar (Brownsafe/Kier) Overlap |
|---|---|---|---|
| **#1** Invoice quantities don't update live | No overlap | No overlap | **Yasar #8** Production timelines stale (similar theme: data staleness) |
| **#2** No place to manage shipments | No overlap | No overlap | No overlap |
| **#3** Partial shipment tracking | No overlap | No overlap | No overlap |
| **#4** No color-coding in grids | No overlap | No overlap | No overlap |
| **#5** Multi-vendor PO creation too many clicks | No overlap | No overlap | No overlap |
| **#6** International addresses break data model | No overlap | No overlap | No overlap |

### New Opportunities Unique to GT Simulators

The following opportunities surfaced here but NOT in previous interviews:
- **#1**: Invoice quantities not updating live — specific to GT Simulators' prepayment inventory model where invoice accuracy drives inventory accuracy
- **#3d**: Prepayment complicates partial shipment tracking — a unique variant of the partial shipping problem where the financial dimension (already paid in full) is decoupled from the fulfillment dimension
- **#6**: International address limitations — specific to GT Simulators' worldwide shipping via Shopify

### Strengthened Opportunities (Corroborated Across Calls)

- **Data staleness / real-time updates** — Yasar's production timelines are 24 hours stale; GT Simulators' invoice quantities don't update live. Both point to the same underlying need: data that reflects current reality, not a snapshot from when it was first created.
- **No place to manage shipments** — SPK Associates (from the same call) and GT Simulators both use Sales Orders as the de facto shipment management tool. Matt confirmed Sales Orders are the most customized app across all 22 of his accounts for this reason.
- **Partial shipping is universal** — Matt described this as happening "all the time" across manufacturing and distribution. GT Simulators' international shipping adds another dimension (different countries, different timelines) to this already-established pattern.

---

*Document created: January 29, 2026*
*Analysis by: Claude Code*
