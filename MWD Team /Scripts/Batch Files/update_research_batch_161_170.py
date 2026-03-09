#!/usr/bin/env python3
"""
Batch update for companies 161-170 research data.
"""

BATCH_161_170 = {
    "Sharp Performance USA Inc.": {
        "industry": "Automotive Promotional Products & Dealer Accessories",
        "workflow_type": "Manufacturing - Custom Branded Solutions",
        "company_description": "Established 2009 (acquired Concord Industries automotive division assets). Irwindale, CA (16029 Arrow Highway, Suite D) and Norwalk, CT locations. Expanded to LA 2012, relocated headquarters. Serves thousands automobile dealers, organizations, corporations worldwide.",
        "product_types": "Dealer copy key tags, license plate frames, auto-related promotional products. Corporate gifts, logoed products for automobile dealers/organizations. High-quality branded merchandise. Custom auto accessories specialization.",
        "product_complexity": "Medium-High - Dealer promotional products manufacturing, license plate frame customization, key tag production, corporate gift branding, logoed product design, automobile dealer market specialization, dual-location operations (CA/CT), Concord Industries asset acquisition integration, worldwide distribution."
    },
    "PTE Golf, LLC": {
        "industry": "Golf Tournament Enhancement Products",
        "workflow_type": "Manufacturing & E-Commerce - Professional Golf Market",
        "company_description": "Founded 2004, industry leader in 'Helping Professionals Look More Professional'. Custom tournament enhancement items for Golf Professionals. Products used across globe. Originally designed high-quality tournament products.",
        "product_types": "Tournament enhancement products: embroidered table covers, tournament cases, pop-up tents, professional presentation items for driving range/on course. Custom products for golf clubs. Retail shop items, awards. Not traditional golf equipment (clubs/balls) but tournament/professional presentation items.",
        "product_complexity": "Medium-High - 20+ years golf professional market expertise, custom tournament enhancement design, embroidered table cover manufacturing, pop-up tent production, driving range/on-course presentation specialization, global distribution, retail/awards product portfolio, Golf Professional client focus."
    },
    "Angels' Share South": {
        "industry": "Boutique Wine Importing & Distribution - Florida Division",
        "workflow_type": "Import & Distribution - Southern Regional Operations",
        "company_description": "Orlando, FL (1700 35th Street, Unit #109). Founded 2004 as Angels' Share Wine Imports, operating southern division since then. Office: 407-601-4951, orders@aswsouth.com. Gerome Tate: 407-230-3297. Florida licensed beverage distributor. Imports from Italy (Caviro Soc. Coop. Agricola), Greece (partnership with Cava Spiliadis). Serves Florida market. Northern division in Brooklyn, NY serves NY/NJ/CT.",
        "product_types": "Exceptional American wineries, curated selection European domaines. Italian wine imports (Caviro), Greek wines (Cava Spiliadis partnership). Distributor for Robert Foley Vineyards, Monticello Napa, Banknote Wine Company. Premium boutique wines.",
        "product_complexity": "High - Florida beverage distributor licensing, Italian/Greek wine import operations, dual regional divisions (North: NY/NJ/CT, South: FL), European domaine curation, American winery portfolio, Caviro Soc. Coop. Agricola partnership, Cava Spiliadis Greece collaboration, multi-winery distribution (Robert Foley/Monticello/Banknote), 20+ years wine importing expertise."
    },
    "California Pacific International, LLC": {
        "industry": "Food Distribution - Rice & Dry Goods Specialist",
        "workflow_type": "Distribution - Freeze, Chill & Dry Services",
        "company_description": "Founded 1950, Burlingame, California. Bay Area headquarters. 70+ years serving Pacific region. State-of-the-art facilities, carefully selected distribution partners. 'Committed to Quality!' Website: calpacsf.com.",
        "product_types": "Large variety dry products (rice main focus - primary specialization), bottled water, saw blades, meats, dairy. Customized freeze, chill, dry services. Diverse product range from food to industrial supplies.",
        "product_complexity": "High - 70+ years Pacific region distribution, rice specialization expertise, state-of-the-art freeze/chill/dry facilities, Bay Area distribution hub, multi-category portfolio (dry goods/meats/dairy/water/industrial), customized temperature-controlled services, carefully selected distribution partner network, Burlingame CA operations."
    },
    "Staples Enterprises Inc.": {
        "industry": "Petroleum Distribution & Retail Convenience Stores",
        "workflow_type": "Wholesale & Retail - Family-Owned Energy Business",
        "company_description": "Family-owned, Windom, MN headquarters (1680 Redding Ave N). 40+ years petroleum industry experience. Sister company to Staples Oil Co., Inc. Operates retail convenience stores, full-line grocery store, Dairy Queen restaurant in Southern Minnesota and Eastern South Dakota communities. Website: staplesoil.com.",
        "product_types": "Wholesale: refined fuels, oils, lubricants to convenience store owners, co-ops, independent bulk fuel dealers, commercial businesses (sole proprietorship to Fortune 500), local/county/state municipalities. Fleet transports: gasoline, diesel, E-85, kerosene, motor oils, renewable fuels (ethanol, bio, biodiesel, feedstocks). Retail: convenience stores, grocery, Dairy Queen. Bulk fuel locations: Windom, Sanborn, Mankato/Pemberton, Shakopee, Fulda (MN), Boone (IA).",
        "product_complexity": "Very High - 40+ years petroleum distribution, wholesale fuel/oil/lubricant supply, Fortune 500 commercial clients, renewable fuels expertise (ethanol/bio/biodiesel), multi-location bulk fuel operations (6 locations MN/IA), retail convenience stores/grocery/Dairy Queen operations, fleet transportation logistics, municipal/co-op/dealer serving, E-85/kerosene specialization, family-owned dual operations (Staples Oil/Staples Enterprises)."
    },
    "MPD Medical Systems, Inc.": {
        "industry": "Medical Carts & Hospital Cabinets Manufacturing",
        "workflow_type": "Manufacturing - USA Made Medical Equipment",
        "company_description": "Central Illinois manufacturing facilities. 30+ years delivering innovative medical carts, workstations, cabinets for fast-paced healthcare demands. Hospital & health care company. Proudly made in USA, 100% latex-free.",
        "product_types": "Premium quality medical carts/accessories: Anesthesia, Emergency, Treatment, Isolation, Medication, general use carts. Maximum security storage/narcotic cabinets. Steel and E-Z Push aluminum construction. Quiet ball bearing slides, full drawer extensions. Workstations for healthcare.",
        "product_complexity": "Very High - 30+ years medical cart innovation, Anesthesia/Emergency/Treatment/Isolation/Medication specialization, maximum security narcotic cabinet engineering, USA manufacturing (central Illinois), 100% latex-free construction, E-Z Push aluminum technology, quiet ball bearing slide systems, full drawer extension mechanisms, healthcare fast-paced environment design, premium quality standards."
    },
    "Office Furniture Centre Ltd": {
        "industry": "Office Furniture Distribution - PENDING RESEARCH",
        "workflow_type": "PENDING - Likely Canadian Distribution",
        "company_description": "PENDING RESEARCH - No specific company information found. Likely Canadian office furniture distributor based on 'Ltd' designation and context. Requires additional verification for accurate details.",
        "product_types": "PENDING RESEARCH - Likely office furniture, desks, chairs, workstations. Requires verification.",
        "product_complexity": "PENDING - Requires additional research to determine specific capabilities and market position."
    },
    "Good Chemistry of Massachusetts, Inc": {
        "industry": "Vertically Integrated Cannabis Cultivation & Dispensary",
        "workflow_type": "Cultivation & Retail - Premium Small Batch Cannabis",
        "company_description": "Founded 2013. Vertically integrated cannabis company (Colorado and Massachusetts). Massachusetts locations: Lynn (696 Western Ave) and Worcester (9 Harrison St). Grows 100% of cannabis flower. 60+ different strains. Sells to dozens of dispensaries across Massachusetts (Cape Cod to NY border). Licensed cultivator and retailer.",
        "product_types": "Cannabis flower (60+ strains, 100% in-house cultivation, GC Uniques proprietary/small batch strains), solventless concentrates (rosin, bubble hash, dry sift, live rosin, water hash), vape products (disposable vaporizers, vape cartridges, premium live resin options). Vertically integrated production (cultivation to retail).",
        "product_complexity": "Very High - Vertically integrated cannabis operations (cultivation/manufacturing/retail), 60+ strain breeding/cultivation, proprietary GC Uniques strain development, solventless concentrate manufacturing (rosin/bubble hash/dry sift technology), live resin vape production, Massachusetts/Colorado dual-state operations, dispensary network serving (Cape Cod to NY border), 10+ years cannabis expertise, premium small batch focus."
    },
    "American Wholesale Distributors": {
        "industry": "Apparel & Custom Logo Branding Wholesale - awdinc.net",
        "workflow_type": "Wholesale Distribution - Men's & Boys' Clothing",
        "company_description": "Canoga Park, California (21224 Vanowen St). SIC code 5136 (Men's and Boys' Clothing and Furnishings). Specializes in quality apparel, Lucky Gambler Clothing brand, custom logo branding/design. Website: awdinc.net. Note: Different from Alabama-based grocery distributor with similar name.",
        "product_types": "Quality apparel products, Lucky Gambler Clothing, custom logo branding and design services. Wholesale for promotional use, retail sales, custom projects. Men's and boys' clothing and furnishings specialization.",
        "product_complexity": "Medium - Wholesale apparel distribution, Lucky Gambler Clothing brand, custom logo branding/design services, men's/boys' clothing specialization, promotional/retail/custom project serving, California operations, SIC 5136 classification."
    },
    "JOUFFRE INC": {
        "industry": "Luxury Upholstery & Interior Decoration - French Craftsmanship",
        "workflow_type": "Atelier Manufacturing - Living Heritage Company",
        "company_description": "Founded 1987, Lyon (French silk capital). Living Heritage Company (EPV) label by French government (awarded 2006, renewed 2012/2018). Workshops: Lyon and New York. Showrooms: Paris and Manhattan. Serves designers worldwide, hotel proprietors, public agencies, individuals. Renowned worldwide high-class upholstery (traditional and contemporary).",
        "product_types": "High-end upholstery: curtains, cushions, bedspreads, reproduction armchairs, contemporary sofas. Gainage technique (covering furniture/moldings - wardrobes, beds, chairs, cornices, casings, picture rails, clear paneling). Materials: linen, alcantara, silk velvet, leather. French luxury craftsmanship.",
        "product_complexity": "Very High - 35+ years French luxury upholstery expertise, Living Heritage Company (EPV) label (French government), patented Gainage technique for furniture covering, silk velvet/alcantara/linen/leather specialization, Lyon textile tradition heritage, dual workshop operations (Lyon/New York), Paris/Manhattan showrooms, worldwide designer/hotel/public agency serving, traditional/contemporary upholstery mastery, furniture reproduction artisan craftsmanship."
    }
}

print(f"Batch 161-170 research data prepared for {len(BATCH_161_170)} companies")
for company in BATCH_161_170:
    print(f"  ✓ {company}")
print(f"\n📊 Progress: 170/200 companies = 85% complete!")
