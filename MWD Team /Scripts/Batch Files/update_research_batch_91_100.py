#!/usr/bin/env python3
"""
Batch update for companies 91-100 research data.
This batch brings us to the halfway point (100/200 = 50%)!
"""

BATCH_91_100 = {
    "Hylunia Skin Care": {
        "industry": "Vegan & Natural Skincare Manufacturing",
        "workflow_type": "Manufacturing & E-Commerce - Plant-Based Wellness",
        "company_description": "Founded 1988 by Dr. Lingam and Dr. Brian Jegasothy, Henderson, NV. Developed for founder's daughter's sensitive skin, collaborated with dermatologists/anti-aging physicians. Certified vegan, cruelty-free, natural, plant-based, non-toxic, clean, anti-inflammatory. 11-50 employees. Combines ancient Ayurvedic principles with modern science.",
        "product_types": "Full skincare line: 100% vegan hyaluronic acid products, safe non-toxic/non-carcinogenic ingredients only. Minimizes fine lines, wrinkles, age spots, breakouts. Brings tone, smoothness, clarity. Effective all skin types. Available hylunia.com and Amazon. Anti-inflammatory formulations protecting from aging effects while repairing skin damage.",
        "product_complexity": "Medium-High - Ayurvedic/modern science integration, vegan hyaluronic acid formulation, dermatologist collaboration, anti-inflammatory technology, hypoallergenic sensitive skin expertise, non-toxic ingredient sourcing, multi-channel distribution (direct/Amazon)."
    },
    "Lore Technology": {
        "industry": "Industrial Imaging Solutions & Vision Systems",
        "workflow_type": "Design & Distribution - Veteran-Owned",
        "company_description": "Founded 2020, Indianapolis, IN (55 Monument Circle, Suite 700). Service-disabled veteran-owned small business. 35+ years vision/electronics industry experience. Team experience: healthcare, manufacturing, physical security, nuclear power, cybersecurity. Subsidiary Wilco Imaging customizing since 2003. Contact: (317) 678-9309.",
        "product_types": "Industrial-grade cameras, lenses, complete vision system solutions, CCTV/security solutions, custom camera services, accessories. Applications: machine vision, autonomous vision, robotic/industrial vision, medical/microscopy, security CCTV, broadcast, military/government. Exceptional imaging technology, customized components. High-quality imaging solutions tailored to client needs.",
        "product_complexity": "High - 35+ years vision/electronics expertise, service-disabled veteran-owned operations, custom imaging component design, multi-industry applications (healthcare/manufacturing/security/nuclear/military), complete vision system integration, subsidiary Wilco Imaging since 2003, specialized government/military solutions."
    },
    "Tritter Feefer Home Collection": {
        "industry": "Custom Home Furnishings Manufacturing - Wholesale",
        "workflow_type": "Custom Manufacturing - Family-Owned, Made in USA",
        "company_description": "Founded 2007 by husband-wife Bill Aultman and ML Littlefield (moved Colorado to Georgia for grandchildren Tristan/Faith - Tritter/Feefer nicknames). 6 relocations before permanent LaGrange, GA home 2015. Family-owned, rich background in retail home furnishings/interior design. Wholesale only, showrooms: Atlanta, New York, High Point, Dallas.",
        "product_types": "Fully customizable fine furniture (custom crafted, hand finished). Unique finishes, environmentally conscious manufacturing, customizable sizes for most products. Low/no VOC water-based finishes hand-applied by skilled artisans. Curated selection transforms living spaces into comfort/elegance havens. US manufacturer.",
        "product_complexity": "High - Custom furniture manufacturing requiring skilled artisan finishes, low/no VOC water-based finish expertise, environmentally conscious production, customizable sizing for most products, wholesale-only distribution model, multi-showroom operations (Atlanta/NY/High Point/Dallas), family-owned US manufacturing."
    },
    "Access2mobility": {
        "industry": "Mobility Equipment & Accessibility Solutions",
        "workflow_type": "Sales & Service - Complete Mobility Solutions",
        "company_description": "Provides complete mobility solutions for individuals with physical limitations. Offers both product sales and service options including repair/maintenance. Full-service mobility equipment provider for home and vehicle accessibility.",
        "product_types": "Home equipment: Harmar/Bruno stair lifts (straight staircases), residential platform lifts, vertical platform lifts (Highlander II for scooters/wheelchairs/powerchairs), overhead/ceiling patient lifts (bed/bath transfers). Vehicle equipment: Bruno/Harmar wheelchair/scooter lifts (cars/trucks/SUVs), MPS hand controls (40+ years), BraunAbility lowered floor minivans, GoShichi pickup truck conversions, transfer seats. Personal mobility: scooters, powerchairs, lift chairs, rolling walkers/rollators (Upwalker/Nova Products), wheelchairs.",
        "product_complexity": "High - Multi-category mobility solutions (home/vehicle/personal), multi-brand distribution (Bruno/Harmar/BraunAbility/MPS/Upwalker/Nova), vehicle modification expertise (lowered floors, lift installations, hand controls), patient lift installation, repair/maintenance services, regulatory compliance (ADA/safety standards)."
    },
    "Binders, Inc.": {
        "industry": "Custom Office Supply Manufacturing - Binders & Related Products",
        "workflow_type": "Full-Service Manufacturing - Made in USA",
        "company_description": "Founded November 1981, Charlotte, NC. 35+ years manufacturing custom three ring binders and associated products. All manufacturing facilities/business offices in USA. Wholly owned subsidiary of Jones Holding Corporation (JHC) - privately funded holding company for small cap manufacturing/distribution acquisitions. Serves healthcare, legal, education, religious institutions, general business.",
        "product_types": "Custom binders: vinyl binders, poly binders, clear view binders, three ring binders, pad holders. Related products: index tabs, certificate/degree holders, restaurant menus, document holders, easels, custom office products, custom presentation folders, custom padfolios, custom diploma covers, packaging options, print/copy services. Marketing/advertising/promotional products.",
        "product_complexity": "Medium-High - 35+ years custom manufacturing expertise, full-service operations (design/manufacturing/printing), Made in USA production, diverse product line evolution (binders to complementary office products), multi-industry serving (healthcare/legal/education/religious/business), subsidiary of JHC holding corporation."
    },
    "MYOS CORP": {
        "industry": "Advanced Nutrition - Muscle Health Products",
        "workflow_type": "Research, Development & Commercialization",
        "company_description": "Research-based advanced nutrition company with Human Nutrition and Animal Health divisions. Built on world class science/research. Portfolio: 8 successful clinical studies, 7 patents. Formerly Myos Rens Technology Inc. Focused on discovery, development, commercialization of nutritional ingredients, functional foods, technologies for muscle tissue health/performance.",
        "product_types": "Fortetropin® (proprietary ingredient from fertilized chicken egg yolks, retains biological integrity/bioactivity, clinically shown to enhance muscle size/lean body mass/strength in resistance training). MYOS PET (pets' muscle health), MYOS VET (veterinarian collaboration, specialized pet muscle solutions), MYOS MD (HCP-exclusive nutraceutical for muscle loss from aging/disuse/surgery/GLP-1 medications). Yolked®, Physician Muscle Health Formula®, MYOS Canine Muscle Formula®, Qurr®.",
        "product_complexity": "Very High - Proprietary Fortetropin® technology from fertilized egg yolks, 8 clinical studies validation, 7 patents portfolio, human/animal divisions, HCP-exclusive products, GLP-1 medication muscle loss addressing, research-based development requiring bioactivity preservation, regulatory compliance (nutraceuticals/pet products)."
    },
    "Animal Hospital Supply Inc.": {
        "industry": "Veterinary Surgical & Critical Care Supplies Manufacturing",
        "workflow_type": "Manufacturing - Pet-Specific Medical Products",
        "company_description": "Established 2012, Flowery Branch, GA (4142 Industry Way). Developed procedure-specific surgical drapes with world's leading veterinary surgeons. Manufacturer partner with MWI Animal Health (major veterinary distributor). Focus: pet-specific designs vs. adapting human medical products. Addresses modern technology need in veterinary medicine.",
        "product_types": "Sterile surgical gowns/drapes, surgical procedure packs tailored for pet patients, procedure-specific surgical drape lines (developed with leading veterinary surgeons), sterile procedure packs (single drapes to full custom packs), warm air equipment (blowers/blankets preventing pet hypothermia during procedures), surgical gowns/accessories. Enhance surgical outcomes, reduce infection rates.",
        "product_complexity": "High - Pet-specific surgical product design requiring veterinary surgeon collaboration, sterile manufacturing processes, custom procedure pack assembly, warm air equipment integration, infection control technology, hypothermia prevention expertise, MWI Animal Health distribution partnership."
    },
    "Supply Shield Inc": {
        "industry": "Electronic Components Distribution - Aerospace/Defense",
        "workflow_type": "Procurement, Stocking & Distribution",
        "company_description": "Saint Petersburg, FL (3224 Bennett St N, 33713). Premier distributor of electronics, hardware, IT equipment. AS 9120 & ISO 9001:2015 certified. Customers: Aerospace/Defense Industries, Original Equipment Manufacturers, Contract Manufacturers. Semiconductors/electronic components sector. 1-10 employees, revenue under $1M.",
        "product_types": "Electronic components for manufacturers, engineers, electronics industry businesses. Factory authorized parts at competitive pricing. Obsolete and hard to find components assistance. Procurement, stocking, distribution services. Aerospace/defense grade electronics, hardware, IT equipment.",
        "product_complexity": "High - AS 9120 & ISO 9001:2015 certifications, aerospace/defense industry compliance, obsolete/hard-to-find component sourcing, factory authorized parts procurement, OEM/contract manufacturer relationships, semiconductor distribution expertise, specialized aerospace/defense requirements."
    },
    "Delmarva Design Center": {
        "industry": "Kitchen & Bath Design Center - Residential Remodeling",
        "workflow_type": "Design & Sales - One-Stop Shop",
        "company_description": "Selbyville, DE 19975 (Delmarva Peninsula, Elizabethan Square-Eden House). 9,600 sq ft showroom with 24 kitchen displays. Kitchen/bath company offering cabinets, countertops, appliances, flooring, tile all in one location. 3D rendering design capability for discovering ideas/creating home designs.",
        "product_types": "Kitchen cabinetry brands: Showplace, Koch and Company, Aristokraft, Bertch. Appliances: Wolf, Sub-Zero, Cove, GE Cafe series. Countertops: various materials/designs for kitchens/bathrooms. Flooring: Luxury Vinyl, Laminate, Engineered Wood, Hardwood, Tile, Carpet. Tile: ceramic, porcelain, glass, cement, natural stone. Wide variety sizes/shapes/materials. Design services with 3D rendering.",
        "product_complexity": "Medium-High - Multi-category product expertise (cabinetry/appliances/countertops/flooring/tile), premium brand distribution (Wolf/Sub-Zero/Cove/Showplace/Koch), 9,600 sq ft showroom operations with 24 kitchen displays, 3D rendering design capabilities, one-stop-shop coordination for complete kitchen/bath remodels."
    },
    "Audio Video Supply": {
        "industry": "MULTIPLE COMPANIES - Requires Clarification",
        "workflow_type": "PENDING - Likely Audio Visual Equipment Distribution",
        "company_description": "MULTIPLE ENTITIES FOUND: (1) Audio Video Supply (avsupply.com) - wholesale distributor providing single source solution to OEMs/system resellers for video components/cameras/lenses, (2) Audio Supply - distributor of commercial/professional A/V products since 1988 (Shure, Atlas, Crown, JBL, Soundtube, TOA), (3) Marshall Industries - leading AV system installation for schools/businesses. Specific 'Audio Video Supply' entity requires verification.",
        "product_types": "PENDING - Varies from video components/cameras/lenses, commercial A/V products (switchers/amplifiers/splitters/extenders/converters/scalers/cables/digital signage), to complete AV system installations",
        "product_complexity": "PENDING - Requires entity identification"
    }
}

print(f"Batch 91-100 research data prepared for {len(BATCH_91_100)} companies")
for company in BATCH_91_100:
    print(f"  ✓ {company}")
print(f"\n🎉 MILESTONE: Halfway point reached! 100/200 companies = 50% complete!")
