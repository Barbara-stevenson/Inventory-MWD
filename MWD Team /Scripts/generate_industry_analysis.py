#!/usr/bin/env python3
"""
Generate industry grouping analysis for top 200 MWD companies.
Outputs comprehensive markdown report with categorization and statistics.
"""

import csv
from pathlib import Path
from collections import defaultdict
import re

def clean_ltv(value):
    """Convert LTV string to float."""
    if not value or value == '0':
        return 0.0
    try:
        return float(value.replace(',', ''))
    except:
        return 0.0

def categorize_company(industry, product_types):
    """
    Categorize company based on industry and product keywords.
    Returns category name.
    """
    industry_lower = industry.lower()
    product_lower = product_types.lower() if product_types else ""

    # Special case: if industry is ambiguous, try categorizing by product types
    if 'multiple companies' in industry_lower or 'requires clarification' in industry_lower:
        # Try to categorize based on product types instead
        if product_lower:
            # Medical products
            if any(keyword in product_lower for keyword in ['medical', 'healthcare', 'cpap', 'respiratory', 'hospital', 'surgical', 'pharmaceutical']):
                return "Medical & Healthcare"
            # Industrial/Conveyor products
            if any(keyword in product_lower for keyword in ['conveyor', 'industrial', 'machinery', 'hydraulic', 'pneumatic']):
                return "Industrial Equipment & Machinery"
            # Electronics/AV products
            if any(keyword in product_lower for keyword in ['audio', 'video', 'av equipment', 'camera', 'electronic', 'switcher', 'amplifier']):
                return "Electronics & Technology"
            # If still can't categorize from products, will fall through to default

    # Medical & Healthcare
    if any(keyword in industry_lower for keyword in ['medical', 'healthcare', 'pharmaceutical', 'hospital', 'surgical', 'health', 'bioscience', 'biotech', 'mobility equipment', 'accessibility', 'wheelchair', 'stair lift']):
        return "Medical & Healthcare"

    # Laboratory & Scientific Equipment
    if any(keyword in industry_lower for keyword in ['laboratory', 'scientific', 'analytical', 'lab instrument', 'proteomics', 'research products', 'life sciences']):
        return "Laboratory & Scientific Equipment"

    # Construction & Building Materials
    if any(keyword in industry_lower for keyword in ['construction', 'building', 'concrete', 'flooring', 'stone', 'tile', 'lumber', 'window', 'door', 'roofing', 'kitchen', 'bath']):
        return "Construction & Building Materials"

    # Industrial Equipment & Machinery
    if any(keyword in industry_lower for keyword in ['industrial', 'machinery', 'equipment manufacturing', 'forklift', 'conveyor', 'material handling', 'welding', 'fabrication', 'machine tool', 'cnc', 'vacuum pump', 'compressor', 'blower', 'hydraulic', 'pneumatic', 'fluid power']):
        return "Industrial Equipment & Machinery"

    # Tools & Hardware
    if any(keyword in industry_lower for keyword in ['tool', 'grinding', 'hardware', 'assembly tool', 'fastener', 'industrial tool']):
        return "Tools & Hardware"

    # Electronics & Technology
    if any(keyword in industry_lower for keyword in ['data acquisition', 'electronic', 'technology', 'software', 'iot', 'smart home', 'fiber optic', 'audio visual', 'av equipment', 'computer memory', 'data storage', 'telecommunications', 'push-to-talk']):
        return "Electronics & Technology"

    # Lighting & Stage Equipment
    if any(keyword in industry_lower for keyword in ['led light', 'lighting', 'theatrical', 'stage', 'rigging', 'lamp', 'led ', ' led', 'illumination']):
        return "Lighting & Stage Equipment"

    # Automotive & Fleet
    if any(keyword in industry_lower for keyword in ['automotive', 'fleet', 'vehicle', 'truck', 'car', 'forklift sales']):
        return "Automotive & Fleet"

    # Energy & Environmental
    if any(keyword in industry_lower for keyword in ['energy', 'hvac', 'heating', 'cooling', 'solar', 'insulation', 'renewable', 'environmental', 'pool', 'water treatment', 'hydrological', 'filtration', 'wastewater']):
        return "Energy & Environmental"

    # Fuel & Gas Distribution
    if any(keyword in industry_lower for keyword in ['petroleum', 'fuel', 'gas distribution', 'co2', 'carbon dioxide', 'dry ice']):
        return "Fuel & Gas Distribution"

    # Chemicals & Industrial Supplies
    if any(keyword in industry_lower for keyword in ['chemical', 'agrichemical', 'industrial chemical', 'gasket', 'seal', 'o-ring']):
        return "Chemicals & Industrial Supplies"

    # Food & Beverage
    if any(keyword in industry_lower for keyword in ['food', 'beverage', 'nutraceutical', 'dietary supplement', 'botanical', 'hop', 'brewery', 'cocktail', 'drink', 'coffee', 'tea', 'confection']):
        return "Food & Beverage"

    # Agriculture & Outdoor
    if any(keyword in industry_lower for keyword in ['agriculture', 'agricultural', 'farm', 'greenhouse', 'outdoor', 'landscape', 'lawn', 'garden', 'irrigation']):
        return "Agriculture & Outdoor"

    # Textiles & Apparel
    if any(keyword in industry_lower for keyword in ['textile', 'fabric', 'apparel', 'embroidery', 'clothing', 'linen', 'hair', 'garment']):
        return "Textiles & Apparel"

    # Security & Access Control
    if any(keyword in industry_lower for keyword in ['security', 'access control', 'gate control', 'safe', 'vault', 'shadow board', 'foam inlay']):
        return "Security & Access Control"

    # Promotional Products & Awards
    if any(keyword in industry_lower for keyword in ['promotional', 'award', 'recognition', 'commemorative', 'deal toy', 'heat transfer']):
        return "Promotional Products & Awards"

    # Fitness & Wellness
    if any(keyword in industry_lower for keyword in ['fitness', 'wellness', 'rehabilitation', 'gym equipment']):
        return "Fitness & Wellness"

    # Defense & Firearms
    if any(keyword in industry_lower for keyword in ['firearm', 'gun', 'defense', 'weapon']):
        return "Defense & Firearms"

    # Specialty Manufacturing (catch custom/niche manufacturing)
    if any(keyword in industry_lower for keyword in ['custom', 'bespoke', 'handcraft', 'specialty', 'niche']):
        return "Specialty Manufacturing"

    # Consumer Goods & Retail
    if any(keyword in industry_lower for keyword in ['retail', 'consumer', 'furniture', 'piano', 'musical', 'sporting', 'toy', 'gift', 'luxury', 'golf', 'recreation', 'cannabis', 'dispensary']):
        return "Consumer Goods & Retail"

    # Packaging & Printing
    if any(keyword in industry_lower for keyword in ['packaging', 'printing', 'label', 'display', 'signage', 'sign ', 'banner']):
        return "Packaging & Printing"

    # Professional Services
    if any(keyword in industry_lower for keyword in ['field service', 'machining service', 'welding service', 'grinding service', 'service solution']):
        return "Professional Services"

    # If still uncategorized, check for distribution/wholesale
    if 'distribution' in industry_lower or 'wholesale' in industry_lower or 'supply' in industry_lower:
        # Try to categorize based on product types
        if 'medical' in product_lower or 'healthcare' in product_lower:
            return "Medical & Healthcare"
        elif 'construction' in product_lower or 'building' in product_lower:
            return "Construction & Building Materials"
        else:
            return "Wholesale & Distribution (General)"

    # Default to Other
    return "Other/Uncategorized"

def main():
    # Paths
    csv_path = Path(__file__).parent.parent / 'MWD_Top_200_Enriched.csv'
    output_path = Path(__file__).parent.parent / 'MWD_Top_200_Industry_Analysis.md'

    print(f"Reading CSV from: {csv_path}")

    # Read and categorize companies
    companies = []
    total_ltv = 0

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company_name = row.get('Company Name in QB', '').strip()
            industry = row.get('Industry (Research)', '').strip()
            product_types = row.get('Product Types', '').strip()
            complexity = row.get('Product Complexity', '').strip()
            ltv = clean_ltv(row.get('SAAS Amount to Date', '0'))

            if company_name and industry != 'PENDING RESEARCH':
                category = categorize_company(industry, product_types)

                companies.append({
                    'name': company_name,
                    'industry': industry,
                    'product_types': product_types,
                    'complexity': complexity,
                    'ltv': ltv,
                    'category': category
                })
                total_ltv += ltv

    print(f"Loaded {len(companies)} companies")
    print(f"Total LTV: ${total_ltv:,.2f}")

    # Group by category
    categories = defaultdict(list)
    for company in companies:
        categories[company['category']].append(company)

    # Sort companies within each category by LTV
    for category in categories:
        categories[category].sort(key=lambda x: x['ltv'], reverse=True)

    # Sort categories by total LTV
    sorted_categories = sorted(categories.items(), key=lambda x: sum(c['ltv'] for c in x[1]), reverse=True)

    print(f"Categories created: {len(sorted_categories)}")

    # Count complexities across all companies
    complexity_counts = defaultdict(int)
    for company in companies:
        comp_level = company['complexity'].split(' - ')[0].strip() if company['complexity'] else "Unknown"
        complexity_counts[comp_level] += 1

    # Generate Markdown
    print(f"Generating markdown report...")

    md_lines = []
    md_lines.append("# Top 200 MWD Customer Industry Analysis\n")
    md_lines.append("## Executive Summary\n")
    md_lines.append(f"- **Total Companies:** {len(companies)}")
    md_lines.append(f"- **Total LTV:** ${total_ltv:,.2f}")
    md_lines.append(f"- **Average LTV:** ${total_ltv/len(companies):,.2f}" if companies else "- **Average LTV:** $0")
    md_lines.append(f"- **Industry Categories:** {len(sorted_categories)}")

    # Complexity overview
    very_high_pct = (complexity_counts.get('Very High', 0) / len(companies) * 100) if companies else 0
    high_pct = (complexity_counts.get('High', 0) / len(companies) * 100) if companies else 0
    medium_pct = ((complexity_counts.get('Medium-High', 0) + complexity_counts.get('Medium', 0)) / len(companies) * 100) if companies else 0
    md_lines.append(f"- **Complexity Overview:** {very_high_pct:.0f}% Very High, {high_pct:.0f}% High, {medium_pct:.0f}% Medium")
    md_lines.append("")

    # Industry Category Breakdown
    md_lines.append("## Industry Category Breakdown\n")

    for idx, (category_name, category_companies) in enumerate(sorted_categories, 1):
        category_ltv = sum(c['ltv'] for c in category_companies)
        avg_ltv = category_ltv / len(category_companies) if category_companies else 0

        md_lines.append(f"### {idx}. {category_name}\n")
        md_lines.append(f"- **Total Companies:** {len(category_companies)}")
        md_lines.append(f"- **Total LTV:** ${category_ltv:,.2f}")
        md_lines.append(f"- **Average LTV:** ${avg_ltv:,.2f} per company")

        # Complexity breakdown for this category
        cat_complexity = defaultdict(int)
        for comp in category_companies:
            comp_level = comp['complexity'].split(' - ')[0].strip() if comp['complexity'] else "Unknown"
            cat_complexity[comp_level] += 1

        md_lines.append(f"- **Product Complexity:**")
        if cat_complexity.get('Very High', 0) > 0:
            md_lines.append(f"  - Very High: {cat_complexity.get('Very High', 0)} companies")
        if cat_complexity.get('High', 0) > 0:
            md_lines.append(f"  - High: {cat_complexity.get('High', 0)} companies")
        if cat_complexity.get('Medium-High', 0) > 0:
            md_lines.append(f"  - Medium-High: {cat_complexity.get('Medium-High', 0)} companies")
        if cat_complexity.get('Medium', 0) > 0:
            md_lines.append(f"  - Medium: {cat_complexity.get('Medium', 0)} companies")
        md_lines.append("")

        # Top 5 companies
        top_companies = category_companies[:5]
        md_lines.append(f"**Top {min(5, len(category_companies))} Companies by LTV:**\n")
        for i, comp in enumerate(top_companies, 1):
            md_lines.append(f"{i}. **{comp['name']}** - ${comp['ltv']:,.2f} LTV")
            md_lines.append(f"   - Industry: {comp['industry']}")
            if comp['product_types']:
                # Truncate product types if too long
                products = comp['product_types'][:200] + "..." if len(comp['product_types']) > 200 else comp['product_types']
                md_lines.append(f"   - Products: {products}")
            comp_level = comp['complexity'].split(' - ')[0].strip() if comp['complexity'] else "Unknown"
            md_lines.append(f"   - Complexity: {comp_level}")
            md_lines.append("")

        # All companies in category
        md_lines.append(f"**All Companies in This Category:**")
        for comp in category_companies:
            md_lines.append(f"- {comp['name']} (${comp['ltv']:,.2f})")
        md_lines.append("\n---\n")

    # Summary Statistics
    md_lines.append("## Summary Statistics\n")
    md_lines.append("### Industry Distribution Table\n")
    md_lines.append("| Industry Category | Companies | Total LTV | Avg LTV | % of Total LTV |")
    md_lines.append("|-------------------|-----------|-----------|---------|----------------|")

    for category_name, category_companies in sorted_categories:
        category_ltv = sum(c['ltv'] for c in category_companies)
        avg_ltv = category_ltv / len(category_companies) if category_companies else 0
        pct_ltv = (category_ltv / total_ltv * 100) if total_ltv > 0 else 0
        md_lines.append(f"| {category_name} | {len(category_companies)} | ${category_ltv:,.2f} | ${avg_ltv:,.2f} | {pct_ltv:.1f}% |")

    md_lines.append("\n### Product Complexity Distribution\n")
    md_lines.append("| Complexity Level | Total Companies | % of Total |")
    md_lines.append("|------------------|-----------------|------------|")

    for comp_level in ['Very High', 'High', 'Medium-High', 'Medium', 'Unknown']:
        count = complexity_counts.get(comp_level, 0)
        pct = (count / len(companies) * 100) if companies else 0
        if count > 0:
            md_lines.append(f"| {comp_level} | {count} | {pct:.1f}% |")

    # Appendix
    md_lines.append("\n## Appendix\n")
    md_lines.append("### Methodology")
    md_lines.append("- **Data source:** MWD_Top_200_Enriched.csv")
    md_lines.append("- **Categorization:** Keyword-based analysis of 'Industry (Research)' field")
    md_lines.append("- **Grouping logic:** Pattern matching with fallback to product types")
    md_lines.append("- **LTV source:** 'SAAS Amount to Date' field")
    md_lines.append("")
    md_lines.append("### Notes")
    md_lines.append("- Companies sorted by LTV (descending) within each category")
    md_lines.append("- Product complexity extracted directly from research data")
    md_lines.append("- Some companies may operate across multiple categories but assigned to primary industry")
    md_lines.append("- Categories with similar themes may be combined for high-level overview")
    md_lines.append("")

    # Write markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    print(f"✓ Markdown report generated: {output_path}")
    print(f"\n📊 Summary:")
    print(f"   Companies analyzed: {len(companies)}")
    print(f"   Categories created: {len(sorted_categories)}")
    print(f"   Total LTV: ${total_ltv:,.2f}")

if __name__ == '__main__':
    main()
