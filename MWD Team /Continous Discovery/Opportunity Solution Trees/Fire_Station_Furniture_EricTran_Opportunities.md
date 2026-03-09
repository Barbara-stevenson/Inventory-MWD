# Opportunity Solution Tree: Fire Station Furniture (Eric Tran, PS)

*Framework: Opportunity Solution Trees from "Continuous Discovery Habits" by Teresa Torres. Opportunities are unmet customer needs, pain points, and desires — framed from the customer's perspective and grounded in what was actually said. They are NOT solutions.*

**Source Interview:** Fujimats & Firestationfurniture Workflows/Customization Review — February 2, 2026
**Interviewee:** Eric Tran (Professional Services, Method)
**Interviewer(s):** John Miranda
**Customer Discussed:** Fire Station Furniture (B2B fireproof furniture manufacturer — sells to fire stations, targets wildfire-prone states)

**Important Context:** Eric is an internal PS team member with hands-on experience customizing Method for MWD accounts (majority of his accounts fall in this vertical). His opportunities are **proxy evidence** — observed patterns from building customizations, not a single customer's firsthand story. Fire Station Furniture has been a longtime customer with a 4-person team (sales, operations, 2 customer support).

---

## Desired Outcome

**Reduce churn in MWD vertical by addressing inventory management gaps**

---

## Opportunity 1: Opportunities app doesn't track what happens after the deal is won

The standard Opportunities app focuses on pre-sale stages (prospecting, qualification, etc.) but manufacturing customers need to track post-acceptance steps: vendor contact, manufacturing progress, payment, shipping. Fire Station Furniture required custom stages to extend beyond "deal won."

**Evidence:**
> "I think what we're what we're lacking a lot in the opportunities for the specific customer was that there was nothing after the deal was won right there's nothing that tracks the deal was one, right? After the deal is won, it's like what else is next, right?" (00:09:15)

> "So we've expanded the opportunities beyond that to capture that information." (00:10:11)

**Child opportunities:**
- **1a.** No native stages for post-acceptance workflow (vendor contact, manufacturing, shipping, payment)
- **1b.** Opportunity stages like "prospecting" are irrelevant for manufacturers with existing customer bases — "all that all that all that stock stuff that prospecting they don't use it" (00:09:15)
- **1c.** Customization required to track handoffs between different team members (sales → operations → invoicing)

---

## Opportunity 2: No native way to track manufacturing progress — activities are the workaround

Fire Station Furniture tracks manufacturing completion status entirely through activities. There's no structured way to track production milestones, part completion, or assembly progress within Method.

**Evidence:**
> "The only part it's really tracked is through the activities, right? That's how they're tracking it. Like, hey, uh, headrest completed, headrest shipped, right? Sunbelt delivery, stitch pallet approved, right? That's their current way. There's no current way of being able to track in method." (00:11:06)

> "We haven't built that way just because it's kind of been separate from their system." (00:12:21)

**Child opportunities:**
- **2a.** No production milestone tracking — just free-form activities
- **2b.** Can't see at a glance what parts/components are complete vs. pending
- **2c.** Manufacturing details tracked in a "different system" outside Method — workflow breaks between estimate acceptance and invoicing

---

## Opportunity 3: Tracking numbers are a very common request but have no native home

Customers frequently need to provide tracking numbers to their customers, but there's no dedicated field for this. Fire Station puts tracking numbers in memos and invoice notes as a workaround.

**Evidence:**
> "The other the other very common asks that we get for these type of customers, right, is we put in a tracking number for them that's visible for the customer and internally. That's a that's another thing that we don't have." (00:14:03)

> "But I guess what the the thing I'm just trying to point out is that tracking number is a very commonly requested thing especially with these type of companies right they'll use it." (00:14:03)

**Child opportunities:**
- **3a.** No dedicated tracking number field on transactions
- **3b.** Tracking numbers need to be visible on portals, print templates, and emails — currently requires custom fields
- **3c.** No integration with shipping carriers for auto-population — "most of the time it's just an input" (00:14:51)

---

## Opportunity 4: Terms and conditions is a massive feature request

MWD customers need formal terms and conditions for their estimates and orders. This is currently handled through customization but is one of the most requested features.

**Evidence:**
> "And terms and conditions. You already have that in there. It's terms and conditions. That's really really they're really big on that." (00:33:33)

> "It's like these are your terms of accepting. Yes, right. That's huge." (00:33:33)

**Child opportunities:**
- **4a.** Terms need to appear on the customer portal alongside estimates
- **4b.** Some customers need terms as a completely separate document — "sometimes they'll ask for it as a separate document completely" (00:33:33)
- **4c.** No native terms acceptance workflow built into the estimate approval process

---

## Opportunity 5: Logo approval workflow required a custom app

Fire Station Furniture offers custom embroidered logo furniture. They needed a way for customers to approve logo designs before production, but this had to be built as a custom app ("Proofs").

**Evidence:**
> "So I created a custo something called proofs, right? Where basically they can upload logos for their customers to sign on their portal, right? Just to make the process a little bit easier." (00:05:38)

> "They're able to basically email out a proof to their customer, right? And they're able to accept or reject it and then give their reason. Very similar to the estimate process." (00:06:32)

**Child opportunities:**
- **5a.** No native approval workflow for design/spec sign-offs between estimate and production
- **5b.** Custom furniture manufacturers need customer approval on visual elements before building
- **5c.** The proof approval step fits "in between the estimate to invoice" but has no natural home (00:06:32)

---

## Opportunity 6: Previous payment portal issues caused permanent trust damage

Fire Station stopped using Method's payment portal due to historical issues with the payment processor, even though the issues have since been fixed. They now collect payment through QuickBooks.

**Evidence:**
> "This one used to, but we stopped because because payment portal kept having issues... Like like credit cards wouldn't wouldn't apply, fees kept like things kept dropping, right? Like like payments wouldn't be recorded properly. But this is before we had the update." (00:15:39)

> "They gave up like we don't want this Eric. I'm like okay sorry right but it's it's fixed now... but like they they they gave up on it just how bad our bad bad our payment processor was like a couple years back." (00:16:23)

**Child opportunity:**
- **6a.** Past reliability issues have lasting impact on customer trust and adoption — even fixed features may not be re-adopted

---

## Opportunities NOT Included (Insufficient Evidence)

| Potential Opportunity | Why Excluded |
|---|---|
| Multi-warehouse management | Not discussed — Fire Station appears to operate from a single location |
| Inventory visibility | Not mentioned as a pain point |
| Pricing levels | Not discussed |
| Barcode scanning | Not mentioned |

---

## Cross-Reference: Opportunities That Also Appear in Other Interviews

| This Call | Yasar (Brownsafe/Kier) Overlap | Matt Shade (SPK/GT) Overlap |
|---|---|---|
| **#1** Opportunities app lacks post-won stages | **Yasar #2** Opportunities force irrelevant fields (close date, probability) | **Matt #1** (SPK) No native place for complex pipeline |
| **#2** Manufacturing tracked via activities only | **Yasar #3** Production happens outside Method | **Matt #3** (SPK) No place to manage shipments |
| **#3** Tracking numbers commonly requested | No overlap | No overlap |
| **#4** Terms and conditions massive request | No overlap | No overlap |
| **#5** Custom approval workflow needed | No overlap | **Matt** Custom "proofs" app pattern similar |
| **#6** Payment portal trust issues | No overlap | No overlap |

### New Opportunities Unique to Fire Station Furniture

The following opportunities surfaced here but NOT in previous interviews:
- **#5**: Custom approval workflow for visual/design sign-offs — specific to furniture manufacturers offering customization
- **#6**: Historical reliability issues causing permanent trust damage — a customer retention insight about the long-term impact of past bugs

### Strengthened Opportunities (Corroborated Across Calls)

- **Central project hub / post-sale tracking** — Yasar, Matt, and now Eric all show that Opportunities (or Sales Orders) are being used as project trackers because there's no native post-deal-won tracking. The core issue is the same: Method's transaction apps don't support the full manufacturing lifecycle.
- **Manufacturing happens outside Method** — Fire Station, like Yasar's accounts, tracks manufacturing completion via activities because Method has no production tracking. This is the third PS interview confirming the gap.
- **Terms and conditions** — Eric explicitly called this a "massive feature request" for MWD customers, adding PS validation to feature request data.

---

*Document created: February 2, 2026*
*Analysis by: Claude Code*
