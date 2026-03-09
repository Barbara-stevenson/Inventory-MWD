#!/usr/bin/env python3
"""
Batch update for companies 111-120 research data.
"""

BATCH_111_120 = {
    "Grothouse, Inc": {
        "industry": "Luxury Wood Countertops & Butcher Blocks Manufacturing",
        "workflow_type": "Custom Manufacturing - Made in USA",
        "company_description": "25+ years wood surfacing excellence, 50 acre farm facility. Master craftsmen, Made in USA, sustainable/renewable/eco-friendly practices. Featured on This Old House, DIY, HGTV networks. Award-winning products proudly manufactured USA.",
        "product_types": "Custom wood countertops, butcher block countertops, wood bar tops, solid wood tables, floating shelves, stair treads, custom furniture (tables, vanities). 60+ wood species: exotic hardwoods (Wenge, Teak, Zebrawood), American favorites (Walnut, Maple), Live Edge millwork, reclaimed woods (Chestnut, Oak, Heart Pine from Pennsylvania barns). Proprietary Durata® waterproof/scratch-resistant finish. Anvil™ metal gilded wood surfaces (8 metal coatings, imitates metal countertops). Food safe butcher block oil, custom cutting boards.",
        "product_complexity": "Very High - 25+ years master craftsman expertise, 60+ wood species offering, proprietary Durata® waterproof finish technology, Anvil™ metal gilding innovation (8 coatings), reclaimed historic barn wood sourcing, Live Edge millwork artistry, custom furniture design/manufacturing, sustainable eco-friendly USA production, HGTV/This Old House featured."
    },
    "Kuumba Made Inc": {
        "industry": "Natural Botanical Fragrances & Aromatherapy Products",
        "workflow_type": "Manufacturing - Vegan & Cruelty-Free",
        "company_description": "Began 1980 as one-person passion project, grown to nationally recognized brand. Focus: natural beauty, holistic wellness, self-expression. Vegan/cruelty-free (no animal-derived ingredients/testing). Clean, free of harmful chemicals. Long-lasting scent (one application, memorable impression). Available Amazon and kuumbamade.com.",
        "product_types": "Botanical fragrance oils (jojoba oil, safflower oil, fragrance), herbal salves, bath/body oils/lotions, aromatherapy products. Popular fragrances: Persian Garden (warm florals, ocean air, light amber), Egyptian Musk (light/sensual, fresh water/sandalwood), Vanilla Bean (creamy/sweet), Frankincense & Myrrh, Oriental Musk, Wind Dancer. Sizes: 1/8 oz, 1/2 oz, larger bottles. Vegan, long-lasting, skin-nourishing formulas.",
        "product_complexity": "Medium-High - 40+ years botanical fragrance expertise, vegan/cruelty-free formulation, clean chemistry (no harmful chemicals), long-lasting scent technology, jojoba/safflower oil base, holistic wellness product development, national brand recognition, multi-channel distribution (direct/Amazon), diverse fragrance portfolio."
    },
    "Wonky Confections LLC": {
        "industry": "Delta-8 THC Edibles Manufacturing",
        "workflow_type": "Food Manufacturing - Cannabis Products",
        "company_description": "North Dakota company (4225 38TH ST SW SHOP A AND B FARGO, ND 58104), Minnesota branch (Moorhead facility). Manufactures ready-to-eat human food products containing Delta-8 tetrahydrocannabinol (THC). Relationship with Alpine Hemp (CBD products). FDA warning letter issued July 2023 for product adulteration.",
        "product_types": "Delta-8 THC products under 'Wonky Weeds' brand: 'Death by Gummy Bears', 'Wonky Weeds' gummy bear products. Ready-to-eat Delta-8 THC human food products. Separate from but related to Alpine Hemp's CBD product line.",
        "product_complexity": "High - Delta-8 THC product formulation, ready-to-eat food manufacturing requiring FDA compliance, gummy bear production technology, cannabis/hemp industry regulatory navigation, FDA warning letter response/remediation, multi-state operations (ND/MN), relationship management with CBD companies."
    },
    "U.S. Testing Equipment, Ltd.": {
        "industry": "Security Screening Technology & Detection Equipment",
        "workflow_type": "Distribution & Service - Checkpoint Security",
        "company_description": "Established 1995, Pacific Northwest's premier provider security screening systems/technology. Recognized leader in Detection Security market. Works closely with TSA, Department of Homeland Security, Military locations across country. Installation, training, on-going maintenance, repair solutions. Partnerships with manufacturing leaders.",
        "product_types": "Checkpoint security technology: Walk Through Metal Detectors, Hand Held Metal Detectors, Security X-ray, Explosive Trace Detection (ETD) devices, Automatic Under Vehicle Inspection Systems (AUVIS), Personnel Screening, Bio-Detection systems. Partners: Morpho Detection, Rapiscan Systems, CEIA, L3 Communications, Gatekeeper Security, Alvarado, Armstrong Monitoring. Serves air cargo, military, TSA, events/stadiums, corrections, critical infrastructure.",
        "product_complexity": "Very High - 25+ years security screening expertise, TSA/DHS/Military partnerships, cutting edge detection technology distribution, explosive trace detection systems, AUVIS engineering, bio-detection capabilities, multi-manufacturer relationships (Morpho/Rapiscan/CEIA/L3), installation/training/maintenance services, critical infrastructure protection, diverse industry serving (air cargo/military/events/corrections)."
    },
    "Nadalie USA": {
        "industry": "Oak Barrel Cooperage - Wine & Spirits",
        "workflow_type": "Manufacturing & Importing - Artisan Craftsmanship",
        "company_description": "Producing American/Eastern European oak barrels in Napa Valley since 1980. Imports French oak products from cooperages in Bordeaux and Marsannay. Pennsylvania milling, 24+ month seasoning before Calistoga facility. 50%+ artisans producing barrels 25+ years. Acquired Barrel Builders (Napa Valley cooperage). Exports worldwide.",
        "product_types": "American/Hybrid/Eastern European oak barrels (hand-crafted by experienced coopers), French oak imports, oak tanks, barrel alternatives (oak chips, stave inserts for stainless steel vessels). Solution line: Expression Rouge with Satin toast (80% Vosges Forest tight-grain, 20% Allier Forest staves). Oak sources: Virginia, Pennsylvania, Minnesota, Missouri forests. 24+ month wood seasoning.",
        "product_complexity": "Very High - 40+ years cooperage expertise, American oak milling/seasoning (24+ months), artisan hand-craftsmanship (50%+ with 25+ years experience), French cooperage imports (Bordeaux/Marsannay), hybrid barrel innovation, oak tank engineering, barrel alternative development, worldwide export operations, Napa Valley/Pennsylvania dual facilities, Barrel Builders acquisition integration."
    },
    "Sumake North America LLC": {
        "industry": "Industrial Assembly Tools & Pneumatic Equipment",
        "workflow_type": "Exclusive Distribution & Service - North America",
        "company_description": "Exclusive authorized Sumake distributor USA, Mexico, Canada. President: Michael DeChambeau. Factory authorized repairs, parts, calibration service for all Sumake industrial tools/accessories/torque assembly products. Serves manufacturing, assembly, automotive industries.",
        "product_types": "Industrial torque tools, industrial air tools, accessories. Comprehensive selection: air/electric/cordless torque screwdrivers, torque meters, torque arms, stands, screwfeeders, industrial air impact wrenches, sanders/buffers, grinders, ratchet wrenches, nippers, tapping tools. CE certified: Impact Wrenches, Ratchet Wrenches, Drills, Grinders, Hammers, Sanders, Screwdrivers, Spray Guns, Riveters, Nail Guns, Bradders. Professional high quality suited to wide range assembly applications.",
        "product_complexity": "High - North America exclusive distribution (USA/Mexico/Canada), factory authorized service/calibration capabilities, industrial torque tool expertise, comprehensive CE certified product line, diverse tool categories (pneumatic/electric/cordless), assembly application specialization, repair/parts/calibration services, professional industrial quality standards."
    },
    "VoltAire Systems, LLC": {
        "industry": "Thermal Management & Cabinet Cooling Systems",
        "workflow_type": "Manufacturing - Industrial HVAC Specialist",
        "company_description": "Apopka, FL USA manufacturing. 40+ years thermal management/controls industry experience. Experts in thermal management/cabinet cooling for telecom/industrial markets. One of few providers offering air conditioners, heat exchangers, pressurization units. UL standards compliance.",
        "product_types": "Industrial air conditioners/heat exchangers (NEMA cabinets, manufacturing controls, industrial systems cooling, 1,000-19,000 BTUh, industrial coatings/stainless-steel units), Heat exchangers (HIX Series Cross Flow, HTC Series Counter Flow - high efficiency/performance closed airflow loop), Pressurization units, Industrial control panels. Serves oil/gas, telecommunications, industrial, manufacturing controls. Small air conditioners for critical elements.",
        "product_complexity": "Very High - 40+ years thermal management expertise, industrial air conditioner design/manufacturing (1,000-19,000 BTUh range), heat exchanger engineering (cross flow/counter flow), pressurization unit development, industrial control panel integration, UL standards compliance, NEMA cabinet specialization, oil/gas/telecom/industrial applications, USA manufacturing (Apopka, FL), complete thermal management solution offering."
    },
    "Angels' Share Wine Imports LLC": {
        "industry": "Boutique Wine Importing & Distribution",
        "workflow_type": "Import & Distribution - Small Production Focus",
        "company_description": "Founded 2004 in Red Hook, Brooklyn by Mark Snyder (music industry to wine distribution). Two regional divisions: Angels Share Wine 'North' (Brooklyn serving NY/NJ/CT) and Angels Share Wine 'South' (Orlando, FL - 1700 35th Street, Unit #109, orders@aswsouth.com serving FL). Focus: small-production, high-quality wines.",
        "product_types": "Exceptional American wineries, curated selection European domaines. Boutique, hand-crafted wines from American/European producers. Small-production, high-quality wines specialization. Wine, beer & spirits distribution.",
        "product_complexity": "Medium-High - 20+ years boutique wine curation expertise, dual regional operations (NY/NJ/CT and FL), American winery/European domaine portfolio, small-production wine sourcing, hand-crafted wine specialization, multi-state distribution logistics (NY/NJ/CT/FL), industry career transition (music to wine) unique perspective."
    },
    "Magnum Automotive Equipment": {
        "industry": "Automotive Lift Equipment Manufacturing",
        "workflow_type": "Manufacturing - Multi-Category Lifts",
        "company_description": "Manufactures premium automotive lifts for all purposes: residential parking solutions to portable mechanic lifts. Complete offering automotive, truck, specialty lift options. Attractive price point with parts/labor warranty. Quality construction (heavy-duty leaf chain, steel pulleys, high-strength cable equalization).",
        "product_types": "Two-Post Lifts (9,000 lb, 11,000 lb capacities, heavy-duty leaf chain, steel pulleys, high-strength cable equalization), Four-Post Lifts ('Deluxe Series' 7,000-9,000 lb capacity, aircraft quality cables rated 14,500 lbs, storage/service), Specialty Lifts (Mid-rise for cars/vans/light-duty trucks, tire/wheel/brake repairs, collision repair, new car prep), Single Post Lifts (4,500 lb, 6,000 lb models, custom configurations). Quality construction with warranty.",
        "product_complexity": "High - Multi-category lift engineering (two-post/four-post/specialty/single-post), capacity range 4,500-11,000+ lbs, heavy-duty component specifications (leaf chain/steel pulleys/aircraft cables), safety feature integration, residential/commercial applications, collision repair/service versatility, custom configuration capabilities, parts/labor warranty program."
    },
    "Veda Farming Solutions": {
        "industry": "Agricultural Equipment Sales - Innovative Farming Implements",
        "workflow_type": "Sales & Distribution - Sustainability Focus",
        "company_description": "20+ years technical/logistical experience in agricultural market. Salinas, CA (63 Monterey Salinas Hwy). Mission: give farmers great mechanical alternatives to face today's agricultural challenges. Reduce fuel cost, labor cost, environmental impact while increasing production, quality, sustainability. Tractors as central mobile power sources.",
        "product_types": "Innovative farming equipment: Shredders, Reverse Tillers, Rippers, Weeders, hemp transplanting machines, weeding machines. Organic farming machines (ground prep, weed control, plastic management, harvesting). Farm implements for all types farming/agricultural services including organic/hemp farming. Focus: reducing operating costs, improving efficiency.",
        "product_complexity": "High - 20+ years agricultural market expertise, innovative farming implement specialization, organic farming technology (ground prep/weed control/plastic management/harvesting), hemp farming equipment, sustainability-focused engineering (fuel/labor/environmental cost reduction), tractor-based mobile power solutions, California agricultural market operations (Salinas), diverse implement portfolio."
    }
}

print(f"Batch 111-120 research data prepared for {len(BATCH_111_120)} companies")
for company in BATCH_111_120:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 120/200 companies = 60% complete!")
