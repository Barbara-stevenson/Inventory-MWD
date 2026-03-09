#!/usr/bin/env python3
"""
Batch update for companies 181-190 research data.
"""

BATCH_181_190 = {
    "Boeckeler Instruments, Inc.": {
        "industry": "Scientific Sample Preparation Equipment Manufacturing",
        "workflow_type": "Manufacturing - Nanoscale Research Equipment",
        "company_description": "Tucson, AZ (4650 S Butterfield Dr). Privately-owned. 26 employees. Acquired Research and Manufacturing Company (RMC) at turn of millennium, bringing ultramicrotome technology. Engineers sample preparation equipment for nanoscale research. RMC Boeckeler product line. Life sciences/materials research emphasis. Website: boeckeler.com.",
        "product_types": "Ultramicrotomy/microtomy solutions, workflow instruments, accessories for sample preparation. Automated tissue processors, glass knife makers, VIA® video measuring/marking devices/software (positioning measuring lines/pointers over images to measure critical features/compare samples). 3D electron microscopy sample preparation. Life sciences/materials research equipment.",
        "product_complexity": "Very High - Nanoscale research equipment engineering, ultramicrotome technology (RMC acquisition), automated tissue processor design, glass knife maker manufacturing, VIA® video measuring/marking software, 3D electron microscopy sample preparation, life sciences/materials research specialization, Tucson AZ operations, RMC Boeckeler brand integration."
    },
    "Stella Lighting Inc": {
        "industry": "LED Task Lamp Design & Manufacturing",
        "workflow_type": "Proprietary Design & Manufacturing - Patented Technology",
        "company_description": "Founded 4/25/2012 by Nathan Wiedenmann (President & Founder). Springfield, OR (88141 Chita Loop). Grown from idea to global company. 16 patents for uniquely-designed LED lamps. In-house design based on direct user feedback. NAMTA Business Innovation Award. Philips Lumiled high performance LEDs. 2-year warranty.",
        "product_types": "LED task lamps: Stella SKY Floor Lamp, Stella GO (wireless charging portable lamp). Features: top-class tri-spectrum technology, multi-stage dimming, adjustable necks, 50,000+ hours LED lifespan, low heat, low energy use (10-14 watts). Philips Lumiled LEDs (brightest marketplace). Vision/eye health optimized. Portable/floor lamp variations.",
        "product_complexity": "Very High - 16 patented LED lamp designs, proprietary tri-spectrum technology, Philips Lumiled high-performance LED integration, 50,000+ hour lifespan engineering, wireless charging innovation (Stella GO), multi-stage dimming systems, adjustable neck mechanisms, vision/eye health optimization, in-house design philosophy, NAMTA Business Innovation Award, 10-14 watt energy efficiency, global distribution, Springfield OR manufacturing."
    },
    "American Engineering Group Ltd": {
        "industry": "Engineering Solutions & Products - Water & Renewable Energy",
        "workflow_type": "Product Design, Engineering & Marketing - Hyde Park Partners",
        "company_description": "Established 2014. Hyde Park Partners holding company owns/provides corporate resources. AEG International operations. Serves nations throughout Africa (including Tanzania) and worldwide. Comprehensive service range: product design/development to engineering analysis/manufacturing/marketing. Website: hydeparkpartners.us.",
        "product_types": "Engineered products/expert engineering solutions: water purification, renewable energy solutions, industrial technologies. CAD/CAM/CAE expertise including finite element analysis (FEA/CFD) consulting. Products improving efficiency/quality of life. Global markets focus (Africa/worldwide).",
        "product_complexity": "Very High - Water purification system engineering, renewable energy solution development, industrial technology products, CAD/CAM/CAE expertise, finite element analysis (FEA/CFD) consulting, product design/development/manufacturing/marketing integration, Africa market specialization (Tanzania), worldwide distribution, Hyde Park Partners corporate structure, AEG International operations."
    },
    "Pipefusion Services Inc.": {
        "industry": "HDPE Pipe Fusion Services & Custom Fabrication",
        "workflow_type": "Field Services & Manufacturing - Polyethylene Specialist",
        "company_description": "35+ years experience. North America subject matter experts in pipe fusion (company named after process). Custom plastics company using HDPE with heat extrusion welding. Trained in all heat fusion techniques/field conditions. Alert (arctic circle) to deep Texas operations. Website: pipefusion.com.",
        "product_types": "HDPE pipe fusion services (on-site pipe fusion), custom HDPE fabrication. High-density polyethylene pipe supply/fusion. All heat fusion techniques. Standard/custom components/fittings/joining systems. Creates homogenous system matching HDPE pipe technical/environmental specifications. Industrial/mechanical applications. Leak risk minimization.",
        "product_complexity": "Very High - 35+ years HDPE pipe fusion expertise, all heat fusion technique mastery, extreme environment capabilities (arctic to Texas), heat extrusion welding for custom fabrication, North America subject matter expert status, on-site field fusion services, custom component/fitting/joining system integration, homogenous system creation, industrial/mechanical application specialization, leak prevention engineering."
    },
    "HOLDiT Marketing & Manufacturing": {
        "industry": "Point of Sale Displays & Shelf Edge Systems - South Africa",
        "workflow_type": "Manufacturing - Retail Signage Inventor",
        "company_description": "Founded 1986 by Paul Woodley (inventor of original self-adhesive Shelf STRiP™). Family owned/run. Port Elizabeth, South Africa (1 Homestead Rd, Kya Sand, Randburg, 2163). Contact: +27 11 244 1600. Premier POS equipment manufacturer. Website: holdit.co.za.",
        "product_types": "Point of Sale displays: shelf strips, POS signage, promotional/custom signage. STRiP™ (original self-adhesive shelf edge data strip, invented 1986). Shelf Edge strips/Data Strips for retail price presentation. Label holder strips/systems (easy to use, durable, practical). Continuing innovation in retail signage.",
        "product_complexity": "High - STRiP™ invention/patent (1986 original self-adhesive shelf edge), 35+ years POS equipment manufacturing, shelf edge data strip innovation, self-adhesive technology, family-owned operations, South Africa manufacturing (Port Elizabeth/Randburg), retail signage specialization, promotional/custom signage capabilities, label holder system engineering."
    },
    "O.K. Foundry Co., Inc.": {
        "industry": "Gray & Ductile Iron Castings - Historic Restoration Specialist",
        "workflow_type": "Foundry Manufacturing - Family-Owned Since 1912",
        "company_description": "Founded 1912 by James N. O'Neil Sr. (Richmond railroad/industrial/agricultural equipment). Incorporated 1956 Virginia Corporation. O'Neil family owned/operated. Richmond, VA. Induction melting since 1976. No Bake resin sand molding line 1979. 2010 ExOne S-Max 3D sand printer (largest at time). Richmond Iron brand.",
        "product_types": "Gray/ductile iron castings: sculpture, columns/capitals, fencing, bollards, stanchions, mantels, fireplaces, chimneys/accessories. Historic restoration, municipal fixture, architectural castings. NYC subway lamp poles/railings (Richmond Iron brand). No-bake molding (25-250 lbs, 50-250 piece runs). 700kw induction melting, two 2,000 lb tilt pour furnaces. 3D sand printing.",
        "product_complexity": "Very High - 110+ years foundry heritage, gray/ductile iron casting expertise, 700kw induction melting (since 1976), No Bake resin bonded sand molding (1979), ExOne S-Max 3D sand printer technology (2010), historic restoration specialization, NYC subway lamp pole/railing manufacturing (Richmond Iron brand), O'Neil family operations, architectural casting mastery, municipal fixture production."
    },
    "Sylva Corporation, Inc.": {
        "industry": "Forest Products Manufacturing - Mulch & Engineered Wood Fiber",
        "workflow_type": "Manufacturing & Wholesale - Family-Owned",
        "company_description": "Founded 1997, Princeton, MN. Family-owned forest products innovator. 25+ years midwest region operations. Affiliate: Wood Chip of Princeton. Website: sylvacorp.com.",
        "product_types": "Bulk Mulch, Bagged Mulch, Bagged Soil, SoftStep® Engineered Wood Fiber (playground surfacing). Soils, composts, organic soil amendments. Bedding for dairy/poultry industry. Prepared wood fuel for alternative energy markets. Landscape mulches. Engineered wood fiber playground surfacing.",
        "product_complexity": "High - 25+ years forest products expertise, SoftStep® Engineered Wood Fiber proprietary product (playground surfacing), bulk/bagged mulch production, soil/compost/organic amendment manufacturing, dairy/poultry bedding specialization, wood fuel for alternative energy, Wood Chip of Princeton affiliate operations, family-owned midwest manufacturing, diverse product applications (landscape/agriculture/energy/playground)."
    },
    "MyTCoat Commercial Outdoor Furniture": {
        "industry": "Commercial Outdoor Furniture Manufacturing - Proprietary Coating",
        "workflow_type": "Manufacturing - Whitney, TX Operations",
        "company_description": "Founded by Robert Webb, Rodney Webb, Troy Stephens. Whitney, TX. 60 years combined industry experience. American manufacturer. Proprietary Advantage Coating (no PVC/phthalates, 7-year warranty, 13 colors). Website: mytcoat.com.",
        "product_types": "Commercial outdoor furniture: picnic tables, park benches, trash receptacles, grills, outdoor furnishings. Advantage Coating (proprietary, won't chip/crack/peel, no drips/runs). Powder coated frames (rust resistant). Non-porous surface (immune to stains/fungus/mold/dirt/acids/salts/seawater). UV/fade resistant, won't crack/peel/warp.",
        "product_complexity": "Very High - Proprietary Advantage Coating technology (no PVC/phthalates, 7-year warranty), 60 years combined founder expertise, non-porous surface engineering (stain/fungus/mold/dirt/acid/salt/seawater immune), UV/fade resistance, powder coating systems, rust prevention, American manufacturing (Whitney, TX), commercial outdoor furniture specialization, 13-color coating options."
    },
    "Stanwood Redi-Mix, Inc.": {
        "industry": "Ready-Mixed Concrete Production & Delivery",
        "workflow_type": "Manufacturing & Distribution - Family-Owned Since 1966",
        "company_description": "Founded 1966, Stanwood, WA (2431 Larson Rd). Third generation ownership. Local family-owned/operated. Leading producer ready-mixed concrete in area. Contact: 360-652-7777, info@stanwoodredi-mix.com. Residential/commercial clients. Website: stanwoodredi-mix.com.",
        "product_types": "Ready-mixed concrete (regular/custom colors), sand, gravel, crushed rock, ecology blocks. Insulated concrete forms (ICF) specialization. Pickup/delivery services. Residential/commercial concrete products. Quality materials, customer service focus.",
        "product_complexity": "High - 55+ years concrete production expertise, third generation family ownership, ready-mixed concrete manufacturing (regular/custom colors), insulated concrete forms (ICF) specialization, sand/gravel/crushed rock supply, ecology block production, pickup/delivery logistics, Stanwood WA operations, residential/commercial serving, long-term business relationship building."
    },
    "Urban Front Ltd": {
        "industry": "Designer Hardwood Door Manufacturing - Bespoke Front Doors",
        "workflow_type": "Handcrafted Manufacturing - UK Made",
        "company_description": "Chesham, Buckinghamshire, UK. 20 years modern door design/manufacturing innovation. Family business, young enthusiastic designer/craftsman team. Handcrafted in UK workshop. All doors designed in-house. Shipped worldwide. LPS1175 Grade 2 security testing, Secured by Design certified. Made in Britain.",
        "product_types": "Bespoke hardwood front doors: contemporary/modern/wooden front doors, internal doors, garage doors. Solid wood, designer doors. Double steel reinforcement, unique ventilation system (prevents movement/warping). High-performance specification. Personalized advice/flexibility for perfect door creation. Made to measure. Raw/Form collections.",
        "product_complexity": "Very High - 20 years modern door design innovation, bespoke handcrafted manufacturing, in-house design team, double steel reinforcement engineering, unique ventilation system (warping prevention), LPS1175 Grade 2 security certification, Secured by Design accreditation, UK workshop (Chesham, Buckinghamshire), worldwide shipping, family business operations, solid hardwood specialization, high-performance specification, made-to-measure customization."
    }
}

print(f"Batch 181-190 research data prepared for {len(BATCH_181_190)} companies")
for company in BATCH_181_190:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 190/200 companies = 95% complete!")
