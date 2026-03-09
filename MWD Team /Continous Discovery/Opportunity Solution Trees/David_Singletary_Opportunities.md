# Opportunity Solution Tree: David Singletary (DJS DIGITAL LLC)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** Discovery Call with David Singletary — January 19, 2026
**Interviewee:** David Singletary, DJS DIGITAL LLC (MWD Partner/Implementer)
**Interviewer(s):** John Miranda, Barbara Stevenson, Elaine Chow

**Important Context:** David is a Partner, not an end customer. He has 27+ years of inventory management experience and ~450 implementations. His opportunities are **proxy evidence** — observed patterns across hundreds of MWD customers. Torres would note this is less direct than a customer's own story, but the volume of implementations gives it breadth that a single customer interview cannot.

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: Customers don't know what inventory they have or where it is

This is the most fundamental opportunity David surfaced. The chemical company story paints a picture of complete inventory blindness before intervention.

**Evidence:**
> "They had no idea how much inventory they had at all. They didn't know what their formulas were. They had one person that had all the formulas in their head. If that person got hit by a car, everything's gone." (00:12:07)

**Child opportunities:**
- **1a.** No tracking of ordered, received, or stocked materials — everything on paper or in spreadsheets
- **1b.** Critical product/formula knowledge locked in one person's head (single point of failure)
- **1c.** Business owner can't see operations without being physically present — chemical company owner drove 4 hours to the office to see what was happening

---

## Opportunity 2: Can't see stock availability at the moment of order entry

David called this out as table stakes — the single most critical moment in the workflow is when someone is entering an order and needs to know if they can fulfill it.

**Evidence:**
> "If they're placing orders, they need to know if they have stock to fill the order. And if they don't have enough stock, they need to be able to create a purchase order to order it from the vendor." (00:12:07)

> "Easily look up quantity on hand as they're entering an order." (table stakes discussion)

**Child opportunities:**
- **2a.** No distinction between quantity on hand vs. quantity available — David specifically flagged this: "That's what I was just going to ask — the distinction between on hand and available"
- **2b.** Have to leave the order entry workflow to check stock in another system or screen
- **2c.** Don't know they can't fulfill until after they've committed to the customer

---

## Opportunity 3: Too many clicks and interruptions to get an order through

David framed this as an intuitiveness problem. The order entry workflow should be frictionless, but currently requires navigating multiple screens and systems.

**Evidence:**
> "It has to be intuitive for the customer. They shouldn't have to click multiple times to get an order through." (table stakes discussion)

> "If the customer is not there, they should be able to add on the fly." (table stakes discussion)

**Child opportunities:**
- **3a.** Can't add a new customer or vendor on the fly during order entry — have to leave, create, come back
- **3b.** Multiple screen navigation required to complete a single order

---

## Opportunity 4: No way to know when inventory status changes

David described a need for proactive notifications at multiple points in the workflow — when stock arrives, when it runs low, and when orders are ready.

**Evidence:**
> "They need to be alerted when that product comes in so they can let the customer know." (00:12:07)

> "They need to be alerted when they're low in stock." (differentiators discussion)

**Child opportunities:**
- **4a.** Don't know when ordered stock arrives from a vendor — can't proactively notify customer
- **4b.** Don't know when stock drops below safe levels until it's too late (no reorder alerts)
- **4c.** No automated triggers when workflow stages change — "Automating workflows, updating fields automatically when XYZ happens"

---

## Opportunity 5: End customers have to call to find out their order status

David surfaced this as a differentiator — the customer's customer has no visibility into where their order stands.

**Evidence:**
> "Maybe the ability to have a portal so a customer can log in and see the status of their order instead of having to call." (differentiators discussion)

**Child opportunity:**
- **5a.** No self-service visibility for end customers — every status check requires a phone call and someone looking it up internally

---

## Opportunity 6: Remote and mobile salespeople can't enter orders from the field

David flagged this as a competitive differentiator. Sales reps in the field need to enter orders on the spot.

**Evidence:**
> "Remote salespeople or mobile salespeople be able to enter an order from wherever they are." (differentiators discussion)

**Child opportunity:**
- **6a.** Field reps have to wait until they're back at a desktop or relay orders to someone at HQ

---

## Opportunity 7: QuickBooks and inventory systems fight over who is the source of truth for stock quantities

This is a technical opportunity that David raised based on implementation experience across multiple platforms. It's a systemic problem, not specific to one customer.

**Evidence:**
> "Most other inventory systems require that tracking quantity on hand in QuickBooks be turned off because they can't handle both. QuickBooks gets confused and ends up overstating cost of goods sold." (technical discussion)

> "This should be their system of record for what's on hand and the total value." (on Method's role)

**Child opportunities:**
- **7a.** COGS gets overstated when both QuickBooks and the inventory system track quantity simultaneously
- **7b.** Stock adjustments made in one system don't reflect in the other — no single source of truth
- **7c.** Customers don't know which system to trust for accurate inventory numbers

---

## Opportunity 8: Don't know how long it takes to get product from a vendor

David identified lead time visibility as important for planning — without it, purchase orders are guesswork.

**Evidence:**
> "They need to know lead times, how long it takes to get that product from that vendor." (differentiators discussion)

**Child opportunity:**
- **8a.** Can't plan reorders effectively without historical or expected lead time data

---

## Opportunity 9: Inventory on mobile assets isn't tracked alongside warehouse stock

This emerged from the roofing company example. It's a niche scenario but represents a real pattern for field service companies.

**Evidence:**
> "I think they're unique because they have the mobile trucks. Most people are not managing inventory in the warehouse and on trucks." (roofing company story)

**Child opportunities:**
- **9a.** Inventory loaded onto trucks leaves the warehouse system's visibility
- **9b.** Returns and add-ons from field jobs create reconciliation complexity the next day

**Note:** David himself flagged this as atypical ("they're unique"). This opportunity may not generalize to the MWD target persona.

---

## Opportunity 10: Can't see important operational metrics without custom reporting

David listed multiple reports that are critical for MWD customers but not available out of the box.

**Evidence:**
> "These type of reports are very important to manufacturers and retailers." (reporting discussion)

> "Good reporting, dashboards, min/max levels, reorder points." (differentiators discussion)

**Child opportunities:**
- **10a.** No visibility into gross margins on orders
- **10b.** No sales breakdown by customer, location, or product
- **10c.** No min/max or reorder point visibility in dashboards

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| BOM / formula management | David mentioned it but flagged it as a separate complexity tier — "you're adding a whole other complexity" — not a current need for the MWD MLP target |
| Batch numbers / expiration dates | Listed as future manufacturing needs, no customer story behind them |
| Barcode scanning | Mentioned in the roofing story but not explored as a pain point |

---

## Cross-Reference: Opportunities That Also Appear in Europena Interview

| Singletary Opportunity | Europena Overlap | Notes |
|---|---|---|
| **#2** Can't see stock at order entry | **Europena #2a** Inventory checked after invoice, not before | Same core problem, different angle — Singletary describes the need, Eve describes the consequence |
| **#3** Too many clicks for an order | **Europena #2** Too many steps from order to getting paid | Singletary frames it as UI friction, Eve frames it as workflow friction — both point to the same streamlining need |
| **#7** QB and inventory system conflict | **Europena #3** Can't trust data without manual verification | Different root cause but same outcome — users don't trust the numbers |
| **#4** No alerts when status changes | No direct overlap | Europena didn't mention alerts — this is additive from Singletary |
| **#6** Mobile salespeople can't enter orders | **Europena #4** Sales reps can't access inventory systems | Related but different — Singletary's is about mobile access, Eve's is about role-based visibility |

---

*Document created: January 28, 2026*
*Analysis by: Claude Code*
