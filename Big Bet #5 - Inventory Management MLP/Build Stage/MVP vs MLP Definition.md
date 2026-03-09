# MVP vs MLP Definition: Inventory Management System

**Purpose:** Establish a shared definition of MVP and MLP for Method's Inventory initiative to guide roadmap and prioritization discussions.

---

## 1. The Customer Problem We Are Solving

Today, Method customers lack clear visibility and control over their inventory. This manifests as:

- Inability to confidently know what inventory exists and where
- Manual workarounds to track stock movements
- Overselling or underselling due to inaccurate availability
- Heavy reliance on customizations or IMS to compensate for missing primitives

This creates friction, erodes trust in data, causes churn and limits customers' ability to scale their operations.

---

## 2. Definitions Used for This Discussion

### MVP (Minimum Viable Product)

The smallest set of capabilities that meaningfully solves the core problem and enables customers to run real, end-to-end workflows.

**Focus:** Foundational visibility and control

### MLP (Minimum Lovable Product)

Make our customers fall in love with our product by adding a new layer of functionality that increases trust, efficiency, and retention, making inventory feel complete, scalable, and reliable for growing businesses. 

**Focus:** Operational maturity and confidence 

---

## 3. Inventory MVP — What We Are Shipping to GA

The following capabilities together establish the core native inventory foundation:

- Multi-Location Management
- Item ↔ Location Linking
- Stock Adjustments
- Available / Committed / Expected Stock Tracking
- S0 & PO Fulfillment flows 

---

## 4. MVP vs MLP Evaluation of Key Roadmap Features

### Stock Transfers — MVP

**Why:**
Once multi-location inventory exists, customers must be able to move stock between locations in a structured, auditable way.

**Without it:**
- Inventory becomes fragmented across locations
- Customers fall back to manual adjustments or external tracking
- "Control" breaks down immediately

**Conclusion:**
Stock transfers are a required primitive to make multi-location inventory viable.

✅ **Classified as MVP**

---

### Reorder Points & Low Stock Alerts — MLP

**Why not MVP:**
Customers can already see low stock using available/committed views. Alerts add proactive optimization, not baseline visibility.

**Why MLP:**
- Reduces manual monitoring
- Encourages habitual inventory engagement
- Builds confidence and operational efficiency

**Conclusion:**
Important for scale, but not required to establish initial control.

🟡 **Classified as MLP**

---

### Backorders — MLP 

**Why not MVP:**
- Introduces meaningful complexity across fulfillment workflows
- Requires nuanced handling of expectations, allocations, and partial fulfillment
- Not universally required by all SMBs on day one

**Why MLP:**
- Critical for growing distributors
- Builds trust in sales workflows ("Can I sell what I don't have yet?")
- Naturally extends expected stock tracking

**Conclusion:**
Essential for maturity, but not foundational for initial inventory trust.

🟡 **Classified as MLP**

---

### Bin Management — MLP

**Why not MVP:**
- Location-level inventory solves the majority of visibility needs
- Bin-level tracking optimizes warehouse execution rather than data clarity
- Not required for target ICP

**Why MLP:**
- Valuable for high-SKU or warehouse-heavy customers
- Improves pick/pack accuracy
- Signals inventory product maturity

**Conclusion:**
Operational optimization after trust is established.

🟡 **Classified as MLP**

---

### Katana x Method Integration — MLP

**Why not MVP:**
- Native inventory features must solve the core problem independently
- Integration requires a stable MVP foundation to build upon
- Not all customers need advanced manufacturing inventory capabilities on day one

**Why MLP:**
- Validates our Hybrid Approach strategy (native basics + integration scalability)
- Proves customers can graduate from native to advanced systems as they grow
- Demonstrates competitive positioning: 90% of CRMs use this model
- Addresses MWD segment needs beyond basic multi-warehouse management

**Conclusion:**
Core to our strategic positioning, but not required for native MVP to solve visibility and control. Integration validates that customers have a growth path beyond native features.

🟡 **Classified as MLP**

---

### Dynamic Item Management in Transactions — MLP

**Why not MVP:**
- Customers can already add, edit, and manage line items in transactions
- Drag-and-drop is a UX enhancement, not a functional capability gap
- Core inventory workflows (fulfillment, stock tracking) don't depend on line item rearrangement

**Why MLP:**
- Reduces friction in high-volume transaction entry
- Improves efficiency for users managing complex orders
- Signals product polish and operational maturity

**Conclusion:**
Operational efficiency improvement, not foundational to solving visibility and control.

🟡 **Classified as MLP**

---

### Item Visualization — MLP

**Why not MVP:**
- Inventory tracking and control work without product images
- Item identification can be achieved through SKUs, descriptions, and naming conventions
- Not universally required across all verticals (more valuable for retail/e-commerce)

**Why MLP:**
- Reduces errors in order picking and fulfillment
- Improves user confidence in item selection
- Enhances customer-facing workflows (quotes, invoices)
- Signals feature completeness compared to competitors

**Conclusion:**
Valuable for operational accuracy and customer experience, but not required to establish inventory trust.

🟡 **Classified as MLP**

---

### Item Audit Trail — MLP

**Why not MVP:**
- Customers can manage day-to-day inventory operations without detailed transaction history
- Stock Adjustments already provide basic tracking of manual changes
- Not required to know current inventory levels or move stock between locations

**Why MLP:**
- Builds trust through transparency and accountability
- Critical for troubleshooting discrepancies ("Why did this change?")
- Required for compliance in regulated industries
- Supports operational maturity and debugging

**Conclusion:**
Important for trust and troubleshooting, but not foundational to solving visibility and control problem.

🟡 **Classified as MLP**

---

## 5. Conclusion

### MVP Solves the Core Problem End-to-End

Our MVP (Multi-Location Management, Item ↔ Location Linking, Stock Adjustments, Available/Committed/Expected Tracking, SO & PO Fulfillment, **plus Stock Transfers**) delivers a complete inventory workflow:

- Customers know what inventory exists and where
- Customers can move stock between locations in a structured way
- Inventory data updates consistently across sales and purchasing workflows
- Method becomes a credible source of truth for inventory operations

**Stock Transfers is the only evaluated feature that must be included in MVP.** Without it, multi-location inventory becomes unmanageable and forces customers back to manual workarounds—defeating the entire purpose.

### MLP Builds Operational Maturity and Strategic Validation

The MLP layer transforms inventory from "functional" to "lovable" by adding:

**Proactive Features:**
- Reorder Points & Low Stock Alerts
- Backorder Awareness

**Efficiency & Trust Features:**
- Dynamic Item Management
- Item Visualization
- Item Audit Trail
- Bin Management

**Strategic Positioning:**
- Katana x Method Integration (validates Hybrid Approach)

These features increase trust, reduce manual effort, and prove that customers can scale beyond native capabilities as their business grows.

### Strategic Implications

**For MVP:**
Focus on shipping a complete, reliable foundation. Stock Transfers is non-negotiable—it's the difference between inventory that works and inventory that creates more problems.

**For MLP:**
Prioritize based on vertical needs and strategic validation:
- Katana Integration proves our Hybrid strategy works
- Reorder Points and Backorders address operational maturity for MWD customers
- Visualization and Audit Trail signal product completeness

**Success Criteria:**
- **MVP Success:** Can customers with 2-5 warehouses manage inventory end-to-end without customizations or workarounds?
- **MLP Success:** Do customers choose Method's inventory over manual tracking or third-party systems? Does churn decrease in target verticals?

This framework ensures we're solving the right problem at each stage—establishing trust first, then building love.
