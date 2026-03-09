#!/usr/bin/env python3
"""
Batch update for companies 101-110 research data.
"""

BATCH_101_110 = {
    "TRASK PERFORMANCE": {
        "industry": "Motorcycle Performance Parts & Custom Builds",
        "workflow_type": "Full Service & Customization - Harley-Davidson Specialist",
        "company_description": "Founded 2000 by Nick Trask (New Zealand to USA following motorcycle passion), Phoenix, AZ (21601 N 3rd Ave). Arizona's premier service/dyno tune facility. New facility brings manufacturing, R&D, customer support under one roof. Made in USA. Certified instructors for installation/tuning/dyno testing.",
        "product_types": "High-performance motorcycle parts/accessories for Harley-Davidson: exhaust systems, turbo kits (all EFI Harley Davidsons), engine components, air cleaners, renowned turbo systems. Award-winning Assault Series custom V-Twin motorcycles. Trask Speed Shop comprehensive performance engine packages/custom builds. Certified training in proper installation, tuning, dyno testing of turbo kits.",
        "product_complexity": "Very High - Turbo system design/manufacturing for EFI Harley-Davidsons, award-winning custom V-Twin motorcycles, dyno tuning facility operations, performance engine package engineering, certified instructor training programs, R&D/manufacturing/customer support integration, USA production."
    },
    "Atlantic Graphic Systems, Inc": {
        "industry": "Printing Machinery Distribution - New & Pre-Owned",
        "workflow_type": "Sales & Service - Factory Trained Support",
        "company_description": "Established 1976, mid-Atlantic USA. 45+ years trusted supplier of quality new/certified pre-owned printing machinery. Factory trained service staff highly proficient in operation, mechanical/electronic repair. Serves mid-Atlantic graphics community with new/refurbished machinery, consumables, technical support.",
        "product_types": "New/certified pre-owned printing equipment: Epson printing equipment, Vanguard Digital Printing Systems VR6D-HS Flatbed LED UV printer, Xante Corporation (envelope printers, small format UV flatbeds), Komori presses/finishing pieces. Bindery/finishing equipment, material handling, paper cutting, press peripherals. Consumables, technical support.",
        "product_complexity": "High - 45+ years printing machinery expertise, new/certified pre-owned equipment requiring inspection/certification, multi-brand distribution (Epson/Vanguard/Xante/Komori), factory trained service staff, mechanical/electronic repair capabilities, mid-Atlantic regional operations, diverse equipment categories (printing/bindery/finishing/cutting)."
    },
    "HOUSTON HYDRAULIC": {
        "industry": "Hydraulic Components & Systems - Fluid Power Solutions",
        "workflow_type": "Distribution, Design & Service - Since 1945",
        "company_description": "Serving hydraulic needs since 1945, Houston, TX (8101 Pinemont Dr). Comprehensive fluid power solutions provider. 60+ years designing/manufacturing hydraulic power units for wide-range applications. Distribution, design, manufacturing, testing, implementation capabilities.",
        "product_types": "Hydraulic components from leading manufacturers: pumps, motors, cylinders, valves. Hydraulic power units (60+ years manufacturing). Design/build custom hydraulic systems. Repair/service: cylinders, pumps, motors, valves, components, complete systems. Technical design, manufacturing, testing, implementation services. Wide variety high-quality hydraulic components.",
        "product_complexity": "Very High - 60+ years hydraulic power unit design/manufacturing, comprehensive fluid power solutions, custom hydraulic system design/build, multi-component repair/service (cylinders/pumps/motors/valves), leading manufacturer distribution, technical design/testing/implementation capabilities, wide-ranging applications expertise."
    },
    "Custom Equipment Company, Inc.": {
        "industry": "Material Handling & Custom Packaging Solutions",
        "workflow_type": "Manufacturing & Distribution - Since 1978",
        "company_description": "Since 1978, United States operations. Custom packaging specialists pioneering collapsible, reusable containers/pallets for semi-bulk liquid/dry products. 40+ years experience, thousands of solutions implemented. Serves manufacturing, distribution, agriculture, aerospace. Authorized distributor multiple brands.",
        "product_types": "Pallets, containers, industrial shelving, ergonomic solutions. Collapsible reusable containers/pallets (semi-bulk liquid/dry products marketplace). Custom fabrication, container modifications, pallet rack repairs. Authorized distributor: Davco Metal Bulk Containers, Eagle Group Manufacturing, Jesco Self-Dumping Hoppers, LEWISBins Plastic Products, Little Giant Industrial Products, Metro Storage solutions. Material handling solutions tailored for industries.",
        "product_complexity": "High - 40+ years custom packaging innovation, pioneering collapsible/reusable container technology, semi-bulk liquid/dry products expertise, custom fabrication capabilities, multi-brand authorized distribution, diverse industry serving (manufacturing/distribution/agriculture/aerospace), thousands of implemented solutions, container modification/pallet rack repair services."
    },
    "SMITH Manufacturing (SSPS, Inc)": {
        "industry": "Surface Preparation Equipment Manufacturing - Pavement/Flooring",
        "workflow_type": "Manufacturing - Contractor Equipment Specialist",
        "company_description": "Pompano Beach, FL. Manufacturer of quality, cost-effective surface-preparation equipment/cutter tools for hard-working contractors. Maintains largest inventory of machines/consumable wear components. Helps contractors repair/maintain asphalt/concrete surfaces, achieve all 10 surface profiles.",
        "product_types": "Surface preparation equipment: scarifiers, planers, grinders, line removers, routers, groovers, shavers, scabblers, prep tools. Models: SPS8 compact scarifier (concrete/asphalt), LNX8 Rotary Eraser (marking removal, no grooves), SPS10/FS200 (powerful asphalt/concrete removal), FS150, FS351 (electric/propane/gasoline versions), crack routers. Consumable wear components. For striping, pavement, flooring contractors.",
        "product_complexity": "High - Surface preparation equipment design/manufacturing, largest inventory of machines/consumables, diverse equipment types (scarifiers/planers/grinders/routers/groovers/shavers/scabblers), multi-power options (electric/propane/gasoline), all 10 surface profile achievement, contractor-focused cost-effective solutions, asphalt/concrete specialization."
    },
    "Pacific Ergonomics": {
        "industry": "Ergonomic Office & Laboratory Furniture Distribution",
        "workflow_type": "Sales & Consulting - Complete Furniture Solutions",
        "company_description": "Escondido, CA (329 W Grand Ave, just outside San Diego). Ergonomic business furniture boutique with specialty solutions for offices, laboratories, manufacturing. Complete office furniture supplier and ergonomic consulting firm. Two divisions: Business Furniture Solutions and Ergonomic Services creating work environments blending style, productivity, health.",
        "product_types": "Office furniture: modern cubicles, reception desks, outdoor furniture, acoustical solutions, modular furniture, lounge furniture, desks/chairs (private offices, conference rooms, teamwork areas, customer spaces), adjustable desks, ergonomic chairs, keyboard trays, monitor arms. Laboratory furniture for startup/established labs. Soundproofing options, ergonomic seating, optimized workstation setups. Stylish contemporary furnishings done ergonomically. Design services for waiting areas, reception, executive spaces.",
        "product_complexity": "High - Ergonomic consulting expertise, dual service divisions (business furniture/ergonomic services), multi-category solutions (office/laboratory/manufacturing), acoustical/soundproofing design, adjustable/ergonomic equipment specialization, laboratory startup/established lab furnishing, comprehensive design services (reception/executive/workstations), San Diego regional operations."
    },
    "Pick on Us, LLC": {
        "industry": "Eco-Friendly Disposables - Restaurant & Hospitality Products",
        "workflow_type": "Manufacturing & Wholesale - Custom Branding",
        "company_description": "Provides eco-friendly disposables elevating presentation, delighting guests, protecting planet. Serves restaurants, hotels, caterers at wholesale prices. Contact: 760-597-0276 M-F 8am-4pm PST, info@pickonus.com. Notable clients: Ketel One Vodka, MGM Resorts International, Ruth's Chris Steakhouse. Supplies stadiums, airlines, cruise lines, large travel/entertainment venues.",
        "product_types": "Eco-friendly disposables: customizable burger picks/skewers, drink stirrers, paper straws, bamboo tableware, earth friendly to-go containers, toothpicks, popsicle sticks, napkins, coffee cups. Custom branding services (online design tool or art team assistance - logos/text). Bamboo custom skewers/toothpicks, fancy toothpicks. www.pickonus.com ordering.",
        "product_complexity": "Medium-High - Eco-friendly product sourcing, custom branding online design tool, art team assistance, bamboo tableware manufacturing, large venue supply logistics (stadiums/airlines/cruise lines), wholesale pricing operations, iconic brand clientele (Ketel One/MGM/Ruth's Chris), earth-friendly to-go container development."
    },
    "Flow-Turn Inc": {
        "industry": "Powered Belt Curves & Spiral Conveyors Manufacturing",
        "workflow_type": "Global Manufacturing - Since 1980",
        "company_description": "Founded 1980, Union, NJ. Global manufacturer of powered belt curves and spiral conveyors. Dedicated to delivering simple, efficient, reliable products to diverse national/international customers. Distribution/fulfillment centers, packaging/parcel facilities, airports installations.",
        "product_types": "Belt curve conveyors: Square-Turn belt power turns, Flow-Merge strip belt merges, Zone-Turn belted curves (low voltage conveyor systems). Flow-Lifts continuously running vertical conveyors (high throughput, low maintenance, parcel handling, e-commerce, factory automation). Flow-Gapper conveyors (consistent spacing for sorter inductions, merge lines, scan tunnels, labeling, weight scale systems). Flow-Merge FMFW (baggage handling, heavy-duty applications). Simple, efficient, reliable conveyor solutions.",
        "product_complexity": "Very High - 40+ years global conveyor manufacturing, powered belt curve technology, vertical conveyor engineering (high throughput/low maintenance), low voltage system integration, consistent spacing technology (Flow-Gapper), baggage handling heavy-duty systems, diverse applications (e-commerce/parcel/airports/factory automation), international customer base."
    },
    "American Wholesale Distributors": {
        "industry": "Apparel & Custom Branding Wholesale Distribution",
        "workflow_type": "Wholesale Distribution - Custom Logo Services",
        "company_description": "Canoga Park, CA (21224 Vanowen St, 91303). Contact: (866) 690-6793. SIC code 5136 (Men's and Boys' Clothing and Furnishings). Offers quality apparel products, Lucky Gambler Clothing. Provides wholesale services for promotional use, retail sales, custom projects.",
        "product_types": "Quality apparel products, Lucky Gambler Clothing, custom logo branding and design services. Wholesale apparel for promotional use, retail sales, custom projects. Men's and boys' clothing and furnishings specialization.",
        "product_complexity": "Medium - Wholesale apparel distribution, custom logo branding/design services, Lucky Gambler Clothing line, multi-purpose serving (promotional/retail/custom projects), men's/boys' clothing specialization, California operations."
    },
    "Mpact Beverage Company": {
        "industry": "Ready-to-Drink Craft Cocktails Manufacturing",
        "workflow_type": "Premium RTD Beverage Production - Award-Winning",
        "company_description": "Houston, TX. Produces premium ready-to-drink adult craft beverage products. Award-winning: Island Style Rita won Best Overall Wine Based RTD Cocktail 2024. Handcrafted small batches using finest ingredients/fruit juices worldwide, pure natural Louisiana cane sugar, proprietary Cryopact™ cold filtration process.",
        "product_types": "Island Style canned cocktails ('Ultimate Craft Cocktail'): hurricane, hipnotical, rita (award-winning wine based), pina colada, sunset, melon bomb, pineapple maretto, arctic russian, peach, lemonade, tea, jamaica me loco, strawberry, mudslide. 12.5% ABV. Ready to drink chilled, over-ice, or frozen. Available bulk 5-gallon pails or single-serve bottles. Orange wine, agave flavoring, natural ingredients.",
        "product_complexity": "High - Award-winning RTD cocktail formulation (2024 Best Overall Wine Based), proprietary Cryopact™ cold filtration technology, small batch handcrafted production, worldwide fruit juice sourcing, Louisiana cane sugar natural sweetening, 14+ flavor SKUs, wine-based cocktail innovation, dual packaging (5-gallon bulk/single-serve), 12.5% ABV engineering."
    }
}

print(f"Batch 101-110 research data prepared for {len(BATCH_101_110)} companies")
for company in BATCH_101_110:
    print(f"  ✓ {company}")
