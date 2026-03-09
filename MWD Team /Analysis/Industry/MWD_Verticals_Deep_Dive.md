# Manufacturing, Wholesale & Distribution (MWD): A Deep Dive

## Executive Summary

Manufacturing, Wholesale, and Distribution (MWD) represents the three major operational hubs of the supply chain—the network of all activities involved in creating and selling a product. This document provides an in-depth look at each vertical, their workflows, tools, objectives, and how they interconnect.

**Key Takeaway:** MWD businesses face unique inventory challenges that require specialized software capabilities. Understanding these verticals is critical for building effective inventory management solutions.

---

## Table of Contents

1. [Understanding the Supply Chain](#1-understanding-the-supply-chain)
2. [The MWD Framework](#2-the-mwd-framework)
3. [Manufacturing: The Value Creation Stage](#3-manufacturing-the-value-creation-stage)
4. [Wholesale: The Volume & Market Stage](#4-wholesale-the-volume--market-stage)
5. [Distribution: The Velocity Stage](#5-distribution-the-velocity-stage)
6. [Workflow Comparison Table](#6-workflow-comparison-table)
7. [How MWD Verticals Connect](#7-how-mwd-verticals-connect)
8. [Critical Integration Challenges](#8-critical-integration-challenges)
9. [Software Requirements by Vertical](#9-software-requirements-by-vertical)
10. [Implications for Method CRM](#10-implications-for-method-crm)

---

## 1. Understanding the Supply Chain

**Definition:** The supply chain is the network of all activities, people, organizations, information, and resources involved in the creation and sale of a product—from raw materials to end consumer.

**Flow Direction:**
- **Information:** Flows upstream (from customer → distributor → wholesaler → manufacturer)
- **Products:** Flow downstream (from manufacturer → wholesaler → distributor → customer)
- **Money:** Flows upstream (from customer back through the chain)

---

## 2. The MWD Framework

MWD categorizes the three major operational hubs of the supply chain:

| Vertical | Primary Function | Value Proposition |
|----------|------------------|-------------------|
| **Manufacturing (M)** | Transform raw materials into finished products | Value creation through production |
| **Wholesale (W)** | Purchase in bulk to bridge production and sales | Risk absorption and market access |
| **Distribution (D)** | Move and store goods to fulfill orders | Logistics efficiency and delivery |

**Important Note:** Many businesses operate across multiple verticals. A manufacturer might distribute directly to customers. A distributor might perform light assembly. The boundaries blur in practice.

---

## 3. Manufacturing: The Value Creation Stage

### Overview
Manufacturing is where the physical product is born. This stage transforms raw materials into finished goods through various production processes.

### Core Methodology: Material Requirements Planning (MRP)
MRP is the brain of manufacturing operations. It answers:
- **What** to produce?
- **How much** to produce?
- **When** to produce it?
- **What materials** are needed?

### Critical Tool: Bill of Materials (BOM)

**Definition:** A hierarchical list of every component, sub-assembly, and raw material needed to build a product.

**Structure Example:**
```
Bicycle (1 unit)
├── Frame Assembly
│   ├── Steel Tubing (2 meters)
│   ├── Welding Wire (0.5kg)
│   └── Paint (0.2 liters)
├── Wheel Assembly (2 units)
│   ├── Rim (1 unit)
│   ├── Spokes (36 units)
│   ├── Hub (1 unit)
│   └── Tire (1 unit)
└── Component Kit
    ├── Handlebars (1 unit)
    ├── Seat (1 unit)
    └── Chain (1 unit)
```

**Why BOMs are Critical:** If a single item on the BOM is unavailable, the entire assembly line stops. A missing $0.50 component can halt production of a $5,000 product.

### Standard Workflow: Plan-to-Produce

```
1. Demand Forecast
   ↓
2. Production Planning (MRP run)
   ↓
3. Raw Material Sourcing
   ↓
4. Sub-Assembly Production
   ↓
5. Final Assembly
   ↓
6. Quality Assurance
   ↓
7. Finished Goods Inventory
```

### Primary Objective: Unit Cost Efficiency

**Goal:** Produce as many units as possible at the lowest possible cost.

**Key Metric:** Overall Equipment Effectiveness (OEE)
- **Formula:** OEE = Availability × Performance × Quality
- **Target:** World-class manufacturing achieves 85%+ OEE

**Cost Drivers:**
- **Fixed Costs:** Machinery, facility rent, salaried workers
- **Variable Costs:** Raw materials, energy, hourly labor
- **Economies of Scale:** Spreading fixed costs across more units

### Unique Inventory Challenge: Work-in-Process (WIP)

**Definition:** Inventory that is currently on the factory floor being transformed—not yet salable.

**WIP Categories:**
1. **Raw Materials:** Received but not yet used
2. **In-Process:** Currently being worked on
3. **Semi-Finished:** Completed sub-assemblies awaiting final assembly
4. **Finished Goods:** Completed and ready for sale

**Management Challenge:** WIP ties up cash but generates no revenue. Manufacturers must balance:
- **Too Much WIP:** Capital locked up, storage costs, risk of obsolescence
- **Too Little WIP:** Production bottlenecks, idle machinery, missed deadlines

### Common Manufacturing Types

| Type | Description | Inventory Needs |
|------|-------------|-----------------|
| **Make-to-Stock (MTS)** | Produce based on forecasts | High finished goods inventory |
| **Make-to-Order (MTO)** | Produce after customer order | High raw materials inventory |
| **Assemble-to-Order (ATO)** | Stock sub-assemblies, final assembly on order | High sub-assembly inventory |
| **Engineer-to-Order (ETO)** | Custom design for each order | Project-based inventory |

### Risk Factors
- Machine breakdowns halting production
- Supply disruptions for raw materials
- Quality defects requiring rework
- Labor shortages or strikes
- Demand volatility causing overproduction or underproduction

---

## 4. Wholesale: The Volume & Market Stage

### Overview
Wholesalers act as the financial "buffer" between manufacturers and retailers/end users. They take on the risk of buying massive quantities to negotiate better pricing.

### Core Activity: Breaking Bulk

**Scenario:**
- **Manufacturer:** Produces 10,000 units per production run (minimum economical batch)
- **Retailer:** Only needs 50 units at a time
- **Wholesaler Role:** Buys 10,000 units, breaks into 200 orders of 50 units each

**Value Created:**
- **For Manufacturer:** Single large transaction instead of 200 small ones
- **For Retailer:** Access to products without massive capital outlay
- **For Wholesaler:** Profit margin on volume

### Standard Workflow: Procure-to-Pay

```
1. Demand Forecasting
   ↓
2. Supplier Negotiation
   ↓
3. Bulk Purchase Order
   ↓
4. Receipt & Inspection
   ↓
5. Warehousing
   ↓
6. B2B Sales & Fulfillment
   ↓
7. Payment Processing
```

### Primary Objective: Inventory Turnover

**Goal:** Sell inventory quickly to free up capital for the next purchase cycle.

**Key Metric:** Gross Margin Return on Investment (GMROI)
- **Formula:** GMROI = Gross Margin ÷ Average Inventory Cost
- **Example:** If you make $40,000 gross profit on $20,000 of average inventory, GMROI = 2.0
- **Interpretation:** For every $1 invested in inventory, you earn $2 in gross margin

**Capital Flow Challenge:**

```
Day 1: Wholesaler spends $100,000 to buy 10,000 units
Day 1-90: Inventory sits in warehouse (capital is "tied up")
Day 90: Sells all units for $150,000
Day 90: Now has $150,000 capital to buy next batch
```

**If inventory doesn't sell quickly:**
- Cash remains locked in unsold goods
- Can't buy new products
- Miss market opportunities
- Risk obsolescence or price drops

### Inventory Turnover Calculation

**Formula:** Inventory Turnover = Cost of Goods Sold ÷ Average Inventory

**Example:**
- Annual COGS: $1,200,000
- Average Inventory: $200,000
- Turnover Ratio: 6x per year (inventory "turns" every 2 months)

**Industry Benchmarks:**
- **Fast-moving consumer goods:** 10-20x per year
- **Electronics:** 6-8x per year
- **Industrial equipment:** 3-5x per year

### Key Advantage: Aggregation

**For Manufacturers:**
- Single point of contact instead of managing thousands of small customers
- Predictable bulk orders
- Reduced sales and marketing costs
- Simplified logistics (one shipment vs. many)

**For Retailers:**
- Access to diverse product lines from multiple manufacturers
- Better payment terms than buying direct
- Smaller order quantities
- Established distribution network

### Risk Factors
- Market price drops after bulk purchase
- Demand shifts making inventory obsolete
- Supplier reliability issues
- Competition from direct-to-consumer manufacturers
- Cash flow constraints if inventory doesn't move

---

## 5. Distribution: The Velocity Stage

### Overview
While wholesale focuses on ownership and sale of goods, distribution focuses on the **physical flow**. This is the logistics engine of the supply chain.

### Core Tool: Warehouse Management System (WMS)

**Purpose:** Track the exact location (aisle, shelf, bin) of every item to enable fast, accurate order fulfillment.

**Key WMS Functions:**
1. **Receiving:** Scan items as they arrive, assign storage locations
2. **Put-away:** Optimize placement based on velocity (fast-movers near shipping)
3. **Picking:** Generate optimal routes through warehouse to gather order items
4. **Packing:** Verify correct items, package appropriately
5. **Shipping:** Generate labels, schedule carriers, track outbound

**Location Precision Example:**
```
Item: Widget ABC-123
Location: Warehouse-North, Zone-A, Aisle-12, Shelf-3, Bin-7
Quantity: 47 units
Status: Available
```

### Standard Workflow: Order-to-Cash

```
1. Customer Order Received
   ↓
2. Order Validation (credit check, inventory availability)
   ↓
3. Pick List Generation
   ↓
4. Warehouse Picking
   ↓
5. Quality Check & Packing
   ↓
6. Carrier Selection & Shipping
   ↓
7. Delivery & Proof of Delivery
   ↓
8. Invoice & Payment Collection
```

### Primary Objective: The Perfect Order

**Definition:** The right product, in the right quantity, in the right condition, at the right place, at the right time, for the right customer, with the right documentation, at the right price.

**Key Metrics:**

| Metric | Formula | Target |
|--------|---------|--------|
| **Order Accuracy** | Error-free orders ÷ Total orders | 99%+ |
| **On-Time Delivery** | On-time deliveries ÷ Total deliveries | 95%+ |
| **Order Cycle Time** | Time from order to delivery | < 24-48 hours |
| **Perfect Order Rate** | Orders meeting all criteria ÷ Total orders | 90%+ |
| **Fill Rate** | Orders filled completely ÷ Total orders | 95%+ |

### Key Technologies

**1. Barcoding**
- Unique identifier for each product and location
- Reduces picking errors by 99%+
- Enables real-time inventory tracking

**2. RFID (Radio Frequency Identification)**
- Automatically reads tags as items pass sensors
- No line-of-sight required (unlike barcodes)
- Can read hundreds of items simultaneously
- Higher cost but better for high-volume operations

**3. Route Optimization Software**
- Calculates most efficient delivery routes
- Considers traffic, delivery windows, vehicle capacity
- Reduces fuel costs by 10-30%

**4. Transportation Management System (TMS)**
- Selects optimal carriers
- Consolidates shipments
- Tracks in-transit inventory
- Manages freight costs

### Distribution Models

| Model | Description | Example |
|-------|-------------|---------|
| **Direct Distribution** | Manufacturer → Customer | Tesla, Dell |
| **Single-Level** | Manufacturer → Retailer → Customer | Most consumer goods |
| **Two-Level** | Manufacturer → Wholesaler → Retailer → Customer | Traditional retail |
| **3PL (Third-Party Logistics)** | Outsourced warehousing and fulfillment | Amazon FBA |

### Risk Factors
- Shipping delays (weather, carrier issues, customs)
- Damage during transit
- Theft or loss
- Delivery to wrong address
- Returns management complexity
- Seasonal demand spikes overwhelming capacity

---

## 6. Workflow Comparison Table

A single day in the life differs significantly across MWD verticals:

| Feature | Manufacturing | Wholesale | Distribution |
|---------|---------------|-----------|--------------|
| **Input** | Raw materials | Finished products (pallets) | Customer orders |
| **Primary Metric** | OEE (Overall Equipment Effectiveness) | GMROI (Gross Margin Return on Investment) | Order Cycle Time |
| **Main Software** | ERP / MRP | CRM / Purchasing System | WMS / TMS |
| **Daily Focus** | Production efficiency | Sales volume & margin | Fulfillment speed |
| **Inventory Type** | WIP, raw materials, finished goods | Finished goods only | Finished goods in transit |
| **Time Horizon** | Long (weeks to months for production) | Medium (days to weeks for sales) | Short (hours to days for delivery) |
| **Risk Factor** | Machine breakdown | Market price drop | Shipping delays |
| **Customer Type** | Wholesalers, distributors, large retailers | Retailers, businesses | End consumers, businesses |
| **Order Size** | Very large (bulk) | Medium to large (cases/pallets) | Small to medium (individual items) |
| **Profit Driver** | Production volume | Inventory turnover | Delivery efficiency |

---

## 7. How MWD Verticals Connect

### Information Flow (Upstream: Customer → Distributor → Wholesaler → Manufacturer)

```
Consumer buys product from retailer
   ↓
Retailer's inventory drops, triggers reorder to distributor
   ↓
Distributor forecasts demand, orders from wholesaler
   ↓
Wholesaler analyzes sales trends, places bulk order with manufacturer
   ↓
Manufacturer receives demand signal, plans production run
```

### Product Flow (Downstream: Manufacturer → Wholesaler → Distributor → Customer)

```
Manufacturer produces finished goods
   ↓
Ships pallets to wholesaler's warehouse
   ↓
Wholesaler receives, breaks bulk, stores
   ↓
Distributor orders cases from wholesaler
   ↓
Distributor receives, stores in local warehouse
   ↓
Customer orders, distributor picks/packs/ships
   ↓
Customer receives product
```

### Money Flow (Upstream: Customer → Distributor → Wholesaler → Manufacturer)

```
Customer pays distributor (credit card, invoice)
   ↓
Distributor pays wholesaler (net 30 terms)
   ↓
Wholesaler pays manufacturer (net 60 terms)
   ↓
Manufacturer pays suppliers for raw materials (various terms)
```

**Payment Terms Impact:**
- Distributor might receive payment in 7 days but owes wholesaler in 30 days = 23 days of cash cushion
- Wholesaler receives payment in 30 days but owes manufacturer in 60 days = must carry 30 days of cash gap
- Extended payment terms throughout the chain require significant working capital

---

## 8. Critical Integration Challenges

### Challenge 1: The Bullwhip Effect

**Definition:** Small fluctuations in consumer demand cause increasingly larger fluctuations upstream in the supply chain.

**Example Scenario:**

```
Retailer sees 5% increase in demand
   ↓
Orders 10% more from distributor (to be safe + build buffer)
   ↓
Distributor orders 15% more from wholesaler (safety stock + anticipated growth)
   ↓
Wholesaler orders 20% more from manufacturer (bulk order minimums + risk mitigation)
   ↓
Manufacturer increases production by 30% (long lead times + economies of scale)
```

**Result:** 5% demand increase triggers 30% production increase = massive overproduction

**Causes:**
1. **Demand Signal Processing:** Each level adds its own forecast buffer
2. **Batch Ordering:** Ordering in large, infrequent batches instead of small, frequent orders
3. **Price Fluctuations:** Promotional discounts cause artificial demand spikes
4. **Rationing & Shortage Gaming:** When supply is tight, customers inflate orders

**Solutions:**
- Real-time demand data sharing across supply chain
- Vendor-managed inventory (VMI)
- Smaller, more frequent orders (enabled by better logistics)
- Everyday low pricing instead of promotions

### Challenge 2: Lead Time Integration

**Definition:** The time required for each vertical to fulfill an order varies dramatically.

**Typical Lead Times:**
- **Manufacturing:** 2-12 weeks (depending on complexity)
- **Wholesale:** 1-2 weeks (receiving, breaking bulk, fulfillment)
- **Distribution:** 1-5 days (picking, packing, shipping)

**Synchronization Problem:**

```
Today: Distributor realizes demand will increase in 3 months
   ↓
Week 1: Places order with wholesaler
   ↓
Week 2: Wholesaler recognizes trend, orders from manufacturer
   ↓
Week 10: Manufacturer completes production run
   ↓
Week 12: Goods flow back to distributor
   ↓
Week 15: Distributor finally has stock to meet demand spike
```

**If forecasting is wrong:**
- **Under-forecast:** Stockouts, lost sales, frustrated customers
- **Over-forecast:** Excess inventory, storage costs, potential obsolescence

**Solution Requirements:**
- Accurate demand forecasting
- Early warning systems for demand changes
- Buffer inventory at strategic points
- Flexible production capacity
- Strong communication between verticals

### Challenge 3: Inventory Visibility

**Problem:** Each vertical maintains its own inventory records, creating blind spots.

**Scenario:**
- Manufacturer ships 1,000 units
- Wholesaler receives 1,000 units, sells 700, has 300 remaining
- Distributor receives 700 units, ships 600 to customers, has 100 remaining
- **Total Inventory:** 300 + 100 = 400 units in the channel

**Without Visibility:**
- Manufacturer doesn't know 400 units are still unsold
- Might produce another batch thinking demand is strong
- Results in oversupply and price pressure

**With Visibility:**
- Manufacturer sees channel inventory levels
- Adjusts production accordingly
- Avoids overproduction and maintains pricing

### Challenge 4: SKU Proliferation

**Definition:** Explosion in the number of unique products (Stock Keeping Units) as goods move through the chain.

**Example:**
```
Manufacturer: 1 product (Widget 2000)
   ↓
Wholesaler: 3 SKUs (Widget 2000 in Red, Blue, Green)
   ↓
Distributor: 9 SKUs (Red-Small, Red-Medium, Red-Large, Blue-Small, Blue-Medium, Blue-Large, etc.)
```

**Complexity Impact:**
- Forecasting difficulty increases exponentially
- Inventory carrying costs rise
- Risk of stockouts on specific SKUs while others sit unused
- Warehouse space and management complexity

---

## 9. Software Requirements by Vertical

### Manufacturing Software Stack

**Core Systems:**
1. **ERP (Enterprise Resource Planning)**
   - Central system integrating all business functions
   - Examples: SAP, Oracle, Microsoft Dynamics, NetSuite

2. **MRP (Material Requirements Planning)**
   - Calculates material needs based on production schedule
   - Often integrated within ERP

3. **MES (Manufacturing Execution System)**
   - Tracks work-in-process on factory floor
   - Real-time production monitoring

4. **PLM (Product Lifecycle Management)**
   - Manages BOMs, engineering changes, product versions

5. **QMS (Quality Management System)**
   - Tracks quality checks, defects, certifications

**Key Inventory Features Needed:**
- Multi-level BOM support
- WIP tracking by production stage
- Raw material tracking with lot/batch numbers
- Component substitution management
- Production yield tracking
- Scrap and rework management

---

### Wholesale Software Stack

**Core Systems:**
1. **CRM (Customer Relationship Management)**
   - Manages B2B customer relationships
   - Examples: Salesforce, HubSpot, Method CRM, Zoho

2. **Purchasing/Procurement System**
   - Manages supplier relationships and purchase orders
   - Often integrated with ERP

3. **Inventory Management System**
   - Tracks stock levels, locations, valuations
   - May be standalone or part of ERP

4. **Order Management System (OMS)**
   - Processes customer orders, manages fulfillment

5. **Pricing & Quoting System**
   - Manages volume discounts, customer-specific pricing

**Key Inventory Features Needed:**
- Multi-warehouse inventory visibility
- Available-to-promise (ATP) calculations
- Reorder point and economic order quantity (EOQ)
- Supplier lead time tracking
- Inventory aging reports
- Customer-specific stock reservations
- Demand forecasting and planning

---

### Distribution Software Stack

**Core Systems:**
1. **WMS (Warehouse Management System)**
   - Core system for distribution operations
   - Examples: Manhattan Associates, Blue Yonder, HighJump

2. **TMS (Transportation Management System)**
   - Manages carrier selection, routing, freight costs
   - Examples: Oracle TMS, JDA, MercuryGate

3. **OMS (Order Management System)**
   - Orchestrates order fulfillment across channels

4. **YMS (Yard Management System)**
   - Manages trucks and trailers at distribution facilities

5. **LMS (Labor Management System)**
   - Tracks worker productivity in warehouse

**Key Inventory Features Needed:**
- Bin/location-level tracking
- Real-time inventory accuracy (99%+)
- Lot/serial number tracking
- Expiration date management (for perishables)
- Cross-docking support
- Wave picking and batch picking
- Returns management and reverse logistics
- Multi-channel inventory allocation

---

## 10. Implications for Method CRM

### Why MWD Customers Are the Primary Target

**Customer Segment Characteristics:**
- **850 current MWD accounts** in Method CRM base
- **199 churned in 2024**—highest churn of any vertical
- **Complex inventory needs** spanning multiple locations
- **QuickBooks Online integration critical**—QBO is their system of record

### Specific MWD Pain Points Method Must Address

**Based on Discovery Research:**

1. **No Real-Time Inventory Visibility**
   - Current State: Must log into QBO to check stock levels
   - MWD Need: See available inventory directly in Method while working with customers

2. **Multi-Warehouse/Location Blind Spots**
   - Current State: QBO tracks locations, but Method doesn't expose this data
   - MWD Need: Know which warehouse has stock before promising delivery

3. **Transaction-Only Inventory Impact**
   - Current State: Inventory only updates when invoices/bills are created
   - MWD Need: Real-time adjustments for production, transfers, shrinkage

4. **No Integration with Advanced Inventory Systems**
   - Current State: Method can't connect to Katana, SOS Inventory, Fishbowl
   - MWD Need: Unified view when using specialized MRP/WMS alongside Method

### Priority Features for MWD Segment

**Mapped to MWD Vertical Needs:**

| MLP Priority | Feature | Manufacturing Need | Wholesale Need | Distribution Need |
|--------------|---------|-------------------|----------------|-------------------|
| **P1** | Multi-Warehouse Management | Track raw materials vs. finished goods by location | Manage regional warehouses | Fulfill from closest warehouse |
| **P1** | Available Inventory Visibility | Prevent selling WIP or reserved materials | Real-time ATP for sales | Accurate pick quantities |
| **P1** | Third-Party Integration | Connect to MRP systems (Katana) | Connect to purchasing systems | Connect to WMS (SOS Inventory) |
| **P2** | Reorder Points & Alerts | Prevent production line stoppages | Maintain inventory turnover targets | Avoid stockouts on fast-movers |
| **P2** | Dynamic Item Management | Handle BOM components | Manage SKU proliferation | Support multi-variant products |
| **P2** | Backorder Awareness | Communicate lead times to sales | Allocate limited stock fairly | Prioritize fulfillment |
| **P3** | Location-Based Tracking | Bin-level WIP tracking | Zone-level bulk storage | Aisle/shelf/bin picking |
| **P3** | Item Visualization | Product photos for configuration | Catalog images for sales | Visual picking aids |
| **P3** | Item Audit Trail | Track engineering changes | Monitor price changes | Investigate discrepancies |

### Competitive Positioning

**Other CRMs Serving MWD:**
- **Salesforce:** Integrates with NetSuite (ERP), TradeGecko (inventory), ShipStation (fulfillment)
- **HubSpot:** Integrates with Unleashed, Katana, Cin7
- **Zoho CRM:** Part of Zoho One suite including Zoho Inventory and Books
- **Pipedrive:** Integrates with Unleashed, DEAR Inventory

**Method's Advantage:**
- **Deep QuickBooks Integration:** Most MWD small businesses use QBO, not NetSuite
- **Hybrid Approach:** Native features for simple needs + integrations for complexity
- **Industry-Specific Templates:** Pre-built workflows for MWD verticals

### Success Metrics

**Churn Reduction:**
- Target: Reduce MWD churn from 199 accounts to <100 accounts annually
- ROI: 99 saved accounts × $2,390.54 LTV = $236,563 annual revenue retention

**New Customer Acquisition:**
- Target: Increase MWD market share from 3.4% to 5% over 2 years
- Opportunity: 1.6% × 25,000 target market = 400 new accounts
- Revenue: 400 accounts × $2,390.54 LTV = $956,216

**Feature Adoption:**
- Target: 80% of MWD customers actively using multi-warehouse features within 6 months of launch
- Measurement: Analytics tracking location-based inventory queries, transfers, reports

---

## Conclusion

Understanding the distinct workflows, objectives, and challenges of Manufacturing, Wholesale, and Distribution businesses is critical for building effective inventory management solutions. Each vertical has unique software needs:

- **Manufacturers** need BOM management, WIP tracking, and MRP integration
- **Wholesalers** need inventory turnover optimization and bulk-to-retail bridging
- **Distributors** need location-level precision and fulfillment velocity

Method CRM's Inventory Management System must address these diverse needs through its hybrid approach: native features for common requirements plus integrations for vertical-specific complexity.

**Key Success Factor:** Real-time inventory visibility across multiple locations—the single feature that addresses pain points across all three MWD verticals.

---

## Additional Resources

### Referenced in This Document
- Big Bet #5 Discovery Research (Partner & PS Team Interviews)
- Prototype Stage Competitive Analysis (12 CRM platforms)
- Build Stage Requirements Documentation (Modal, Multi-Location Management)

### Industry References
- APICS CPIM Certification (Manufacturing operations)
- Supply Chain Management Review (Industry trends)
- Gartner Magic Quadrant for WMS, TMS, ERP (Technology landscape)

### Method CRM Context
- See `/CLAUDE.md` for full product strategy context
- See `/Big Bet #5 - Inventory Management MLP/` for detailed requirements
- See `/Documentation/` for technical specifications

---

**Document Version:** 1.0
**Last Updated:** January 13, 2026
**Maintained By:** Product Management
**Related Documents:** CLAUDE.md, MLP Scope Definition, Multi-Warehouse Requirements
