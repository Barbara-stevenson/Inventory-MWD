# Opportunity Solution Tree: SPK Associates (Matt Shade, PS)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** SPK Associates Workflow/Customization Review — January 29, 2026
**Interviewee:** Matt Shade Silver (Professional Services, Method)
**Interviewer(s):** John Miranda, Elaine Chow, Barbara Stevenson
**Customer Discussed:** SPK Associates (manufacturing broker/middleman — artwork, tapestries, custom goods)

**Important Context:** Matt is an internal PS team member with hands-on experience customizing Method for ~22 MWD accounts. His opportunities are **proxy evidence** — observed patterns across multiple customers, not a single customer's firsthand story. However, like Yasar, Matt has built the actual customizations, which gives him concrete knowledge of what's missing. He inherited SPK Associates recently (~2 months) from other PS contacts (Cole and Ryan).

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: No native place to manage a complex sales pipeline with multiple document types per deal

Manufacturing brokers like SPK Associates need to track RFQS, quote worksheets, purchase orders, sales orders, estimates, and invoices — sometimes multiple of each — all tied to a single deal. The Opportunities app works but only because of extensive customization.

**Evidence:**
> "They have the purchase orders, they have the sales orders, they have estimates, they have invoices, and sometimes it's multiple because one chair to five chairs." (00:04:28)

> "You need a an app that's like not only project management but like just holding all the information stuff to view. That's what we like about opportunities." (00:06:32)

> "If you did in the estimates in this case it really doesn't make sense because with the estimate it's like estimate invoice. There's no managing of that process." (00:05:29)

**Child opportunities:**
- **1a.** Estimates can't hold multiple related transactions (POs, SOs, invoices) — they only support a linear estimate → invoice path
- **1b.** No native way to track multiple RFQS, quote worksheets, and POs all tied to one deal
- **1c.** Opportunities work but only after heavy customization — out of the box they don't support the manufacturing workflow
- **1d.** Reporting on deal success requires custom definition (e.g., "successful = has a sales order") that isn't natively supported

---

## Opportunity 2: Creating purchase orders for multiple vendors from a single sales order takes too many steps

Every account that uses Purchase Orders (4 out of 22) requires customization on the PO creation screen. The out-of-box workflow forces users to create POs one vendor at a time, navigating back and forth.

**Evidence:**
> "If you wanted to create two purchase orders with different vendors for this one, you'd have to go from the sales order, create purchase order, put the drop, select the items, create the purchase order, then you have to go back to the sales order, then hit the drop down, do the other vendor, select the items that you want." (00:47:24)

> "Four out of 22 that are using purchase orders. And they all I've customized like so this screen for everyone." (00:48:17)

> "Let's say it took him like 20 15 minutes to like make two now it's like one button right." (00:47:24)

**Child opportunities:**
- **2a.** No option to automatically split a purchase order by vendor — requires manual one-at-a-time creation
- **2b.** Each round-trip (create PO → go back → create another) wastes time and increases error risk
- **2c.** PO creation screen behavior depends on where you came from (sales order vs. estimate vs. invoice) — inconsistent experience (00:49:26)
- **2d.** No per-line vendor assignment on the PO creation screen — only a single vendor dropdown for the whole PO

---

## Opportunity 3: No place to manage shipments — Sales Orders have become the workaround

Sales Orders are the most customized app across all of Matt's accounts because Method has no dedicated shipment management area. Customers repurpose Sales Orders as shipment trackers.

**Evidence:**
> "Sales orders. Well, more more people again... they need a way to man... this manages all the shipments where we don't have a place to manage it." (00:43:37)

> "The sales order is kind of like where the magic is because this is kind of like the project manager thing." (00:41:11)

**Child opportunities:**
- **3a.** No native way to track what's been shipped vs. what's outstanding on an order
- **3b.** Fulfillment status (packed, partially shipped, fulfilled) requires HTML customization to visualize (00:40:07)
- **3c.** Sales Orders weren't designed as shipment trackers — they're being forced into a role they weren't built for

---

## Opportunity 4: Partial shipments are the norm but tracking them requires workarounds

Items from different vendors arrive at different times. SPK Associates sources materials from multiple wholesalers per deal, so items arrive at different times. But Method has no native partial shipment tracking.

**Evidence:**
> "Biggest thing with this is partial shipping. Got to think about that. It happens all the time where it's like when things are ready, that's you ship it. Like that's like think about Amazon. You order 10 things, they don't all come together. They're coming from different places." (00:42:48)

> "With the manufacturing process it's like you do it when it comes... hey, you're ready for right now to give me all the screws for that chair... but the wood's not going to be ready for two weeks." (00:15:56)

**Child opportunities:**
- **4a.** No visual indicator of shipment status (partial vs. complete) without HTML customization
- **4b.** Can't easily see at a glance which items on a sales order have shipped and which haven't
- **4c.** Need to track both what's been shipped AND what's been paid for — two different dimensions of "complete" (00:42:48)

---

## Opportunity 5: The Request for Quote (RFQ) process doesn't exist natively — manufacturing customers need spec gathering before pricing

Manufacturing workflows require gathering material specifications, design details, and build requirements BEFORE pricing. Estimates jump straight to pricing, which doesn't match the manufacturing process.

**Evidence:**
> "RFQS is a big thing for manufacturing because it's not the same... the biggest difference is not really like an overall like numeric amount. It's more like getting all the details they need for more of like the design process side of things rather than like actual pricing aspect which kind of comes in later." (00:07:27, 00:08:32)

> "They don't even get to like the actual item information till they get all that stuff from the client." (00:09:26)

**Child opportunities:**
- **5a.** Estimates are pricing-first — no structured way to capture specs before pricing
- **5b.** Multiple RFQS per deal need to consolidate into a single estimate/quote — no native support for this (00:05:29)
- **5c.** Design breakdown and build instructions need to be attached to quotes but have no native home

---

## Opportunity 6: Sales reps have to enter the same information multiple times across systems

SPK Associates sales reps gather information from customers, enter it into a spreadsheet, and then re-enter it into Method. The same data gets typed 3-5 times.

**Evidence:**
> "They have to ask the exact same questions, put in the same thing. So they're pretty much like they ask all the questions and sometimes we'll be driving and doing this then they have to put it all into a spreadsheet and put it into method." (00:31:40)

> "Game changer for them because now they don't have to repeat stuff three times. Even though because like they were doing it I think like five times more." (00:32:31)

**Child opportunities:**
- **6a.** No way to capture information on the go (mobile/voice) and have it flow into Method automatically
- **6b.** Opportunity creation requires manual data entry — can't import from external sources without custom integration
- **6c.** Sales reps in the field are often driving and can't type — they need a hands-free way to enter data

---

## Opportunity 7: Vendor communication requires excessive back-and-forth outside of Method

Before the custom Vendor Portal, SPK Associates managed vendor communication through emails and phone calls. Vendors are notoriously difficult to communicate with, and losing track of communication threatens business relationships.

**Evidence:**
> "Their vendors are like the harder people to communicate with their customers." (00:13:52)

> "This was like a like a call or an email process that would go back and forth and had to be confirmed and stuff versus now it's like they hit save pallet details when they hit that sends an email." (00:21:07)

> "Like once you lose a good wholesaler, like you that part of the business sort of thing." (00:22:01)

**Child opportunities:**
- **7a.** No native messaging/communication channel between Method users and external vendors
- **7b.** Email-based vendor communication isn't logged in Method — no audit trail
- **7c.** Vendor follow-ups are manual — no automated "you haven't responded" reminders without custom activities

---

## Opportunity 8: No native color-coding or visual status indicators in grid views

Grid-level visual status indicators (color-coded rows by fulfillment status, overdue status, etc.) are one of the most commonly requested features but require extensive HTML customization.

**Evidence:**
> "Do you know the amount of people that request coloring? ... this is all HTML... this took us like a year just like literally just the HTML stuff took us like six months." (00:45:32)

**Child opportunities:**
- **8a.** No conditional formatting for grid rows based on field values
- **8b.** HTML customization for visual indicators is expensive (6+ months of work) and fragile
- **8c.** Color-coding is requested for internal views only — report templates already support it, but the working grid doesn't

---

## Opportunity 9: Customers who need vendors and customers kept separate have no native access controls for this

Middleman/broker businesses fundamentally depend on preventing vendors from knowing customers and vice versa. Method has user permissions but no relationship-level information separation.

**Evidence:**
> "The vendors can't know their customers like that's like a huge... whenever we do anything they cannot talk to each other, see each other, know each other, who they are." (00:01:12, 00:02:31)

**Child opportunity:**
- **9a.** No native way to create "information walls" between vendor contacts and customer contacts within the same Method account

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| EDI support | Matt said one distributor asked, but he personally hasn't had requests (00:44:42) |
| ShipStation / shipping API integration | Pre-built in the catalog, already solved for customers who are ready — not an unmet need, more of a timing/readiness issue |
| Inventory tracking | SPK Associates operates with non-inventory items — "comes in and goes out immediately" (00:16:55) |
| Packing slips | SPK Associates doesn't use packing slips |

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Singletary Overlap | Europena Overlap | Yasar (Brownsafe/Kier) Overlap |
|---|---|---|---|
| **#1** No place to manage complex pipeline | No overlap | No overlap | **Yasar #1** No central place to manage project/job |
| **#2** Multi-vendor PO creation too many clicks | No overlap | No overlap | No overlap |
| **#3** No place to manage shipments | No overlap | No overlap | No overlap |
| **#4** Partial shipment tracking | No overlap | No overlap | No overlap |
| **#5** No native RFQ process | No overlap | No overlap | No overlap |
| **#6** Same info entered multiple times | **Singletary #3** Too many clicks for an order | **Europena #2** Too many steps from order to getting paid | **Yasar #1c** Jumping between screens is a hassle |
| **#7** Vendor communication outside Method | No overlap | No overlap | No overlap |
| **#8** No color-coding in grids | No overlap | No overlap | No overlap |
| **#9** Vendor-customer separation | No overlap | No overlap | No overlap |

### New Opportunities Unique to SPK Associates

The following opportunities surfaced here but NOT in previous interviews:
- **#2**: Multi-vendor PO creation — a specific implementation pain point from a PS member who's customized it for every PO-using account
- **#5**: Native RFQ process — the spec-before-pricing workflow is specific to manufacturing brokers
- **#7**: Vendor communication management — specific to middleman/broker businesses
- **#9**: Vendor-customer information separation — a business model constraint not seen in previous interviews

### Strengthened Opportunities (Corroborated Across Calls)

- **Central project/deal hub** — Yasar called it "opportunities on steroids," Matt shows SPK Associates using Opportunities as exactly that hub. The pattern is consistent: complex MWD workflows need a central hub, but the right shape depends on business complexity.
- **Too many clicks / data re-entry** — Singletary said order entry should be intuitive, Europena described too many steps, and now Matt shows sales reps entering the same data 3-5 times. The friction pattern appears at every level of the workflow.
- **No place to manage shipments** — While Yasar focused on production tracking, Matt's insight that Sales Orders are the most customized app across 22 accounts reveals the same gap from a different angle: Method has no native fulfillment/shipment management area.

---

*Document created: January 29, 2026*
*Analysis by: Claude Code*
