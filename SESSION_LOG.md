# SESSION LOG — Method Inventory Work

**Purpose** — The "where are we right now" doc. Read this first in a new chat
to pick up without losing momentum. For the history of *what has shipped*, see
[`CHANGELOG.md`](./CHANGELOG.md). For prototype architecture, see
`sales-order/PROJECT_CONTEXT.md` (in the separate `sales-order/` folder —
sibling to the parent `Inventory Management/` directory on your Mac).

Last updated: **2026-04-14**

---

## Currently in flight

### 🟡 Paused — Back Orders + Reorder Awareness research

**Status:** Skill invoked on 2026-04-13, paused before Mode 1 to set up docs.

**Decision made:** Research them **together**, not independently. They're two
sides of the same coin — reorder awareness prevents stockouts, back orders
handle what happens when stockouts occur anyway. Splitting them risks designing
two flows that don't talk to each other.

**Next action:** Resume the `inventory-research-agent` skill (still named
that — see open thread below). Suggested entry point is Mode 0 (orchestrator)
or Mode 1 (competitor research) for the joint feature. The skill will read
`PROJECT_CONTEXT.md` and the insights folder
(`Industry Vertical Playbook/insights/`) before going external.

**Prompt to restart the work in a new chat:**
> "Let's resume the back orders + reorder awareness research. Kick off the
> inventory-research-agent skill in Mode 1 — research them together as a joint
> feature. Don't split them."

---

## Recently completed

### ✅ 2026-04-14 — Documentation setup + git discovery

- Replaced Vite boilerplate in `sales-order/README.md` with a real project overview.
- Added CHANGELOG and this SESSION_LOG.
- Confirmed this folder (`Inventory-MWD-/`) is connected to GitHub at
  `github.com/Barbara-stevenson/Inventory-MWD`. Pick-pack research work has
  been sitting uncommitted on the local clone — needs a commit + push from
  your Mac's terminal (commands at the bottom of this file).
- `sales-order/` is not yet in git. Needs its own repo.

### ✅ 2026-04-13 — State persistence + hash routing + toolbar polish

Major session. Four substantive things landed:

1. **SO state persists across navigations.** `SavedOrderState` lifted to
   App.tsx; `SalesOrderScreen` takes `savedState` + `onStateChange`.
   Shipped-items and invoice state no longer reset when you go SO → Invoice → back.
2. **Hash routing with browser back/forward.** Hash ↔ View helpers, popstate
   listener in App.tsx.
3. **Collapsible sections.** Items and Pick List tables now have an
   expand/collapse chevron on their section headers.
4. **Toolbar + Pack cleanup.** Search w-64 → w-32, toolbar gap standardized to
   `gap-1.5`, Pack moved from the action bar into the Pick List section header
   next to Unpick.

### ✅ 2026-04-12 — Pick/Pack implementation

`PickPackWizard`, `PickListSection`, `UnpickModal` created and wired through
App.tsx and SalesOrderScreen. Types and mock data updated. Build + type-check
green.

### ✅ 2026-03-28 — Pick/Pack Mode 3 + Mode 4

PRD, user stories, stakeholder summary updated in `Research/pick-pack/`.
Decision log session 002 captured.

---

## Open threads / known issues

These are pending items worth surfacing in any new chat:

1. **Skill rename did NOT stick.** On 2026-04-13 I tried to rename the skill
   from `inventory-research-agent` → `inventory-research-skill` by editing
   SKILL.md frontmatter. The skills directory is read-only from the sandbox and
   the change was not persisted. Current state: everything still says
   `inventory-research-agent`. If you want the rename, it has to happen on your
   Mac in Finder (rename the folder in `.claude/skills/`) and inside the
   `SKILL.md` frontmatter.

2. **Invoice visual match.** `InvoiceScreen.tsx` was built by mirroring
   `SalesOrderScreen` layout because Pencil screens 4 & 5 are placeholder
   shells. Need Figma designs to verify exact visual match.

3. **Invoice counter.** Starts at 5 each session (see `SalesOrderScreen.tsx:116`).
   Now persisted across in-session navigation via `SavedOrderState`, but reloads
   back to 5 on page refresh. Fine for demo; needs real persistence for production.

4. **Multiple invoices per SO.** The flow supports partial invoicing (multiple
   invoices per SO), but there's no invoice list/history surface on the SO
   screen yet.

5. **`sales-order/PROJECT_CONTEXT.md` is slightly stale.** The state-persistence
   / hash-routing / collapsible-sections changes from 2026-04-13 aren't
   reflected there yet. The "Pending / Known Issues" section still lists the
   back-nav state loss as open (it's been fixed). Worth a refresh next time
   we're editing architecture docs.

6. **`sales-order/` not in git.** No repo, no commits, no GitHub remote. Needs
   its own repo — recommend a new GitHub repo under your account.

---

## Feedback / conventions worth remembering

Captured in auto-memory so they persist across chats:

- **PRD format** — Stock Transfers PRD is the canonical structure. Context
  sections → FR tables with embedded user stories. No implementation details
  in the PRD. Mode 4 does NOT produce a separate user stories file; stories
  live inside the FR tables.
- **Pack UX** — Contextual actions belong next to the data they operate on
  (Pack lives in the Pick List section header, not the global action bar).
- **Design source of truth** — Figma, match exactly. Infer behavior only where
  Figma is silent. Flag conflicts instead of guessing.

---

## Resuming in a new chat — checklist

Copy these four steps into a new chat if the current one compacts:

1. Read `Inventory-MWD-/SESSION_LOG.md` (this file).
2. Read `Inventory-MWD-/CHANGELOG.md` for recent history.
3. Read `sales-order/PROJECT_CONTEXT.md` for architecture (with the staleness
   caveat noted above).
4. Resume the in-flight item above, or tell me what you want to work on next.

---

## Git commands (run from your Mac terminal)

### Commit + push this repo (Inventory-MWD-)

```bash
cd "/path/to/Inventory Management/Inventory-MWD-"

# Clear any stuck lock from sandbox attempts
rm -f .git/index.lock

# Optional: stop .DS_Store noise forever
echo ".DS_Store" >> .gitignore
git rm --cached .DS_Store Research/.DS_Store 2>/dev/null || true

# Stage the pick-pack research + new docs
git add CHANGELOG.md SESSION_LOG.md .gitignore
git add Research/decision-logs/INDEX.md
git add Research/decision-logs/pick-pack-flow/
git add Research/pick-pack/

git commit -m "Add pick-pack research deliverables, CHANGELOG, and SESSION_LOG"
git push origin main
```

### Set up sales-order on GitHub (separate repo)

```bash
cd "/path/to/sales-order"
rm -rf .git                 # clear any half-init state from sandbox
git init -b main
git add .
git commit -m "Initial commit: sales order / inventory prototype"

# Create a new repo on github.com (UI), then:
git remote add origin git@github.com:Barbara-stevenson/sales-order.git
git push -u origin main
```

---

## How to update this log

When a session ends or a chat is about to compact:

1. Move any "currently in flight" items that finished down into "Recently
   completed", then port them into `CHANGELOG.md` under today's date.
2. Update the "currently in flight" section with what's genuinely in progress
   (include the restart prompt so a fresh chat can pick up cleanly).
3. Refresh open threads — mark resolved ones, add new ones.
4. Bump the "Last updated" date at the top.
