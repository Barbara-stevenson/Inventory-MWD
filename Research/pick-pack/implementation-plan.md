# Pick & Pack — Implementation Plan

**Date:** 2026-04-11
**Target prototype:** http://localhost:5174/ (`/Users/barbarastevenson/Learning Claude/sales-order`)
**Source PRD:** `Inventory-MWD-/Research/pick-pack/prd.md`

## Scope for Mode 7

This implementation covers Paths A (one-go), B (save & resume), and C (bypass) from the flow options doc, plus Unpick and Unpack undo flows. Packing slip generation is wired as a browser print action on a hidden printable block rather than a real PDF library — sufficient for prototype review and matches how FR-308 handles document output today.

## New Components

| Component | Story | Purpose |
|---|---|---|
| `PickPackWizard.tsx` | US-100 / US-200 / US-202 / US-300 | 2-step modal (Pick → Pack) launched from the SO action bar. Mirrors `SelectShippedItemsModal` sizing (864px) so it sits in the existing visual family. |
| `PickListSection.tsx` | US-500 / US-501 / US-600 / US-801 | Section on the SO detail screen between Items not shipped and Items shipped; shows pick-list table with Qty Picked editable inline, Print icon, Pack / Unpick / Unpack buttons. |
| `UnpickModal.tsx` | US-800 | Checkbox selection modal; mirrors the existing Undo Shipping modal pattern. |

## Modified Components

| File | Change | Stories |
|---|---|---|
| `types.ts` | Add `FulfillmentStatus` union, `PickListItem`, `PickList` interfaces. Add `fulfillmentStatus` to `SalesOrderSummary`. | US-400 |
| `data/mock.ts` | Add `fulfillmentStatus` on every mock summary row. Add `getPickListByOrderId()` helper (returns undefined for now — pick lists are created in-session). | US-400 |
| `App.tsx` | Extend `SavedOrderState` to include `pickList: PickList \| null` so pick list state survives the invoice round-trip. | US-600 |
| `SalesOrdersListScreen.tsx` | Add `Fulfillment` column next to Invoice Status with coloured badges. Add fulfillment filter above the table. | US-400 |
| `SalesOrderScreen.tsx` | Wire Pick & Pack button in the action bar (between Send and Ship). Visibility per US-100 acceptance criteria. Render `PickListSection` when `pickList` exists. Persist pick list state. Hook Ship confirmation so items shipped also leave the pick list and FulfillmentStatus recomputes. | US-100, US-500, US-600, US-802, US-900 |

## State machine for FulfillmentStatus

```
Not Started
   ↓ (Save Pick List or Next → in wizard)
Pick in Progress
   ↓ (all pick list items Qty Picked == Qty to Pick)
Picked
   ↓ (Confirm Pack)
Packed
   ↓ (Ship from existing FR-300 flow)
Shipped
```

Status is recomputed on every state change by looking at the pick list + shipped items — never stored as plain value internally. On the list screen, the recomputed status is written back onto `SalesOrderSummary` when the SO is saved or navigated away from.

## Print handling (US-201, US-701)

Rather than introducing jsPDF/pdfmake in a prototype, we render a hidden `<div id="printable-pick-list">` (or packing slip) that contains the list / slip markup and call `window.print()` on click. Tailwind `print:` modifiers suppress the app shell during print. Good enough for Barbara's stakeholder review and matches the lightweight approach of the existing shipping flow.

## Out of scope (parking lot for follow-up)

- Persistent fulfillment analytics dashboard (bypass rate metric)
- PDF library integration — prototype uses browser print
- Per-item source-location reassignment on the pick step
- Real-time available-qty updates from other open orders

---

## Implementation order

1. Types + mock ← foundation
2. List screen Fulfillment column ← visible from t=0 so baseline matches PRD
3. PickPackWizard + PickListSection + UnpickModal ← core flow
4. Wire into SalesOrderScreen ← integration
5. App.tsx SavedOrderState extension ← persistence
6. Ship integration + Undo shipment tie-in ← edge cases
7. Build + smoke test
