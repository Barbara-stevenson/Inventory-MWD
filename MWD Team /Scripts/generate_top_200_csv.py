#!/usr/bin/env python3
"""
Generate CSV with only the top 200 researched MWD companies by LTV.
"""

import csv
import sys
from pathlib import Path
from company_research_data import COMPANY_RESEARCH

def clean_saas_amount(value):
    """Convert SAAS Amount to float for sorting."""
    if not value or value == '0':
        return 0.0
    try:
        return float(value.replace(',', ''))
    except:
        return 0.0

def load_and_sort_accounts(csv_path):
    """Load CSV and sort by SAAS Amount to Date (LTV) descending."""
    accounts = []

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            row['_saas_amount_numeric'] = clean_saas_amount(row.get('SAAS Amount to Date', '0'))
            accounts.append(row)

    # Sort by SAAS Amount descending
    accounts.sort(key=lambda x: x['_saas_amount_numeric'], reverse=True)

    return accounts, fieldnames

def enrich_account(account, research_data):
    """Add research data to account."""
    company_name = account.get('Company Name in QB', '').strip()

    if company_name in research_data:
        research = research_data[company_name]
        account['Industry (Research)'] = research.get('industry', '')
        account['Workflow Type'] = research.get('workflow_type', '')
        account['Company Description'] = research.get('company_description', '')
        account['Product Types'] = research.get('product_types', '')
        account['Product Complexity'] = research.get('product_complexity', '')
    else:
        account['Industry (Research)'] = 'NOT RESEARCHED'
        account['Workflow Type'] = 'NOT RESEARCHED'
        account['Company Description'] = 'NOT RESEARCHED'
        account['Product Types'] = 'NOT RESEARCHED'
        account['Product Complexity'] = 'NOT RESEARCHED'

    return account

def main():
    # Paths relative to script location
    csv_path = Path(__file__).parent.parent / 'MWD Raw accounts data.csv'
    output_path = Path(__file__).parent.parent / 'MWD_Top_200_Enriched.csv'

    print(f"Loading accounts from {csv_path}...")
    accounts, original_fieldnames = load_and_sort_accounts(csv_path)

    print(f"Loaded {len(accounts)} accounts")
    print(f"Taking top 200 by LTV...")

    # Take only top 200
    top_200_accounts = accounts[:200]

    # Enrich accounts with research data
    enriched_accounts = []
    researched_count = 0

    for account in top_200_accounts:
        enriched = enrich_account(account, COMPANY_RESEARCH)
        enriched_accounts.append(enriched)

        company_name = account.get('Company Name in QB', '').strip()
        if company_name in COMPANY_RESEARCH:
            researched_count += 1

    # Define new fieldnames with research columns
    new_fieldnames = list(original_fieldnames) + [
        'Industry (Research)',
        'Workflow Type',
        'Company Description',
        'Product Types',
        'Product Complexity'
    ]

    # Write top 200 enriched CSV
    print(f"\nWriting top 200 enriched data to {output_path}...")
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()

        for account in enriched_accounts:
            # Remove the temp sorting field
            if '_saas_amount_numeric' in account:
                del account['_saas_amount_numeric']
            writer.writerow(account)

    print(f"✓ Top 200 enriched CSV created successfully!")

    print(f"\n📊 Summary:")
    print(f"   Total companies in output: 200")
    print(f"   Researched: {researched_count}")
    print(f"   Not researched: {200 - researched_count}")

    print(f"\n🔝 Top 10 companies by LTV:")
    for i, acc in enumerate(enriched_accounts[:10], 1):
        company = acc.get('Company Name in QB', 'N/A')
        ltv = acc.get('SAAS Amount to Date', '0')
        research_status = "✓ RESEARCHED" if company in COMPANY_RESEARCH else "✗ NOT RESEARCHED"
        print(f"{i}. {company}: ${ltv} {research_status}")

if __name__ == '__main__':
    main()
