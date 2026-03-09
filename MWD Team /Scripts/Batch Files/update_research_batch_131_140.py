#!/usr/bin/env python3
"""
Batch update for companies 131-140 research data.
"""

BATCH_131_140 = {
    "OFFICE FIRST SOLUTIONS": {
        "industry": "Office Furniture Sales & Liquidation - New & Used",
        "workflow_type": "Wholesale & Retail - Full Service Solutions",
        "company_description": "Columbus, OH (1665 Westbelt Dr). One of Ohio's largest used office furniture stores. Buys/sells new & used office furniture, cubicles, chairs. Years of experience providing office furniture solutions and liquidations. Services: interior design, space planning, delivery & installation. Contact: (614) 899-2300. Hours: M-F 9am-5pm, Sat 10am-2pm.",
        "product_types": "New & used office furniture: cubicles, chairs, desks, filing cabinets. Home office furniture. Interior design services, space planning, delivery & installation. Office furniture liquidations. Buy, sell and liquidate office furniture.",
        "product_complexity": "Medium - New/used office furniture buying/selling/liquidation expertise, interior design services, space planning capabilities, delivery/installation operations, Ohio's largest used furniture inventory, cubicle/chair specialization, home office market, multi-service offering (design/planning/delivery)."
    },
    "TechniSoil Global, Inc.": {
        "industry": "Soil Stabilization & Eco-Friendly Pavement Solutions",
        "workflow_type": "Manufacturing - Nano-Polymer Technology",
        "company_description": "Founded 2006 by Sean Weaver. Redding, CA (5670 Westside Road). World-wide leader developing/manufacturing eco-friendly nano-polymer liquid sealers, binders, stabilizers. Patented TechniSoil G5® super-polymer proven on military/tank roads, energy sector roads, wineries, park systems. Innovation in modern landscapes.",
        "product_types": "G3 Pathway Stabilizer (liquid polymer for residential pathways/planter beds/xeriscaping, decomposed granite/limestone/bluestone), G3 Commercial Surface (heavy-use commercial surfaces), TechniSoil G5® (patented super-polymer for roads, durability equal to asphalt), EKOFLO Permeable Pebble Binder, Ground Cover Stabilizer, MOLECULE SRS, NANOPAVE JSS. Natural pavement surfaces for landscape/xeriscape/hardscape/masonry.",
        "product_complexity": "Very High - Patented TechniSoil G5® super-polymer technology, nano-polymer liquid sealer development, eco-friendly binder innovation, military/tank road proven durability, asphalt-equivalent strength engineering, decomposed granite stabilization, commercial/residential applications, worldwide distribution, founder-led innovation since 2006."
    },
    "Diamond Technologies, Inc.": {
        "industry": "Industrial Automation & Data Collection Solutions",
        "workflow_type": "Manufacturing & Distribution - OEM Embedded Systems",
        "company_description": "Hudson, MA (43 Broad Street, Unit C103). Solutions provider for Data Collection and Automation challenges. Distributor and manufacturer since 1997. Specialized engineers design/manufacture/service customised solutions for OEM customers. Part of discoverIE Group plc. Value-added manufacturing services.",
        "product_types": "Embedded barcode reading, RFID, machine vision, industrial communications modules. Embedded/wireless industrial networking, M2M gateways, industrial network gateways/controllers, distributed I/O, wiring systems, embedded web servers, remote machine control/monitoring, Bluetooth to serial adapters, data collection software. OEM solutions for medical devices, lab instrumentation, kiosks, vending machines, packaging machines, AGVs, robotic systems.",
        "product_complexity": "Very High - OEM embedded systems design/manufacturing, custom hardware/firmware development, barcode/RFID/machine vision integration, industrial networking expertise, software application development, value-added manufacturing, medical device/lab instrumentation specialization, AGV/robotic systems integration, 25+ years engineering expertise."
    },
    "Camacho Coffee": {
        "industry": "Specialty Coffee Roasting - Small-Batch Air Roasted",
        "workflow_type": "Manufacturing & Wholesale - Ethical Sourcing",
        "company_description": "Founded 2017 by Jesse and Megan Walters. Columbia, Missouri (4009 Frontgate Dr). Small-batch roaster focused on ethically sourced beans, bold balanced flavor. Fair-trade, single-origin coffee. Unique air roasting technique (smooth tasting, low acidic). Serves 40-50 wholesale clients (cafes, restaurants, offices, grocery stores). Retail tasting room, online ordering.",
        "product_types": "Air roasted coffee beans: Colombian, Colombian decaf, Peruvian, Ethiopian (fair-trade, single-origin). Certified organic. Air roasting technique (beans roasted on hot air bed vs drum surface for even roasting, aromatic flavor, less acidic, never scorched/burnt/smoke flavor). Wholesale and retail. Smooth tasting, low acidic, charitable, ethically sourced.",
        "product_complexity": "High - Air roasting technology (hot air vortex floating beans, consistent temperature), small-batch roasting precision, fair-trade/certified organic sourcing, single-origin bean expertise, low acidic formulation, 4+ coffee varieties, wholesale/retail dual operations, ethical sourcing commitment, tasting room operations."
    },
    "Cool Seal Gaskets, LLC": {
        "industry": "Commercial Refrigeration Repair & Gasket Services",
        "workflow_type": "Service - Veteran-Owned Specialist",
        "company_description": "Founded by Anthony Ricciardo (former USMC Sergeant). Orlando and Kissimmee, FL (210 N Goldenrod Rd Ste 9B, Orlando). Veteran-owned company specializing in commercial refrigerator repair and gasket replacement. Free on-site inspection. Serves restaurants, hotels, supermarkets, medical facilities.",
        "product_types": "Commercial refrigerator repair services: gasket replacement (free on-site inspection determines exact gasket type), door hardware assessment/replacement, full door replacement, strip curtain installation (walk-in coolers/freezers), temperature monitoring solutions. High-quality gaskets for restaurants, hotels, supermarkets, medical facilities. Commercial refrigeration sealing expertise.",
        "product_complexity": "Medium-High - Commercial refrigeration gasket specialization, on-site inspection/diagnosis, door hardware assessment expertise, full door replacement capabilities, strip curtain installation for walk-ins, temperature monitoring systems, diverse sector serving (restaurants/hotels/supermarkets/medical), veteran-owned operations, Orlando/Kissimmee service area."
    },
    "Antares Health Products": {
        "industry": "Pharmaceutical Grade Vitamin E TPGS Manufacturing",
        "workflow_type": "Manufacturing - cGMP Certified Facility",
        "company_description": "Sole US manufacturer of vitamin E TPGS. Supplies customers internationally including global pharmaceutical companies. cGMP manufacturing facility compliant with EU GMP Part II, ICH Q7, ISO 9001, ISO 14001, ISO 45001. Regularly inspected by US-FDA, Italian AIFA, Japanese PMDA. Leading supplier for pharmaceuticals, dietary supplements, food/beverage, personal care, animal nutrition.",
        "product_types": "Vitamin E TPGS (tocopheryl polyethylene glycol succinate): Pharmaceutical Grade (NF), Food Grade (FG). Antares Sunflower TPGS™ (only commercially available non-GMO TPGS). Applications: emulsifier, absorption enhancer for fat-soluble nutrients in liquid/solid dietary supplements, pharmaceuticals, food/beverage, personal care, animal nutrition.",
        "product_complexity": "Very High - Only US manufacturer of vitamin E TPGS, cGMP facility (EU GMP Part II/ICH Q7 compliant), multi-ISO certified (9001/14001/45001), US-FDA/Italian AIFA/Japanese PMDA inspections, Pharmaceutical Grade (NF) and Food Grade production, proprietary non-GMO Sunflower TPGS™, international pharmaceutical company supply, absorption enhancer technology."
    },
    "Gitch Sportswear": {
        "industry": "Custom Sublimated Sports Apparel & Team Uniforms",
        "workflow_type": "Manufacturing - Custom Design & Sublimation",
        "company_description": "Established 2009, Toronto, Ontario, Canada. Sublimation sports apparel company that sells/designs customized team logo jerseys, uniforms, hats, bags. Low minimums, affordable price. Client base: sports clubs, schools, coaches, first responders. Corporate/events custom branded promotional products.",
        "product_types": "Custom team uniforms and sports apparel: sublimated jerseys, hoodies, shirts, tracksuits, sweatpants, shorts, hats, bags. Custom-branded promotional products (bags, shirts, hats with company logos/colors). Top quality custom products for sports teams, corporate organizations, team building events, first responders. Designer services for bespoke ranges.",
        "product_complexity": "Medium-High - Sublimation printing technology, custom logo design services, low minimum order capabilities, team uniform customization, diverse apparel categories (jerseys/tracksuits/hats/bags), corporate branded promotional products, sports club/school/first responder specialization, Toronto operations, affordable pricing model."
    },
    "MOBILITY PLUS VA LLC": {
        "industry": "Mobility Equipment Sales, Rental & Service - VA-Approved",
        "workflow_type": "Distribution & Service - Veterans & Disabled Focus",
        "company_description": "Founded 2007. VA-approved provider serving disabled veterans and aging Americans with disabilities for 15+ years. Serves VA patients and government employees. Relationships with top US mobility equipment manufacturers. Multiple locations. Complete sales, service, rental options. Prompt delivery, fair prices.",
        "product_types": "Comprehensive mobility equipment: power wheelchairs, manual wheelchairs, mobility scooters, lift chairs/recliners, stair lifts, platform lifts, hospital beds, walkers/rollators, patient lifts, scooter lifts for vehicles, ramps/accessibility equipment, bathroom safety products. Purchase and rental options. Top manufacturer partnerships.",
        "product_complexity": "High - VA-approved provider status (15+ years), Department of Veterans Affairs partnership, comprehensive mobility equipment portfolio, sales/service/rental tri-service model, top US manufacturer relationships, multi-location operations, aging Americans/disabled veterans specialization, government employee serving, accessibility equipment expertise."
    },
    "APDM Wearable Technologies, Inc.": {
        "industry": "Wearable Motion Sensors & Digital Health Technology",
        "workflow_type": "Manufacturing - Clinical Research & Healthcare",
        "company_description": "Founded 2007 by Dr. James McNames, Portland, Oregon. Acquired by ERT in 2020 (now part of Clario). Digital health company offering Opal IMU sensor-based solutions for quantifying human movement. Trusted by 1,000+ researchers, featured in 700+ peer-reviewed publications. Medical-grade wearable sensors, digital biomarkers for clinical trials.",
        "product_types": "Opal V2R System (research use only), Opal V2C System (clinical trials in-clinic/at-home digital endpoints), Moveo Explorer (portable motion capture lab, joint angles/gait/balance metrics/raw data reports), Mobility Lab (clinical software for gait/balance analysis). Motion data: joint angles, stride patterns, balance, muscle activation. Applications: Parkinson's disease, Multiple Sclerosis, Ataxia, stroke, neurological disorders.",
        "product_complexity": "Very High - Medical-grade wearable IMU sensor technology, digital biomarker development, clinical trial endpoint measurement, Parkinson's disease/MS/Ataxia/stroke applications, portable motion capture lab engineering, gait/balance analysis software, real-time joint angle/stride/muscle activation data, 1,000+ researcher network, 700+ peer-reviewed publications, ERT/Clario acquisition integration."
    },
    "Centanni Tile Inc.": {
        "industry": "European Tile & Stone Importing - Premium Ceramics",
        "workflow_type": "Import & Distribution - Western Canada",
        "company_description": "Burnaby, British Columbia (3737 Napier St). Tile & Stone importer servicing Western Canada. Curated selection of unique European-imported ceramics and porcelains from Italy, Spain, worldwide. Distributes complete line of Laticrete Installation materials & Miracle Sealants Products. Supplies high-end homes, restaurants, hotels, spas.",
        "product_types": "European-imported tile & stone: Italian ceramics, Spanish porcelains, premium tiles from worldwide sources. Laticrete Installation materials (complete line), Miracle Sealants Products. Tile/stone/hard surface specifications, design consultation, technical consultation, project sales, hospitality sales, continuing education. Seasonal collections, 'Last Call' promotions (heavy discounts on premium products).",
        "product_complexity": "High - European import operations (Italy/Spain/worldwide), Western Canada distribution network, Laticrete/Miracle Sealants authorized distributor, high-end market specialization (homes/restaurants/hotels/spas), design/technical consultation services, project/hospitality sales expertise, seasonal collections curation, premium ceramics/porcelains sourcing."
    }
}

print(f"Batch 131-140 research data prepared for {len(BATCH_131_140)} companies")
for company in BATCH_131_140:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 140/200 companies = 70% complete!")
