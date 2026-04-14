# CHANGELOG — Method Inventory Prototype

Dated log of changes to the `sales-order/` prototype and the research deliverables
in this repo (`Inventory-MWD-/Research/`). Read top-down for the latest state.

Dates are pulled from the conversation transcript. Entries older than the
transcript window are summarized in the "Pre-transcript" section at the bottom.

Format: `## YYYY-MM-DD — [area] — Title`

---

## 2026-04-14 — Docs — README / CHANGELOG / SESSION_LOG

- Rewrote `sales-order/README.md` — replaced Vite boilerplate with a real
  project overview (tech stack, layout, what's built, related docs).
- Added `CHANGELOG.md` (this file) to the `Inventory-MWD-` repo.
- Added `SESSION_LOG.md` to the `Inventory-MWD-` repo for continuity across
  compacted chats.
- Confirmed the `Inventory-MWD-` repo is connected to
  `github.com/Barbara-stevenson/Inventory-MWD` (origin) with
  `github.com/J4randa/Inventory-MWD-` as upstream. Pick-pack research was
  uncommitted/untracked until this session.
- `sales-order/` is not yet in git. Attempted `git init` locally — sandbox
  permissions block git from releasing `.git/index.lock`; setup needs to
  happen from the Mac terminal.

---

## 2026-04-13 — Sales Order Screen — State persistence, hash routing, toolbar polish, Pack relocation

Large session. Multiple linked changes:

**State persistence across navigations** (App.tsx, SalesOrderScreen.tsx)
- Added `SavedOrderState` interface in App.tsx: `{ order, shippedItems, invoiceCounter, pickList }`.
- Lifted saved-state map to App.tsx and passed `savedState` prop into
  `SalesOrderScreen`, with `onStateChange` callback to sync changes back up.
- Fixes the previous issue where navigating SO → Invoice → back reset shipped
  items / invoice state in the SO detail view.

**Hash-based routing with browser back/forward** (App.tsx)
- Added `viewToHash` / `hashToView` helpers, `useEffect` listening for `popstate`,
  and a `setView` callback that syncs view → hash.
- Browser back/forward now works across SO list / SO detail / invoice / items.

**PickPackWizard refinements** (PickPackWizard.tsx)
- Cleaned up `buildPickList` status logic.
- Step indicator only shows both dots when Pick was the entry point (otherwise
  the wizard entered directly at Pack).

**Collapsible section headers** (ItemsTable.tsx, PickListSection.tsx)
- Added `expanded` local state and a `ChevronDown` / `ChevronRight` toggle on
  the section headers so users can collapse the Items and Pick List tables.
- Removed the now-unused `ViewAllInventoryModal` import from `ItemsTable.tsx`.

**Toolbar consistency** (ItemsTable.tsx, PickListSection.tsx, SalesOrderScreen.tsx)
- Standardized the three SO section toolbars (Items not shipped, Pick List,
  Items shipped).
- Shrunk the search input: `w-64` → `w-32`.
- Iterated the gap between search / filter / more icons: `gap-1` → `gap-2` →
  `gap-1.5` (final).

**Pack action moved to Pick List section header** (SalesOrderScreen.tsx)
- Pack button was living in both the bottom action bar and the Pick List
  section header. Action-bar Pack was ambiguous — it felt disconnected from
  the pick list data it operates on.
- Decision: Pack belongs next to the data. Kept Pack in the Pick List section
  header next to Unpick; removed it from the action bar.
- Final action bar: **More Actions · Send · Pick · Ship · Save**.

**Select primitive update** (select.tsx)
- Minor update to `SelectItem` forwardRef typing / trigger label handling.

**Skill rename attempt** (SKILL.md)
- Tried to rename the `inventory-research-agent` skill to
  `inventory-research-skill` by editing SKILL.md frontmatter. The skills
  directory is read-only from the sandbox — **the rename did not persist**.
  Current state: skill is still `inventory-research-agent` everywhere.

---

## 2026-04-12 — Pick / Pack — Implementation landed

**Implementation plan** written to
`Research/pick-pack/implementation-plan.md`.

**New components** (in `sales-order/src/components/`)
- `PickPackWizard.tsx` — guided pick → pack → ship wizard.
- `PickListSection.tsx` — pick list table on the SO detail screen.
- `UnpickModal.tsx` — reverse a pick with a confirm step.

**Type + data changes**
- `src/types.ts` — added `PickList`, `PickListItem`, and related types.
- `src/data/mock.ts` — added mock pick list data + lookups.

**Wiring**
- `src/App.tsx` — routed the new wizard, lifted pick list state.
- `src/components/SalesOrderScreen.tsx` — integrated `PickListSection`, Pick
  button, wizard hooks.
- `src/components/SalesOrdersListScreen.tsx` — surfaced fulfillment status.

Type-check + full build verified green before wrap.

---

## 2026-04-11 — Exploration / resume

- Resumed after compaction. Located the sales-order repo and the pick-pack
  research folder. No code changes this day — context gathering for the
  implementation work that kicked off on 2026-04-12.

---

## 2026-04-02 — Skill — Packaging updates

- Updated the `inventory-research-agent` skill and packaged a `.skill` file.
- Related artifacts in `Inventory Management/` (outside this repo):
  - `inventory-research-agent.skill`
  - `inventory-research-agent-update.skill`
  - `skill-updates/`

---

## 2026-03-28 — Pick / Pack — Mode 3 (PRD) + Mode 4 (user stories)

- Ran Mode 3 (PRD) and Mode 4 (user story refinement) for pick/pack.
- Updated:
  - `Research/pick-pack/prd.md`
  - `Research/pick-pack/user-stories.md`
  - `Research/pick-pack/stakeholder-summary.md`
- Decision log updated:
  - `Research/decision-logs/pick-pack-flow/2026-03-28-session-002.md`
  - `Research/decision-logs/INDEX.md`

---

## Pre-transcript — Earlier foundation (approximate)

These landed before the current transcript window. Details sourced from
`sales-order/PROJECT_CONTEXT.md`, not reconstructed from session history:

- **Sales Order CRUD** — List + detail screens, 3-column form grid, editable
  line items table, SO summary persistence.
- **Shipping (FR-300 series)** — Ship some / Ship all, select-items modal,
  confirmation step, ShippedItem records, status transitions.
- **Undo Shipping (FR-308)** — Undo button on shipped items table (non-invoiced
  only), confirm modal, qty restoration.
- **Invoicing (FR-400 / FR-401 / FR-402)** — Invoice has no inventory impact,
  Create Invoice modal with AR Account + shipped-items checkbox table, success
  dialog, dedicated `InvoiceScreen.tsx`, auto-updating invoice status.
- **Pick-Pack research — Mode 1 + Mode 2** — Competitor research, flow options,
  diagrams, HTML galleries (all in `Research/pick-pack/`).

---

## How to add an entry

When shipping a change to the prototype or landing a research deliverable, add
an entry at the top of this file under today's date:

```markdown
## YYYY-MM-DD — [area] — Title

**What changed** — bullets of concrete changes (files, components, behavior)
**Why** — one or two sentences on the rationale (link to decision log if relevant)
**Related** — links to PRD / flow options / decision log entries
```

Keep entries terse and scannable — `SESSION_LOG.md` is the right place for
longer-form context on in-flight work.
