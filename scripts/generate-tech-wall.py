#!/usr/bin/env python3
"""
Generate 3D Dimensional Skill Cards for GitHub Profile.
Reads structured data from profile/technology-stack.json and generates
XML-validated elevated 3D SVG cards with multi-layer drop shadows,
physical bevel extrusion, top specular highlights, and primary gold indicators.
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
CARDS_DIR = ROOT_DIR / "assets/skills/cards"
GENERATED_DIR = ROOT_DIR / "assets/generated/cards"

CARDS_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

def extract_svg_content(svg_path: Path, fallback_color: str):
    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip XML declaration and comments
    content = re.sub(r"<\?xml.*?\?>", "", content, flags=re.DOTALL)
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)

    # Extract viewBox
    vb_match = re.search(r'viewBox=["\']([^"\']+)["\']', content)
    viewbox = vb_match.group(1) if vb_match else "0 0 32 32"

    # Extract outer fill if any
    fill_match = re.search(r'<svg[^>]*\sfill=["\']([^"\']+)["\']', content)
    outer_fill = fill_match.group(1) if fill_match else ""

    # If outer fill is missing, 'none', or pure black, use fallback brand color
    if not outer_fill or outer_fill.lower() in ("none", "#000", "#000000", "black"):
        outer_fill = fallback_color

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

    return viewbox, inner_content, outer_fill

def generate_cards():
    if not CONFIG_FILE.exists():
        print(f"❌ Configuration not found: {CONFIG_FILE}", file=sys.stderr)
        return False

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        technologies = json.load(f)

    print(f"⚙️ Generating 3D cards for {len(technologies)} technologies...")
    success_count = 0
    errors = []

    for tech in technologies:
        tech_id = tech["id"]
        name = tech.get("shortName") or tech.get("name")
        brand_color = tech.get("color", "#00F2FE")
        is_primary = tech.get("isPrimary", False)
        
        # Locate logo file
        logo_rel = tech.get("logoPath", f"assets/skills/logos/{tech_id}/{tech_id}.svg")
        logo_path = ROOT_DIR / logo_rel

        if not logo_path.exists():
            # Fallback search inside assets/skills/logos
            matches = list((ROOT_DIR / "assets/skills/logos").glob(f"**/{Path(logo_rel).name}"))
            if matches:
                logo_path = matches[0]
            else:
                msg = f"Missing logo file for '{tech_id}': {logo_path}"
                print(f"⚠️ {msg}")
                errors.append(msg)
                continue

        try:
            viewbox, inner_logo, logo_fill = extract_svg_content(logo_path, brand_color)
        except Exception as e:
            msg = f"Error extracting SVG for '{tech_id}': {e}"
            print(f"⚠️ {msg}")
            errors.append(msg)
            continue

        escaped_name = html.escape(name)
        label_color = "#FFEDB3" if is_primary else "#E2E8F0"
        border_opacity = "0.70" if is_primary else "0.42"
        border_width = "1.4" if is_primary else "1.1"
        ambient_glow_opacity = "0.32" if is_primary else "0.20"

        primary_indicator = ""
        if is_primary:
            primary_indicator = """
  <!-- Primary Expertise Gold Indicator with Radiant Halo -->
  <circle cx="87" cy="14" r="5.5" fill="#FFDB70" opacity="0.18"/>
  <circle cx="87" cy="14" r="3.5" fill="#FFDB70" opacity="0.45"/>
  <circle cx="87" cy="14" r="2" fill="#FFDB70"/>"""

        svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="104" height="106" viewBox="0 0 104 106">
  <defs>
    <!-- Top-to-bottom elevated face gradient -->
    <linearGradient id="tileFace_{tech_id}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1B2232"/>
      <stop offset="45%" stop-color="#111622"/>
      <stop offset="100%" stop-color="#080B12"/>
    </linearGradient>
    <!-- Subtle bottom bevel shadow for 3D extrusion -->
    <linearGradient id="bevelShadow_{tech_id}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080B10"/>
      <stop offset="100%" stop-color="#030508"/>
    </linearGradient>
  </defs>

  <!-- 1. Ambient Drop Shadows (Multi-Layer Elevation) -->
  <rect x="8" y="12" width="88" height="88" rx="14" fill="#000000" opacity="0.62"/>
  <rect x="4" y="8" width="96" height="92" rx="13" fill="#000000" opacity="0.40"/>

  <!-- 2. Bottom 3D Extrusion Bevel (Physical Thickness Lip) -->
  <rect x="4" y="4" width="96" height="94" rx="12" fill="url(#bevelShadow_{tech_id})" stroke="{brand_color}" stroke-opacity="0.20" stroke-width="1"/>

  <!-- 3. Primary Elevated Card Face (Lifted 2px up) -->
  <rect x="4" y="2" width="96" height="92" rx="12" fill="url(#tileFace_{tech_id})" stroke="{brand_color}" stroke-opacity="{border_opacity}" stroke-width="{border_width}"/>

  <!-- 4. Inner Glass / Acrylic Chamfer Reflection -->
  <rect x="5.5" y="3.5" width="93" height="89" rx="10.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.08" stroke-width="1"/>

  <!-- 5. Top Specular Glass Highlight -->
  <path d="M 16 3.5 L 88 3.5" stroke="#FFFFFF" stroke-opacity="0.32" stroke-width="1.2" stroke-linecap="round"/>
  <path d="M 6.5 12 L 6.5 38" stroke="#FFFFFF" stroke-opacity="0.10" stroke-width="1" stroke-linecap="round"/>

  <!-- 6. Subtle Ambient Bottom Color Sheen -->
  <ellipse cx="52" cy="90" rx="32" ry="3.5" fill="{brand_color}" opacity="{ambient_glow_opacity}"/>{primary_indicator}

  <!-- 7. Logo Container (with subtle drop shadow & brand glow) -->
  <g transform="translate(34, 18)">
    <circle cx="18" cy="18" r="19" fill="{brand_color}" opacity="0.07"/>
    <ellipse cx="18" cy="34" rx="15" ry="3" fill="#000000" opacity="0.45"/>
    <svg width="36" height="36" viewBox="{viewbox}" fill="{logo_fill}">
      {inner_logo}
    </svg>
  </g>

  <!-- 8. Crisp High-Contrast Typography Label -->
  <text x="52" y="83" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="{label_color}" letter-spacing="-0.1">
    {escaped_name}
  </text>
</svg>
"""

        # Verify XML well-formedness before saving
        try:
            ET.fromstring(svg_template)
        except ET.ParseError as err:
            msg = f"XML syntax error in card '{tech_id}': {err}"
            print(f"❌ {msg}")
            errors.append(msg)
            continue

        # Save to assets/skills/cards and assets/generated/cards
        card_file = CARDS_DIR / f"{tech_id}.svg"
        generated_file = GENERATED_DIR / f"{tech_id}.svg"

        with open(card_file, "w", encoding="utf-8") as out:
            out.write(svg_template)

        with open(generated_file, "w", encoding="utf-8") as out:
            out.write(svg_template)

        success_count += 1

    print(f"✅ Successfully generated {success_count} / {len(technologies)} 3D cards into assets/skills/cards/ and assets/generated/cards/")
    return len(errors) == 0

if __name__ == "__main__":
    success = generate_cards()
    sys.exit(0 if success else 1)
