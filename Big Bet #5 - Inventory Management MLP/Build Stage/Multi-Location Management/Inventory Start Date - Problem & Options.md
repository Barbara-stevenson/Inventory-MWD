# Inventory Start Date — Problem & Options

**Date:** February 18, 2026
**Participants:** John Miranda, Barbara Stevenson
**Status:** Pending engineering spike (Rich) — Launch target February 27

---

## The Problem

When a customer enables inventory management in Method, validations on Sales Orders and Purchase Orders are applied to **all transactions** — both new and existing. This means a customer who has been on Method for years and simply wants to update a memo, add an attachment, or make a minor edit to an old SO or PO will be **blocked on save** because those old transactions don't have inventory fields (like source location) filled in.

This is an architectural issue: Method is validating against an inventory start date versus the transaction's created date, with no distinction between pre-inventory and post-inventory transactions.

**The core user experience failure:** A customer who never intended to retroactively track inventory gets locked out of editing their own historical transactions.

---

## Three Options for Inventory Start Date

### Option 1 — Auto-set to Date of Enablement (Recommended for MVP)

**How it works:**
When a customer enables inventory management, the system automatically sets the inventory start date to today. Validations apply only to transactions created **on or after** that date. All transactions predating enablement are permanently exempt.

The start date is surfaced clearly in the multilocation settings page — e.g., *"Inventory tracking active since February 18, 2026"* — so customers always know when it started.

If a customer needs to backdate transactions or add inventory tracking to older records, they contact the support team.

**Pros:**
- Eliminates the problem entirely with zero user friction
- No decisions required at setup — no wrong answer a customer can pick
- No edge cases at the UI level
- Consistent with how QBO, Cin7, NetSuite, and Fishbowl all handle this (industry standard "go-live date" pattern)
- The "start date visibility" concern from engineering is solved by displaying the date in settings — a display problem, not a design problem

**Cons:**
- Customers who want to backfill recent transactions must contact support
- Not self-serve for backdating

**Engineering caveat addressed:** Rich raised the concern that customers won't know when their inventory started. The fix is simple: show the start date prominently in multilocation settings. This is already close to the current design plan. It's a label, not a new feature.

---

### Option 2 — Preset Options During Enablement

**How it works:**
When the customer clicks Enable, the confirmation modal presents a choice:

- Start tracking from **today**
- Start tracking from **3 months ago**
- Start tracking from **6 months ago**
- Start tracking from **1 year ago** *(max, based on PS team input that customers typically update transactions within the previous fiscal year)*

The customer selects one, and the system sets validations accordingly for all transactions within that window.

**Pros:**
- Gives customers who need recent backfill a self-serve path
- Bounded options reduce the risk of customers picking an unreasonable date
- PS team confirmed 1 year is the realistic maximum window

**Cons:**
- Adds a decision to the enablement flow — customers don't always know what they need
- If a customer picks 6 months, all transactions in that window now require inventory fields → they may have just created hundreds of blocked transactions voluntarily (shipping the bug by choice)
- Increases development complexity and edge cases
- The "right" preset is unclear to most customers at setup time

---

### Option 3 — Free Date Picker

**How it works:**
When the customer clicks Enable, they are presented with a calendar date picker and can choose any date they want as their inventory start date.

**Pros:**
- Maximum flexibility

**Cons:**
- Highest support burden — customers will pick wrong dates
- Most complex to engineer
- Creates unbounded edge cases depending on how far back a customer goes
- Not appropriate for MVP
- Dismissed during design jam as too complex

> **Note:** If a customer needs this level of control, the current approach is to direct them to the PS or support team.

---

## Industry Precedent

Every major inventory and accounting platform converges on the same pattern: set a start date, surface it, and exempt everything before it.

| Platform | Approach |
|---|---|
| **QuickBooks Online** | Per-item "As of Date" — transactions cannot be dated before it. Same validation behavior Method is experiencing. |
| **Cin7** | "Order lock date" — a cutoff point set at integration go-live. Visible and configurable in settings. |
| **NetSuite** | Go-live date established during implementation. Opening balances entered as of that date; historical transactions exempt. |
| **Fishbowl** | "GO Live Date" serves as the cutoff for all inventory bills. |

No platform ships a free date picker for MVP. The date is either automatic or set once during onboarding — and always visible in settings.

---

## Re-enabling After Disabling

Customers can disable inventory management at any time. The current system does **not** hard delete data — disabling is essentially a UI state (hiding/showing). When re-enabled, all previous inventory data is still intact.

The question is: what start date behavior applies when a customer re-enables?

Three flows were considered:

### Flow 1 — Automatically Resume (Simplest)

**How it works:**
When the customer re-enables, the system automatically restores the previous state with no prompt. Inventory tracking resumes from the original start date. No choice is presented.

If there's a gap period (e.g., they disabled for 2 months), transactions created during that time won't have inventory data — the customer may need to do stock adjustments to reconcile.

**Best for:** MVP. Predictable, no ambiguity, no additional engineering beyond the current architecture.

---

### Flow 2 — Give User a Choice on Re-enable

**How it works:**
When the customer re-enables, they are shown a prompt:

- **"Pick up where I left off"** — Restores previous start date and all existing tracking data
- **"Start tracking from today"** — Sets a new start date to today; effectively resets inventory tracking

**Note:** "Start tracking from today" would require erasing all previous inventory tracking associations and restarting — significant engineering complexity.

**Best for:** Post-MVP, once there's data on how often customers actually disable and re-enable and why.

---

### Flow 3 — Let User Define a New Historical Date (Dismissed)

**How it works:**
On re-enable, the customer can freely input a past date as their new start date.

**Why it was dismissed:** Too much complexity. Creates edge cases on top of already-complex edge cases. Not needed for MVP. If a customer needs this, they contact the PS/support team.

---

## Summary Table

| Scenario | MVP Decision |
|---|---|
| First enable | Start date = today (automatic, no user choice) |
| Start date visibility | Display "Inventory tracking active since [date]" in multilocation settings |
| Backdating need | Direct customer to support team |
| Disable | Confirm disable; inform customer that transactions during disabled period won't be reflected in inventory |
| Re-enable | Resume from previous start date automatically (Flow 1) |
| Re-enable with fresh start | Post-MVP consideration (Flow 2) |

---

## Next Steps

- [ ] John: Create Jira ticket detailing the three options with this document linked
- [ ] Barbara: Ask Rich to spike the ticket and estimate scope increase
- [ ] Barbara: Clean up Figma exploration with the three options clearly shown
- [ ] John: Block Barbara's calendar to review service/non-inventory items in the invoice flow
- [ ] Barbara: Mock up the invoicing modal redesign with a switchable tab for service vs. inventory items
