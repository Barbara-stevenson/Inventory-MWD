#!/usr/bin/env python3
"""
Batch update for companies 121-130 research data.
"""

BATCH_121_130 = {
    "D. COOPER WORKS, LLC": {
        "industry": "Metal Fabrication & Press Brake Repair",
        "workflow_type": "Custom Fabrication & Equipment Repair - Family-Owned",
        "company_description": "Family-owned/operated since 2003, Pennsylvania (Honey Brook, incorporated). Ephrata, PA operations. Press Brake Repair specialist. Custom fabrication, prototyping, problem solving for commercial/industrial community. Partners with companies specializing in custom replacement parts - niche in restoring older/orphaned equipment. Contact: (717) 733-4220. ~5 employees, $808K annual revenue.",
        "product_types": "Press brake repair services (dedicated solutions for each individual machine), plate metal fabrication, ironwork, welding, industrial prototypes. Table top cheese cutters (cut 5 lb loaves into equal portions), vertical pneumatic cheese cutters. Custom replacement parts for older/orphaned equipment. Poultry processing machinery specialization.",
        "product_complexity": "High - Press brake repair expertise, custom fabrication/prototyping, orphaned equipment restoration (replacement parts sourcing), commercial/industrial problem solving, poultry processing machinery knowledge, cheese cutting equipment manufacturing, pneumatic systems, family-owned operations since 2003."
    },
    "GEN-PRO LLC": {
        "industry": "MULTIPLE COMPANIES - Requires Clarification",
        "workflow_type": "PENDING - Likely Cable/Generator or Livestock Equipment",
        "company_description": "MULTIPLE ENTITIES FOUND: (1) Gen-Pro Gig Harbor WA - TCERDirect™ cable/accessories manufacturing, SmoothStarter™ soft starters, X-Riser™ gas risers (standby generator/solar/pool/spa/EV charger installations, Made in USA, UL Type TC-ER-JP cable), (2) GenPro LLC - generator maintenance/service (telecommunications/healthcare/government/commercial standby generators), (3) GENEPRO Inc - global reproductive technology (livestock supplies engineering/manufacturing), (4) GenPro Energy Solutions - renewable energy (solar PV/water pumping/purification/LED). Specific 'GEN-PRO LLC' entity requires verification.",
        "product_types": "PENDING - Varies from cables/electrical (TCERDirect™, SmoothStarter™, X-Riser™), to generator services, to livestock reproductive supplies, to renewable energy solutions",
        "product_complexity": "PENDING - Requires entity identification"
    },
    "Inspired Sciences dba thermabliss": {
        "industry": "Spa & Wellness Self-Heating/Cooling Products",
        "workflow_type": "Manufacturing - Patented Mineral Technology",
        "company_description": "20th Anniversary celebration, originally Spa Revolutions. Las Vegas, NV. Inspired Sciences, LLC dba thermabliss. Patented Lava Gel natural mineral energy source (magnesium, iron, salt, water) produces precise heat levels. Mission: empower spas/salons with professional thermal wellness tools making operations more efficient/safe/profitable. Recovers 60+ minutes prep/cleaning/reheating time.",
        "product_types": "Mineral-activated self-heating/cooling spa tools: self-heating Thai herbal compression tools, heat-infused masks, self-heating paraffin treatments (hands/feet in medical-grade mitts), Divine Eyes Self-Heating Mask, natural wood heating chambers. Patented Lava Gel technology (elements of earth). No cords, no hassle. Client-exclusive thermal wellness experiences replacing electrical appliances.",
        "product_complexity": "Very High - 20+ years spa innovation, patented Lava Gel mineral technology, self-heating/cooling engineering (no electrical cords), medical-grade materials, Thai herbal compression expertise, operational efficiency optimization (60+ minutes time savings), spa/salon professional market, natural mineral energy source development (magnesium/iron/salt/water)."
    },
    "Paladin Power Inc": {
        "industry": "Residential & Commercial Energy Storage Systems",
        "workflow_type": "Design & Manufacturing - US Veteran-Owned",
        "company_description": "US Veteran-owned/led. Leading residential/commercial ESS company. 5+ years R&D field testing. $10M+ contracted revenue. Designed/built in USA through strategic JABIL partnership (Tier 1 global manufacturer). Launched 2023 InterSolar and Energy Storage North America Show. California SGIP approved March 2023. Wefunder crowdfunding.",
        "product_types": "Paladin Power ESS (Energy Storage System): complete off-grid system powering all home loads (A/Cs, EV charging, lights, refrigerator, appliances). Only ESS powering 100% home loads including A/Cs/EVs. Stacking system, scalable inverters/batteries. SB24/SB48 configurations. 20-year warranty. Solid-state graphene battery technology (100-year lifespan). 9-13X power of Tesla Powerwall, superior energy efficiency. Inverters, batteries, charge controller, MPPT, power isolation - all in one enclosure.",
        "product_complexity": "Very High - Solid-state graphene battery innovation (100-year lifespan), 100% home load capability (only system on market), scalable inverter/battery stacking technology, 5+ years R&D/field testing, 20-year warranty engineering, 9-13X Tesla Powerwall power, US manufacturing (JABIL partnership), California SGIP compliance, complete off-grid system integration, veteran-owned operations."
    },
    "Simple Solutions and Innovations, Inc.": {
        "industry": "Printing Trades Machinery Repair & Wholesale",
        "workflow_type": "Repair, Maintenance & Distribution - Printhead Specialist",
        "company_description": "Established 1990 in New Britain, PA. Currently Danville, VA (701 Loyal St). Electronic/precision equipment repair and maintenance, machinery/equipment/supplies merchant wholesalers. Printing trades machinery/equipment repair specialization. Website: ssiprintheads.com. Contact: (434) 792-7392.",
        "product_types": "Printing trades machinery/equipment repair services, printhead products/services for printing equipment industry, printing machinery supplies wholesale distribution. Electronic/precision equipment repair and maintenance. Printhead specialization.",
        "product_complexity": "High - 30+ years printing machinery expertise, printhead repair/maintenance specialization, electronic/precision equipment capabilities, printing trades technical knowledge, wholesale distribution operations, merchant wholesaler business model, VA operations."
    },
    "DMITRIY & CO.": {
        "industry": "Luxury Couture Upholstery - Custom Furniture",
        "workflow_type": "Bespoke Manufacturing - Made-to-Order Atelier",
        "company_description": "Founded 2011 by husband-wife team Donna and David Feldman, New York, NY. Modern upholstery atelier, timeless furniture design, exquisite craftsmanship. Three generations mastery from Lower East Side NY. Industry leader couture upholstery/contemporary furniture design. Acquired by Restoration Hardware December 2022 to support RH Couture Upholstery launch.",
        "product_types": "Bespoke made-to-order furniture: sofas, sectionals, lounge/occasional chairs, beds, daybeds, chaises, benches, ottomans, handcrafted fabrics. Distinctive upholstery produced by hand. Customizable details. Couture upholstery specialization. Contemporary furniture design.",
        "product_complexity": "Very High - 3 generations furniture-making mastery, couture upholstery artisan craftsmanship, bespoke made-to-order customization, handcrafted fabric production, contemporary design leadership, New York atelier operations, Restoration Hardware acquisition (December 2022) for RH Couture Upholstery, luxury home furnishing market."
    },
    "Delta Kits, Inc.": {
        "industry": "Windshield Repair & Headlight Restoration Products",
        "workflow_type": "Manufacturing & Training - Professional Systems",
        "company_description": "Leading manufacturer of windshield repair products. Professional windshield rock chip glass repair kits using innovative easy-to-use system. Certified training, exceptional customer service. Free support (telephone/chat), free technical videos/articles. Exhaustive laboratory/field testing for all resins.",
        "product_types": "Professional windshield repair kits/systems (shop/mobile technician): EZ-450D Mobile Pro (cordless rechargeable UV curing light Elite Plus, extensive resin/polish/razor blades/equipment), professional-grade windshield repair resins (proprietary formulations, laboratory/field tested, exceed industry standards), headlight restoration products. Available Amazon. Rock chip/crack repair for car windshields.",
        "product_complexity": "High - Proprietary resin formulation (exhaustive lab/field testing), professional windshield repair system engineering, cordless UV curing light technology, certified training programs, technical support infrastructure (telephone/chat/videos/articles), shop/mobile technician kit variations, auto glass repair industry expertise."
    },
    "CathX Medical, Inc.": {
        "industry": "Medical Device Contract Manufacturing - Catheters",
        "workflow_type": "Design, Prototyping & Manufacturing - Zeus Company",
        "company_description": "Acquired by Zeus Industrial Products June 10, 2021. San Jose, CA. Zeus opened 75,600 sq ft Minnesota facility housing CathX Medical 2023. Single-source contract manufacturer for medical device companies/OEMs. Design engineering services, rapid prototyping, manufacturing, full/sub-assemblies. zeusinc.com/catheter-solutions/.",
        "product_types": "Advanced catheter manufacturing solutions (design to full-scale production): balloon catheters, smart catheters, mapping/diagnostic catheters, energy-delivery catheters. Neurovascular, structural heart, cardiovascular catheter projects. Catheter components, sub-assemblies, products for interventional/surgical procedures. Laser cutting, ablation, welding capabilities (added through acquisition).",
        "product_complexity": "Very High - Advanced catheter design/engineering, rapid prototyping to full-scale production, balloon catheter technology, smart catheter innovation, energy-delivery systems, neurovascular/structural heart/cardiovascular specialization, laser cutting/ablation/welding capabilities, Zeus acquisition integration, 75,600 sq ft Minnesota facility, single-source contract manufacturing, interventional/surgical procedure support."
    },
    "The Equipment Guys, Inc.": {
        "industry": "Strength Training Equipment Manufacturing",
        "workflow_type": "Manufacturing - Exclusive Brand Producer",
        "company_description": "Founded 1995, Newark, OH (185 Westgate Dr, 43055-9313). Exclusive manufacturer of Stray Dog Strength training equipment. Premium brand manufactured in Ohio 15+ years. Weight Room Marketplace and Installation Services. Sporting/athletic goods manufacturing specialization. Contact: (614) 871-9220.",
        "product_types": "Stray Dog Strength brand strength training equipment: dumbbells, weightlifting equipment, weight room equipment. Premium quality manufactured in Ohio. Installation services, weight room marketplace solutions. Sporting and athletic goods.",
        "product_complexity": "Medium-High - 25+ years manufacturing expertise, exclusive Stray Dog Strength brand production, 15+ years premium strength equipment, Ohio manufacturing operations, weight room installation services, dumbbell/weightlifting equipment engineering, sporting goods industry specialization, marketplace solutions."
    },
    "Nationwide Architectural Metals, Inc.": {
        "industry": "Pre-Polished Architectural Metals & Specialty Fabrication",
        "workflow_type": "Supply & Custom Fabrication - One-Stop Metal Supplier",
        "company_description": "Founded 1981, 40+ years experience. One-stop pre-polished metals supplier North America and worldwide. Reputation as single-source solution. Contact: 800-851-5053, metal@namusa.com. Design/build customer focus. Patented products.",
        "product_types": "Pre-polished metals: stainless steel, brass, bronze, aluminum, nickel (sheet/plate various sizes/thicknesses, stock shapes). Custom/satin/mirror finishes. Patented OmniSills elevator door sills (complex specifications for elevator thresholds). Polishing, precision metal cutting services. Applications: exterior walls, large statues, interior lighting fixtures, kitchen prep tables. Specialty fabrication services.",
        "product_complexity": "Very High - 40+ years architectural metals expertise, pre-polished metal specialization (stainless/brass/bronze/aluminum/nickel), patented OmniSills elevator sill technology, custom/satin/mirror finish capabilities, precision metal cutting, worldwide distribution, one-stop supplier operations, complex elevator threshold fabrication, diverse architectural applications, specialty fabrication services."
    }
}

print(f"Batch 121-130 research data prepared for {len(BATCH_121_130)} companies")
for company in BATCH_121_130:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 130/200 companies = 65% complete!")
