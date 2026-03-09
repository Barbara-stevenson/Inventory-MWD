# Top 200 MWD Accounts: Supply Chain Position Analysis

## Executive Summary

Analysis of Method CRM's top 200 MWD enriched accounts reveals the supply chain positioning of each business. This categorization helps identify specific inventory management needs based on whether they operate as manufacturers, wholesalers, distributors, or hybrid models.

**Key Finding:** 55.5% are primarily manufacturers, but 16.5% operate hybrid models spanning multiple verticals, requiring more sophisticated inventory management capabilities.

---

## Overall Breakdown

**Total Accounts Analyzed:** 200

| Supply Chain Position | Count | Percentage | Inventory Complexity |
|----------------------|-------|------------|---------------------|
| **Manufacturing Only** | 111 | 55.5% | High (BOM, WIP, multi-stage) |
| **Distribution Only** | 32 | 16.0% | Medium-High (multi-location) |
| **Manufacturing + Distribution** | 14 | 7.0% | Very High (full supply chain) |
| **Wholesale + Distribution** | 11 | 5.5% | High (breaking bulk + fulfillment) |
| **Manufacturing + Wholesale** | 10 | 5.0% | Very High (production + bulk sales) |
| **Manufacturing + Wholesale + Distribution** | 8 | 4.0% | Extreme (entire supply chain) |
| **Wholesale Only** | 6 | 3.0% | Medium (bulk inventory turnover) |
| **Unclear** | 8 | 4.0% | Unknown |

---

## Strategic Insights

### 1. Manufacturing Dominance (55.5%)

**111 accounts are primarily manufacturers**, indicating:
- Heavy need for BOM management
- Work-in-Process (WIP) tracking critical
- Multi-stage production workflows
- Component-level inventory visibility

**Example Manufacturers:**
- **DEWESoft LLC** - Data acquisition systems manufacturing with in-house European production
- **Architectural Glass and Metal Co.** - Custom architectural glass fabrication
- **AAA Fire Protection Resources** - Fire protection equipment manufacturing

**Inventory Management Needs:**
- Multi-level BOMs
- Raw materials tracking with lot/batch numbers
- WIP tracking by production stage
- Component substitution management
- Production yield tracking

---

### 2. Hybrid Operations Are Common (16.5%)

**33 accounts operate across multiple verticals**, requiring:
- Unified inventory view across production, warehousing, and fulfillment
- Different inventory types in one system (raw materials, WIP, finished goods)
- Complex location tracking (factory floor, warehouses, distribution centers)

#### Manufacturing + Distribution (14 accounts, 7.0%)
These companies make products AND ship directly to customers.

**Examples:**
- **FUJI Mats, LLC** - Manufactures martial arts mats in USA, ships worldwide through dealer network
- **PowerHandling, Inc** - Manufactures air-powered roll movers, ships from Spokane HQ worldwide
- **San Jamar** - Food service products manufactured and distributed globally

**Unique Challenge:** Must track inventory from raw materials through production to multi-location distribution centers, then to end customers.

#### Wholesale + Distribution (11 accounts, 5.5%)
These companies buy in bulk and handle fulfillment logistics.

**Examples:**
- **Central Infusion Alliance** - Wholesale medical supplies with nationwide distribution to 25,000+ customers
- **Chadwell Supply** - Wholesale material handling equipment with regional distribution
- **Amerinac Packaging Supply** - Packaging materials wholesale with multi-location fulfillment

**Unique Challenge:** Breaking bulk orders into smaller shipments while maintaining inventory accuracy across multiple warehouses.

#### Manufacturing + Wholesale (10 accounts, 5.0%)
These companies produce goods and sell in bulk to other businesses.

**Examples:**
- **J2 Medical Supply Inc** - Manufacturer of medical products + wholesale distribution with 300,000+ SKUs
- **Leef Brands** - CBD product manufacturing with wholesale distribution channel
- **Zogics** - Manufactures cleaning/facility supplies, sells wholesale to businesses

**Unique Challenge:** Managing production inventory alongside finished goods for bulk sale, with different pricing tiers and customer types.

#### Manufacturing + Wholesale + Distribution (8 accounts, 4.0%)
These companies handle the ENTIRE supply chain from raw materials to end customer delivery.

**Examples:**
- **FUJI Mats, LLC** - Makes mats, sells wholesale to dealers, ships direct to end users
- **American Orthodontics** - Manufactures orthodontic products, wholesale to practitioners, ships globally
- **Acorn Engineering Company** - Manufactures plumbing fixtures, wholesale channel, multi-location distribution

**Unique Challenge:** Most complex inventory needs. Must manage:
- Raw materials and WIP (Manufacturing)
- Bulk inventory and breaking bulk (Wholesale)
- Multi-location fulfillment and shipping (Distribution)

---

### 3. Distribution-Focused Accounts (16.0%)

**32 accounts are primarily distributors**, focusing on:
- Multi-warehouse management
- Location-level precision (aisle, shelf, bin)
- Fast order fulfillment
- Available-to-promise calculations

**Examples:**
- **Conequip Parts & Equipment LLC** - Construction equipment parts distribution across USA, Canada, UK
- **Rhoback** - Apparel distribution with multi-location warehousing
- **Taylor-Ramsey Corp** - Industrial MRO products distribution

**Inventory Management Needs:**
- Real-time available inventory by location
- Transfer management between warehouses
- Shipping/receiving workflows
- Order fulfillment optimization

---

### 4. Wholesale-Focused Accounts (3.0%)

**6 accounts are primarily wholesalers**, prioritizing:
- Inventory turnover optimization
- Bulk purchasing and breaking bulk
- B2B customer pricing tiers
- Supplier management

**Examples:**
- **BioAg Energy Services** - Bulk petroleum and fuel wholesale to agricultural customers
- **Elotec, Inc** - Electronics wholesale distribution
- **Wholesale Bridal** - Bridal gown wholesale to retailers

**Inventory Management Needs:**
- Bulk inventory tracking
- Customer-specific pricing and allocations
- Reorder point optimization for cash flow
- Supplier lead time management

---

## Implications for Method CRM Inventory MLP

### Priority 1 Features (Must-Have)

Based on the account distribution:

1. **Multi-Warehouse Management** (Critical for 73% of accounts)
   - 111 manufacturers likely have raw material storage + finished goods warehouses
   - 32 distributors operate multiple fulfillment centers
   - 33 hybrid operators manage production facilities + warehouses

2. **Available Inventory Visibility** (Critical for 100% of accounts)
   - All verticals need real-time stock levels
   - Manufacturing needs available raw materials to prevent line stoppages
   - Distribution needs accurate ATP for order fulfillment
   - Wholesale needs turnover metrics

3. **Third-Party Integration** (Critical for complex operations)
   - 22 accounts with "Very High" or "Extreme" complexity likely use specialized systems
   - Manufacturing accounts may use MRP systems (Katana, Fishbowl)
   - Distribution accounts may use WMS systems (SOS Inventory, Ordoro)

### Priority 2 Features (High Value)

4. **Reorder Points & Low Stock Alerts**
   - Manufacturing: Prevent production line stoppages
   - Wholesale: Maintain inventory turnover targets
   - Distribution: Avoid stockouts on fast-movers

5. **Dynamic Item Management in Transactions**
   - 55.5% manufacturers need to handle BOM components
   - 16.5% hybrid accounts manage SKU proliferation
   - All accounts need multi-variant product support

6. **Backorder Awareness**
   - Manufacturing: Communicate lead times to sales
   - Wholesale: Allocate limited stock fairly across customers
   - Distribution: Prioritize fulfillment based on customer tier

### Feature Prioritization by Account Segment

| Feature | Manufacturing (111) | Distribution (32) | Wholesale (6) | Hybrid (43) |
|---------|---------------------|-------------------|---------------|-------------|
| Multi-Warehouse | High | Critical | Medium | Critical |
| Available Inventory | Critical | Critical | Critical | Critical |
| BOM Management | Critical | Low | Low | High |
| WIP Tracking | Critical | None | None | Medium |
| Location Tracking | Medium | Critical | Low | High |
| Transfer Management | Medium | Critical | Medium | Critical |
| Reorder Points | High | Critical | Critical | High |
| Third-Party Integration | High | High | Medium | Critical |

---

## Account Examples by Category

### Manufacturing Only (111 accounts)

**High Complexity Manufacturing:**

1. **DEWESoft LLC** (Data Acquisition Systems)
   - In-house European design/development/manufacturing/calibration
   - Complex product: SIRIUS, IOLITE, KRYPTON systems
   - 7-year warranty indicates robust quality tracking
   - **Needs:** BOM management, WIP tracking, quality assurance integration

2. **Architectural Glass and Metal Co.** (Custom Architectural Glass)
   - Project-based manufacturing (Engineer-to-Order)
   - Custom specifications for each project
   - **Needs:** Project-based inventory, custom BOMs per job, material allocation

3. **AAA Fire Protection Resources** (Fire Protection Equipment)
   - Manufacturers fire extinguishers, suppression systems
   - Regulatory compliance requirements (UL, NFPA)
   - **Needs:** Lot tracking for compliance, expiration date management

**Medium Complexity Manufacturing:**

4. **San Jamar** (Food Service Products)
   - Standardized product lines
   - High volume production
   - **Needs:** Standard BOMs, batch tracking, quality control

5. **Acorn Engineering Company** (Plumbing Fixtures)
   - Make-to-stock manufacturing
   - Multiple product lines
   - **Needs:** Finished goods inventory management, multi-location production

---

### Distribution Only (32 accounts)

1. **Conequip Parts & Equipment LLC** (Construction Equipment Parts)
   - Multi-brand parts catalog (CAT, Komatsu, Case, Deere, Kobelco)
   - Warehouse network in USA, Canada, UK
   - New, aftermarket, used, and rebuilt parts
   - **Needs:** Multi-location inventory, cross-reference catalog, condition tracking

2. **Rhoback** (Apparel Distribution)
   - Multi-location warehousing
   - Size/color variants
   - **Needs:** Variant tracking, location-based fulfillment, seasonal inventory management

3. **Taylor-Ramsey Corp** (Industrial MRO Distribution)
   - 20,000+ SKUs
   - Fast-moving consumables
   - **Needs:** High inventory turnover tracking, reorder automation, bulk order breaking

---

### Wholesale Only (6 accounts)

1. **BioAg Energy Services** (Bulk Petroleum Wholesale)
   - Bulk fuel facilities in multiple locations
   - Agricultural customer focus
   - **Needs:** Commodity pricing fluctuation management, delivery scheduling, tank level monitoring

2. **Elotec, Inc** (Electronics Wholesale)
   - Purchasing from manufacturers, selling to retailers
   - **Needs:** Bulk inventory tracking, customer pricing tiers, supplier lead times

3. **Wholesale Bridal** (Bridal Gown Wholesale)
   - Seasonal inventory
   - Size/style variants
   - **Needs:** Style/size matrix tracking, seasonal demand forecasting

---

### Manufacturing + Distribution (14 accounts)

1. **FUJI Mats, LLC** (Martial Arts Equipment)
   - Manufactures in USA
   - Worldwide distribution through resellers and international distributors
   - Official IJF supplier (quality standards)
   - **Needs:** Production + finished goods tracking, dealer inventory visibility, international shipping

2. **PowerHandling, Inc** (Material Handling Equipment)
   - Manufactures in Spokane, WA
   - Ships worldwide
   - Custom configurations available
   - **Needs:** Build-to-order tracking, component inventory, finished goods by location

3. **San Jamar** (Food Service Products)
   - Global manufacturing facilities
   - International distribution network
   - **Needs:** Multi-facility production tracking, regional distribution centers, transfer management

---

### Wholesale + Distribution (11 accounts)

1. **Central Infusion Alliance, Inc.** (Medical Supplies)
   - 25,000+ customers nationwide
   - Multi-facility distribution
   - Physicians, dentists, hospitals as customers
   - **Needs:** Breaking bulk orders, customer-specific pricing, multi-location fulfillment, compliance tracking

2. **Chadwell Supply** (Material Handling Equipment)
   - Regional distribution centers
   - Wholesale pricing to businesses
   - **Needs:** Bulk purchasing tracking, regional inventory allocation, freight optimization

3. **Amerinac Packaging Supply** (Packaging Materials)
   - Bulk purchasing from manufacturers
   - Breaking bulk for small business customers
   - **Needs:** Supplier lead time management, bulk inventory tracking, customer allocation

---

### Manufacturing + Wholesale (10 accounts)

1. **J2 Medical Supply, Inc.** (Medical Equipment & Supplies)
   - FDA-approved manufacturer AND distributor
   - 300,000+ products including national brands + private label
   - 5,000+ manufacturers represented
   - **Needs:** Private label manufacturing tracking + reseller inventory, FDA compliance, massive SKU management

2. **Leef Brands** (CBD Products)
   - Manufactures CBD products in-house
   - Wholesale distribution to retailers
   - **Needs:** Batch tracking for compliance, wholesale pricing tiers, production + finished goods inventory

3. **Zogics** (Cleaning & Facility Supplies)
   - Manufactures proprietary products
   - Sells wholesale to gyms, spas, hotels
   - **Needs:** Production tracking + bulk wholesale inventory, customer-specific kitting

---

### Manufacturing + Wholesale + Distribution (8 accounts)

1. **FUJI Mats, LLC** (Martial Arts Equipment)
   - Manufactures mats in USA
   - Sells wholesale to martial arts dealers
   - Ships direct to end users internationally
   - **Needs:** Full supply chain visibility from raw materials to end customer delivery

2. **American Orthodontics** (Orthodontic Products)
   - Manufactures orthodontic appliances
   - Wholesale to dental practitioners
   - Global distribution network
   - **Needs:** Medical device compliance tracking, practitioner-specific pricing, international fulfillment

3. **Acorn Engineering Company** (Plumbing Fixtures)
   - Manufactures commercial plumbing products
   - Wholesale channel to distributors
   - Multi-location distribution to end customers
   - **Needs:** Production + channel inventory visibility, transfer management, wholesale vs. direct pricing

---

## Unclear Categorization (8 accounts)

These accounts require further research to determine their supply chain position:

1. **Lenworth Building Services Limited** - Sells/installs/services overhead doors (service business, minimal inventory?)
2. **Shropshire Audiology LTD** - Hearing healthcare services (service-based?)
3. **Clarity Hearing AID Centers** - Hearing aid services (medical devices, unclear if resale or dispensing)

These may be primarily service businesses rather than product-based MWD operations.

---

## Recommended Next Steps

### 1. Account Segmentation Strategy

Create targeted messaging for each segment:

**For Pure Manufacturers (111 accounts):**
- Lead with BOM management capabilities
- Emphasize WIP tracking and production integration
- Highlight raw materials reorder automation

**For Pure Distributors (32 accounts):**
- Lead with multi-warehouse visibility
- Emphasize location-level tracking and fulfillment
- Highlight transfer management and order routing

**For Hybrid Operators (43 accounts):**
- Lead with "unified inventory view across entire supply chain"
- Emphasize third-party integration capabilities
- Highlight scalability from simple to complex needs

### 2. Customer Interview Prioritization

Interview representatives from each segment to validate inventory needs:

**Hybrid Accounts (Highest Priority):**
- Most complex needs = most likely to churn without solution
- Can provide insights into multiple vertical requirements
- Likely already using workarounds or third-party systems

**Large Manufacturers (High Priority):**
- Largest segment = biggest impact on churn reduction
- Many likely experiencing BOM/WIP tracking pain
- May have insights into desired MRP integration

**Distributors (Medium Priority):**
- Already have some QuickBooks location support
- May need Method to expose QBO location data better
- Can validate multi-warehouse feature requirements

### 3. Feature Development Sequencing

Based on account distribution:

**Phase 1 (Addresses 100% of accounts):**
- Multi-warehouse management (basic location tracking)
- Available inventory visibility in Method UI
- Real-time sync with QuickBooks Online inventory

**Phase 2 (Addresses 55.5% manufacturers + 16.5% hybrid = 72%):**
- BOM support (simple, single-level initially)
- WIP tracking basics
- Component-level inventory visibility

**Phase 3 (Addresses 16.5% hybrid + 7.5% wholesale/dist = 24%):**
- Advanced multi-location (bin/aisle tracking)
- Transfer management between locations
- Shipping/receiving workflows

**Phase 4 (Addresses 22% most complex accounts):**
- Third-party integration (Katana, SOS Inventory)
- Advanced BOM (multi-level, nested)
- Full supply chain visibility

---

## Appendix: Full Account Categorization

The complete categorization of all 200 accounts is available in CSV format:
`/tmp/claude/.../scratchpad/mwd_categorized.csv`

This file includes:
- Account Name
- Company Name in QuickBooks
- Vertical (as tagged in Method)
- Industry (Research classification)
- Workflow Type
- Company Description
- **Supply Chain Position** (our analysis)

---

**Analysis Date:** January 13, 2026
**Methodology:** Keyword analysis of company descriptions, workflow types, and industry classifications to categorize supply chain positioning
**Data Source:** MWD_Top_200_Enriched.csv (200 accounts)
**Related Documents:** MWD_Verticals_Deep_Dive.md, CLAUDE.md
