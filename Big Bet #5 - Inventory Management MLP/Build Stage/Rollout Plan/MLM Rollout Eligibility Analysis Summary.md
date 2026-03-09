# Multi-Location Management (MLM) Rollout Eligibility Analysis

**Spike Investigation:** [PL-58840](https://method.atlassian.net/browse/PL-58840)
**Completed:** November 21, 2025
**Analyst:** Nirmith Victor D'Almeida

## Executive Summary

This analysis evaluated 32 unique Method accounts (across two target segments) to determine eligibility for the Multi-Location Management (MLM) rollout based on existing screen customizations. The investigation assessed whether customizations on inventory-related screens would break or degrade the new MLM workflows.

### Key Findings

- **✅ Fully Eligible:** 8 accounts (25%)
- **🟡 Generally Functional:** 10 accounts (31%)
- **⚠️ Partially Broken Flows:** 8 accounts (25%)
- **❌ Blocked/Unusable:** 6 accounts (19%)

**Important Note:** Some accounts marked with ✅ show "Eligibility = No" in the original data because they have at least one customized screen. However, the spike investigation determined these customizations won't break MLM flows (mostly grid column changes). These accounts CAN receive the rollout BUT must be informed before release.

---

## Eligibility Classification System

| Symbol | Status | Description | Rollout Recommendation |
|--------|--------|-------------|------------------------|
| ✅ | Fully Functional | No customizations OR customizations won't impact MLM flows | Safe for rollout with customer notification |
| 🟡 | Generally Functional | Minor issues, still usable with some additional work | Rollout possible with monitoring |
| ⚠️ | Partially Broken | Some flows will fail or behave inconsistently | Requires customer consultation before rollout |
| ❌ | Blocked | Completely broken/unusable flows | Not eligible for rollout |

---

## Section 1: Accounts that Requested Inventory Features
**Priority:** High (these customers explicitly asked for inventory features)
**Total Accounts:** 15

### ✅ Fully Eligible Accounts (5)

| Account Name | Company Name | Feature Request | Customized Screens | Analysis Notes |
|--------------|--------------|-----------------|-------------------|----------------|
| dylanwilliamscpa | Park Models & Modulars, LLC | SOS | 0 | No customizations - fully eligible |
| miminternationalinc | MIM International, Inc. | SOS | 0 | No customizations - fully eligible |
| nuewal | NUEWAL Inc. | SOS | 0 | No customizations - fully eligible |
| mcbautobodyandcustomsltd | MCB Autobody and Customs Ltd | Locations in Transactions | 0 | No customizations - fully eligible |
| sanecotecltd | SanEcoTec Ltd. | Katana | 1 (Invoice) | Special case - only change is printing packing slip. Consultant confirmed flows won't break |

**Rollout Impact:** These 5 accounts (33% of this segment) can be rolled out immediately with customer notification.

---

### 🟡 Generally Functional (5)

| Account Name | Company Name | Feature Request | Customized Screens | Analysis Notes |
|--------------|--------------|-----------------|-------------------|----------------|
| refexpertsandhvacllc | REF EXPERTS AND HVAC LLC | Warehouse | 3 (Items List, PO List, Invoice) | New Invoice customization will not prevent flows but requires additional customizations to match |
| cooksdoorsandmouldingsinc | Cooks Doors and Mouldings Inc | SOS | 4 (SO, SO List, PO, Invoice) | Complexity is dropdowns and datetime pickers - otherwise everything will work |
| hydrospraywashsystemsinc | HydroSpray Wash Systems Inc | SOS | 4 (Items List, SO, PO, Invoice) | Should be OK for most part but PO, Invoice and SO could be missing some flows from other teams |
| prosourcegroup | Pro-Source Group | Warehouse | 4 (NIP, Items List, SO, Invoice) | Should be OK - common occurrence is ship method dropdowns in SO. Rest of screens seem to be copies of stock apps |
| carolinalightinggroup | Carolina Lighting Group LLC | SOS | 3 (SO, PO, Invoice) | Screens are dated and missing sync widgets/new Job changes from SD - OK to bring changes but requires monitoring |

**Rollout Impact:** These 5 accounts (33% of this segment) can likely receive rollout with enhanced monitoring and potential follow-up customization work.

---

### ⚠️ Partially Broken Flows (4)

| Account Name | Company Name | Feature Request | Customized Screens | Analysis Notes |
|--------------|--------------|-----------------|-------------------|----------------|
| a2zsupplies | A2Z Supplies LLC | SOS | 3 (NIP, Items List, Invoice) | Heavy customizations on New/Edit Inventory Part and Items List - Invoice is fine |
| lancasterandassociatesinc2 | Lancaster & Associates, Inc. | SOS | 6 (Items List, SO, SO List, PO, PO List, Invoice) | Heavy customization in Invoices and Sales Order List (print PDFs). Other screens OK for changes |
| botanaway | BotanaWay, Inc. | Katana | 7 (NIP, SO, SO List, PO, PO List, Invoice, Bill) | Heavy customizations in Invoice and Items List. Items List uses custom grid designs. Other screens OK |
| ebamethod | EUROBOOR USA INCORPORATED | Warehouse | 5 (NIP, Items List, SO, PO, Invoice) | Large number of customizations on Invoices and Purchase Orders using custom table structures. SO and Bills not customized |

**Rollout Impact:** These 4 accounts (27% of this segment) require customer consultation and potentially custom migration plans before rollout.

---

### ❌ Blocked Accounts (1)

| Account Name | Company Name | Feature Request | Customized Screens | Analysis Notes |
|--------------|--------------|-----------------|-------------------|----------------|
| cypressengine | Cypress Engine Accessories, LLC | SOS | 7 (NIP, Items List, SO, SO List, PO, PO List, Invoice) | WAY too many flows: Invoice and Item List have multiple API calls. NIP heavily customized with different designs for QOH/On Order. SO/PO have unique components and flows that will break |

**Rollout Impact:** cypressengine (7% of this segment) cannot receive rollout without major rework.

---

## Section 2: Target ICP Wholesale & Distribution Accounts
**Priority:** Medium (target ICP accounts for proactive outreach)
**Total Accounts:** 21 (3 overlap with Section 1)

### ✅ Fully Eligible Accounts (3)

| Account Name | Company Name | Customized Screens | Analysis Notes |
|--------------|--------------|-------------------|----------------|
| crimsonimaging | Crimson Imaging Supplies LLC | 1 (Items List) | Only column customization - fine |
| hendersonenterprises | Henderson Enterprises | 1 (Invoice) | Exact same copy for customized Invoices Screen - fine |
| aosolutions | Solutions Office Interiors, Inc. | 0 | No customizations on any screen - good to go |

**Note:** cardmonster (Card Monster Pty Ltd) is a cancelled account and excluded from analysis.

**Rollout Impact:** These 3 accounts (15% of active accounts in this segment) can be rolled out immediately with customer notification.

---

### 🟡 Generally Functional (8)

| Account Name | Company Name | Customized Screens | Analysis Notes |
|--------------|--------------|-------------------|----------------|
| sitepieces2 | Site Pieces | 1 (Invoice) | API test flow in invoices app |
| fullcirclesolutionsllc | Full Circle Solutions LLC | 2 (SO, SO List) | Customization on New/Edit Sales Orders and SO List has columns |
| area51sportsltd | Area 51 Sports | 3 (SO, PO, Invoice) | SO and Invoice are pretty customized |
| dolphinheatexchangerusa | DOLPHIN HEAT EXCHANGER USA Inc | 4 (Items List, SO, SO List, Invoice) | Sales Order New Edit Screen has a LOT of customizations and flows that we can break |
| metkonusainc | Metkon USA, Inc. | 5 (Items List, SO, PO, PO List, Invoice) | Flows seem OK for most screens but there are a few that are dated and could cause conflicts when bringing in our flows |
| hydrospraywashsystemsinc | HydroSpray Wash Systems Inc | 4 (Items List, SO, PO, Invoice) | Should be OK for most part, Items List is green (also appears in Section 1) |
| prosourcegroup | Pro-Source Group | 4 (NIP, Items List, SO, Invoice) | Primarily due to customization and print packing slip flows in Invoice and Sales Order (also appears in Section 1) |
| carolinalightinggroup | Carolina Lighting Group LLC | 3 (SO, PO, Invoice) | Heavy customizations for Invoices, SO and PO (also appears in Section 1 as ✅) |

**Rollout Impact:** These 8 accounts (40% of this segment) can likely receive rollout with enhanced monitoring.

---

### ⚠️ Partially Broken Flows (4)

| Account Name | Company Name | Customized Screens | Analysis Notes |
|--------------|--------------|-------------------|----------------|
| dtsdirect | DTS Direct, LLC | 5 (Items List, SO, SO List, PO, Invoice) | Heavy customization and flows in Invoice. Items List has separate flow that sets On Hand columns to 0 - might be an issue with our columns |
| tppincrestore20250710 | TPP, Inc (entry 1) | 4 (SO, PO, Invoice, Bill) | PO has its own flows and customizations |
| southgateprocessequipmentinc | Southgate Process Equipment, Inc. | 2 (PO, Invoice) | Heavy customization in New/Edit PO with rbLineType. Heavy customization in New/Edit Invoice |
| unicellsupply2 | Unicell Janitorial Supplies | 4 (NIP, Items List, Invoice, Bill) | Heavy customization flows for Invoice, NIP, and Bills. Bills also have tax calculation like Invoices BUT seem to be missing some flows from main screen |

**Rollout Impact:** These 4 accounts (20% of this segment) require customer consultation before rollout.

---

### ❌ Blocked Accounts (5)

| Account Name | Company Name | Customized Screens | Analysis Notes |
|--------------|--------------|-------------------|----------------|
| progressivewestman372 | Progressive Westman | 3 (NIP, Items List, Invoice) | Blocking primarily due to heavy customizations |
| ensureaseal2 | Ensure-A-Seal | 2 (SO, PO) | Heavy customizations for SO and PO |
| wearingwilliamsltd2 | Wearing Williams Limited | 8 (NIP, Items List, SO, SO List, PO, PO List, Invoice, Bill) | Heavy customizations across all screens except Items List, SO List and PO List |
| flowmeasurementservices | Flow Measurement Services | 2 (PO, Invoice) | Blocking primarily due to multiple dynamic customization flows between their 2 screens. Invoice has mobile flows that are different and dated. PO has medium customization within the screen |
| gitchsportswearco1restore20250919 | Gitch Sportswear (entry 1) | 6 (SO, SO List, PO, PO List, Invoice, Bill) | Heavy customizations across all screens: Invoice has new sections and flows, Bills have different tax calculation flows and Add Item Flows, PO List has custom columns and flows, New/Edit PO has different flow extensions and customizations, SO has different flows in function button clicks. SOL is fine |

**Rollout Impact:** These 5 accounts (25% of this segment) cannot receive rollout without major rework.

---

## Accounts Appearing in Both Segments

Three accounts appear in both "Requested Features" and "Target ICP" lists:

### prosourcegroup (Pro-Source Group)
- **Section 1 Rating:** 🟡 Generally Functional
- **Section 2 Rating:** 🟡 Generally Functional
- **Analysis:** Should be OK - common occurrence is ship method dropdowns in SO. Rest of screens seem to be copies of stock apps. Some concern about print packing slip flows in Invoice and Sales Order.
- **Recommendation:** Rollout possible with enhanced monitoring

### carolinalightinggroup (Carolina Lighting Group LLC)
- **Section 1 Rating:** 🟡 Generally Functional (screens are dated, OK to bring changes but requires monitoring)
- **Section 2 Rating:** 🟡 Generally Functional (heavy customizations for Invoices, SO, PO)
- **Analysis:** Screens are dated and missing sync widgets and new Job changes from SD. While safe to introduce new MLM flows, the customizations warrant enhanced monitoring during rollout.
- **Recommendation:** Phase 2 (Monitored Rollout) - rollout possible with enhanced monitoring

### hydrospraywashsystemsinc (HydroSpray Wash Systems Inc)
- **Section 1 Rating:** 🟡 Generally Functional
- **Section 2 Rating:** 🟡 Generally Functional
- **Analysis:** Should be OK for most part but PO, Invoice and SO could be missing some flows from other teams. Items List is in good shape.
- **Recommendation:** Rollout possible with enhanced monitoring

---

## Alpha Rollout Accounts

This section identifies accounts eligible for the Alpha rollout of Multi-Location Management (MLM), combining all ✅ Fully Eligible and 🟡 Generally Functional accounts from both target segments.

**Total Alpha Rollout Pool:** 18 unique accounts (56% of total evaluated accounts)

---

### Tier 1: Fully Eligible (8 accounts)
**Risk Level:** Low
**Rollout Readiness:** Immediate

These accounts have no customizations or only non-breaking customizations. They can receive MLM immediately with standard customer notification.

| Account Name | Company Name | Source Segment | Feature Request | Customized Screens |
|--------------|--------------|----------------|-----------------|-------------------|
| dylanwilliamscpa | Park Models & Modulars, LLC | Requested Features | SOS | 0 |
| miminternationalinc | MIM International, Inc. | Requested Features | SOS | 0 |
| nuewal | NUEWAL Inc. | Requested Features | SOS | 0 |
| mcbautobodyandcustomsltd | MCB Autobody and Customs Ltd | Requested Features | Locations in Transactions | 0 |
| sanecotecltd | SanEcoTec Ltd. | Requested Features | Katana | 1 (Invoice) |
| crimsonimaging | Crimson Imaging Supplies LLC | Target ICP W&D | N/A | 1 (Items List) |
| hendersonenterprises | Henderson Enterprises | Target ICP W&D | N/A | 1 (Invoice) |
| aosolutions | Solutions Office Interiors, Inc. | Target ICP W&D | N/A | 0 |

**Tier 1 Actions:**
1. Send advance notification of MLM release (1 week prior)
2. Provide MLM feature documentation and training materials
3. Schedule post-rollout check-ins (1 week after release)
4. Monitor for unexpected issues during first 2 weeks

---

### Tier 2: Generally Functional (10 accounts)
**Risk Level:** Medium
**Rollout Readiness:** With Enhanced Monitoring

These accounts have customizations that require monitoring but are expected to function properly with MLM. Includes 3 accounts that appear in both segments.

| Account Name | Company Name | Source Segment | Feature Request | Customized Screens | Notes |
|--------------|--------------|----------------|-----------------|-------------------|-------|
| refexpertsandhvacllc | REF EXPERTS AND HVAC LLC | Requested Features | Warehouse | 3 | New Invoice customization requires additional work |
| cooksdoorsandmouldingsinc | Cooks Doors and Mouldings Inc | Requested Features | SOS | 4 | Dropdowns and datetime pickers |
| hydrospraywashsystemsinc ⭐ | HydroSpray Wash Systems Inc | Both Segments | SOS | 4 | Missing some flows from other teams |
| prosourcegroup ⭐ | Pro-Source Group | Both Segments | Warehouse | 4 | Ship method dropdowns, print packing slip flows |
| carolinalightinggroup ⭐ | Carolina Lighting Group LLC | Both Segments | SOS | 3 | Dated screens, missing sync widgets |
| sitepieces2 | Site Pieces | Target ICP W&D | N/A | 1 | API test flow in invoices |
| fullcirclesolutionsllc | Full Circle Solutions LLC | Target ICP W&D | N/A | 2 | SO customizations |
| area51sportsltd | Area 51 Sports | Target ICP W&D | N/A | 3 | SO and Invoice customized |
| dolphinheatexchangerusa | DOLPHIN HEAT EXCHANGER USA Inc | Target ICP W&D | N/A | 4 | Heavy SO customizations |
| metkonusainc | Metkon USA, Inc. | Target ICP W&D | N/A | 5 | Dated screens that may conflict |

⭐ = Appears in both "Requested Features" and "Target ICP" segments

**Tier 2 Actions:**
1. Conduct pre-rollout customer calls to explain MLM changes and set expectations
2. Provide enhanced documentation on potential conflicts specific to their customizations
3. Offer dedicated support window during rollout (first 48 hours)
4. Schedule follow-up customization work if needed (within 1 week of rollout)
5. Monitor closely for 2 weeks post-rollout with daily check-ins for first 3 days
6. For ⭐ accounts: Extra attention due to dual-segment presence

---

## Critical Notes for Product Team

### P.S. from Spike Investigation
**"The Green marked accounts with Eligibility being No is basically saying the flow will work since most of those changes could be column changes in grid BUT it will not be recommended to release without the customers being informed prior to release"**

This means:
- CSV "Eligible = No" flag is overly conservative
- Many accounts with customizations can still receive rollout
- Customer notification is CRITICAL before release
- Don't use CSV eligibility flag alone - use spike analysis ratings

### Accounts with Resolved Ratings
Three accounts appear in both segments and have been assigned consistent rollout strategies:
1. **carolinalightinggroup** - Rated 🟡 in Section 1 (dated screens, safe to update but requires monitoring) and 🟡 in Section 2 (heavier customizations). Overall strategy: **Tier 2 - Alpha Rollout with Enhanced Monitoring**
2. **prosourcegroup** - Rated 🟡 in both sections. Common customizations like ship method dropdowns. Overall strategy: **Tier 2 - Alpha Rollout with Enhanced Monitoring**
3. **hydrospraywashsystemsinc** - Rated 🟡 in both sections. Generally functional with some missing flows. Overall strategy: **Tier 2 - Alpha Rollout with Enhanced Monitoring**

### Customization Patterns That Break MLM

Based on the analysis, these customization types cause the most issues:

1. **Heavy API integrations** in transaction screens (Invoice, SO, PO)
2. **Custom table structures** for inventory data
3. **Complex print PDF workflows** in Sales Orders and Invoices
4. **Custom quantity/location calculation flows**
5. **Multiple dynamic flows** across related screens
6. **Heavy modifications to New/Edit Inventory Part** screens

---

## Next Steps

1. **Create customer communication templates** for Alpha Rollout (Tier 1 and Tier 2)
2. **Develop rollout monitoring checklist** for Tier 1 and Tier 2 accounts
3. **Prepare enhanced support resources** for Tier 2 accounts (especially the 3 ⭐ accounts that appear in both segments)
4. **Execute Alpha Rollout** following the 4-week timeline recommendation
5. **Schedule consultation calls** with ⚠️ Partially Broken Flows accounts (8 accounts) to assess business impact
6. **Document exclusion rationale** for ❌ Blocked accounts (6 accounts) and explore alternative solutions
7. **Gather Alpha feedback** in Week 4 and adjust strategy for remaining 14 accounts

---

**Document Created:** December 2, 2025
**Related Jira Epic:** [PL-56600 - Multi-Location MVP](https://method.atlassian.net/browse/PL-56600)
**Source Data:** `MLM Rollout Customized Accounts List` CSVs in this folder
