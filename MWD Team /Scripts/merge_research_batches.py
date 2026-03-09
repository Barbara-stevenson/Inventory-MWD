#!/usr/bin/env python3
"""
Merge research batches into the main company_research_data.py file.
"""

import importlib.util
import sys
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent
batch_dir = script_dir / "Batch Files"

# Load the main research data
data_file = script_dir / "company_research_data.py"
spec = importlib.util.spec_from_file_location("company_research_data", data_file)
research_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(research_module)

# Load DEWESoft update
batch_file = batch_dir / "update_dewesoft.py"
spec_batch = importlib.util.spec_from_file_location("update_dewesoft", batch_file)
batch_module = importlib.util.module_from_spec(spec_batch)
spec_batch.loader.exec_module(batch_module)

# Merge the data
main_data = research_module.COMPANY_RESEARCH
batch_data = batch_module.DEWESOFT_DATA

print(f"Main research data: {len(main_data)} companies")
print(f"DEWESoft update data: {len(batch_data)} companies")

# Add batch data to main data
for company, data in batch_data.items():
    main_data[company] = data

print(f"Merged total: {len(main_data)} companies")

# Write back to the main file
output_file = script_dir / "company_research_data.py"
with open(output_file, "w") as f:
    f.write('#!/usr/bin/env python3\n')
    f.write('"""\n')
    f.write('Store research data for MWD companies.\n')
    f.write('This file will be progressively updated with company research.\n')
    f.write('"""\n\n')
    f.write('# Company research data - manually curated from web searches\n')
    f.write('COMPANY_RESEARCH = {\n')

    for company, data in sorted(main_data.items()):
        f.write(f'    "{company}": {{\n')
        for key, value in data.items():
            # Escape quotes in the value
            escaped_value = value.replace('"', '\\"')
            f.write(f'        "{key}": "{escaped_value}",\n')
        f.write('    },\n')

    f.write('}\n')

print("✓ Research data merged successfully!")
print(f"\nCompanies in database: {len(main_data)}")
