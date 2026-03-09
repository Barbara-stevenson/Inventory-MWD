#!/usr/bin/env python3
"""
Batch update for companies 171-180 research data.
"""

BATCH_171_180 = {
    "CAD Supplies Specialty Inc.": {
        "industry": "Wide Format Printing Equipment & Supplies Distribution",
        "workflow_type": "Sales, Service & Distribution - Austin, TX",
        "company_description": "Founded 1996, Austin, Texas. Helping businesses, architects, sign shops, reprographics professionals for 25+ years. Factory-trained technicians, installation/setup/expert advice. On-site/depot repair across Central Texas. Texas state contract vendor.",
        "product_types": "Wide format printers (HP, Canon, Epson, Mimaki, Mutoh, Roland, Seiko Teriostar), cutters, SEAL laminators, CET Color flatbeds, Roland 3D/Engraver machines, inkjet printers, graphic printers, scanners, office equipment. Media: vinyl, banner, canvas, photo, backlit. Inks: aqueous, eco-solvent, UV, latex compatible. Refurbished printers/accessories.",
        "product_complexity": "High - 25+ years wide format printing expertise, multi-brand distribution (HP/Canon/Epson/Mimaki/Mutoh/Roland/Seiko), factory-trained technician services, Central Texas on-site/depot repair, vinyl/banner/canvas/photo/backlit media specialization, aqueous/eco-solvent/UV/latex ink compatibility, SEAL laminator/CET flatbed/Roland 3D expertise, refurbished equipment sales."
    },
    "T. Friedl Enterprises (2000) Inc.": {
        "industry": "Printed Circuit Board Manufacturing Equipment & Supplies",
        "workflow_type": "Distribution & Service - PCB Industry Specialist",
        "company_description": "Ontario, Canada. 25+ years providing high quality products/services to printed circuit board manufacturing industry. Exceptional technical expertise/customer service. Importer/distributor. Serves Printed Circuit Board, Printed Electronics, Wafer Level Products sectors.",
        "product_types": "PCB manufacturing equipment/consumables: HAM precision drills, HPTec, ERBO systems, Bipico Band Saw Blades, cutting tool/CNC machine accessories, Electra Polymers distributor. Equipment and supplies for electronics manufacturing companies.",
        "product_complexity": "High - 25+ years PCB manufacturing expertise, HAM precision drill distribution, HPTec/ERBO systems, Bipico Band Saw Blade specialization, cutting tool/CNC machine accessories, Printed Electronics/Wafer Level Products sector serving, Electra Polymers authorized distributor, Canadian electronics manufacturing market, exceptional technical expertise."
    },
    "Reuning-McKim, Inc.": {
        "industry": "Steelmaking Technology & Telescopic Lances Manufacturing",
        "workflow_type": "Design, Manufacturing & Distribution - Global Steel Industry",
        "company_description": "Saxonburg, PA. Half century steel industry experience. Serves customers across 11 countries on 4 continents. Innovative steelmaking technology. Designs/manufactures/distributes telescopic lances and insulating powders. Partnership with Trefimet.",
        "product_types": "Telescopic lances (oxygen lances for meltshop furnaces/ladles/casters), Thermal lances (cutting/cleaning/scrapping, Trefimet partnership), Insulating powders (Rice Hull Ash powder), Telescopic T-lances, Shrouded ladles. Steel manufacturing solutions.",
        "product_complexity": "Very High - 50 years steelmaking technology expertise, telescopic lance design/manufacturing, oxygen lance engineering (furnaces/ladles/casters), thermal lance technology (Trefimet partnership), Rice Hull Ash insulating powder specialization, shrouded ladle systems, 11-country/4-continent global distribution, meltshop furnace specialization."
    },
    "HYDROLOGICAL SERVICES AMERICA": {
        "industry": "Hydrological & Meteorological Equipment - Data Solutions",
        "workflow_type": "Manufacturing & Software - KISTERS Acquisition",
        "company_description": "Now HyQuest Solutions America (merged with KISTERS June 1, 2023). Leading provider hydrological/meteorological equipment. Joined KISTERS AG global family (data management/analysis software). KISTERS North America branding. End-to-end solutions.",
        "product_types": "Hydrological/meteorological equipment: discharge radar, level radar, velocity radar, cableways, tipping bucket rain gauge, water quality sensors, flood warning systems, dataloggers, snow measurement, hail sensors, weather sensors. Data visualization/analytics software. Monitoring equipment + software integration.",
        "product_complexity": "Very High - KISTERS AG merger integration, hydrological/meteorological equipment manufacturing, radar technology (discharge/level/velocity), tipping bucket rain gauge engineering, water quality sensor systems, flood warning technology, snow/hail measurement, data visualization/analytics software, end-to-end monitoring solutions, environmental management systems, KISTERS North America operations."
    },
    "The Equipment Lock Company": {
        "industry": "Heavy Equipment Security Locks Manufacturing",
        "workflow_type": "Manufacturing & Design - USA Made Security Solutions",
        "company_description": "Founded 2001, Winchester, VA. One-stop shop for securing logistics/construction/recreational equipment. Pro-Active Equipment Security philosophy. Universal barrel-style key locks (pick/Freon/corrosion resistant). Designed USA, withstands thousands of pounds of force. Bright red steel locking devices.",
        "product_types": "Heavy equipment security locks: Heavy Duty Cargo Door Locks (#1 seller, secures semi-trailers/sea containers), Excavator Locks, Backhoe Locks, Attachment Locks, Trailer hitch locks, Rolling door locks, Jobsite office door locks. Universal for all manufacturers. Battle-tested products. Secure in seconds.",
        "product_complexity": "Very High - Patented universal barrel-style key lock technology (pick/Freon/corrosion resistant), thousands-of-pounds force withstanding engineering, semi-trailer/sea container security specialization, USA design/manufacturing, universal manufacturer compatibility, bright red steel construction, excavator/backhoe/attachment lock customization, pro-active theft prevention, Winchester VA operations."
    },
    "PPFD Ltd.": {
        "industry": "Third-Party Logistics & Fulfillment Services",
        "workflow_type": "Warehousing & Distribution - 3PL Provider",
        "company_description": "Founded 1986, Greater Toronto area. Promotional Products Fulfillment & Distribution Ltd. 125,000 sq ft state-of-the-art warehouse (custom designed/built 2001). Tailored supply chain solutions. Website: ppfd.com.",
        "product_types": "3PL services: e-commerce fulfillment, pick and pack, kitting, cross docking, storage, contest administration, warehousing, logistics. Tailored solutions for supply chain operations/market responsiveness. Distribution center services.",
        "product_complexity": "High - 35+ years 3PL expertise, 125,000 sq ft custom-designed warehouse facility, e-commerce fulfillment specialization, pick/pack operations, kitting services, cross docking logistics, contest administration capabilities, Greater Toronto area distribution hub, supply chain optimization, market responsiveness solutions."
    },
    "MULTI SEAL": {
        "industry": "Industrial Tire Sealant Manufacturing",
        "workflow_type": "Manufacturing - USA Made High-Performance Sealants",
        "company_description": "CEO: Wynand Schlechter. USA manufacturing. $5.2M revenue, <25 employees. Contact: (281) 591-0111. Industrial-grade sealants for demanding industrial equipment. Not recommended for passenger vehicles. Website: multiseal.us.",
        "product_types": "High-performance tire sealants: MULTI SEAL and FlatOut brands. Industrial applications/recreational lifestyles. Advanced formula featuring synthetic TangleTek™ fibers and DamRight™ fillers for puncture protection. Industrial equipment focus.",
        "product_complexity": "Medium-High - USA tire sealant manufacturing, proprietary TangleTek™ synthetic fiber technology, DamRight™ filler innovation, industrial-grade formulation, industrial equipment specialization, puncture protection engineering, recreational lifestyle applications, MULTI SEAL/FlatOut dual brands, $5.2M revenue operations."
    },
    "LAMP NUTRA": {
        "industry": "Kratom Supplements & Nutraceuticals",
        "workflow_type": "Online Retail & Distribution - Royal Kratom Brand",
        "company_description": "Founded 8/20/2014, Carlsbad, CA (3133 Tiger Run Ct Suite 107). Sole Proprietorship. Operates as LAMP Holdings and Royal Kratom. Contact: (800) 520-0966, info@lampnutra.com. NOT BBB Accredited. 11 years in business.",
        "product_types": "Online shopping services for kratom supplement products. Royal Kratom brand operations. Nutraceutical supplements.",
        "product_complexity": "Medium - Kratom supplement specialization, Royal Kratom brand operations, online shopping platform, sole proprietorship business model, Carlsbad CA operations, 11 years nutraceutical market experience, LAMP Holdings corporate structure."
    },
    "Imperial Privacy Systems LLC": {
        "industry": "Healthcare Privacy Curtains & ICRA Barriers Manufacturing",
        "workflow_type": "Manufacturing - Family-Owned USA Made",
        "company_description": "Formerly Imperial Fastener Co. 50+ years trusted leader. Family owned/operated, Pompano Beach, Florida. American-made cubicle curtains/temporary construction walls for healthcare/institutional settings. Website: imperialprivacy.com.",
        "product_types": "Hospital privacy curtains, ICRA barriers, cubicle curtains, cubicle tracks, IV track systems, specialty curtains, snap-on curtains, shower curtains, security shower curtains, blackout curtains. For patient rooms, clinics, behavioral health, education, senior care, healthcare facilities. Fabric-based privacy solutions (not bathroom partitions).",
        "product_complexity": "Very High - 50+ years healthcare privacy expertise, American-made manufacturing (Pompano Beach FL), ICRA barrier engineering, cubicle track/IV track systems, snap-on curtain technology, security shower curtain innovation, behavioral health/senior care specialization, family-owned operations, healthcare institutional focus, fabric-based privacy solutions."
    },
    "Ozop Energy Systems, Inc.": {
        "industry": "Renewable Energy Products & EV Charging Solutions",
        "workflow_type": "Manufacturing & Distribution - Public Company (OZSC)",
        "company_description": "Founded with 29 years industry experience. Warwick, NY. OTC ticker: OZSC. Manufacturer/distributor Renewable Energy products. Subsidiary: Automated Room Controls Inc. National Field Service Partner for Leviton through Ozop Engineering and Design. Website: ozopenergy.com.",
        "product_types": "Energy Storage solutions, Solar products, Microgrids, EV charging stations (on-grid level 1/2/3 Superchargers, multi-use portable systems), Digital lighting controls (relay panels, controllers, occupancy/vacancy sensors, daylight sensors, wall switch stations), ultra-high-power chargers/inverters/power supplies (defense, heavy industrial, aircraft ground support, maritime). Ozop West operations.",
        "product_complexity": "Very High - 29 years renewable energy expertise, Energy Storage/Solar/Microgrid/EV charging integration, level 1/2/3 Supercharger technology, portable EV charging systems, ultra-high-power charger engineering (defense/industrial/aircraft/maritime), digital lighting control automation, Leviton national partnership, Automated Room Controls subsidiary, public company operations (OZSC), Ozop Engineering and Design restructuring, competitive pricing/customer satisfaction focus."
    }
}

print(f"Batch 171-180 research data prepared for {len(BATCH_171_180)} companies")
for company in BATCH_171_180:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 180/200 companies = 90% complete!")
