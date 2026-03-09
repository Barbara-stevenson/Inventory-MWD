#!/usr/bin/env python3
"""
Batch update for companies 141-150 research data.
"""

BATCH_141_150 = {
    "MHQ of Arizona": {
        "industry": "Emergency Vehicle Equipment & Upfitting",
        "workflow_type": "Manufacturing & Service - Turnkey Solutions",
        "company_description": "Family-owned business with locations in Arizona and New Mexico. Serves western law enforcement, fire services, public works, highway departments, housing authorities, utility companies, environmental safety, emergency medical services. Streamlined team-build approach. Service area: NM, AZ, TX, CO, UT, NV, CA and beyond.",
        "product_types": "Emergency vehicle equipment, lighting, upfitting services. Turnkey approach handling vehicle selection, custom graphics, equipment installation under one roof. Commercial-grade materials, industry-best techniques. Vehicles built to withstand demanding emergency response conditions.",
        "product_complexity": "High - Turnkey emergency vehicle upfitting (selection/graphics/installation), commercial-grade materials engineering, multi-state service area (7+ states), family-owned streamlined operations, law enforcement/fire/EMS/public works specialization, custom graphics design, industry-best installation techniques."
    },
    "Artemis Bio-Solutions LLC": {
        "industry": "Bio-Technology Decontamination & Remediation Solutions",
        "workflow_type": "Manufacturing - Sandia National Labs Licensed Technology",
        "company_description": "Founded 2013, Wood Dale, Illinois. Bio-technology company offering next generation extremely safe decontamination/disinfection/deodorization solutions with high effectiveness and unprecedented efficacy. Predecessor introduced patented Sandia National Labs DF-200 formulation to insurance/restoration industry. Supplies international customers.",
        "product_types": "Bio-Oxygen® Chem Decon (flagship product exclusively licensed from Sandia National Laboratories, EPA-registered on List N and List Q). Solutions for: mold remediation, cleaning/disinfecting, fire smoke damage, illicit drug cleanup, trauma biohazard decontamination. Restoration, remediation, decontamination products/services.",
        "product_complexity": "Very High - Sandia National Labs exclusive license, patented DF-200 formulation, EPA-registered (List N and List Q), bio-technology decontamination innovation, trauma biohazard expertise, illicit drug cleanup specialization, mold remediation technology, fire smoke damage restoration, insurance/restoration industry focus."
    },
    "ENZ USA  INC": {
        "industry": "Sewer & Pipe Cleaning Equipment - Water Jetting Technology",
        "workflow_type": "Distribution & Manufacturing - Swiss Engineering",
        "company_description": "Aurora, Illinois (1585 Beverly Court, Unit 115). US subsidiary of Swiss company established 1985. 95% products developed/manufactured in Switzerland. Worldwide leader in sewer/pipe cleaning equipment up to 36,000 PSI. Serves 50+ countries. Subsidiaries: Germany, Sweden, UK, USA.",
        "product_types": "Swiss-made water jetting nozzles & water blasting tools: standard nozzles, rotating nozzles, wire rope/chain scrapers, milling cutters, camera nozzles, hydro excavation nozzles. CrossJet Technology UC Line (heat exchangers, clogged pipes in industrial settings). Applications: sewer cleaning, pipe cleaning, plumbing, industrial plants/municipalities, chemical/oil/petrochemical industries, nuclear power plants. Sizes 1/8\" to 1/2\", up to 36,000 PSI.",
        "product_complexity": "Very High - Swiss-made precision engineering (95% Switzerland manufacturing), worldwide leader status, 36,000 PSI high-pressure systems, CrossJet Technology innovation, multi-application expertise (sewer/industrial/nuclear), camera nozzle integration, hydro excavation technology, global distribution (50+ countries), hardened steel/ceramic insert engineering."
    },
    "JAFE Decorating Inc.": {
        "industry": "Custom Glass Decorating & Candle Fulfillment",
        "workflow_type": "Manufacturing - Commercial Glassware Decoration",
        "company_description": "Founded 1978, Greenville, Ohio. Industry leader in commercial glassware decorating for 40+ years. 67,000 square foot facility with 4 state-of-the-art robotic spray lines. Serves candle, skincare/beauty care, beverage/spirit markets. USA-made, eco-friendly glass decoration services. Member National Candle Association.",
        "product_types": "Custom glass decorating solutions: screen printing on glass, painting, packaging. Full-service candle fulfillment (glass decorating + fragrance filling). Decorated candle jars, perfume/fragrance bottles, cosmetic containers, beverage/spirit bottles. 20+ different decoration techniques in thousands of colors. All shapes/sizes of glassware. Private label solutions.",
        "product_complexity": "Very High - 40+ years glassware decoration expertise, 4 robotic spray lines (67,000 sq ft facility), 20+ decoration techniques, thousands of color options, full-service candle fulfillment integration (decorating + filling), eco-friendly USA manufacturing, skincare/beauty/beverage/spirit market specialization, private label capabilities."
    },
    "Photovac Laser Corporation, Inc.": {
        "industry": "CO2 Laser Repair & Remanufacturing Services",
        "workflow_type": "Service & Remanufacturing - Global Third-Party Provider",
        "company_description": "Founded 1994, Grove City, Ohio (3513 Farm Bank Way). Leading provider of CO2 laser repair/remanufacturing for all major laser/engraver brands. Global reach: North/South America, Europe, Asia. Premier service firm supporting aerospace, automotive, electronics manufacturing, packaging, medical device fabrication, scientific research. President: Christopher Zelich.",
        "product_types": "CO2 laser repair/remanufacturing services (all major brands): DC power supplies/modules, RF exciters, RF laser tubes, engravers, scientific glass services. CO₂ laser tube remanufacturing, RF power system repair, precision gas refill services. Expert-level support for aerospace/automotive/electronics/packaging/medical device/scientific sectors.",
        "product_complexity": "Very High - 30+ years CO2 laser expertise, worldwide third-party provider (Americas/Europe/Asia), all major brand compatibility, RF power system repair specialization, precision gas refill technology, laser tube remanufacturing, scientific glass services, aerospace/automotive/medical device market serving, DC/RF power supply expertise."
    },
    "SWS Detention Group Inc": {
        "industry": "Correctional Facility Equipment Distribution & Contracting",
        "workflow_type": "Distribution & Installation - Canadian Market Leader",
        "company_description": "Founded 1999, Winnipeg, MB (1-2120 Notre Dame Ave). One of most successful Canadian providers/distributors/contractors of intensive use products/services nationwide. Factory Certified Detention Equipment Contractor. Exclusive distributor of Norix Furniture in Canada. Serves correctional facilities, behavioral healthcare, education, transitional housing.",
        "product_types": "Correctional facility furniture/detention product solutions: furniture, pillows, mattresses, personal care, fitness equipment, eco-security utensils, security/detention accessories/hardware. Norix Furniture exclusive Canadian distribution. Replacement locks/parts, maintenance advice/documentation, maintenance training/service, pneumatic locks, sliding devices.",
        "product_complexity": "High - 25+ years corrections industry expertise, Factory Certified Detention Equipment Contractor status, Norix Furniture exclusive Canadian distribution, intensive use product specialization, nationwide Canadian operations, multi-sector serving (corrections/behavioral healthcare/education/transitional housing), maintenance training/service capabilities."
    },
    "PSI Pressure Systems, LLC": {
        "industry": "High-Pressure Water-Blasting Equipment Manufacturing",
        "workflow_type": "Manufacturing - Patented Fluid End Technology",
        "company_description": "Founded 2013 by Todd A. Shawver (formerly Union Pump Textron and NLB Corp). Full service waterblasting equipment manufacturer. Major source in water-blasting industry for equipment, technology, services. Manufactures high-pressure pumps 8,000-40,000 PSI (552-2,800 bar).",
        "product_types": "NX-Series high-pressure pumps (patented fluid end conversion system, only pump in world capable of 8,000-40,000 PSI operation with single discharge manifold). Applications: tank cleaning, surface preparations, tube bundle cleaning, pipe cleaning/cutting, hydrodemolition. Water jetting equipment for various industrial applications.",
        "product_complexity": "Very High - Patented NX-Series fluid end conversion technology (only pump worldwide 8,000-40,000 PSI single manifold operation), hydrodemolition equipment engineering, tank/tube bundle cleaning systems, pipe cutting capabilities, founder expertise from Union Pump Textron/NLB Corp, full service manufacturing operations."
    },
    "GEX Corporation": {
        "industry": "Dosimetry Products & Radiation Measurement Services",
        "workflow_type": "Manufacturing & Laboratory Services - ISO 17025 Accredited",
        "company_description": "Founded 1991. Single source provider of complete dosimetry products/services for radiation processing industry. International standards laboratory accredited by NVLAP to ISO/IEC 17025:2017 for calibrations/dose measurements (0.100 kGy to 100 kGy). Serves gamma, e-beam, X-ray radiation process applications.",
        "product_types": "Proprietary B3 radiochromic film dosimeter (dose range <1.0 kGy to >150 kGy), alanine pellets/tubes, CTA film, GEX Radiation Indicators (Type 1 process chemical indicators, visual color change), calorimeters, calibration phantoms. Turnkey dosimeter batch calibration services. Applications: medical device sterilization, surface sterilization, ink/coating curing, food irradiation.",
        "product_complexity": "Very High - Proprietary B3 radiochromic film technology, ISO/IEC 17025:2017 NVLAP accreditation, international standards laboratory, 30+ years dosimetry expertise, gamma/e-beam/X-ray radiation specialization, medical device sterilization calibration, food irradiation measurement, turnkey calibration services, 0.100-100 kGy range."
    },
    "EGE Products": {
        "industry": "Agricultural Spray Adjuvants & Micronutrients Manufacturing",
        "workflow_type": "Manufacturing - Family-Owned Agricultural Innovation",
        "company_description": "Founded 2007, Minneola, KS. Family owned/operated agricultural business serving rural America. Fixture of agricultural innovation. Manufactures quality spray adjuvants & micronutrients. Focuses on enhancing effectiveness of agricultural spray applications and crop nutrients.",
        "product_types": "Spray adjuvants: encapsulators (protection for active ingredients in chemical applications), drift control, surfactants, water conditioners for accurate/efficient chemical applications. Fertilizers tailored to specific crop needs (developed with agricultural chemistry advancements). Micronutrients. Agricultural oils.",
        "product_complexity": "Medium-High - Encapsulator technology for active ingredient protection, spray adjuvant formulation expertise, micronutrient development, crop-specific fertilizer tailoring, agricultural chemistry innovation, drift control engineering, surfactant/water conditioner specialization, 15+ years agricultural market serving, family-owned operations."
    },
    "VIRGINIA LAB SUPPLY CORPORATION": {
        "industry": "Laboratory Equipment, Supplies & Chemicals Distribution",
        "workflow_type": "Distribution & Manufacturing - Multi-Industry Specialist",
        "company_description": "Founded 1982, Richmond, VA (5400 Byrdhill Rd). Family owned business selling lab products for 25+ years. Also does business as Q/C Resource. HubZone Business, Small Business, Small Disadvantage Business, Woman Owned Business certifications. Serves every type of industry. Contact: (804) 261-3700.",
        "product_types": "ALL laboratory equipment, supplies and chemicals. Testing equipment, chemicals and supplies for every industry type. Professional equipment distribution: drafting instruments, laboratory equipment, scientific instruments. Comprehensive lab product portfolio.",
        "product_complexity": "High - 40+ years laboratory distribution expertise, comprehensive ALL lab equipment/supplies/chemicals offering, multi-industry serving (every industry type), woman-owned small disadvantage business, HubZone Business certification, manufacturing/distribution dual capabilities, Q/C Resource brand, family-owned operations, Richmond VA regional focus."
    }
}

print(f"Batch 141-150 research data prepared for {len(BATCH_141_150)} companies")
for company in BATCH_141_150:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 150/200 companies = 75% complete!")
