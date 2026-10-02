#!/usr/bin/env python3
"""
Generate the Wide Horizontal Technical Hero Banner SVG for GitHub Profile.
Consumes configuration from profile/profile-data.json and renders
a 1200x340 vector SVG banner with:
- Dark technical background gradient
- Precision technical coordinate grid & corner brackets
- Status chip indicator
- Clean typography for identity, role, and specialization
- Monospace focus line
- Capability badges
- Right-hand enterprise cybersecurity / IAM visual network
- Valid XML syntax checking
"""

import json
import html
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT_DIR / "profile/profile-data.json"
HERO_SVG = ROOT_DIR / "assets/hero-banner.svg"
HERO_DIR_SVG = ROOT_DIR / "assets/hero/hero-banner.svg"

def generate_hero():
    if not CONFIG_FILE.exists():
        print(f"❌ Configuration not found: {CONFIG_FILE}", file=sys.stderr)
        return False

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    personal = data.get("personal", {})
    name = html.escape(personal.get("name", "SUBHAJIT KAR"))
    role = html.escape(personal.get("role", "Senior IAM Assistant Manager"))
    specialization = html.escape(personal.get("specialization", "Enterprise Identity Governance & Large-Scale Data Analytics"))
    status = personal.get("statusIndicator", {})
    left_status = html.escape(status.get("leftText", "DELOITTE CYBER & STRATEGIC RISK"))
    right_status = html.escape(status.get("rightText", "ENTERPRISE IGA"))
    focus_line = html.escape(personal.get("focusLine", "Saviynt IGA · Identity Recon (300K+) · JML Workflows · AI Dev Team"))

    badges = data.get("badges", [])
    badge_elements = []
    x_offset = 0
    for b in badges:
        label = html.escape(b["label"])
        color = b.get("color", "#00F2FE")
        border = b.get("borderColor", color)
        # Approximate width based on character length
        badge_w = max(100, len(label) * 8 + 36)
        
        badge_svg = f"""    <!-- Badge: {label} -->
    <g transform="translate({x_offset}, 0)">
      <rect width="{badge_w}" height="28" rx="6" fill="#0E1726" stroke="{border}" stroke-width="1" stroke-opacity="0.45"/>
      <circle cx="16" cy="14" r="3.5" fill="{color}"/>
      <text x="28" y="18" class="font-mono pill-label" fill="{color}">{label}</text>
    </g>"""
        badge_elements.append(badge_svg)
        x_offset += badge_w + 12

    badges_markup = "\n".join(badge_elements)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C15"/>
      <stop offset="50%" stop-color="#0B111E"/>
      <stop offset="100%" stop-color="#060911"/>
    </linearGradient>

    <radialGradient id="cyanGlow" cx="25%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.12"/>
      <stop offset="50%" stop-color="#00F2FE" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0.0"/>
    </radialGradient>

    <radialGradient id="emeraldGlow" cx="80%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.10"/>
      <stop offset="45%" stop-color="#00F2FE" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.0"/>
    </radialGradient>

    <linearGradient id="bannerBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.6"/>
      <stop offset="35%" stop-color="#1E293B" stop-opacity="0.4"/>
      <stop offset="70%" stop-color="#10B981" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0.3"/>
    </linearGradient>

    <linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#10B981" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.0"/>
    </linearGradient>

    <linearGradient id="coreGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="techGrid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#1E293B" stroke-width="0.75" stroke-opacity="0.35"/>
      <circle cx="30" cy="0" r="1" fill="#00F2FE" fill-opacity="0.25"/>
    </pattern>

    <!-- Filter for subtle outer glow -->
    <filter id="subtleGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .font-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; }}
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    .title-name {{ font-size: 38px; font-weight: 800; fill: #FFFFFF; letter-spacing: 1.8px; }}
    .role-title {{ font-size: 19px; font-weight: 600; fill: #00F2FE; letter-spacing: 0.5px; }}
    .sub-role {{ font-size: 14px; font-weight: 400; fill: #94A3B8; letter-spacing: 0.3px; }}
    .pill-label {{ font-size: 11px; font-weight: 600; letter-spacing: 0.8px; }}
  </style>

  <!-- 1. Background Fill -->
  <rect width="1200" height="340" rx="14" fill="url(#bgGrad)"/>
  <rect width="1200" height="340" rx="14" fill="url(#cyanGlow)"/>
  <rect width="1200" height="340" rx="14" fill="url(#emeraldGlow)"/>

  <!-- 2. Technical Coordinate Grid -->
  <rect width="1200" height="340" rx="14" fill="url(#techGrid)"/>

  <!-- 3. Outer Frame Border and Specular Highlight -->
  <rect x="1" y="1" width="1198" height="338" rx="13" fill="none" stroke="url(#bannerBorder)" stroke-width="1.2"/>
  <path d="M 40 1.5 L 1160 1.5" stroke="#FFFFFF" stroke-opacity="0.22" stroke-width="1" stroke-linecap="round"/>

  <!-- 4. Corner Tech Decals -->
  <path d="M 16 32 L 16 16 L 32 16" fill="none" stroke="#00F2FE" stroke-width="1.5" opacity="0.7"/>
  <path d="M 1184 32 L 1184 16 L 1168 16" fill="none" stroke="#00F2FE" stroke-width="1.5" opacity="0.7"/>
  <path d="M 16 308 L 16 324 L 32 324" fill="none" stroke="#10B981" stroke-width="1.5" opacity="0.7"/>
  <path d="M 1184 308 L 1184 324 L 1168 324" fill="none" stroke="#10B981" stroke-width="1.5" opacity="0.7"/>

  <!-- ================= LEFT COLUMN: IDENTITY & GOVERNANCE ================= -->
  
  <!-- Live Status Chip -->
  <g transform="translate(60, 42)">
    <rect width="324" height="24" rx="12" fill="#0C1424" stroke="#00F2FE" stroke-opacity="0.3" stroke-width="1"/>
    <circle cx="14" cy="12" r="4.5" fill="#10B981"/>
    <circle cx="14" cy="12" r="8" fill="#10B981" opacity="0.25"/>
    <text x="28" y="15.5" class="font-mono pill-label" fill="#38BDF8">{left_status}</text>
    <circle cx="254" cy="12" r="1.5" fill="#64748B"/>
    <text x="264" y="15.5" class="font-mono pill-label" fill="#10B981">{right_status}</text>
  </g>

  <!-- Name -->
  <text x="60" y="112" class="font-sans title-name">{name}</text>

  <!-- Role Hierarchy -->
  <text x="60" y="148" class="font-sans role-title">{role}</text>
  <text x="60" y="174" class="font-sans sub-role">{specialization}</text>

  <!-- Accent Rule -->
  <path d="M 60 196 L 580 196" stroke="url(#accentLine)" stroke-width="1.5" stroke-linecap="round"/>

  <!-- Specialization Focus Line -->
  <g transform="translate(60, 222)">
    <text class="font-mono" font-size="12.5" fill="#CBD5E1" letter-spacing="0.4px">
      {focus_line}
    </text>
  </g>

  <!-- Capability Badges -->
  <g transform="translate(60, 256)">
{badges_markup}
  </g>

  <!-- ================= RIGHT COLUMN: SUBTLE CYBER / IAM VISUAL ================= -->
  <g transform="translate(935, 170)">
    <!-- Ambient Radial Aura -->
    <circle cx="0" cy="0" r="140" fill="#00F2FE" opacity="0.04"/>
    <circle cx="0" cy="0" r="100" fill="#10B981" opacity="0.05"/>

    <!-- Concentric Technical Radar / Scope Rings -->
    <circle cx="0" cy="0" r="130" fill="none" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 5"/>
    <circle cx="0" cy="0" r="106" fill="none" stroke="#00F2FE" stroke-opacity="0.22" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="82" fill="none" stroke="#1E293B" stroke-width="1" stroke-dasharray="2 4"/>
    <circle cx="0" cy="0" r="60" fill="none" stroke="#10B981" stroke-opacity="0.25" stroke-width="1.2"/>

    <!-- Crosshair Ticks -->
    <path d="M 0 -138 L 0 -122 M 0 122 L 0 138 M -138 0 L -122 0 M 122 0 L 138 0" stroke="#00F2FE" stroke-opacity="0.45" stroke-width="1.2"/>
    <path d="M -90 -90 L -80 -80 M 90 90 L 80 80 M 90 -90 L 80 -80 M -90 90 L -80 80" stroke="#10B981" stroke-opacity="0.35" stroke-width="1"/>

    <!-- Data Bus / Network Edges connecting nodes to center -->
    <line x1="0" y1="0" x2="-86" y2="-52" stroke="#00F2FE" stroke-opacity="0.35" stroke-width="1.4"/>
    <line x1="0" y1="0" x2="86" y2="-52" stroke="#00F2FE" stroke-opacity="0.35" stroke-width="1.4"/>
    <line x1="0" y1="0" x2="-100" y2="35" stroke="#10B981" stroke-opacity="0.35" stroke-width="1.4"/>
    <line x1="0" y1="0" x2="100" y2="35" stroke="#10B981" stroke-opacity="0.35" stroke-width="1.4"/>
    <line x1="0" y1="0" x2="0" y2="-106" stroke="#38BDF8" stroke-opacity="0.4" stroke-width="1.4"/>
    <line x1="0" y1="0" x2="0" y2="106" stroke="#A855F7" stroke-opacity="0.4" stroke-width="1.4"/>

    <!-- Geometric Hexagonal Security Perimeter -->
    <polygon points="0,-48 42,-24 42,24 0,48 -42,24 -42,-24" fill="#0C1525" stroke="#00F2FE" stroke-width="1.6" filter="url(#subtleGlow)"/>
    <polygon points="0,-40 35,-20 35,20 0,40 -35,20 -35,-20" fill="#070E1A" stroke="#10B981" stroke-width="1" stroke-opacity="0.4"/>

    <!-- Central Core IAM Shield Icon -->
    <path d="M 0 -18 L 14 -10 L 14 5 C 14 14 0 21 0 21 C 0 21 -14 14 -14 5 L -14 -10 Z" fill="url(#coreGlow)" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="1"/>
    <!-- Keyhole / Trust Glyph in Core -->
    <circle cx="0" cy="-2" r="3.2" fill="#070E1A"/>
    <path d="M -1.8 -1 L 1.8 -1 L 2.8 6 L -2.8 6 Z" fill="#070E1A"/>

    <!-- Node 1: Workday (HR Truth) Top -->
    <g transform="translate(0, -106)">
      <circle cx="0" cy="0" r="13" fill="#091220" stroke="#00F2FE" stroke-width="1.4"/>
      <circle cx="0" cy="0" r="4" fill="#00F2FE"/>
      <text x="18" y="4" class="font-mono" font-size="9" fill="#94A3B8" letter-spacing="0.5">HR TRUTH</text>
    </g>

    <!-- Node 2: Saviynt Core (Top-Right) -->
    <g transform="translate(86, -52)">
      <circle cx="0" cy="0" r="14" fill="#091220" stroke="#FFDB70" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="4.5" fill="#FFDB70"/>
      <text x="18" y="4" class="font-mono" font-size="9" fill="#FFDB70" font-weight="700" letter-spacing="0.5">SAVIYNT</text>
    </g>

    <!-- Node 3: Entra ID / AD (Bottom-Right) -->
    <g transform="translate(100, 35)">
      <circle cx="0" cy="0" r="12" fill="#091220" stroke="#38BDF8" stroke-width="1.2"/>
      <circle cx="0" cy="0" r="3.5" fill="#38BDF8"/>
      <text x="16" y="4" class="font-mono" font-size="9" fill="#94A3B8" letter-spacing="0.5">DIRECTORY</text>
    </g>

    <!-- Node 4: Autonomous AI Dev Team (Bottom) -->
    <g transform="translate(0, 106)">
      <circle cx="0" cy="0" r="13" fill="#091220" stroke="#A855F7" stroke-width="1.4"/>
      <circle cx="0" cy="0" r="4" fill="#A855F7"/>
      <text x="18" y="4" class="font-mono" font-size="9" fill="#C084FC" letter-spacing="0.5">AI DEV TEAM</text>
    </g>

    <!-- Node 5: 300K+ Reconciliation (Bottom-Left) -->
    <g transform="translate(-100, 35)">
      <circle cx="0" cy="0" r="14" fill="#091220" stroke="#10B981" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="4.5" fill="#10B981"/>
      <text x="-76" y="4" class="font-mono" font-size="9" fill="#34D399" font-weight="700" letter-spacing="0.5">300K+ RECON</text>
    </g>

    <!-- Node 6: SoD Matrix (Top-Left) -->
    <g transform="translate(-86, -52)">
      <circle cx="0" cy="0" r="12" fill="#091220" stroke="#F43F5E" stroke-width="1.2"/>
      <circle cx="0" cy="0" r="3.5" fill="#F43F5E"/>
      <text x="-74" y="4" class="font-mono" font-size="9" fill="#FDA4AF" letter-spacing="0.5">SOD MATRIX</text>
    </g>

    <!-- Ambient Orbital Data Packets -->
    <circle cx="48" cy="-29" r="2" fill="#00F2FE" opacity="0.9"/>
    <circle cx="-55" cy="19" r="2" fill="#10B981" opacity="0.9"/>
    <circle cx="0" cy="58" r="2" fill="#A855F7" opacity="0.8"/>
  </g>
</svg>
"""

    # Verify XML
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as err:
        print(f"❌ XML error in generated hero SVG: {err}", file=sys.stderr)
        return False

    HERO_SVG.parent.mkdir(parents=True, exist_ok=True)
    HERO_DIR_SVG.parent.mkdir(parents=True, exist_ok=True)

    with open(HERO_SVG, "w", encoding="utf-8") as out:
        out.write(svg_content)

    with open(HERO_DIR_SVG, "w", encoding="utf-8") as out:
        out.write(svg_content)

    print(f"✅ Hero banner generated successfully at {HERO_SVG} and {HERO_DIR_SVG}")
    return True

if __name__ == "__main__":
    success = generate_hero()
    sys.exit(0 if success else 1)
