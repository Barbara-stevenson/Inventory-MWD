# Opportunity Solution Tree: Fuji Mats (Eric Tran, PS)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** Fujimats & Firestationfurniture Workflows/Customization Review — February 2, 2026
**Interviewee:** Eric Tran (Professional Services, Method)
**Interviewer(s):** John Miranda
**Customer Discussed:** Fuji Mats (large martial arts mat manufacturer — mats for jiu-jitsu, karate; high-profile clients including Joe Rogan)

**Important Context:** Eric is an internal PS team member with hands-on experience customizing Method for MWD accounts. He has had the Fuji Mats account for approximately 4 months and described the workflow as "hyper complicated" — "I still do not. I don't understand what's going on." This is partial evidence; a follow-up session was planned to go deeper.

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: Sales Orders are being used as the project tracker because Opportunities don't fit

Fuji Mats doesn't use the Opportunities app. Instead, they use Sales Orders as their project tracking hub — managing handoffs between sales, operations, and invoicing. This is a fundamental repurposing of the Sales Order function.

**Evidence:**
> "There's like so they treat the sales order as their opportunity, so to speak." (00:24:37)

> "So basically what happens is that um after the sales orders aspect gets approved comes into the sales orders teams take over right so for example it starts with the sales team right just making sure like hey was this correct the customer accept it boom right then what happens is that they'll ask there's a button here but it's hidden right they'll click a button they'll basically say okay this is good to go send it to operations." (00:25:35)

**Child opportunities:**
- **1a.** Opportunities app doesn't fit manufacturing workflows — Fuji Mats bypasses it entirely
- **1b.** Sales Orders require heavy customization to function as project trackers
- **1c.** Handoffs between teams (sales → operations → invoicing) require custom buttons and workflows
- **1d.** No native way to track deal progression through fulfillment stages on a Sales Order

---

## Opportunity 2: Need to accept deposits/payments before the invoice exists

Fuji Mats accepts payments toward Sales Orders before converting them to invoices. This is unusual in the industry but necessary for their workflow. Since Sales Orders aren't posting transactions, the payment is held in a custom table until invoice conversion.

**Evidence:**
> "They take payments towards sales orders which is not a that's not that's that's not normal in the in the industry in my opinion but basically instead of paying the invoice they pay the sales they pay the deposit or they pay the sales order first then when that when that sales order gets converted invoice the payment is applied." (00:27:34)

> "So the sales order is not a posting transaction right so it's completely hosted on a custom table and then once it actually you know gets um created sorry gets converted then it you know um actually applies to the real invoice." (00:27:34)

**Child opportunities:**
- **2a.** No native way to record deposits against non-posting transactions (Sales Orders, Estimates)
- **2b.** Deposit tracking requires custom tables and payment application logic
- **2c.** Prepayment workflows are common in manufacturing but not supported out of the box

---

## Opportunity 3: Hyper-complicated workflows require extensive customization on estimates

Fuji Mats' estimate screen has numerous custom fields, dropdowns, and even a micro-dashboard showing expected revenue. The complexity suggests the base Estimates app lacks flexibility for large manufacturers.

**Evidence:**
> "So first everything starts off with an estimate. They'll make an estimate, right? But as you can see, they're like, 'Where does it go? What is it for? Custom? What are we waiting for?' Right? Is it a parent? Is it a child estimate? etc." (00:23:40)

> "There are several ways you can email it. You can email, you can show it, they can show the discount, they can hide discount, they can show it as an order. There's related activities, there's related estimates, related sales orders, there's even a micro dashboard for how much money they think they'll make for the specific customer, right?" (00:24:37)

**Child opportunities:**
- **3a.** Base Estimates app doesn't support parent/child estimate relationships natively
- **3b.** No built-in customer revenue dashboard or deal forecasting at the estimate level
- **3c.** Multiple email/print template variations require customization for each output type
- **3d.** Related transaction visibility (linked estimates, sales orders, activities) requires custom builds

---

## Opportunity 4: Manufacturing and production happen outside of Method

Like other MWD accounts, Fuji Mats handles manufacturing externally. Method tracks handoffs and completion status but not the actual production process.

**Evidence:**
> "So uh Fujimat also handles the whole manufacturing side but not within method here. It's just more so um the tracking of like whether things are have been completed or are on track." (00:28:26)

> "Yes, if you really want to see like a manufacturing account... But like it's like a custom app where they're recording if we were to generalize it to record the results of that manufacturing or of that repair so to speak, right?" (00:30:06) — referring to SCS Automations as a rare exception

**Child opportunities:**
- **4a.** No native production tracking — only status tracking via custom fields and activities
- **4b.** Operations team manages manufacturing outside Method, then updates completion status manually
- **4c.** No work order or job tracking functionality for manufacturing stages

---

## Opportunity 5: International shipping via containers requires custom tracking

Fuji Mats ships internationally via shipping containers. They built a custom "Containers" app to track shipments by vessel, but this is entirely manual with no shipping API integration.

**Evidence:**
> "So containers is that these are these are ships. All these are big ships. They ship these mats right from like with these like with you know with these POS with these sales orders to their country so they can pick it up, right." (00:31:51)

> "But it's like it's not but it's there's no uh I don't know the exact I don't think there's there's no shipping API but this all handwritten right but it's like you know here you know here's the container size number date right etc right you can see and they can see it in their portal as well." (00:31:51)

**Child opportunities:**
- **5a.** No native container/freight shipping tracking — requires custom app
- **5b.** International shipping workflows (container booking, port tracking) aren't supported
- **5c.** Shipping information is manually entered with no carrier API integration

---

## Opportunity 6: Inventory dashboard exists but is display-only from QuickBooks

Fuji Mats has an inventory dashboard showing quantity on hand, committed, and expected — but it's pulling from QuickBooks with no automation or real-time updates in Method.

**Evidence:**
> "Um they technically have an inventory dashboard." (00:32:45)

> "But it's not but it's not like no no automation. It's on ClickBook side. We're just displaying it in a way where it's more palpitable. It's easier to understand." (00:32:45)

**Child opportunity:**
- **6a.** Inventory visibility in Method is read-only from QuickBooks — no native Method inventory management
- **6b.** Committed and expected quantities require custom display logic since Method doesn't calculate these natively

---

## Opportunity 7: Terms and conditions is a massive feature request

Fuji Mats, like other MWD customers, needs formal terms and conditions displayed on estimates and the customer portal.

**Evidence:**
> "Uh, it's estimates I would say, right? And terms and conditions... That's really really they're really big on that." (00:32:45)

> "It's like these are your terms of accepting. Yes, right. That's huge." (00:33:33)

**Child opportunities:**
- **7a.** Terms need to appear on customer portal with estimates
- **7b.** Some customers need terms as a separate, standalone document
- **7c.** No native terms acceptance workflow tied to estimate approval

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| Multi-warehouse management | Not discussed in detail |
| Pricing levels | Not mentioned |
| Reorder points / low stock alerts | Not mentioned |
| Barcode scanning | Not discussed |

**Note:** This interview was cut short due to time constraints. Eric noted he would need another session to fully explain Fuji Mats' complex workflow. Additional opportunities may emerge from the follow-up session.

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Yasar (Brownsafe/Kier) Overlap | Matt Shade (SPK/GT) Overlap | Fire Station (Eric) Overlap |
|---|---|---|---|
| **#1** Sales Order as project tracker | **Yasar #1** No central project hub | **Matt #2,3** Sales Orders as shipment manager | **Fire Station #1** Opportunities extended post-won |
| **#2** Deposits on non-posting transactions | No overlap | No overlap | No overlap |
| **#3** Estimates heavily customized | No overlap | **Matt #1** Complex pipeline tracking | — |
| **#4** Manufacturing outside Method | **Yasar #3** Production outside Method | **Matt** Manufacturing tracked via activities | **Fire Station #2** Same pattern |
| **#5** International container shipping | No overlap | **Matt #6** (GT) International addresses | — |
| **#6** Inventory dashboard from QBO | **Yasar #6** Multi-location inventory | **Matt** Inventory workarounds | — |
| **#7** Terms and conditions | No overlap | No overlap | **Fire Station #4** Same |

### New Opportunities Unique to Fuji Mats

The following opportunities surfaced here but NOT in previous interviews:
- **#2**: Deposits on non-posting transactions — Fuji Mats' prepayment workflow where customers pay deposits toward Sales Orders before invoice creation is a unique pattern not seen in other interviews
- **#3**: Hyper-complex estimates — Parent/child estimates, micro-dashboards, multiple email templates all in one screen suggests a level of estimate complexity beyond other accounts
- **#5**: International container shipping — While GT Simulators had international address issues, Fuji Mats' container-level shipping tracking is a distinct workflow

### Strengthened Opportunities (Corroborated Across Calls)

- **No central project hub for manufacturing** — Fuji Mats uses Sales Orders as their "opportunity," Fire Station uses actual Opportunities with extended stages, Yasar described needing "opportunities on steroids." Every MWD customer needs a project tracker, but the right shape varies.
- **Manufacturing happens outside Method** — This is now confirmed in 4 accounts across 3 PS interviews. Method is used for tracking status, not actual production management.
- **Terms and conditions** — Eric called this a "massive feature request" and both Fuji Mats and Fire Station need it. This validates feature request data from multiple angles.
- **Inventory display from QuickBooks** — Fuji Mats has an inventory dashboard that displays QBO data. This aligns with the Inventory MLP strategy of showing QuickBooks inventory in Method.

---

*Document created: February 2, 2026*
*Analysis by: Claude Code*
