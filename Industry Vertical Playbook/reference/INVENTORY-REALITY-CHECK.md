# Inventory Reality Check — What Method Can and Cannot Do Today

**Created:** March 2026
**Purpose:** Single source of truth for how we position inventory in the MWD playbook. The upcoming Inventory Management product is NOT launched yet and is several quarters out. Do not reference it in any playbook deliverable.

---

## What Method Has Today (via QuickBooks Sync)

Method does not have a standalone inventory management system. What it has is **inventory item types that sync with QuickBooks**, giving users visibility into QB inventory data within Method's interface.

### Inventory Part Items
- Tracks quantity on hand, reorder points, quantities on sales orders and purchase orders
- Stores sales prices, purchase costs, preferred vendors, SKUs, manufacturer part numbers
- Syncs with QB for accounts (asset, income, COGS), vendors, and unit of measure
- Works with both QBO and QB Desktop

### Inventory Assembly Items (QB Desktop ONLY)
- Groups component items into finished products (basic BOM-like functionality)
- Tracks quantity on hand, quantity on sales orders, quantity on order
- Has a "build point" — minimum threshold that triggers assembly
- **Not available for QuickBooks Online users at all**

### Advanced Inventory Sync (QB Desktop ONLY)
- Syncs with QB Desktop's Advanced Inventory feature
- Supports site tracking, lot numbers, and serial numbers on Sales Orders and Invoices
- **Critical limitation:** Method does not track inventory per site location — it shows ALL site locations for any item
- Requires customization to implement on Method screens
- **Not available for QBO users**

## What Breaks When Migrating from QB Desktop to QBO

This is critical for MWD positioning because many target customers are on QB Desktop:

- **Sales Orders:** Not available in QBO (Method can't sync them)
- **Assemblies/BOMs:** No support in QBO
- **Item-level custom fields:** Unavailable in QBO
- **Price Levels:** Unsupported in QBO
- **Received Quantity and Is Fully Received fields:** Don't sync from QBO, making inventory tracking and PO workflows limited
- Overall: fewer synced tables, limited custom field syncing, weaker transaction detail

## How to Position Inventory in This Playbook

### What we CAN say:
- Method gives you visibility into your QuickBooks inventory data alongside your CRM, sales, and operational workflows
- For QB Desktop users: assembly items, advanced inventory (site tracking, lot numbers, serial numbers) sync into Method
- Method connects inventory data to your sales pipeline, quotes, and work orders — eliminating the "islands of information" problem
- Customization can extend inventory workflows (e.g., custom screens for warehouse operations, field crew inventory visibility)

### What we CANNOT say:
- Method has native inventory management (it doesn't — it syncs QB inventory)
- Method has multi-warehouse inventory management (the Jan 2026 launch referenced in the market landscape doc is the upcoming product — NOT launched yet)
- Method replaces dedicated inventory tools like Fishbowl, Cin7, or Katana
- Method handles BOM, kitting, lot tracking, or shop floor control natively
- Method offers committed vs. available stock tracking (that's the upcoming product)

### What we should say about the gap:
- For businesses with complex inventory needs (multi-warehouse, BOM, production planning), Method works alongside dedicated inventory tools as the CRM/operations layer
- Method's customization can bridge some inventory gaps — but deep manufacturing inventory is not Method's core strength today
- The QB sync means your inventory data is always accurate in Method without double entry — that's the real value

## How Customers Use Inventory in Method Today (Customization Examples)

Method's full customizability means customers have built inventory workflows that go well beyond the default QB sync. These real examples prove two viable approaches:

### Approach 1: Third-Party Integration (SOS Inventory via API)

**SLE Technologies** — Uses Method as CRM + SOS Inventory for stock management. Method connects to SOS via API so reps see real-time inventory data inside Method without leaving the CRM. The integration keeps customer data, sales pipeline, and inventory visibility in one place.

**Cypress Engine** — Similar setup. Method handles CRM and customer-facing operations; SOS Inventory handles the inventory side. The API integration means the sales team works entirely in Method while warehouse operations run in SOS.

**Takeaway for playbook:** Method doesn't need to BE the inventory system. It can connect to dedicated inventory tools and surface that data where sales and operations teams need it. This is a strong positioning angle — Method as the operations hub that ties inventory data to your CRM workflows.

### Approach 2: In-House Custom Builds Within Method

**Warehouse Inventory Tracking (custom build by Safwan)** — Built custom fields and screens inside Method to track inventory across multiple warehouse locations. Uses Method's customization engine to create warehouse-specific views and workflows without a third-party tool.

**Euroboor (custom build by Joseph)** — Advanced inventory customization including serial number tracking, bin location management, inventory allocation, and back order handling — all built within Method's customization framework. This is the most sophisticated in-house inventory build, showing that Method's platform can support detailed warehouse operations when customized.

**Takeaway for playbook:** For businesses that don't want to pay for a separate inventory tool, Method's customization can handle surprisingly complex inventory workflows. This is real proof that the platform's flexibility extends to inventory — not as an out-of-the-box feature, but as a buildable solution.

### Positioning Guidance from These Examples

When talking to MWD prospects about inventory:
- **Lead with the customization story:** "Method customers have built everything from basic warehouse tracking to full serial number and bin location management inside Method"
- **Offer both paths:** "You can integrate your existing inventory tool via API, or we can build custom inventory workflows directly in Method"
- **Be honest about trade-offs:** Custom builds require implementation effort; third-party integrations require a separate subscription. Neither is plug-and-play inventory management
- **Use these as proof points:** Named customer examples (with permission) demonstrate that Method handles real inventory workflows in production environments

---

## Items to Correct in Existing Deliverables

The Section 1 Market Landscape doc (01-mwd-market-landscape.md) contains multiple references to "Native multi-warehouse inventory management (Jan 2026 launch)" that need to be corrected. These references should be updated to reflect current capabilities only.

Specific sections to revise:
- "Inventory visibility across locations" pain theme — reframe around QB sync capabilities, not native inventory
- Competitive comparison table — remove "Yes (native, Jan 2026)" for inventory and replace with accurate positioning
- "Honest Gaps" section — expand to be more transparent about inventory limitations
- Pricing analysis tables — update inventory column
- Strategic implications point #4 — rewrite to reflect current state
