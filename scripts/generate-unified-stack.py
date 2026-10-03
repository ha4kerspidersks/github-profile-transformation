#!/usr/bin/env python3
"""
Generate Unified Technology Wall (Master V2) for Subhajit Kar's GitHub Profile.
Synthesizes a 1280x750 widescreen SVG constellation featuring:
- ALL 56 verified technologies from Subhajit Kar's portfolio
- Unified 8-column x 7-row constellation grid (NO category headers)
- Dimensional cards with specular highlights, multi-layer drop shadows, and brand glow
- Exactly 10 Primary Expertise skills highlighted with glowing gold micro-indicators (●)
- Embedded SVG logos scaled into crisp 28x28 icon viewports
"""

import json
import os
import re
import html
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
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

def generate_unified_stack():
    if not CONFIG_FILE.exists():
        print(f"❌ Configuration not found: {CONFIG_FILE}", file=sys.stderr)
        return False

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        technologies = json.load(f)

    print(f"⚙️ Synthesizing Unified 56-Technology Constellation Wall (Master V2)...")

    # Layout parameters: 8 columns x 7 rows = 56 cards
    cols = 8
    rows = 7
    card_w = 136
    card_h = 74
    gap_x = 16
    gap_y = 16

    grid_total_w = cols * card_w + (cols - 1) * gap_x  # 8*136 + 7*16 = 1088 + 112 = 1200
    grid_total_h = rows * card_h + (rows - 1) * gap_y  # 7*74 + 6*16 = 518 + 96 = 614
    margin_x = (1280 - grid_total_w) // 2  # 40px
    top_y = 90
    svg_total_h = top_y + grid_total_h + 40  # 744px

    cards_xml_parts = []
    symbol_defs = []

    for idx, tech in enumerate(technologies):
        tech_id = tech["id"]
        name = tech.get("shortName") or tech.get("name")
        brand_color = tech.get("color", "#00F2FE")
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

        # Primary vs Supporting styling
        if is_primary:
            border_color = "#FFDB70"
            border_opacity = "0.75"
            border_width = "1.2"
            bg_grad = "url(#primaryCardGrad)"
            glow_attr = 'filter="url(#primaryGlow)"'
            indicator_xml = f'''
              <circle cx="{x + card_w - 12}" cy="{y + 12}" r="3.5" fill="#FFDB70" filter="url(#goldDotGlow)"/>
              <circle cx="{x + card_w - 12}" cy="{y + 12}" r="1.5" fill="#FFFFFF"/>
            '''
        else:
            border_color = brand_color
            border_opacity = "0.35"
            border_width = "1"
            bg_grad = "url(#standardCardGrad)"
            glow_attr = ""
            indicator_xml = ""

        # Safe label
        safe_name = html.escape(name)
        # If name is long, split or adjust font size
        font_size = "11.5"
        if len(name) > 14:
            font_size = "10.2"
        if len(name) > 18:
            font_size = "9.2"

        card_xml = f'''
    <!-- Card: {tech_id} -->
    <g transform="translate(0, 0)">
      <!-- Drop Shadow -->
      <rect x="{x + 2}" y="{y + 4}" width="{card_w}" height="{card_h}" rx="12" fill="#020408" fill-opacity="0.85"/>
      <!-- Outer Card Container -->
      <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="12" fill="{bg_grad}" stroke="{border_color}" stroke-opacity="{border_opacity}" stroke-width="{border_width}" {glow_attr}/>
      <!-- Specular Top Highlight -->
      <path d="M {x + 12} {y + 1} L {x + card_w - 12} {y + 1}" stroke="#FFFFFF" stroke-opacity="0.18" stroke-width="1.2" stroke-linecap="round"/>
      <!-- Icon Container -->
      <g transform="translate({x + 10}, {y + 16})">
        <rect x="0" y="0" width="38" height="42" rx="8" fill="#060C18" stroke="{brand_color}" stroke-opacity="0.35" stroke-width="0.8"/>
        <use href="#{symbol_id}" x="5" y="7" width="28" height="28"/>
      </g>
      <!-- Label -->
      <text x="{x + 54}" y="{y + 41}" class="f-sans" font-size="{font_size}" font-weight="700" fill="#F1F5F9" letter-spacing="0.1">{safe_name}</text>
      {indicator_xml}
    </g>'''
        cards_xml_parts.append(card_xml)

    all_symbols = "\n".join(symbol_defs)
    all_cards = "\n".join(cards_xml_parts)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 {svg_total_h}" width="100%" height="auto" role="img" aria-label="Complete Technology Constellation — 56 Verified Technologies">
  <title>Complete Technology Constellation — 56 Verified Technologies</title>
  <desc>Unified visual technology wall showcasing all 56 verified enterprise technologies from Subhajit Kar's portfolio across IAM/IGA, Cloud, AI, DevOps, Security, Programming, and Enterprise architecture.</desc>
  <defs>
    <!-- Typography -->
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&amp;family=Space+Grotesk:wght@600;700;800&amp;family=Inter:wght@500;600;700&amp;display=swap');

      .f-mono {{ font-family: 'JetBrains Mono', monospace; }}
      .f-display {{ font-family: 'Space Grotesk', -apple-system, sans-serif; }}
      .f-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      @keyframes ambientConstellation {{
        0%, 100% {{ opacity: 0.25; }}
        50% {{ opacity: 0.65; }}
      }}
      .anim-constellation {{ animation: ambientConstellation 6s ease-in-out infinite; }}
    </style>

    <!-- Gradients -->
    <linearGradient id="wallBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#080E1A"/>
      <stop offset="100%" stop-color="#04060D"/>
    </linearGradient>

    <linearGradient id="standardCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0D1628"/>
      <stop offset="100%" stop-color="#070C16"/>
    </linearGradient>

    <linearGradient id="primaryCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#121D33"/>
      <stop offset="100%" stop-color="#080E1C"/>
    </linearGradient>

    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="60%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#FFDB70"/>
    </linearGradient>

    <radialGradient id="gridGlow1" cx="30%" cy="20%" r="50%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="gridGlow2" cx="80%" cy="70%" r="50%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <!-- Pattern -->
    <pattern id="constellationGrid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#162032" stroke-width="0.6" stroke-opacity="0.5"/>
    </pattern>

    <!-- Filters -->
    <filter id="primaryGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="goldDotGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Symbols -->
    {all_symbols}
  </defs>

  <!-- Background Base -->
  <rect width="1280" height="{svg_total_h}" fill="url(#wallBg)"/>
  <rect width="1280" height="{svg_total_h}" fill="url(#constellationGrid)"/>
  <rect width="1280" height="{svg_total_h}" fill="url(#gridGlow1)"/>
  <rect width="1280" height="{svg_total_h}" fill="url(#gridGlow2)"/>

  <!-- Outer Frame -->
  <rect x="16" y="16" width="1248" height="{svg_total_h - 32}" rx="18" fill="none" stroke="#1E293B" stroke-width="1.2"/>
  <rect x="22" y="22" width="1236" height="{svg_total_h - 44}" rx="14" fill="none" stroke="#00F2FE" stroke-opacity="0.12" stroke-width="0.8"/>

  <!-- Top Constellation Header Bar -->
  <g transform="translate(40, 52)">
    <!-- Header Title -->
    <text x="0" y="14" class="f-mono" font-size="12" font-weight="700" fill="#00F2FE" letter-spacing="2.2">// UNIFIED TECHNOLOGY CONSTELLATION</text>
    <text x="360" y="14" class="f-display" font-size="14" font-weight="700" fill="#94A3B8" letter-spacing="0.5">· 56 Verified Production Tools &amp; Engines</text>

    <!-- Primary Legend -->
    <g transform="translate(930, -4)">
      <rect x="0" y="0" width="270" height="28" rx="14" fill="#0A1324" stroke="#FFDB70" stroke-opacity="0.35" stroke-width="1"/>
      <circle cx="16" cy="14" r="4.5" fill="#FFDB70" filter="url(#goldDotGlow)"/>
      <circle cx="16" cy="14" r="2" fill="#FFFFFF"/>
      <text x="28" y="18" class="f-mono" font-size="10" font-weight="700" fill="#FFDB70" letter-spacing="0.8">10 PRIMARY EXPERTISE</text>
      <text x="175" y="18" class="f-mono" font-size="10" fill="#94A3B8">· 46 SUPPORT</text>
    </g>
  </g>

  <!-- Constellation Cards Grid -->
  <g>
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

    print(f"✅ Generated Unified 56-Technology Constellation Wall at {STACK_OUTPUT_SVG}")
    print(f"   Size: {os.path.getsize(STACK_OUTPUT_SVG) / 1024:.1f} KB")
    return True

if __name__ == "__main__":
    success = generate_unified_stack()
    sys.exit(0 if success else 1)
