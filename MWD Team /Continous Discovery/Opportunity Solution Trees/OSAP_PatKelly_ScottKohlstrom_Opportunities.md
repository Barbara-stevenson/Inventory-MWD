# Opportunity Solution Tree: OSAP (Patrick Kelly & Scott Kohlstrom, Customer)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** OSAP Discovery Call — February 20, 2026
**Interviewees:** Patrick Kelly (Customer Success Manager), Scott Kohlstrom (General Manager)
**Interviewer(s):** John Miranda
**Customer:** OSAP (custom shadow board manufacturer — foam and plastic tool control boards for aerospace, defense, and lean manufacturing; B2B; ~10 years old; owned by Blackstone Global with 5 shared business units)

**Important Context:** Patrick and ScottK are direct end customers — this is **first-party evidence**. OSAP uses Method in a narrow but deliberate way: exclusively for quoting and sales orders. They do NOT use Method for CRM (HubSpot handles that), inventory (QuickBooks Desktop Enterprise handles that), or invoicing (accounting team refuses to migrate). Their core system is a proprietary custom app called "Blue Manager" which manages all project data, design, and manufacturing. ScottK (General Manager) is actively building a Method API integration to automate quote generation. Scott Leaver (Estimator) is the primary daily Method user — he couldn't be heard on the call. This makes OSAP a "Method as middleware" account: their hub is Blue Manager, and Method is the widget sitting between it and QuickBooks. Their satisfaction is genuine but narrow — and the risks are real if Blue Manager eventually absorbs the quoting function entirely.

---

## Desired Outcome

**Retain and expand MWD account by reducing cross-system quoting friction and deepening Method's role in OSAP's workflow**

---

## Opportunity 1: Quoting requires a manual CSV export from Blue Manager and import into Method — with no preserved customer linkages or pricing validation

The #1 pain point for OSAP. Project and part data originates in Blue Manager. Getting it into Method to generate a quote requires manually exporting a CSV and importing it. Once in Method, the customer record and shipping address are not automatically linked — the estimator (Scott Leaver) must manually identify and connect the right customer and ship-to for each quote. Pricing rules must then be manually verified. The current workaround is offloading some of this to a design team in India, adding coordination overhead without solving the underlying problem.

**Evidence:**
> "That system currently manually exports project and part numbers and we manually import them into method to generate our quotes." (00:07:32)

> "It's such a tedious task to manually export our data CSV get it into method as a little bit of a process and the customer information is not linked right now. So once it's in the system then Scott comes in looks at all these new quotes and now has to figure out the right customer the right shipping address. That takes time. So this is our first immediate thing to fix." (00:18:49)

> "And then once it's in there, we got to make sure the pricing rules worked right and any other things and nothing else was missed. So it's a tedious task right now. And certainly there's too many points where mistakes happen." (00:18:49)

**Child opportunities:**
- **1a.** No API or native import path to bring structured project/part data from an external system directly into a Method quote — requires manual CSV handling
- **1b.** Customer and shipping address records in Method are disconnected from imported quote data — manual matching required for every single quote
- **1c.** Complex, custom pricing rules must be manually verified after import — no automated validation to catch pricing errors before a quote is sent
- **1d.** Manual effort has been partially delegated to an offshore design team, adding coordination overhead without eliminating error risk

---

## Opportunity 2: The end-to-end quote workflow spans three separate systems with no native handoffs — each transition is hundreds of manual clicks

When a project is ready to quote, data must travel: Blue Manager (design + specs) → Method (quote creation) → HubSpot (quote delivery to customer). There is no native connection between any of these systems. Patrick described the "fantasy" as pressing two buttons — one in Blue Manager to create the quote, one in Method to confirm and send it via HubSpot. Today that same workflow requires hundreds of clicks.

**Evidence:**
> "The perfect world for me would be, you know, the project gets put together in our blue manager software which has all the details about what needs to be built... and that when a button gets pushed in blue manager which creates the quote and then a button gets pushed in method to confirm it, which sends it out via HubSpot. So there's a record that it went out with the quote attached to it and all of that is the pressing of two buttons instead of today, which would require a few hundred clicks, right?" (00:23:17)

> "Our focus has been all the things looking hard at all the things that we do manually that take time and seeing if there's a reasonable way to automate pieces of that... every time we humans touch something there's a risk. So we're looking hard at all those touch points where we're having to do something manually and seeing if there's a reasonable amount of effort to get it to go automatically." (00:16:26)

**Child opportunities:**
- **2a.** No native way to trigger quote creation in Method from an external system — even with the API, this requires custom development investment that most customers cannot execute
- **2b.** No native quote delivery mechanism in Method — the quote must be sent via a separate platform (HubSpot) to maintain customer communication records with quote attachments
- **2c.** No audit trail in Method tying a sent quote to the customer communication log — record of delivery lives in HubSpot, record of the quote lives in Method, and they're unconnected
- **2d.** Accuracy trust is a blocker to automation — "our quotes need to be right... if we make a mistake it costs money" (00:24:32) — the manual process persists partly because there's no confidence in automated output

---

## Opportunity 3: Method's CRM capabilities were evaluated and rejected — marketing, service, and customer communications live entirely in HubSpot

OSAP went through multiple CRM systems (including Salesforce) before settling on HubSpot approximately one to two years ago. They explicitly do not use Method for CRM. HubSpot handles: marketing web pages, knowledge base with connected chatbot, tech support and ticketing, activity tracking, and drip campaigns. ScottK acknowledged that Method has been adding features they haven't been paying attention to — but HubSpot is deeply entrenched with significant investment.

**Evidence:**
> "We use HubSpot for all our CRM. So we don't utilize method for that." (00:03:22)

> "We're using it on the marketing side. We're using it to manage some of our web pages. We use it to manage our knowledge base. We have a chatbot on our website connected to our knowledge base. It's really helpful for that... we use it on the service side for tech support and ticketing and tracking our activities around there... marketing uses the database for drip campaigning and things like that." (00:05:37)

> "I don't know how much you've been — it looks like Method has been adding more and more features, too, and we're just not paying attention to it. So, apologize for that." (00:04:26)

**Child opportunities:**
- **3a.** No native knowledge base or self-service support tools in Method — customers with complex, highly technical products need structured documentation for their customers
- **3b.** No service/ticketing module in Method — post-sale customer support and tech support tracking require a separate platform
- **3c.** No marketing automation or drip campaign functionality — customer acquisition and nurturing happen entirely outside Method
- **3d.** Sending a quote from Method provides no email delivery tracking, open/click visibility, or communication record — quote history in Method and customer communication history in HubSpot are siloed

---

## Opportunity 4: Accounting team won't move invoicing to Method — they live in QuickBooks and see no reason to change

ScottK and leadership want to bring invoicing into Method to consolidate the workflow. But the shared accounting team (across 5 Blackstone Global business units) refuses. They have credit card and payment processing fully configured in QuickBooks Desktop Enterprise, they don't "live in" Method, and they view the current setup as working. One small business unit asking for a system change doesn't carry enough weight to shift a shared resource. This is an organizational blocker as much as a product gap.

**Evidence:**
> "Once the order ships, the order goes to our accounting people and accounting people live in QuickBooks and they have other systems and things they're using. So all the invoicing and payments and everything are just done in QuickBooks." (00:07:32)

> "They told me... one is all the payment things, credit card, everything else has all been set up in there. They also said that they live in there. They don't like what's this method thing? They don't live in method. So that's where I keep getting all the push back... they're basically saying everything works on my side. I don't know why I need to change." (00:22:14)

> "We believe that the invoicing piece needs to get brought over to method. It's just that's going to require a little bit more effort to get our accounting people on board. The problem is we're owned by Blackstone Global and there's about five business units here. So we share the resources of accounting and everything else... one little business unit asking for some change doesn't go very far." (00:21:03)

**Child opportunities:**
- **4a.** Method invoicing is not perceived as trustworthy or complete by accounting teams already running on QuickBooks — there is no migration path or confidence-building mechanism
- **4b.** Payment processing (credit cards, payment terms, existing setup) is fully configured in QuickBooks — Method doesn't offer a comparable payment infrastructure that accounting teams would trust
- **4c.** Organizational structure (shared accounting across multiple BUs under a parent company) makes system change decisions for a single BU nearly impossible without top-down mandate

---

## Opportunity 5: Shipping has no connection to Method — carrier apps are used on a separate computer and tracking data never enters the system

After a sales order is created in Method, shipping is handled entirely outside of it — on a dedicated shipping computer using FedEx and UPS carrier apps. Tracking numbers are obtained manually and are not captured in Method. ScottK explicitly identified shipping as the next gap on his list after quoting and inventory.

**Evidence:**
> "Shipping, we have a separate computer for shipping. It's all done externally. So if it's FedEx, we use their app. If it's UPS, we use their app... it's a little bit of a manual process there to get the actual tracking numbers and things, but our order desk person handles all that logistics." (00:10:47)

> "And then the next things I think would be better inventory control and then shipping and where we can notify and stuff. So we understand where all our gaps are and just trying to figure out, kind of taking chunks of it at a time." (00:13:08)

**Child opportunities:**
- **5a.** No native carrier integration in Method — shipping labels and tracking numbers are generated in separate carrier systems with no sync back
- **5b.** No way to capture shipment confirmation or tracking data on a sales order in Method — order closure requires crossing over to QuickBooks
- **5c.** No outbound customer shipping notifications triggered from Method — customers must be updated through a separate communication channel

---

## Opportunity 6: No native forecasting or commission reporting — leadership wants these from Method data but must custom-build them through PS

Leadership at OSAP wants to use Method's transaction data for two business intelligence needs: sales forecasting and commission reporting. Neither exists natively. Both are being built as custom solutions through PS developer Alex. While Alex is highly trusted and effective, dependency on a single developer for core reporting creates fragility.

**Evidence:**
> "We'd like to be able to do more forecasting and stuff. Um and we've been sort of working on that. That's kind of our next thing to work on with Alex. And then this whole thing about generating commission reports through method instead. Um these are some newer things we've been working with Alex on." (00:21:03)

**Child opportunities:**
- **6a.** No native sales forecasting reports based on quote pipeline and historical sales order data in Method
- **6b.** No commission calculation or tracking built into the quote/sales order workflow — reps have no visibility into earned commissions without a custom build
- **6c.** Leadership's reporting needs are entirely dependent on a PS developer — there is no self-serve business intelligence in Method for operational leaders

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| Inventory management in Method | OSAP manages all inventory in QuickBooks Desktop Enterprise and has explicitly signaled they may move inventory control into Blue Manager. "We're going to look more into possibly moving the inventory control over to our software, too." (00:11:56) Inventory in Method is not a current use case or near-term desire. |
| Method CRM replacing HubSpot | They have significant investment in HubSpot and are not seeking a replacement. The CRM gap is documented (Opportunity 3) but the opportunity is awareness/retention, not a feature request to replace HubSpot directly. |
| Blue Manager as a generalizable integration pattern | ScottK's API integration work is connecting OSAP's proprietary custom software — not a pattern that generalizes to a native Method feature. This is a PS/API enablement story specific to this account. |

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Singletary Overlap | Europena Overlap | Yasar (Brownsafe/Kier) Overlap | Fuji Mats (Eric) Overlap | Matt Shade (SPK/GT) Overlap | Liquid Medlock (Toby) Overlap |
|---|---|---|---|---|---|---|
| **#1** Manual data import / too many error points in quoting | No overlap | No overlap | No overlap | No overlap | No overlap | **Liquid Medlock #1 & #2** Human error, no validation; manual reconciliation |
| **#2** Multi-system workflow with no native handoffs | No overlap | **Europena #2** Too many steps order to payment | No overlap | No overlap | **Matt #3** No place to manage shipments | **Liquid Medlock #3** Manual shipment upload to CRM |
| **#3** Method CRM rejected in favor of HubSpot | No overlap | No overlap | No overlap | No overlap | No overlap | No overlap — **NEW** |
| **#4** Accounting won't move invoicing from QuickBooks to Method | **Singletary #7** QB and inventory system conflict | No overlap | No overlap | No overlap | No overlap | **Liquid Medlock #8** Operations vs. accounting source of truth conflict |
| **#5** Shipping outside Method, no tracking data captured | No overlap | No overlap | No overlap | No overlap | **Matt #3** No place to manage shipments | **Liquid Medlock #3** Manual shipment upload |
| **#6** No native forecasting or commission reporting | No overlap | No overlap | No overlap | No overlap | No overlap | No overlap — **NEW** |

### New Opportunities Unique to OSAP

The following opportunities surfaced here but NOT in previous interviews:

- **#3: Method CRM losing to HubSpot** — This is the first interview where a customer explicitly described evaluating and rejecting Method CRM in favor of a third-party CRM, and articulated the specific features driving that decision (knowledge base, chatbot, ticketing, drip campaigns). Other accounts may be in the same situation but haven't said so directly. This is a significant competitive signal.
- **#6: Commission reporting and sales forecasting** — No prior interview raised these as Method gaps. These are operational intelligence needs that sit on top of the quote and order data Method already holds, suggesting there's an untapped reporting opportunity for leadership users.

### Strengthened Opportunities (Corroborated Across Calls)

- **Accounting teams won't leave QuickBooks for invoicing** — This pattern has now appeared in three separate interviews: Singletary (QB sync conflict across implementations), Liquid Medlock (operations vs. accounting source of truth tension), and now OSAP (shared accounting team refuses to adopt Method). This is systemic — it's not a customization problem, it's a trust and adoption gap in Method's invoicing experience.
- **Shipping is invisible inside Method** — Both Liquid Medlock (manual nightly upload of warehouse shipment reports) and OSAP (separate shipping computer with carrier apps) confirm that shipment status and tracking never make it back into Method. Matt Shade also flagged no shipment management. This is three accounts, three different contexts, same gap.
- **Manual processes are the primary source of risk and error** — Every interview has surfaced some version of "every time a human touches it, there's a risk." OSAP's Patrick Kelly stated it as a guiding principle: "every time we humans touch something there's a risk." This validates that automation and data connectivity — not just feature parity — are what MWD customers are actually asking for.

### Notable Insight: OSAP as a "Method as Middleware" Use Case

OSAP represents a use pattern not seen in other interviewed accounts: Method is not their hub — it's a widget. Blue Manager is their hub. QuickBooks is their financial ledger. HubSpot is their CRM. Method sits in the middle handling quoting and sales order generation because it offers customization that QuickBooks lacks and a cleaner interface than going directly to accounting systems.

This is worth watching. ScottK explicitly said: *"I think our software is going to end up being the hub and you're the widget between the financial side of things."* (00:11:56)

If Blue Manager eventually absorbs quoting via the API integration ScottK is building, Method could be reduced to a pass-through — or eliminated from the workflow entirely. The retention play here is making Method's quoting and sales order experience so good that displacing it creates more friction than value. The current state does not confidently support that.

---

*Document created: February 20, 2026*
*Analysis by: Claude Code*
