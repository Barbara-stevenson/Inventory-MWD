#!/usr/bin/env python3
"""
Analyze product categories and complexity across top 5 industries.
Creates hierarchical product taxonomy and maps complexity drivers.
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter

def extract_complexity_level(complexity_str):
    """Extract complexity level from complexity string."""
    if not complexity_str:
        return "Unknown"

    # Extract first part before dash
    parts = complexity_str.split(' - ')
    if parts:
        level = parts[0].strip()
        if level in ['Very High', 'High', 'Medium-High', 'Medium', 'Low']:
            return level
    return "Unknown"

def categorize_products(product_str, industry_desc):
    """Categorize products based on keywords and patterns."""
    if not product_str:
        return []

    product_lower = product_str.lower()
    industry_lower = industry_desc.lower() if industry_desc else ""

    categories = []

    # Material Handling Equipment
    if any(kw in product_lower for kw in ['forklift', 'pallet jack', 'pallet truck', 'roll mover', 'conveyor', 'material handling', 'lift table', 'cart mover']):
        categories.append("Material Handling Equipment")

    # Manufacturing Machinery
    if any(kw in product_lower for kw in ['cnc', 'machine tool', 'welding', 'fabrication', 'lathe', 'mill', 'drilling', 'machining']):
        categories.append("Manufacturing Machinery & Tools")

    # Hydraulic & Pneumatic Systems
    if any(kw in product_lower for kw in ['hydraulic', 'pneumatic', 'compressor', 'pump', 'cylinder', 'valve', 'fluid power']):
        categories.append("Hydraulic & Pneumatic Systems")

    # Security Equipment
    if any(kw in product_lower for kw in ['safe', 'vault', 'security', 'access control', 'surveillance', 'lock']):
        categories.append("Security & Access Control Equipment")

    # Medical Devices & Equipment
    if any(kw in product_lower for kw in ['medical device', 'fda', 'therapy', 'diagnostic', 'surgical', 'clinical']):
        categories.append("Medical Devices & Clinical Equipment")

    # Medical Supplies & Distribution
    if any(kw in product_lower for kw in ['ppe', 'glove', 'mask', 'gown', 'medical supply', 'catheter', 'iv supply', 'surgical instrument']):
        categories.append("Medical Supplies & PPE")

    # Construction Equipment & Parts
    if any(kw in product_lower for kw in ['excavator', 'loader', 'bulldozer', 'backhoe', 'construction equipment', 'heavy machinery']):
        categories.append("Construction Equipment & Heavy Machinery")

    # Building Materials
    if any(kw in product_lower for kw in ['flooring', 'tile', 'stone', 'concrete', 'lumber', 'window', 'door', 'roofing', 'kitchen', 'bath']):
        categories.append("Building Materials & Finishes")

    # Greenhouses & Outdoor Structures
    if any(kw in product_lower for kw in ['greenhouse', 'chicken coop', 'shed', 'outdoor structure', 'enclosure']):
        categories.append("Greenhouses & Outdoor Structures")

    # Data Acquisition & Test Equipment
    if any(kw in product_lower for kw in ['data acquisition', 'daq', 'test equipment', 'measurement', 'sensor', 'instrumentation']):
        categories.append("Data Acquisition & Test Equipment")

    # Electronics & Components
    if any(kw in product_lower for kw in ['electronic', 'component', 'circuit', 'semiconductor', 'pcb', 'memory', 'data storage']):
        categories.append("Electronics & Components")

    # IoT & Software Systems
    if any(kw in product_lower for kw in ['iot', 'smart home', 'software', 'platform', 'telematics', 'tracking', 'gps', 'fleet management']):
        categories.append("IoT & Software Systems")

    # Lighting Equipment
    if any(kw in product_lower for kw in ['led', 'lighting', 'lamp', 'illumination', 'light therapy']):
        categories.append("Lighting Equipment")

    # Sporting Goods
    if any(kw in product_lower for kw in ['mat', 'football', 'sporting', 'athletic', 'gym', 'fitness', 'training']):
        categories.append("Sporting Goods & Athletic Equipment")

    # Furniture & Home Goods
    if any(kw in product_lower for kw in ['furniture', 'desk', 'chair', 'table', 'cabinet', 'office furniture']):
        categories.append("Furniture & Office Equipment")

    # Pool & Spa Equipment
    if any(kw in product_lower for kw in ['pool', 'spa', 'cover', 'aquamatic']):
        categories.append("Pool & Spa Equipment")

    # If no categories matched, return "Other"
    if not categories:
        categories.append("Other/Specialized Products")

    return categories

def analyze_complexity_drivers(complexity_str):
    """Extract complexity drivers from complexity description."""
    if not complexity_str:
        return []

    drivers = []
    comp_lower = complexity_str.lower()

    # Regulatory
    if any(kw in comp_lower for kw in ['fda', 'regulated', 'compliance', 'certification', 'military-grade', 'astm', 'ul ']):
        drivers.append("Regulatory Compliance")

    # Custom/MTO
    if any(kw in comp_lower for kw in ['custom', 'made-to-order', 'bespoke', 'handcraft', 'tailored']):
        drivers.append("Custom/Made-to-Order")

    # SKU Proliferation
    if any(kw in comp_lower for kw in ['sku', '000+', '000 sku', 'multi-brand', 'catalog']):
        drivers.append("SKU Proliferation")

    # Technical Complexity
    if any(kw in comp_lower for kw in ['advanced', 'proprietary', 'technology', 'software', 'precision', 'engineering']):
        drivers.append("Technical Complexity")

    # Supply Chain
    if any(kw in comp_lower for kw in ['international', 'multi-location', 'distribution', 'sourcing']):
        drivers.append("Supply Chain Complexity")

    return drivers if drivers else ["Standard Operations"]

def main():
    # Load extracted data
    data_path = Path(__file__).parent.parent / 'product_data_extraction.json'
    output_path = Path(__file__).parent.parent / 'product_category_analysis.json'

    print("Loading product data...")
    with open(data_path, 'r', encoding='utf-8') as f:
        industry_data = json.load(f)

    # Analyze each industry
    analysis = {}

    for industry_name, companies in industry_data.items():
        print(f"\nAnalyzing {industry_name}...")

        # Track product categories
        category_companies = defaultdict(list)
        complexity_distribution = Counter()
        complexity_drivers_count = Counter()

        for company in companies:
            # Categorize products
            categories = categorize_products(company['product_types'], company['industry_description'])

            for cat in categories:
                category_companies[cat].append(company['company_name'])

            # Extract complexity
            complexity_level = extract_complexity_level(company['complexity'])
            complexity_distribution[complexity_level] += 1

            # Analyze drivers
            drivers = analyze_complexity_drivers(company['complexity'])
            for driver in drivers:
                complexity_drivers_count[driver] += 1

        # Sort categories by frequency
        sorted_categories = sorted(category_companies.items(), key=lambda x: len(x[1]), reverse=True)

        analysis[industry_name] = {
            'total_companies': len(companies),
            'product_categories': {
                cat: {
                    'count': len(comps),
                    'companies': comps[:5]  # Top 5 examples
                }
                for cat, comps in sorted_categories
            },
            'complexity_distribution': dict(complexity_distribution),
            'complexity_drivers': dict(complexity_drivers_count.most_common())
        }

        print(f"  Categories identified: {len(sorted_categories)}")
        print(f"  Complexity levels: {dict(complexity_distribution)}")

    # Save analysis
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Analysis complete! Saved to: {output_path}")

    # Print summary
    print("\n" + "="*80)
    print("PRODUCT CATEGORY ANALYSIS SUMMARY")
    print("="*80)

    for industry_name, data in analysis.items():
        print(f"\n{industry_name}")
        print(f"  Total Companies: {data['total_companies']}")
        print(f"  Product Categories: {len(data['product_categories'])}")
        print(f"\n  Top Product Categories:")
        for i, (cat, info) in enumerate(list(data['product_categories'].items())[:5], 1):
            print(f"    {i}. {cat}: {info['count']} companies")

        print(f"\n  Complexity Distribution:")
        for level, count in sorted(data['complexity_distribution'].items(),
                                   key=lambda x: {'Very High': 4, 'High': 3, 'Medium-High': 2, 'Medium': 1, 'Unknown': 0}.get(x[0], 0),
                                   reverse=True):
            pct = (count / data['total_companies'] * 100) if data['total_companies'] > 0 else 0
            print(f"    {level}: {count} ({pct:.1f}%)")

        print(f"\n  Top Complexity Drivers:")
        for i, (driver, count) in enumerate(list(data['complexity_drivers'].items())[:3], 1):
            print(f"    {i}. {driver}: {count} companies")

if __name__ == '__main__':
    main()
