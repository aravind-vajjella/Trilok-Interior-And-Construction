#!/usr/bin/env python3
"""
Insert the comprehensive Brands Section into index.html and update footer links.
"""

brands_data = [
    # Plywood
    {
        'cat': 'plywood',
        'cat_label': 'Plywood',
        'logo': 'assets/brands/centuryply.svg',
        'name': 'Century Ply',
        'spec': 'Club Prime & Marine Grade BWP',
        'desc': 'Boiling waterproof calibrated core plywood with patented ViroKill technology and 25-30 year anti-borer/termite warranty.',
        'perk1': '25+ Yr Warranty',
        'perk2': 'Carcasses & Shutter Cores'
    },
    {
        'cat': 'plywood',
        'cat_label': 'Plywood',
        'logo': 'assets/brands/greenply.svg',
        'name': 'Greenply',
        'spec': 'Green Club Platinum E-0 Emission',
        'desc': 'India\'s premier zero-emission E-0 structural plywood with 400% lifetime replacement guarantee and uncompromised internal air quality.',
        'perk1': 'Zero Toxic Emissions',
        'perk2': 'Master Beds & Living Millwork'
    },
    {
        'cat': 'plywood',
        'cat_label': 'Plywood',
        'logo': 'assets/brands/duroply.svg',
        'name': 'Duro Ply',
        'spec': 'Duro Pumaply & Duro Marine',
        'desc': '100% select hardwood veneer construction since 1957. Renowned across Telangana for unmatched structural density and screw-holding strength.',
        'perk1': 'Hardwood Core',
        'perk2': 'Heavy Duty Partitions'
    },
    {
        'cat': 'plywood',
        'cat_label': 'Plywood',
        'logo': 'assets/brands/austinply.svg',
        'name': 'Austin Ply',
        'spec': 'Austin Defender BS-1088 Marine',
        'desc': 'Quad-press calibrated plywood with micro-gapless veneer technology. Perfectly flat surfaces optimized for acrylic and laminate pressing.',
        'perk1': 'BS-1088 Marine Spec',
        'perk2': 'Modular Kitchen Boxes'
    },
    {
        'cat': 'plywood',
        'cat_label': 'Plywood',
        'logo': 'assets/brands/sylvanply.svg',
        'name': 'Sylvan Ply',
        'spec': 'Robusta & Z-Black Premium Plywood',
        'desc': 'High-density timber core with high-pressure preservative vacuum treatment. Engineered for tropical climate stability in Hyderabad & AP.',
        'perk1': 'High Preservative BWP',
        'perk2': 'Vanity & Wet Area Millwork'
    },

    # Hardware
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/hafele.svg',
        'name': 'Häfele',
        'spec': 'German Architectural Hardware & Hinges',
        'desc': 'World-standard German hydraulic soft-close concealed hinges, Metalla drawer systems, push-to-open catches, and wardrobe profile runners.',
        'perk1': 'German Engineering',
        'perk2': 'Lifetime Action Smoothness'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/hettich.svg',
        'name': 'Hettich',
        'spec': 'Sensys Soft-Close & InnoTech Atira',
        'desc': 'Signature German hardware with integrated dampening, Quadro runner channels, corner cargo carousels, and concealed sliding wardrobe fittings.',
        'perk1': 'Silent Damping Hinge',
        'perk2': 'Deep Kitchen Pull-Outs'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/ebco.svg',
        'name': 'Ebco',
        'spec': 'Livsmart Furniture & Bed Fittings',
        'desc': 'Heavy-duty hydraulic bed lift mechanisms, soft-closing telescopic slides, concealed keyboard drawers, and modular wire accessories.',
        'perk1': 'High Weight Rating',
        'perk2': 'Bed Storage & Pull-Out Trays'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/nimmi.svg',
        'name': 'Nimmi',
        'spec': 'Architectural Profile Handles & Pulls',
        'desc': 'Architectural aluminium J-profile handles, concealed edge trims, mortise door hardware, and designer brass-tone wardrobe pulls.',
        'perk1': 'Solid Anodized Finish',
        'perk2': 'Wardrobes & TV Units'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/ozone.svg',
        'name': 'Ozone',
        'spec': 'Architectural Glass Hardware & Locks',
        'desc': 'Frameless glass shower hinges, sliding barn-door rollers, digital touch biometric locks, and stainless steel patch fittings.',
        'perk1': 'SS 304 Grade Metal',
        'perk2': 'Glass Showers & Partitions'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/blum.svg',
        'name': 'Blum',
        'spec': 'Austrian Blumotion & Aventos Systems',
        'desc': 'Ultra-smooth motion technology. Aventos lift mechanisms for overhead wall cabinets, tandembox soft-close drawer runners with zero sag.',
        'perk1': 'Austrian Precision',
        'perk2': 'Overhead Flap Units'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/godrej.svg',
        'name': 'Godrej',
        'spec': 'Main Door Locks & Mortise Systems',
        'desc': 'High-security multi-lock Euro-profile brass cylinders, Aldrop latches, and computer-coded master keying systems for total peace of mind.',
        'perk1': 'Multi-Point Security',
        'perk2': 'Main & Bedroom Entrance Doors'
    },
    {
        'cat': 'hardware',
        'cat_label': 'Hardware',
        'logo': 'assets/brands/sleek.svg',
        'name': 'Sleek by Asian Paints',
        'spec': 'Modular Kitchen Components & Pull-outs',
        'desc': 'Specialized stainless steel cutlery trays, pull-out pantry larders, under-sink organizers, and rolling shutter appliance garages.',
        'perk1': 'Asian Paints Endorsed',
        'perk2': 'Pantry & Spice Organizers'
    },

    # Construction Steel
    {
        'cat': 'steel',
        'cat_label': 'TMT Steel',
        'logo': 'assets/brands/tatasteel.svg',
        'name': 'Tata Steel',
        'spec': 'Tata Tiscon 550D Super Ductile TMT',
        'desc': 'India\'s leading primary TMT rebar. Superior earthquake ductility, low carbon purity, and enhanced concrete bonding for home foundations & columns.',
        'perk1': 'Fe 550D Super Ductile',
        'perk2': 'RCC Foundations & Pillars'
    },
    {
        'cat': 'steel',
        'cat_label': 'TMT Steel',
        'logo': 'assets/brands/jswsteel.svg',
        'name': 'JSW Steel',
        'spec': 'JSW Neosteel 550D High Tensile',
        'desc': 'HYQST technology rebar with uniform rib geometry, high strain-hardening ratio, and exceptional thermal resistance during civil construction.',
        'perk1': 'HYQST Quenched Purity',
        'perk2': 'Roof Slabs & Beam Frames'
    },
    {
        'cat': 'steel',
        'cat_label': 'TMT Steel',
        'logo': 'assets/brands/jindalsteel.svg',
        'name': 'Jindal Steel',
        'spec': 'Jindal Panther 550D TMT Rebar',
        'desc': 'Virgin iron ore steel with parallel rib patterns for high seismic zones. Guaranteed bendability with zero micro-cracks in foundation footings.',
        'perk1': 'Clean Virgin Steel',
        'perk2': 'Plinth & Column Binders'
    },
    {
        'cat': 'steel',
        'cat_label': 'TMT Steel',
        'logo': 'assets/brands/kamdhenusteel.svg',
        'name': 'Kamdhenu Steel',
        'spec': 'Kamdhenu PAS 10000 TMT',
        'desc': 'Double-rib high-grip rebars engineered for heavy structural loads, anti-corrosive properties, and maximum concrete matrix adhesion.',
        'perk1': 'Double-Rib Grip Matrix',
        'perk2': 'Sump & Retaining Walls'
    },

    # Paints
    {
        'cat': 'paints',
        'cat_label': 'Paints',
        'logo': 'assets/brands/asianpaints.svg',
        'name': 'Asian Paints',
        'spec': 'Royale Luxury Emulsion & PU Italian Polish',
        'desc': 'Washable Teflon-protected luxury emulsions, Nilaya wall coverings, and polyurethane Italian wood polishes for rich lustre and longevity.',
        'perk1': 'Teflon Stain Shield',
        'perk2': 'Interior Living & Teak Polish'
    },
    {
        'cat': 'paints',
        'cat_label': 'Paints',
        'logo': 'assets/brands/berger.svg',
        'name': 'Berger Paints',
        'spec': 'Silk Breathe Easy & WeatherCoat',
        'desc': 'Ultra-luxury interior emulsions with silver ion anti-bacterial technology and WeatherCoat Long Life exterior protection for independent villas.',
        'perk1': 'Anti-Bacterial Silver Ion',
        'perk2': 'Bedrooms & Exterior Facades'
    },
    {
        'cat': 'paints',
        'cat_label': 'Paints',
        'logo': 'assets/brands/nerolac.svg',
        'name': 'Nerolac',
        'spec': 'Impressions HD & Low-VOC Emulsions',
        'desc': 'Japanese micro-pigment technology delivering rich high-definition depths, zero lead formulation, and breathable surface finishes.',
        'perk1': 'Ultra Low VOC & Eco-Clean',
        'perk2': 'Ceilings & Feature Walls'
    },
    {
        'cat': 'paints',
        'cat_label': 'Paints',
        'logo': 'assets/brands/dulux.svg',
        'name': 'Dulux',
        'spec': 'Velvet Touch & Lumitec Sheen',
        'desc': 'Rich velvety touch emulsions with light-reflecting Lumitec pearls, creating luminous room ambiance and glowing cove illumination.',
        'perk1': 'Velvet Touch Glow',
        'perk2': 'Dining & Foyer Areas'
    },

    # Plumbing
    {
        'cat': 'plumbing',
        'cat_label': 'Plumbing',
        'logo': 'assets/brands/astralpipes.svg',
        'name': 'Astral Pipes',
        'spec': 'CPVC Pro & DrainMaster SWR Pipes',
        'desc': 'NSF-certified lead-free CPVC hot & cold water lines capable of 93°C pressure, combined with ring-fit DrainMaster acoustic soil drainage.',
        'perk1': '100% Lead Free & 93°C Safe',
        'perk2': 'Concealed Bathroom Lines'
    },
    {
        'cat': 'plumbing',
        'cat_label': 'Plumbing',
        'logo': 'assets/brands/ashirvadpipes.svg',
        'name': 'Ashirvad Pipes',
        'spec': 'FlowGuard Plus & Silent SWR by Aliaxis',
        'desc': 'Triple-layer acoustic drainage piping minimizing flush noise in multistory homes, with high chemical resistance and zero calcification.',
        'perk1': 'Aliaxis Silent Drainage',
        'perk2': 'Vertical Shafts & Under-Slab'
    },

    # Electrical Items
    {
        'cat': 'electrical',
        'cat_label': 'Electrical',
        'logo': 'assets/brands/goldmedal.svg',
        'name': 'Goldmedal',
        'spec': 'Air & Curve Luxury Modular Switches',
        'desc': 'Ultra-flat modular glass switch plates, feather-touch smart dimmers, USB-C wall outlets, and night footlight step illuminators.',
        'perk1': 'Glass Plate Luxury',
        'perk2': 'Living & Master Switchboards'
    },
    {
        'cat': 'electrical',
        'cat_label': 'Electrical',
        'logo': 'assets/brands/legrand.svg',
        'name': 'Legrand',
        'spec': 'Arteor & Myrius French Switch Systems',
        'desc': 'World-renowned French electrical systems with self-extinguishing polycarbonate plates, silver contact switches, and smart home modules.',
        'perk1': 'French Engineering & Safety',
        'perk2': 'Executive Residences & Villas'
    },
    {
        'cat': 'electrical',
        'cat_label': 'Electrical',
        'logo': 'assets/brands/havells.svg',
        'name': 'Havells',
        'spec': 'Fabio Modular Switchgear & Distribution',
        'desc': 'Dual-shutter spark-free switches, heavy-duty miniature circuit breakers (MCBs), and RCCB residual current shock-prevention panels.',
        'perk1': 'Shock-Proof Protection',
        'perk2': 'Main DB & Appliance Boards'
    },
    {
        'cat': 'electrical',
        'cat_label': 'Electrical',
        'logo': 'assets/brands/anchor.svg',
        'name': 'Anchor by Panasonic',
        'spec': 'Roma & Rider Modular Electricals',
        'desc': 'Japanese Panasonic quality assurance. High endurance 10A-25A heavy load power sockets with child safety shutters and captive screws.',
        'perk1': 'Panasonic Japanese Quality',
        'perk2': 'AC, Geyser & Kitchen Sockets'
    },
    {
        'cat': 'electrical',
        'cat_label': 'Electrical',
        'logo': 'assets/brands/polycab.svg',
        'name': 'Polycab',
        'spec': 'Switchgear, Isolators & PVC Conduits',
        'desc': 'Heavy mechanical strength flame-retardant PVC electrical conduits, distribution boxes, and industrial-grade isolators.',
        'perk1': 'Heavy-Duty Concealed Conduit',
        'perk2': 'Slab & Wall Concealed Chasing'
    },

    # Wiring
    {
        'cat': 'wiring',
        'cat_label': 'Wiring',
        'logo': 'assets/brands/finolex.svg',
        'name': 'Finolex',
        'spec': 'Flame Retardant (FR) Copper Cables',
        'desc': '100% electrolytic virgin high-conductivity copper conductors with specialized oxygen-free insulation preventing heat accumulation.',
        'perk1': '100% Electrolytic Copper',
        'perk2': 'Full House Main Lines'
    },
    {
        'cat': 'wiring',
        'cat_label': 'Wiring',
        'logo': 'assets/brands/polycab.svg',
        'name': 'Polycab',
        'spec': 'Green Wire FRLS-H Zero Halogen',
        'desc': 'Fire-retardant low-smoke copper cables with zero halogen emission during extreme heat. Highest safety certified for luxury apartments.',
        'perk1': 'FRLS-H Low Toxic Smoke',
        'perk2': 'Lighting & Power Circuits'
    },
    {
        'cat': 'wiring',
        'cat_label': 'Wiring',
        'logo': 'assets/brands/havells.svg',
        'name': 'Havells',
        'spec': 'LifeLine Plus S3 HRFR Copper Wires',
        'desc': 'Triple-layer insulation certified to withstand temperatures up to 105°C, with built-in anti-termite and anti-rodent sheath repellents.',
        'perk1': '105°C Thermal Tolerance',
        'perk2': 'Heavy Kitchen & Inverter Feeds'
    },
    {
        'cat': 'wiring',
        'cat_label': 'Wiring',
        'logo': 'assets/brands/anchor.svg',
        'name': 'Anchor by Panasonic',
        'spec': 'Advance FR Multi-Strand House Wires',
        'desc': 'Precision multi-strand annealed copper wires with uniform current density and Japanese Panasonic quality testing on every coil.',
        'perk1': 'Uniform Current Density',
        'perk2': 'False Ceiling & Cove Feeds'
    }
]

# Ticker unique logos
unique_logos = []
seen = set()
for b in brands_data:
    if b['logo'] not in seen:
        seen.add(b['logo'])
        unique_logos.append((b['logo'], b['name']))

ticker_html = '<div class="brand-ticker-wrap reveal-on-scroll">\n<div class="brand-ticker-track">\n'
for _ in range(2): # duplicate for seamless loop
    for logo, name in unique_logos:
        ticker_html += f'  <div class="brand-ticker-item" title="{name}"><img src="{logo}" alt="{name} Logo" loading="lazy" width="140" height="38"/></div>\n'
ticker_html += '</div>\n</div>\n'

cards_html = ''
for b in brands_data:
    cards_html += f'''<div class="brand-card reveal-on-scroll" data-category="{b['cat']}">
  <div class="brand-card__header">
    <span class="brand-cat-pill">{b['cat_label']}</span>
    <span class="brand-verified" title="Certified Brand Partner"><i class="fa-solid fa-circle-check"></i> Genuine</span>
  </div>
  <div class="brand-logo-container">
    <img src="{b['logo']}" alt="{b['name']} Logo" class="brand-logo-img" loading="lazy" width="180" height="44"/>
  </div>
  <h3 class="brand-card__title">{b['name']}</h3>
  <p class="brand-card__spec">{b['spec']}</p>
  <p class="brand-card__desc">{b['desc']}</p>
  <div class="brand-card__footer">
    <span><i class="fa-solid fa-shield-halved"></i> {b['perk1']}</span>
    <span>{b['perk2']}</span>
  </div>
</div>
'''

section_html = f'''
<section class="section-brands" id="brands">
<div class="container">
<div class="section-head text-center reveal-on-scroll">
<span class="section-tag"><i class="fa-solid fa-certificate"></i> Certified Material Standards</span>
<h2 class="section-title">World-Class Brands Used by <span class="text-gold-shimmer">Trilok</span></h2>
<p class="section-subtitle">
We partner exclusively with India's and the world's most trusted manufacturers. Zero counterfeit or unbranded materials — every sheet of plywood, hinge, steel bar, paint coat, pipe, and electrical wire comes with certified manufacturer warranty.
</p>
</div>

{ticker_html}

<!-- Brand Category Filter Buttons -->
<div class="brand-filters reveal-on-scroll">
<button class="brand-filter-btn active" data-filter="all"><i class="fa-solid fa-layer-group"></i> All Brands (29)</button>
<button class="brand-filter-btn" data-filter="plywood"><i class="fa-solid fa-tree"></i> Plywood (5)</button>
<button class="brand-filter-btn" data-filter="hardware"><i class="fa-solid fa-gears"></i> Hardware &amp; Fittings (8)</button>
<button class="brand-filter-btn" data-filter="steel"><i class="fa-solid fa-cubes-stacked"></i> TMT Steel (4)</button>
<button class="brand-filter-btn" data-filter="paints"><i class="fa-solid fa-brush"></i> Paints &amp; Finishes (4)</button>
<button class="brand-filter-btn" data-filter="plumbing"><i class="fa-solid fa-faucet-drip"></i> Plumbing &amp; Pipes (2)</button>
<button class="brand-filter-btn" data-filter="electrical"><i class="fa-solid fa-plug"></i> Electrical Switches (5)</button>
<button class="brand-filter-btn" data-filter="wiring"><i class="fa-solid fa-bolt"></i> High-Grade Wiring (4)</button>
</div>

<!-- Brands Grid -->
<div class="brands-grid" id="brandsGrid">
{cards_html}
</div>

</div>
</section>
'''

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '</section>\n\n<section class="section-process" id="process">'
if target in content:
    new_content = content.replace(target, '</section>\n' + section_html + '\n<section class="section-process" id="process">')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully inserted section-brands into index.html!")
else:
    print("Target string not found in index.html!")
