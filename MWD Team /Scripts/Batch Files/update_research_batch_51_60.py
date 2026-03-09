#!/usr/bin/env python3
"""
Batch update for companies 51-60 research data.
This will be merged into the main research file.
"""

BATCH_51_60 = {
    "Mid Florida Material Handling, Inc": {
        "industry": "Material Handling Equipment Distribution",
        "workflow_type": "Sales, Service, Rentals & Parts - Full-Suite Provider",
        "company_description": "Founded 2011 by Paul Sutherland and Andrea Ahern. True 'one-stop shop' for material handling and warehouse design. Orlando HQ, Tampa branch. Notable clients: Michelin, Delta, Disney, NASA. Authorized Komatsu, CLARK dealer. Phone: (407) 859-8750.",
        "product_types": "New/used forklifts (Komatsu, CLARK, Toyota, Nissan, Yale, Noblelift, Bendi, Drexel, ePicker, 2,000-35,000 lbs capacity), pallet rack, mezzanines, material handling equipment. Sales/service/rentals/parts throughout Florida. Mobile forklift service fleet.",
        "product_complexity": "High - Multi-brand forklift dealership, full-service provider (sales/rentals/parts/service), warehouse design capabilities, mobile service fleet logistics, thousands of projects, large inventory management."
    },
    "A Beep, LLC": {
        "industry": "Push-to-Talk Telecommunications",
        "workflow_type": "PoC Provider & Two-Way Radio Services",
        "company_description": "Founded 1996, Joliet, IL. 25+ year anniversary. Nation's largest privately held Push-to-Talk over Cellular (PoC) provider. Grown from small regional paging carrier and 2-way radio service to recognized PoC provider with proprietary Diga-Talk+ product line.",
        "product_types": "Two-way Push-To-Talk radios (Diga-Talk+, Diga-Talk2, Diga-Trax), Kenwood radios and accessories, Nationwide PoC Push Over Cellular, mobile/digital communication solutions, extensive analog LTR trunked network.",
        "product_complexity": "High - Proprietary PoC technology development, nationwide cellular network operations, analog LTR trunked network maintenance, dynamic mobile radio solutions for industry/schools/fleets/municipalities."
    },
    "CDS ANALYTICAL, LLC": {
        "industry": "Analytical Laboratory Instrumentation Manufacturing",
        "workflow_type": "Design, Manufacturing & Support - Thermal Sample Preparation",
        "company_description": "50+ years focused on thermal sample preparation instrumentation. Oxford, PA. Leading global provider. Incorporated as Chemical Data Systems 1969, introduced first Pyroprobe®. Made in USA. Acquired by LabTech LT May 2020.",
        "product_types": "Pyrolyzers (Py-GC-MS), thermal desorbers (TD-GC-MS), purge and trap concentrators (EPA 524, 624, 8260 methods), headspace analyzers. Catalyst screening, reaction optimization, organic headspace analysis, environmental testing. Front end all GCMS manufacturers.",
        "product_complexity": "Very High - Specialized analytical instrumentation requiring advanced engineering, 50+ years exclusive focus, integration with all GCMS manufacturers and software, made in USA manufacturing, diverse applications across analytical chemistry."
    },
    "Sky Products": {
        "industry": "MULTIPLE COMPANIES - Requires Clarification",
        "workflow_type": "PENDING - Multiple companies with this name",
        "company_description": "MULTIPLE ENTITIES FOUND: (1) Sky Manufacturing - Aerospace fasteners (high-strength, fatigue-rated for aerospace, acquired by Novaria 2015), (2) Sky Manufacturing - Custom private-label apparel (run specialty since June 2020), (3) Sunny Sky Products - Dispensed beverage industry liquids/powders (6 facilities, Houston HQ), (4) Sky's Offroad Design - 800+ Toyota/Ford/Chevy off-road parts, (5) Sky Industries - Hook and loop manufacturer India since 1994. Specific entity requires verification.",
        "product_types": "PENDING - Varies from aerospace fasteners to apparel to beverage products to off-road parts",
        "product_complexity": "PENDING - Requires entity identification"
    },
    "Data Memory Sales, Inc.": {
        "industry": "Computer Memory & Storage Distribution",
        "workflow_type": "Distribution - Memory Upgrades & Components",
        "company_description": "Data Memory Systems (DMS) supplying electronics industry with high quality components since 1963, memory modules since 1987. Salem, NH. Leading provider of memory upgrades and storage devices. BBB accredited. Lifetime replacement warranty.",
        "product_types": "Memory upgrades (DDR, DDR2, DDR3, Dual Channel, SDRAM, EDO - Samsung/Micron/Hynix), desktop/laptop/Mac/server memory, hard drives (SATA, PATA, IDE, notebook, desktop, server, RAID, NAS, SSD), flash memory (compact flash, SD, SDHC, microSDHC cards from Transcend/Wintec/Sandisk).",
        "product_complexity": "High - Wide range of memory types and storage solutions, compatibility across all major computer brands, fully tested and qualified in memory test lab, lifetime warranty program, long-standing industry presence (60+ years)."
    },
    "Safari Belting Systems, Inc.": {
        "industry": "Plastic Modular Conveyor Belting Manufacturing",
        "workflow_type": "Specialized Manufacturing - Food Processing Focus",
        "company_description": "Founded 2005 by Chris and Julia Smith. Acquired 2021 by Chiorino S.p.A. (international leader in light-weight conveyor belting). Specialized American manufacturer, primary belting provider to largest food processors. Over 400 belting solutions used in plants worldwide.",
        "product_types": "Plastic modular belts (Acetal, Polyethylene, Polypropylene), ULTRA-TUFF™ (revolutionary high-performance resin), ULTRA-TUFF XMD™ (metal/x-ray detectable, 1.5mm ferrous equivalent), roller-top solutions, accessories. Direct food application approved materials.",
        "product_complexity": "Very High - Proprietary material development (ULTRA-TUFF), metal/x-ray detectable formulations, FDA food contact compliance, 400+ belting solutions catalog, meat/poultry/baked goods/snack food/fruits/vegetables applications, chemical/abrasion resistance engineering."
    },
    "Nu Kitchens, LLC": {
        "industry": "Custom Kitchen & Bath Design",
        "workflow_type": "Complete Renovation - Design to Installation",
        "company_description": "Founded 1950s by Joseph Najmy. Kitchen renovation company offering concept, design, installation, remodeling. South Norwalk, CT showroom (132 Water Street). Best of Houzz awards 2014, 2016, 2017, 2018. Decades of experience, family background in renovation/furniture craft/interior design.",
        "product_types": "Custom all-wood cabinetry (Plain & Fancy dealer), custom kitchen cabinets, custom bathroom vanities, custom pantries, granite, limestone, tiles, hardware, sinks, faucets, kitchen lighting, bathroom design. Finest materials, kitchen remodeling services.",
        "product_complexity": "High - Full-service renovation requiring design expertise, custom cabinetry specifications, material selection (wood/granite/stone/tile), plumbing fixtures, lighting design, project management from concept to completion, showroom operations."
    },
    "ELM USA Inc.": {
        "industry": "MULTIPLE COMPANIES - Requires Clarification",
        "workflow_type": "PENDING - Multiple companies with this name",
        "company_description": "MULTIPLE ENTITIES FOUND: (1) Environmental Lubricants Manufacturing - sustainable lubricants with on-site lab for conventional/synthetic/eco-friendly formulations, (2) Elm Industries - thermoset molding for military/aerospace/electronics with tight tolerances (phenolics, DAP, Urea, Epoxy, BMC), (3) ELM USA - disc repair equipment sales/service/parts distributor for ECO machines in Americas. Specific entity requires verification.",
        "product_types": "PENDING - Varies from lubricants to precision molded parts to disc repair equipment",
        "product_complexity": "PENDING - Requires entity identification"
    },
    "ASCO CARBON DIOXIDE INC.": {
        "industry": "CO2 & Dry Ice Solutions Manufacturing",
        "workflow_type": "Design, Manufacturing & Installation - Complete CO2 Solutions",
        "company_description": "Swiss global company, part of Messer Group since 2007 (centre of competence for CO2). US subsidiary founded July 2016 in Orange Park, FL. 130+ years practical experience. CO2 production/recovery plants installed in 100+ countries.",
        "product_types": "Carbon capture plants, CO2 recovery systems (ASCOSORB stack gas technology), ASCOJET dry ice blasting machines, dry ice production machines, CO2 cylinder filling systems, CO2 vaporizers, CO2 storage tanks, CO2 dosing systems (water neutralization), CO2 accessories.",
        "product_complexity": "Very High - Energy-efficient CO2 gas recovery technology, carbon capture engineering, proprietary ASCOSORB technology, complete turnkey CO2 solutions, global installations requiring technical support, dry ice production equipment, industrial gas expertise."
    },
    "Continental Field Systems": {
        "industry": "Field Machining & Welding Services",
        "workflow_type": "On-Site & Shop Manufacturing Services",
        "company_description": "Savannah, GA. 125,000 sq ft facility (20,000 sq ft expansion, $4M investment). Proprietary field equipment designed/tested/manufactured in-house. Serves power, pulp and paper, chemical, marine, steel, recycling industries and beyond. 24/7 emergency services.",
        "product_types": "Field machining, shop machining (CNC centers, lathes, manual centers), manual/automatic welding, valve repair, turbine repair, laser tracking/alignment, quality assurance, project management. Portable lathe (220-ton capacity). Nuclear power, oil and gas, marine applications.",
        "product_complexity": "Very High - Proprietary field equipment development, on-site machining capabilities (portable 220-ton lathe), CNC manufacturing, 24/7 emergency response, laser tracking precision work, nuclear/power industry certifications, large facility operations."
    }
}

print(f"Batch 51-60 research data prepared for {len(BATCH_51_60)} companies")
for company in BATCH_51_60:
    print(f"  ✓ {company}")
