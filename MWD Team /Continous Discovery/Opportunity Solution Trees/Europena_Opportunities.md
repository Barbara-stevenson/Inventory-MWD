# Opportunity Solution Tree: Europena (Food Distribution)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what they actually said. They are NOT solutions.*

**Source Interview:** Europena: Method Feedback / Chat with Noor & Evelin — January 23, 2026
**Customer:** Evelin Hodges (Eve), Europena
**Interviewer(s):** Noor Shamji, John Miranda, Thomas Darlington

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: Product data loses its identity as it moves between systems

Eve's story about Fishbowl is the clearest opportunity in this interview. The data degradation is not a one-time annoyance — it cascades through every downstream system.

**Evidence:**
> "Everything just became like a Fishbowl item. It didn't matter if it's the actual product or credits or disbursements, everything just came in as like a Fishbowl item." (00:05:22)

> "If I wanted to search for one of our products, citrus and lemon, I'm not able to pull it out as citrus and lemon." (00:08:17)

**Child opportunities:**
- **1a.** Can't search for specific products across systems (item-level searchability is broken)
- **1b.** Descriptions end up in the wrong field (memo vs. description), requiring manual data cleanup
- **1c.** Have to manually re-enter item descriptions that should have carried over automatically — "triple the amount of work when it should just have been once"

---

## Opportunity 2: Too many steps from order to getting paid

This is the opportunity Eve identified as her **biggest friction point** when John asked directly. She described a workflow where steps that should flow naturally require backtracking.

**Evidence:**
> "I think we have a lot of steps. It would be nice to cut them down honestly." (00:23:20)

> "It's the invoice in the PO, then we get the sales order, then we have to create the invoice, and then we have to go back and then we check with the inventory, and then if it's missing, and then after that we have to then change that invoice around and make it a final invoice." (00:24:47)

**Child opportunities:**
- **2a.** Inventory isn't checked until after the invoice is created — forcing rework when stock is insufficient
- **2b.** Invoices have to be modified after the fact rather than being correct the first time
- **2c.** Invoicing and inventory live in separate systems, requiring manual handoffs between Fishbowl → QuickBooks → Method

---

## Opportunity 3: Can't trust that the data in Method matches reality without manually verifying

Eve described a trust problem with sync reliability that forces her to double-check numbers.

**Evidence:**
> "Sometimes when you wake up and the numbers are not correct, but then if you do another sync... and then all of a sudden the numbers are correct." (00:20:30)

> "I've double, triple-checked my numbers — what's in QuickBooks and what's in Method — just to see, and we're good." (00:21:25)

**Child opportunities:**
- **3a.** Numbers appear incorrect after initial sync, requiring a second sync to resolve
- **3b.** No way to know if data is correct without cross-referencing QuickBooks manually
- **3c.** Historical trust issues (pre-Thomas customization) created adoption resistance — "people didn't like using it a lot" (00:04:22)

---

## Opportunity 4: Sales reps need to see product/inventory information but can't access the systems that hold it

Europena deliberately keeps sales reps out of QuickBooks and Fishbowl. Method is their only window. But Method currently doesn't surface inventory data natively.

**Evidence:**
> "Our sales reps don't get to use QuickBooks. There's a department that does all of that processing." (00:19:37)

> "What we use Method for is more for the sales rep. So they have more access to just being able to see their numbers." (00:18:24)

**Child opportunities:**
- **4a.** Sales reps have no visibility into stock levels from Method
- **4b.** Reps can only send copies of existing sales orders — they can't initiate or check inventory status themselves
- **4c.** Accounting data needs to stay hidden from reps while product/inventory data becomes visible (permission granularity needed)

---

## Opportunity 5: Managing multiple disconnected systems creates ongoing maintenance burden

Eve manages two mirrored Method setups across two companies, each with its own inventory tool and QuickBooks instance. Every change has to be replicated.

**Evidence:**
> "We have two companies... two different companies but we have like almost the same thing, so we can kind of mirror every app that we're using." (00:00:00)

> She's migrating one company from Fishbowl to Marov while the other already works differently — each requires its own customization approach.

**Child opportunities:**
- **5a.** Switching inventory tools requires re-building customizations in Method (Fishbowl → Marov)
- **5b.** Two parallel systems means double the maintenance for similar workflows
- **5c.** Data structure differences between inventory tools mean Method customizations aren't portable

---

## Opportunity 6: Dirty data accumulates when multiple people input contacts

Smaller and less inventory-specific, but Eve called it out as a real problem.

**Evidence:**
> "When we have a ton of people putting in contacts... we end up having a lot of dirty stuff in there." (00:01:11)

**Child opportunity:**
- **6a.** Parent-child data structure makes duplicate detection harder

---

## Opportunities NOT Included (Insufficient Evidence from This Interview)

Per Torres' framework, opportunities must be grounded in customer evidence. The following were deliberately excluded:

| Potential Opportunity | Why Excluded |
|---|---|
| Multi-warehouse management | Eve has one distribution center per company — no evidence of multi-warehouse need |
| Reorder points / low stock alerts | Not mentioned by Eve |
| Serial number tracking | Not mentioned by Eve |
| BOM / formula management | Future state only — "I'm not yet at that place where I know exactly how we're going to be managing inventory" (00:16:14) |

These may be valid opportunities from other interviews but do not belong on the tree based on this customer's evidence alone.

---

*Document created: January 28, 2026*
*Analysis by: Claude Code*
