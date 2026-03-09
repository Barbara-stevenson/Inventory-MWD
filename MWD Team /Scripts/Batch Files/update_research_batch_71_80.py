#!/usr/bin/env python3
"""
Batch update for companies 71-80 research data.
"""

BATCH_71_80 = {
    "Hundegger USA LLC": {
        "industry": "CNC Timber Construction Machinery Manufacturing",
        "workflow_type": "Sales & Service - Advanced Joinery Equipment",
        "company_description": "US branch of Hans Hundegger AG (world market leader with 90%+ market share). Founded 2001, Charleston, UT. Over 5,300 Hundegger machines worldwide. Serves Mass Timber, CLT, Timber Frame Joinery, Wood Truss, Panel saws, EWP saws, off-site construction facilities.",
        "product_types": "CNC-controlled joinery machines, automatic cutting machines, planers, gantry-style machine centres, automatic panel processing machines, solid wood wall production lines (WALL-Master), robotic systems (ROBOT-Max, ROBOT-Compact), SPM-2 Speed Panel Machine, Turbo Drive II linear saw, profiled wood element production lines, handling systems. All timber construction sectors: carpentry, contract joinery, timber frame, log house, prefabricated house, glulam joinery, playground equipment.",
        "product_complexity": "Very High - World-leading CNC timber construction technology, 90%+ market share, automated robotic systems, complex CAD/CAM integration, mass timber production equipment, highly specialized engineering requiring expert installation and support."
    },
    "Conveyor Technology": {
        "industry": "MULTIPLE COMPANIES - Requires Clarification",
        "workflow_type": "PENDING - Likely Conveyor Systems Design/Manufacturing",
        "company_description": "MULTIPLE ENTITIES FOUND: (1) US Conveyor Technologies - complete system design firm, Mackinaw IL, founded 1988, serves scrap yards/recycling facilities, (2) QC Conveyors - leading manufacturer with automation/stainless/industrial series, (3) Power Pack Conveyor Company - 90+ years designing/manufacturing conveyor systems. Specific 'Conveyor Technology' entity requires verification.",
        "product_types": "PENDING - Varies from rotary trommels, specialty conveyors, automation series, stainless steel frames, industrial conveyors, timing belt systems",
        "product_complexity": "PENDING - Requires entity identification"
    },
    "Whisper Carts LLC": {
        "industry": "Luxury Electric Golf Carts & Recreational Vehicles Manufacturing",
        "workflow_type": "Design, Manufacturing & Retail - Multi-Brand Operations",
        "company_description": "Founded 2021 by Dave Hatley, Johnson City, TN. Tennessee-based leader in luxury electric golf carts with explosive growth. Recently acquired American Landmaster (UTV manufacturer) and Qwest Pontoons (pontoon boats). Expanded from golf carts into outdoor recreational vehicles.",
        "product_types": "Street-legal electric golf carts: Whisper Halo (floating experience), Whisper W5 XL (high performance), Whisper G4 (golf course & beyond). Also UTVs (via Landmaster acquisition) and pontoon boats (via Qwest acquisition). Premium designs combining cutting-edge performance with refined aesthetics, quiet yet powerful driving.",
        "product_complexity": "High - Premium electric vehicle design/manufacturing, street-legal certification, modern styling and engineering, multi-brand acquisition integration, expanding product lines (carts/UTVs/boats), Tennessee manufacturing focus."
    },
    "National Tool Grinding, Inc.": {
        "industry": "Precision Tool & Centerless Grinding Services",
        "workflow_type": "Job Shop - Specialized Grinding & Machining",
        "company_description": "Established 1951, Erie, PA. Specializes in centerless grinding and tool grinding services. General machining job shop also supplies carbide cutting tools. Fast turnaround times, high-quality service. BBB accredited.",
        "product_types": "Centerless grinding services (.06 to 12 inch diameters, up to 20 feet lengths), tool grinding, exotic materials grinding (inconel, monel, stellite), welding and metal fabrication, carbide cutting tools supply, packaging and handling services. Serves plastics, automotive, aerospace, construction industries. Precise tolerances and finishes.",
        "product_complexity": "High - Exotic materials expertise (inconel, monel, stellite), precision centerless grinding requiring tight tolerances, 70+ years specialized experience, wide diameter/length ranges, diverse industry applications, fast turnaround capabilities."
    },
    "Novamen Inc.": {
        "industry": "Industrial Chemical Distribution & Manufacturing",
        "workflow_type": "Distribution & Custom Solutions - Indigenous-Owned",
        "company_description": "Indigenous-owned and operated, based Red Deer, Alberta. Serves oil, natural gas, mining, forestry, construction, transportation industries throughout Canada. 100 tanks with 5+ million liters bulk storage at 2 locations. Facilities: Red Deer, Blackfalds, Pincher Creek, Fort McKay, Chetwynd, Penhold, Grande Prairie.",
        "product_types": "Dust control products (unpaved roads, construction), deicing agents, cleaners/degreasers (NovaSol HD for oils/greases), industrial process chemicals (Tri-Ethylene Glycol, Propylene Glycol), H₂S scavenging, hydro testing chemicals, wastewater treatment solutions, DEF products (NovaBlue DEF for diesel vehicles), various glycols. Custom formulations for oil/gas/mining/forestry.",
        "product_complexity": "High - Multi-facility bulk chemical storage (5M+ liters), diverse industrial applications, custom chemical formulation, specialized products (H₂S scavenging, DEF), environmental compliance (dust control, wastewater treatment), Indigenous business operations across Western Canada."
    },
    "Division 9 Associates,Inc.": {
        "industry": "Commercial Flooring Distribution - Multi-Line Sales Agency",
        "workflow_type": "Sales Agency - Multi-Manufacturer Representation",
        "company_description": "Co-founded 2010 by Scott Goldman and Larry Hooper (previously with J&J Flooring Group). Single source for quality flooring in Washington DC and Baltimore metropolitan markets. Multi-line sales agency representing several manufacturers.",
        "product_types": "Full range of commercial flooring: carpet, wood, cork, tile, rubber, resilient flooring. Represents multiple manufacturers, simplifying finish specification for architects, designers, and facility managers. Washington and Baltimore metro markets.",
        "product_complexity": "Medium-High - Multi-manufacturer representation requiring product expertise across diverse flooring types, specification support for design professionals, metropolitan market sales agency operations, commercial project coordination."
    },
    "AP Packaging Corp": {
        "industry": "Protective Packaging Manufacturing",
        "workflow_type": "Manufacturing - Eco-Friendly & Temperature-Controlled Solutions",
        "company_description": "Manufacturing facilities in Poughkeepsie, NY and Ohio. Produces high-quality protective packaging. Exclusive manufacturer of BioNatur Bubble (biodegradable, 79.9% biodegradation in 1284 days). Focus on eco-friendly paper-based and biodegradable solutions.",
        "product_types": "Bubble packaging wrap, mailers, envelopes, polyethylene products, eco-friendly paper-based packaging (honeycomb rolls, honeycomb dispensers, honeycomb mailers), temperature-controlled Pacron Temp line (for wine, fish, meats, chocolates, pharmaceuticals), biodegradable BioNatur Bubble, protective mailers, pouches, closed-cell polyethylene foam sheeting. Applications: office mailing, large furniture, electronics, temperature-sensitive foods/pharmaceuticals.",
        "product_complexity": "High - Biodegradable technology development (BioNatur Bubble partnership), temperature-controlled packaging engineering, multi-facility manufacturing, eco-friendly materials innovation, diverse applications (food, pharmaceuticals, electronics, furniture), custom protective solutions."
    },
    "Art Brands Holdings, LLC": {
        "industry": "Heat Transfer Manufacturing & Garment Decoration",
        "workflow_type": "Custom Manufacturing & Stock Products - Made in USA",
        "company_description": "Blacklick, OH (225 Business Center Dr, just outside Columbus). Manufactures world's best heat transfers applied with commercial heat press to apparel and promotional products. Made in USA, ships worldwide. Serves businesses, schools, sports teams, organizations, individuals.",
        "product_types": "Custom heat transfers (customer graphics/artwork), stock designs (2,000+ unique ready-made screen-printed designs ready-to-ship), DTF transfers (Direct-to-Film on various garments/fabrics/textiles/materials), decorated apparel and accessories. Heat applied graphics for apparel, gifts, promotional products.",
        "product_complexity": "Medium-High - Custom heat transfer production, 2,000+ stock design inventory, DTF technology, commercial heat press applications, made in USA manufacturing, worldwide shipping, diverse customer base (businesses/schools/teams/organizations)."
    },
    "Siegel Performance Systems, Inc.": {
        "industry": "Fitness & Rehabilitation Equipment Distribution",
        "workflow_type": "Full-Service Distribution - Facility Planning & Design",
        "company_description": "Established 1993, Huntington, NY. Industry-leading full-service distributor of quality fitness and rehabilitation products. 30+ years as leading distributor for performance & cardio equipment. Now expanding into medical industry. Specialize in facility planning, layout & design for maximum space/equipment utilization.",
        "product_types": "Full range exercise equipment, modalities, treatment/massage tables. Brands: Cybex, Exer-Rest by Nims, Chattanooga, Hausmann, Keiser, NuStep, Marpo Kinetics. CPM's, TENS, NMES, e-stim, hi-lo tables, hydrocolators, ColPac machines. Performance equipment, cardio equipment, physical therapy equipment, rehabilitation products.",
        "product_complexity": "High - Multi-brand distribution requiring product expertise across fitness/rehabilitation/medical equipment, facility planning and design services, 30+ years industry relationships, expanding into medical industry, layout optimization consulting, diverse equipment categories (performance, cardio, therapy, rehabilitation)."
    },
    "The Shed Yard": {
        "industry": "Custom Outdoor Structures Manufacturing & Retail",
        "workflow_type": "Custom Building & Delivery - Family-Owned",
        "company_description": "Local, family-owned, trusted business serving Colorado and New Mexico. Provides Colorado's highest quality custom-built storage sheds, studios, chicken coops, barns, garages. Builds and delivers premium outdoor structures. Free delivery to most of Colorado. Online customizer tool available.",
        "product_types": "Storage sheds (multiple styles, customizable), garden sheds, studio sheds, barn sheds (farm equipment, livestock protection), custom-built garages (vehicles, equipment), loafing sheds (livestock shelter), chicken coops, animal shelters. Built to withstand weather, durable construction. Custom design options.",
        "product_complexity": "Medium - Custom outdoor structure design/manufacturing, regional delivery operations (CO/NM), multiple building types requiring construction expertise, online customizer tool, free delivery logistics, family-owned business operations, weather-resistant engineering."
    }
}

print(f"Batch 71-80 research data prepared for {len(BATCH_71_80)} companies")
for company in BATCH_71_80:
    print(f"  ✓ {company}")
