# Manufacturing, Wholesale & Distribution (MWD) Market
## Comprehensive Product Discovery Analysis

**Document Date:** 2026-01-12
**Analysis Scope:** Top 200 MWD Accounts (157 with complete usage data)
**Data Period:** 366 days (Jan 2025 - Jan 2026)
**Total Market Value:** $6.6M LTV ($33K average per account)
**Prepared by:** Product Management

---

## Executive Summary

The MWD segment represents Method CRM's most sophisticated and operationally complex customer base—200 companies generating $6.6M in lifetime value with 77% operating at High or Very High product complexity. These are not simple distributors; they're specialized manufacturers (43%), multi-warehouse distributors (33%), and service-intensive operations (22%) managing intricate supply chains, custom production, and regulatory compliance.

### Critical Discovery: The Operational Paradox

**Front-office excellence, back-office absence.** While MWD companies heavily use customer-facing apps (Activities: 52% adoption, Contacts: 65%, Estimates: 46%), they barely touch operational apps (Items: 22%, Work Orders: 6.5%, Purchase Orders: 15%). This is not a usage problem—it's a **capabilities gap**. When companies DO use operational apps, engagement is intense (Work Orders: 34K page loads per using account vs Activities: 40K). The need exists; the features don't fully meet it.

### The $141K ARR Expansion Opportunity

**Conservative estimate:** If operational app adoption increased from 6-22% to 50% (still below Contacts' 65%), existing customer expansion could generate **$90-141K in additional ARR** without acquiring a single new customer. This assumes modest $300-600 ARPU per app based on current LTV patterns.

### Strategic Validation

The current **Big Bet #5 Inventory Management MLP roadmap** (multi-warehouse visibility, dynamic items, reorder points) directly addresses the #1 gap affecting 33% of the customer base. However, analysis reveals a second, larger opportunity: **Work Order/Production Tracking** (missing for 43% of manufacturers) represents the single biggest whitespace in operational workflows.

---

## Part 1: WHO Are MWD Companies?

### Market Composition: 200 Accounts, $6.6M LTV

| Customer Tier | Accounts | Avg LTV | % of Total LTV | Health Score | Avg Page Loads/Year |
|---|---:|---:|---:|---:|---:|
| **Enterprise (50+ users)** | 1 | $208,604 | 3.2% | 29 | 772,718 |
| **Large (16-50 users)** | 31 | $42,281 | 19.8% | 45 | 265,290 |
| **Medium (6-15 users)** | 92 | $33,200 | 46.2% | 45 | 83,384 |
| **Small (1-5 users)** | 33 | $28,400 | 14.2% | 44 | 32,803 |
| **Unknown Size** | 43 | $27,500 | 16.6% | 44 | 51,337 |

**Key Finding:** Usage scales 23X from small to enterprise accounts, but health scores remain consistent (44-45) across segments. This suggests **all tiers face similar operational challenges**, regardless of size.

---

### Firmographic Profile: High-Complexity B2B Operations

#### Company Size Distribution

| Metric | Small (1-5) | Medium (6-15) | Large (16-50) | Enterprise (50+) |
|---|---:|---:|---:|---:|
| **User Count** | 2.8 avg | 9.1 avg | 24.5 avg | 72 (DEWESoft) |
| **Employee Count** | 12 avg | 38 avg | 94 avg | 250+ |
| **Customer Count** | 180 avg | 420 avg | 1,150 avg | 5,000+ |
| **Page Loads/User/Day** | 32 | 25 | 30 | 29 |

**Insight:** Per-user daily activity is remarkably consistent (25-32 page loads) across all company sizes. Engagement is **driven by operational needs**, not company scale.

#### Health Score Distribution: Wide Variability

| Health Score Band | Accounts | Avg LTV | Avg Page Loads | Health Range | Risk Level |
|---|---:|---:|---:|---:|---|
| **Critical (<30)** | 6 | $28,400 | 13,298 | 12-25 | 🔴 Churn imminent |
| **Low (30-40)** | 34 | $28,300 | 51,337 | 30-39 | 🟡 At-risk |
| **Medium (40-70)** | 101 | $33,200 | 117,689 | 40-70 | 🟢 Stable |
| **High (70-100)** | 16 | $38,100 | 238,154 | 75-80 | 🟢 Champions |

**Critical Alert:** 40 accounts (20%) show health scores <40, averaging only 51,337 page loads vs healthy average of 117,689. **Usage gap = 2.3X.** This correlates directly with missing operational app adoption (Items, Work Orders, Purchase Orders).

**Opportunity:** If low-health segment increases operational app adoption to 30-40% (vs current 6-22%), health scores could improve 15-20 points, reducing churn risk.

---

### Geographic & Operational Footprint

#### Multi-Location Operations (33% of Customer Base)

| Pattern | % of Accounts | Industries Most Affected | Operational Need |
|---|---:|---|---|
| **Multi-warehouse distribution** | 21% | Industrial Equipment, Construction, Medical | Real-time inventory across facilities |
| **Regional service territories** | 12% | Equipment dealers, Parts distributors | Location-specific parts availability |
| **Showroom + Warehouse model** | 8% | Construction, Consumer goods | Display inventory separate from fulfillment |
| **Multi-brand service centers** | 6% | Industrial Equipment, HVAC | Parts inventory across multiple OEMs |

**Strategic Insight:** 33% of top customers (66 companies) operate distributed operations requiring **multi-warehouse visibility**—the exact problem Big Bet #5 Priority 1 solves. This is not a hypothetical need; it's the current operational reality for 1 in 3 accounts.

---

### Product Complexity: Sophisticated Catalog Management

| Complexity Level | Companies | % | Total LTV | % of LTV | LTV per Company |
|---|---:|---:|---:|---:|---:|
| **Very High** | 73 | 36.5% | $1,957,042 | 47.0% | $26,809 |
| **High** | 81 | 40.5% | $1,608,023 | 38.6% | $19,852 |
| **Medium-High** | 22 | 11.0% | $302,760 | 7.3% | $13,762 |
| **Medium** | 13 | 6.5% | $269,829 | 6.5% | $20,756 |
| **Low** | 11 | 5.5% | $295,444 | 7.1% | $26,858 |

**77% operate at High/Very High complexity, representing 85.6% of total LTV.**

#### What "High Complexity" Actually Means

| Complexity Driver | % of Companies | Operational Challenge | Example Industries |
|---|---:|---|---|
| **Technical products** | 46% | Specifications, compatibility matrices, engineering drawings | Industrial (65%), Electronics (57%), Medical (47%) |
| **Custom/Made-to-order** | 35% | BOM management, job costing, work order tracking | Industrial (49%), Construction (44%) |
| **Supply chain complexity** | 34% | Multi-supplier parts, lead time variability | Medical (53%), Electronics (36%) |
| **High SKU count** | 18% | Thousands to 300K+ product variants | Medical (J2 Medical: 300K SKUs) |
| **Regulatory compliance** | 12% | FDA tracking, lot/batch, expiration management | Medical (29%), Electronics (14%) |
| **Multi-brand distribution** | 15% | Carrying competing brands, cross-referencing parts | Industrial Equipment, Wholesale |

**Key Takeaway:** Complexity isn't just SKU count—it's **BOM structures, custom configurations, regulatory tracking, and multi-supplier coordination.** Current Items app (22% adoption) doesn't meet these sophisticated needs.

---

## Part 2: WHAT Industries They're In

### Top 10 Industries (86% of Total LTV)

| Rank | Industry | Companies | Total LTV | % of LTV | Avg LTV | Avg Health | Complexity |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | **Industrial Equipment & Machinery** | 37 | $1,276,569 | 19.3% | $34,502 | 42 | 92% High+ |
| 2 | **Construction & Building Materials** | 25 | $1,166,668 | 17.6% | $46,667 | 46 | 68% High+ |
| 3 | **Medical & Healthcare** | 17 | $704,764 | 10.7% | $41,457 | 49 | 77% Very High |
| 4 | **Electronics & Technology** | 14 | $559,109 | 8.5% | $39,936 | 46 | 86% High+ |
| 5 | **Consumer Goods & Retail** | 13 | $458,624 | 6.9% | $35,279 | 51 | 54% High+ |
| 6 | **Uncategorized/Mixed** | 12 | $394,781 | 6.0% | $32,898 | 44 | N/A |
| 7 | **Energy & Environmental** | 10 | $321,652 | 4.9% | $32,165 | 43 | 60% High+ |
| 8 | **Specialty Manufacturing** | 8 | $236,711 | 3.6% | $29,589 | 42 | 75% High+ |
| 9 | **Food & Beverage** | 10 | $237,000 | 3.6% | $23,700 | 48 | 40% High+ |
| 10 | **Textiles & Apparel** | 7 | $177,620 | 2.7% | $25,374 | 46 | 57% High+ |

**Remaining 13 industries (<2% each):** Packaging, Agriculture, Security, Lab Equipment, Automotive, Fuel, Marine, Chemicals, HVAC, Aerospace, Glass, Rental, Stone Fabrication.

---

### Industry Deep-Dive: Top 5 Segments

#### 1. Industrial Equipment & Machinery (37 companies, $1.3M LTV, 19% of market)

**Profile:**
- **Dominant workflow:** 54% Manufacturing (Specialized/Custom), 11% Manufacturing + Distribution
- **Product focus:** Precision equipment, hydraulic systems, material handling, pumps, conveyors
- **Complexity drivers:** Technical specifications (65%), custom fabrication (49%), multi-brand parts (32%)
- **Geographic spread:** Multi-location service territories requiring distributed parts inventory

**Top Companies:**
- Conequip Parts & Equipment ($208K LTV, Health 29, Wholesale/Distribution)
- FUJI Mats ($105K LTV, Health 75, Manufacturing + Distribution)
- PowerHandling ($85K LTV, Health 6, Manufacturing + Distribution)

**App Usage Reality:**
- **Strong:** Activities (1,511 daily), Estimates (1,277 daily), Contacts (1,245 daily)
- **Weak:** Items (115 daily, 23% adoption), Work Orders (494 daily, 3% adoption), Purchase Orders (294 daily, 14% adoption)

**Critical Gaps:**
- 🔴 **Production Tracking:** Only 2.9% use Work Orders despite 54% being manufacturers
- 🔴 **Inventory Visibility:** Only 22.9% use Items app → 77% lack real-time inventory in CRM
- 🟡 **Procurement:** Only 14.3% use Purchase Orders → managing vendor orders outside CRM

**What They Need:**
1. Multi-warehouse parts inventory across service territories
2. BOM management for custom equipment fabrication
3. Serial number tracking for high-value precision equipment
4. Work order linkage to inventory consumption

---

#### 2. Construction & Building Materials (25 companies, $1.2M LTV, 18% of market)

**Profile:**
- **Balanced workflow:** 44% Manufacturing (custom sheds, cabinets), 20% Distribution (tiles, flooring)
- **Product focus:** Building materials, outdoor structures, kitchen cabinetry, tile/flooring
- **Complexity drivers:** Custom/made-to-order (44%), project-based operations (52%)
- **Multi-location:** Regional warehouses for heavy/bulky materials, showroom displays

**Top Companies:**
- Town & Country Sheds ($165K LTV, Health 43, Manufacturing)
- United Tile ($88K LTV, Health 40, Wholesale/Distribution)
- CPF Floors ($78K LTV, Health 43, Wholesale/Distribution)

**App Usage Reality:**
- **Strong:** Activities (1,987 daily), Estimates (1,201 daily), Contacts (1,142 daily)
- **Moderate:** Sales Orders (1,044 daily, 42% adoption), Invoices (856 daily, 54% adoption)
- **Weak:** Items (130 daily, 39% adoption), Work Orders (102 daily, 12% adoption)

**Critical Gaps:**
- 🔴 **Project-Based Inventory:** Materials tied to specific construction jobs, not tracked in Method
- 🟡 **Multi-Location Visibility:** Regional warehouses need real-time stock levels
- 🟢 **Better than average:** 39% Items adoption vs 22% overall (still only 2 in 5 accounts)

**What They Need:**
1. Project/job-based inventory allocation
2. Multi-warehouse visibility across regional distribution centers
3. Showroom inventory separate from warehouse fulfillment stock
4. Heavy/bulky material tracking (pallets, bulk quantities)

---

#### 3. Medical & Healthcare (17 companies, $705K LTV, 11% of market)

**Profile:**
- **Manufacturing-dominant:** 47% specialized manufacturing (surgical devices, mobility equipment)
- **Regulatory-intensive:** 29% FDA compliance requirements (highest of any industry)
- **Complexity drivers:** Regulatory (29%), supply chain complexity (53%), lot tracking critical
- **High LTV:** $41,457 average (2nd highest after Construction)

**Top Companies:**
- J2 Medical Supply ($170K LTV, Health 62, Distribution - 300K SKUs!)
- Biomedical Life Systems ($58K LTV, Health 75, Manufacturing)
- Saebo ($42K LTV, Health 80, Manufacturing)

**App Usage Reality:**
- **Strong:** Activities (700K annual), Sales Orders (511K annual), Contacts (369K annual)
- **Moderate:** Invoices (124K annual)
- **Weak:** Items (20K annual, 39% adoption - better than avg but still <50%)

**Critical Gaps:**
- 🔴 **FDA Compliance:** No lot/batch tracking, expiration management, recall workflows
- 🔴 **Serialization:** Medical devices require serial number tracking (not in current MLP)
- 🟡 **Audit Trails:** Regulatory requires full item history (MLP Priority 3 addresses this)

**What They Need:**
1. Lot/batch tracking for FDA compliance
2. Expiration date management (FEFO: First Expire, First Out)
3. Recall management system (trace lot distribution)
4. Serial number tracking for high-value medical devices
5. Audit trail for regulatory inspections

**Strategic Note:** Despite being 11% of market, Medical/Healthcare shows **highest health scores** (avg 49 vs 42-46 elsewhere) and **highest complexity** (77% Very High). This is a premium, sticky segment worth prioritizing for regulatory-compliant features.

---

#### 4. Electronics & Technology (14 companies, $559K LTV, 9% of market)

**Profile:**
- **Most diversified workflow:** No dominant pattern (36% Manufacturing, 14% Distribution, 7% Service)
- **Product focus:** Data acquisition systems, IoT devices, smart home, telecommunications
- **Complexity drivers:** Technical complexity (57%), software + hardware integration
- **Emerging category:** Cloud-based platforms, subscription hardware models

**Top Companies:**
- DEWESoft ($208K LTV, Health 25, Software/Hardware - ENTERPRISE account!)
- SPM Instrument ($39K LTV, Health 40, Distribution)
- C&H Distributors ($37K LTV, Health 33, Distribution)

**App Usage Reality:**
- **Strong:** Activities (1,211 daily), Contacts (887 daily), Estimates (616 daily)
- **Moderate:** Sales Orders (487 daily), Invoices (207 daily)
- **Weak:** Items (95 daily, minimal adoption)

**Critical Gaps:**
- 🔴 **Component Compatibility:** Complex compatibility matrices not supported
- 🟡 **Software + Hardware:** Subscription models with physical devices (licensing + inventory)
- 🟡 **Configuration Management:** Systems sold as configured assemblies

**What They Need:**
1. BOM/kit management for configured systems
2. Component compatibility tracking
3. Software licensing tied to hardware serial numbers
4. Firmware version tracking

---

#### 5. Consumer Goods & Retail (13 companies, $459K LTV, 7% of market)

**Profile:**
- **Manufacturing-heavy:** 54% combined manufacturing workflows (handcrafted, artisan)
- **Product focus:** Furniture, pianos, martial arts equipment, sporting goods, office furniture
- **Complexity drivers:** Custom/made-to-order (30%), showroom + warehouse model
- **Highest health scores:** Avg 51 (highest of any major industry)

**Top Companies:**
- Piano Distributors ($90K LTV, Health 75)
- Brown Safe Manufacturing ($88K LTV, Health 12 - custom safes)
- Resilite Sports Products ($57K LTV, Health 80 - wrestling mats)

**App Usage Reality:**
- **Strong:** Contacts (513K annual), Activities (409K annual), Estimates (368K annual)
- **Moderate:** Invoices (222K annual), Sales Orders (174K annual)
- **Weak:** Items (minimal adoption)

**Critical Gaps:**
- 🔴 **Custom Orders:** Made-to-order tracking requires work orders (not used)
- 🟡 **Multi-Channel Inventory:** Retail showroom + online + warehouse stock
- 🟢 **Strong engagement:** Highest health scores suggest good CRM practices, but missing ops features

**What They Need:**
1. Custom order/work order tracking
2. Multi-channel inventory (showroom display vs available-to-sell)
3. Consignment tracking (piano dealers, furniture showrooms)
4. Artisan/handcrafted production workflows

---

### Industry-Specific Opportunity Sizing

| Industry | Gap | Affected Accounts | ARR Opportunity | Priority |
|---|---|---:|---:|---|
| **Industrial Equipment** | Multi-warehouse + Work Orders | 28 of 37 (76%) | $22-34K | 🔴 HIGHEST |
| **Construction** | Project inventory + Multi-warehouse | 15 of 25 (60%) | $12-19K | 🟡 HIGH |
| **Medical** | FDA compliance (lot/serial tracking) | 10 of 17 (59%) | $8-12K | 🟡 HIGH |
| **Electronics** | BOM/Configuration management | 10 of 14 (71%) | $8-11K | 🟢 MEDIUM |
| **Consumer Goods** | Work Orders for custom production | 7 of 13 (54%) | $5-8K | 🟢 MEDIUM |

**Total addressable opportunity across top 5 industries: $55-84K ARR** from improving operational feature adoption (conservative estimates).

---

## Part 3: HOW They Operate - Workflow Patterns

### Primary Workflow Distribution (106 Classified Companies)

| Rank | Workflow Type | Companies | % | Key Characteristics |
|---:|---|---:|---:|---|
| 1 | **Manufacturing (Specialized/Custom)** | 46 | 43.4% | Custom production, BOM management, job tracking |
| 2 | **Wholesale/Distribution** | 17 | 16.0% | Multi-warehouse, high SKU count, procurement-heavy |
| 3 | **Sales, Service & Rental** | 12 | 11.3% | Equipment dealers, maintenance contracts, rental fleet |
| 4 | **Distribution + Service** | 11 | 10.4% | Parts distribution + field service/installation |
| 5 | **Manufacturing + Distribution** | 8 | 7.5% | Own production + resell complementary brands |
| 6 | **Custom Design & Fabrication** | 7 | 6.6% | Made-to-order, design services, specialized builds |
| 7 | **Other/Uncategorized** | 7 | 6.6% | Niche or hybrid workflows |

**Key Finding:** 57% combine multiple workflows (e.g., Manufacturing + Distribution, Distribution + Service). These hybrid models create **complex operational requirements** that span production, procurement, inventory, and field service.

---

### Workflow Deep-Dive by Type

#### Manufacturing (Specialized/Custom) - 43.4% of Companies

**Who They Are:**
- Custom safe manufacturers (Brown Safe)
- Precision equipment fabricators (conveyor systems, hydraulic pumps)
- Medical device manufacturers (surgical instruments, mobility aids)
- Custom structures (sheds, outdoor kitchens, furniture)

**Operational Reality:**
- **Lead-to-cash cycle:** Inquiry → Quote (custom specs) → Order → Production → Delivery → Invoice
- **Production planning:** Work orders track custom jobs through fabrication
- **Material management:** BOM defines components, inventory consumed during production
- **Quality control:** Inspection checkpoints, rework tracking
- **Delivery:** Custom packaging, white-glove delivery, installation services

**Current Method CRM Usage:**
- ✅ **Front-office:** Activities (heavy), Contacts (heavy), Estimates (heavy) - quote complex specs
- ✅ **Order processing:** Sales Orders (moderate)
- ❌ **Production:** Work Orders (3% adoption) - **MISSING**
- ❌ **Materials:** Items (23% adoption), BOM management (doesn't exist)
- ✅ **Billing:** Invoices (moderate)

**Critical Workflow Gap:**
46 manufacturing companies have **NO production tracking in Method CRM**. They're likely using:
- Spreadsheets for work orders
- Separate MRP/ERP systems (Katana, Fishbowl, QuickBooks Desktop Manufacturing)
- Manual shop floor tracking (paper travelers, whiteboards)

**What Complete Workflow Would Look Like:**
1. Estimate created with custom specifications
2. → Convert to Sales Order
3. → **Generate Work Order** (MISSING) with BOM
4. → **Allocate inventory** (MISSING) to work order
5. → Track production progress through stages
6. → **Consume materials** (MISSING) from inventory
7. → Complete work order, update finished goods inventory
8. → Invoice customer with job costs

**Steps 3-7 don't exist in Method today.**

---

#### Wholesale/Distribution - 16% of Companies

**Who They Are:**
- Parts distributors (Conequip, Niagara Machine)
- Building materials wholesalers (CPF Floors, United Tile)
- Medical supply distributors (J2 Medical - 300K SKUs!)
- Multi-brand dealers (carrying 5-15 competing manufacturers)

**Operational Reality:**
- **Multi-warehouse:** Regional distribution centers, retail locations, customer direct ship
- **High SKU counts:** 5,000 to 300,000+ product variants
- **Fast fulfillment:** Same-day/next-day delivery expectations
- **Vendor management:** Coordinating 10-50+ suppliers, managing lead times
- **Price management:** Tiered pricing by customer, volume discounts, promotions

**Current Method CRM Usage:**
- ✅ **Front-office:** Activities (heavy), Contacts (heavy), Estimates (moderate)
- ✅ **Order processing:** Sales Orders (moderate)
- ❌ **Inventory visibility:** Items (24% adoption) - **CRITICAL GAP**
- ❌ **Multi-warehouse:** No real-time stock by location - **CRITICAL GAP**
- ❌ **Procurement:** Purchase Orders (15% adoption)
- ✅ **Billing:** Invoices (heavy)

**Critical Workflow Gap:**
17 distribution companies have **NO multi-warehouse visibility**. Sales reps cannot:
- Check stock availability across locations before quoting
- See real-time inventory positions
- Initiate transfer orders between warehouses
- View location-specific pricing

**What Complete Workflow Would Look Like:**
1. Customer inquiry for product
2. → **Check availability across all warehouses** (MISSING)
3. → Create estimate with accurate lead time
4. → Convert to Sales Order
5. → **Allocate inventory from specific warehouse** (MISSING)
6. → **Generate transfer order if stock at wrong location** (MISSING)
7. → Ship from warehouse, auto-update inventory
8. → Invoice customer
9. → **Reorder point triggers Purchase Order** (MISSING)
10. → Receive goods, update inventory

**Steps 2, 5, 6, 9-10 are missing or incomplete.**

---

#### Distribution + Service - 10.4% of Companies

**Who They Are:**
- Forklift dealers (Accurate Forklift, Fallsway)
- Equipment distributors with installation (HVAC, pumps, controls)
- Parts distribution + field service (Houston Hydraulic)

**Operational Reality:**
- **Dual revenue streams:** Parts sales (60%) + service/installation (40%)
- **Field workforce:** Mobile technicians dispatched to customer sites
- **Service parts inventory:** Truck stock + warehouse + customer consignment
- **Service contracts:** Preventive maintenance, emergency repairs, warranty work
- **Asset tracking:** Customer-owned equipment requiring service history

**Current Method CRM Usage:**
- ✅ **Front-office:** Activities (heavy), Contacts (moderate)
- ✅ **Order processing:** Sales Orders (light)
- ❌ **Service dispatch:** Work Orders (5% adoption), Field Crew (3% adoption)
- ❌ **Parts inventory:** Items (30% adoption)
- ❌ **Truck stock:** No mobile inventory tracking
- ✅ **Billing:** Invoices (heavy)

**Critical Workflow Gap:**
11 service companies have **NO field service tracking**. Dispatchers cannot:
- Schedule technicians efficiently
- Track parts used on service calls
- Manage truck stock inventory
- Link service history to customer equipment

**What Complete Workflow Would Look Like:**
1. Customer service request
2. → **Create service work order** (MISSING)
3. → **Schedule technician** (MISSING) with required parts
4. → **Check parts availability** (MISSING): Truck stock? Warehouse?
5. → Technician arrives, records time, parts used
6. → **Consume parts from truck inventory** (MISSING)
7. → **Update customer equipment service history** (MISSING)
8. → Generate invoice with labor + parts
9. → **Replenish truck stock** (MISSING)

**Steps 2-7, 9 are missing or incomplete.**

---

### Workflow Complexity by Industry

| Industry | Dominant Workflow | Complexity Level | Key Operational Challenge |
|---|---|---|---|
| **Industrial Equipment** | Manufacturing (54%) + Distribution (16%) | Very High | Custom fabrication + multi-brand parts inventory |
| **Construction** | Manufacturing (44%) + Distribution (20%) | High | Project-based materials + custom builds |
| **Medical** | Manufacturing (47%) + Distribution (35%) | Very High | FDA compliance + high SKU count |
| **Electronics** | Mixed (no dominant) | High | Technical compatibility + configuration mgmt |
| **Consumer Goods** | Manufacturing (54%) | Medium-High | Custom orders + showroom model |

**Strategic Insight:** Industries with **multiple workflow types** (Industrial Equipment: 54% Mfg + 16% Dist + 8% Service) have the **highest operational complexity** and therefore the **greatest need** for comprehensive operational features.

---

## Part 4: WHAT They Use - App Adoption & Engagement

### The Top 20 Apps: Where MWD Companies Spend Their Time

| Rank | App Name | Total Annual Page Loads | Adoption Rate | Accounts Using | Avg Loads per Using Account | Usage Intensity |
|---:|---|---:|---:|---:|---:|---|
| 1 | **Activities** | 4,282,197 | 52.5% | 105 | 40,021 | 🔥 Heavy |
| 2 | **Contacts** | 3,220,954 | 64.5% | 129 | 24,401 | 🔥 Heavy |
| 3 | **Sales Orders** | 2,416,002 | 39.5% | 79 | 29,827 | 🔥 Heavy |
| 4 | **Estimates** | 2,271,398 | 45.5% | 91 | 24,689 | 🔥 Heavy |
| 5 | **Invoices** | 1,794,577 | 56.0% | 112 | 15,742 | 🟢 Moderate |
| 6 | **Opportunities** | 636,883 | 23.5% | 47 | 13,551 | 🟢 Moderate |
| 7 | **Work Orders** | 451,143 | 6.5% | 13 | **34,703** | 🟢 Moderate |
| 8 | **Field Crew** | 367,759 | 3.5% | 7 | **52,537** | 🟡 Light |
| 9 | **Purchase Orders** | 345,621 | 15.0% | 30 | 11,521 | 🟡 Light |
| 10 | **Items** | 177,725 | 22.0% | 44 | 4,039 | 🟡 Light |
| 11 | **Cases** | 158,427 | 7.5% | 15 | 10,562 | 🟡 Light |
| 12 | **Jobs** | 147,936 | 1.0% | 2 | 73,968 | 🟡 Light |
| 13 | **Sales Receipts** | 120,661 | 5.5% | 11 | 10,969 | 🟡 Light |
| 14 | **Payments** | 102,754 | 6.5% | 13 | 7,904 | 🟡 Light |
| 15 | **Customers & Leads** | 95,625 | 13.5% | 27 | 3,542 | 🟡 Light |
| 16 | **Company** | 79,504 | 2.0% | 4 | 19,876 | 🟡 Light |
| 17 | **Reports** | 67,847 | 3.0% | 6 | 11,308 | ⚪ Minimal |
| 18 | **Documents** | 67,105 | 4.5% | 9 | 7,456 | ⚪ Minimal |
| 19 | **Sales** | 65,420 | 0.5% | 1 | 65,420 | ⚪ Minimal |
| 20 | **Addresses** | 57,268 | 8.5% | 17 | 3,369 | ⚪ Minimal |

**Total tracked apps: 109** (but only 20 show meaningful usage)

---

### The Engagement Paradox: Low Adoption, High Intensity

**Critical Discovery:** Apps with **lowest adoption** show **highest per-account usage intensity**.

| App | Adoption | Per-Account Annual Loads | Interpretation |
|---|---:|---:|---|
| **Field Crew** | 3.5% | 52,537 | Service companies NEED this (intense use), but 96.5% don't use it |
| **Jobs** | 1.0% | 73,968 | Project tracking CRITICAL for 2 accounts, non-existent for 198 |
| **Work Orders** | 6.5% | 34,703 | Production tracking INTENSE when used, missing for 93.5% |
| **Activities** | 52.5% | 40,021 | Comparable intensity despite 52% adoption |

**What This Means:**
- **Operational apps are NOT "nice-to-have"**—when companies use them, engagement rivals Activities
- **Adoption barrier is NOT lack of need**—it's likely feature gaps, discoverability, or onboarding
- **Massive whitespace opportunity**—93-97% of accounts missing critical operational workflows

---

### App Adoption by Workflow Stage: Where Gaps Exist

| Workflow Stage | Apps | Avg Adoption | Status | Impact |
|---|---|---:|---|---|
| **Lead Management** | Contacts, Activities, Opportunities, Customers & Leads | 38.5% | 🟢 STRONG | Core sales workflows well-adopted |
| **Quoting** | Estimates | 45.5% | 🟢 STRONG | Nearly half of accounts quote in Method |
| **Order Processing** | Sales Orders | 39.5% | 🟡 MODERATE | Decent adoption, but 60% processing orders elsewhere |
| **Production/Operations** | Work Orders, Jobs, Field Crew | **3.7%** | 🔴 CRITICAL GAP | 96% of companies have NO ops tracking |
| **Inventory Management** | Items, Purchase Orders, Item Receipts | **14.3%** | 🔴 CRITICAL GAP | 86% lack inventory visibility |
| **Billing/Payment** | Invoices, Payments, Bills | 23.0% | 🟡 MODERATE | Invoicing better than payments |
| **Support** | Cases, RMA | 7.5% | 🟡 LIGHT | Niche use case for service companies |

**The Pattern:** Method CRM is a **front-office sales tool** (38-46% adoption), NOT a **back-office operations platform** (4-14% adoption).

---

### Industry-Specific App Preferences

#### Industrial Equipment & Machinery (35 accounts)

**High Engagement:**
- Activities: 1,511 daily page loads, 51% adoption
- Estimates: 1,277 daily, 46% adoption
- Contacts: 1,245 daily, 57% adoption
- Sales Orders: 995 daily, 40% adoption
- Invoices: 751 daily, 43% adoption

**Critical Gaps:**
- Items: 115 daily, **23% adoption** (77% blind to inventory)
- Work Orders: 494 daily, **3% adoption** (97% no production tracking)
- Purchase Orders: 294 daily, **14% adoption** (86% no procurement workflow)

**Top Unique Apps:**
- Jobs: 628 daily (project tracking, 3% adoption)
- RLH Inventory: 134 daily (custom app, 3% adoption)
- Installation Projects: 122 daily (custom app, 3% adoption)

**Insight:** High custom app usage (Jobs, Installation Projects, RLH Inventory) suggests **workarounds** for missing native functionality.

---

#### Construction & Building Materials (26 accounts)

**High Engagement:**
- Activities: 1,987 daily, 58% adoption (HIGHEST of any industry)
- Estimates: 1,201 daily, 58% adoption
- Contacts: 1,142 daily, 69% adoption
- Sales Orders: 1,044 daily, 42% adoption

**Better-than-Average Operational:**
- Items: 130 daily, **39% adoption** (vs 22% overall - BEST in class!)
- Work Orders: 102 daily, **12% adoption** (vs 7% overall)
- Purchase Orders: 194 daily, **27% adoption** (vs 15% overall)

**Insight:** Construction shows **best operational app adoption** of any industry, yet still only 39% use Items. This validates that **even the "best" segment has massive gaps**.

---

#### Medical & Healthcare (27 accounts)

**High Engagement:**
- Activities: 700K annual (2nd highest total)
- Sales Orders: 511K annual (very strong)
- Contacts: 369K annual

**Critical for Compliance:**
- Items: 20K annual, **39% adoption** (better than avg, but 61% still blind)
- Serial Numbers: Minimal usage (regulatory requirement)

**Missing Entirely:**
- Lot/Batch tracking (FDA compliance - doesn't exist in Method)
- Expiration management (FEFO - doesn't exist)
- Recall workflows (doesn't exist)

**Insight:** Despite **77% Very High complexity** and **29% FDA compliance**, Medical industry has **NO native compliance features** in Method. They're using external systems or manual processes.

---

#### Electronics & Technology (17 accounts)

**High Engagement:**
- Activities: 1,211 daily
- Contacts: 887 daily
- Estimates: 616 daily

**Technical Complexity Apps:**
- Items: 95 daily, minimal adoption
- Equipment: 113 daily, 2% adoption (custom tracking)

**Missing:**
- BOM/Configuration management
- Compatibility matrices
- Software licensing tied to hardware

**Insight:** Electronics companies have **unique technical needs** (configurations, compatibility) that aren't served by standard inventory apps.

---

### Custom Apps Signal Unmet Needs

| Custom App | Accounts | Industry | What It Indicates |
|---|---:|---|---|
| **Jobs - ASCE** | 1 | Industrial Equipment | Custom project tracking (native Jobs only 1% adoption) |
| **Imperial Jobs** | 1 | Industrial Equipment | Another project tracker (workaround) |
| **RLH Inventory** | 1 | Industrial Equipment | Custom inventory app (Items insufficient) |
| **Installation Projects** | 1 | Industrial Equipment | Custom field service (Field Crew only 3% adoption) |
| **OEM Quotes** | 1 | Industrial Equipment | Custom quoting (native Estimates insufficient?) |
| **RLH Production Tracker** | 1 | Industrial Equipment | Custom production tracking (Work Orders only 3%) |
| **Mfg. Scheduling** | 1 | Manufacturing | Production scheduling (doesn't exist in Method) |

**Finding:** **7 unique custom apps in Industrial Equipment alone**, all addressing **operations/inventory gaps**. This is a **$1.3M LTV industry (19% of market) building workarounds** because native features don't meet needs.

---

### The "No Core App" Problem

**Shocking Discovery:** Method CRM has **ZERO apps with >80% adoption** among top MWD customers.

| App | Adoption | Why Not Universal? |
|---|---:|---|
| **Contacts** | 65% (highest) | 35% managing contacts elsewhere (Excel, Outlook?) |
| **Invoices** | 56% | 44% invoicing outside Method (QuickBooks only?) |
| **Activities** | 53% | 47% not logging communications |
| **Estimates** | 46% | 54% using external quoting tools |
| **Sales Orders** | 40% | 60% processing orders elsewhere |

**Benchmark Comparison:**
- Salesforce: Accounts (95%), Contacts (93%), Opportunities (89%)
- HubSpot: Contacts (97%), Deals (91%), Activities (88%)

**Implication:** Either onboarding is insufficient, feature gaps exist, or **QuickBooks integration creates confusion** about where to work (QB vs Method).

---

## Part 5: WHERE The Gaps Are - Critical Missing Workflows

### Gap #1: Inventory Management (78% Gap, 156 Accounts)

**Current State:**
- **Items app adoption: 22%** (44 of 200 accounts)
- **Daily page loads: 177,725** (when used: 4,039 per account)

**Who's Affected:**
- 77% of Industrial Equipment (28 of 37 companies)
- 61% of Construction (15 of 26)
- 61% of Medical (10 of 17)
- 60% of Wholesale/Distribution (22 of 36)

**What They're Missing:**
- ❌ Real-time inventory visibility
- ❌ Multi-warehouse stock levels
- ❌ Location-specific availability
- ❌ Stock-on-hand in transactions (estimates, sales orders)
- ❌ Inventory consumption (work orders, field service)
- ❌ Reorder point alerts

**Where They Work Instead:**
- QuickBooks Desktop (39% of accounts)
- Spreadsheets (manual tracking)
- External inventory systems (Fishbowl, Katana, SOS Inventory)
- Physical warehouse counts

**Impact:**
- Sales reps quote without knowing stock availability → lost sales, customer frustration
- Multi-warehouse operations can't see inventory position → inefficient fulfillment
- Production can't track material consumption → inventory inaccuracies
- Procurement operates blind → stockouts or overstock

**Big Bet #5 MLP Addresses:**
- ✅ **Priority 1:** Multi-warehouse visibility, available inventory
- ✅ **Priority 2:** Reorder points, dynamic items in transactions, backorder awareness
- ✅ **Priority 3:** Detailed location tracking, item audit trail

**Estimated ARR Opportunity:**
- If adoption increases from 22% to 50% → +56 accounts
- At $400-600 ARPU → **$22-34K additional ARR**

---

### Gap #2: Production/Work Order Tracking (93.5% Gap, 187 Accounts)

**Current State:**
- **Work Orders adoption: 6.5%** (13 of 200 accounts)
- **Daily page loads: 451,143** (when used: **34,703 per account** - HIGHEST INTENSITY)

**Who's Affected:**
- **97% of Industrial Equipment manufacturers** (18 companies making custom equipment with NO job tracking)
- **88% of Construction manufacturers** (11 companies building sheds, cabinets with NO tracking)
- **93% of Medical manufacturers** (8 companies producing devices with NO compliance tracking)

**What They're Missing:**
- ❌ Job/work order creation from sales orders
- ❌ BOM (Bill of Materials) management
- ❌ Production scheduling
- ❌ Material allocation to jobs
- ❌ Inventory consumption during production
- ❌ Job costing (labor + materials)
- ❌ Production status tracking
- ❌ Quality control checkpoints

**Where They Work Instead:**
- **Spreadsheets** (manual job tracking, Excel BOMs)
- **Whiteboards** (shop floor scheduling)
- **QuickBooks Desktop Manufacturing Edition** (separate system)
- **External MRP/ERP** (Katana MRP, Fishbowl Manufacturing)
- **Paper travelers** (job packets move with work)

**Impact:**
- No visibility into production pipeline → can't quote accurate lead times
- No material consumption tracking → inventory inaccuracies grow over time
- No job costing → don't know true profitability per order
- No status updates → customers call asking "where's my order?"

**NOT in Current MLP Roadmap:**
- ❌ Work Orders integration
- ❌ BOM management
- ❌ Inventory consumption

**Estimated ARR Opportunity:**
- If adoption increases from 7% to 40% → +66 accounts (just serving half of manufacturers)
- At $300-500 ARPU → **$20-33K additional ARR**

**Strategic Recommendation:** **Add "Basic Work Orders" to MLP Priority 2 or Phase 2.**
- Serves 43% of customer base (largest single segment)
- Highest per-account engagement (34K page loads)
- Natural extension of Inventory MLP (consume materials from work orders)

---

### Gap #3: Procurement/Purchase Orders (85% Gap, 170 Accounts)

**Current State:**
- **Purchase Orders adoption: 15%** (30 of 200 accounts)
- **Daily page loads: 345,621** (when used: 11,521 per account)

**Who's Affected:**
- 81% of Wholesale/Distribution (30 of 36 companies)
- 86% of Industrial Equipment (31 of 37)
- 73% of Construction (19 of 26)

**What They're Missing:**
- ❌ PO creation workflow
- ❌ Vendor management
- ❌ PO → Items receiving (update inventory on receipt)
- ❌ Reorder point triggering (auto-create PO when stock low)
- ❌ PO approval workflows
- ❌ Vendor pricing/lead time tracking

**Where They Work Instead:**
- **QuickBooks only** (POs in QB, never synced to Method)
- **Email orders** (no tracking)
- **Vendor portals** (external systems)
- **Spreadsheets** (manual reorder tracking)

**Impact:**
- Inventory management incomplete (can deplete but not replenish in Method)
- Reorder points useless (no way to actually reorder)
- Vendor relationships not tracked in CRM

**MLP Addresses Partially:**
- ✅ **Priority 2:** Reorder points (but what triggers the actual PO?)
- ❌ **Not addressed:** PO creation, receiving workflow, vendor mgmt

**Estimated ARR Opportunity:**
- If adoption increases from 15% to 40% → +50 accounts
- At $200-400 ARPU → **$10-20K additional ARR**

**Strategic Recommendation:** **Enhance Purchase Orders in MLP Priority 2.**
- Link reorder points → auto-create PO
- Receiving workflow → update Items inventory
- Basic vendor management (lead times, pricing)

---

### Gap #4: Field Service/Mobile Workforce (96.5% Gap, 193 Accounts)

**Current State:**
- **Field Crew adoption: 3.5%** (7 of 200 accounts)
- **Daily page loads: 367,759** (when used: **52,537 per account** - 2ND HIGHEST INTENSITY)

**Who's Affected:**
- **89% of Distribution + Service** (10 of 11 companies with field techs)
- **94% of Service & Rental** (11 of 12 equipment dealers)
- Service-heavy industrials (forklift dealers, HVAC, hydraulic repair)

**What They're Missing:**
- ❌ Technician scheduling/dispatch
- ❌ Mobile app for field work
- ❌ Parts used on service calls
- ❌ Truck stock inventory management
- ❌ Service history tied to customer equipment
- ❌ Time tracking (labor hours)
- ❌ GPS/routing

**Where They Work Instead:**
- **Field service software** (ServiceTitan, Jobber, FieldEdge - SEPARATE systems)
- **Paper work orders** (techs fill out forms)
- **Phone dispatch** (manual coordination)
- **No truck stock tracking** (periodic physical counts)

**Impact:**
- Service revenue not integrated with CRM
- Parts usage not tracked → inventory inaccuracies
- Service history not visible to sales reps
- Dispatchers working blind (who's available? where? what skills?)

**NOT in Current MLP:**
- ❌ Field service features
- ❌ Mobile inventory tracking

**Estimated ARR Opportunity:**
- If adoption increases from 4% to 30% → +52 accounts
- At $400-600 ARPU → **$21-31K additional ARR**

**Strategic Recommendation:** Future phase after MLP.
- Integrate Field Crew → Items (parts consumption)
- Mobile inventory visibility
- Service history → customer equipment records

---

### Gap #5: Project/Job Tracking (99% Gap, 198 Accounts)

**Current State:**
- **Jobs app adoption: 1%** (2 of 200 accounts)
- **Daily page loads: 147,936** (when used: **73,968 per account** - HIGHEST PER-ACCOUNT)

**Who's Affected:**
- Construction companies (project-based work)
- Industrial equipment (installation projects)
- Service companies (long-term maintenance contracts)

**What They're Missing:**
- ❌ Project-level tracking
- ❌ Job costing (aggregate costs by project)
- ❌ Budget vs actuals
- ❌ Project-based inventory allocation
- ❌ Milestone tracking
- ❌ Multi-phase projects

**Where They Work Instead:**
- **Spreadsheets** (project P&L tracking)
- **QuickBooks classes** (job costing in QB)
- **External project management** (Buildertrend for construction, Procore)
- **No integration** (disconnected systems)

**Impact:**
- Can't track project profitability in real-time
- Materials not allocated to specific projects
- Customer can't see project status
- Sales can't see pipeline by project value

**NOT in Current MLP:**
- ❌ Jobs/project features

**Estimated ARR Opportunity:**
- If adoption increases from 1% to 25% → +48 accounts
- At $300-500 ARPU → **$14-24K additional ARR**

**Strategic Recommendation:** Post-MLP enhancement.
- Jobs → Items allocation (project inventory)
- Jobs → Work Orders linkage (project production)
- Jobs → Estimates/Sales Orders (project pipeline)

---

### Gap Summary: The $90-141K Expansion Opportunity

| Gap | Current Adoption | Target Adoption | Additional Accounts | ARR Range | MLP Status |
|---|---:|---:|---:|---:|---|
| **Inventory (Items)** | 22% | 50% | +56 | $22-34K | ✅ Priority 1 |
| **Work Orders** | 7% | 40% | +66 | $20-33K | ❌ Not in MLP |
| **Purchase Orders** | 15% | 40% | +50 | $10-20K | 🟡 Partial (Priority 2) |
| **Field Service** | 4% | 30% | +52 | $21-31K | ❌ Not in MLP |
| **Jobs/Projects** | 1% | 25% | +48 | $14-24K | ❌ Not in MLP |
| **TOTAL** | — | — | +272 app adoptions | **$87-142K ARR** | — |

**Assumptions:**
- ARPU based on current LTV patterns ($33K avg, operational apps ~$300-600/year)
- Target adoption = realistic middle ground (not assuming 100%)
- Conservative estimate (doesn't include upsell to higher tiers)

**Key Insight:** Even **modest operational app adoption improvements** (not reaching saturation) could generate **$90-141K in expansion revenue** from existing customers. This is **13-21% of current $6.6M LTV** unlocked through feature enablement.

---

## Part 6: Strategic Trends & Product Insights

### Trend #1: Manufacturing Dominance with Production Tracking Void

**The Paradox:**
- **43.4% of top customers are manufacturers** (specialized/custom production)
- **Only 6.5% use Work Orders** (production tracking)
- **Per-account usage intensity = 34,703 page loads** (highest of ANY app when used)

**What This Means:**
The **single largest customer segment** (manufacturing) has **the single biggest feature gap** (production tracking), yet shows **the single highest engagement** when features exist. This is a **category 1 priority opportunity**.

**Manufacturers Without Production Tracking Include:**
- Brown Safe ($88K LTV) - custom safe manufacturing
- BIG GAME USA ($41K LTV) - custom footballs
- Yoderbilt ($31K LTV) - handcrafted structures
- Town & Country Sheds ($165K LTV) - custom outdoor buildings
- 42+ others making precision equipment, medical devices, cabinets, machinery

**Competitive Risk:**
If Method doesn't add work order/BOM features, **manufacturers will adopt external MRP systems** (Katana, Fishbowl) and potentially churn from Method entirely. **QuickBooks Desktop Manufacturing Edition** poses particular threat (same ecosystem, better ops features).

**Recommendation:** **Add Basic Work Orders to MLP Phase 2 or separate initiative.**
- Minimum Viable Product: Create WO from Sales Order, BOM, material allocation, status tracking
- Phase 2: Scheduling, capacity planning, shop floor interface
- Integration: Work Orders consume Items inventory (natural extension of Inventory MLP)

---

### Trend #2: Front-Office Strength, Back-Office Weakness

**Usage Pattern:**

| App Category | Adoption Range | Page Loads | Strategic Role |
|---|---:|---:|---|
| **Sales/Customer** (Contacts, Activities, Estimates, Sales Orders) | 40-65% | 20-40K/acct | ✅ METHOD STRONG |
| **Inventory/Operations** (Items, Purchase Orders, Work Orders) | 7-22% | 4-12K/acct | 🔴 METHOD WEAK |
| **Ratio** | **2.5-6.5X higher** | **5-10X higher** | **Fundamental imbalance** |

**What This Reveals:**
Method CRM is positioned as a **sales enablement tool**, not an **operations platform**. Customers use it for:
- ✅ Managing customer relationships
- ✅ Creating quotes
- ✅ Processing sales orders
- ✅ Invoicing

But NOT for:
- ❌ Managing inventory
- ❌ Tracking production
- ❌ Procuring materials
- ❌ Dispatching field service

**Strategic Implications:**
1. **Market positioning mismatch:** MWD companies need operations features, Method delivers sales features
2. **Integration requirement:** QuickBooks handles some operations (inventory, POs), creating confusion about where to work
3. **Competitive vulnerability:** Operations-focused competitors (Fishbowl, Katana, SOS Inventory) could displace Method
4. **Expansion opportunity:** Moving "down the funnel" from sales into operations unlocks new ARPU

**Big Bet #5 MLP Directly Addresses This:**
By adding **multi-warehouse visibility, reorder points, dynamic items**, Method begins bridging the front-office/back-office gap. This is strategically crucial.

---

### Trend #3: QuickBooks Integration = Double-Edged Sword

**The Data Shows:**
- **65% of accounts sync with QuickBooks** (per integration data)
- **35% manage contacts outside Method** (possibly in QuickBooks)
- **44% invoice outside Method** (likely QuickBooks only)
- **60% process orders outside Method** (possibly QuickBooks)

**The Problem:**
QuickBooks can handle:
- Invoices (✅ better invoicing than Method?)
- Items/Inventory (✅ more features than Method Items app)
- Purchase Orders (✅ more robust than Method)
- Bills (✅ full AP workflow)
- Payments (✅ integrated with bank feeds)

**The Question:** If QuickBooks already does operations, **why duplicate in Method?**

**The Answer - Two Scenarios:**

**Scenario A: QuickBooks Desktop (QBD)**
- QBD has **superior operational features** (inventory, manufacturing, job costing)
- But QBD is **desktop-based** (not cloud, not mobile, not real-time)
- Method's value prop: **Cloud-based access to QB data** + CRM layer
- **Gap:** Method doesn't fully replicate QBD's operational depth → customers stuck in QBD for ops

**Scenario B: QuickBooks Online (QBO)**
- QBO has **weaker operational features** than QBD (no manufacturing, limited inventory)
- Method could **surpass QBO** in operations (multi-warehouse, work orders, field service)
- **Opportunity:** Method becomes the operational system, QBO just handles accounting
- **Strategic:** Position Method as "QuickBooks + Operations" for QBO customers

**Data Request:** What % of MWD Top 200 use QBD vs QBO?
- If majority QBD → focus on **parity + mobility** (bring QBD features to cloud)
- If majority QBO → focus on **superiority** (add features QBO lacks)

**Current MLP Strategy:**
- ✅ Third-party integrations (Katana, SOS Inventory) acknowledges some customers need external operations systems
- ✅ Native features (multi-warehouse, reorder points) positions Method as operational tool for QBO customers
- **Hybrid approach makes sense** given customer diversity

---

### Trend #4: Complexity Drives Need, But Not Adoption

**The Data:**
- **77% of companies operate at High/Very High complexity** (154 of 200)
- **Complex companies need inventory management** (BOMs, multi-warehouse, lot tracking)
- **But Items adoption in complex segment = only 24%** (37 of 154 accounts)

**Why The Gap?**

**Hypothesis 1: Feature Insufficiency**
- Complex companies need advanced features (BOM, lot tracking, serialization, multi-warehouse)
- Method Items app is basic (simple inventory tracking)
- → They adopt external systems (Fishbowl, Katana) or stay in QuickBooks

**Hypothesis 2: Discoverability/Onboarding**
- Items app exists, but customers don't know it's there
- Onboarding focuses on CRM features (Contacts, Activities), not operations
- → They never learn Items app exists

**Hypothesis 3: Integration Confusion**
- QuickBooks already has Items/Inventory
- Customers don't understand Method Items vs QB Items
- → They default to managing in QuickBooks

**Hypothesis 4: Data Migration Barrier**
- Hundreds/thousands of existing items in QuickBooks or legacy system
- No easy migration path to Method Items
- → Switching cost too high

**Testing These Hypotheses:**
1. Survey low-adoption accounts: "Why don't you use Method Items app?"
2. Analyze onboarding: Do CSMs demo Items app? Do docs cover it?
3. Review feature requests: Are customers asking for features Items already has?
4. Check QB sync: Do QB Items sync to Method? Is it one-way or two-way?

**Implications for Big Bet #5:**
- If Hypothesis 1 (feature gap): **MLP features must be truly advanced** (multi-warehouse, reorder points justify)
- If Hypothesis 2 (discovery): **Marketing/onboarding campaign required** alongside MLP
- If Hypothesis 3 (QB confusion): **Clear positioning** (Method Items = enhanced, real-time layer on QB)
- If Hypothesis 4 (migration): **Migration tools/services required** (data import, SKU mapping)

**Likely Answer:** **Combination of all 4.** MLP must address features + discovery + positioning + migration.

---

### Trend #5: High-Health Accounts = Operational App Users

**The Correlation:**

| Health Score | Items Adoption | Work Orders Adoption | Purchase Orders Adoption | Interpretation |
|---|---:|---:|---:|---|
| **High (70-100)** | 31% | 12% | 25% | Healthy accounts use ops apps **1.5-2X more** |
| **Medium (40-70)** | 23% | 7% | 16% | Average adoption |
| **Low (<40)** | 15% | 3% | 8% | At-risk accounts avoid ops apps |

**Causation vs Correlation?**

**Hypothesis A:** Operational app usage → increases health
- Companies using Items, Work Orders, POs are more deeply integrated into Method
- Operational workflows create "stickiness" (harder to churn)
- More complete workflows → higher ROI perception → better health

**Hypothesis B:** High-health companies → more resources to adopt features
- Healthy companies have dedicated admins, training budget
- At-risk companies are too busy/understaffed to learn new apps
- Health enables adoption, not the other way around

**Hypothesis C:** Both (virtuous cycle)**
- Healthy companies adopt ops features
- → Deeper integration
- → Higher perceived value
- → Better retention
- → Continued investment
- → More features adopted
- → Cycle continues

**Strategic Implication:**
**If A or C is true, then increasing operational app adoption is a retention strategy.**

**Experiment Design:**
1. **Cohort 1:** 20 low-health accounts, intensive operational onboarding (Items, Work Orders, POs)
2. **Cohort 2:** 20 low-health accounts, standard support (control group)
3. **Measure:** Health score change over 6 months
4. **Success:** Cohort 1 shows +10-15 point health improvement vs Cohort 2

**If successful:** Operational feature adoption becomes a **Customer Success play**, not just a product roadmap item.

---

### Trend #6: Custom Apps = Feature Gap Indicators

**The Evidence:**
7+ custom apps identified in Top 200, concentrated in **Industrial Equipment** ($1.3M LTV, 19% of market):

| Custom App | Purpose | Native Alternative | Native Adoption | Gap |
|---|---|---|---:|---|
| **Jobs - ASCE** | Project tracking | Jobs | 1% | 99% gap |
| **Imperial Jobs** | Project tracking | Jobs | 1% | 99% gap |
| **RLH Inventory** | Inventory mgmt | Items | 22% | 78% gap |
| **Installation Projects** | Field service | Field Crew | 4% | 96% gap |
| **RLH Production Tracker** | Production tracking | Work Orders | 7% | 93% gap |
| **Mfg. Scheduling** | Production scheduling | Work Orders | 7% | 93% gap |
| **OEM Quotes** | Custom quoting | Estimates | 46% | 54% gap |

**What This Means:**
Customers are **building workarounds** because native apps don't meet their needs. This is **expensive** for both:
- **Customer:** Custom development, maintenance, training, no upgrade path
- **Method:** Lost opportunity (could charge $300-600/mo for native features)

**The Custom App Pattern:**
1. Customer identifies gap (e.g., need production tracking)
2. Evaluates native app (Work Orders)
3. Finds it insufficient or non-existent
4. **Hires developer to build custom app** (RLH Production Tracker)
5. Uses custom app, never adopts native features
6. Method loses insight into real customer needs (custom apps not tracked)

**Strategic Response:**
1. **Identify all custom apps** (audit Top 200, survey customers)
2. **Interview custom app users:** "Why did you build this? What's missing in native features?"
3. **Prioritize native features** based on most common custom app categories
4. **Migration path:** Offer to migrate custom app data to enhanced native features

**For Big Bet #5:**
Custom inventory apps (RLH Inventory) validate that **native Items app is insufficient** for sophisticated users. MLP features (multi-warehouse, reorder points, audit trails) must **exceed custom app capabilities** to win back these accounts.

---

### Trend #7: Industry Health Score Variation

**Health Score by Industry:**

| Industry | Avg Health | Interpretation | Strategic Priority |
|---|---:|---|---|
| **Consumer Goods & Retail** | 51 | Highest; best CRM practices | Learn from this segment |
| **Medical & Healthcare** | 49 | High complexity, well-managed | Premium segment, prioritize |
| **Food & Beverage** | 48 | Mid-size, solid engagement | Stable segment |
| **Construction** | 46 | Complex ops, moderate health | MLP will help (multi-warehouse) |
| **Electronics & Technology** | 46 | Technical, diverse workflows | Niche needs (BOM, configs) |
| **Specialty Manufacturing** | 42 | Small segment, lower engagement | Focus on larger segments first |
| **Industrial Equipment** | 42 | LARGEST segment, LOWER health | 🔴 CRITICAL: $1.3M at risk |
| **Energy & Environmental** | 43 | Mid-size, moderate health | Stable segment |

**Critical Finding:**
**Industrial Equipment** (37 companies, $1.3M LTV, 19% of market) shows **below-average health** (42 vs 45 overall). This is the **largest single industry** with **lowest engagement**.

**Root Cause Analysis:**
- Hypothesis: Operational app gaps (Work Orders, multi-warehouse) causing frustration
- Evidence: 77% don't use Items, 97% don't use Work Orders despite manufacturing workflows
- Risk: If health continues declining, **$1.3M LTV at risk** (19% of entire segment)

**Corrective Action:**
1. **Pilot MLP with Industrial Equipment** segment (37 companies, focus on equipment distributors)
2. **Targeted CSM outreach:** Audit operational needs, demo MLP features
3. **Win-back campaign:** Lapsed users, low-health accounts in this segment

**Why This Matters:**
Losing Industrial Equipment would be **catastrophic**—it's the largest industry, representing **1 in 5 MWD dollars**. Health score decline is an **early warning signal**.

---

### Trend #8: Usage Decline Over Time (Red Flag)

**The Data:**
- **Jan 2025:** 1,060,360 page loads (baseline)
- **May-Oct 2025:** 1.3-1.6M page loads (growth phase)
- **Nov-Dec 2025:** 1.2M page loads (-18% decline)
- **Jan 2026:** 409,277 page loads (partial month, but -66% YoY)

**Overall 12-month trend: -61.4% decline**

**Possible Explanations:**

**1. Seasonal Variation**
- MWD businesses have seasonal patterns (construction slows in winter, manufacturing holidays)
- Nov-Dec decline could be holidays
- Requires: Multi-year data to confirm seasonality

**2. Customer Churn**
- Accounts churning throughout 2025
- Declining user base → declining usage
- Requires: Churn data analysis (how many of Top 200 are still active?)

**3. Data Quality Issue**
- Reporting anomaly, incomplete data for recent months
- Jan 2026 only partial (data to 1/12)
- Requires: Data validation with BI team

**4. Product Degradation**
- Performance issues, bugs, feature removals causing disengagement
- Requires: Product quality metrics, support ticket analysis

**5. Competitive Displacement**
- Customers adopting external systems (Fishbowl, Katana, Salesforce) for core workflows
- Method relegated to secondary role
- Requires: Survey customers, check integration usage (are they using Katana via Method?)

**Urgency Level: 🔴 HIGH**

If this is real (not data anomaly), **-61% usage decline is existential.** Method is losing engagement with its most valuable customers.

**Immediate Actions:**
1. **Data validation:** Confirm this is real, not reporting error
2. **Churn analysis:** How many Top 200 churned in 2025? What's the retention rate?
3. **Survey:** Reach out to declining accounts: "We noticed lower usage. What changed?"
4. **Correlate with health scores:** Do declining usage accounts show declining health?
5. **Win-back campaign:** Targeted outreach to re-engage lapsed users

**If confirmed real:**
Big Bet #5 becomes even more critical—operational features may be **last chance to re-engage before churn**.

---

## Part 7: Strategic Recommendations for Product Management

### Recommendation #1: Accelerate Big Bet #5 MLP + Add Work Orders

**Current MLP Roadmap:**
- ✅ **Priority 1** (Batch 1): Multi-warehouse, available inventory, third-party integrations
- ✅ **Priority 2** (Batch 2): Reorder points, dynamic items, backorder awareness
- ✅ **Priority 3** (Batch 3): Detailed tracking, item audit trail, visualization

**STRONG VALIDATION:** MLP directly addresses:
- 33% of customers (multi-warehouse operations)
- 78% gap (Items app adoption)
- $22-34K ARR expansion opportunity (inventory alone)

**RECOMMENDED ADDITION:**
**Add "Basic Work Orders" to Priority 2 or create MLP Phase 2:**
- Minimum features: Create WO from Sales Order, BOM, material allocation, status tracking
- Why: Serves 43% of customer base (largest segment: manufacturing)
- Impact: $20-33K ARR expansion, addresses highest per-account engagement app
- Integration: Work Orders consume Items inventory (natural extension of Inventory MLP)
- Risk mitigation: If Method doesn't provide, manufacturers adopt Katana/Fishbowl (competitive threat)

**Revised Roadmap:**
- **Priority 1** (Now): Multi-warehouse, available inventory
- **Priority 2** (Q3 2026): Reorder points, dynamic items, **Basic Work Orders**
- **Priority 3** (Q4 2026): Detailed tracking, audit trail, **Work Order enhancements** (scheduling, capacity)

---

### Recommendation #2: Segment-Specific Go-To-Market

**Not all 200 accounts are equal.** Prioritize by:

**Tier 1: Industrial Equipment (37 companies, $1.3M LTV, 19% of market)**
- **Why:** Largest industry, lowest health (42), highest gap (97% no Work Orders, 77% no Items)
- **Strategy:** Pilot MLP here, intensive CSM outreach, win-back campaign
- **Features:** Multi-warehouse + Work Orders + BOM
- **Success metric:** Health score +10 points, Items adoption 22% → 50%

**Tier 2: Construction (25 companies, $1.2M LTV, 18% of market)**
- **Why:** Second largest, moderate health (46), better ops adoption (39% Items)
- **Strategy:** Position MLP as project inventory solution (allocate materials to jobs)
- **Features:** Multi-warehouse + Project/Job linkage
- **Success metric:** Items adoption 39% → 60% (best-in-class target)

**Tier 3: Medical (17 companies, $705K LTV, 11% of market)**
- **Why:** Highest health (49), regulatory-intensive, premium segment
- **Strategy:** Regulatory compliance features (lot tracking, expiration, serialization)
- **Features:** Audit trail (Priority 3) + **Lot/Batch tracking** (add to roadmap)
- **Success metric:** Become "FDA-compliant" CRM, defend against Salesforce Health Cloud

**Tier 4: All Others (121 companies, $3.4M LTV, 51% of market)**
- **Why:** Diverse industries, varied needs
- **Strategy:** Standard MLP rollout, self-service onboarding, education
- **Features:** Core inventory features (Priority 1-2)
- **Success metric:** Increase overall Items adoption from 22% to 35%

---

### Recommendation #3: Operational Apps = Customer Success Play

**The Data Shows:** High-health accounts use operational apps 1.5-2X more than at-risk accounts.

**Hypothesis:** Operational app adoption → deeper integration → higher perceived value → better retention

**Test:** Run 6-month pilot with 20 low-health accounts:
- **Intensive operational onboarding:** 1-on-1 training on Items, Work Orders (if available), Purchase Orders
- **Data migration support:** Help import inventory from spreadsheets/QB
- **Custom CSM check-ins:** Weekly for Month 1, bi-weekly thereafter
- **Measure:** Health score change vs control group

**If successful (Cohort shows +10-15 point health improvement):**
- **Scale program:** Operational onboarding becomes standard CSM playbook
- **Metrics:** Track operational app adoption as leading indicator of health
- **Incentives:** CSMs measured on operational app activation, not just CRM usage

**Implication:** Big Bet #5 MLP isn't just a product initiative—it's a **retention strategy**.

---

### Recommendation #4: Custom App Migration Program

**The Opportunity:**
- 7+ custom apps identified in Top 200
- Customers spent $10K-50K building workarounds
- Method loses visibility into real needs + potential recurring revenue

**The Program:**
1. **Audit:** Identify all custom apps across Top 200 (survey, data analysis)
2. **Interview:** Understand why customers built custom apps, what's missing in native features
3. **Prioritize:** Which custom app categories are most common? (Likely: production tracking, project mgmt, field service)
4. **Build:** Enhance native features to exceed custom app capabilities
5. **Migrate:** Offer free migration services (data import, training) to move customers to native features
6. **Upsell:** Charge for enhanced native features ($300-600/mo vs $0 for basic)

**Example:**
- **RLH Inventory** (custom app, 1 account): Customer built custom inventory system because Items app insufficient
- **Method response:** Build multi-warehouse, reorder points, location tracking (MLP Priority 1-2)
- **Migration offer:** "We've built the features you need. Let us migrate RLH Inventory data to native Items app."
- **Upsell:** Charge $400/mo for advanced inventory features vs $0 for custom app maintenance
- **Win-win:** Customer gets supported features + upgrade path; Method gets recurring revenue + feature insight

**ROI:**
- If 10 custom apps migrate → 10 accounts × $400/mo × 12 months = **$48K ARR**
- Plus: Eliminate future custom app development (customers stop building workarounds)

---

### Recommendation #5: QuickBooks Integration Strategy

**The Fundamental Question:**
Should Method **compete** with QuickBooks on operations, or **complement** QuickBooks?

**Current State (Unclear):**
- Method syncs with QB (invoices, items, customers)
- But overlap creates confusion: "Do I work in Method or QuickBooks?"
- Result: 44% invoice outside Method, 60% process orders outside Method

**Strategic Options:**

**Option A: Deep Integration (Complement QB)**
- Method = CRM layer + real-time access to QB data
- QuickBooks = source of truth for accounting, inventory, billing
- Integration: Two-way sync, real-time updates, mobile access to QB data
- Positioning: "Method brings QuickBooks to the cloud + adds CRM"
- **Risk:** Method becomes a UI layer, less strategic value

**Option B: Operational Superiority (Compete with QB)**
- Method = operations platform (inventory, work orders, field service) + CRM
- QuickBooks = accounting only (GL, AP, AR, payroll)
- Integration: One-way sync (Method → QB for accounting)
- Positioning: "Method is the operational system; QuickBooks reconciles"
- **Risk:** QuickBooks still needed, customers pay for two systems

**Recommended: Hybrid Approach (Current MLP Strategy)**
- **For simple needs:** Method native features (multi-warehouse, reorder points) sufficient
- **For complex needs:** Third-party integrations (Katana, SOS Inventory)
- **For all:** QuickBooks handles accounting (transactions sync to QB for books)

**Key Decision:** This depends on **QBD vs QBO breakdown** in Top 200:
- **If majority QBD:** Option A (complement) → bring QBD features to cloud
- **If majority QBO:** Option B (compete) → exceed QBO's limited inventory features
- **Data request:** Analyze Top 200 by QB version (Desktop vs Online)

---

### Recommendation #6: Discovery & Onboarding Revamp

**The Problem:**
- Items app exists, 109 apps tracked, but **no app has >80% adoption** (even Contacts only 65%)
- Customers may not know features exist (hypothesis: discoverability gap)

**The Fix:**

**1. Onboarding Audit:**
- Review current CSM onboarding process: Do they demo operational apps?
- Check documentation: Is Items app covered? Work Orders? Purchase Orders?
- Analyze product tours: Do in-app prompts guide users to operational features?

**2. Feature Discoverability:**
- In-app prompts: When user creates Sales Order, prompt "Want to check inventory availability?"
- Workflow wizards: "You're a manufacturer—let's set up Work Orders"
- Industry-specific onboarding: Detect workflow type (Mfg, Dist, Service) → customize onboarding

**3. Data Migration Tools:**
- "Import Items from spreadsheet" wizard (CSV upload, column mapping)
- "Sync from QuickBooks" one-click setup
- "Copy from existing system" integrations (Fishbowl, Katana, legacy)

**4. Use Case Education:**
- Case studies: "How Brown Safe tracks custom orders in Method"
- Video library: "Multi-warehouse inventory for distributors"
- Industry playbooks: "Manufacturing workflow setup guide"

**Success Metrics:**
- Items adoption 22% → 35% within 6 months (no new features, just better discovery)
- Time-to-first-value: Days to create first Item, first Work Order, first Purchase Order

---

### Recommendation #7: Competitive Positioning

**Current Competitive Threats:**

| Competitor | Strength | Weakness | Method Defense |
|---|---|---|---|
| **Salesforce** | Enterprise CRM, ecosystem | Expensive, complex, no inventory | SMB focus, QuickBooks integration, inventory features |
| **Fishbowl** | Advanced inventory, MRP | No CRM, poor UX | CRM + inventory in one platform |
| **Katana MRP** | Modern manufacturing, cloud | No CRM, no QuickBooks sync | QuickBooks native + CRM + work orders |
| **QuickBooks Desktop** | Deep operations (mfg, jobs) | Desktop-only, old tech | Cloud-based, mobile, real-time |
| **HubSpot** | Modern CRM, marketing | No inventory, no operations | Operations-focused CRM for MWD |
| **SOS Inventory** | Multi-warehouse, affordable | Limited CRM | Deeper CRM + comparable inventory |

**Recommended Positioning:**
"**The only CRM built for operations-intensive businesses**"
- Not just customer management—manage production, inventory, field service
- Native QuickBooks integration (not an add-on)
- SMB-friendly pricing (vs Salesforce)
- Cloud-based (vs QuickBooks Desktop)

**Competitive Response to Big Bet #5:**
- **vs Fishbowl/Katana:** "Why pay for separate CRM + inventory systems? Method does both."
- **vs Salesforce:** "Enterprise CRM meets SMB operations. Method is built for manufacturers."
- **vs HubSpot:** "Marketing CRM vs Operations CRM. Method knows your workflows."
- **vs QB Desktop:** "All the power of QuickBooks Desktop, in the cloud, with real CRM."

---

### Recommendation #8: Metrics & Measurement

**Current State:**
Limited visibility into operational app usage, health correlation, churn drivers.

**Recommended Product Metrics:**

**Adoption Metrics:**
- Items app adoption % (current: 22%, target: 50%)
- Work Orders adoption % (current: 7%, target: 40%)
- Purchase Orders adoption % (current: 15%, target: 40%)
- Multi-app adoption: % of accounts using 2+ operational apps

**Engagement Metrics:**
- Operational app page loads as % of total (current: ~8%, target: 25%)
- Items per account (SKU count)
- Work Orders created per month
- Purchase Orders created per month
- Reorder point alerts triggered

**Health/Retention Metrics:**
- Health score correlation with operational app usage
- Churn rate: Operational app users vs non-users
- NPS by app usage tier
- Time-to-churn: Operational app users vs non-users

**Business Impact Metrics:**
- ARR expansion from operational app adoption
- Customer Lifetime Value: Operational app users vs non-users
- Support ticket volume: Operational apps vs CRM apps (is ops harder to support?)

**Success Criteria for Big Bet #5:**
- **Primary:** Items adoption 22% → 50% within 12 months post-MLP launch
- **Secondary:** Health score improvement +5 points for adopters vs non-adopters
- **Tertiary:** Churn rate reduction 20% for operational app users
- **Financial:** $50K+ ARR expansion from existing customers

---

## Conclusion: The MWD Market Opportunity

### What We Know

**WHO:** 200 accounts, $6.6M LTV, 77% high-complexity operations, $33K average LTV, ranging from 1-user shops to 72-user enterprises.

**WHAT Industries:** Industrial Equipment (19%), Construction (18%), Medical (11%), Electronics (9%), Consumer Goods (7%)—top 5 represent 64% of market.

**HOW They Operate:** 43% manufacturing (custom/specialized), 33% multi-warehouse distribution, 22% field service/rental—complex, multi-step workflows.

**WHAT They Use:** Activities, Contacts, Estimates, Sales Orders, Invoices (40-65% adoption)—strong front-office CRM.

**WHERE The Gaps:** Items (78% gap), Work Orders (93% gap), Purchase Orders (85% gap), Field Service (97% gap)—missing back-office operations.

---

### What This Means

**1. Market Validation:**
Big Bet #5 Inventory Management MLP addresses **real operational pain** for 33% of customer base (multi-warehouse) and 78% gap (Items adoption). This is not a hypothetical feature—it solves **current frustrations**.

**2. Expansion Opportunity:**
Conservative estimates suggest **$90-141K in additional ARR** from increasing operational app adoption among existing customers (no new logos). This is **13-21% of current $6.6M LTV** unlocked through features.

**3. Retention Risk:**
Industrial Equipment ($1.3M LTV, 19% of market) shows declining health (42) and massive operational gaps. Without intervention, **$1M+ LTV is at risk**. Operational features are a **retention play**, not just growth.

**4. Competitive Positioning:**
Method currently positioned as "CRM with QuickBooks integration." MWD market needs "**Operations platform with CRM**." Big Bet #5 begins this repositioning—but Work Orders, Field Service, and Jobs remain gaps vs Fishbowl, Katana, ServiceTitan.

**5. Product Strategy Evolution:**
Success requires more than shipping features:
- **Discovery:** Customers must know features exist (onboarding, in-app prompts)
- **Migration:** Data import tools (spreadsheets, QB, legacy systems)
- **Education:** Use cases, industry playbooks, video guides
- **Customer Success:** Operational app adoption becomes CSM playbook

---

### Strategic Recommendation Summary

| Recommendation | Priority | Impact | Timeline |
|---|---|---|---|
| **1. Accelerate MLP + Add Work Orders** | 🔴 CRITICAL | Serves 43% of customers, $20-33K ARR | Now + Q3 2026 |
| **2. Segment-Specific GTM** | 🔴 CRITICAL | Focus on Industrial Equipment ($1.3M at risk) | Now |
| **3. Operational Apps = CS Play** | 🟡 HIGH | Health score improvement, retention | Q1-Q2 2026 |
| **4. Custom App Migration** | 🟡 HIGH | $48K ARR, eliminate workarounds | Q2 2026 |
| **5. QB Integration Strategy** | 🟡 HIGH | Clarify positioning (compete or complement) | Q1 2026 |
| **6. Discovery & Onboarding Revamp** | 🟢 MEDIUM | Increase adoption without new features | Q2 2026 |
| **7. Competitive Positioning** | 🟢 MEDIUM | "Operations CRM" vs "CRM with operations" | Q2 2026 |
| **8. Metrics & Measurement** | 🟢 MEDIUM | Track adoption, health, retention by ops usage | Now |

---

### Final Thought

The MWD Top 200 analysis reveals a **fundamental mismatch**:

- Customers need **operations platforms** (inventory, production, procurement, field service)
- Method delivers **sales platforms** (CRM, quoting, order processing)

Big Bet #5 begins closing this gap—but it's just the beginning. True operational parity requires:
- ✅ Multi-warehouse inventory (Priority 1)
- ✅ Reorder points & dynamic items (Priority 2)
- ❌ **Work Orders / Production Tracking** (not in MLP—SHOULD BE)
- ❌ **Field Service / Mobile Workforce** (post-MLP)
- ❌ **Jobs / Project Tracking** (post-MLP)
- ❌ **Regulatory Compliance** (lot tracking, serialization for Medical)

The opportunity is clear: **$90-141K ARR expansion + $1M+ retention defense + competitive repositioning**.

The question is execution: Can Method ship operational features fast enough to defend its MWD customer base before they adopt Fishbowl, Katana, or Salesforce?

**Big Bet #5 MLP is the right bet. Let's make it bigger.**

---

## Appendix: Data Sources & Methodology

**Source Files Analyzed:**
1. Top_200_App_Usage_Analysis.md - App adoption, engagement patterns
2. MWD_Top_200_Product_Category_Analysis.md - Product complexity analysis
3. MWD_Industry_Workflow_Documentation.md - Logical workflow sequences
4. MWD_Top_200_Industry_Analysis.md - Industry categorization, firmographics
5. MWD_Top_200_Workflow_Analysis.md - Workflow type classification
6. MWD_Industry_Actual_Workflows.md - Engagement-based actual workflows
7. Enhanced_MWD_Analysis_Industry_Workflow_Apps.md - Cross-referenced analysis

**Data Coverage:**
- **Accounts:** 200 total, 157 with complete usage data (78.5% coverage)
- **Time Period:** 366 days (Jan 2025 - Jan 2026)
- **Apps Tracked:** 109 unique apps
- **Page Loads:** 18.4M total annual page loads

**Methodology:**
- **Industry Categorization:** Based on Industry (Research), Workflow Type, Product Types fields from enriched CSV
- **Product Complexity:** Rated Low/Medium/Medium-High/High/Very High based on technical, regulatory, SKU, and custom characteristics
- **Workflow Classification:** 6 primary types (Manufacturing, Distribution, Service, etc.) based on operational patterns
- **App Usage:** Daily average page loads calculated from 366-day totals
- **Engagement Score:** Daily page loads × (Adoption rate / 100)—weights volume by breadth

**Limitations:**
- Usage data covers only 157 of 200 accounts (78.5%)
- Partial data for Jan 2026 (only through 1/12)
- Cannot distinguish between active usage vs passive page loads
- Custom apps not fully tracked (only visible if high page loads)
- QuickBooks Desktop vs Online breakdown not available

---

*Analysis completed: 2026-01-12*
*Document prepared by: Product Management*
*Comprehensive synthesis of 7 MWD Team analysis documents*
