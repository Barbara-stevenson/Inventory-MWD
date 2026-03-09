# Comprehensive Summary: MWD-Related Insights from Dovetail

## Overview

After searching all available Dovetail projects, data, and insights, I found MWD (Manufacturing, Wholesale & Distribution) related content across multiple sources. This document compiles all MWD-related findings from the Dovetail research repository.

**Data Sources Analyzed:**
- 47 Dovetail projects
- 154+ insights
- Multiple customer and partner interviews
- PS Team meeting notes
- Inventory prototype usability tests

---

## 1. Explicit MWD Mentions (PS Team Meeting - August 2023)

**Source:** PS Team Notes (Project: Continuous Interviewing 2023)

The PS team explicitly discussed MWD verticals in the context of:

### Packing Slips
> "A lot of customers ask for packing slips - basically the same as invoices without rates and amounts. **This is common in parts and automation (MWD), and textile.**" - Eric

### Advanced Inventory
> "A lot of customers have been asking about advanced inventory." - Brandon

> "A lot of people who work from sales orders and use fields like qty on hand, qty on order etc. Typically don't want to ship to their customers if they don't have the item in stock." - Salman

### Key Pain Points Identified

| Pain Point | Quote | Source |
|------------|-------|--------|
| Inventory sync limitations | "Have had a customer stop using Method because advanced inventory doesn't sync" | Aleks |
| Link Sales Orders to Purchase Orders | "Ability to create purchase transactions from sales transactions. Supporting both accounts receivable and accounts payable workflows... Want these to be linked together so they know when goods are ready to be sent out to the customer." | Ryan |
| Line item reordering | "Ability to reorder line items. Have more control over how Invoices, Estimates, Purchase Orders etc. appear." | Cameron |

---

## 2. Inventory Prototype Testing Interviews (4 Partners)

### Partner: Charvi Anand

**Key Insights:**

- **Serial numbers should be tracked per quantity, not as a static field:**
  > "You would have one serial number per quantity... each iPhone would have a serial number"

- **Warehouses shouldn't be required:**
  > "I don't know if everyone would want it this advanced. So maybe this should be an option than a requirement"

- **Location tracking** (aisle/bin/lot) should potentially be per serial number for items stored in multiple locations

- **Purchase order receiving:** In QuickBooks, inventory increases from bills or item receipts, not purchase orders directly

---

### Partner: Ryan

**Key Insights:**

- **Multi-warehouse filtering on transactions:**
  > "I've definitely worked with clients who have different warehouses based on very deep locations... entire order would be specifically like Victoria in Australia, whereas the other order might be Queensland"

- **Item audit trail is critical:**
  > "I would like the ability to see where the items kind of came from... on this day, you know, we added 500 quantity of this item to this warehouse. Or 500 of the 100 of this quantity was removed from this invoice"

- **Sales order backorder handling:**
  > "On sales orders it doesn't make much sense to stop someone from creating a sales order with a quantity that's not available... allocation of quantities once purchase orders are received"

- **Reorder points and low stock alerts:**
  > "I do really like this... from this case you could create the purchase order from there"

---

### Partner: Jason

**Key Insights:**

- **Real-time inventory sync is critical:**
  > "Having the quantity on hand being accurate in real time is very important. But quantity on hand doesn't update in method... it could take like 20 minutes or longer to update"

- **Purchase order receiving:**
  > "There's no way in Method with a QBO integrated account... to receive that product and sync it to QuickBooks. It has to be done in QuickBooks"

- **Dynamic reorder quantities:**
  > "Auto calculate the reorder quantity... based off sales history. Looking at the last quarter and seeing how much of this product has actually been ordered"

- **Key inventory fields needed:**
  - On hand
  - Available (on hand minus sales orders)
  - Reserved (committed to sales orders)
  - Incoming (quantity on PO)

---

### Partner: Paulette

**Key Insights:**

- **GL account requirements:**
  > "The item requires a sales and cost of goods sold account. You cannot enter this without having the GL numbers"

- **Proper inventory workflow:** Items should be entered first, then purchase orders, then receiving against POs - not direct quantity entry

- **Inventory adjustments:** Should only be done by authorized personnel in QuickBooks or Katana, not by salespeople in Method

- **Integration preference:**
  > "I happen to like Katana better. Visually it looks better, but SOS has been around for a long time"

---

## 3. Manufacturing Customer Interviews

### BrownSafe (Manufacturing - High-End Luxury Safes)

**Source:** Customer Interviews Project

**Company Profile:**
- Manufacturing business building high-end luxury safes
- 120 employees, 12-week production process
- Uses QuickBooks Desktop (Enterprise), Method CRM since 2018
- 177 custom screens built

**MWD-Relevant Pain Points:**

- **Production tracking:**
  > "The biggest challenge... is in manufacturing process is everything at the moment is done manually from start to finish"

- **Build sheets & barcoding:** Attempted to implement barcode tracking for production stages (cutting, welding, painting)

- **Production app issues:**
  > "The production app, I don't know if it's built out wrong, but it's very laggy"

**Key Use Cases:**
- Estimates, invoices, installation projects, payments, activities
- Build sheets generated from invoice data with dimensions and features

---

### Vintage Makers (Manufacturing - Wine Cellars)

**Source:** Customer Interviews Project

**Company Profile:**
- 32-year old wine cellar manufacturing company
- Only company that both manufactures AND installs in-house
- Also runs cigar humidor business with 3,400 SKUs
- Uses QuickBooks Enterprise (cloud-based)

**MWD-Relevant Insights:**

- **Multi-site inventory:**
  > "We're using QuickBooks for inventory because it's multi site"

- **Field sales with real-time inventory:** Technicians use tablets to access inventory data, pricing, and customer history in real-time

- **Complex tax calculations:** Different states have different taxes; Method handles these calculations

- **Item enrichment:** Photos associated with inventory items for field demonstrations

- **POS bi-directional sync:** Major pain point - QuickBooks POS discontinued, need bi-directional sync between POS and QuickBooks through Method

---

## 4. MWD-Tagged Insights (Insights Hub)

### "Transaction Items Improvements"
**Vertical Tag:** MWD, Field Services

- Need for better item management within transactions
- Line item reordering capabilities
- Grouping related items together

### "Search is critical and painful"
**Vertical Tag:** MWD, Field Services

- Fuzzy search needed for items in dropdowns
- Global search improvements
- Difficulty finding items leads to duplicates and data issues

---

## 5. Big Bet #2 PS Team Interviews (Customer Prioritization Focus)

### Zach Interview

**Relevant to MWD:**
- **Purchase history customization:** Commonly requested - shows purchases, lifetime value
- **Overdue balance tracking:** Block invoice creation when customer exceeds threshold
- **B2B complexity:** Managing multiple contacts at same company, sub-customer relationships

### Ashur Interview

**Relevant to MWD:**
- **Sales pipeline/Kanban boards:** Long-requested feature for tracking sales process
- **Department-specific apps:** Production apps for production team, warehouse apps for warehouse team
- **Data-driven insights:** Need to track what's selling, conversion rates per rep

---

## 6. Key Themes Across All MWD Data

### Must-Have Features

| Priority | Feature | Description |
|----------|---------|-------------|
| 1 | Multi-warehouse management | Location-based tracking (aisle/bin/lot) |
| 2 | Real-time inventory visibility | Across all transactions |
| 3 | Purchase order receiving | Currently blocked by QBO sync limitations |
| 4 | Reorder points & low stock alerts | With automatic PO generation |
| 5 | Serial number tracking | Per unit, not static |
| 6 | Item audit trail | History of quantity changes with source transactions |

### Critical Pain Points

1. **Inventory doesn't sync in real-time** - 20+ minute delays
2. **No PO receiving in Method** - must be done in QuickBooks
3. **Advanced inventory fields don't sync** - causing churn
4. **Sales orders blocked** when inventory unavailable (should allow backorders)
5. **Packing slips** needed without prices (common MWD request)
6. **Line item reordering** on transactions

### Integration Preferences

| Platform | Feedback |
|----------|----------|
| Katana | Visually better, modern interface |
| SOS Inventory | Established, reliable, long track record |
| **Hybrid approach** | Validated - core features native + integration for advanced |

### Workflow Requirements

```
1. Item setup → Purchase Order → Receiving → Inventory available
2. Sales Order → Check availability → Invoice → Decrease inventory
3. Backorder workflow when inventory unavailable
4. Dynamic reorder quantity based on sales history
```

---

## 7. Recommendations Based on Dovetail Research

### Immediate Priorities (Batch 1)
- Multi-warehouse management with real-time sync
- Available inventory visibility on all transaction screens
- Third-party integration (Katana/SOS) for advanced features

### Secondary Priorities (Batch 2)
- Reorder points with low stock alerts
- Backorder awareness and management
- Dynamic item management in transactions

### Future Considerations (Batch 3)
- Detailed location-based tracking (aisle/bin/lot)
- Serial number tracking per unit
- Item audit trail with full transaction history
- Item visualization (photos/images)

---

## Appendix: Dovetail Data Sources

| Project | Type | Key Content |
|---------|------|-------------|
| Continuous Interviewing 2023 | Interviews | PS Team meeting with explicit MWD mentions |
| Inventory mgt prototype usability tests | Usability Testing | 4 partner interviews (Charvi, Ryan, Jason, Paulette) |
| Big bet 2 - interviews with PS team | Interviews | Zach, Ashur interviews |
| Customer interviews | Interviews | BrownSafe (manufacturing), Vintage Makers (manufacturing) |
| Insights hub | Insights | MWD-tagged insights on transactions and search |
| Field Services Customer Interviews | Interviews | 24 interviews with field service customers |

---

*Document generated from Dovetail research repository - January 2026*
