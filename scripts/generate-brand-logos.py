#!/usr/bin/env python3
"""
Generate authentic, high-quality vector SVG logos for Trilok's partner brands:
- Plywood: Century Ply, Greenply, Duro Ply, Austin Ply, Sylvan Ply
- Hardware: Hafele, Hettich, Ebco, Nimmi, Ozone, Blum, Godrej, Sleek
- Construction Steel: Tata Steel, JSW Steel, Jindal Steel, Kamdhenu Steel
- Paints: Asian Paints, Berger Paints, Nerolac, Dulux
- Plumbing: Astral Pipes, Ashirvad Pipes
- Electrical & Wiring: Goldmedal, Legrand, Havells, Anchor by Panasonic, Polycab, Finolex
"""

import os

os.makedirs('assets/brands', exist_ok=True)

logos = {
    # ---------------- PLYWOOD ----------------
    "centuryply.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <defs>
    <linearGradient id="cpGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E31B23"/>
      <stop offset="100%" stop-color="#C01018"/>
    </linearGradient>
  </defs>
  <!-- Red emblem mark -->
  <path d="M18 18 L38 18 L48 35 L38 52 L18 52 L8 35 Z" fill="url(#cpGrad)"/>
  <path d="M23 25 L33 25 L39 35 L33 45 L23 45 L17 35 Z" fill="#FFFFFF"/>
  <path d="M28 29 L32 35 L28 41 Z" fill="#E31B23"/>
  <!-- Typography -->
  <text x="56" y="38" font-family="'Montserrat', 'Arial Black', sans-serif" font-weight="900" font-size="20" fill="#FFFFFF" letter-spacing="1.5">CENTURY</text>
  <rect x="56" y="44" width="98" height="3" fill="#E31B23"/>
  <text x="160" y="38" font-family="'Montserrat', 'Arial Black', sans-serif" font-weight="900" font-size="20" fill="#E31B23" letter-spacing="2">PLY</text>
  <text x="56" y="56" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E5CD95" letter-spacing="3.5">PROMISE OF QUALITY</text>
</svg>''',

    "greenply.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <defs>
    <linearGradient id="gpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00A859"/>
      <stop offset="100%" stop-color="#006837"/>
    </linearGradient>
  </defs>
  <!-- Iconic Triple Leaf Eco Mark -->
  <g transform="translate(10, 15)">
    <circle cx="20" cy="20" r="18" fill="url(#gpGrad)" opacity="0.2"/>
    <path d="M20 7 C27 12 30 20 20 28 C10 20 13 12 20 7 Z" fill="#00A859"/>
    <path d="M20 28 C28 28 34 35 24 38 C18 40 16 33 20 28 Z" fill="#39B54A"/>
    <path d="M20 28 C12 28 6 35 16 38 C22 40 24 33 20 28 Z" fill="#8DC63F"/>
  </g>
  <!-- Typography -->
  <text x="58" y="40" font-family="'Montserrat', 'Arial Black', sans-serif" font-weight="900" font-size="22" fill="#FFFFFF" letter-spacing="1">GREEN</text>
  <text x="145" y="40" font-family="'Montserrat', 'Arial Black', sans-serif" font-weight="900" font-size="22" fill="#00A859" letter-spacing="1">PLY</text>
  <text x="58" y="54" font-family="'Manrope', sans-serif" font-weight="700" font-size="7.5" fill="#A0AEC0" letter-spacing="3">ZERO EMISSION PLYWOOD</text>
</svg>''',

    "duroply.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Duro Ply Badge -->
  <rect x="12" y="15" width="40" height="40" rx="8" fill="#0054A6"/>
  <text x="32" y="42" font-family="'Arial Black', sans-serif" font-weight="900" font-size="24" fill="#FFFFFF" text-anchor="middle">D</text>
  <circle cx="42" cy="23" r="5" fill="#EE2A24"/>
  <!-- Typography -->
  <text x="60" y="38" font-family="'Montserrat', sans-serif" font-weight="900" font-size="22" fill="#FFFFFF" letter-spacing="2">DURO</text>
  <text x="135" y="38" font-family="'Montserrat', sans-serif" font-weight="900" font-size="22" fill="#EE2A24" letter-spacing="2">PLY</text>
  <text x="60" y="54" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#E5CD95" letter-spacing="3">SINCE 1957 • PREMIUM PLY</text>
</svg>''',

    "austinply.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Austin Crown / Shield -->
  <g transform="translate(14, 16)">
    <path d="M0 6 L10 0 L20 6 L30 0 L40 6 L36 32 L20 38 L4 32 Z" fill="#E31E24"/>
    <text x="20" y="27" font-family="'Arial Black', sans-serif" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle">A</text>
  </g>
  <!-- Typography -->
  <text x="64" y="36" font-family="'Montserrat', sans-serif" font-weight="900" font-size="19" fill="#FFFFFF" letter-spacing="2">AUSTIN</text>
  <text x="145" y="36" font-family="'Montserrat', sans-serif" font-weight="800" font-size="19" fill="#E31E24" letter-spacing="2">PLY</text>
  <text x="64" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#A0AEC0" letter-spacing="3">ADVANCED BS-1088 MARINE</text>
</svg>''',

    "sylvanply.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Sylvan Tree Emblem -->
  <g transform="translate(12, 14)">
    <circle cx="21" cy="21" r="19" fill="#1C3F24" stroke="#E5CD95" stroke-width="1.5"/>
    <path d="M21 9 L15 19 L19 19 L13 29 L29 29 L23 19 L27 19 Z" fill="#E5CD95"/>
    <rect x="19.5" y="29" width="3" height="6" fill="#E5CD95"/>
  </g>
  <!-- Typography -->
  <text x="62" y="36" font-family="'Playfair Display', serif" font-weight="700" font-size="20" fill="#FFFFFF" letter-spacing="2">SYLVAN</text>
  <text x="156" y="36" font-family="'Montserrat', sans-serif" font-weight="700" font-size="18" fill="#E5CD95" letter-spacing="2">PLY</text>
  <text x="62" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#9DA6B8" letter-spacing="3">SIGNATURE TIMBER BOARDS</text>
</svg>''',

    # ---------------- HARDWARE ----------------
    "hafele.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Häfele Signature German Red Logo -->
  <g transform="translate(14, 18)">
    <rect x="0" y="4" width="30" height="26" rx="4" fill="#D4002A"/>
    <circle cx="9" cy="12" r="2" fill="#FFF"/>
    <circle cx="21" cy="12" r="2" fill="#FFF"/>
    <path d="M8 22 L22 22" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  <text x="52" y="38" font-family="'Helvetica Neue', 'Arial', sans-serif" font-weight="900" font-size="23" fill="#D4002A" letter-spacing="2">HÄFELE</text>
  <text x="54" y="54" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#A0AEC0" letter-spacing="3.5">GERMAN FITTINGS &amp; HARDWARE</text>
</svg>''',

    "hettich.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Hettich Blue Logo with Iconic Hinge Curves -->
  <g transform="translate(10, 14)">
    <path d="M8 6 C16 6 24 14 24 22 C24 30 16 38 8 38 C14 34 18 28 18 22 C18 16 14 10 8 6 Z" fill="#005BA9"/>
    <path d="M14 10 C20 10 26 16 26 22 C26 28 20 34 14 34 C18 31 21 27 21 22 C21 17 18 13 14 10 Z" fill="#E5CD95"/>
  </g>
  <text x="46" y="40" font-family="'Georgia', serif" font-weight="700" font-size="25" fill="#FFFFFF" letter-spacing="0.5">Hettich</text>
  <text x="48" y="55" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E5CD95" letter-spacing="2.5">TECHNIK FÜR MÖBEL</text>
</svg>''',

    "ebco.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- ebco Logo -->
  <g transform="translate(14, 18)">
    <circle cx="16" cy="16" r="15" fill="#005BAA"/>
    <path d="M10 16 L22 16 M16 10 L16 22" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  <text x="52" y="39" font-family="'Arial Black', sans-serif" font-weight="900" font-size="24" fill="#005BAA" letter-spacing="1">ebco</text>
  <text x="54" y="53" font-family="'Manrope', sans-serif" font-weight="700" font-size="8" fill="#FFF" letter-spacing="3.5">LIVSMART FURNITURE HARDWARE</text>
</svg>''',

    "nimmi.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(16, 16)">
    <rect x="0" y="2" width="28" height="28" rx="6" fill="#F4511E"/>
    <path d="M8 20 L14 10 L20 20" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  </g>
  <text x="52" y="38" font-family="'Montserrat', sans-serif" font-weight="800" font-size="22" fill="#FFFFFF" letter-spacing="2">nimmi</text>
  <text x="54" y="53" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#F4511E" letter-spacing="2.5">ARCHITECTURAL HARDWARE</text>
</svg>''',

    "ozone.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(16, 16)">
    <circle cx="16" cy="16" r="14" fill="none" stroke="#00A3E0" stroke-width="3"/>
    <circle cx="16" cy="16" r="6" fill="#00A3E0"/>
  </g>
  <text x="54" y="39" font-family="'Montserrat', sans-serif" font-weight="800" font-size="23" fill="#FFFFFF" letter-spacing="2.5">OZONE</text>
  <text x="56" y="53" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#00A3E0" letter-spacing="3">ARCHITECTURAL GLASS HARDWARE</text>
</svg>''',

    "blum.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Blum Signature Orange Logo -->
  <rect x="14" y="15" width="40" height="38" rx="4" fill="#EA592A"/>
  <text x="34" y="41" font-family="'Arial Black', sans-serif" font-weight="900" font-size="22" fill="#FFFFFF" text-anchor="middle">b</text>
  <text x="62" y="40" font-family="'Arial Black', sans-serif" font-weight="900" font-size="26" fill="#EA592A" letter-spacing="1">blum</text>
  <text x="64" y="54" font-family="'Manrope', sans-serif" font-weight="700" font-size="7.5" fill="#A0AEC0" letter-spacing="3">PERFECTING MOTION • AUSTRIA</text>
</svg>''',

    "godrej.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Godrej Signature Cursive Mark -->
  <g transform="translate(16, 15)">
    <path d="M8 8 C18 0 26 12 18 20 C12 26 2 28 6 36 C10 40 22 36 28 26" fill="none" stroke="#D11242" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="56" y="38" font-family="'Great Vibes', 'Brush Script MT', cursive" font-size="32" fill="#FFFFFF">Godrej</text>
  <text x="58" y="53" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#D11242" letter-spacing="2">LOCKS &amp; ARCHITECTURAL HARDWARE</text>
</svg>''',

    "sleek.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(14, 18)">
    <circle cx="16" cy="16" r="14" fill="#E31E24"/>
    <path d="M10 16 L14 20 L22 12" stroke="#FFF" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  </g>
  <text x="52" y="37" font-family="'Montserrat', sans-serif" font-weight="800" font-size="21" fill="#FFFFFF" letter-spacing="2">SLEEK</text>
  <text x="122" y="37" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#E31E24">by asianpaints</text>
  <text x="52" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#A0AEC0" letter-spacing="2.5">SPECIALIZED MODULAR KITCHENS</text>
</svg>''',

    # ---------------- STEEL (CONSTRUCTION) ----------------
    "tatasteel.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Tata Cobalt Blue Logo -->
  <g transform="translate(14, 15)">
    <circle cx="18" cy="18" r="17" fill="#005696"/>
    <path d="M9 13 L27 13 M18 13 L18 27" stroke="#FFF" stroke-width="3.5" stroke-linecap="round"/>
  </g>
  <text x="56" y="35" font-family="'Montserrat', 'Arial Black', sans-serif" font-weight="900" font-size="18" fill="#005696" letter-spacing="2">TATA</text>
  <text x="114" y="35" font-family="'Montserrat', sans-serif" font-weight="800" font-size="18" fill="#FFFFFF" letter-spacing="2">STEEL</text>
  <text x="56" y="52" font-family="'Manrope', sans-serif" font-weight="700" font-size="8" fill="#E5CD95" letter-spacing="3">TISCON 550D SUPER DUCTILE TMT</text>
</svg>''',

    "jswsteel.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(14, 18)">
    <path d="M0 0 L18 0 L24 16 L14 30 L0 30 Z" fill="#00508F"/>
    <path d="M16 0 L32 0 L22 30 L10 30 Z" fill="#ED1C24"/>
  </g>
  <text x="54" y="36" font-family="'Arial Black', sans-serif" font-weight="900" font-size="22" font-style="italic" fill="#00508F" letter-spacing="1">JSW</text>
  <text x="112" y="36" font-family="'Montserrat', sans-serif" font-weight="800" font-size="19" fill="#FFFFFF" letter-spacing="2">STEEL</text>
  <text x="54" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#ED1C24" letter-spacing="2.5">NEOSTEEL 550D EARTHQUAKE RESISTANT</text>
</svg>''',

    "jindalsteel.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(14, 16)">
    <circle cx="18" cy="18" r="16" fill="#003865" stroke="#E5CD95" stroke-width="1.5"/>
    <text x="18" y="24" font-family="'Arial Black', sans-serif" font-weight="900" font-size="15" fill="#FFFFFF" text-anchor="middle">J</text>
  </g>
  <text x="56" y="36" font-family="'Montserrat', sans-serif" font-weight="900" font-size="19" fill="#FFFFFF" letter-spacing="1.5">JINDAL</text>
  <text x="142" y="36" font-family="'Montserrat', sans-serif" font-weight="700" font-size="19" fill="#00A3E0" letter-spacing="1.5">STEEL</text>
  <text x="56" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#A0AEC0" letter-spacing="3">PANTHER 550D HIGH TENSILE TMT</text>
</svg>''',

    "kamdhenusteel.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(12, 14)">
    <polygon points="18,2 34,10 34,28 18,36 2,28 2,10" fill="#D32F2F"/>
    <polygon points="18,6 30,12 30,26 18,32 6,26 6,12" fill="#FFA000"/>
    <text x="18" y="24" font-family="'Arial Black', sans-serif" font-size="13" font-weight="900" fill="#FFF" text-anchor="middle">K</text>
  </g>
  <text x="54" y="36" font-family="'Montserrat', sans-serif" font-weight="900" font-size="18" fill="#FFFFFF" letter-spacing="1.5">KAMDHENU</text>
  <text x="54" y="52" font-family="'Manrope', sans-serif" font-weight="700" font-size="8" fill="#FFA000" letter-spacing="3">PAS 10000 WORLD-CLASS STEEL</text>
</svg>''',

    # ---------------- PAINTS ----------------
    "asianpaints.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Asian Paints Iconic Multi-color Ribbon Symbol -->
  <g transform="translate(14, 14)">
    <path d="M16 4 C24 4 30 10 30 18 C30 26 22 34 14 34 C6 34 2 28 2 20 Z" fill="#EE3124"/>
    <path d="M16 10 C22 10 26 14 26 19 C26 24 20 28 14 28 C9 28 7 24 7 19 Z" fill="#FFC107"/>
    <circle cx="16" cy="19" r="4" fill="#00A3E0"/>
  </g>
  <text x="54" y="38" font-family="'Manrope', 'Helvetica Neue', sans-serif" font-weight="800" font-size="21" fill="#FFFFFF" letter-spacing="0.5">asian<tspan fill="#EE3124">paints</tspan></text>
  <text x="56" y="53" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E5CD95" letter-spacing="2.5">ROYALE LUXURY EMULSIONS</text>
</svg>''',

    "berger.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Berger Heraldic Crest -->
  <g transform="translate(14, 15)">
    <path d="M2 4 L34 4 L34 22 C34 32 18 36 18 36 C18 36 2 32 2 22 Z" fill="#D71920"/>
    <path d="M6 10 L14 10 L14 14 L18 10 L22 14 L22 10 L30 10" stroke="#FFF" stroke-width="2" fill="none"/>
    <text x="18" y="27" font-family="'Georgia', serif" font-weight="700" font-size="12" fill="#FFF" text-anchor="middle">B</text>
  </g>
  <text x="56" y="38" font-family="'Georgia', serif" font-weight="700" font-size="24" fill="#FFFFFF" letter-spacing="1">Berger</text>
  <text x="58" y="53" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#D71920" letter-spacing="2.5">PAINT YOUR IMAGINATION</text>
</svg>''',

    "nerolac.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(14, 16)">
    <circle cx="8" cy="18" r="6" fill="#EE3124"/>
    <circle cx="20" cy="10" r="6" fill="#00A3E0"/>
    <circle cx="24" cy="24" r="6" fill="#FFC107"/>
  </g>
  <text x="54" y="37" font-family="'Montserrat', sans-serif" font-weight="900" font-size="21" fill="#FFFFFF" letter-spacing="1.5">NEROLAC</text>
  <text x="56" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#00A3E0" letter-spacing="2.5">BEAUTY THAT PROTECTS</text>
</svg>''',

    "dulux.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Dulux Paint Flourish Wave -->
  <g transform="translate(10, 16)">
    <path d="M4 28 C12 12 24 6 36 12 C24 16 16 26 10 32 Z" fill="#00A859"/>
    <path d="M12 22 C20 10 30 6 40 10 C30 16 22 24 16 30 Z" fill="#FFC107"/>
    <path d="M20 18 C28 8 36 6 44 8 C36 14 28 22 22 28 Z" fill="#005BAA"/>
  </g>
  <text x="56" y="37" font-family="'Georgia', serif" font-weight="700" font-size="23" fill="#FFFFFF" letter-spacing="0.5">Dulux</text>
  <text x="58" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E5CD95" letter-spacing="2.5">LET'S COLOUR • VELVET TOUCH</text>
</svg>''',

    # ---------------- PLUMBING ----------------
    "astralpipes.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(14, 16)">
    <circle cx="17" cy="17" r="16" fill="#E31E24"/>
    <path d="M8 17 L26 17 M17 8 L17 26" stroke="#FFF" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="54" y="36" font-family="'Montserrat', sans-serif" font-weight="900" font-size="20" fill="#E31E24" letter-spacing="2">ASTRAL</text>
  <text x="145" y="36" font-family="'Montserrat', sans-serif" font-weight="700" font-size="20" fill="#FFFFFF" letter-spacing="2">PIPES</text>
  <text x="54" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#A0AEC0" letter-spacing="2.5">CPVC PRO &amp; DRAINMASTER LEAD-FREE</text>
</svg>''',

    "ashirvadpipes.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <g transform="translate(14, 16)">
    <rect x="0" y="2" width="30" height="30" rx="6" fill="#E30613"/>
    <circle cx="15" cy="17" r="6" fill="#FFF"/>
  </g>
  <text x="52" y="36" font-family="'Montserrat', sans-serif" font-weight="800" font-size="19" fill="#FFFFFF" letter-spacing="1">ashirvad</text>
  <text x="144" y="36" font-family="'Montserrat', sans-serif" font-weight="700" font-size="19" fill="#E30613" letter-spacing="1">PIPES</text>
  <text x="52" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E5CD95" letter-spacing="2.5">BY ALIAXIS • SILENT SWR &amp; FLOWGUARD</text>
</svg>''',

    # ---------------- ELECTRICAL & WIRING ----------------
    "goldmedal.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Goldmedal Electricals -->
  <g transform="translate(14, 15)">
    <circle cx="18" cy="18" r="16" fill="#E31B23"/>
    <circle cx="18" cy="18" r="10" fill="none" stroke="#FFF" stroke-width="2"/>
    <circle cx="18" cy="18" r="4" fill="#FFF"/>
  </g>
  <text x="56" y="36" font-family="'Montserrat', sans-serif" font-weight="900" font-size="18" fill="#FFFFFF" letter-spacing="1.5">GOLDMEDAL</text>
  <text x="56" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="8" fill="#E31B23" letter-spacing="2.5">MODULAR SWITCHES &amp; AUTOMATION</text>
</svg>''',

    "legrand.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Iconic Legrand Red Square Mark -->
  <rect x="14" y="16" width="34" height="34" rx="2" fill="#E2001A"/>
  <path d="M22 22 L22 42 M22 42 L34 42" stroke="#FFF" stroke-width="3" stroke-linecap="square"/>
  <text x="56" y="38" font-family="'Helvetica Neue', 'Arial', sans-serif" font-weight="700" font-size="22" fill="#FFFFFF" letter-spacing="1">legrand</text>
  <text x="58" y="53" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E2001A" letter-spacing="3">GLOBAL ELECTRICAL SPECIALIST</text>
</svg>''',

    "havells.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Havells Red Logo -->
  <g transform="translate(12, 16)">
    <polygon points="18,0 36,16 18,32 0,16" fill="#E30613"/>
    <circle cx="18" cy="16" r="5" fill="#FFF"/>
  </g>
  <text x="56" y="37" font-family="'Montserrat', sans-serif" font-weight="900" font-size="20" fill="#E30613" letter-spacing="2">HAVELLS</text>
  <text x="56" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#FFFFFF" letter-spacing="2.5">WIRES, SWITCHES &amp; SMART LIVING</text>
</svg>''',

    "anchor.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Anchor by Panasonic -->
  <g transform="translate(14, 15)">
    <circle cx="17" cy="17" r="16" fill="#E30613"/>
    <!-- Anchor symbol -->
    <circle cx="17" cy="10" r="2.5" fill="#FFF"/>
    <path d="M17 12 L17 24 M11 15 L23 15 M11 20 C11 25 23 25 23 20" stroke="#FFF" stroke-width="2" fill="none" stroke-linecap="round"/>
  </g>
  <text x="54" y="34" font-family="'Montserrat', sans-serif" font-weight="900" font-size="18" fill="#FFFFFF" letter-spacing="1.5">ANCHOR</text>
  <text x="54" y="47" font-family="'Manrope', sans-serif" font-weight="600" font-size="8.5" fill="#00457C" letter-spacing="1">by Panasonic</text>
  <text x="54" y="58" font-family="'Manrope', sans-serif" font-weight="500" font-size="6.5" fill="#A0AEC0" letter-spacing="2">ROMA SWITCHES &amp; ADVANCE WIRING</text>
</svg>''',

    "polycab.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Polycab Red & Green Logo -->
  <g transform="translate(14, 16)">
    <circle cx="16" cy="16" r="15" fill="#E31E24"/>
    <path d="M16 6 C22 10 24 16 16 26 C12 20 10 14 16 6 Z" fill="#008848"/>
  </g>
  <text x="52" y="37" font-family="'Montserrat', 'Arial Black', sans-serif" font-weight="900" font-size="20" fill="#FFFFFF" letter-spacing="1.5">POLYCAB</text>
  <text x="52" y="52" font-family="'Manrope', sans-serif" font-weight="600" font-size="7.5" fill="#E31E24" letter-spacing="2.5">CONNECTION ZINDAGI KA • WIRES &amp; CABLES</text>
</svg>''',

    "finolex.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 70" width="240" height="70">
  <!-- Finolex Red Oval Logo -->
  <g transform="translate(12, 16)">
    <ellipse cx="18" cy="16" rx="17" ry="14" fill="#ED1C24"/>
    <path d="M10 16 L26 16 M14 11 L22 21" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  <text x="54" y="37" font-family="'Arial Black', sans-serif" font-weight="900" font-size="20" fill="#ED1C24" letter-spacing="1">Finolex</text>
  <text x="54" y="52" font-family="'Manrope', sans-serif" font-weight="700" font-size="7.5" fill="#FFFFFF" letter-spacing="3">FLAME RETARDANT WIRING CABLES</text>
</svg>'''
}

for filename, content in logos.items():
    path = os.path.join('assets/brands', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created: {path}")

print(f"Total logos generated: {len(logos)}")
