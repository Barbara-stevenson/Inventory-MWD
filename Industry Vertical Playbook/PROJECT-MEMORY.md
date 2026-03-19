# PROJECT-MEMORY.md — Mia's Notebook

**Purpose:** Project-wide decisions, constraints, and corrections that every agent must respect. Read this FIRST before producing any deliverable.

**Last updated:** March 16, 2026

---

## Critical Constraints

### 1. Inventory Positioning — DO NOT OVERSTATE
Method has NOT launched its Inventory Management product. It is several quarters away. Every deliverable must position inventory based on current capabilities only:
- QB-synced inventory items (Inventory Parts for QBO + Desktop, Assembly Items for Desktop only, Advanced Inventory sync for Desktop only)
- Customer customization examples (third-party API integrations like SOS Inventory, and in-house custom builds for warehouse tracking, serial numbers, bin locations)
- See `reference/INVENTORY-REALITY-CHECK.md` for the full source of truth
- **Never reference:** native multi-warehouse inventory, committed vs. available stock, or a Jan 2026 inventory launch

### 2. Output Format — Option A Modular Card System
The playbook will NOT be a single long PDF or a long-scroll website. It uses a **hub-and-spoke model**:
- **Central hub:** Short overview (2-3 pages) linking to standalone cards
- **Cards:** Self-contained 1-3 page deliverables (persona cards, battlecards, message houses, discovery guides, one-pagers)
- **Appendix cards:** Deeper reference material for those who want it
- Each card must stand alone — someone should be able to pick up a single battlecard or persona card without reading anything else
- Format spec to be documented separately

### 3. Section 1 Market Landscape — Needs Corrections
`deliverables/section-1/01-mwd-market-landscape.md` contains incorrect inventory references from an earlier draft. Specific fixes listed in `reference/INVENTORY-REALITY-CHECK.md` under "Items to Correct in Existing Deliverables."

---

## Working Rules

### Agent-First Decision Making
When a question comes up about content strategy, positioning, structure, or whether something belongs — consult the relevant agent(s) FIRST and present their recommendation, rather than asking the user to decide from scratch. The user wants agent-informed recommendations, not open-ended questions. These agents were built before the project started for a reason — their perspectives are consistently valuable and should be used proactively, not just when asked.

**Always consult agents when:**
- Making structural decisions (Mia)
- Writing or rewriting messaging (Marcus, Vera)
- Adding data claims or proof points (Maya, Jordan)
- Building content or campaigns (Sam, Leah, Kai)
- Scoping competitive angles (Dex, Kai)
- Defining ICPs or personas (Riya)

**Multi-agent consultation:** When a decision crosses squad boundaries (e.g., "should this quote be used in marketing?"), consult all relevant agents and synthesize their perspectives before presenting a recommendation. The M9 Prospect Voice card is a good example — Mia (strategy), Marcus (brand voice), and Sam (production) all had distinct, valuable inputs.

Examples: "Is this a job or a benefit?" → ask Jordan. "Does this tone work?" → ask Vera. "Should this be a standalone card or fold into another?" → ask Mia. "Can we use prospect quotes externally?" → ask Mia + Marcus + Sam.

---

## Project Decisions Log

| Date | Decision | Context |
|---|---|---|
| Mar 16, 2026 | M9 Prospect Voice Library added to toolkit | Mia (strategy) + Marcus (voice) + Sam (production) consensus: "voice mining, not quoting" — internal quotes inspire deployable lines, raw quotes separated into Voice Vault, aggregate stats are external-safe. Permission Pipeline for best quotes. |
| Mar 16, 2026 | Agent-First rule strengthened in Working Rules | Multi-agent consultation required for cross-squad decisions. Agents should be used proactively, not just when asked. |
| Mar 16, 2026 | Trial duration updated: 14 days → 10 days | Updated across M1, M4, M5, M6, and gen_whitepaper.py customer journey diagram |
| Mar 16, 2026 | Method Donor removed from M6 | Not a priority for Method. Only Field Services and Proposals remain as "other product lines." |
| Mar 16, 2026 | Customer name errors fixed in M3 | Cigar & Wine Distributor = Vintage Makers (was incorrectly Europena). $25M Food Distributor = Europena (was incorrectly Atalanta). Full QA audit confirmed no other factual errors. |
| Mar 13, 2026 | Job 7 (Systematize Tribal Knowledge) dropped from JTBD | Jordan's call: it's a buying trigger and benefit, not a standalone job. Knowledge-retention absorbed into Jobs 1 and 4. |
| Mar 12, 2026 | Agent system with 11 agents across 3 squads + PMM lead | Organized by Research → Messaging → Execution pipeline |
| Mar 12, 2026 | Mia = Head of Product Marketing (strategy + QA), not just QA | She validates that deliverables serve the GTM motion, not just that they're well-written |
| Mar 12, 2026 | Option A modular card system for output format | 57-page PDF and long Gamma site both failed the "skimmability" test |
| Mar 12, 2026 | Layered memory (Option 3): PROJECT-MEMORY.md + per-agent CONTEXT.md | Keeps project-wide constraints centralized and agent-specific notes local |
| Mar 12, 2026 | Inventory reality check created | Upcoming Inventory Management product is NOT launched — position only current QB sync capabilities + customization examples |
| Mar 12, 2026 | Customer customization examples added to inventory knowledge | 4 examples: SLE Technologies, Cypress Engine, Warehouse Tracking (Safwan), Euroboor (Joseph) |

---

## Method Positioning Anchors

These are non-negotiable across all deliverables:
- **Core positioning:** "The CRM that adapts to your business, not the other way around"
- **Three Yes pillars:** Yes to customization, Yes to QuickBooks, Yes to support
- **ICP:** US/Canada SMBs, QuickBooks-first, 10+ employees, $2M+ revenue
- **Primary vertical (this playbook):** Manufacturing, Warehousing & Distribution (MWD)
- **Tone:** Direct, conversational, grade 8 vocabulary. No buzzwords. Bold but not silly.

---

## Known Gaps to Be Transparent About

These should appear in honest gaps sections, not be hidden:
- Inventory management is QB sync, not native — complex needs require third-party tools or customization
- No native BOM, kitting, lot tracking, or shop floor control
- QBO users lose significant functionality vs. QB Desktop users (assemblies, sales orders, advanced inventory, price levels)
- No native e-commerce integration
- Reporting requires customization for MWD-specific dashboards
- Mobile app is functional but not warehouse-optimized out of the box

---

## Playbook Build Order

1. **Market & Customer Foundation** (Section 1) — Maya, Jordan, Riya ← IN PROGRESS, needs inventory corrections
2. **Positioning & Messaging** (Section 2) — Marcus, Leah, Kai, Vera
3. **Competitive Intelligence** (Section 3) — Dex, Kai
4. **Sales Enablement** (Section 4) — Sam, Dex, Riya
5. **Launch Plans** (Section 5) — Leo, Marcus, Sam, Leah

All sections reviewed by Mia before shipping.

---

## File Reference Quick Links

| File | What it is |
|---|---|
| `AGENTS.md` | Full agent roster, skills, squad assignments, step mapping |
| `playbook-plan.md` | Master plan — 5 sections, build order, deliverable specs |
| `reference/INVENTORY-REALITY-CHECK.md` | Inventory positioning source of truth |
| `reference/product/Inventory-Customizations-Examples.pdf` | 4 customer inventory customization case studies |
| `deliverables/section-1/01-mwd-market-landscape.md` | Section 1 deliverable (needs inventory corrections) |
| `knowledge-graph.html` | Visual knowledge graph of playbook relationships |
