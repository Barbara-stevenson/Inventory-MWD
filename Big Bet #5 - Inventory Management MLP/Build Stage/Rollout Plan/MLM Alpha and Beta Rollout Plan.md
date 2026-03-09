# Multi-Location Management (MLM) Alpha and Beta Rollout Plan

**Document Created:** December 2, 2025
**Analysis Source:** MLM Rollout Eligibility Analysis Summary + Wholesale & Distribution CSV
**Related Jira Epic:** [PL-56600 - Multi-Location MVP](https://method.atlassian.net/browse/PL-56600)
**Spike Investigation:** [PL-58840](https://method.atlassian.net/browse/PL-58840)

---

## Executive Summary

This rollout plan identifies **34 Alpha accounts** and **27 Beta accounts** eligible for the Multi-Location Management (MLM) feature release across two phases:

- **Alpha Rollout:** 34 accounts with strong ICP fit and minimal/no customization conflicts
  - Phase 1 (Tier 1): 24 accounts - Fully eligible, low risk
  - Phase 2 (Tier 2): 10 accounts - Generally functional, enhanced monitoring required

- **Beta Rollout:** 27 accounts that are technically eligible but don't match ideal customer profile
  - Eligible=Yes (no blocking customizations) but ICP Fit Verified=No
  - Includes regulated industries (food/beverage, cannabis, tobacco) and edge cases

---

## Table of Contents

1. [Alpha Rollout Strategy](#alpha-rollout-strategy)
2. [Beta Rollout Strategy](#beta-rollout-strategy)

---

## Alpha Rollout Strategy

### Overview

**Total Alpha Accounts:** 34 unique accounts
**Risk Level:** Low to Medium
**Timeline:** 4 weeks (2-week Tier 1, 2-week Tier 2)

Alpha accounts meet BOTH criteria:
- ✅ **ICP Fit Verified = Yes**: Distribute non-regulated, non-perishable finished goods
- ✅ **Eligible = Yes**: No customizations OR customizations won't break MLM flows

---

### Phase 1 - Tier 1: Fully Eligible Accounts (24 accounts)

**Risk Level:** LOW
**Rollout Week:** Week 1-2
**Characteristics:** Zero customizations OR only non-breaking customizations (grid columns, minor layout changes)

#### From Original Eligibility Analysis (8 accounts)

| # | Account Name | Company Name | Source | Feature Request | Screens |
|---|--------------|--------------|--------|-----------------|---------|
| 1 | dylanwilliamscpa | Park Models & Modulars, LLC | Requested Features | SOS | 0 |
| 2 | miminternationalinc | MIM International, Inc. | Requested Features | SOS | 0 |
| 3 | nuewal | NUEWAL Inc. | Requested Features | SOS | 0 |
| 4 | mcbautobodyandcustomsltd | MCB Autobody and Customs Ltd | Requested Features | Locations in Transactions | 0 |
| 5 | sanecotecltd | SanEcoTec Ltd. | Requested Features | Katana | 1 |
| 6 | crimsonimaging | Crimson Imaging Supplies LLC | Target ICP W&D | N/A | 1 |
| 7 | hendersonenterprises | Henderson Enterprises | Target ICP W&D | N/A | 1 |
| 8 | aosolutions | Solutions Office Interiors, Inc. | Target ICP W&D | N/A | 0 |

#### From Wholesale & Distribution CSV - NEW Additions (16 accounts)

| # | Account Name | Company Name | Industry | Business Type | Warehouses | Screens |
|---|--------------|--------------|----------|---------------|------------|---------|
| 9 | acsdistributionllc | ACS Distribution LLC | Fiber Optic Materials Distribution | B2B | 1 | 0 |
| 10 | aedeschristiholdingsincdbadubalbros | Aedes Christi Holdings, Inc. | Wholesale Apparel (Men's Accessories) | B2B | 1 | 0 |
| 11 | bloomco3 | Bloomco | Automotive Detailing Products Manufacturing | Both | 1 | 0 |
| 12 | hps1source3 | Hps1source | Watch & Jewelry Repair Supplies | B2B | 1 | 0 |
| 13 | lightingxcorp | LightingX Corp. | Commercial LED Lighting | B2B | 1 | 0 |
| 14 | pikkl | PIKKL | Sporting Goods (Pickleball Equipment) | B2B | 1 | 0 |
| 15 | puzzlesthatrock | Puzzles That Rock, LLC. | Novelty Puzzles & Gifts | B2C | 1 | 0 |
| 16 | theatticdepot2 | The Attic Depot, LLC | Solar Attic Ventilation Systems | B2B | 1 | 0 |
| 17 | acocamtradinginc | Acocam Trading Inc | Logistics & Freight | B2B | 1 | 0 |
| 18 | cappadociarugsllc | Cappadocia Rugs LLC | Home Furnishings Retail | B2C | 1 | 0 |
| 19 | independenteyewearcollective | Independent Eyewear Collective LLC | Eyewear Distribution (Luxury) | B2B | 1 | 0 |
| 20 | londontec | LONDONTEC LLC | Electronics Distribution/Trading | B2B | 1 | 0 |
| 21 | proautodealersupplyinc | PRO-Auto Dealer Supply, Inc. | Automotive Dealer Supplies | B2B | 1 | 0 |
| 22 | rjdrews3 | R.J. Drews & Sons Inc | Industrial PVF Distribution | B2B | 1 | 0 |
| 23 | sensorytoys4uretailltd | Sensory Toys4U Retail Ltd | Specialty Toy Retail (E-commerce) | B2C | 1 | 0 |
| 24 | thermalbridgingsolutions | Thermal Bridging Solutions | Building Materials (Thermal Breaks) | B2B | 1 | 0 |

---

### Phase 2 - Tier 2: Generally Functional Accounts (10 accounts)

**Risk Level:** MEDIUM
**Rollout Week:** Week 3-4
**Characteristics:** Customizations require monitoring but expected to function with MLM

| # | Account Name | Company Name | Source | Feature Request | Screens | Key Concerns |
|---|--------------|--------------|--------|-----------------|---------|--------------|
| 1 | refexpertsandhvacllc | REF EXPERTS AND HVAC LLC | Requested Features | Warehouse | 3 | New Invoice customization requires additional work |
| 2 | cooksdoorsandmouldingsinc | Cooks Doors and Mouldings Inc | Requested Features | SOS | 4 | Dropdowns and datetime pickers |
| 3 | hydrospraywashsystemsinc ⭐ | HydroSpray Wash Systems Inc | Both Segments | SOS | 4 | Missing some flows from other teams |
| 4 | prosourcegroup ⭐ | Pro-Source Group | Both Segments | Warehouse | 4 | Ship method dropdowns, print packing slip |
| 5 | carolinalightinggroup ⭐ | Carolina Lighting Group LLC | Both Segments | SOS | 3 | Dated screens, missing sync widgets |
| 6 | sitepieces2 | Site Pieces | Target ICP W&D | N/A | 1 | API test flow in invoices |
| 7 | fullcirclesolutionsllc | Full Circle Solutions LLC | Target ICP W&D | N/A | 2 | SO customizations |
| 8 | area51sportsltd | Area 51 Sports | Target ICP W&D | N/A | 3 | SO and Invoice customized |
| 9 | dolphinheatexchangerusa | DOLPHIN HEAT EXCHANGER USA Inc | Target ICP W&D | N/A | 4 | Heavy SO customizations |
| 10 | metkonusainc | Metkon USA, Inc. | Target ICP W&D | N/A | 5 | Dated screens may conflict |

⭐ = Appears in both "Requested Features" and "Target ICP" segments (extra attention required)

---

## Beta Rollout Strategy

### Overview

**Total Beta Accounts:** 27 accounts
**Risk Level:** HIGH (product-market fit risk, not technical risk)
**Timeline:** Post-Alpha (Week 5+)
**Rollout Approach:** Opt-in with explicit consent

Beta accounts are:
- ✅ **Eligible = Yes**: No blocking customizations (technically safe to roll out)
- ❌ **ICP Fit Verified = No**: Don't match ideal customer profile

### Why These Accounts Don't Fit ICP

Common reasons for ICP exclusion:
1. **Regulated industries**: Food/beverage, alcohol, tobacco, cannabis products
2. **Perishable goods**: Plants, live products, fresh food
3. **Edge cases**: Very narrow product lines, non-distributor business models
4. **Service businesses**: Logistics companies without product inventory

### Beta Rollout Rationale

While these accounts don't fit the primary ICP, they may still benefit from MLM if:
- They have secondary product lines that are non-perishable/non-regulated
- They want to track inventory for internal operational reasons
- They explicitly request the feature despite non-ideal fit

---

### Beta Account List (27 accounts)

| # | Account Name | Company Name | Industry | Why Not ICP Fit | Warehouses |
|---|--------------|--------------|----------|-----------------|------------|
| 1 | banksdistro | Banks Distro LLC | Hemp/Cannabis Product Distribution | Regulated products (CBD/hemp) | 1 |
| 2 | thecelticgroup | Celtic Group Limited | Consumer Goods Distribution (Jamaica) | Regulated products (vaping) | 1 |
| 3 | grazianobrothers | Graziano Brothers Inc. | Specialty Grocery (Italian Foods) | Perishable/regulated food | 1 |
| 4 | gsova | Growth Services of Virginia LLC | Hydroponics Supply Retail | Agriculture/cultivation supplies | 1 |
| 5 | hattrickdistributioninc | HETTA GLOGG, LLC | Alcoholic Beverages (Mulled Wine) | Regulated alcohol products | 1 |
| 6 | hucksterinc | Huckster, Inc. | Convenience & Tobacco Product Distribution | Regulated tobacco products | 1 |
| 7 | lesgerstionsdmanagementlin | Les gestions D management Inc. | Business Management Services | Not a product distributor | 1 |
| 8 | lot49llcdbabox7imports | Lot 49 LLC | Importer of Organic Goods | Organic import services | 1 |
| 9 | magicgreensinc | Magic Greens, Inc. | Wholesale Plant Nursery (Florida) | Perishable plants | 1 |
| 10 | perlite | Perlite.com | Perlite Mining & Supply | Mining/raw materials | 1 |
| 11 | rojascigarsllc | Rojas Cigars LLC | Cigar Manufacturing & Distribution | Regulated tobacco products | 1 |
| 12 | santafetreeco2restore20250205 | Santa Fe Tree Company | Tree Services & Nursery | Perishable plants/services | 1 |
| 13 | strongwellness | StrongWellness, LLC | Health & Wellness Products | Consumable supplements | 1 |
| 14 | trifunoretailsolutionsinc | Trifuno Retail Solutions Inc. | Retail Technology & Fixtures | Service/technology focus | 1 |
| 15 | twobirds | Two Birds Coffee | Coffee Roasting & Cafés | Perishable food/beverage | 1 |
| 16 | appenninofoodusa | Appennino USA Corp. | Food & Beverage (Gourmet Foods) | Perishable/regulated food | 1 |
| 17 | dbuoy | Databuoy | Security Technology (Surveillance) | Technology services | 0 |
| 18 | fireprosupply3 | Fire Pro Supply Ltd. | Firefighting Equipment Supply | Specialized equipment | 1 |
| 19 | geomarinetrade | GEO MARINE TRADE LTD | Marine Fuel & Lubricants Trading | Hazardous materials | 0 |
| 20 | jonescoffeeroasters2 | Jones Coffee Roasters | Coffee Roasting & Retail | Perishable food/beverage | 1 |
| 21 | lightforgedlogistics | Lightforged Logistics | Logistics (Freight/Trucking) | Service business (non-inventory) | 0 |
| 22 | mogselections3 | MOG SELECTIONS | Wine Production & Distribution | Regulated alcohol products | 1 |
| 23 | op76cattle | Outpost 76 Operations Co., Inc | Ranching & Premium Meats | Perishable food/livestock | 1 |
| 24 | pagonislivebait | Pagonis Live Bait | Fishing Bait Supply | Perishable live products | 1 |
| 25 | empirecoatingsolutions | SOCAL ECS (Empire Coating Solutions) | Construction Materials (Coatings) | Specialized materials | 1 |
| 26 | villasurgicalandequipments | VILLA SURGICAL AND EQUIPMENTS LTD | Medical Equipment Supply | Medical/regulated equipment | 1 |
| 27 | wellcraftedacuratedliquoragency | Well Crafted – A Curated Liquor Agency | Alcohol Beverage Agency | Regulated alcohol products | 0 |


---

## Communication Plan


---

## Appendix: Account Selection Methodology

### Alpha Selection Criteria

Accounts must meet BOTH requirements:

1. **ICP Fit Verified = Yes**
   - Distribute non-regulated, non-perishable finished goods
   - B2B or B2C business model
   - 1-3 warehouse locations
   - Moderate SKU complexity (100-5,000 SKUs)
   - Non-serialized inventory

2. **Eligible = Yes**
   - Zero customizations on inventory-related screens, OR
   - Only non-breaking customizations (grid columns, minor layout changes)
   - No heavy API integrations in transaction screens
   - No custom quantity/location calculation flows

### Beta Selection Criteria

Accounts meet ONE requirement only:

1. **Eligible = Yes** (no blocking customizations)
2. **ICP Fit Verified = No** for reasons such as:
   - Regulated industries (food, beverage, alcohol, tobacco, cannabis)
   - Perishable goods (plants, fresh food, live products)
   - Service businesses without significant product inventory
   - Edge cases (very narrow product lines, non-distributor models)

---

**Document Owner:** Product Management
**Last Updated:** December 2, 2025
**Next Review:** Post-Alpha Tier 1 completion (Week 3)
