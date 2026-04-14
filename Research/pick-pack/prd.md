# Pick & Pack PRD

| Field | Value |
|-------|-------|
| **Status** | Draft |
| **Author** | Barbara + Inventory Research Agent |
| **Date** | 2026-03-28 |
| **Epic** | — |
| **Confluence** | — |

---

> **Problem Statement**
>
> Customers cannot reliably track what has been picked, packed, and made ready to ship within Method. Without a structured pick and pack flow, warehouse teams rely on memory, sticky notes, and spreadsheets to manage fulfillment — leading to mis-ships, lost orders, and no audit trail of who pulled what.

---

## Problem Space

### Background & Rationale

Now that Method supports sales orders, shipping, and invoicing, customers need a structured way to manage the steps *before* shipping — pulling items from shelves (picking) and preparing them for dispatch (packing). In real-world distribution operations, the sequence is always: pick → pack → ship. Method currently skips straight from sales order to ship, leaving the picking and packing steps completely untracked.

Without a native pick and pack flow:

- Warehouse staff have no printed pick list telling them what to pull, from which location, and in what quantity
- There is no way to track whether an order has been picked, packed, or is still waiting — the team has to open each SO individually
- Partial picks (not all items in stock) have no structured handling — staff either ship what they have or wait with no system visibility
- Packing slips must be created manually outside Method, or customers repurpose the sales order printout (which includes pricing they may not want the end customer to see)
- Fulfillment bottlenecks are invisible — a manager cannot answer "how many orders are waiting to be picked?" without checking every SO

A proper pick and pack function standardizes the fulfillment workflow between order creation and shipping, gives warehouse teams a clear checklist, and provides the operational visibility required for multi-person fulfillment operations. Pick and pack is a core, table-stake capability of any inventory system that supports order fulfillment.

### How do we know this is a real problem & worth solving?

Order & Fulfillment Tracking is a top JTBD across 83 companies (17.8% of all transcripts), and Order Management is the #1 pain point (244 companies, 53.5%). Any business shipping physical goods needs to track what has been picked and packed before it ships — and they expect their inventory system to support that natively.

A real example illustrates this clearly:

> **Phil Helms — Bluewatercas**
>
> **Pain Point:**
>
> Phil needs a document that travels with the shipment — a delivery ticket or packing slip. His team currently repurposes the sales order printout, but it includes pricing that the end customer should not see. He explicitly asked: *"We need, like, a delivery ticket. Our thought was we could use the sales order, but if we could toggle on and off the price list of it, where the customer does not see it and we can print it out."*
>
> **Solution:**
>
> The Pick & Pack wizard generates a packing slip with a price toggle (show/hide prices), giving Phil's team a customer-facing document that goes in the box — without exposing pricing. The pick list gives the warehouse a printed checklist of what to pull from which location.

> **Kano Model Analysis**
>
> Pick & Pack was not included as a standalone item in the February 2026 Kano survey, but it is a direct sub-component of Order & Fulfillment Tracking — which scored as a top JTBD. The competitive landscape confirms this is table-stakes: every competitor surveyed (Fishbowl, Katana, Cin7, SOS Inventory, Zoho, inFlow) includes some form of pick list generation and packing slip creation. The absence of this capability is a gap that competitors exploit.
>
> **Verdict:** Fulfillment tracking is validated as a P1 need. Pick & Pack is the operational mechanism that delivers it.

---

### Who are we building for?

We are building for small (1–100 employee) B2B distribution and manufacturing companies that ship physical goods from one or more warehouse locations. These are operational SMBs where the same person may create the sales order, pick items from shelves, pack the box, and hand it to a carrier — or where a small team divides these tasks across 2–3 people.

---

### Goals

1. **Enable Structured Fulfillment Before Shipping**: Give warehouse teams a clear pick → pack → ship workflow with printed pick lists and packing slips, eliminating reliance on memory and manual documents.
2. **Provide Fulfillment Visibility Across Orders**: Add a Fulfillment Status column to the Sales Order list screen so managers can instantly see which orders need picking, which are packed, and which are ready to ship.
3. **Reduce Churn & Improve Competitive Positioning**: Close the pick/pack gap that every major competitor already fills, increasing Method's value proposition as a viable all-in-one solution for MWD customers.

---

### Solution Space

Deliver a native Pick & Pack wizard within Method that integrates before the existing Ship flow:

1. A 2-step modal wizard (Pick → Pack) launched from a new "Pick & Pack" button on the Sales Order action bar
2. Persistent PickList records that enable save & resume, reprinting, and audit
3. A Fulfillment Status column on the Sales Order list screen (Not Started → Pick in Progress → Picked → Packed → Shipped)
4. A Pick List section on the SO detail screen between "Items not shipped" and "Items shipped"
5. Packing slip generation with a price toggle (show/hide prices)

**Important:** Pick & Pack does not reduce inventory. Inventory is only reduced at Ship time, consistent with the existing shipping flow (FR-300). Pick & Pack tracks the fulfillment *process* — picking and packing are operational steps, not inventory transactions.

---

### Success Metrics

| Category | Metric | Rationale |
|----------|--------|-----------|
| **Adoption (Habit Formation)** | 20% of W&D accounts completing ≥3 pick & pack flows (reaching "Packed" status) within 30 days of first use | Measures true adoption and repeated value among the ICP by focusing on completed pack flows — the point at which the user has verified items and generated a packing slip. |
| **Workflow Health** | 60% of pick lists created that progress to "Packed" or "Shipped" within 48 hours of creation | Measures whether the pick & pack workflow completes successfully — ensuring pick lists don't stall as abandoned drafts. |
| **Bypass Rate** | <40% of shipments skip pick & pack entirely (using Ship All directly) after 60 days | Measures whether users adopt the structured flow vs. bypassing it. Some bypass is expected for simple orders, but if most users skip pick & pack, the feature isn't delivering value. |

---

## Functional Requirements

Below are the functional requirements (in-scope) that describe how the experience must look like from a user's perspective.

---

### FR 1: Pick & Pack Button & Wizard Entry

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-100 | DRAFT | Link | As a user, I want to start the pick and pack process directly from a Sales Order, so that I can begin fulfilling the order without leaving the SO screen. | 1. **Pick & Pack button appears on SO action bar** | None |
| | | | | • **Given** I am on a Sales Order detail screen with Status = "Open" or "Partially Shipped" | |
| | | | | • **And** the order has one or more unfulfilled line items in the "Items not shipped" table | |
| | | | | • **When** the screen loads | |
| | | | | • **Then** I see a "Pick & Pack" button in the action bar between "Send" and "Ship" | |
| | | | | • **And** the button is a single action (no dropdown) | |
| | | | | 2. **Pick & Pack button opens wizard modal** | |
| | | | | • **Given** I am on a Sales Order with unfulfilled line items | |
| | | | | • **When** I click the "Pick & Pack" button | |
| | | | | • **Then** a modal opens (870px width, matching existing modal patterns) | |
| | | | | • **And** the modal header shows "Pick & Pack — [SO Number]" and the customer name | |
| | | | | • **And** a 2-step indicator shows: ● Pick ○ Pack | |
| | | | | • **And** Step 1 (Pick) is displayed | |
| | | | | 3. **Pick & Pack button is hidden when no items to pick** | |
| | | | | • **Given** I am on a Sales Order where all line items have been picked or shipped | |
| | | | | • **When** the screen loads | |
| | | | | • **Then** the "Pick & Pack" button is not visible in the action bar | |
| | | | | 4. **Existing Ship button remains unchanged** | |
| | | | | • **Given** I am on a Sales Order detail screen | |
| | | | | • **When** the screen loads | |
| | | | | • **Then** the Ship ∨ dropdown ("Ship Some..." / "Ship All") remains in the action bar in its current position | |
| | | | | • **And** the Ship flow continues to work as it does today (FR-300) | |

---

### FR 2: Wizard Step 1 — Pick (Select Items)

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-200 | DRAFT | Link | As a user, I want to select which items to pick from the sales order and see their availability at each location, so that I can create an accurate pick list for the warehouse. | 1. **Step 1 displays all unfulfilled line items** | US-100 |
| | | | | • **Given** the Pick & Pack wizard is open on Step 1 (Pick) | |
| | | | | • **When** the step loads | |
| | | | | • **Then** I see a table with columns: Checkbox, Item, Location, Available Qty, Qty to Pick | |
| | | | | • **And** every unfulfilled line item from the "Items not shipped" table is listed | |
| | | | | • **And** each row shows the item's source location from the sales order | |
| | | | | • **And** a "Select All" / "Deselect All" checkbox is available above the table | |
| | | | | 2. **Available Qty shows current stock at the source location** | |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **When** the table displays | |
| | | | | • **Then** each row shows the Available Qty at the item's source location | |
| | | | | • **And** the Available Qty updates in real-time if Qty to Pick is adjusted | |
| | | | | 3. **Qty to Pick is editable for partial picking** | |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **And** a line item has Qty to Pick defaulting to the full order quantity | |
| | | | | • **When** I change the Qty to Pick to a lower number | |
| | | | | • **Then** the system accepts the value as long as it is greater than 0 and does not exceed the order line quantity | |
| | | | | • **And** the availability indicator recalculates based on the new Qty to Pick | |
| | | | | 4. **Qty to Pick validation** | |
| | | | | • **Given** I am editing Qty to Pick for a line item | |
| | | | | • **When** I enter a value that is 0, negative, non-numeric, or greater than the order line quantity | |
| | | | | • **Then** an inline validation message appears on that row | |
| | | | | • **And** the "Next" and "Save Pick List" buttons are disabled until the error is resolved | |
| US-201 | DRAFT | Link | As a user, I want to print a pick list from the wizard so that I can hand a physical checklist to warehouse staff before confirming the pick. | 1. **Print Pick List button generates a PDF** | US-200 |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **And** one or more items are checked | |
| | | | | • **When** I click "Print Pick List" | |
| | | | | • **Then** a PDF is generated containing: SO number, customer name, ship-to address, print date, and a table of checked items with Item, SKU, Location, Qty to Pick, and a blank "Picked ☐" checkbox column | |
| | | | | • **And** items are grouped by location for efficient warehouse walking | |
| | | | | • **And** out-of-stock items (Available Qty = 0) are excluded from the printed list | |
| | | | | • **And** the PDF includes a "Picked by" signature line and date/time fields at the bottom | |
| | | | | 2. **Print Pick List requires at least one checked item** | |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **And** no items are checked | |
| | | | | • **When** I look at the "Print Pick List" button | |
| | | | | • **Then** the button is disabled | |
| US-202 | DRAFT | Link | As a user, I want three clear exit paths from Step 1 so that I can either continue to packing, save my progress for later, or cancel entirely. | 1. **"Next →" advances to Step 2** | US-200 |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **And** one or more items are checked with valid Qty to Pick values | |
| | | | | • **When** I click "Next →" | |
| | | | | • **Then** the wizard advances to Step 2 (Pack) | |
| | | | | • **And** the step indicator updates to: ● Pick ● Pack | |
| | | | | • **And** only the checked items carry forward to Step 2 | |
| | | | | 2. **"Save Pick List" saves progress and closes wizard** | |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **And** one or more items are checked with valid Qty to Pick values | |
| | | | | • **When** I click "Save Pick List" | |
| | | | | • **Then** a PickList record is created with the selected items and quantities | |
| | | | | • **And** the wizard closes | |
| | | | | • **And** the FulfillmentStatus updates to "Pick in Progress" | |
| | | | | • **And** a Pick List section appears on the SO detail screen | |
| | | | | • **And** a success message appears: "Pick list saved" | |
| | | | | 3. **"Cancel" discards and closes wizard** | |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **When** I click "Cancel" or the ✕ close button | |
| | | | | • **Then** the wizard closes | |
| | | | | • **And** no PickList record is created | |
| | | | | • **And** no status changes occur | |
| | | | | • **And** the SO returns to its previous state | |
| | | | | 4. **"Next →" and "Save Pick List" require at least one checked item** | |
| | | | | • **Given** I am on Step 1 of the wizard | |
| | | | | • **And** no items are checked | |
| | | | | • **Then** the "Next →" and "Save Pick List" buttons are disabled | |

---

### FR 3: Wizard Step 2 — Pack (Confirm & Packing Slip Options)

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-300 | DRAFT | Link | As a user, I want to review the items I picked and configure packing slip options, so that I can confirm the pack and generate a document for the shipment box. | 1. **Step 2 displays picked items as a read-only summary** | US-202 |
| | | | | • **Given** I advanced to Step 2 from Step 1 | |
| | | | | • **When** the step loads | |
| | | | | • **Then** I see a read-only table of items carried from Step 1: Item, Location, Qty | |
| | | | | • **And** the quantities and items cannot be edited on this step | |
| | | | | • **And** the step indicator shows: ● Pick ● Pack | |
| | | | | 2. **Packing slip toggles are available** | |
| | | | | • **Given** I am on Step 2 of the wizard | |
| | | | | • **When** the step loads | |
| | | | | • **Then** I see a "Generate packing slip" toggle (on by default) | |
| | | | | • **And** I see a "Show prices on packing slip" toggle (off by default) | |
| | | | | • **And** I see an optional "Packing notes" text field | |
| | | | | 3. **"Confirm Pack" saves pack and generates packing slip** | |
| | | | | • **Given** I am on Step 2 of the wizard | |
| | | | | • **And** "Generate packing slip" is toggled on | |
| | | | | • **When** I click "Confirm Pack" | |
| | | | | • **Then** the items are marked as packed on the PickList record | |
| | | | | • **And** a packing slip PDF is generated (see FR 7) | |
| | | | | • **And** the wizard closes | |
| | | | | • **And** the FulfillmentStatus updates to "Packed" | |
| | | | | • **And** a success message appears: "Items packed" | |
| | | | | 4. **"Confirm Pack" without packing slip** | |
| | | | | • **Given** I am on Step 2 of the wizard | |
| | | | | • **And** "Generate packing slip" is toggled off | |
| | | | | • **When** I click "Confirm Pack" | |
| | | | | • **Then** the items are marked as packed | |
| | | | | • **And** no packing slip is generated | |
| | | | | • **And** the wizard closes and FulfillmentStatus updates to "Packed" | |
| | | | | 5. **"← Back" returns to Step 1** | |
| | | | | • **Given** I am on Step 2 of the wizard | |
| | | | | • **When** I click "← Back" | |
| | | | | • **Then** I return to Step 1 with all previously checked items and quantities preserved | |

---

### FR 4: Fulfillment Status on Sales Order List Screen

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-400 | DRAFT | Link | As a user, I want to see the fulfillment status of every sales order on the list screen, so that I can quickly identify which orders need picking, packing, or shipping without opening each one. | 1. **Fulfillment Status column appears on SO list screen** | None |
| | | | | • **Given** I am on the Sales Orders list screen | |
| | | | | • **When** the list loads | |
| | | | | • **Then** I see a "Fulfillment" column alongside the existing Order Status and Invoice Status columns | |
| | | | | • **And** every sales order row displays a Fulfillment Status value | |
| | | | | 2. **Fulfillment Status values and progression** | |
| | | | | • **Given** a sales order exists in the system | |
| | | | | • **Then** the Fulfillment Status is one of: "Not Started", "Pick in Progress", "Picked", "Packed", "Shipped" | |
| | | | | • **And** "Not Started" is the default for new or untouched orders | |
| | | | | • **And** statuses progress sequentially — each status implies all previous steps are complete | |
| | | | | 3. **Fulfillment Status updates automatically based on actions** | |
| | | | | • **Given** a user performs a fulfillment action on a sales order | |
| | | | | • **When** the user saves a pick list → **Then** status = "Pick in Progress" | |
| | | | | • **When** all items on the pick list are marked as picked → **Then** status = "Picked" | |
| | | | | • **When** the user confirms pack in the wizard or via the Pack button → **Then** status = "Packed" | |
| | | | | • **When** all items are shipped via the Ship flow → **Then** status = "Shipped" | |
| | | | | 4. **Partial fulfillment shows the earliest incomplete stage** | |
| | | | | • **Given** a sales order has multiple line items at different fulfillment stages | |
| | | | | • **Then** the Fulfillment Status reflects the earliest incomplete stage (e.g., if some items are packed but others are still being picked, status = "Pick in Progress") | |
| | | | | 5. **Filter by Fulfillment Status** | |
| | | | | • **Given** I am on the Sales Orders list screen | |
| | | | | • **When** I select a status from the Fulfillment Status filter | |
| | | | | • **Then** the table displays only sales orders matching the selected status | |
| | | | | • **And** the available filter options are: All Statuses (default), Not Started, Pick in Progress, Picked, Packed, Shipped | |

---

### FR 5: Pick List Section on SO Detail Screen

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-500 | DRAFT | Link | As a user, I want to see the pick list status directly on the Sales Order detail screen, so that I can track which items have been picked and packed without reopening the wizard. | 1. **Pick List section appears after a pick list is created** | US-202 |
| | | | | • **Given** a PickList record exists for this sales order | |
| | | | | • **When** I view the SO detail screen | |
| | | | | • **Then** a "Pick List" section appears between "Items not shipped" and "Items shipped" | |
| | | | | • **And** the section shows a table with columns: Item, Location, Qty to Pick, Qty Picked, Status | |
| | | | | • **And** each row's Status is one of: "Pending", "Picked", "Packed" | |
| | | | | 2. **Qty Picked is editable inline for pending items** | |
| | | | | • **Given** a pick list item has Status = "Pending" | |
| | | | | • **When** I click on the Qty Picked field | |
| | | | | • **Then** I can edit the value inline | |
| | | | | • **And** the value must be between 0 and Qty to Pick | |
| | | | | • **And** when Qty Picked = Qty to Pick, the row's Status changes to "Picked" | |
| | | | | 3. **Pick List section shows action buttons** | |
| | | | | • **Given** a pick list exists with picked items that are not yet packed | |
| | | | | • **Then** a [Pack ▸] button appears on the Pick List section header | |
| | | | | • **And** a [Unpick ▸] button appears on the Pick List section header | |
| | | | | • **And** a "Print Pick List" icon is available | |
| | | | | 4. **Pick List section is hidden when no pick list exists** | |
| | | | | • **Given** no PickList record exists for this sales order | |
| | | | | • **When** I view the SO detail screen | |
| | | | | • **Then** the Pick List section is not visible | |
| US-501 | DRAFT | Link | As a user, I want to reprint the pick list from the SO detail screen, so that I can give warehouse staff a fresh copy without reopening the wizard. | 1. **Print Pick List from section header** | US-500 |
| | | | | • **Given** a Pick List section is visible on the SO detail screen | |
| | | | | • **When** I click the print icon on the Pick List section | |
| | | | | • **Then** a PDF pick list is generated with the current pick list items and quantities | |
| | | | | • **And** the PDF uses the same format as the wizard's print output (see US-201) | |

---

### FR 6: Save & Resume Flow

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-600 | DRAFT | Link | As a user, I want to save a pick list and resume packing later, so that the warehouse can pick items at one time and pack them at another without losing progress. | 1. **Resuming pack from the Pick List section** | US-500 |
| | | | | • **Given** a pick list was saved from Step 1 of the wizard (via "Save Pick List") | |
| | | | | • **And** items on the pick list have been marked as picked (Qty Picked = Qty to Pick) | |
| | | | | • **When** I click [Pack ▸] on the Pick List section header | |
| | | | | • **Then** a Pack modal opens pre-populated with all picked items | |
| | | | | • **And** the modal shows the same layout as Step 2 of the wizard: read-only item summary, packing slip toggles, packing notes field | |
| | | | | • **And** I can confirm pack to advance items to "Packed" status | |
| | | | | 2. **Pack button requires at least one picked item** | |
| | | | | • **Given** a pick list exists but no items have been marked as picked yet (all Qty Picked = 0) | |
| | | | | • **When** I view the Pick List section | |
| | | | | • **Then** the [Pack ▸] button is disabled | |
| US-601 | DRAFT | Link | As a user, I want to reopen the Pick & Pack wizard to add more items to an existing pick list, so that I can handle new line items or items that were out of stock earlier. | 1. **Wizard opens with existing pick list context** | US-500 |
| | | | | • **Given** a pick list already exists for this sales order | |
| | | | | • **And** there are additional unfulfilled line items in "Items not shipped" that are not on the current pick list | |
| | | | | • **When** I click the "Pick & Pack" button in the action bar | |
| | | | | • **Then** the wizard opens on Step 1 showing only the items NOT already on the pick list | |
| | | | | • **And** a note at the top states: "Items already on the pick list are not shown. View existing pick list on the SO screen." | |
| | | | | 2. **Pick & Pack button is hidden when all items are already on the pick list** | |
| | | | | • **Given** a pick list exists that includes all unfulfilled line items | |
| | | | | • **When** I view the SO detail screen | |
| | | | | • **Then** the "Pick & Pack" button is not visible in the action bar | |

---

### FR 7: Packing Slip Document

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-700 | DRAFT | Link | As a user, I want the packing slip to include shipment details with an option to show or hide prices, so that I can use it as a customer-facing document in the box or as an internal delivery ticket. | 1. **Packing slip content** | US-300 |
| | | | | • **Given** a packing slip is generated (via Confirm Pack with "Generate packing slip" toggled on) | |
| | | | | • **Then** the PDF includes: company name/logo, ship-from address, ship-to address (from SO), SO number, pack date, and a table of packed items with Item, SKU, and Qty Packed | |
| | | | | • **And** if packing notes were entered, they appear at the bottom of the slip | |
| | | | | 2. **Price toggle controls price visibility** | |
| | | | | • **Given** "Show prices on packing slip" is toggled ON | |
| | | | | • **Then** the packing slip includes Price and Amount columns per item, and Subtotal, Tax, and Total at the bottom | |
| | | | | • **Given** "Show prices on packing slip" is toggled OFF (default) | |
| | | | | • **Then** the packing slip does NOT include Price, Amount, Subtotal, Tax, or Total | |
| | | | | 3. **Packing slip is accessible after generation** | |
| | | | | • **Given** a packing slip was generated for this sales order | |
| | | | | • **When** I view the Pick List section on the SO detail screen | |
| | | | | • **Then** a document icon is available that allows me to view or reprint the packing slip | |

---

### FR 8: Undo Flows (Unpick & Unpack)

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-800 | DRAFT | Link | As a user, I want to unpick items from the pick list and move them back to "Items not shipped", so that I can correct picking errors or cancel fulfillment for specific items before shipping. | 1. **Unpick opens a selection modal** | US-500 |
| | | | | • **Given** a Pick List section exists with one or more items that have been picked or are pending | |
| | | | | • **When** I click [Unpick ▸] on the Pick List section header | |
| | | | | • **Then** a modal opens (870px, matching existing modal patterns) showing a checkbox table of all items on the pick list: Checkbox, Item, Location, Qty Picked | |
| | | | | • **And** I can select which items to return to "Items not shipped" | |
| | | | | 2. **Confirming unpick moves items back** | |
| | | | | • **Given** I have selected one or more items in the Unpick modal | |
| | | | | • **When** I click "Confirm Unpick" | |
| | | | | • **Then** the selected items are removed from the Pick List | |
| | | | | • **And** the selected items reappear in the "Items not shipped" table with their original quantities | |
| | | | | • **And** the FulfillmentStatus recalculates: if no items remain on the pick list → "Not Started"; if some items remain → "Pick in Progress" | |
| | | | | • **And** a success message appears: "Items returned to unfulfilled" | |
| | | | | 3. **Unpick all items removes the Pick List section** | |
| | | | | • **Given** I unpick all items from the pick list | |
| | | | | • **Then** the PickList record is removed | |
| | | | | • **And** the Pick List section disappears from the SO detail screen | |
| | | | | • **And** the FulfillmentStatus returns to "Not Started" | |
| US-801 | DRAFT | Link | As a user, I want to unpack items that were marked as packed but not yet shipped, so that I can revert them to "Picked" status if the pack was premature or incorrect. | 1. **Unpack option is available for packed items** | US-300 |
| | | | | • **Given** the Pick List section has items with Status = "Packed" | |
| | | | | • **And** those items have not yet been shipped | |
| | | | | • **Then** an [Unpack] action is available on the Pick List section | |
| | | | | 2. **Confirming unpack reverts items to Picked status** | |
| | | | | • **Given** I initiate an Unpack action | |
| | | | | • **When** I confirm the unpack | |
| | | | | • **Then** the selected items' status reverts from "Packed" to "Picked" | |
| | | | | • **And** any packing slip generated for those items is invalidated | |
| | | | | • **And** the FulfillmentStatus recalculates (e.g., "Packed" → "Picked") | |
| US-802 | DRAFT | Link | As a user, I want the existing Undo Shipment flow (FR-308) to work correctly with picked and packed items, so that undoing a shipment returns items to the appropriate fulfillment stage. | 1. **Undo shipment returns items to "Items not shipped"** | US-500 |
| | | | | • **Given** items were picked, packed, and then shipped | |
| | | | | • **When** I click [Undo] on the Items Shipped table (existing FR-308 behavior) | |
| | | | | • **Then** the shipped items are moved back to the "Items not shipped" table | |
| | | | | • **And** those items are removed from the Pick List (they are no longer picked or packed) | |
| | | | | • **And** the FulfillmentStatus recalculates based on remaining pick list items | |

---

### FR 9: Ship Integration for Packed Items

| FR ID | Status | Design | User Story | Acceptance Criteria | Dependencies |
|-------|--------|--------|------------|---------------------|--------------|
| US-900 | DRAFT | Link | As a user, I want the Ship flow to show me which items are packed and ready to ship, so that I only ship items that have been through pick and pack. | 1. **Ship modal shows packed items** | US-300 |
| | | | | • **Given** items have been packed (FulfillmentStatus = "Packed" or some items are packed) | |
| | | | | • **When** I click Ship ∨ → "Ship Some..." | |
| | | | | • **Then** the Ship modal displays packed items with a "Ready to Ship" indicator | |
| | | | | • **And** items still in "Items not shipped" (not picked/packed) are also shown but without the indicator | |
| | | | | 2. **"Ship All" ships all packed items** | |
| | | | | • **Given** one or more items are packed | |
| | | | | • **When** I click Ship ∨ → "Ship All" | |
| | | | | • **Then** all packed items are shipped using the existing shipping flow (FR-300) | |
| | | | | • **And** those items move from the Pick List section to the "Items shipped" table | |
| | | | | • **And** the FulfillmentStatus updates to "Shipped" (if all items are now shipped) or recalculates based on remaining items | |
| | | | | 3. **Shipping without pick & pack still works (bypass path)** | |
| | | | | • **Given** a sales order with items in "Items not shipped" that have NOT been picked or packed | |
| | | | | • **When** I click Ship ∨ → "Ship All" or "Ship Some..." | |
| | | | | • **Then** the existing Ship flow works as it does today (FR-300) | |
| | | | | • **And** the FulfillmentStatus jumps directly to "Shipped" for those items | |
| | | | | • **And** no pick list is created — the user has chosen to bypass pick & pack | |

---

## Non-Functional Requirements

| Requirement | Description |
|-------------|-------------|
| **Performance** | The Pick & Pack wizard modal must open within 1 second of clicking the button. Pick list PDF generation must complete within 3 seconds. |
| **Packing Slip Print Quality** | Packing slips must render cleanly on standard letter (8.5"×11") paper with proper margins, and be suitable for inclusion in a shipping box. |
| **Consistency** | All modals (Pick & Pack wizard, Unpick, Pack) must use the same 870px width and visual patterns as the existing SelectShippedItemsModal and InvoiceCreation modals. |
| **Data Integrity** | PickList records must persist across browser refreshes and sessions. A user who saves a pick list and returns hours later must see the same pick list state. |
| **Backward Compatibility** | The existing Ship flow (FR-300) and Undo Shipment (FR-308) must continue to work exactly as they do today. Pick & Pack adds to the fulfillment sequence — it does not alter existing shipping behavior. |
| **Accessibility** | All wizard steps, modals, and toggles must be keyboard-navigable and screen-reader compatible. |
