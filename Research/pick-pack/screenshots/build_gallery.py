#!/usr/bin/env python3
"""
Build a comprehensive HTML screenshot gallery for pick/pack competitor research.
Converts Fishbowl local PNGs to base64 data URIs and includes external CDN images.
"""

import base64
import os
import json
from pathlib import Path

def image_to_base64_uri(filepath):
    """Convert an image file to a base64 data URI."""
    with open(filepath, 'rb') as img_file:
        img_data = base64.b64encode(img_file.read()).decode('utf-8')
        return f"data:image/png;base64,{img_data}"

def create_html_gallery():
    """Create the complete HTML screenshot gallery."""

    # Base directory
    base_dir = "/sessions/vigilant-practical-hamilton/mnt/Inventory Management/Inventory-MWD-/Research/pick-pack/screenshots"

    # Fishbowl screenshots (local, will be converted to base64)
    fishbowl_screens = [
        {
            "file": "fishbowl-01-pick-search-pane.png",
            "step": "Step 1: Pick Search Queue",
            "desc": "Color-coded pick queue. Green = ready, yellow = partial, red = short. Columns: Pick #, Status (Entered/Finished/Committed), Priority. Double-click a pick to view details."
        },
        {
            "file": "fishbowl-02-pick-details.png",
            "step": "Step 2: Pick Details",
            "desc": "Pick item table with tabs (General, Details, Memo, Custom). Header: Priority, Scheduled date, Status, Location Group. Item table: Status icon, Number, Description, Qty, UOM, Location. Action buttons: Combine, Hold, Start, Commit, Find, Finish."
        },
        {
            "file": "fishbowl-03-pick-location.png",
            "step": "Step 3: Serial Number Selection",
            "desc": "Dialog for selecting serial numbers during pick. Shows serial numbers for item (e.g., FG2100 - Extreme Mountain Bike). Buttons: Select, Select Needed, Select All."
        },
        {
            "file": "fishbowl-04-pick-hold.png",
            "step": "Step 4: Ungroup Picks",
            "desc": "Ungroup picks dialog. Options: by Order, Date Scheduled, Location Group, Location Type, Pick Item Status, Order Item."
        },
        {
            "file": "fishbowl-05-group-picks.png",
            "step": "Step 5: Picking Permissions",
            "desc": "User permissions for Picking module. Settings: Allow Over Picking For Sales Orders, Allow Over Picking For Work Orders, Can Always Change Memos, Commit."
        },
        {
            "file": "fishbowl-06-pick-tracking.png",
            "step": "Step 6: Advanced Search",
            "desc": "Advanced search for picks. Fields: Number, Status, Type, Priority, Location Group, Date Scheduled, Username, Carrier, Carrier Service. Filter options: Show All, Show Has Fulfillable, Show Completely Fulfillable. Order filters: Part Number, Part Description, Order Number, Order Type."
        }
    ]

    # Katana MRP (external CDN)
    katana_screens = [
        {
            "step": "Step 1: Initiate Pick from SO",
            "desc": "Pack some / Pack all status dropdown on sales order card",
            "url": "https://downloads.intercomcdn.com/i/o/ep5ydul3/1609013048/7d5fc45efed8533d8940e26e97a3/image.png?expires=1773936000&signature=613071d7695032eb82d3af4af7e4e6374abaa7a75f586cf899558af55ff3f6e0&req=dSYnH8l%2FnoFbUfMW1HO4zSpSiQFIliMCxXS%2BKL6lwJ52CVegY6bVMY5WVbW3%0ANCdWl%2BI7IJ7C6RmuV7g%3D%0A"
        },
        {
            "step": "Step 2: View Pick Queue",
            "desc": "Sales Orders list with 'Ready for packing' pipeline status",
            "url": "https://downloads.intercomcdn.com/i/o/ep5ydul3/1609013743/db9765ff06d4b5da953427dc090a/image.png?expires=1773936000&signature=0c8eeae130b99c40266d348e1b70d2176c0bab1dea81ba7ff0a7f2337b1593a2&req=dSYnH8l%2FnoZbWvMW1HO4zfSzM9DWHLath13%2F%2Fe5TZYKaoCF%2FUt67oPTYjbPR%0A%2B61t0sJ71xwYg0fOYMs%3D%0A"
        },
        {
            "step": "Step 3: Assign Batches (Pre-assign)",
            "desc": "Batch assignment popup - pre-assign batches to items",
            "url": "https://downloads.intercomcdn.com/i/o/ep5ydul3/1609015046/da597ff6d0a5de0dcc6cf75446da/image.png?expires=1773936000&signature=40cd25345f5066830f7e28d4f912fb3293d79369be692bd438c493e9634c0059&req=dSYnH8l%2FmIFbX%2FMW1HO4zVl04AihmoJ77t2rxVQRNG%2BKJqqcKK9lBJj%2Bnjej%0AlWWZHSNYFauVKf6EuR4%3D%0A"
        },
        {
            "step": "Step 4: Assign Batches (Operator Choose)",
            "desc": "Batch assignment popup - let operators choose during picking",
            "url": "https://downloads.intercomcdn.com/i/o/ep5ydul3/1609015442/00701f92be8e5d23a1f18b150e92/image.png?expires=1773936000&signature=73e38913c253248836d05f5beb7ecd76ce2af2d79a3c7379f931321a02207781&req=dSYnH8l%2FmIVbW%2FMW1HO4zSJ2gDO51EpR2ZkuE2EoKC99h6IyCj3sEqgGfbCv%0A3UbRiENhQNHGchT%2FPQE%3D%0A"
        },
        {
            "step": "Step 5: Packed Items View",
            "desc": "Packed items showing who packed, tracking info, deliver/revert buttons",
            "url": "https://downloads.intercomcdn.com/i/o/ep5ydul3/1609017588/54338289ee9079ec043b46620881/image.png?expires=1773936000&signature=e13d40185714ce96b2e561c8dac72125826dd0a0c7b29496a3878bd8b63c59f1&req=dSYnH8l%2FmoRXUfMW1HO4zcGBIYaEuFc016eD%2B%2FnwLe9ICEqG8mUnvouyjoF1%0AkNtW%0A"
        }
    ]

    # Cin7 Core (DEAR) - Zendesk CDN
    cin7_screens = [
        {
            "step": "Sale Order — Create Order",
            "desc": "Order tab with items, quantities, prices, tax rules. +Copy from Quote or add manually. Assign picker.",
            "url": "https://help.core.cin7.com/hc/article_attachments/15484529025423"
        },
        {
            "step": "Authorize Sale Order",
            "desc": "Once authorized, stock is reserved. Can split order, backorder, or create purchase order if out of stock.",
            "url": "https://help.core.cin7.com/hc/article_attachments/15484502238607"
        },
        {
            "step": "Pick — Select Items from Inventory",
            "desc": "Select Pick tab → +Auto Pick copies lines from order. Click line to see stock at locations. Assign picker. Authorize when done.",
            "url": "https://help.core.cin7.com/hc/article_attachments/15484529052687"
        },
        {
            "step": "Pack — Prepare for Shipping",
            "desc": "Select Pack tab → +Copy from Pick. Assign box numbers. Authorize. Print packing slip.",
            "url": "https://help.core.cin7.com/hc/article_attachments/15484548449039"
        },
        {
            "step": "Ship — Final Fulfillment",
            "desc": "Select Ship tab → +Auto Fill. Enter ship date, carrier, tracking number. Check Ship box. Authorize. Items removed from inventory.",
            "url": "https://help.core.cin7.com/hc/article_attachments/15484548468879"
        },
        {
            "step": "Automating Pick/Pack/Ship",
            "desc": "Settings → General → Sales process customization. Change Pick, Pack, Ship to automatic if these steps don't apply to your business.",
            "url": "https://help.core.cin7.com/hc/article_attachments/15484548479759"
        }
    ]

    # Zoho Inventory - Picklist (external CDN)
    zoho_picklist = [
        {
            "step": "Direct Picklist",
            "desc": "Creating a picklist directly from sales order",
            "url": "https://www.zoho.com/inventory/help/images/picklist/direct-picklist.png"
        },
        {
            "step": "Add Items",
            "desc": "Selecting items to include in picklist",
            "url": "https://www.zoho.com/inventory/help/images/picklist/add-items.png"
        },
        {
            "step": "New Picklist",
            "desc": "Picklist creation form",
            "url": "https://www.zoho.com/inventory/help/images/picklist/new-picklist.png"
        },
        {
            "step": "Create Picklist",
            "desc": "Confirming picklist creation",
            "url": "https://www.zoho.com/inventory/help/images/picklist/create-picklist.png"
        },
        {
            "step": "Bulk Actions",
            "desc": "Batch operations on picklist items",
            "url": "https://www.zoho.com/inventory/help/images/picklist/bulk-actions.png"
        },
        {
            "step": "Update Button",
            "desc": "Updating picklist status",
            "url": "https://www.zoho.com/inventory/help/images/picklist/update-button.png"
        },
        {
            "step": "Update Picklist",
            "desc": "Picklist update confirmation",
            "url": "https://www.zoho.com/inventory/help/images/picklist/update-picklist.png"
        },
        {
            "step": "Set Status",
            "desc": "Changing picklist status (Picked/Packed)",
            "url": "https://www.zoho.com/inventory/help/images/picklist/set-status.png"
        },
        {
            "step": "Picklist → Package",
            "desc": "Converting picklist to package for shipping",
            "url": "https://www.zoho.com/inventory/help/images/picklist/picklist-package.png"
        }
    ]

    # Zoho Inventory - Packages (external CDN)
    zoho_packages = [
        {
            "step": "Package Flow",
            "desc": "End-to-end package workflow diagram",
            "url": "https://www.zoho.com/inventory/help/images/flow/zom-package-flow.png"
        },
        {
            "step": "Package Increase",
            "desc": "Adding items to a package",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/package-increase.png"
        },
        {
            "step": "Create Button",
            "desc": "Initiating package from SO",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/package-create-button.png"
        },
        {
            "step": "New Package Page",
            "desc": "Package creation form",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/package-new-page.png"
        },
        {
            "step": "Advanced Tracking",
            "desc": "Package-level inventory tracking",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/pkg-advanced-inventory-tracking.png"
        },
        {
            "step": "Import Step 1",
            "desc": "Importing package data",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/package-import-1.png"
        },
        {
            "step": "Import Step 2",
            "desc": "Mapping import fields",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/package-import-2.png"
        },
        {
            "step": "Shipment Export",
            "desc": "Exporting shipment data",
            "url": "https://www.zoho.com/inventory/help/images/sales-orders/package-shipment-export.png"
        }
    ]

    # Convert Fishbowl images to base64
    fishbowl_with_uris = []
    for screen in fishbowl_screens:
        filepath = os.path.join(base_dir, screen["file"])
        if os.path.exists(filepath):
            uri = image_to_base64_uri(filepath)
            fishbowl_with_uris.append({
                "uri": uri,
                "step": screen["step"],
                "desc": screen["desc"]
            })
        else:
            print(f"WARNING: File not found: {filepath}")

    # HTML Template
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pick/Pack Competitor Research Gallery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            min-height: 100vh;
        }}

        /* Header & Navigation */
        header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(26, 26, 46, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1rem 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}

        header h1 {{
            font-size: 1.8rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #00d4ff, #0099ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        nav {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            align-items: center;
        }}

        nav a {{
            padding: 0.6rem 1.2rem;
            background: rgba(0, 150, 255, 0.1);
            color: #00d4ff;
            text-decoration: none;
            border-radius: 4px;
            border: 1px solid rgba(0, 212, 255, 0.3);
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }}

        nav a:hover {{
            background: rgba(0, 150, 255, 0.2);
            border-color: rgba(0, 212, 255, 0.6);
            transform: translateY(-2px);
        }}

        /* Main Container */
        main {{
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }}

        /* Section Styles */
        section {{
            margin-bottom: 4rem;
            scroll-margin-top: 100px;
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
            border-bottom: 2px solid rgba(0, 212, 255, 0.3);
            padding-bottom: 1rem;
        }}

        .section-header h2 {{
            font-size: 1.8rem;
            color: #00d4ff;
            flex: 1;
        }}

        .badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .badge-local {{
            background: rgba(76, 175, 80, 0.2);
            color: #81c784;
            border: 1px solid rgba(76, 175, 80, 0.4);
        }}

        .badge-cdn {{
            background: rgba(255, 152, 0, 0.2);
            color: #ffb74d;
            border: 1px solid rgba(255, 152, 0, 0.4);
        }}

        .badge-reference {{
            background: rgba(156, 39, 176, 0.2);
            color: #ce93d8;
            border: 1px solid rgba(156, 39, 176, 0.4);
        }}

        /* Gallery Grid */
        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
            gap: 2rem;
        }}

        .card {{
            background: linear-gradient(135deg, rgba(30, 30, 60, 0.8), rgba(40, 50, 80, 0.8));
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            overflow: hidden;
            transition: all 0.3s ease;
            cursor: pointer;
            display: flex;
            flex-direction: column;
        }}

        .card:hover {{
            transform: translateY(-8px);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.1);
        }}

        .card-image {{
            width: 100%;
            aspect-ratio: 16 / 10;
            background: #000;
            overflow: hidden;
            position: relative;
        }}

        .card-image img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }}

        .card:hover .card-image img {{
            transform: scale(1.05);
        }}

        .card-image .loading {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #999;
            font-size: 0.9rem;
        }}

        .card-content {{
            padding: 1.5rem;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}

        .card-title {{
            font-size: 1.1rem;
            font-weight: 600;
            color: #fff;
            margin-bottom: 0.8rem;
            line-height: 1.4;
        }}

        .card-desc {{
            font-size: 0.95rem;
            color: #b0b0b0;
            flex: 1;
            margin-bottom: 1rem;
            line-height: 1.5;
        }}

        .card-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 1rem;
            border-top: 1px solid rgba(0, 212, 255, 0.1);
        }}

        .zoom-icon {{
            display: inline-block;
            padding: 0.5rem 1rem;
            background: rgba(0, 150, 255, 0.1);
            color: #00d4ff;
            border-radius: 4px;
            font-size: 0.85rem;
            text-decoration: none;
            transition: all 0.2s ease;
            border: 1px solid rgba(0, 212, 255, 0.3);
        }}

        .zoom-icon:hover {{
            background: rgba(0, 150, 255, 0.2);
            border-color: rgba(0, 212, 255, 0.6);
        }}

        /* Reference Section */
        .reference-section {{
            background: linear-gradient(135deg, rgba(30, 30, 60, 0.6), rgba(40, 50, 80, 0.6));
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
        }}

        .reference-section h3 {{
            color: #00d4ff;
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }}

        .reference-section p {{
            color: #b0b0b0;
            margin-bottom: 1rem;
            line-height: 1.6;
        }}

        .reference-links {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-top: 1rem;
        }}

        .reference-links a {{
            color: #00d4ff;
            text-decoration: none;
            font-size: 0.9rem;
            padding: 0.5rem;
            border-radius: 4px;
            transition: all 0.2s ease;
            word-break: break-all;
        }}

        .reference-links a:hover {{
            background: rgba(0, 212, 255, 0.1);
            padding-left: 1rem;
        }}

        /* Process Flow */
        .process-flow {{
            background: linear-gradient(135deg, rgba(30, 30, 60, 0.6), rgba(40, 50, 80, 0.6));
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
        }}

        .flow-diagram {{
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
            font-size: 0.95rem;
            color: #b0b0b0;
            line-height: 1.6;
        }}

        .flow-step {{
            padding: 1rem;
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 4px;
            min-width: 140px;
            text-align: center;
        }}

        .flow-arrow {{
            color: #00d4ff;
            font-weight: bold;
            margin: 0 0.5rem;
        }}

        /* Lightbox */
        .lightbox {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            backdrop-filter: blur(5px);
        }}

        .lightbox.active {{
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.3s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        .lightbox-content {{
            position: relative;
            max-width: 90%;
            max-height: 90%;
            background: #000;
            border-radius: 8px;
            overflow: auto;
        }}

        .lightbox-image {{
            width: 100%;
            height: auto;
            display: block;
        }}

        .lightbox-close {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            border: none;
            font-size: 2rem;
            padding: 0.5rem 1rem;
            cursor: pointer;
            border-radius: 4px;
            transition: all 0.2s ease;
        }}

        .lightbox-close:hover {{
            background: rgba(0, 0, 0, 0.9);
        }}

        .lightbox-title {{
            position: absolute;
            bottom: 1rem;
            left: 1rem;
            right: 1rem;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            padding: 1rem;
            border-radius: 4px;
            font-size: 1rem;
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            header {{
                padding: 1rem;
            }}

            header h1 {{
                font-size: 1.3rem;
            }}

            nav {{
                flex-direction: column;
                gap: 0.5rem;
            }}

            nav a {{
                width: 100%;
                text-align: center;
            }}

            main {{
                padding: 1rem;
            }}

            .gallery {{
                grid-template-columns: 1fr;
            }}

            .section-header {{
                flex-direction: column;
                align-items: flex-start;
            }}

            .flow-diagram {{
                flex-direction: column;
            }}

            .flow-arrow {{
                transform: rotate(90deg);
            }}

            .lightbox-content {{
                max-width: 95%;
                max-height: 95%;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>Pick/Pack Competitor Research Gallery</h1>
        <nav>
            <a href="#fishbowl">Fishbowl</a>
            <a href="#katana">Katana MRP</a>
            <a href="#cin7">Cin7 Core</a>
            <a href="#zoho">Zoho Inventory</a>
            <a href="#inflow">inFlow</a>
            <a href="#sos">SOS Inventory</a>
            <a href="#amazon">Amazon MCF/FBA</a>
        </nav>
    </header>

    <main>
        <!-- Fishbowl Section -->
        <section id="fishbowl">
            <div class="section-header">
                <h2>Fishbowl Inventory</h2>
                <span class="badge badge-local">Local Base64</span>
            </div>
            <div class="gallery">
"""

    # Add Fishbowl cards
    for item in fishbowl_with_uris:
        html_template += f"""                <div class="card" onclick="openLightbox(this)">
                    <div class="card-image">
                        <img src="{item['uri']}" alt="{item['step']}" loading="lazy">
                    </div>
                    <div class="card-content">
                        <div class="card-title">{item['step']}</div>
                        <div class="card-desc">{item['desc']}</div>
                        <div class="card-footer">
                            <span class="zoom-icon">Click to zoom</span>
                        </div>
                    </div>
                </div>
"""

    html_template += """            </div>
        </section>

        <!-- Katana MRP Section -->
        <section id="katana">
            <div class="section-header">
                <h2>Katana MRP</h2>
                <span class="badge badge-cdn">External CDN</span>
            </div>
            <div class="gallery">
"""

    # Add Katana cards
    for item in katana_screens:
        html_template += f"""                <div class="card" onclick="openLightbox(this)">
                    <div class="card-image">
                        <img src="{item['url']}" alt="{item['step']}" loading="lazy" onerror="this.alt='Image failed to load'">
                    </div>
                    <div class="card-content">
                        <div class="card-title">{item['step']}</div>
                        <div class="card-desc">{item['desc']}</div>
                        <div class="card-footer">
                            <span class="zoom-icon">Click to zoom</span>
                        </div>
                    </div>
                </div>
"""

    html_template += """            </div>
        </section>

        <!-- Cin7 Core Section -->
        <section id="cin7">
            <div class="section-header">
                <h2>Cin7 Core (DEAR)</h2>
                <span class="badge badge-cdn">External CDN</span>
            </div>
            <div class="gallery">
"""

    # Add Cin7 cards
    for item in cin7_screens:
        html_template += f"""                <div class="card" onclick="openLightbox(this)">
                    <div class="card-image">
                        <img src="{item['url']}" alt="{item['step']}" loading="lazy" onerror="this.alt='Image failed to load'">
                    </div>
                    <div class="card-content">
                        <div class="card-title">{item['step']}</div>
                        <div class="card-desc">{item['desc']}</div>
                        <div class="card-footer">
                            <span class="zoom-icon">Click to zoom</span>
                        </div>
                    </div>
                </div>
"""

    html_template += """            </div>
        </section>

        <!-- Zoho Inventory Section -->
        <section id="zoho">
            <div class="section-header">
                <h2>Zoho Inventory</h2>
                <span class="badge badge-cdn">External CDN</span>
            </div>

            <!-- Picklist Subsection -->
            <h3 style="color: #00d4ff; margin-bottom: 1.5rem; margin-top: 2rem; font-size: 1.2rem;">Picklist Workflow</h3>
            <div class="gallery">
"""

    # Add Zoho Picklist cards
    for item in zoho_picklist:
        html_template += f"""                <div class="card" onclick="openLightbox(this)">
                    <div class="card-image">
                        <img src="{item['url']}" alt="{item['step']}" loading="lazy" onerror="this.alt='Image failed to load'">
                    </div>
                    <div class="card-content">
                        <div class="card-title">{item['step']}</div>
                        <div class="card-desc">{item['desc']}</div>
                        <div class="card-footer">
                            <span class="zoom-icon">Click to zoom</span>
                        </div>
                    </div>
                </div>
"""

    html_template += """            </div>

            <!-- Packages Subsection -->
            <h3 style="color: #00d4ff; margin-bottom: 1.5rem; margin-top: 2rem; font-size: 1.2rem;">Package Workflow</h3>
            <div class="gallery">
"""

    # Add Zoho Packages cards
    for item in zoho_packages:
        html_template += f"""                <div class="card" onclick="openLightbox(this)">
                    <div class="card-image">
                        <img src="{item['url']}" alt="{item['step']}" loading="lazy" onerror="this.alt='Image failed to load'">
                    </div>
                    <div class="card-content">
                        <div class="card-title">{item['step']}</div>
                        <div class="card-desc">{item['desc']}</div>
                        <div class="card-footer">
                            <span class="zoom-icon">Click to zoom</span>
                        </div>
                    </div>
                </div>
"""

    html_template += """            </div>
        </section>

        <!-- inFlow Inventory Section -->
        <section id="inflow">
            <div class="section-header">
                <h2>inFlow Inventory</h2>
                <span class="badge badge-reference">Reference Links</span>
            </div>
            <div class="reference-section">
                <h3>Workflow Overview</h3>
                <p>
                    inFlow uses a tabbed Pick → Ship workflow on sales orders. Pick tab: manual or auto-fill from SO.
                    Ship tab: add carrier, tracking, print shipping label. 50+ built-in carrier integrations.
                    Barcode scanning native throughout. Split order support for partial fulfillment.
                </p>
                <div class="reference-links">
                    <a href="https://www.inflowinventory.com" target="_blank">inFlow Inventory - Main Site</a>
                    <a href="https://www.inflowinventory.com" target="_blank">Sales Orders: Pick, Pack, & Ship (Learning Center)</a>
                </div>
            </div>
        </section>

        <!-- SOS Inventory Section -->
        <section id="sos">
            <div class="section-header">
                <h2>SOS Inventory</h2>
                <span class="badge badge-reference">Reference Links</span>
            </div>
            <div class="reference-section">
                <h3>Workflow Overview</h3>
                <p>
                    SOS uses text-based pick tickets generated from sales orders. QuickBooks-tight integration.
                    Serial/lot tracking optional per item. Simple instruction document approach rather than formal WMS.
                </p>
                <div class="reference-links">
                    <a href="https://www.sosinventory.com/features/pick-tickets" target="_blank">SOS Inventory - Pick Tickets</a>
                    <a href="https://www.sosinventory.com/features/packing-slips" target="_blank">SOS Inventory - Packing Slips</a>
                </div>
            </div>
        </section>

        <!-- Amazon MCF/FBA Section -->
        <section id="amazon">
            <div class="section-header">
                <h2>Amazon MCF/FBA</h2>
                <span class="badge badge-reference">Black-Box System</span>
            </div>
            <div class="process-flow">
                <h3 style="color: #00d4ff; margin-bottom: 1.5rem;">Fulfillment Process Flow</h3>
                <div class="flow-diagram">
                    <div class="flow-step">Inbound Shipment</div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step">Receive & Stow</div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step">Auto Pick Task</div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step">Scanner Pick</div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step">Pack Station</div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step">Carrier Sort & Ship</div>
                    <div class="flow-arrow">→</div>
                    <div class="flow-step">Tracking</div>
                </div>
            </div>
            <div class="reference-section">
                <h3>Key Metrics & Features</h3>
                <p>
                    <strong>Pick Accuracy:</strong> 99.97%+ | <strong>Technology:</strong> CubiScan auto-boxing |
                    <strong>Picking Model:</strong> Tote-based multi-order picking | <strong>Integration:</strong> Seller Central API
                </p>
                <div class="reference-links">
                    <a href="https://sell.amazon.com/fulfillment-by-amazon" target="_blank">Amazon FBA - Main Program</a>
                    <a href="https://sell.amazon.com/multi-channel-fulfillment" target="_blank">Amazon MCF - Multi-Channel Fulfillment</a>
                </div>
            </div>
        </section>
    </main>

    <!-- Lightbox -->
    <div id="lightbox" class="lightbox">
        <div class="lightbox-content">
            <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
            <img id="lightbox-image" class="lightbox-image" src="" alt="">
            <div class="lightbox-title" id="lightbox-title"></div>
        </div>
    </div>

    <script>
        function openLightbox(card) {
            const lightbox = document.getElementById('lightbox');
            const img = card.querySelector('img');
            const title = card.querySelector('.card-title').textContent;

            document.getElementById('lightbox-image').src = img.src;
            document.getElementById('lightbox-image').alt = title;
            document.getElementById('lightbox-title').textContent = title;

            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        // Close lightbox on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeLightbox();
            }
        });

        // Close lightbox on background click
        document.getElementById('lightbox').addEventListener('click', (e) => {
            if (e.target.id === 'lightbox') {
                closeLightbox();
            }
        });
    </script>
</body>
</html>
"""

    return html_template

# Main execution
if __name__ == "__main__":
    base_dir = "/sessions/vigilant-practical-hamilton/mnt/Inventory Management/Inventory-MWD-/Research/pick-pack/screenshots"
    output_file = os.path.join(base_dir, "screenshot-gallery.html")

    print("Building HTML screenshot gallery...")
    print(f"Converting Fishbowl PNG images to base64...")

    # Generate HTML
    html_content = create_html_gallery()

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Gallery created successfully!")
    print(f"✓ Output: {output_file}")
    print(f"\nGallery includes:")
    print(f"  • Fishbowl Inventory (6 images, base64 embedded)")
    print(f"  • Katana MRP (5 images, external CDN)")
    print(f"  • Cin7 Core/DEAR (6 images, external CDN)")
    print(f"  • Zoho Inventory (17 images: 9 picklist + 8 package)")
    print(f"  • inFlow Inventory (reference links)")
    print(f"  • SOS Inventory (reference links)")
    print(f"  • Amazon MCF/FBA (process flow + reference links)")
    print(f"\nTotal: 39 competitor screenshots + reference sections")
