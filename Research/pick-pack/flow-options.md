# Pick/Pack Flow Analysis & Options — Method CRM
## Date: March 23, 2026
## Mode: 2 — Flow Analysis & Options
## Feature: Pick List Generation + Packing Slip + Pack Confirmation
## Author: Barbara + Inventory Research Agent

**Interactive visual version with rendered diagrams + wireframes:** [View Flow Diagrams](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html)

---

## Pre-Design Context

### Current Prototype State (from PROJECT_CONTEXT.md)

The Method prototype at localhost:5200 already has:

- **Sales Order CRUD** — list screen, detail/form screen with 3-column grid layout
- **Shipping Flow (FR-300)** — "Ship some" / "Ship all" dropdown → Select Items modal → Confirm modal → creates ShippedItem records, updates order status (Open → Partially Shipped → Fully Shipped)
- **Undo Shipping (FR-308)** — undo button on shipped items table, moves qty back to line items
- **Invoice Creation Flow (FR-400–402)** — Create Invoice button + modal + navigation to dedicated InvoiceScreen, auto-updating invoice status (Not Invoiced → Partially Invoiced → Fully Invoiced)



**Key architectural fact:** Shipping already exists as a first-class flow. Pick/Pack must integrate *before* shipping in the fulfillment sequence without breaking the existing Ship → Invoice chain.

### What the Core User Job Is


**The job:** "When I have a sales order ready to fulfill, I need to tell my warehouse team what to pull from the shelves, confirm it's been pulled, pack it, and generate a document that goes in the box — without switching tools or re-entering data."

### MVP Design Constraints (from Competitor Research)

| Constraint | Decision |
|-----------|----------|
| Tracking level | SKU/quantity only — no serial numbers |
| QB sync | Inventory transactions do NOT sync to QB |
| Input method | Manual entry first — no barcode scanning this quarter |
| Automation | All manual confirmation — no auto-complete |
| Platform | Desktop-first, mobile-responsive |
| Location model | Multi-location (first level only) — no bins/aisles/lots |
| Carton tracking | Optional, not core |
| Backorders | Deferred — not in current MVP |
| Packing slip | Print option at ship time (not a workflow gate) |

### Key Design Decisions for Pick/Pack

Based on the competitor synthesis, there are five fundamental design decisions that differentiate the flow options:

1. **Is picking a separate step or embedded in shipping?** — Fishbowl/Cin7 require formal pick steps; SOS/inFlow embed picking into the ship flow; Zoho makes it entirely optional.

2. **Where does pick/pack live in the UI?** — Separate module (Fishbowl), tabs within the SO (Cin7), modal workflow (Method's existing shipping pattern), or inline on the SO screen.

3. **Is packing a distinct step or merged with picking?** — Cin7 separates pick and pack explicitly; Katana merges them; SOS treats the shipment record as the packing slip.

4. **How is the packing slip generated?** — As a print template from the SO (Katana/inFlow), as part of a formal Pack step (Cin7/Zoho), or as a view of the shipment record (SOS).

5. **What status states does the order pass through?** — Current Method has Open → Partially Shipped → Fully Shipped. Do we add picking/packing states, or keep the existing statuses and track pick/pack as sub-states?

---

## Option 1: "Fulfillment Sidebar" — Pick/Pack as an Embedded Panel on the Sales Order

### Philosophy

Pick and pack are contextual actions on a sales order, not separate workflows. The user never leaves the SO screen — a collapsible sidebar panel provides picking instructions, pack confirmation, and packing slip generation inline. This treats pick/pack as a lightweight enhancement to the existing shipping flow rather than a new workflow.

### Why This Approach

This is inspired by **inFlow's tab-based approach** (Pick tab → Ship tab on the same order) and **SOS Inventory's model** (shipment record = packing slip). Method's customers are 3–50 person operations where the same person often creates the SO, pulls items, packs them, and ships them. A separate module or multi-step wizard adds friction for these small teams.

Customer evidence: Phil Helms needs a "delivery ticket" from the sales order — this approach literally generates the pick list and packing slip *from* the SO screen, matching his mental model.

The existing prototype already has the SO detail screen as the hub for shipping and invoicing. Adding pick/pack as another panel on this screen keeps everything in one place.

### Flow Steps

1. **User opens a Sales Order** with status "Open" (has unfulfilled line items).

2. **User clicks "Fulfill" dropdown** (replaces or extends existing "Ship" dropdown). Options:
   - "Pick & Pack" — opens the fulfillment sidebar
   - "Ship All" (existing quick-ship, skips picking for simple orders)
   - "Ship Some" (existing partial ship)

3. **Fulfillment sidebar slides in** from the right side of the SO screen (similar to a detail panel, ~400px wide). The sidebar shows:
   - **Pick List section** — table of line items to pick: Item name, Location, Qty to Pick, Qty Available, checkbox per item
   - "Print Pick List" button generates a printable PDF pick ticket
   - **Status indicators** per item: unchecked (not picked), checked (picked)

4. **User checks off items as they're picked** from the warehouse. Can adjust quantities if doing a partial pick (e.g., only 8 of 10 available). Each checkbox is a confirmation that the physical item has been pulled.

5. **Once items are checked, the sidebar transitions to the Pack section:**
   - Shows picked items ready to pack
   - "Generate Packing Slip" button — creates a printable packing slip (PDF) with customer info, items, quantities, optional price toggle
   - Optional: notes field for special packing instructions

6. **User clicks "Confirm Pack & Ship"** — this triggers the existing shipping flow:
   - Creates ShippedItem records (reuses existing FR-300 logic)
   - Updates order status (Open → Partially Shipped → Fully Shipped)
   - Removes/reduces line items from the main items table
   - Items appear in the "Items Shipped" table below

7. **Packing slip available from shipped items** — after shipping, user can re-print packing slip from the Items Shipped section via a "Print" icon.

### Flow Diagram

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Key UX Decisions

- **Sidebar vs. modal:** Sidebar keeps the SO visible for reference (customer address, notes, other line items). Modals hide context. The existing shipping modals work for simple confirmation but picking benefits from seeing the full order.
- **Pick list as checkboxes, not a separate document:** The pick list is the sidebar itself — no need to navigate to a separate pick list screen. Print if you want a physical copy.
- **Pack merged with pick confirmation:** Since Method's users are small teams, pack is not a separate step — it's confirming that picked items are ready to ship. This avoids the Cin7 problem of requiring a formal pack stage.
- **"Ship All" still works:** Users who don't need picking can skip the sidebar entirely and use the existing ship flow. This mirrors Zoho's optional picking philosophy without the shrinkage gap (because shipping still tracks inventory).
- **Price toggle on packing slip:** Phil Helms' explicit need. Packing slip generation includes a toggle: "Show prices" / "Hide prices".

### Pros

- Zero navigation — everything happens on the SO screen the user already knows
- Reuses existing shipping infrastructure (ShippedItem records, status transitions)
- Optional picking — small orders can skip straight to Ship All
- Pick list and packing slip are views of SO data, not separate entities (SOS pattern)
- Minimal new types needed — PickConfirmation could be a lightweight record
- Matches Method's existing "hub and spoke" SO screen pattern (shipping modal, invoice modal — now fulfillment sidebar)
- Lowest implementation complexity of the three options

### Cons

- Sidebar may feel cramped on smaller screens (1280px and below)
- No batch picking across multiple orders (one SO at a time)
- Pick and pack status not tracked independently — once you ship, it's shipped. No "picked but not yet packed" state.
- Sidebar pattern is new to the prototype (existing flows use modals) — slight consistency concern
- Power users processing 50+ orders/day may find the per-order sidebar slow

### Best For

The office admin at a 5-person shop who creates SOs, walks to the shelf, pulls items, packs them, and ships — all in one sitting. This is the "SPK Associates" persona: low volume, low complexity, same person does everything.

---

## Option 2: "Staged Fulfillment" — Pick → Pack → Ship as Distinct Steps with Status Tracking

### Philosophy

Picking, packing, and shipping are operationally distinct activities that may be done by different people at different times. The system should track each stage independently so the team always knows where every order stands. This is a structured, stage-gated workflow.

### Why This Approach

This draws from **Cin7's 3-stage sequential model** (Pick → Pack → Ship) and **Fishbowl's status progression** (Entered → Committed → Fulfilled → Packed → Shipped). For Method's larger customers — 20–50 person warehouses with dedicated pickers — the person creating the SO is NOT the person picking items. The flow needs handoff points between roles.

Customer evidence: 83 companies (17.8%) cite Order & Fulfillment Tracking as a top JTBD. They need to know "is this order picked? is it packed? is it shipped?" — not just "is it shipped or not." The existing Open → Partially Shipped → Fully Shipped status is too coarse for fulfillment-heavy operations.

Fishbowl's color-coded availability (red/yellow/green) is highly valued by users but requires setup. We can achieve the same visibility with simpler status badges.

### Flow Steps

1. **Sales Order list screen** gains a new column: **Fulfillment Status** (separate from Order Status). Values: Not Started → Pick in Progress → Picked → Pack in Progress → Packed → Ready to Ship. This is a *sub-status* — the existing Order Status (Open/Partially Shipped/Fully Shipped) remains unchanged and only transitions when items are actually shipped.

2. **User opens SO and clicks "Create Pick List"** button (appears when order has unfulfillable line items). This opens a **Pick List modal** (870px, matching existing SelectShippedItemsModal pattern):
   - Info banner: "Select items to include in the pick list"
   - Checkbox table: Item, Location, Qty Available, Qty to Pick (editable), Available indicator (green/yellow/red based on Qty Available vs. Qty to Pick)
   - Cancel / Create Pick List buttons
   - On create: generates a PickList record, fulfillment status → "Pick in Progress"

3. **Pick List appears as a new section on the SO screen** (below line items, above Items Shipped). Table columns: Item, Location, Qty to Pick, Qty Picked, Status (Pending/Picked), Pick Date.
   - "Print Pick List" button generates a PDF pick ticket
   - User updates Qty Picked as items are pulled (editable inline field)
   - When Qty Picked = Qty to Pick for a line item, that row's status changes to "Picked"
   - Items appear in the "Items Shipped" table below

### Flow Diagram

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Fulfillment Status State Machine

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Key UX Decisions

- **FulfillmentStatus as a sub-status:** Adding fulfillment tracking without changing the existing OrderStatus enum. This is non-breaking — the list screen gets a new column, existing status logic is untouched.
- **Pick List as a first-class entity:** Unlike Option 1 where picking is just checkboxes, here the pick list is a saved record with its own state. This enables: re-printing pick lists, tracking pick dates, auditing who picked what.
- **Stage gates:** Ship is gated behind Pack, which is gated behind Pick. This prevents shipping un-picked items (a real problem in Zoho where skipping picking masks shrinkage). Users who want to skip can still use "Ship All" as a bypass.
- **Modal pattern for create/confirm:** Matches the existing SelectShippedItemsModal and InvoiceCreation patterns. Consistent with the prototype's interaction model.
- **Availability indicators:** Green (full stock) / Yellow (partial) / Red (none) per line item on the pick list creation modal. Fishbowl's most-loved feature, simplified.

### Pros

- Full visibility into fulfillment progress — team always knows where orders stand
- Supports role separation (office creates SO → warehouse picks → packer confirms → shipper ships)
- Pick list is a referenceable, printable, auditable document
- Availability indicators prevent wasted picks (red = don't even try)
- Stage gates prevent fulfillment errors (can't ship unpicked items)
- Consistent with existing modal interaction patterns
- Fulfillment Status on the list screen enables queue management ("show me everything that needs picking")

### Cons

- More clicks to complete fulfillment (Create Pick List → update picks → Pack → Ship = 4 distinct actions)
- ulfill' dropdown"}
 FD -->|"Fulfill Items..."| WIZARD["Open Fulfillment Wizard\n870px modal, 3 steps"]
 FD -->|"Quick Ship All"| QS["Existing Ship All\n(unchanged, fast path)"]
 WIZARD --> S1[" STEP 1 — PICK\n\n Select items to fulfill\n Adjust quantities\n Availability indicators\n Print Pick List button\n\nStep: "]
 S1 -->|"Next →"| S2[" STEP 2 — PACK\n\n Review items summary\n Generate packing slip\n Show prices on slip\n Packing notes\n\nStep: "]
 S2 -->|"← Back"| S1
 S2 -->|"Next →"| S3[" STEP 3 — SHIP\n\n Confirm shipment to Customer\n Ship date: Today\n Carrier: ___\n Tracking #: ___\n\nStep: "]
 S3 -->|"← Back"| S2
 S3 -->|"Confirm Shipment"| PROCESS[" Process Shipment\n• Create ShippedItem records\n• Update OrderStatus\n• Generate packing slip PDF\n• Remove/reduce line items"]
 QS --> PROCESS
 PROCESS --> SUCCESS[" Success Modal\n'Shipment created successfully'\n\n View Packing Slip | OK"]
 SUCCESS --> UPDATED[" SO Screen Updated\n• Items Shipped table shows new items\n• Status: Partially/Fully Shipped\n• Packing slip in Print menu"]
 style S1 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
 style S2 fill:#fff8e1,stroke:#f57f17,stroke-width:2px
 style S3 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
 style PROCESS fill:#f3e5f5,stroke:#7b1fa2
 style SUCCESS fill:#e0f7fa,stroke:#00838f,stroke-width:2px
 style QS fill:#f5f5f5,stroke:#9e9e9e
```ethod's UI?" A multi-step wizard within a single modal achieves this by keeping the user in one focused flow.

This approach explicitly avoids the trap of building separate pick and pack infrastructure when the existing Ship flow handles the hardest part (inventory deduction, status transitions, ShippedItem creation) already.

### Flow Steps

1. **User opens SO and clicks "Fulfill" dropdown**. Options:
   - "Fulfill Items..." — opens the enhanced fulfillment modal (pick + pack + ship)
   - "Quick Ship All" — existing Ship All (bypass for simple orders)

2. **Fulfillment modal opens (870px, 3-step wizard):**

   **Step 1 — Pick (Select & Confirm Items):**
   - Table: Checkbox, Item, Location, Qty Available, Qty to Fulfill (editable)
   - Availability indicators: green/yellow/red dots
   - "Print Pick List" button (generates PDF from current selection — user can print, walk to warehouse, come back)
   - Select All / Deselect All
   - Next button (disabled until at least one item selected with qty > 0)

   **Step 2 — Pack (Review & Generate Packing Slip):**
   - Summary table of items being fulfilled (read-only): Item, Location, Qty
   - Packing slip options:
     - Toggle: "Generate packing slip" (on by default)
     - Toggle: "Show prices on packing slip" (off by default — Phil Helms' need)
     - Optional: packing notes field
   - Back / Next buttons
   - Step indicator: ● ○ ○ → ● ● ○ → ● ● ●

   **Step 3 — Ship (Confirm & Complete):**
   - Final confirmation: "You are about to ship [N] items to [Customer Name]"
   - Ship date (defaults to today)
   - Optional: carrier, tracking number fields
   - Back / Confirm Shipment buttons
   - On confirm: creates ShippedItem records, updates order status, generates packing slip PDF if toggled on, shows success modal

3. **Success modal** (matching existing pattern): "Shipment created successfully. [View Packing Slip] [OK]"

4. **Packing slip accessible afterward** from the Items Shipped table via a document icon, or from a "Print" dropdown on the SO.

### Flow Diagram

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Status Transitions (unchanged from current prototype)

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Key UX Decisions

- **Wizard within a modal:** 3-step flow with back/next navigation and a step indicator. This is a new pattern for Method's prototype but is standard in B2B SaaS. The step indicator (● ● ○) gives visibility without adding screen real estate.
- **Pick list is an action within the flow, not a saved entity:** The "Print Pick List" button in Step 1 generates a PDF from the current selection. No PickList record is persisted — the pick list is ephemeral. This keeps the data model simple.
- **Packing slip is generated at ship time:** The packing slip is a document created when the shipment is confirmed, not during a separate "pack" step. This matches inFlow's pattern and the MVP constraint ("packing slip = print option at ship time").
- **Unified flow, optional depth:** Users who don't need the full wizard can use "Quick Ship All" — same as today's Ship All. Users who want picking and packing go through the wizard. Both paths end with ShippedItem records and status updates.
- **No new status states:** The existing OrderStatus (Open → Partially Shipped → Fully Shipped) is unchanged. No FulfillmentStatus, no PickList entity, no new sections on the SO screen. This is the lightest touch on the data model.
- **Carrier/tracking fields:** Step 3 adds optional carrier and tracking number fields that don't exist in the current ship flow. These are commonly requested (57 companies cite shipping/logistics needs) and fit naturally in the confirmation step.

### Pros

- Fewest changes to existing architecture — extends the ship modal, no new entities
- Familiar modal pattern (users already know the SelectShippedItemsModal)
- Pick list and packing slip are generated as part of the flow, not maintained separately
- Step indicator provides structure without rigidity
- "Quick Ship All" preserves the fast path for simple orders
- Carrier and tracking number fields added naturally
- Lowest data model impact — no new types beyond optional fields on ShippedItem
- The 2-minute test: experienced user can complete pick → pack → ship in one continuous flow

### Cons

- No persistent pick list record — can't track "who picked what, when" after the fact
- No fulfillment status visibility on the list screen — can't filter "orders waiting to be picked"
- Wizard modal is a new UI pattern (existing prototype uses single-step modals)
- All-in-one flow doesn't support role separation well (picker and shipper must be the same session)
- If user prints pick list, walks to warehouse, comes back 30 minutes later, the modal state may be lost (depends on implementation)
- No batch picking across multiple orders
- Packing slip can only be generated at ship time — can't preview before committing

### Best For

The 3-10 person operation where one or two people handle everything from SO creation to shipping. They want structure (pick list, packing slip) without bureaucracy (separate stages, status tracking). This is the core Method customer today — operational SMBs who are upgrading from spreadsheets and QuickBooks, not from Fishbowl.

---

## UX Heuristic Comparison

| Heuristic | Option 1: Fulfillment Sidebar | Option 2: Staged Fulfillment | Option 3: Smart Ship Wizard | Notes |
|-----------|:----:|:----:|:----:|-------|
| **Efficiency** | 4 | 2 | 5 | Option 3 is fewest clicks (one continuous flow). Option 2 requires 4 distinct actions across multiple interactions. Option 1 is in-between — sidebar is always available but requires manual state management. |
| **Learnability** | 3 | 4 | 4 | Option 2's explicit stages are most self-documenting ("Create Pick List" → "Pack" → "Ship" is clear). Option 3's wizard with step indicator is nearly as learnable. Option 1's sidebar is a new pattern that needs discovery. |
| **Error Prevention** | 3 | 5 | 4 | Option 2's stage gates prevent shipping un-picked items. Option 3's wizard enforces sequence within the modal. Option 1 allows shipping without picking (by design, but risk of skipping). |
| **Consistency** | 3 | 5 | 4 | Option 2 uses existing modal patterns (SelectShippedItemsModal). Option 3 introduces a wizard but in a modal frame. Option 1 introduces a sidebar — new pattern entirely. |
| **Visibility of Status** | 3 | 5 | 2 | Option 2's FulfillmentStatus on the list screen is the strongest — team-wide visibility. Option 1 shows pick/pack state in the sidebar. Option 3 has no persistent status — once the modal closes, there's no record of pick/pack state until shipment. |
| **Flexibility** | 4 | 3 | 4 | Options 1 and 3 both allow skipping picking for simple orders. Option 2's stage gates can be bypassed but the bypass path feels secondary. All handle partial fulfillment. |
| **Recovery** | 4 | 4 | 3 | Options 1 and 2 allow pausing mid-flow (sidebar stays open; pick list persists). Option 3's modal state is lost if closed accidentally. |
| **Total** | **24** | **28** | **26** | |

### Scoring Rationale

**Option 1 (Sidebar) — 24 total:** Scores well on efficiency and flexibility because everything is inline and skippable. Loses on consistency (new UI pattern), visibility (no list-level status), and learnability (sidebar discovery). The sidebar approach is genuinely useful for power users who live on the SO screen, but it doesn't help the warehouse manager who needs to see fulfillment status across all orders.

**Option 2 (Staged) — 28 total:** Highest total, driven by error prevention (5), consistency (5), and visibility (5). The FulfillmentStatus column on the list screen is a major differentiator — it answers the question "which orders need picking?" without opening each SO. Loses on efficiency (4 distinct actions vs. 1 continuous flow in Option 3).

**Option 3 (Smart Ship) — 26 total:** Strong on efficiency (5) and flexibility (4). The wizard modal is the fastest path from "I have an SO" to "it's shipped with a packing slip." Loses on visibility (2) — there's no persistent fulfillment state, so the team can't see where orders stand in the pick/pack process. Also loses on recovery (3) — closing the modal loses progress.

---

## Operational Reality Assessment

| Dimension | Option 1: Fulfillment Sidebar | Option 2: Staged Fulfillment | Option 3: Smart Ship Wizard |
|-----------|------|------|------|
| **Team reality** | Assumes one person does everything on one screen. Works for the solo operator but breaks down when roles are separated. | Explicitly supports role separation. Office creates SO + pick list, warehouse picks, someone else packs and ships. Each stage has a clear handoff. | Assumes one person does everything in one sitting. The wizard is a single session — doesn't support handing off mid-flow. |
| **Interruption tolerance** | **High.** Sidebar stays open; SO screen persists. User can walk away, come back, resume where they left off. | **High.** Pick list persists as a record. User can close the SO, reopen it later, and see the pick list with current progress. Best interruption tolerance. | **Low.** Modal state may be lost if closed. If user prints pick list, walks to warehouse for 30 min, and the session times out, they restart. |
| **Exception handling** | Partial picks handled via qty adjustment. No formal short-pick fl>|"Yes"| A5["Quick Ship All\nbypass preserved"]
 style A1 fill:#e8f5e9,stroke:#2e7d32
 style A2 fill:#e8f5e9,stroke:#2e7d32
 style A3 fill:#e8f5e9,stroke:#2e7d32
 style A4 fill:#e8f5e9,stroke:#2e7d32
 style A5 fill:#e8f5e9,stroke:#2e7d32
```]
 B2 --> B3["Pick List section<br/>appears on SO"]
 B3 --> B4["Update Qty Picked<br/>inline"]
 B4 --> B5["'Pack' button →<br/>Pack modal"]
 B5 --> B6["'Ship' button →<br/>Ship flow"]
 B6 --> B7["ShippedItems<br/>created"]
 end
 subgraph OPT3["OPTION 3: Smart Ship Wizard "]
 C1["Open SO"] --> C2["'Fulfill Items...'"]
 C2 --> C3["Step 1: Pick<br/>(select + qty)"]
 C3 --> C4["Step 2: Pack<br/>(slip + options)"]
 C4 --> C5["Step 3: Ship<br/>(confirm)"]
 C5 --> C6["ShippedItems<br/>created"]
 end
 style OPT1 fill:#fff3e0,stroke:#e65100
 style OPT2 fill:#e8eaf6,stroke:#283593
 style OPT3 fill:#e8f5e9,stroke:#1b5e20
```st once learned — sidebar is always there, no modals to open/close. Good for high-volume single-operator flows. | Slow — 4 separate interactions per order. Power users will hate the ceremony. No batch picking means every order is individual. | Fast in the modal, but opening a wizard for every single order gets repetitive. "Quick Ship All" helps but then they skip pick/pack entirely. |
| **Operational assumptions** | Assumes: same person creates SO and fulfills it. Small team, low volume, no role separation needed. | Assumes: team may have role separation. Fulfillment is a process, not a one-time action. Pick lists may be printed and given to different people. | Assumes: one person handles everything in one session. Picking is a quick check, not a delegated task. |

### Operational Reality Summary

**Option 1** fits the smallest operations (1-5 people, same person does everything) but breaks when the team grows.

**Option 2** is the only option that works across the full range of Method's customers — from 3-person shops to 50-person warehouses. The cost is ceremony (more clicks, more states).

**Option 3** is the fastest for the solo operator but doesn't scale to team operations. The lack of persistent state is a real gap.

---

## Recommendation

### Primary Recommendation: Option 3 (Smart Ship Wizard) for MVP, with Option 2 elements as Phase 2

**Why Option 3 for MVP:**

1. **Lowest implementation risk.** Extends the existing ship modal rather than building new UI patterns (sidebar) or new data entities (PickList, FulfillmentStatus). The prototype already has the modal infrastructure — this adds steps to it.

2. **Passes the 2-minute test.** A non-specialist can pick, pack, and ship an order in one continuous flow. The step indicator provides just enough structure without forcing the user through bureaucratic stage gates.

3. **Matches the current customer base.** Method's core MWD customers today are 3-15 person operations. They don't have dedicated pickers and packers — the same person does everything. Option 3 is built for this reality.

4. **Preserves the fast path.** "Quick Ship All" remains for users who don't need pick/pack. No one is forced into a new workflow.

5. **Adds the most-requested features.** Pick list printing, packing slip generation with price toggle, and carrier/tracking fields — all delivered with minimal architectural disruption.

6. **Aligns with MVP constraints.** No serial tracking, no barcode scanning, manual-first, desktop-first. Option 3 doesn't require features that are deferred.

**Why not Option 2 for MVP:**

Option 2 scores highest on UX heuristics (28 vs. 26) and is the best long-term architecture. But it requires: a new FulfillmentStatus type, a new PickList entity with CRUD, a new section on the SO screen, a new column on the list screen, and new state management. That's significant scope for an MVP that explicitly defers backorders and automation. The risk of over-engineering is real.

**Why not Option 1:**

The sidebar pattern is unfamiliar in the current prototype and doesn't offer enough advantage over Option 3 to justify the new UI pattern. It also has the worst learnability score.

### Phase 2 Upgrade Path (Option 2 elements)

After Option 3 ships and real users provide feedback, add:

1. **FulfillmentStatus on the list screen** — the single highest-value addition from Option 2. Enables "show me orders that need picking" without opening each SO.
2. **Persistent PickList records** — once users need audit trails ("who picked what, when"), upgrade the ephemeral pick list to a saved entity.
3. **Pick list section on SO screen** — for operations that print pick lists and hand them to warehouse staff who pick asynchronously.

This phased approach gives Method a working pick/pack flow *now* (Option 3) and a growth path *later* (Option 2) based on real usage data rather than speculative design.

### Decision Criteria Summary

| Criterion | Option 1 | Option 2 | **Option 3** |
|-----------|----------|----------|------------|
| UX heuristic score | 24 | **28** | 26 |
| Operational reality (small team) | Good | Overkill | **Best** |
| Operational reality (large team) | Poor | **Best** | Moderate |
| Consistency with prototype | New pattern | **Matches existing** | Near match (wizard is new) |
| Implementation complexity | Medium | **High** | **Low** |
| Data model impact | Low | High | **Minimal** |
| Scalability to future features | Medium | **High** | Medium (upgradable) |
| Passes 5-person warehouse test | Yes | Yes (with training) | **Yes (fastest)** |
| Passes 50-person warehouse test | No | **Yes** | Partial |

**Recommended: Option 3 (Smart Ship Wizard) for MVP → Phase 2 adds Option 2 fulfillment tracking.**

---

## Flow Diagrams

> **Note:** Detailed flow diagrams for each option are included inline within their respective sections above. This section provides the cross-option comparison views.

### Side-by-Side Comparison: All Three Options

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Decision Summary

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

### Phased Rollout

*See rendered diagram in the [interactive flow diagrams page](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html).*

---

## Appendix: Sources Consulted

### Competitor Research
- Full competitor deep-dive report: `Inventory-MWD-/Research/pick-pack/competitor-research.md` (7 competitors, 1279 lines)
- Screenshot reference guide: `Inventory-MWD-/Research/pick-pack/competitor-screenshots-reference.md`
- HTML screenshot galleries: `screenshots/screenshot-gallery.html`, `screenshots/fishbowl-pick-pack-reference.html`, `screenshots/katana-pick-pack-reference.html`
- Competitor flow diagrams: `diagrams/comparison-overview.md`, `diagrams/fishbowl-pick-pack-flow.md`, `diagrams/katana-pick-pack-flow.md`, `diagrams/cin7-pick-pack-flow.md`

### Internal Customer Data (465 MWD transcripts)
- Pain points: `Industry Vertical Playbook/insights/pain_points.md` — Order management (244 co., 53.5%), Shipping/logistics (57 co., 12.9%)
- Feature requests: `Industry Vertical Playbook/insights/feature_requests.md` — Shipping/logistics (57 co., 12.9%), Inventory mgmt (71 co., 15.9%)
- JTBD evidence: `Industry Vertical Playbook/insights/jtbd_evidence.md` — Order & Fulfillment Tracking (83 co., 17.8%)
- Competitor mentions: `Industry Vertical Playbook/insights/competitor_mentions.md`

### Prototype Context
- PROJECT_CONTEXT.md — architecture, types, components, existing flows
- Existing patterns: SelectShippedItemsModal (870px), ItemsTable, SalesOrderScreen 3-column grid, OrderStatus/InvoiceStatus state machines

---

**End of Flow Analysis — Pick/Pack for Method CRM**
