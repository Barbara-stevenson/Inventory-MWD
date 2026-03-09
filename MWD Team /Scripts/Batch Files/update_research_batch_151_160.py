#!/usr/bin/env python3
"""
Batch update for companies 151-160 research data.
"""

BATCH_151_160 = {
    "Hundegger USA, L.C.": {
        "industry": "CNC Timber Processing Machinery Manufacturing",
        "workflow_type": "Manufacturing - Global Market Leader (90%+ Share)",
        "company_description": "Heber City, Utah. Global market leader in CNC joinery machines with 90%+ market share. Strategic collaboration with Stiles Machinery. Serves timber construction worldwide. Swiss precision engineering. Applications: timber framing, roof truss making, log home construction, stick frame construction, glulam processing, playground equipment production.",
        "product_types": "CNC timber processing machines: K2-Industry joinery machines (20x50mm to 300x450mm cross sections), ROBOT-Max with Cambium software (mass-timber production), Speed Cut (quick/precise cutting/drilling/milling/slotting/marking/ink-jet printing), PBA-Industry panel processing (wall/floor/roof elements, solid wood/glulam/cross laminated timber/sandwich elements). Universal flexible machines for all timber construction areas.",
        "product_complexity": "Very High - 90%+ global market share, CNC timber processing technology, mass-timber production software (Cambium), cross sections 20x50mm to 300x450mm capability, panel processing for CLT/glulam, ink-jet printing integration, playground equipment manufacturing expertise, Stiles Machinery strategic partnership, worldwide timber construction applications."
    },
    "LIQUIMEDLOCK INC.": {
        "industry": "Secure Medication Packaging - Methadone Specialty",
        "workflow_type": "Manufacturing - Patented Compliance Packaging",
        "company_description": "Founded by Jack Finkelstein (10+ years ago) to solve inefficient/insecure methadone dispensing in MAT programs. Focused exclusively on specialty compliance packaging for hand-fill/auto-fill methadone operations. ISO 8317 tested/certified. Serves pharmacies, nurses, treatment centers. Patented gasket design.",
        "product_types": "LiquiMedLock™ methadone bottles (secure, tamper-evident, child-resistant, leak-proof, two-piece click-lock closure, patented gasket for leak-free transport/in-flight air travel, ISO 8317 certified, child resistant spin top, orange tamper-evident band). MethaLock™ bottles, MedLock Box™ (multi-day methadone storage, 14 doses), urine collection devices. Meets stringent US regulatory requirements.",
        "product_complexity": "Very High - Patented gasket design for leak-free transport, ISO 8317 child-resistant certification, tamper-evident band technology, two-piece click-lock closure innovation, in-flight air travel approved, Methadone Assisted Treatment (MAT) program specialization, hand-fill/auto-fill operations compatibility, 14-day secure storage engineering."
    },
    "Mailbox Groceries Alaska LLC": {
        "industry": "Rural Alaska Grocery Delivery & Shipping",
        "workflow_type": "E-Commerce & Distribution - Remote Community Specialist",
        "company_description": "#1 Alaskan Shipper of Groceries to Rural Alaskans. Anchorage-based. Large selection major brand groceries, fair prices, fast delivery. Priority mail service to zip codes 995/996/997 from Anchorage to village post office boxes. USPS, marine, air freight options. Quest cards accepted for air freight of perishables. Contact: chris@mbgak.com, 1-800-248-4419. 100% guarantee on nonperishables.",
        "product_types": "Extensive grocery categories: Baby Supplies, Cereal, Condiments, Beverages, Canned Foods, Candy, Chilled Foods, Fresh Meat (Frozen), Fresh Produce, Health And Beauty Aids, Bakery, Pet Care, Laundry/Cleaning, Organic Food Products, Emergency Foods, Ethnic Foods, Restaurant Size Products, Meat Packages. Major brand groceries. Dry goods include priority mail. Perishables include Ted Stevens Airport delivery (air freight separate).",
        "product_complexity": "High - Remote Alaska distribution expertise, multi-transportation mode coordination (USPS/marine/air freight), priority mail service to rural zip codes 995/996/997, perishable/frozen food logistics, Quest card payment processing, village post office delivery, 1-800 customer service, Ted Stevens International Airport operations, comprehensive grocery category management."
    },
    "Erazor bits": {
        "industry": "Patriotic & Military Apparel E-Commerce",
        "workflow_type": "Design & Print - USA Manufacturing",
        "company_description": "Serving patriots since 1993. All clothing printed in USA. South Florida operations. Specializes in patriotic apparel for US Military men/women. Serves military members, firefighters, police officers, first responders, fishermen, electricians, miners, mechanics, hunters, welders, truckers, poker players. Website: shoperazorbits.com. Available on Amazon.",
        "product_types": "Patriotic & military apparel: t-shirts, sweatshirts, hoodies, long sleeves, glassware, decals, aluminum art signs, throw blankets, towels, mugs, coasters, Christmas ornaments, face masks. Armed Forces designs for all US branches (Air Force, Army, Coast Guard, Marine Corps, Navy). USA printed clothing. Multi-category merchandise for patriots.",
        "product_complexity": "Medium-High - 30+ years patriotic apparel expertise, USA printing operations, all US military branches design licensing/representation, multi-category product portfolio (apparel/glassware/signage/home goods), e-commerce/Amazon dual-channel distribution, first responder market specialization, diverse occupational targeting (fishermen/electricians/miners/mechanics/hunters/welders/truckers), South Florida manufacturing."
    },
    "Agpro, Inc.": {
        "industry": "Agricultural Equipment Manufacturing - Conservation Drills",
        "workflow_type": "Custom Design & Manufacturing - Pacific Northwest",
        "company_description": "Founded 1987 by Wayne Neace and Jerry Harper. Specializes in No-Till Conservation Drills built for hills of Palouse. Lewiston, Idaho operations. Products throughout Pacific North-West. Expanding operations while designing/manufacturing better conservation drills. American craftsmanship.",
        "product_types": "Conservation drills (custom design, banding/uniform spreading single/multiple products), 3-Point Sprayers (65/110/150/200/300 gallon sizes), ATV Sprayers (15/25 gallon molded poly tanks), Skid Sprayers (60/100/200/300 gallon), Hydraulic Tilt Trailers (Lewiston, Idaho built), Commodity Carts (custom designs), Multi-Bin Fertilizer Applicators (orchards/vineyards/row crops), Sprayer Drones (XAG P150, max liquid payload 154 lbs).",
        "product_complexity": "Very High - No-Till Conservation Drill specialization (Palouse hills engineering), custom design capabilities, multi-bin fertilizer applicator technology (orchard/vineyard/row crop specific), hydraulic tilt trailer manufacturing, drone integration (XAG P150, 154 lb payload), multi-product banding/spreading systems, 15-300 gallon sprayer range, American craftsmanship commitment, Pacific North-West regional expertise."
    },
    "American Hat Makers - HNH": {
        "industry": "Premium Handcrafted Hats - Head n' Home Brand",
        "workflow_type": "Manufacturing - Family-Owned 50 Year Expertise",
        "company_description": "Family-owned company with 50 years hat making experience. Owned by Garth Watrous (learned from father Gary Watrous, founder). Santa Cruz, California handcrafted operations. 50-Year Craftsmanship Guarantee. Head n' Home (HNH) brand. Finest materials. Highest standards of craftsmanship.",
        "product_types": "Head n' Home hats: cowboy hats, fedoras, sun hats, straw hats for men/women. Diverse collection from classic to contemporary styles. Premium handcrafted headwear. High-quality materials. Santa Cruz, California handmade. Multiple occasion styles.",
        "product_complexity": "High - 50 years family hat making expertise, Head n' Home (HNH) brand, Santa Cruz California handcrafting, 50-Year Craftsmanship Guarantee, finest materials sourcing, multi-generational knowledge transfer (Gary to Garth Watrous), classic/contemporary style diversity, men's/women's collections, cowboy/fedora/sun/straw specialization."
    },
    "Hi Signs, The Fath Group Ltd.": {
        "industry": "Architectural Signage & Wayfinding Manufacturing",
        "workflow_type": "Design, Fabrication & Installation - Western Canada",
        "company_description": "Founded 1974, acquired by THE FATH GROUP 2005. Part of Fath Group of Companies (Edmonton since 1956). 55,000 sq ft facility (moved 1999). Acquired 310-SIGN, Knorth Creative, Banff Sign Company. Edmonton and Calgary locations. Comprehensive services: planning/design to custom fabrication/project management.",
        "product_types": "Architectural signage, wayfinding systems, design services (navigation, safety, arrival, community, belonging, brand awareness). Custom manufacturing, welding, wide-format printing, installation. Oilfield signage specialization. Project management. Technical capabilities: 55,000sf facility with custom fabrication/welding/printing.",
        "product_complexity": "Very High - 50+ years Fath Group heritage, 55,000 sq ft manufacturing facility, comprehensive design-to-installation services, multi-brand acquisition integration (310-SIGN/Knorth Creative/Banff Sign Company), custom welding/wide-format printing capabilities, architectural wayfinding expertise, oilfield signage specialization, Edmonton/Calgary dual operations, project management services."
    },
    "PMA-13": {
        "industry": "Interior Architectural Signage & Wayfinding Systems",
        "workflow_type": "Manufacturing & Distribution - Wholesale Solutions",
        "company_description": "Operates as Clarke Systems (clarkesystems.com). Allentown, PA. 35+ years leading wholesale interior wayfinding solutions. 2019 received $25,000 Ben Franklin investment for continuation project with Lehigh University's Center for Supply Chain Research. Serves sign companies/design specifiers nationwide.",
        "product_types": "ADA-compatible integrated sign systems (maximum functionality/changeability, low-maintenance). Aluminum and plastic components (both recyclable). Architectural signage, wholesale wayfinding systems, ADA-compliant signs, modular signs, aluminum extrusions. Interior signage systems for commercial buildings.",
        "product_complexity": "High - 35+ years wholesale wayfinding expertise, ADA-compatible system engineering, aluminum/plastic recyclable component manufacturing, modular sign systems, maximum changeability design, Lehigh University Center for Supply Chain Research partnership, Ben Franklin investment recipient, nationwide sign company/design specifier distribution, Allentown PA operations."
    },
    "Legit Ship LLC": {
        "industry": "Hemp & CBD Industry B2B Connector - Wholesaling",
        "workflow_type": "Network Platform & Distribution - Seed to Sale",
        "company_description": "Prospect, OR. Created to connect vetted Buyers, Suppliers, Service Providers within Hemp Industry on one trusted network. Managed by Corey Rauch, Managing Member. Connects businesses from seed to sale and everything in between. B2B connector and wholesaler. Website: legitshipcbd.com. Social media presence.",
        "product_types": "B2B network connecting Hemp/CBD Industry: buyers, suppliers, service providers. CBD wholesaling (flower and other CBD items). Trusted network for selling/promoting products/services. Exploring new industry avenues. Hemp industry connections seed to sale.",
        "product_complexity": "Medium-High - Hemp/CBD industry B2B network platform, vetted buyer/supplier/service provider connections, seed to sale supply chain integration, trusted network operations, CBD wholesaling (flower/products), industry exploration services, multi-stakeholder coordination (buyers/suppliers/services), Oregon operations, social media network building."
    },
    "Classic Rock Face Block": {
        "industry": "Historic Concrete Rock Face Block Manufacturing",
        "workflow_type": "Manufacturing - Historical Replication Specialist",
        "company_description": "Manufacturer of historic concrete rock face blocks (also known as rusticated or molded concrete blocks). Uses castings from original blocks and design plates to create historically accurate replicas. Suitable for restoration projects and period-style new construction. Approved by historic neighborhood associations, city historic commissions, National Park Service. Ships nationwide, no minimum quantity.",
        "product_types": "Historic rock face concrete blocks: exact replica full size blocks, veneers for historically accurate restoration/period-style new construction. Meets ASTM standards. Early 20th century home restoration specialization. Sears Kit Homes blocks. Created using cast-iron face plates or plaster molds from cut stone blocks. Portland cement/sand/gravel construction.",
        "product_complexity": "Very High - Historical accuracy expertise (original block castings/design plates), National Park Service approval, ASTM standards compliance, historic neighborhood association/city commission approvals, early 20th century construction replication, Sears Kit Homes specialization, cast-iron face plate/plaster mold technology, nationwide shipping (no minimums), restoration/period-style new construction dual applications."
    }
}

print(f"Batch 151-160 research data prepared for {len(BATCH_151_160)} companies")
for company in BATCH_151_160:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 160/200 companies = 80% complete!")
