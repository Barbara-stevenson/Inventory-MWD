# Opportunity Solution Tree: Liquid Medlock (Toby Merker, Customer)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** Liquid Medlock Discovery Call — February 5, 2026
**Interviewee:** Toby Merker (Supply Chain Manager, Liquid Medlock)
**Interviewer(s):** John Miranda
**Customer:** Liquid Medlock (medical-compliant packaging company — child-resistant and compliance packaging for pharmaceutical/cannabis industries, methadone dispersement packaging; Canadian-based, expanding into US market)

**Important Context:** Toby is a direct end customer, not PS or Partner — this is **first-party evidence**. He manages the entire supply chain "birth to death" (order through to invoice) and is the sole operational user of Method CRM at Liquid Medlock. The company operates out of 4 separate warehouse locations, sources product from factories in China, and uses QuickBooks Online. Notably, Liquid Medlock has one of the most mature custom inventory implementations in Method — built over months with PS developer Safwan — including a custom container app, purchase order app, inventory dashboard with run rates, and QBO sync. Toby is highly satisfied with the current setup and skeptical that a general-purpose inventory solution would match what they've built. This makes his remaining pain points especially significant: they represent gaps that even extensive customization hasn't fully closed.

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: Human error in data entry is the sole remaining cause of inventory discrepancies — and there's no system validation to catch it

Despite a mature, heavily customized inventory setup, Toby identified human error as the only remaining problem in their otherwise streamlined workflow. Warehouse code typos and quantity entry mistakes cascade into inventory misalignment that requires manual detective work to resolve.

**Evidence:**
> "The only issue that we have found so far is humans. So, every time a human makes a mistake either in a quantity or in a skew code or listing an item incorrectly or ordering the wrong thing, errors happen. And um if I could remove the humans, it would be great." (00:09:31)

> "So it's very very simple in fact is uh we get a container of items and we have a code that marks it that it's going to a G warehouse or to our BMPon warehouse and it's one letter difference. So when you're inputting the wrong letter code for the warehouse it'll say we have units in G when they're supposed to be and actually in Bmpton." (00:10:28)

> "An item comes in and you key in that we received 10,000, but we actually received a 100,000 and now things don't align and you're missing inventory." (00:10:28)

**Child opportunities:**
- **1a.** No validation or safeguards on warehouse code entry — a single-character typo assigns inventory to the wrong location
- **1b.** No quantity validation on receipt entry — order-of-magnitude errors (10,000 vs. 100,000) go undetected until reconciliation
- **1c.** Errors aren't caught at the point of entry — they surface later when QuickBooks says "you don't have this item on hand" during order processing, triggering manual investigation
- **1d.** No automated anomaly detection or data integrity checks to flag likely entry errors before they propagate

---

## Opportunity 2: Inventory reconciliation is entirely manual — reviewing documents, tracking down errors, and making stock adjustments by hand

Annual inventory reconciliation requires cross-referencing CRM records, warehouse reports, orders, and transactions to find discrepancies — then manually adjusting stock counts. Every discrepancy traces back to human error, but the resolution process has no system support.

**Evidence:**
> "We're just completing our inventory reconciliation for last year and we're going through it... every single error and misalignment is due to some kind of human error. Every single one." (00:10:28)

> "Our warehouse is coming to us and saying, 'No, we shipped out this much on this date, and here's the orders, and that's the quantity we're supposed to have.' And then me and Rey, our accountant, go back and look through our inventory and our orders, and it's like, 'Oh, yeah, this order was coded wrong, or oh yeah, this order, uh, the quantities didn't match.'" (00:11:44)

> "Manual adjustment, make the counts match. I don't want to talk about it anymore." (00:11:44)

**Child opportunities:**
- **2a.** No audit trail or change log to quickly identify when and where an entry error occurred — requires manual investigation across documents
- **2b.** No system-assisted reconciliation workflow — comparing CRM inventory against warehouse WMS reports is entirely manual
- **2c.** Stock adjustments are manual one-off corrections with no structured reconciliation process in Method
- **2d.** Reconciliation frequency is artificially low (annually, negotiated to semi-annually) because the process is so painful — the accountant wants monthly but the effort isn't justified

---

## Opportunity 3: Shipment confirmation from warehouses must be manually uploaded one-by-one into CRM to generate invoices

After warehouses ship orders, they send reports to Toby, who manually uploads tracking data into CRM and generates invoices one at a time. This is the "magic wand" request — the single thing Toby would change about Method if he could.

**Evidence:**
> "At the end of the day, we get a it's manual where end of the day the warehouses are sending us the paperwork or the reports saying these orders have shipped and we are uploading that data into CRM and then generating invoices um double-checking that the right ship items have been shipped and generating the invoices manually." (00:16:35)

> "The end of day shipped out documents from the warehouse, I would like them to automatically upload and if not automatically generate an invoice, be like, everything's uploaded and done and look at it before I hit the invoice. Um, that would be that's the only thing." (00:27:59)

> "I get an Excel file every night at like 11:00 at night that says, 'Here's all the orders that shipped out. Here's the lot numbers, here's the items, here's the tracking, here's the orders.' Um, and then I literally just open the Excel file and then upload one by one into CRM." (00:27:59)

**Child opportunities:**
- **3a.** No way to import structured shipment data (Excel) from warehouses into CRM — each shipment must be entered manually
- **3b.** Four warehouses with four different WMS systems produce reports in four different formats — there's no standard data format that CRM could ingest
- **3c.** Invoice generation after shipment confirmation is manual — no automated or semi-automated sales order → invoice conversion triggered by shipment data
- **3d.** The manual process works (5-10 minutes/day for 5-10 shipments) but introduces yet another point where human error can enter the system

---

## Opportunity 4: Sales team had no inventory visibility in CRM — required custom QuickBooks integration to solve

Before the custom QBO-CRM sync was built, sales reps had no way to check available stock without consulting daily warehouse reports or asking Toby directly. The custom integration solved this, but the solution only updates once daily and is not a native Method capability.

**Evidence:**
> "Two main things that we wanted was visibility through CRM because we were getting daily reports from our warehouses... sales was coming and going do we have this, do we have that? or sales was copied on reports and having to pull them up. Um, and I don't know if you've dealt with anybody in sales, they're not always great at reports and Excel or data. So, um, there would always be questions." (00:05:20)

> "The one change we made um was tying in CRM to our inventory with QuickBooks so that when you type in the product at a specific warehouse, it will tell you the available quantity as of this morning's QuickBooks count." (00:06:15)

> "We can see what's available real time. Well, with daily, I won't say real time. It's every morning it gets updated." (00:05:20)

**Child opportunities:**
- **4a.** No native inventory visibility in Method at point of order entry — required custom development to display QBO inventory data
- **4b.** Inventory data is stale by design — syncs once daily (~11 AM), so availability shown during order entry may not reflect actual stock
- **4c.** Inventory visibility is per-warehouse — the sales team needed to see stock at a specific location, not just aggregate totals

---

## Opportunity 5: No native way to track inbound international shipments and purchase orders from suppliers

Liquid Medlock sources products from factories in China. Tracking containers, items, quantities, arrival dates, and shipping documents required building two entirely custom apps (Container app and Purchase Order app) in Method.

**Evidence:**
> "The main function that was started with CRM after the order placement was uh with our container uh containers and shipments coming from China. We needed a database to track items, track quantities, track arrival dates, track shipping documents." (00:07:09)

> "That container app ties into a purchase order app that is also on CRM. So that when I send a purchase order over to China, the quantities and units that we've ordered is real time updated. Um, but that ties over to our inventory page to say you have 150,000 of these units, you have 50,000 more on the water and you have an open PO of a 100,000 still to be made and still to ship." (00:07:09)

**Child opportunities:**
- **5a.** No native container or freight shipment tracking — customers sourcing internationally have no way to track inbound goods without custom apps
- **5b.** No native connection between purchase orders and expected inventory — "on the water" and "open PO" quantities aren't tracked natively
- **5c.** The custom apps took months of iterative development with PS — "we spent, you know, weeks and months um, here's a step, here's a step" (00:26:11) — this level of effort is a barrier for most customers

---

## Opportunity 6: No native run rate calculations, replenishment timelines, or low stock email alerts

Liquid Medlock built a custom inventory tab that calculates 12-month run rates, estimates replenishment time, and sends email alerts for low-stock items. None of this exists natively in Method.

**Evidence:**
> "We even have a piece on our inventory tab that gives us run rates now... that says these items you have on hand. This is your 12 month sales. This is how long it takes you to replenish it. And I get an email that says you need to look at these items. Do you need to order more?" (00:08:30, 00:09:31)

> "So like we're fully integrated with CRM in our entire um supply chain management, ordering our orders um our visibility on our items." (00:09:31)

**Child opportunities:**
- **6a.** No native run rate or velocity calculation for inventory items — had to be custom built
- **6b.** No native replenishment time tracking — customers can't see how long it takes to restock an item without custom development
- **6c.** No native low stock alerts or email notifications when inventory drops below safe levels

---

## Opportunity 7: No place to capture customer-specific delivery instructions tied to ship-to addresses

Liquid Medlock's customers have specific delivery requirements per location (tailgate needed, delivery time windows, item restrictions) but there's no native field on ship-to addresses to store and surface these notes during order creation.

**Evidence:**
> "In our specific customer ship to addresses. We are having customer-specific delivery requests and items. There's nowhere to capture those items easily for each shipment location." (00:28:51)

> "I want to be able to go into Shoppers Drug Mart, Shoppers Drug Mart Monton, and say, 'This location needs a tailgate. This location delivers before 2 p.m., this location needs specific items only.'" (00:28:51)

> "Even if it's only 280 characters or 200 characters of notes that I could type in for each ship to address that when I then go into ordering an item or creating a sales order, it gives me that box that's prepopulated and I can save and overwrite it on every order if I need to, but it's always there for that destination." (00:29:53)

**Child opportunities:**
- **7a.** No native notes or instructions field on ship-to addresses — delivery requirements aren't stored in a structured, reusable way
- **7b.** Delivery instructions don't pre-populate on sales orders when a ship-to address is selected — users must remember or look them up separately
- **7c.** No ability to save default instructions per destination while allowing per-order overrides

---

## Opportunity 8: Method CRM and QuickBooks compete as source of truth for inventory — operations and accounting don't agree on which system to trust

Toby treats Method CRM (backed by warehouse WMS reports) as the operational source of truth. The accountant treats QuickBooks as the ledger of record. This creates ongoing tension, compounded by the fact that human errors in either system can cause them to diverge.

**Evidence:**
> "Method is the source of truth for day-to-day operations and inventory. Yes. Um, however, uh, as God is a source of truth, my WMS reports from my warehouses are my backup." (00:22:07, 00:23:02)

> "Our accountant wants to use QuickBooks as our um as our ledger and this is the be-all and end-all and I have learned due to human error and data entry and back and forth invoicing issues... like our accountant wants to use QuickBooks and I don't care about QuickBooks. So, I guess we're always going to bang heads." (00:23:02)

**Child opportunities:**
- **8a.** No single, authoritative source of truth for inventory — CRM, QuickBooks, and warehouse WMS reports all have different numbers at different times
- **8b.** Operations and accounting use different systems as their "source" which creates internal conflict when numbers don't match
- **8c.** Bi-directional sync between CRM and QBO doesn't resolve which system "wins" when discrepancies arise

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| Pick and pack workflow management | Toby explicitly stated they don't do pick and pack — "We just do picking generally. We don't unpack a box and repack it. We sell full cases." (00:15:41) |
| Sales team CRM features (leads, follow-ups, marketing) | Toby mentioned Jack and sales are pushing for these but said "I don't really care if they do or if they don't" — not his pain point and no direct evidence (00:20:09) |
| US market / Shopify integration | US operations use Shopify separately and are set up differently — this is a business model choice, not a Method gap (00:04:22) |
| WMS-CRM direct integration | Toby explicitly doesn't want this — "No, we don't want it to communicate with the CRM. We want to have our own tracking of our inventory and orders separate from the warehouses." (00:14:50) |

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Singletary Overlap | Europena Overlap | Yasar (Brownsafe/Kier) Overlap | Fuji Mats (Eric) Overlap | Matt Shade (SPK/GT) Overlap |
|---|---|---|---|---|---|
| **#1** Human error / no data validation | No overlap | **Europena #3** Can't trust data without verification | No overlap | No overlap | No overlap |
| **#2** Manual inventory reconciliation | No overlap | No overlap | No overlap | No overlap | No overlap |
| **#3** Manual shipment upload to CRM | No overlap | **Europena #2** Too many steps order to payment | No overlap | No overlap | **Matt #3** No place to manage shipments |
| **#4** Sales had no inventory visibility | **Singletary #1** Customers don't know inventory; **Singletary #2** Can't see stock at order entry | **Europena #4** Sales reps can't access inventory | **Yasar #6** Can't track inventory across locations | **Fuji Mats #6** Inventory dashboard from QBO | No overlap |
| **#5** No native inbound shipment/PO tracking | No overlap | No overlap | No overlap | **Fuji Mats #5** International container shipping | No overlap |
| **#6** No native run rates or low stock alerts | **Singletary #4** No alerts when inventory changes | No overlap | No overlap | No overlap | No overlap |
| **#7** No delivery instructions on ship-to | No overlap | No overlap | No overlap | No overlap | No overlap |
| **#8** CRM vs QBO source of truth conflict | **Singletary #7** QB and inventory system conflict | **Europena #3** Can't trust data without verification | No overlap | No overlap | No overlap |

### New Opportunities Unique to Liquid Medlock

The following opportunities surfaced here but NOT in previous interviews:
- **#2**: System-supported inventory reconciliation — Toby gave a vivid, detailed account of the manual reconciliation pain. Other interviews touched on inventory accuracy problems but none described the actual reconciliation process this concretely.
- **#7**: Customer-specific delivery instructions on ship-to addresses — A net-new request not seen in any other interview. This is specific to distribution workflows where fulfillment involves third-party warehouses and carrier coordination.
- **#8**: CRM vs. QuickBooks source of truth tension — David Singletary raised the QB conflict from an implementer's perspective, but Toby described the *internal organizational* conflict: operations trusts CRM while accounting trusts QuickBooks, and they "bang heads."

### Strengthened Opportunities (Corroborated Across Calls)

- **Sales inventory visibility at order entry** — This is now confirmed from 5+ sources: Singletary called it table stakes, Europena's sales reps couldn't access systems, Yasar built multi-location views, Fuji Mats has a QBO dashboard, and now Liquid Medlock built a custom QBO sync specifically because "sales was coming and going do we have this, do we have that?" This is the single most validated opportunity across all interviews.
- **International container/shipment tracking** — Both Fuji Mats and Liquid Medlock independently built custom container tracking apps to manage inbound shipments from overseas factories. Two separate customers, two separate PS developers, same gap.
- **Low stock alerts and reorder notifications** — Singletary described the need, and now Liquid Medlock has actually built it as a custom solution with email notifications and run rate calculations. This validates that the need is real AND that customers will invest significant PS effort to get it.
- **QuickBooks vs. CRM inventory conflict** — Singletary raised this as a systemic problem across implementations ("QuickBooks gets confused and ends up overstating cost of goods sold"). Liquid Medlock demonstrates the same tension playing out organizationally — operations and accounting can't agree on which system is authoritative.

### Notable Insight: What a "Mature" Custom Inventory Implementation Looks Like

Liquid Medlock represents the ceiling of what's achievable through Method customization. Their setup includes:
1. Daily QBO-CRM inventory sync by warehouse location
2. Custom container app for inbound international shipment tracking
3. Custom purchase order app with real-time quantity tracking
4. Inventory dashboard showing on-hand, on-the-water, and open PO quantities
5. Run rate calculations with 12-month sales velocity
6. Low stock email alert notifications

Even with all of this, their remaining pain points — human error with no validation, manual shipment upload, manual reconciliation, and no delivery instruction fields — reveal gaps that customization alone cannot close. These are platform-level needs.

---

*Document created: February 5, 2026*
*Analysis by: Claude Code*
