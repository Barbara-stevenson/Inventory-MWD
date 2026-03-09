#!/usr/bin/env python3
"""
Batch update for companies 191-200 research data - FINAL BATCH.
"""

BATCH_191_200 = {
    "Pure Filtration Products, Inc": {
        "industry": "Air & Liquid Filtration Solutions Manufacturing",
        "workflow_type": "Manufacturing & Distribution - Filtration Specialist",
        "company_description": "Founded 2009, Spokane, WA (4008 E Broadway Ave). Contact: (509) 315-8460. Serves commercial, industrial, residential sectors. State-of-the-art filtration solutions. Pure Care Program, resource library support. Delivery service for timely access to essential filtration products. Website: pfpspokane.com.",
        "product_types": "Air filtration: HEPA filters, pleated filters, custom filters, furnace/HVAC/AC filters, bag filters, final filters, high capacity filters, UV lights. Mini-pleat filters: PURACELL VP (4V)/VPX (2V) extended surface (high efficiency particulate removal, extended service life, extremely low resistance). PURACELL V & VX (high efficiency, low initial pressure drop). MAGNA ASHRAE Series (high degree cleanliness). Liquid filtration: GFHD-Series single-cartridge liquid filter vessels.",
        "product_complexity": "Very High - 15+ years air/liquid filtration expertise, HEPA filter engineering, PURACELL VP/VPX/V/VX mini-pleat technology (extended surface/low resistance/high efficiency), MAGNA ASHRAE high-cleanliness systems, custom filter design, liquid filtration vessels, commercial/industrial/residential applications, Pure Care Program, Spokane WA operations, UV light integration, delivery logistics."
    },
    "BPX Solutions, LLC": {
        "industry": "Packaging Equipment & Supplies Distribution",
        "workflow_type": "Distribution & Consulting - Formerly Excel Packaging",
        "company_description": "Formerly Excel Packaging. 35+ years experience. Ontario, CA. Leading packaging equipment supplier offering industrial equipment solutions. Carries Preferred Pack® brand equipment. Serves bakeries to printing companies to manufacturers. Website: bpxsolutions.com.",
        "product_types": "Packaging equipment: sealing machines, heat shrink tunnels, flow wrappers, pallet wrappers. Packaging materials: shrink films. Preferred Pack® brand equipment. Parts, service. Consulting services for new packaging line installation/product evaluation. Wide variety of packaging equipment systems for all business types.",
        "product_complexity": "High - 35+ years packaging equipment expertise, Preferred Pack® brand operations, sealing machine/heat shrink tunnel/flow wrapper/pallet wrapper distribution, shrink film supply, packaging line consulting, multi-industry applications (bakeries/printing/manufacturing), Ontario CA operations, parts/service support, installation evaluation services."
    },
    "Wipe-on Wipe-off, LLC": {
        "industry": "Automotive Detailing Products Distribution",
        "workflow_type": "Distribution & Retail - Family-Owned New England Distributor",
        "company_description": "WOWO. Family-owned. 35+ years combined experience. Fitchburg, MA storefront (57A Summit St, open to public). Distributes auto detailing products to New England businesses via trucks. Education, training, quality products, dependable service focus. Website: wowotogo.com.",
        "product_types": "Automotive detailing product distribution: Represents Ardex, AutoMagic, Coilhose, Collinite, Dell Corning, Flex, GTechniq, Hi-Tech, IK Sprayers, Jenesco, Lake Country, Little Trees, Meguiar's, Mytee, Nanoskin, P&S, Rupes, S.M. Arnold, Tornador, Veloci & Zenex brands. Abrasives, accessories, aerosols, air fresheners, ceramic coatings, clay bars, cleaners/degreasers, compounds, polishers, fabric cleaners, glass cleaners, leather products. Professional detailing supplies.",
        "product_complexity": "High - 35+ years automotive detailing expertise, 20+ premium brand distribution (Meguiar's/GTechniq/Rupes/P&S/Nanoskin), truck delivery logistics, New England territory operations, retail storefront (Fitchburg MA), family-owned operations, ceramic coating/clay bar/polisher specialization, professional detailing business serving, education/training programs."
    },
    "Vintage Makers, LLC": {
        "industry": "Custom Wine Cellar Design & Manufacturing",
        "workflow_type": "Custom Manufacturing - In-House Wine Cellar Specialist",
        "company_description": "Founded 1994 (first store). Hudson, NH (15 Park Ave). All products built in-house in New Hampshire shop. Custom residential/retail wine cellar design, manufacturing, installation since 1994. Website: vintagemakers.com.",
        "product_types": "Custom wine cellar components (all built in-house): entry doors, cabinets, humidors, wine racking. Custom home bars. Wine cellar construction/installation services. Residential/retail wine cellar solutions.",
        "product_complexity": "Very High - 30+ years wine cellar expertise (since 1994), in-house manufacturing (entry doors/cabinets/humidors/racking), custom wine cellar design/installation, custom home bar construction, residential/retail wine cellar specialization, Hudson NH shop operations, humidor engineering, wine storage solutions."
    },
    "Nellie's Hair Emporium Inc.": {
        "industry": "Hair Extensions & Wigs Manufacturing - Canada",
        "workflow_type": "Manufacturing & Distribution - Premium Hair Products Specialist",
        "company_description": "30+ years manufacturing experience. Canada's #1 beauty supplier. Markham, ON (20-25 Valleywood Dr, L3R 5L9). Contact: (905) 604-6680. Specializes in high quality hair/eyelash extensions, custom/stock wigs, toupees, hair pieces. Constantly innovating new solutions. Infinitude brand (long-lasting real Remy hair). Websites: nellieshair.com, shopnhe.com.",
        "product_types": "Hair extensions (largest selection, premium Infinitude Remy hair): Tape, Invisible Tape, Fusion, I-Tip, Nano-Tip, Secret Weft, Weft, Halo, Ponytail, Clip-In Weft, Bangs. Wigs: custom/stock wigs, toupees, hair pieces. Eyelash extensions. Hair products. Nellie's Hair Emporium Academy training.",
        "product_complexity": "Very High - 30+ years hair manufacturing expertise, Canada's #1 beauty supplier status, premium Infinitude Remy hair technology, 12+ extension method specialization (Tape/Fusion/I-Tip/Nano-Tip/Secret Weft/Halo), custom/stock wig manufacturing, toupee/hair piece engineering, eyelash extension production, Markham ON operations, Nellie's Academy training programs, innovation/development focus."
    },
    "North America Mattress Corp": {
        "industry": "Specialty Foam Mattress Manufacturing - USA Made",
        "workflow_type": "Manufacturing - Healthcare & Specialty Mattress Specialist",
        "company_description": "Nearly 3 decades experience. Clackamas, OR. Each mattress handmade in USA facility. Originally labor/delivery mattress company, expanded to extended healthcare departments. Gold HIRE Vets Medallion Award (US Dept Labor). RoamRest brand (camper van mattresses since 2010). Products used worldwide (hospitals, summer camps, universities, disaster relief). Website: northamericamattress.com.",
        "product_types": "Healthcare: stretchers, operating tables, overlay comfort pads, X-ray/Angio pads, medical mattresses, seat cushions, siderail pads, home health, mental health mattresses. Consumer: home mattresses, truck mattresses, RV/camper van mattresses (RoamRest brand), camp pads, urine-resistant bed-wetting mattresses, pet mattresses. Specialty: disaster relief mattresses, university dorm mattresses.",
        "product_complexity": "Very High - 30 years specialty mattress expertise, USA handmade manufacturing (Clackamas OR), healthcare specialization (stretchers/operating tables/X-ray pads/mental health), labor/delivery mattress heritage, RoamRest camper van brand (since 2010), truck/RV mattress customization, urine-resistant technology, disaster relief mattresses, Gold HIRE Vets Award, worldwide hospital distribution, camp/university applications."
    },
    "Bon Opus Biosciences": {
        "industry": "Life Science Products & Custom Protein Production",
        "workflow_type": "Manufacturing & Services - Custom Biosciences Specialist",
        "company_description": "Founded 2018. Millburn, NJ (150 Essex St). Name from Latin Bonum Opus (good work). Leading supplier life science products/custom services. Trusted supplier for 1,000+ organizations. Dedicated to elevating research through scientific/academic community partnerships. Molecular biology/gene synthesis expertise. Website: bonopusbio.com.",
        "product_types": "Catalog products: Antibodies, LinkLight™ Cell Lines, ELISA Kits & Reagents, Recombinant Proteins. Custom services: custom assay development/screening, custom peptide synthesis, custom antibody production, recombinant protein production, recombinant antibodies. Life science research products.",
        "product_complexity": "Very High - Custom protein production specialization, LinkLight™ Cell Lines proprietary technology, recombinant protein/antibody engineering, custom peptide synthesis, ELISA kit development, custom assay development/screening, molecular biology expertise, gene synthesis capabilities, 1,000+ organization serving, biotechnology/life sciences research focus, Millburn NJ operations, scientific/academic partnership model."
    },
    "Hotsy Equipment Company": {
        "industry": "Industrial Pressure Washer Sales & Service",
        "workflow_type": "Distribution & Service - Callan Industrial (Hotsy Franchise)",
        "company_description": "Hotsy of Houston part of Callan Industrial. North America's #1 cleaning equipment brand. Experienced sales/service staff, industrial cleaning equipment experts. Multiple regional locations (Michigan, Ohio, Kentucky, West Virginia, North Carolina, Texas including Houston/San Antonio/Rio Grande Valley). Website: callhotsy.com (Callan Industrial connection: hotsyhouston.com).",
        "product_types": "Commercial/industrial pressure washers: hot/cold water pressure washers (Hotsy brand), parts, detergents, accessories. Waste oil heaters, HVLS fans, radiant heat lamps. 7-year warranty (high-pressure pump), 5-year warranty (heating coil). Durable high-quality equipment for all-season business operations.",
        "product_complexity": "Very High - Hotsy franchise operations (North America #1 brand), hot/cold water pressure washer technology, 7-year pump warranty/5-year heating coil warranty, waste oil heater integration, HVLS fan systems, radiant heat lamp distribution, multi-state regional coverage (Michigan/Ohio/Kentucky/WV/NC/Texas), Callan Industrial corporate structure, industrial cleaning equipment specialization, seasonal equipment support."
    },
    "Endless Fun, LLC": {
        "industry": "Novelty Drinking Straws Manufacturing",
        "workflow_type": "Manufacturing - Magic Straws Specialist",
        "company_description": "Minneapolis, MN (6401 West 106th St). Bloomington, MN location. Primarily operates in drinking straws business. Makes straws from purchased material. Wholesale novelties. Website: magicstraws.com.",
        "product_types": "Magic drinking straws (novelty straws). Wholesale novelty products. Manufactured from purchased materials.",
        "product_complexity": "Medium - Drinking straw manufacturing, magic straws novelty product specialization, wholesale novelty operations, material purchasing/conversion process, Minneapolis/Bloomington MN operations, retail shop display distribution."
    },
    "Pro AV (Professional Audio Visual Ltd.)": {
        "industry": "Audio Visual Equipment Sales & Service - Canada",
        "workflow_type": "Sales & Service - AV Industry Since 1983",
        "company_description": "Professional Audio Visual Ltd. Regina, Saskatchewan, Canada. In audio-visual industry since 1983. Started primarily as service business offering repair/installation of audio visual equipment. 40+ years AV industry experience.",
        "product_types": "Audio visual equipment: repair, installation, sales. AV equipment service for events/corporate. Audio visual solutions for various applications.",
        "product_complexity": "High - 40+ years AV industry expertise (since 1983), audio visual equipment repair/installation/sales, Regina Saskatchewan operations, service business heritage, corporate/event AV solutions, Canadian AV market specialization, equipment installation expertise."
    }
}

print(f"Batch 191-200 research data prepared for {len(BATCH_191_200)} companies")
for company in BATCH_191_200:
    print(f"  ✓ {company}")
print(f"\n🎉 FINAL BATCH COMPLETE! Progress: 200/200 companies = 100% complete!")
