#!/usr/bin/env python3
"""
Enrich MWD accounts data with company research from Google.
Processes companies ordered by LTV (SAAS Amount to Date).
"""

import csv
import json
import time
from pathlib import Path

def clean_saas_amount(value):
    """Convert SAAS Amount to float for sorting."""
    if not value or value == '0':
        return 0.0
    # Remove commas and convert to float
    try:
        return float(value.replace(',', ''))
    except:
        return 0.0

def load_and_sort_accounts(csv_path):
    """Load CSV and sort by SAAS Amount to Date (LTV) descending."""
    accounts = []

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['_saas_amount_numeric'] = clean_saas_amount(row.get('SAAS Amount to Date', '0'))
            accounts.append(row)

    # Sort by SAAS Amount descending
    accounts.sort(key=lambda x: x['_saas_amount_numeric'], reverse=True)

    return accounts

def main():
    csv_path = Path('MWD Team /MWD Raw accounts data.csv')
    accounts = load_and_sort_accounts(csv_path)

    print(f"Loaded {len(accounts)} accounts")
    print(f"\nTop 10 accounts by LTV:")
    for i, acc in enumerate(accounts[:10], 1):
        company = acc.get('Company Name in QB', 'N/A')
        ltv = acc.get('SAAS Amount to Date', '0')
        website = acc.get('Website', 'N/A')
        print(f"{i}. {company}: ${ltv} - {website}")

    # Save sorted list for reference
    output_path = Path('MWD Team /sorted_accounts.json')
    with open(output_path, 'w') as f:
        json.dump(accounts[:100], f, indent=2)  # Save top 100 for now

    print(f"\nSaved top 100 accounts to {output_path}")

if __name__ == '__main__':
    main()
