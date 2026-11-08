#!/usr/bin/env python3
"""
Add the Brand Directory & Specifications into materials.html.
"""

import sys
import importlib.util

spec = importlib.util.spec_from_file_location("ibs", "scripts/insert-brands-section.py")
ibs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ibs)

materials_brands_html = f'''
<section class="section-brands" id="brands" style="padding: 90px 0;">
<div class="container">
<div class="section-head text-center reveal-on-scroll">
<span class="section-tag"><i class="fa-solid fa-award"></i> Certified Material Specification Directory</span>
<h2 class="section-title">Verified Brands Specified by <span class="text-gold-shimmer">Trilok</span></h2>
<p class="section-subtitle">
We install only genuine materials sourced directly from authorized company distributors with factory test certificates. Explore the tier-1 brands powering our civil construction and bespoke interior carpentry.
</p>
</div>

{ibs.ticker_html}

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
<div class="brands-grid" id="materialsBrandsGrid">
{ibs.cards_html}
</div>

<!-- Instagram Callout for Material Testing & Unboxing -->
<div class="instagram-profile-header reveal-on-scroll mt-5">
<div class="instagram-profile-left">
<div class="instagram-avatar-wrap">
<img src="logo.jpg" alt="Trilok Interiors &amp; Construction" class="instagram-avatar"/>
<span class="instagram-badge-live">REELS</span>
</div>
<div class="instagram-profile-info">
<h3>Watch Material Quality Tests on Instagram</h3>
<p>See water boiling tests, plywood calibration checks, and hardware durability demos on <strong>@trilok._interior</strong></p>
</div>
</div>
<div class="instagram-profile-actions">
<a class="btn-instagram-follow magnetic-target" href="https://www.instagram.com/trilok._interior/" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-instagram"></i> Watch Material Tests on Instagram
</a>
</div>
</div>

</div>
</section>
'''

with open('materials.html', 'r', encoding='utf-8') as f:
    m_content = f.read()

target = '</section>\n\n</main>'
if target in m_content:
    new_m = m_content.replace(target, '</section>\n' + materials_brands_html + '\n</main>')
    with open('materials.html', 'w', encoding='utf-8') as f:
        f.write(new_m)
    print("Successfully added brands section to materials.html!")
else:
    print("Target not found in materials.html")
