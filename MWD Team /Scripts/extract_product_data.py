#!/usr/bin/env python3
"""
Extract product data for all 106 companies in top 5 industries.
Organize data for web research and analysis.
"""

import csv
import json
import sys
from pathlib import Path
from collections import defaultdict

# Import categorization function
sys.path.insert(0, str(Path(__file__).parent))
from generate_industry_analysis import categorize_company

def clean_ltv(value):
    """Convert LTV string to float."""
    if not value or value == '0':
        return 0.0
    try:
        return float(value.replace(',', ''))
    except:
        return 0.0

def main():
    csv_path = Path(__file__).parent.parent / 'MWD_Top_200_Enriched.csv'
    output_path = Path(__file__).parent.parent / 'product_data_extraction.json'

    # Top 5 industries
    top_5_categories = [
        "Industrial Equipment & Machinery",
        "Construction & Building Materials",
        "Medical & Healthcare",
        "Electronics & Technology",
        "Consumer Goods & Retail"
    ]

    # Extract data by industry
    industry_data = {cat: [] for cat in top_5_categories}

    print(f"Extracting product data from: {csv_path}")

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company_name = row.get('Company Name in QB', '').strip()
            industry = row.get('Industry (Research)', '').strip()
            product_types = row.get('Product Types', '').strip()
            complexity = row.get('Product Complexity', '').strip()
            website = row.get('Website', '').strip()
            ltv = clean_ltv(row.get('SAAS Amount to Date', '0'))
            workflow = row.get('Workflow Type', '').strip()

            if company_name and industry != 'PENDING RESEARCH':
                category = categorize_company(industry, product_types)

                if category in top_5_categories:
                    industry_data[category].append({
                        'company_name': company_name,
                        'industry_description': industry,
                        'product_types': product_types,
                        'complexity': complexity,
                        'website': website,
                        'ltv': ltv,
                        'workflow_type': workflow
                    })

    # Sort companies within each industry by LTV (descending)
    for category in top_5_categories:
        industry_data[category].sort(key=lambda x: x['ltv'], reverse=True)

    # Save to JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(industry_data, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\n✓ Product data extracted successfully!")
    print(f"Output saved to: {output_path}\n")

    print("Summary by Industry:")
    print("=" * 80)
    total_companies = 0
    total_ltv = 0

    for category in top_5_categories:
        companies = industry_data[category]
        cat_ltv = sum(c['ltv'] for c in companies)
        total_companies += len(companies)
        total_ltv += cat_ltv

        print(f"\n{category}")
        print(f"  Companies: {len(companies)}")
        print(f"  Total LTV: ${cat_ltv:,.2f}")
        print(f"  Avg LTV: ${cat_ltv/len(companies):,.2f}" if companies else "  Avg LTV: $0")

        # Show companies with and without websites
        with_website = sum(1 for c in companies if c['website'])
        without_website = len(companies) - with_website
        print(f"  With Website: {with_website} ({with_website/len(companies)*100:.1f}%)")
        print(f"  Without Website: {without_website}")

        # Show top 3 by LTV
        print(f"  Top 3 by LTV:")
        for i, company in enumerate(companies[:3], 1):
            has_website = "✓" if company['website'] else "✗"
            print(f"    {i}. {company['company_name']} - ${company['ltv']:,.2f} [Web: {has_website}]")

    print(f"\n{'='*80}")
    print(f"TOTAL: {total_companies} companies, ${total_ltv:,.2f} LTV")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    main()
