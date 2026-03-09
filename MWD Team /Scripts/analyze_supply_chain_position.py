#!/usr/bin/env python3
"""
Analyze top 200 enriched accounts to categorize their supply chain position
"""
import csv
import re
from collections import defaultdict

def categorize_account(row):
    """
    Categorize an account as Manufacturing, Wholesale, Distribution, or Hybrid
    based on multiple data points
    """
    company_name = row.get('Company Name in QB', '').lower()
    workflow_type = row.get('Workflow Type', '').lower()
    company_desc = row.get('Company Description', '').lower()
    product_types = row.get('Product Types', '').lower()
    industry = row.get('Industry (Research)', '').lower()

    # Score each category
    manufacturing_score = 0
    wholesale_score = 0
    distribution_score = 0

    # Manufacturing indicators
    manufacturing_keywords = [
        'manufactur', 'fabricat', 'assembl', 'produc', 'factory',
        'machining', 'welding', 'injection mold', 'cnc', 'casting',
        'extrusion', 'processing', 'custom build', 'made in', 'built in',
        'engineering', 'design and build', 'oem', 'proprietary'
    ]

    # Wholesale indicators
    wholesale_keywords = [
        'wholesal', 'distribut', 'supplier', 'bulk', 'import',
        'resell', 'vendor', 'dealer', 'broker', 'trading',
        'sourcing', 'procure', 'stock and sell', 'purchase and sell'
    ]

    # Distribution indicators
    distribution_keywords = [
        'distribution', 'logistics', 'fulfillment', 'warehouse',
        'shipping', 'delivery', 'supply chain', '3pl', 'freight',
        'transport', 'courier', 'nationwide', 'multi-location',
        'regional hub', 'service center network'
    ]

    # Combine all text for analysis
    all_text = f"{workflow_type} {company_desc} {product_types} {industry}"

    # Count keyword matches
    for keyword in manufacturing_keywords:
        if keyword in all_text:
            manufacturing_score += 1

    for keyword in wholesale_keywords:
        if keyword in all_text:
            wholesale_score += 1

    for keyword in distribution_keywords:
        if keyword in all_text:
            distribution_score += 1

    # Specific workflow type analysis
    if 'manufacturing' in workflow_type or 'production' in workflow_type:
        manufacturing_score += 3

    if 'wholesale' in workflow_type or 'bulk' in workflow_type:
        wholesale_score += 3

    if 'distribution' in workflow_type or 'fulfillment' in workflow_type:
        distribution_score += 3

    # Company description patterns
    if re.search(r'manufacturer (and|&) distributor', company_desc):
        return 'Manufacturing + Distribution'

    if re.search(r'manufacturer (and|&) supplier', company_desc):
        return 'Manufacturing + Wholesale'

    if re.search(r'wholesale (and|&) distribution', company_desc):
        return 'Wholesale + Distribution'

    if re.search(r'importer (and|&) distributor', company_desc):
        return 'Wholesale + Distribution'

    # Determine primary category
    max_score = max(manufacturing_score, wholesale_score, distribution_score)

    if max_score == 0:
        return 'Unclear'

    # Check for hybrid operations (multiple high scores)
    high_scores = []
    if manufacturing_score >= max_score - 1 and manufacturing_score > 0:
        high_scores.append('Manufacturing')
    if wholesale_score >= max_score - 1 and wholesale_score > 0:
        high_scores.append('Wholesale')
    if distribution_score >= max_score - 1 and distribution_score > 0:
        high_scores.append('Distribution')

    if len(high_scores) > 1:
        return ' + '.join(high_scores)
    elif high_scores:
        return high_scores[0]
    else:
        return 'Unclear'

def main():
    input_file = '/Users/johnmiranda/Documents/Sales Management/MWD Team /MWD_Top_200_Enriched.csv'
    output_file = '/tmp/claude/-Users-johnmiranda-Documents-Sales-Management/aa29808c-8971-4d81-96e9-c76091fa2cfa/scratchpad/mwd_categorized.csv'

    # Read and categorize
    accounts = []
    category_counts = defaultdict(int)

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = categorize_account(row)
            accounts.append({
                'Account Name': row.get('Account Name', ''),
                'Company Name': row.get('Company Name in QB', ''),
                'Vertical': row.get('Vertical', ''),
                'Industry': row.get('Industry (Research)', ''),
                'Workflow Type': row.get('Workflow Type', ''),
                'Company Description': row.get('Company Description', ''),
                'Supply Chain Position': category
            })
            category_counts[category] += 1

    # Write output
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Account Name', 'Company Name', 'Vertical', 'Industry',
                      'Workflow Type', 'Company Description', 'Supply Chain Position']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accounts)

    # Print summary
    print(f"\n=== SUPPLY CHAIN CATEGORIZATION SUMMARY ===")
    print(f"Total Accounts: {len(accounts)}\n")

    print("Category Breakdown:")
    for category in sorted(category_counts.keys()):
        count = category_counts[category]
        percentage = (count / len(accounts)) * 100
        print(f"  {category:40s}: {count:3d} accounts ({percentage:5.1f}%)")

    print(f"\nDetailed results saved to: {output_file}")

    # Print examples from each category
    print("\n=== EXAMPLES BY CATEGORY ===\n")

    categories_shown = set()
    for account in accounts:
        category = account['Supply Chain Position']
        if category not in categories_shown:
            categories_shown.add(category)
            print(f"{category}:")
            print(f"  Company: {account['Company Name']}")
            print(f"  Workflow: {account['Workflow Type']}")
            print(f"  Description: {account['Company Description'][:150]}...")
            print()

            if len(categories_shown) >= 10:  # Show first 10 categories
                break

if __name__ == '__main__':
    main()
