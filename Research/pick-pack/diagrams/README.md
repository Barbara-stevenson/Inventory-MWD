# Pick/Pack Workflow Diagrams - Top 4 Competitors

This directory contains comprehensive Mermaid flowchart diagrams for pick/pack workflows from four leading inventory management competitors, plus a detailed comparison overview.

## Files Included

### 1. **fishbowl-pick-pack-flow.md**
Fishbowl Inventory's complete 12-step pick process + 8-step pack process.

**Key Features:**
- Color-coded availability states (Red/Yellow/Green)
- 4 pick status options (Hold/Start/Commit/Finish)
- 3 picking methods (Individual/Batch/Wave + location-sorted)
- Carton configuration and per-carton packing slips
- Additional documents (BOL, commercial invoices, RMA slips)

**Best For:** Manufacturing, wholesale distributors, batch picking operations

### 2. **katana-pick-pack-flow.md**
Katana MRP's mobile-first picking workflow with automatic task assignment.

**Key Features:**
- SO status progression (Not Shipped → Ready for Packing → In Progress → Packed → Delivered)
- Automatic task assignment to first operator
- Mobile Warehouse App (primary interface)
- Visual indicators: Green (full pick) / Yellow (partial pick)
- Integrated picking and packing
- Batch/serial number tracking

**Best For:** Small manufacturers, e-commerce, mobile-first operations

### 3. **cin7-pick-pack-flow.md**
DEAR/Cin7 Core's formal three-stage sequential workflow.

**Key Features:**
- 3 mandatory stages: Pick → Pack → Ship
- Directed vs. Free-form picking options
- Configurable pack stage (manual or automatic)
- Automatic backorder creation for partial picks
- Multi-box shipping support
- WMS-based picking with bin location optimization

**Best For:** Formal warehouse operations, multi-location fulfillment, WMS users

### 4. **comparison-overview.md**
Comprehensive side-by-side comparison of all three competitors.

**Contents:**
- High-level workflow diagrams (all 4 systems)
- Sales order status progression state diagrams
- Detailed comparison table (18 characteristics)
- Picking method comparison
- Mandatory vs. optional process flows
- Partial fulfillment approach comparison
- Document generation specifications
- Operational maturity assumptions
- Key differentiators and pricing model impacts

## How to Use These Diagrams

### In GitHub/Markdown:
The diagrams are wrapped in Mermaid code fences and will render automatically in:
- GitHub markdown files
- GitLab markdown files
- Notion (with Mermaid plugin)
- Any Markdown preview that supports Mermaid

### In Other Tools:
1. Copy the Mermaid code from the flowchart section
2. Paste into [Mermaid Live Editor](https://mermaid.live)
3. Export as PNG, SVG, or PDF

### For Presentations:
- Use the high-level workflow diagram from comparison-overview.md
- Include the status progression diagrams to show process flow
- Reference the comparison table for feature analysis

## Key Insights

### Interface Strategy
- **Fishbowl**: Desktop-first (comprehensive, powerful, requires training)
- **Katana**: Mobile-first (simple, fast implementation, phone-native)
- **Cin7**: Web-based (flexible, WMS-standard, steeper learning curve)

### Picking Approach
- **Fishbowl**: Multiple methods (individual/batch/wave) optimized per operation
- **Katana**: Single mobile task-based method with auto assignment
- **Cin7**: Choice of directed (optimized) or free-form (flexible) picking

### Partial Fulfillment
- **Fishbowl**: Manual decision-making (wait/cancel/ship partial)
- **Katana**: Explicit "Pack Some" option with implicit backorder
- **Cin7**: Automatic backorder creation with manual reauthorization

### Complexity Spectrum
1. **Low**: Katana MRP (days to implement, simple workflows)
2. **Medium**: DEAR/Cin7 (weeks, WMS learning curve)
3. **High**: Fishbowl (months to tune, comprehensive configuration)

## Document Specifications

### Mermaid Diagrams Used
- **Flowchart TD (Top-Down)**: For pick/pack process flows
- **State Diagrams**: For sales order status progressions
- **Subgraphs**: For phase/stage grouping
- **Color Coding**: For visual distinction of statuses and decision points

### Color Convention
- **Green**: Happy path, successful completion
- **Yellow**: Alternate paths, partial fulfillment
- **Red**: Errors, holds, edge cases
- **Blue**: Process steps, standard operations
- **Purple/Pink**: Decision points, configurations

## Notes

- All diagrams based on official documentation and research as of March 2026
- Fishbowl diagrams cover Advanced and Warehouse editions
- Katana diagrams reflect Professional plan features
- Cin7 diagrams show Core WMS capabilities
- Comparison includes operational maturity assumptions and pricing model impacts
