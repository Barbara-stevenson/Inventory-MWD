# MWD Company Research Scripts

This folder contains Python scripts used to research and enrich the top 200 MWD customer accounts by LTV (Lifetime Value).

## Main Scripts

### `generate_top_200_csv.py` ⭐ RECOMMENDED
**Purpose:** Generates CSV with ONLY the top 200 researched companies.

**What it does:**
- Reads `MWD Raw accounts data.csv`
- Sorts companies by LTV (SAAS Amount to Date) in descending order
- Takes **only the top 200** companies
- Merges with research data from `company_research_data.py`
- Outputs `MWD_Top_200_Enriched.csv` (200 rows, all researched)

**Output:** Clean dataset with 200 companies, all with complete research data.

**How to run:**
```bash
cd "MWD Team /Research Scripts"
python3 generate_top_200_csv.py
```

### `generate_enriched_csv.py`
**Purpose:** Generates enriched CSV for ALL 1,204 companies (top 200 researched, rest pending).

**What it does:**
- Reads `MWD Raw accounts data.csv`
- Sorts companies by LTV (SAAS Amount to Date) in descending order
- Merges with research data from `company_research_data.py`
- Outputs `MWD_Enriched_Accounts.csv` with 5 additional research columns:
  - Industry (Research)
  - Workflow Type
  - Company Description
  - Product Types
  - Product Complexity

**Note:** This outputs all 1,204 companies. Only top 200 have research; remaining 1,004 show "PENDING RESEARCH".

**How to run:**
```bash
cd "MWD Team /Research Scripts"
python3 generate_enriched_csv.py
```

### `merge_research_batches.py`
**Purpose:** Merges batch research files into the main research database.

**What it does:**
- Loads `company_research_data.py` (main database)
- Loads a batch file from `Batch Files/` directory
- Merges the batch data into the main database
- Writes updated `company_research_data.py`

**How to use:**
1. Edit the script to specify which batch file to load (lines 20-24)
2. Run the script to merge that batch
3. Run `generate_enriched_csv.py` to update the CSV output

**How to run:**
```bash
cd "MWD Team/Research Scripts"
python3 merge_research_batches.py
```

### `company_research_data.py`
**Purpose:** Main database storing all company research data.

**Structure:**
```python
COMPANY_RESEARCH = {
    "Company Name": {
        "industry": "...",
        "workflow_type": "...",
        "company_description": "...",
        "product_types": "...",
        "product_complexity": "..."
    },
    # ... 199 companies total
}
```

**Status:** Contains 199 companies (top 200 by LTV, all researched)

### `batch_research_tracker.py`
**Purpose:** Legacy tracker script (archived).

## Batch Files Directory

The `Batch Files/` subdirectory contains:
- **20 batch files** (`update_research_batch_1_10.py` through `update_research_batch_191_200.py`)
  - Each contains research for 10 companies
  - Organized by LTV ranking (companies 1-10, 11-20, etc.)

- **`update_dewesoft.py`** - Special update file for DEWESoft LLC (ranked #3 by LTV)

## Research Methodology

Each company was researched using:
1. Company website analysis
2. Google web searches
3. LinkedIn company profiles
4. Industry databases

Data collected includes:
- **Industry:** Specific industry vertical and product category
- **Workflow Type:** Business model and operational approach
- **Company Description:** Location, size, history, key differentiators
- **Product Types:** Detailed product/service catalog
- **Product Complexity:** Complexity rating with key technical capabilities

## Project Status

✅ **Complete:** All 200 companies researched (100%)
- Database: 199 unique companies
- CSV enriched entries: 222 (due to company name variations)

## Legacy Files

### `enrich_mwd_accounts.py`
Early prototype script, superseded by `generate_enriched_csv.py`. Kept for reference.
