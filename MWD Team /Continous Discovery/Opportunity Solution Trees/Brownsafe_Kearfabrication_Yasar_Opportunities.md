# Opportunity Solution Tree: Brown Safe & Kier Fabrication (Yasar Zaman, PS)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** Brownsafe & Kearfabrication Workflow/Customization Review — January 28, 2026
**Interviewee:** Yasar Zaman (Professional Services, Method)
**Interviewer(s):** John Miranda, Elaine Chow, Barbara Stevenson
**Customers Discussed:** Brown Safe (safe manufacturing), Kier Fabrication (fabric/equipment manufacturing)

**Important Context:** Yasar is an internal PS team member with hands-on experience customizing Method for 10-30 MWD accounts. His opportunities are **proxy evidence** — observed patterns across multiple customers, not a single customer's firsthand story. However, unlike a partner (e.g., Singletary), Yasar has built the actual workarounds, which gives him concrete knowledge of what's missing.

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: No central place to manage everything related to a project/job

This is the strongest and most recurring opportunity from the call. MWD customers need a single hub that ties together transactions, tasks, inventory, and custom fields for a project — but nothing in Method does this out of the box.

**Evidence:**
> "At the end of the day they need a place to manage everything. A central place... it's not just housing the transactions and the interactions, but also here's all the custom stuff. Here's all the inventory that's related, all the things that we need to do, the to-do list, everything like that all in one place. It's kind of like opportunities on steroids." (00:25:39)

> "I think that's like a common point between all of those types of customers." (00:26:39)

**Child opportunities:**
- **1a.** Transactions (estimates, invoices, POs, bills) are scattered across separate apps with no unified view per project
- **1b.** Custom elements (inventory, to-do lists, notes) can't be attached to a project without building a custom app
- **1c.** Jumping between screens to view related information is a hassle — "it becomes a hassle to come into the same screen... directs you to that work order then you have to go back" (00:48:38)

---

## Opportunity 2: The Opportunities app forces MWD customers to use fields that don't apply to their business

Opportunities would be the natural home for project tracking, but mandatory fields (close date, stages, probability) are irrelevant to manufacturing workflows. This drives customers to pay for custom app development.

**Evidence:**
> "The problem with opportunities is you need a close date. Like why do you need a close date? We don't know when this opportunity is going to close. Or having stages, probabilities... there's a lot of bloat in an opportunity that prevents a user from going into it and finding it appealing for them." (00:38:14)

> "A lot of the common customizations revolve around can we just have a separate app that just gives us what we want." (00:38:14)

**Child opportunities:**
- **2a.** Mandatory close date has no meaning for open-ended manufacturing projects
- **2b.** Pipeline stages and probability percentages are irrelevant for production tracking
- **2c.** Opportunity lines and lead sources add noise that obscures what matters
- **2d.** Both Brown Safe and Kier Fabrication paid for custom apps to get around this — cost that shouldn't be necessary

---

## Opportunity 3: Production and material management happens outside Method with no integration back

Both customers manage their production cycle — material ordering, stock checks, production scheduling — in external tools. Method stops being useful between "estimate accepted" and "ready to invoice."

**Evidence:**
> "That entire production schedule happens outside of Method." (00:13:17)

> "We tried to use Method to do that at one point but the original person that was on that project left the company, so we never got around to incorporating Method. So what they did instead is they use a different software for it." (00:06:33) — Brown Safe on Base 44

> "Inventory. I don't think they track at all to be honest. If they do, it's somewhere else. It's not in Method." (00:22:29) — on Kier Fabrication

**Child opportunities:**
- **3a.** After an estimate is approved, there's a "pause" where users leave Method entirely to handle production (00:10:13)
- **3b.** Can't determine what materials are needed or what's in stock from within Method
- **3c.** No way to connect an invoice/estimate to a production schedule natively — Brown Safe is attempting a custom integration with Base 44
- **3d.** When production is done, users have to come back into Method to pick up the workflow where they left off

---

## Opportunity 4: No automated reminders or notifications for upcoming dates and actions

The #1 feature request across all of Yasar's customers, regardless of industry.

**Evidence:**
> "That's probably like the number one thing that I've always been asked for is automations. Whether it's emailing customers or emailing users... just like an easier process to handle automation and setting up rules for automation." (00:42:46)

> "The reminders piece where maybe it could be an estimate, but it could also be like, hey, the order date for this date is coming up. Remember to go check up on this order." (00:42:46)

**Child opportunities:**
- **4a.** No automated estimate follow-up reminders
- **4b.** No alerts when order dates or ship dates are approaching
- **4c.** Setting up automation rules is not easy for end users — requires PS customization work
- **4d.** Brown Safe uses activities to manually track follow-ups on invoices and installation dates (00:03:30) — a manual workaround for missing automation

---

## Opportunity 5: Different customers need different prices for the same item and Method doesn't support this natively

Custom pricing levels are one of the most common PS customizations for MWD accounts.

**Evidence:**
> "Price levels for sure. That's one of them." (00:34:53) — when asked about common MWD customizations

> PS team has built pricing level solutions multiple times: a catalog solution using routines (00:31:46), and a customer-level price rules system for QuickBooks Desktop Enterprise where rules don't sync to Method (00:32:51)

**Child opportunities:**
- **5a.** No native support for customer-specific pricing tiers
- **5b.** QuickBooks Desktop Enterprise price rules don't sync to Method, requiring PS to rebuild them (00:32:51)
- **5c.** Each implementation is slightly different — customer-level vs. item-level pricing rules — suggesting the problem has multiple valid shapes

---

## Opportunity 6: Can't track inventory across multiple locations from within Method

Manufacturing customers ask for multi-location inventory management but Method doesn't provide it natively.

**Evidence:**
> "This is something that a lot of customers that are in that business kind of ask for is like managing your inventory in different locations." (00:36:06)

> PS built a catalog customization for this: "You can have different locations, you can have different items in those locations, and you can calculate the quantity that you have for that location." (00:34:53)

**Child opportunities:**
- **6a.** Can't see how much stock exists at a specific location when creating an estimate or invoice
- **6b.** No automatic quantity decrease when items are pulled from a location on a transaction (00:36:06)
- **6c.** No prompt to create a purchase order when stock at a location is low

---

## Opportunity 7: Can't scan barcodes for pick and pack processes

Customers who want to do pick/pack in Method are blocked by the lack of barcode scanning support.

**Evidence:**
> "A lot of the time they want the barcode scanner, right? And so we can't... there's no way to support that." (00:40:59)

> "I promise you I tried everything. I promise you." (00:41:52)

**Child opportunities:**
- **7a.** Warehouse workers can't scan items to pick/pack from Method
- **7b.** Customers who use barcodes in other systems can't integrate that process with Method
- **7c.** Workarounds (QR codes linking to Method portal pages) require customers to change their entire existing process (00:41:52)

---

## Opportunity 8: Production timelines are stale because calculated fields only update once per day

Kier Fabrication uses "weeks in production" and "ship date" fields that are calculated by a daily routine, meaning the data is always up to 24 hours behind.

**Evidence:**
> "These two columns are calculated outside of Method, so there's like a daily routine that runs that calculates it... But maybe you want an up-to-date number itself. And so in order to get the up-to-date number, you actually have to click on one of these two buttons, at which point it's going to update all of whatever all projects, all jobs, which takes a while." (00:22:29)

**Child opportunities:**
- **8a.** Production timeline data is always stale by up to 24 hours
- **8b.** Getting real-time data requires manually triggering an update across all 280+ jobs — which is slow
- **8c.** No way to see real-time production status without manual intervention

---

## Opportunity 9: Subcontractors/installers need access to project information without being full Method users

Brown Safe outsources installation to one-time subcontractors who need to see job details and communicate with customers, but giving each one a Method user seat doesn't make sense.

**Evidence:**
> "A lot of times they just outsource to other vendors or other employees, so it's like a one-time subcontractor... it doesn't make sense for them to have a dedicated user put into Method to be able to see it on a portal or something." (00:16:27)

**Child opportunity:**
- **9a.** No lightweight access model for external contractors who need temporary, project-scoped visibility

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| EDI support | Only two customers have asked about it — Yasar doesn't know enough about it to give a solid answer (00:40:08) |
| Job costing | Being addressed by John Sandy's module using the jobs app — more of an active development item than an unmet need |
| Drag and drop for line items | Yasar mentioned it briefly (arrows to reorder items) but it's a UI preference, not a pain point with evidence of impact |

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Singletary Overlap | Europena Overlap |
|---|---|---|
| **#4** No automated reminders | **Singletary #4** No alerts when inventory status changes | No direct overlap |
| **#6** Can't track inventory across locations | **Singletary #2** Can't see stock at order entry | **Europena #2a** Inventory checked after invoice |
| **#1** No central project hub | No overlap (Singletary focused on inventory, not project tracking) | No overlap |
| **#3** Production happens outside Method | No overlap (Singletary's customers used external inventory tools similarly) | **Europena #5** Managing multiple disconnected systems |
| **#5** No native pricing levels | No overlap | No overlap |
| **#7** No barcode scanning | No overlap | No overlap |

### New Opportunities Unique to This Call

The following opportunities surfaced here but NOT in previous interviews:
- **#1 and #2**: Central project hub / Opportunities bloat — this is a PS-specific insight about how MWD customers actually use (or refuse to use) Method's existing tools
- **#5**: Pricing levels — a frequent customization need not mentioned by customers directly
- **#7**: Barcode scanning — a hard blocker for pick/pack processes
- **#8**: Stale production timeline data — specific to manufacturing workflows
- **#9**: Lightweight contractor access — specific to outsourced installation/field service workflows

### Strengthened Opportunities (Corroborated Across Calls)

- **Stock visibility during transactions** — Singletary called it table stakes, Europena showed the consequence of not having it, and now Yasar confirms PS has built a multi-location inventory customization to address it
- **Automation / reminders** — Singletary mentioned alerts for stock arrival; Yasar says it's the #1 request across all industries

---

*Document created: January 28, 2026*
*Analysis by: Claude Code*
