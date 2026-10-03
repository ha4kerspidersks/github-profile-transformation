#!/usr/bin/env python3
"""
Generate Reference-Faithful Unified Technology Wall for Subhajit Kar's GitHub Profile.
Synthesizes a 1280x780 SVG constellation featuring:
- EXACTLY 56 verified portfolio technologies (8 columns x 7 rows)
- Reference-identical color palette (#0d0e16, #22d3ee, #262a42, #eceef6, #8d93ab)
- Embedded WOFF2 reference fonts (Space Grotesk & JetBrains Mono)
- Unified card grid with zero category headings
- Embedded vector logos with high contrast labels
"""

import json
import os
import re
import html
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))
from shared_svg_fonts import SHARED_FONTS

CONFIG_FILE = ROOT_DIR / "profile/technology-stack.json"
STACK_OUTPUT_SVG = ROOT_DIR / "assets/stack.svg"

def extract_logo_details(svg_path: Path, fallback_color: str):
    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip XML declaration and comments
    content = re.sub(r"<\?xml.*?\?>", "", content, flags=re.DOTALL)
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)

    vb_match = re.search(r'viewBox=["\']([^"\']+)["\']', content)
    viewbox = vb_match.group(1) if vb_match else "0 0 32 32"

    # Extract inner content between <svg ...> and </svg>
    svg_start = content.find("<svg")
    if svg_start != -1:
        svg_open_end = content.find(">", svg_start)
        svg_close = content.rfind("</svg>")
        if svg_open_end != -1 and svg_close != -1:
            inner_content = content[svg_open_end + 1:svg_close].strip()
        else:
            inner_content = content.strip()
    else:
        inner_content = content.strip()

    return viewbox, inner_content

def generate_reference_stack():
    if not CONFIG_FILE.exists():
        print(f"❌ Configuration not found: {CONFIG_FILE}", file=sys.stderr)
        return False

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        technologies = json.load(f)

    expected_count = len(technologies)
    print(f"⚙️ Synthesizing Reference-Faithful Tech Stack ({expected_count} technologies)...")

    # Layout: 8 columns x 7 rows = 56 cards
    cols = 8
    rows = 7
    card_w = 138
    card_h = 74
    gap_x = 14
    gap_y = 14

    grid_total_w = cols * card_w + (cols - 1) * gap_x  # 8*138 + 7*14 = 1104 + 98 = 1202
    grid_total_h = rows * card_h + (rows - 1) * gap_y  # 7*74 + 6*14 = 518 + 84 = 602
    margin_x = (1280 - grid_total_w) // 2  # 39px
    top_y = 128
    svg_total_h = top_y + grid_total_h + 36  # 766px

    cards_xml_parts = []
    symbol_defs = []
    rendered_count = 0

    for idx, tech in enumerate(technologies):
        tech_id = tech["id"]
        name = tech.get("shortName") or tech.get("name")
        brand_color = tech.get("color", "#22d3ee")
        is_primary = tech.get("isPrimary", False) or tech.get("expertiseTier") == "primary"

        logo_rel = tech.get("logoPath", f"assets/skills/logos/{tech_id}/{tech_id}.svg")
        logo_path = ROOT_DIR / logo_rel

        if not logo_path.exists():
            print(f"⚠️ Logo not found: {logo_path}", file=sys.stderr)
            continue

        vb, inner_svg = extract_logo_details(logo_path, brand_color)
        symbol_id = f"sym-{tech_id}"
        symbol_defs.append(f'<symbol id="{symbol_id}" viewBox="{vb}">{inner_svg}</symbol>')

        r = idx // cols
        c = idx % cols
        x = margin_x + c * (card_w + gap_x)
        y = top_y + r * (card_h + gap_y)

        # Reference-identical tile styling
        if is_primary:
            border_stroke = "#22d3ee"
            border_opacity = ".6"
            indicator_xml = f'''
              <circle cx="{x + card_w - 10}" cy="{y + 10}" r="3" fill="#22d3ee"/>
              <circle cx="{x + card_w - 10}" cy="{y + 10}" r="2" fill="#ffffff"/>
            '''
        else:
            border_stroke = "#262a42"
            border_opacity = "1"
            indicator_xml = ""

        # Safe label
        safe_name = html.escape(name)
        font_size = "11.5"
        if len(name) > 13:
            font_size = "10.2"
        if len(name) > 17:
            font_size = "9.2"

        card_xml = f'''
    <!-- Card: {tech_id} -->
    <g class="tile">
      <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="14" fill="#ffffff" fill-opacity=".03" stroke="{border_stroke}" stroke-opacity="{border_opacity}" stroke-width="1.2"/>
      <!-- Top Specular Sheen -->
      <path d="M {x + 14} {y + 1} L {x + card_w - 14} {y + 1}" stroke="#ffffff" stroke-opacity=".15" stroke-width="1" stroke-linecap="round"/>
      <!-- Logo Container -->
      <g transform="translate({x + 10}, {y + 17})">
        <rect x="0" y="0" width="38" height="40" rx="8" fill="#121423" stroke="#262a42" stroke-width="1"/>
        <use href="#{symbol_id}" x="5" y="6" width="28" height="28"/>
      </g>
      <!-- Label -->
      <text x="{x + 54}" y="{y + 42}" class="sg" font-size="{font_size}" fill="#eceef6">{safe_name}</text>
      {indicator_xml}
    </g>'''
        cards_xml_parts.append(card_xml)
        rendered_count += 1

    # MANDATORY VALIDATION: expected == rendered
    if rendered_count != expected_count:
        print(f"❌ Completeness validation failed: expected {expected_count}, rendered {rendered_count}", file=sys.stderr)
        return False

    all_symbols = "\n".join(symbol_defs)
    all_cards = "\n".join(cards_xml_parts)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 {svg_total_h}" width="1280" height="{svg_total_h}" role="img" aria-label="Tech Stack — 56 Verified Technologies"><title>Tech Stack — 56 Verified Technologies</title><desc>Complete 56-technology constellation wall representing all verified enterprise technologies from Subhajit Kar's portfolio.</desc><defs><style>{SHARED_FONTS}
text{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.sg{{font-family:'SG','Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}}
.sgm{{font-family:'SGM','Segoe UI',Helvetica,Arial,sans-serif;font-weight:500}}
.jb{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.jbb{{font-family:'JBMB',ui-monospace,Menlo,Consolas,monospace;font-weight:700}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.fu{{animation:fadeUp .7s cubic-bezier(.2,.8,.2,1) both}}
.fi{{animation:fadeIn .7s ease both}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}
</style>

<linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#141829"/>
  <stop offset="100%" stop-color="#0d0e16"/>
</linearGradient>

<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#a78bfa" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#262a42" stop-opacity=".8"/>
</linearGradient>

<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
  <circle cx="11" cy="11" r=".8" fill="#ffffff" fill-opacity=".05"/>
</pattern>

<!-- Extracted Symbols -->
{all_symbols}
</defs>

<!-- Outer Container Frame matching Reference -->
<rect width="1280" height="{svg_total_h}" rx="24" fill="url(#cardbg)"/>
<rect width="1280" height="{svg_total_h}" rx="24" fill="url(#dots)"/>
<rect x=".75" y=".75" width="1278.5" height="{svg_total_h - 1.5}" rx="23.25" fill="none" stroke="url(#edge)" stroke-width="1.5"/>

<!-- Header matching Reference -->
<g class="fu" style="animation-delay:.1s">
  <text class="jbb" x="40" y="54" font-size="12.5" fill="#22d3ee" letter-spacing="2.2">// TECH STACK</text>
  <text class="sg" x="40" y="94" font-size="29" fill="#eceef6" letter-spacing="-.5">Tools I build with</text>
  <!-- Verified Badge -->
  <g transform="translate(1000,70)">
    <rect x="0" y="-18" width="240" height="28" rx="14" fill="#22d3ee" fill-opacity=".1" stroke="#22d3ee" stroke-opacity=".4"/>
    <circle cx="16" cy="-4" r="4" fill="#22d3ee"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
    <text class="jbb" x="28" y="0" font-size="10" fill="#22d3ee" letter-spacing="1.2">56 VERIFIED ENGINES</text>
  </g>
</g>

<!-- Unified Cards Grid (No Category Headers) -->
<g class="fi" style="animation-delay:.25s">
  {all_cards}
</g>
</svg>'''

    # Validate XML
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as err:
        print(f"❌ XML error in generated stack SVG: {err}", file=sys.stderr)
        return False

    STACK_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    with open(STACK_OUTPUT_SVG, "w", encoding="utf-8") as out:
        out.write(svg_content)

    print(f"✅ Generated Reference-Faithful stack.svg ({len(svg_content) / 1024:.1f} KB)")
    print(f"   Rendered: {rendered_count} / Expected: {expected_count} (100% COMPLETE)")
    return True

if __name__ == "__main__":
    success = generate_reference_stack()
    sys.exit(0 if success else 1)
