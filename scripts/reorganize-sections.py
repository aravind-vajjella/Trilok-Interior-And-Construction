#!/usr/bin/env python3
"""
Update index.html:
1. Update Instagram section to feature exactly the 4 requested Reels with authentic extracted thumbnails.
2. Remove the duplicated brands section from above #process.
3. Place a single clean brands section right under #founder.
"""

import re
import importlib.util

spec = importlib.util.spec_from_file_location("ibs", "scripts/insert-brands-section.py")
ibs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ibs)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -------------------------------------------------------------
# 1. Instagram Section with the 4 Exact Reels
# -------------------------------------------------------------
reels_html = '''<section class="section-instagram" id="instagram">
<div class="container">
<div class="section-head text-center reveal-on-scroll">
<span class="section-tag"><i class="fa-brands fa-instagram"></i> Real On-Site Stories &amp; Reels</span>
<h2 class="section-title">Daily Transformations on <span class="text-gold-shimmer">Instagram</span></h2>
<p class="section-subtitle">
Watch real site walkthroughs, structural column casting, modular kitchen fittings, and material guides straight from our job sites across Hyderabad, Siddipet &amp; Warangal. Click any video to open and watch the reel on Instagram.
</p>
</div>

<!-- Instagram Profile Live Header -->
<div class="instagram-profile-header reveal-on-scroll">
<div class="instagram-profile-left">
<div class="instagram-avatar-wrap">
<img src="logo.jpg" alt="Trilok Interiors &amp; Construction" class="instagram-avatar"/>
<span class="instagram-badge-live">REELS</span>
</div>
<div class="instagram-profile-info">
<h3>@trilok._interior <i class="fa-solid fa-circle-check instagram-verified-check" title="Verified Studio"></i></h3>
<p>Trilok Interiors &amp; Construction • Civil House Construction &amp; Turnkey Luxury Interiors • <strong>Hyderabad &amp; AP</strong></p>
</div>
</div>
<div class="instagram-profile-actions">
<a class="btn-instagram-follow magnetic-target" href="https://www.instagram.com/trilok._interior/" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-instagram"></i> Follow on Instagram
</a>
<a class="btn-instagram-outline magnetic-target" href="https://wa.me/918332098477?text=Hello%20Trilok%20Team,%20I%20saw%20your%20Instagram%20reels%20and%20want%20to%20discuss%20my%20home%20project" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-whatsapp"></i> WhatsApp Founder
</a>
</div>
</div>

<!-- 4 Featured Reels Grid -->
<div class="reels-grid">

<!-- Reel 1: When to Plan Interiors (Right After Slab & Brickwork) -->
<div class="reel-card reveal-on-scroll">
<a class="reel-media-wrap" href="https://www.instagram.com/reel/DaAkDWPtYVt/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank" title="Watch on Instagram: When to Plan Home Interiors">
<img class="reel-thumbnail" src="assets/instagram/reel-daakdwptyvt.jpg" alt="Building your dream home? Don't make the biggest mistake - Plan Interiors Early" loading="lazy" width="360" height="640"/>
<div class="reel-top-bar">
<span class="reel-badge-pill"><i class="fa-brands fa-instagram"></i> Reel</span>
<span class="reel-views-pill"><i class="fa-solid fa-heart"></i> 595+</span>
</div>
<div class="reel-center-play">
<i class="fa-solid fa-play"></i>
</div>
<div class="reel-bottom-gradient">
<span class="reel-location"><i class="fa-solid fa-lightbulb"></i> Construction Tip</span>
<h3 class="reel-title">When to Plan Interiors? Right After Slab &amp; Brickwork</h3>
<p class="reel-tags">#ConstructionTips #HomeConstruction #SaveCosts</p>
</div>
</a>
<div class="reel-action-footer">
<a class="btn-reel-redirect magnetic-target" href="https://www.instagram.com/reel/DaAkDWPtYVt/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-instagram"></i> Watch Reel on Instagram
</a>
</div>
</div>

<!-- Reel 2: 3 Rules to Make Bathroom Look Big, Rich & Neat -->
<div class="reel-card reveal-on-scroll">
<a class="reel-media-wrap" href="https://www.instagram.com/reel/DaZBmNDpnB4/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank" title="Watch on Instagram: 3 Simple Rules to Make Bathroom Look Big, Rich & Neat">
<img class="reel-thumbnail" src="assets/instagram/reel-dazbmndpnb4.jpg" alt="Want to make your bathroom look BIG, RICH, and NEAT? 3 Simple Rules" loading="lazy" width="360" height="640"/>
<div class="reel-top-bar">
<span class="reel-badge-pill"><i class="fa-brands fa-instagram"></i> Reel</span>
<span class="reel-views-pill"><i class="fa-solid fa-bath"></i> Designer Bath</span>
</div>
<div class="reel-center-play">
<i class="fa-solid fa-play"></i>
</div>
<div class="reel-bottom-gradient">
<span class="reel-location"><i class="fa-solid fa-ruler-combined"></i> Technical Design</span>
<h3 class="reel-title">3 Simple Rules: Make Your Bathroom Look Big &amp; Rich</h3>
<p class="reel-tags">#BathroomDesign #GlassPartition #FloatingVanity</p>
</div>
</a>
<div class="reel-action-footer">
<a class="btn-reel-redirect magnetic-target" href="https://www.instagram.com/reel/DaZBmNDpnB4/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-instagram"></i> Watch Reel on Instagram
</a>
</div>
</div>

<!-- Reel 3: Civil Construction & Space Planning -->
<div class="reel-card reveal-on-scroll">
<a class="reel-media-wrap" href="https://www.instagram.com/reel/Daxevp-pwi5/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank" title="Watch on Instagram: Civil & Interior Space Planning">
<img class="reel-thumbnail" src="assets/instagram/reel-daxevp-pwi5.jpg" alt="Civil Construction & Space Planning - Maximize Every Sq.Ft" loading="lazy" width="360" height="640"/>
<div class="reel-top-bar">
<span class="reel-badge-pill"><i class="fa-brands fa-instagram"></i> Reel</span>
<span class="reel-views-pill"><i class="fa-solid fa-compass-drafting"></i> Space Guide</span>
</div>
<div class="reel-center-play">
<i class="fa-solid fa-play"></i>
</div>
<div class="reel-bottom-gradient">
<span class="reel-location"><i class="fa-solid fa-building"></i> Site Planning</span>
<h3 class="reel-title">Civil &amp; Interior Space Planning: Maximize Every Sq.Ft</h3>
<p class="reel-tags">#SpacePlanning #CivilEngineering #LuxuryInteriors</p>
</div>
</a>
<div class="reel-action-footer">
<a class="btn-reel-redirect magnetic-target" href="https://www.instagram.com/reel/Daxevp-pwi5/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-instagram"></i> Watch Reel on Instagram
</a>
</div>
</div>

<!-- Reel 4: Dream Home Craftsmanship & Finishing -->
<div class="reel-card reveal-on-scroll">
<a class="reel-media-wrap" href="https://www.instagram.com/reel/DajVTiBJR9m/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank" title="Watch on Instagram: Dream Home Deserves The Best Interiors">
<img class="reel-thumbnail" src="assets/instagram/reel-dajvtibjr9m.jpg" alt="Your Dream Home Deserves the Best: Quality, Budget & Finishing" loading="lazy" width="360" height="640"/>
<div class="reel-top-bar">
<span class="reel-badge-pill"><i class="fa-brands fa-instagram"></i> Reel</span>
<span class="reel-views-pill"><i class="fa-solid fa-gem"></i> Dream Home</span>
</div>
<div class="reel-center-play">
<i class="fa-solid fa-play"></i>
</div>
<div class="reel-bottom-gradient">
<span class="reel-location"><i class="fa-solid fa-house"></i> Hyderabad &amp; AP</span>
<h3 class="reel-title">Dream Home: Quality, Budget &amp; Flawless Finishing</h3>
<p class="reel-tags">#TeluguReels #HyderabadInteriors #DreamHome</p>
</div>
</a>
<div class="reel-action-footer">
<a class="btn-reel-redirect magnetic-target" href="https://www.instagram.com/reel/DajVTiBJR9m/?utm_source=ig_web_copy_link" rel="noopener noreferrer" target="_blank">
<i class="fa-brands fa-instagram"></i> Watch Reel on Instagram
</a>
</div>
</div>

</div>
</div>
</section>'''

# Replace current section-instagram
html = re.sub(r'<section class="section-instagram" id="instagram">.*?</section>', reels_html, html, flags=re.DOTALL)

# -------------------------------------------------------------
# 2. Remove duplicate brands section from above #process
# -------------------------------------------------------------
# Current structure has <section class="section-services" id="services">...</section> followed by 1 or 2 brands sections, then <section class="section-process" id="process">
# We want: </section>\n\n<section class="section-process" id="process">
services_to_process_pattern = r'(</section>\s*)(?:<section class="section-brands" id="brands">.*?</section>\s*)+(\s*<section class="section-process" id="process">)'
html = re.sub(services_to_process_pattern, r'\1\n\2', html, flags=re.DOTALL)

# -------------------------------------------------------------
# 3. Insert single brands section right UNDER #founder
# -------------------------------------------------------------
# Locate </section> of #founder and <section class="section-curator" id="curator">
founder_to_curator_pattern = r'(<section class="section-founder" id="founder">.*?</section>)\s*(<section class="section-curator" id="curator">)'

brands_section_clean = ibs.section_html.strip()

replacement = r'\1\n\n' + brands_section_clean + r'\n\n\2'
html = re.sub(founder_to_curator_pattern, replacement, html, flags=re.DOTALL)

# -------------------------------------------------------------
# 4. Update Header Navbar to match new section order:
# Spaces -> Style Explorer -> Reels & Videos -> Services -> Process -> Founder -> Partner Brands -> Curate Space
# -------------------------------------------------------------
old_nav = r'<nav class="navbar-apple__nav" id="appleNavLinks">.*?</nav>'
new_nav = '''<nav class="navbar-apple__nav" id="appleNavLinks">
<a class="navbar-apple__link magnetic-target" href="#spaces">Spaces</a>
<a class="navbar-apple__link magnetic-target" href="#transformations">Style Explorer</a>
<a class="navbar-apple__link magnetic-target" href="#instagram">Reels &amp; Videos</a>
<a class="navbar-apple__link magnetic-target" href="#services">Services</a>
<a class="navbar-apple__link magnetic-target" href="#process">Process</a>
<a class="navbar-apple__link magnetic-target" href="#founder">Founder</a>
<a class="navbar-apple__link magnetic-target" href="#brands">Partner Brands</a>
<a class="navbar-apple__link magnetic-target" href="#curator">Curate Space</a>
</nav>'''
html = re.sub(old_nav, new_nav, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
