# Kano Model Analysis: Inventory Roadmap Validation
**Date:** February 18, 2026
**Respondents:** 11 total — 2 Partners, 8 PS Team, 1 Customer
**Surveyed Features:** 10 inventory capabilities across current roadmap and adjacent opportunities

---

## Background

Ben tasked us with using the Kano Model to pressure-test the inventory roadmap prioritization before committing to the build sequence. We ran a structured Kano survey with partners, the PS team, and active customers. The goal: validate which features are table stakes, which are differentiators, which delight, and which don't move the needle.

This analysis classifies each feature, surfaces roadmap misalignments, and flags gaps not currently in scope.

---

## How to Read This Analysis

The Kano Model uses two survey questions per feature — one functional ("how would you feel if this existed?") and one dysfunctional ("how would you feel if this did NOT exist?") — to classify features into five categories:

| Category | What It Means | Strategic Implication |
|---|---|---|
| **Must-have (M)** | Expected baseline. Absence causes dissatisfaction, but presence doesn't delight. | Ship it. Not having it costs you customers. |
| **One-dimensional (O)** | Linear satisfaction. More = better, less = worse. | Compete on it. Better execution = direct satisfaction gains. |
| **Attractive (A)** | Unexpected delight. Absence is forgiven; presence surprises positively. | Differentiate with it. Don't let it block shipping. |
| **Indifferent (I)** | Doesn't move the needle either way. | Deprioritize. Don't build for its own sake. |
| **Reverse (R)** | Feature actively unwanted by some respondents. | Investigate before building. May add complexity without value. |

**Satisfaction (CS) and Dissatisfaction (DS) Coefficients** quantify the impact:
- **CS** (0–1): How much satisfaction the feature adds when present. Higher = more delight potential.
- **DS** (0 to −1): How much dissatisfaction the feature creates when absent. More negative = more pain when missing.

The ideal Must-have sits at low CS / high DS (expected, not exciting). The ideal Attractive sits at high CS / low DS (exciting, but not missed if absent). One-dimensional features sit near the diagonal (high CS and high DS).

---

## Respondent Breakdown

| Group | Count | Notes |
|---|---|---|
| Partners | 2 | Paulette, David |
| PS Team | 8 | Full team survey |
| Customers | 1 | Toby, Liquimed Lock |

**Important caveat:** With only 1 customer respondent, customer-specific findings should not be treated as statistically significant. The analysis leans on PS team data (n=8) as the primary signal, supplemented by partner perspective. A follow-up customer survey with broader participation is recommended before acting on customer-specific conclusions.

---

## Feature-by-Feature Classifications

### Classification Summary Table

| Feature | Classification | M | O | A | I | R | CS | DS |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stock Transfers | **Must-have** | 5 | 4 | 1 | 1 | 0 | 0.45 | -0.82 |
| Low Stock Alerts | **Must-have** | 5 | 4 | 0 | 2 | 0 | 0.36 | -0.82 |
| Audit Trail | **Must-have** | 6 | 2 | 3 | 0 | 0 | 0.45 | -0.73 |
| Packing Slips | **Must-have** | 4 | 2 | 2 | 2 | 1 | 0.40 | -0.60 |
| Serial Number Tracking | **Must-have*** | 4 | 2 | 4 | 1 | 0 | 0.55 | -0.55 |
| Backorder Support | **Split (M/O/A)** | 3 | 3 | 3 | 2 | 0 | 0.55 | -0.55 |
| Price Variations | **One-dimensional** | 3 | 4 | 3 | 1 | 0 | 0.64 | -0.64 |
| Bin/Sub-location Tracking | **Attractive** | 1 | 3 | 6 | 1 | 0 | 0.82 | -0.36 |
| Item Images | **Attractive** | 1 | 1 | 6 | 3 | 0 | 0.64 | -0.18 |
| Reorder Line Items | **Indifferent** | 3 | 2 | 1 | 5 | 0 | 0.27 | -0.45 |

*Serial Number: M and A tied at 4 each; Must-have assigned by Kano priority convention (M > A).*

---

### CS/DS Coefficient Positioning

```
High CS (delight when present)
     1.0 |
         |
     0.8 |         [Bin Tracking]
         |
     0.6 |      [Item Images]  [Price Variations]
         |                  [Serial #] [Backorder]
     0.4 |         [Stock Transfers] [Audit Trail]
         |          [Packing Slips]
     0.2 |            [Low Stock Alerts]
         |                [Reorder Line Items]
     0.0 +----------------------------------------
         0.0  -0.2  -0.4  -0.6  -0.8  -1.0
              Low DS ← → High DS (pain when absent)

Quadrants:
  Top-right (high CS, high DS):  Performance/One-dimensional — compete on these
  Top-left  (high CS, low DS):   Attractive — delight features, safe to delay
  Bottom-right (low CS, high DS): Must-have — ship these first, no negotiation
  Bottom-left  (low CS, low DS):  Indifferent — deprioritize or cut
```

---

### Feature Deep Dives

---

#### 1. Stock Transfers (Multi-Location Inventory)
**Classification: Must-have** | CS: 0.45 | DS: -0.82

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 2 | 0 | 0 | 0 |
| PS Team | 2 | 4 | 1 | 1 |
| Customer | 1 | 0 | 0 | 0 |

Partners are unanimous: this is table stakes. The PS team is slightly more nuanced (4 of 8 classify it as One-dimensional, meaning they see it as a quality-of-execution issue, not just presence/absence). The -0.82 DS score is one of the highest in the survey — customers will feel the pain of its absence acutely.

**Verdict:** Priority 1 placement is validated. Ship this.

---

#### 2. Low Stock Alerts / Reorder Points
**Classification: Must-have** | CS: 0.36 | DS: -0.82

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 2 | 0 | 0 | 0 |
| PS Team | 2 | 4 | 0 | 2 |
| Customer | 1 | 0 | 0 | 0 |

Tied with Stock Transfers for highest dissatisfaction score (-0.82). Partners and most customers treat it as expected. The PS team is split between Must-have and One-dimensional, suggesting MWD customers feel this deeply but some PS members assess it more as a competitive quality dimension. The low CS (0.36) confirms it won't delight — but missing it will cost you.

**Verdict:** Priority 1 placement is validated. Ship this.

---

#### 3. Audit Trail / Inventory Change History
**Classification: Must-have** | CS: 0.45 | DS: -0.73

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 2 | 0 | 0 | 0 |
| PS Team | 4 | 2 | 2 | 0 |
| Customer | 0 | 0 | 1 | 0 |

**This is the biggest roadmap surprise.** Audit trail is currently in Priority 3, but the Kano data classifies it as a Must-have with strong conviction (M=6, no Indifferent responses). Six of eleven respondents say they expect it; three say they'd like it (Attractive); none are neutral. DS of -0.73 means its absence generates significant pain. Partners are unanimous that this is required. The PS team skews heavily toward Must-have with Attractive secondary responses.

The likely explanation: MWD customers operate with fragile, manual inventory systems. When something goes wrong — a discrepancy, a missing item, a mislabeled transfer — they need to reconstruct what happened. Audit trail isn't exciting, but it's the safety net that enables trust in the entire system.

**Verdict:** Audit Trail is misplaced in Priority 3. Should be elevated to Priority 2 at minimum, with consideration for Priority 1 inclusion. No other Priority 3 feature scores as high on dissatisfaction potential.

---

#### 4. Packing Slips
**Classification: Must-have** | CS: 0.40 | DS: -0.60
*(Note: 1 Reverse response excluded from coefficients; valid n=10)*

| Group | M | O | A | I | R |
|---|:---:|:---:|:---:|:---:|:---:|
| Partners | 1 | 0 | 0 | 1 | 0 |
| PS Team | 3 | 2 | 1 | 1 | 1 |
| Customer | 0 | 0 | 1 | 0 | 0 |

**Packing slips are not in the current roadmap, but the data suggests they should be.** Four respondents classify this as a Must-have. The DS of -0.60 signals meaningful pain when absent. This makes operational sense: MWD merchants ship physical goods, and packing slips are the physical handoff document between warehouse and customer.

One Reverse response (PS team) is worth noting: one team member dislikes the feature when it exists, likely because they believe packing slips belong in QBO rather than Method, or because duplicating the output across tools creates confusion. This is a valid architectural concern to investigate — we should clarify whether the intent is to generate packing slips natively in Method or to link/trigger them from QBO.

**Verdict:** Packing slips appear to be a roadmap gap. Validate whether this should be added to the backlog. Resolve the QBO vs. Method ownership question before scoping.

---

#### 5. Serial Number Tracking
**Classification: Must-have** (tied with Attractive) | CS: 0.55 | DS: -0.55

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 1 | 0 | 1 | 0 |
| PS Team | 3 | 2 | 3 | 0 |
| Customer | 0 | 0 | 0 | 1 |

This feature has the most evenly split classification in the dataset (M=4, A=4). The CS/DS positioning (0.55 / -0.55) sits almost exactly on the One-dimensional diagonal, suggesting it may be best understood as a performance feature that skews toward Must-have for some segments.

Segment context matters here: medical and healthcare accounts (47% Very High complexity) need serial number tracking for FDA compliance and traceability. For those customers, this is an absolute requirement. For general distribution or wholesale customers, it's more of a nice-to-have. The PS team reflecting 3 Must-have and 3 Attractive responses likely mirrors this split in their customer base.

**Verdict:** Not in the current MLP scope. Should be treated as a Priority 2/3 addition for medical and regulated-goods segments specifically. Consider gating behind the integration path (Katana/SOS) rather than native build.

---

#### 6. Backorder Support
**Classification: Split (M/O/A — 3-way tie)** | CS: 0.55 | DS: -0.55

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 2 | 0 | 0 | 0 |
| PS Team | 1 | 3 | 2 | 2 |
| Customer | 0 | 0 | 1 | 0 |

The three-way tie is a meaningful signal itself: backorder support means different things to different customer types. Partners see it as expected (M=2). But the PS team is split across all three satisfaction categories, and the 2 Indifferent responses suggest some accounts don't have the workflow complexity where backorders are relevant.

The CS/DS positioning (0.55, -0.55) places this firmly in One-dimensional territory — better execution on backorder workflows yields proportional satisfaction gains.

**Verdict:** Priority 2 placement is validated, but scope carefully. The feature is useful but not universal — avoid over-engineering for edge cases (partial backorders, complex fulfillment rules) in the initial cut.

---

#### 7. Price Variations / Customer-Specific Pricing
**Classification: One-dimensional** | CS: 0.64 | DS: -0.64

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 1 | 0 | 1 | 0 |
| PS Team | 2 | 4 | 2 | 0 |
| Customer | 0 | 0 | 0 | 1 |

**This is also not in the current roadmap, but it scores as the strongest One-dimensional feature in the dataset.** With a CS of 0.64 and DS of -0.64, it sits at the top-right of the positioning chart — more execution here directly equals more satisfaction. The PS team particularly clusters around One-dimensional (4 of 8), reflecting frequent customer ask in implementation scenarios where distributors and wholesalers need price tiers by customer group, volume, or promotion.

This is a known QBO feature (price levels), but Method's current UX doesn't surface it contextually during order entry — which is the most critical workflow moment identified in the product thesis.

**Verdict:** Roadmap gap. Surfacing customer-specific pricing at order entry aligns directly with the thesis that stock visibility at order entry is the single most critical moment. Recommend adding to the backlog with consideration for Priority 2 or 3.

---

#### 8. Bin / Sub-Location Tracking
**Classification: Attractive** | CS: 0.82 | DS: -0.36

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 1 | 0 | 1 | 0 |
| PS Team | 0 | 3 | 5 | 0 |
| Customer | 0 | 0 | 0 | 1 |

Highest CS score in the dataset (0.82), with a modest DS of -0.36. This is the clearest Attractive feature — respondents light up when it's present, but don't feel burned by its absence. One Paulette (partner) classifies it as Must-have, suggesting that for some sophisticated warehouse accounts, bin-level visibility is already an expectation.

**Verdict:** Priority 3 placement is validated. This is a differentiation opportunity once the Must-have foundation (Stock Transfers, Low Stock, Audit Trail) is in place. Don't let it block earlier priorities.

---

#### 9. Item Images / Item Visualization
**Classification: Attractive** | CS: 0.64 | DS: -0.18

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 0 | 0 | 1 | 1 |
| PS Team | 1 | 1 | 4 | 2 |
| Customer | 0 | 0 | 1 | 0 |

The DS of -0.18 is the lowest in the dataset — respondents barely notice when it's absent. The CS of 0.64 shows it delights when present. This is a pure Attractive feature: low stakes, high upside. The 3 Indifferent responses (partners indifferent + 2 PS) confirm this isn't a segment-wide pain point.

**Verdict:** Priority 3 placement is validated. Good low-risk delight feature, but deprioritize below any Must-have gaps.

---

#### 10. Reorder Line Items in Transactions
**Classification: Indifferent** | CS: 0.27 | DS: -0.45

| Group | M | O | A | I |
|---|:---:|:---:|:---:|:---:|
| Partners | 2 | 0 | 0 | 0 |
| PS Team | 1 | 2 | 1 | 4 |
| Customer | 0 | 0 | 0 | 1 |

The clearest Indifferent result in the survey. Five PS respondents are neutral either way. The CS of 0.27 is the lowest in the dataset, meaning even when present, this feature doesn't move the needle. The 2 Partner Must-have responses are the outlier and likely reflect power users who do significant manual transaction work — not the majority workflow.

**Verdict:** This feature is currently in Priority 2 as "Dynamic Item Management in Transactions." The Kano data does not support that prioritization. Recommend deferring to Priority 3 or cutting entirely in favor of higher-signal items. The DS of -0.45 is not high enough to justify build investment ahead of Audit Trail, Packing Slips, or Price Variations.

---

## Segment Analysis

### Partners vs. PS Team vs. Customer

Partners consistently classified features as Must-have. Of 20 partner classifications, 14 were Must-have (70%). This is expected: partners set customer expectations and have internalized what their accounts demand — they don't distinguish between "nice to have" and "required" when they're the ones fielding support calls.

PS team responses were more differentiated, which makes their data the most analytically useful. They have direct exposure to a wide range of MWD accounts across industries and complexity tiers, giving them calibrated intuitions about what's actually painful vs. aspirational.

| Feature | Partners | PS Team (plurality) | Customer |
|---|---|---|---|
| Stock Transfers | Must-have | One-dimensional | Must-have |
| Low Stock Alerts | Must-have | One-dimensional | Must-have |
| Backorder Support | Must-have | Split A/O | Attractive |
| Bin Tracking | Split M/A | Attractive | Indifferent |
| Reorder Line Items | Must-have | Indifferent | Indifferent |
| Item Images | Split I/A | Attractive | Attractive |
| Audit Trail | Must-have | Must-have | Attractive |
| Packing Slips | Split I/M | Must-have | Attractive |
| Price Variations | Split M/A | One-dimensional | Indifferent |
| Serial Number | Split M/A | Split M/A | Indifferent |

The divergence on Reorder Line Items is the starkest: partners see it as Must-have, PS team sees it as Indifferent. This suggests partner feedback on this feature may be based on their own workflow preferences rather than their customers' expressed pain.

---

## Roadmap Validation

### Current Priority vs. Kano Classification

| Feature | Current Priority | Kano Classification | Verdict |
|---|---|---|---|
| Stock Transfers | Priority 1 | Must-have | ✅ Validated |
| Low Stock Alerts / Reorder Points | Priority 1 | Must-have | ✅ Validated |
| Third-Party Integration (Katana/SOS) | Priority 1 | Not surveyed | — |
| Backorder Awareness | Priority 2 | Split (M/O/A) | ✅ Validated |
| Dynamic Item Management (Reorder Line Items) | Priority 2 | Indifferent | ⚠️ Over-prioritized |
| Bin / Sub-location Tracking | Priority 3 | Attractive | ✅ Validated |
| Item Images | Priority 3 | Attractive | ✅ Validated |
| Audit Trail | Priority 3 | **Must-have** | 🔴 Under-prioritized |
| Packing Slips | Not in roadmap | **Must-have** | 🔴 Roadmap gap |
| Price Variations | Not in roadmap | One-dimensional | ⚠️ Potential gap |
| Serial Number Tracking | Not in roadmap | Must-have / Attractive | ⚠️ Segment-specific gap |

### Key Calls

**🔴 Audit Trail needs to move up.** It's the highest-conviction Must-have finding that contradicts the current roadmap. Six of eleven respondents classify it as a baseline expectation. The DS score of -0.73 is the third highest in the survey. The rationale for Priority 3 placement was likely that it's "operational" rather than "customer-facing" — but this data challenges that framing. For MWD merchants with fragile, complex inventory systems, the ability to reconstruct what happened is not a nice-to-have.

**🔴 Packing Slips should enter the backlog.** This is not in scope at all, but scores higher on dissatisfaction potential than Item Images, Bin Tracking, and Reorder Line Items — all of which are in scope. Before adding it, resolve the QBO ownership question and the single Reverse response.

**⚠️ Dynamic Item Management / Reorder Line Items should be deprioritized.** The data does not support Priority 2 placement. It is the lowest-performing feature in the survey on CS (0.27). The partner Must-have responses appear to reflect partner preferences, not customer pain. If keeping it in scope, push to Priority 3.

**⚠️ Price Variations warrants a strategic conversation.** At CS 0.64 / DS 0.64, this is the strongest competitive differentiator not in the roadmap. Surfacing customer-specific pricing at the order entry moment is directly aligned with the product thesis. This doesn't have to be native pricing rules — it could be surfacing existing QBO price levels within Method's transaction view. Low build cost, high satisfaction impact.

---

## Recommendations

### Immediate Roadmap Actions

1. **Elevate Audit Trail to Priority 2.** The Kano signal is clear. Consider pairing it with the Stock Transfers release since both address multi-location operational accountability.

2. **Investigate Packing Slips.** Run a focused discovery session with 3–5 PS team members to understand: (a) whether customers are asking for this, (b) whether QBO already satisfies this need, and (c) what the right Method role is. Add to the backlog pending findings.

3. **Deprioritize Reorder Line Items.** Move from Priority 2 to Priority 3 or defer entirely. Free up the capacity for Audit Trail or Packing Slips investigation.

4. **Add Price Variations discovery to the roadmap.** Don't build yet, but define the MVP scope. Start with surfacing QBO price levels in Method transaction views — this is likely low-cost and high-impact.

### Survey Limitations & Next Steps

- **Expand customer sample size.** One customer respondent is not sufficient for statistical confidence. Run a broader survey with 10–20 active MWD customers segmented by manufacturer, distributor, and hybrid.
- **Segment by account type.** The next survey should filter results by manufacturing vs. distribution vs. hybrid. Serial number tracking and bin-level tracking will likely split cleanly across these segments.
- **Follow up on Serial Number Tracking.** The M/A tie suggests segment dependency. Identify which accounts in the PS team's portfolio actively use serial numbers and validate with those customers directly.

---

*Kano evaluation table applied: Functional × Dysfunctional response pairs mapped using the standard 5-option Kano classification matrix. CS = (A + O) / (A + O + M + I). DS = −(O + M) / (A + O + M + I). Reverse and Questionable responses excluded from coefficient calculations.*
