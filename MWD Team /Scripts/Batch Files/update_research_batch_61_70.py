#!/usr/bin/env python3
"""
Batch update for companies 61-70 research data.
"""

BATCH_61_70 = {
    "City Floral": {
        "industry": "Garden Center & Greenhouse Retail",
        "workflow_type": "Retail Sales & Growing Operations",
        "company_description": "Denver's oldest remaining greenhouse, established 1911. Only full-service year-round garden center within Denver city limits. Founded by Lammermann family for cut flower production. Growing facilities now in Golden, CO (purchased early 90s). 1440 Kearney St, Denver, CO.",
        "product_types": "Annuals, perennials, herbs, vegetables, houseplants, trees and shrubs, florist services, gift shop, gardening equipment. GreenHouse.shop online plant store. Historic cut flowers: carnations, roses, snapdragons, iris, tulips, poinsettias, chrysanthemums.",
        "product_complexity": "Medium-High - Full-service garden center requiring plant care expertise, seasonal inventory management, florist services, online delivery (Denver metro), greenhouse growing operations, tree nursery management, year-round operations."
    },
    "Jeffs atWork Office Furniture": {
        "industry": "Office Furniture Retail & Distribution",
        "workflow_type": "Sales & Service - New & Pre-Owned",
        "company_description": "Family owned and operated since 2000 (atWork network in Brantford since 1989). Largest selection of new and pre-owned office furniture in Brantford, Hamilton, Niagara area. 1125 Colborne Street E, Brantford, ON. Works with Canadian furniture suppliers, many in Ontario.",
        "product_types": "Ergonomic chairs and desks, new and pre-owned office furniture, workspace solutions. Prompt delivery and assembly services. Canadian furniture brands, Ontario suppliers.",
        "product_complexity": "Medium - Large inventory management (new/pre-owned), ergonomic furniture expertise, delivery/assembly logistics, knowledge of Canadian furniture manufacturers, workspace design consultation."
    },
    "Working Fire Furniture & Mattress Co, Inc.": {
        "industry": "Fire Station Furniture & Mattresses Manufacturing",
        "workflow_type": "Specialized Manufacturing - Firefighter-Owned",
        "company_description": "Firefighter-owned and operated company supplying fire stations and emergency service facilities nationwide. Does not ship to residential addresses. Built Firehouse Tough® - engineered for 24/7 firehouse life. All products tested for emergency service environments.",
        "product_types": "Fire station recliners (Ultimate Firefighter Recliner™), heavy-duty mattresses (made in USA, 10-year warranty), fire station furniture, beds. Designed specifically for firefighters and emergency services. Free shipping on mattresses/protectors.",
        "product_complexity": "High - Specialized products for 24/7 emergency service use, firefighter-owned design expertise, heavy-duty engineering and testing, nationwide B2B distribution (no residential), industry-specific requirements, warranty programs."
    },
    "Hollingbery and Son, Inc.": {
        "industry": "Hop Supply & Processing",
        "workflow_type": "Brokerage, Processing & Farming",
        "company_description": "Yakima, WA hop supplier. Hops in family since 1942. Brokered hundreds of millions of pounds worldwide. Modern technology for storage, T90 pellet production, laboratory analysis. 400-acre farm in Wapato, WA (300 acres tree fruit, 100 acres row crops).",
        "product_types": "90+ hop varieties, T90 hop pellets (in-house production), whole leaf hops, organic hops, HopKick® (100% hop-derived aqueous extract for seltzers/teas/hop water/NA beers/kombuchas). Tree fruit (apples, pears, peaches, nectarines), alfalfa, wheat, dry beans.",
        "product_complexity": "Very High - Specialized hop processing requiring advanced technology, 90+ variety expertise, international brokerage operations, in-house T90 pellet production, laboratory analysis capabilities, proprietary HopKick® product, diversified farming operations."
    },
    "Keast Enterprises Inc": {
        "industry": "Agricultural, Construction & Forestry Equipment Distribution",
        "workflow_type": "Sales, Parts & Service - Multi-Brand Dealer",
        "company_description": "Henderson, IA. Iowa's source for ag/construction/forestry equipment and attachments. Serves all 50 states regularly. 80+ shortline brands. Thousands of parts on hand. Experienced technicians. Worldwide delivery.",
        "product_types": "Grain vacuums, manure spreaders, augers, conveyors, fuel trailers, forestry mulchers, forage trailers, mills, compact tractors, bale processors, sprayers, bale trailers, ejection scrapers, windrower shredders, seed tenders, grain carts, smoothwall bins, rakes, feed wagons, drills, seeders, Outback guidance systems, hundreds of attachments. Brands: Art's Way, Batco, BEFCO, Cloverdale, Farm King, Haybuster, IronCraft, J&M, Kelly Ryan, Loftness, Maschio Gaspardo, REM, Renn, Rowse Rakes, Thunder Creek, Travis Seed Cart, Universal Implements, Walinga.",
        "product_complexity": "Very High - 80+ brand dealer requiring extensive product knowledge, nationwide distribution logistics, comprehensive parts inventory (thousands on hand), experienced technician team, diverse equipment categories (ag/construction/forestry), worldwide delivery capabilities."
    },
    "Tippmann Arms Company LLC": {
        "industry": "Firearms Manufacturing",
        "workflow_type": "Design & Manufacturing - In-House Machining",
        "company_description": "New Haven/Fort Wayne, IN. Founded by Dennis Tippmann Jr. (formerly Tippmann Paintball - sold 2014). 86,000 sq ft state-of-the-art facility. All critical components machined in-house (upper/lower receivers, barrels, bolts/BCG). 4-axis CNC machines, gun drilling, rifling equipment.",
        "product_types": "M4-22 rifles (.22LR semi-automatic), M4-22 pistols, AR platform variations, magazines, accessories. Focus on .22LR caliber firearms based on popular AR platform.",
        "product_complexity": "Very High - Firearms manufacturing requiring precision machining, in-house production of critical components, state-of-the-art CNC/gun drilling/rifling equipment, 20 patents from paintball background, quality control, dealer network management, regulatory compliance."
    },
    "RedEagle International LLC": {
        "industry": "Generic Agrichemicals Manufacturing & Distribution",
        "workflow_type": "Direct-to-Farmer Distribution",
        "company_description": "Founded 2008 by Yingxue Yu. Lakeland, FL (5143 S Lakeland Dr Ste 4). Mission: provide farmers better value and more choice in agrichemical costs. Avoids high overhead, bundling incentives, rebates for transparent value. Pesticide, fertilizer, agricultural chemical manufacturing.",
        "product_types": "Generic agrichemicals: herbicides (Bentazon 4, Dicamba 49.8% SL, Glyphosate 54, Paraquat 43.2% SL, Clethodim 2E, Flumioxazin, Glufosinate, Metribuzin 75% DF, Chlorimuron-ethyl 25% WDG), fungicides (Azoxystrobin 22.9% SC, Captan 80WDG). Same proven active ingredients, high quality.",
        "product_complexity": "High - Generic agrichemical formulation and distribution, regulatory compliance (EPA registration), quality control matching brand-name products, direct farmer relationships, transparent pricing model, multiple active ingredient formulations."
    },
    "LPI SHOW NETWORK LLC": {
        "industry": "PENDING - Company Not Clearly Identified",
        "workflow_type": "PENDING - Possible Event Production",
        "company_description": "PENDING RESEARCH - No specific information found for 'LPI SHOW NETWORK LLC' as event production company. Multiple LPI companies exist (LPi Network web services, LPI Productions media, Lawrence Productions video). May operate under different name or limited online presence.",
        "product_types": "PENDING RESEARCH",
        "product_complexity": "PENDING RESEARCH"
    },
    "VPNZ Ltd": {
        "industry": "Industrial Vacuum Pumps, Compressors & Blowers",
        "workflow_type": "Sales, Service, Rental & Parts",
        "company_description": "Vacuum Pumps NZ Ltd, established 1998. Leading supplier to New Zealand and Pacific Islands for 20+ years. Family-owned (Directors Valerie & David Walls bought 2007). Exclusive NZ agent/distributor: Ingersoll Rand, Becker, Olympias, Masport. Repair/servicing cornerstone.",
        "product_types": "Vacuum pumps (Piston, Screw, Scroll, Carbon Vane, Oil Sealed, truck pumps, Roots, Claw, Rotary Vane, Linear Diaphragm, Side Channel), compressors (oil-free, various types), low-pressure blowers, air treatment (dryers, filtration), hire/loan equipment. Repair/service all brands.",
        "product_complexity": "High - Wide range of pump/compressor/blower technologies, multi-brand service expertise, exclusive agency relationships, hire/loan fleet management, professional service engineers, serves diverse industries (food, manufacturing, wastewater, pharmaceutical, printing, wood, automotive, construction)."
    },
    "SunShine USA, LLC 2023": {
        "industry": "Hot Tub & Swim Spa Manufacturing/Retail",
        "workflow_type": "Manufacturing & Retail - Multi-Brand Operations",
        "company_description": "LPI Inc (Leisure Products International) - largest hot tub/swim spa retailer in US with 70+ company-owned stores. Employee owned. Made in USA. 450,000+ sq ft manufacturing space. Sister companies: MD Carts, Beast Carts, Sunco Tanning. Online: aqualivingstores.com.",
        "product_types": "Hot tub brands: Catalina Luxury Spas, Dr. Wellness Therapy Spas, Tuff Spas, Plug and Power Spas, Hudson Bay Spas. Swim spas. Luxury golf carts, golf cart accessories, tanning beds (sister companies). Cutting-edge technology for therapeutic/leisure experiences.",
        "product_complexity": "Very High - Multi-brand hot tub/swim spa manufacturing, 70+ retail locations nationwide, 450,000 sq ft production facilities, e-commerce operations, sister company product lines (golf carts, tanning beds), employee-owned structure, therapeutic technology integration."
    }
}

print(f"Batch 61-70 research data prepared for {len(BATCH_61_70)} companies")
for company in BATCH_61_70:
    print(f"  ✓ {company}")
