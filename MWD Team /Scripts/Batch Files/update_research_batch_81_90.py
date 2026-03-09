#!/usr/bin/env python3
"""
Batch update for companies 81-90 research data.
"""

BATCH_81_90 = {
    "RayBiotech Life": {
        "industry": "Life Sciences - Proteomics Research Products Manufacturing",
        "workflow_type": "Manufacturing & Services - Antibodies & Immunological Products",
        "company_description": "Founded 2001, Peachtree, GA. Leading life sciences company. Introduced first commercially available cytokine antibody array. ISO 13485:2016, cGMP manufacturing, ISO 17025:2017, CLIA certified. Serves scientific research, biotechnology, pharmaceutical development. All antibodies manufactured on-site.",
        "product_types": "18,000+ monoclonal/polyclonal research antibodies, Quantibody Multiplex ELISA Arrays, cytokine antibody arrays, glycobiology products, protein arrays, ELISA kits, functional assays, reagents, antibody services. 15+ species across diverse formats, targets, research areas, sample types. Enables drug target identification, personalized medicine advancement.",
        "product_complexity": "Very High - Proprietary multiplex array technology, 18,000+ antibody catalog requiring on-site manufacturing, ISO 13485:2016/cGMP/ISO 17025:2017/CLIA certifications, proteomics research innovation, biotechnology/pharmaceutical applications, stringent quality control."
    },
    "KNF Neille Olson": {
        "industry": "Diaphragm Pumps & Vacuum Systems Manufacturing",
        "workflow_type": "Design, Manufacturing & Distribution - Global Leader",
        "company_description": "KNF Neuberger, Inc. - renowned global leader in manufacturing/distribution of high-quality vacuum pumps with decades of history. Develops, designs, manufactures diaphragm pumps for moving gases/liquids in industries worldwide. Environmentally-friendly, cost-effective alternatives to water aspirators.",
        "product_types": "LABOPORT® vacuum pumps (laboratory focus, ease of use), micro diaphragm pumps (gases/vacuum transfer), diaphragm vacuum pumps, rotary vane pumps, piston pumps, liquid ring pumps. Standard miniature pumps: 0.33-16 l/min flow rates, pressure up to 5.5 bar, vacuum down to 50 mbar abs. Low pressure, accurate control.",
        "product_complexity": "High - Global vacuum pump manufacturing requiring diverse technologies (diaphragm, rotary vane, piston, liquid ring), precision engineering for laboratory applications, environmentally-friendly design, accurate pressure/vacuum control, worldwide distribution."
    },
    "MTA-USA, LLC": {
        "industry": "Industrial Process Cooling & Compressed Air Treatment Manufacturing",
        "workflow_type": "Manufacturing - Now Part of Trane",
        "company_description": "Leader in compressed air treatment products and process cooling equipment since 1982. Buffalo, NY. Over 35 years manufacturing industrial process cooling solutions for tough environments. Now part of Trane (leader in building technology, energy solutions), enhancing capabilities and service network.",
        "product_types": "Compressed air treatment products, process cooling equipment, industrial chillers. High-performance chillers for automotive, food and beverage, pharmaceuticals. Reliable, efficient equipment for demanding industrial applications. Designed to perform in tough manufacturing environments.",
        "product_complexity": "High - 35+ years industrial cooling expertise, integration with Trane technologies, high-performance chiller engineering for automotive/food/pharma, compressed air treatment systems, tough environment applications, enhanced service network operations."
    },
    "Centricity Vision, Inc": {
        "industry": "Ophthalmic Technology & Cataract Surgery Devices",
        "workflow_type": "Medical Device Design & Manufacturing - FDA Cleared",
        "company_description": "Carlsbad, CA. Global ophthalmic technology company, formerly Mynosys Cellular Devices (rebranded May 2020). Developer of ZEPTO® and ZEPTOLink IOL Positioning Systems. FDA 510(k) clearance for ZEPTOLink (May 2023). October 2024 platform enhancements reduced treatment time by 60%.",
        "product_types": "ZEPTO® IOL Positioning System (first/only instantaneous capsulotomy device, proprietary precision pulse technology, four-millisecond energy pulse, calibrated suction, 360-degree IOL overlap), ZEPTOLink™ IOL Positioning System (integrates with any phaco system, streamlines cataract surgery, 60% faster treatment). Ideal for premium IOLs, complex cases requiring precision. Cost/time savings, easy workflow integration.",
        "product_complexity": "Very High - Proprietary precision pulse capsulotomy technology, FDA 510(k) cleared medical devices, four-millisecond energy control algorithm, cataract surgery innovation, integration with phaco systems, premium IOL applications, continuous platform enhancements (60% time reduction)."
    },
    "Affordable Medical LLC": {
        "industry": "MULTIPLE COMPANIES - Requires Clarification",
        "workflow_type": "PENDING - Medical Equipment/Supplies Distribution",
        "company_description": "MULTIPLE ENTITIES FOUND: (1) Affordable Medical Equipment (affordable-medical.myshopify.com) - professional distributor, AME LLC Nevada subsidiary, (2) Affordable Medical Supplies Arkansas/Missouri - respiratory equipment specialization (CPAP/BiPAP/oxygen), (3) Affordable Medical Supplies Dallas - family-owned 20+ years, 10,000+ customers, (4) Affordable Medical Supply Colorado Springs - rentals/sales general public/medical professionals, (5) Affordable Medical Supply (affordablemedical.com) - in-home supplies/equipment. Specific entity requires verification.",
        "product_types": "PENDING - Varies from respiratory equipment (CPAP/BiPAP/ventilation/oxygen) to general medical supplies, durable equipment rentals (knee walkers, beds, wheelchairs), in-home medical equipment",
        "product_complexity": "PENDING - Requires entity identification"
    },
    "Exloc Instruments, Inc.": {
        "industry": "Hazardous Area Equipment & Intrinsically Safe Solutions",
        "workflow_type": "Distribution - Explosion-Proof Instrumentation",
        "company_description": "Founded 1994, Montgomery, TX. Provides instruments, electronic devices, products designed/approved for hazardous classified locations (flammable gas, dust atmospheres). Partnered with experienced manufacturers in Europe and North America. Serves oil/gas, pharmaceutical, wastewater treatment, food/beverage (distillers, brewers).",
        "product_types": "Hazardous area tablets, smartphones, Wi-Fi, RFID readers, intrinsically safe indicators, isolators, solenoid valves, Ex cameras, portable lights, barcode scanners, process instrumentation, alarm annunciators, beacons, stack lights, LEDs, horns, process machinery, road tanker loading applications. Explosion-proof and intrinsically safe devices.",
        "product_complexity": "Very High - Hazardous area certification expertise (flammable gas/dust atmospheres), intrinsically safe/explosion-proof engineering, multi-manufacturer partnership requiring technical knowledge, regulatory compliance (Ex certifications), diverse applications (oil/gas/pharma/food/beverage), specialized process instrumentation."
    },
    "Back2 International Ltd": {
        "industry": "Ergonomic Office Furniture Distribution - UK Market",
        "workflow_type": "Sales & Services - DSE Assessments & Ergonomic Solutions",
        "company_description": "30+ years providing ergonomic help to companies and individuals. London, England (40 Half Moon Crescent, N1 0TJ). UK's leading supplier of ergonomic office chairs for home/workplace. Authorized dealer: Herman Miller, HAG, Humanscale, Okamura, RH, Lavoro, Luxy, Moll. 5 stars, 1,713 customer reviews.",
        "product_types": "Ergonomic office chairs, standing desks (Lavoro to Nowy Styl range), furniture accessories, ergonomic keyboards/mice, office accessories, recliner chairs, sofas, children's furniture. Premium international brands promoting ergonomics and wellbeing. DSE assessments, DSE training, furniture audit, furniture consultancy, installations, loan chairs.",
        "product_complexity": "High - 30+ years ergonomic expertise, multi-brand authorized dealer (Herman Miller, HAG, Humanscale, etc.), DSE assessment/training services, furniture consultancy, UK market operations, 1,713+ customer relationships, comprehensive ergonomic solutions (chairs/desks/accessories/training)."
    },
    "Caribbean Diagnostics Inc": {
        "industry": "Medical Laboratory Equipment & Service Provider",
        "workflow_type": "Distribution & Service - Caribbean Regional Specialist",
        "company_description": "Cayman company owned by laboratory technologist and physician. George Town, Grand Cayman (Elizabethan Square-Eden House, PO Box 189, KY1-1004). Provides leading medical laboratories with best equipment/service in Caribbean region. Addresses regional challenges: hurricanes, customs issues, reagent supply concerns.",
        "product_types": "Medical laboratory equipment and service for Caribbean region laboratories. Equipment supplier and service provider helping laboratories deal with regional challenges. Professional support for Caribbean medical testing facilities.",
        "product_complexity": "Medium-High - Caribbean regional distribution requiring logistics expertise, medical laboratory equipment knowledge, regional challenge management (hurricanes, customs, reagent supply), laboratory technologist/physician ownership, service provider operations across island nations."
    },
    "Prof. Whyte Kratom": {
        "industry": "Botanical Products - Kratom Manufacturing & Retail",
        "workflow_type": "Manufacturing & E-Commerce - Plant-Based Wellness",
        "company_description": "Founded in South Florida. Reputable kratom brand committed to premium plant-based wellness products. Emphasizes quality and transparency. Trusted supplier sourcing with rigorous third-party testing for each batch. Organic sourcing. 21+ only. Products $12-$160 range.",
        "product_types": "Kratom powders (Uplift, Euphoria, Calm, Trainwreck flavors, 100g organically sourced, custom Red/White/Green vein blends), kratom capsules (0.5g per pill, 50-2000 capsule quantities), kratom extracts (K-Plex Tincture Shots 300mg in 15ml bottles, Rogue Punch/Citrus Blast/Blueberry Lemonade flavors), kratom gummies (30 MIT per gummy, 10 gummies per jar $24). Third-party lab tested.",
        "product_complexity": "High - Botanical product formulation requiring custom Red/White/Green vein blending, third-party testing for potency/purity, organic sourcing, multiple product formats (powders/capsules/extracts/gummies), tincture extraction technology, age verification (21+), regulatory compliance, quality control standards."
    },
    "Agralarm, Inc.": {
        "industry": "Agricultural Monitoring & Alarm Systems - Poultry/Livestock",
        "workflow_type": "Installation & Service - Farm Monitoring Solutions",
        "company_description": "Based Salisbury, MD. 30+ years experience installing/providing service to poultry/livestock business owners across Southeast. Serves all major poultry integrators, over 2,200 farms. Contact: 888-968-2802. Tagline: 'Serving the Industry that Feeds the World'.",
        "product_types": "AGRALINK® cloud-based wireless alarm system (flagship product - state-of-the-art alarm notification/detail/control, real-time alerts/updates about farm conditions, AGRALINK Gateway manages barn alarm info/sends to AGRALINK Cloud, all major cellular carriers, supervised backup battery/UPS, IP-67 rating for tough environments), traditional alarm monitoring systems for poultry houses, VOIP services, internet connectivity for poultry industry.",
        "product_complexity": "High - 30+ years agricultural monitoring expertise, cloud-based wireless alarm technology development, multi-cellular carrier integration, ruggest IP-67 environmental rating, backup power systems, 2,200+ farm installations, major poultry integrator relationships, Southeast regional service network, VOIP/internet infrastructure for farms."
    }
}

print(f"Batch 81-90 research data prepared for {len(BATCH_81_90)} companies")
for company in BATCH_81_90:
    print(f"  ✓ {company}")
