# Pick & Pack Feature — Stakeholder One-Pager

**Date:** March 28, 2026
**Status:** MVP Ready for Approval
**Scope:** Combined Approach (Option 3 Smart Ship Wizard + Option 2 Persistent Tracking)

---

## The Problem

Method CRM customers (3–50 person manufacturing, warehousing, and distribution firms) manage order fulfillment as a critical bottleneck:

- **244 companies (53.5%)** cite Order Management as their #1 pain point
- **83 companies (17.8%)** identify Order & Fulfillment Tracking as a top job to be done
- **57 companies (12.9%)** specifically request shipping/logistics improvements

**The Gap:** Method has shipping (Ship Some/All) but no formal picking or packing. Users manually pick items from SOs without a formal list, there's no visibility into fulfillment progress, and no role separation between office, warehouse, and shipping staff.

**The Ask:** Phil Helms (Bluewatercas) articulates the core need: *"We need a delivery ticket where we can toggle pricing on and off for the packing slip."* This pattern repeats across customers—they need **flexible documents that blend picking instructions + packing slips + delivery tickets without switching tools.**

---

## What We're Building

A **2-step Pick & Pack wizard modal** combined with **persistent fulfillment tracking** that enables:

1. **Formal Pick List** — Users select items, see stock availability (green/yellow/red indicators), print a location-optimized pick list, and warehouse staff pick asynchronously
2. **Packing Confirmation** — After picking, users confirm items are packed and generate a packing slip (with optional pricing toggle)
3. **Fulfillment Visibility** — New "Fulfillment Status" column on the sales order list (Not Started → Pick in Progress → Picked → Packed → Shipped) so warehouse managers see what needs picking without opening each order
4. **Role Separation** — Office admin creates pick list → warehouse staff picks items → office confirms pack → shipper ships. Each step tracked and auditable.
5. **Undo/Reverse** — Users can unpick, unpack, or undo shipment to handle exceptions and corrections

### Three User Paths

| Path | Use Case | Time | When |
|------|----------|------|------|
| **A: All-in-One** | Pick & Pack in one session, ship later | ~5 min | Fast-moving small teams |
| **B: Save & Resume** | Pick now, pack/ship later (warehouse picks asynchronously) | Variable | Teams with dedicated pickers |
| **C: Skip (Bypass)** | Simple orders—just ship without picking | <2 min | Existing workflow, unchanged |

---

## Why This Approach

### Competitive Landscape

- **Fishbowl** dominates high-structure operations (overkill for 5-person shops, expensive)
- **Katana** is great for small manufacturers but focused on manufacturing
- **Zoho/inFlow** offer simplicity but lack audit trail (users can skip picking entirely, masking shrinkage)
- **No competitor perfectly solves for Method's persona** — 3–50 person SMBs with no barcode infrastructure who need "good enough" picking without a full WMS

### Method's Advantage

**Standalone, no external infrastructure required:**
- No barcode scanners needed (manual entry first)
- No separate WMS system required
- No QB sync needed for picking (only shipping impacts QB)
- Works for 3-person shops and 50-person warehouses with same UI

**Combines speed and structure:**
- Option 3's 2-step wizard is fast (~5 min per order)
- Option 2's persistent PickList + FulfillmentStatus column provides visibility and role separation
- Neither option alone worked; the combination solves both efficiency and scalability

### Decision Criteria

| Criterion | Score | Why |
|-----------|-------|-----|
| **UX Efficiency** | 5/5 | Fewest clicks for most common path (Pick & Pack in one session) |
| **Visibility** | 5/5 | FulfillmentStatus on list screen answers "what needs picking?" instantly |
| **Role Separation** | 4/5 | Pick List section enables asynchronous workflows; tracking is auditable |
| **Small Team Fit** | 5/5 | 2-step wizard feels natural; no stage gates or bureaucracy |
| **Large Team Fit** | 4/5 | Status tracking + persistent records enable 20–50 person operations |
| **Implementation Simplicity** | 4/5 | Moderate complexity; extends existing Ship flow, no full WMS needed |
| **Total** | **30/35** | Highest-scoring option across all dimensions |

---

## What It Affects

### Users Who Get Value

| Role | Benefit |
|------|---------|
| **Office Admin** | Formal workflow to delegate picking; no more manual "walk to warehouse" steps |
| **Warehouse Manager** | Filter orders by FulfillmentStatus to manage queue; see progress without opening each SO |
| **Warehouse Picker** | Printed pick list (location-optimized) feels professional; formal confirmation |
| **Packer** | New formal role; can specialize in packing with confirmation step |
| **Shipper** | Cleaner workflow; only packed items shown in Ship modal; packing slip pre-generated |

### Operational Gains

- **Time savings:** ~5 min per order (vs. current ad-hoc)
- **Error reduction:** Formal pick list + tracking reduces missing items, wrong quantities
- **Visibility:** Warehouse manager gains real-time queue status (orders needing picking, picked, packed, ready to ship)
- **Audit trail:** Every pick, pack, ship action is timestamped and attributed (supports cycle counts, shrinkage investigation)

### Systems Impacted

| System | Change | Impact |
|--------|--------|--------|
| **Sales Order List** | New "Fulfillment Status" column | Warehouse manager can filter/sort by status |
| **Sales Order Detail** | New "Pick List" section, new action bar button | Warehouse staff updates Qty Picked inline; enables async workflows |
| **Shipping Flow** | Ship modal filtered to show packed items first | No breaking changes; existing "Ship All" bypass still works |
| **Invoicing Flow** | No changes | Invoice creation unchanged; pick list visible for audit |
| **Undo Shipment** | Enhanced to work with Pick List section | Existing FR-308 behavior preserved; undoing shipment returns items to Pick List section (if it exists) |

---

## Key Trade-offs

| Trade-off | Decision | Rationale |
|-----------|----------|-----------|
| **Pick impacts inventory immediately vs. Pick is just a confirmation** | Pick is just a confirmation; inventory only reduced at Ship | Prevents double-reduction if user unpicks; aligns with current ShippedItem logic |
| **Barcode scanning in MVP vs. Phase 2** | Manual entry only in MVP | Barcode scanning adds complexity and requires scanner hardware; deferred to Phase 2 |
| **Batch picking (multiple SOs in one list) vs. Per-SO** | Per-SO in MVP | Single SO per pick list in MVP; batch picking deferred to Phase 2 |
| **QB sync for picking vs. No sync** | No QB sync for picking | Picking doesn't change QB inventory; shipping already handles QB sync (or doesn't, per current design) |
| **Packing slip at Pack time vs. Ship time** | At Pack time | Enables preview and signature; aligns with competitor patterns (Cin7, Fishbowl) |
| **Price toggle on packing slip** | Off by default (Phil Helms' request) | Customers don't see pricing; internal delivery ticket can show pricing |
| **Staging/bureaucracy vs. Optional flexibility** | Optional flexibility | Users can skip Pick & Pack entirely via "Ship All" (Path C); no forced stage gates |

---

## Open Questions for Leadership

1. **QuickBooks Sync:** Should picking or packing trigger QB inventory adjustments? (Current: No. Proposed: No change—only shipping affects QB.)

2. **Staff Assignment:** Should pick lists track which warehouse staff member did the picking? (Impacts workflow design—deferred to Phase 2 if needed.)

3. **Carton Tracking:** Should packing support "Box 1 of 3" carton numbering? (Current: No. Deferred to Phase 2.)

4. **Mobile Optimization:** Should Phase 1 include full mobile modal redesign, or is desktop-first acceptable? (Current: Desktop-first, responsive but not mobile-optimized. Mobile optimization in Phase 2.)

5. **Backorder Handling:** Should users be able to partially pick orders (pick 5 of 10, ship those, backorder the rest)? (Current: Yes, supported. No impact on design.)

---

## Implementation Timeline

| Phase | Duration | Scope |
|-------|----------|-------|
| **MVP** | 11 weeks | Pick & Pack wizard, Fulfillment Status, Pick List section, Undo/reverse, PDF generation |
| **Phase 2** | 6–12 weeks | Batch picking, barcode scanning, role-based workflows, fulfillment analytics |
| **Phase 3+** | TBD | Serial/lot tracking, mobile app, carton management, multi-location picking |

**MVP Launch:** End of Week 11 (early June 2026)

---

## Success Metrics (30 Days Post-Launch)

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Adoption Rate** | >60% of active customers use Pick & Pack | Baseline for feature viability |
| **Avg Fulfillment Time** | <10 min per order | Competitive with Katana/inFlow; shows efficiency gain |
| **Pick Accuracy** | >98% SKU/qty match to pick list | Indicates picking instructions are clear |
| **Undo/Rework Rate** | <5% of pick lists reversed | Low rate suggests users understand the workflow |
| **FulfillmentStatus Visibility** | >80% of warehouse managers report "can see order progress on list screen" | Validates that visibility problem is solved |
| **Packing Slip Generation** | >70% of shipments have packing slip | Shows adoption of the full pick-pack-ship flow |

---

## Risk & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|-----------|
| **Modal state lost if browser closes mid-pick** | Medium | User loses partial selections | Save to backend on "Save Pick List" button; Phase 1 supports save + resume |
| **FulfillmentStatus state machine complexity** | Medium | Edge cases in undo/reverse logic | Extensive unit + E2E testing; start with simple undo, enhance in Phase 2 |
| **PDF generation performance** | Low | Pick list/packing slip slow to generate | Use client-side PDF library (jsPDF); async generation if needed |
| **Integration with existing Ship flow breaks** | Low | Shipping no longer works | New Ship modal filters to packed items; falls back to "Items not shipped" if no pick list |
| **Small teams find it bureaucratic** | Low | 3-person shops skip picking entirely | "Ship All" bypass remains unchanged; no forced stage gates |

---

## Budget & Resource Requirements

**Development:** ~7–11 weeks (FE + BE + QA in parallel)
**Design:** Update button/badge styles, new modal template (2–3 weeks)
**Stakeholders:** Product, Engineering, Design, QA, Customer Success (training)
**Customer Communication:** Beta cohort (5–10 customers) for feedback during development

---

## Approval Checklist

- [ ] Product Leadership approves MVP scope
- [ ] Engineering confirms resource availability and timeline
- [ ] Design confirms UI/UX specifications
- [ ] Customer Success prepares training materials
- [ ] Roadmap updated to reflect Pick & Pack as Q2 2026 priority

---

## Visual References

- [Flow Diagrams](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-diagrams.html) — Interactive rendered diagrams of all 3 flow options
- [Flow Walkthrough](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/flow-walkthrough.html) — Step-by-step walkthrough of the recommended MVP flow
- [Competitor Screenshot Gallery](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/screenshots/screenshot-gallery.html) — Side-by-side competitor UI screenshots
- [Fishbowl Pick/Pack](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/screenshots/fishbowl-pick-pack-reference.html) | [Fishbowl Shipping](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/screenshots/fishbowl-shipping-reference.html) | [Katana Pick/Pack](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/screenshots/katana-pick-pack-reference.html) | [Zoho](https://barbara-stevenson.github.io/Inventory-MWD/Research/pick-pack/screenshots/zoho_downloads.html)

---

*Full PRD: [prd.md](prd.md)*
*Competitor Research: [competitor-research.md](competitor-research.md)*
*Flow Options: [flow-options.md](flow-options.md)*
*User Stories: [user-stories.md](user-stories.md)*

---

**Questions? Contact:** Product Team
**Next Steps:** Development kick-off (first day of Week 1)

---
