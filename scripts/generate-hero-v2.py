#!/usr/bin/env python3
"""
Generate Cinematic Hero Banner (Master V2) for Subhajit Kar's GitHub Profile.
Synthesizes a 1280x540 widescreen cinematic cyber-identity visual featuring:
- Left: Authentic name, role, specialization, verified metrics, terminal HUD telemetry
- Right: Authentic portfolio portrait embedded as base64 in an animated cybernetic frame,
  with scanner line, targeting brackets, holographic rings, and floating glass chips.
"""

import base64
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PORTRAIT_PATH = ROOT_DIR / "assets/hero/generated/portrait-500.jpg"
HERO_OUTPUT_SVG = ROOT_DIR / "assets/hero.svg"
HERO_BANNER_SVG = ROOT_DIR / "assets/hero-banner.svg"
HERO_DIR_SVG = ROOT_DIR / "assets/hero/hero-banner.svg"

def get_portrait_base64():
    if not PORTRAIT_PATH.exists():
        # Fallback to source
        alt = ROOT_DIR / "assets/avatar/github-avatar.jpg"
        if alt.exists():
            with open(alt, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
        raise FileNotFoundError(f"Portrait not found at {PORTRAIT_PATH}")
    with open(PORTRAIT_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def generate_hero():
    portrait_b64 = get_portrait_base64()

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 540" width="100%" height="auto" role="img" aria-label="Subhajit Kar — Senior IAM Assistant Manager &amp; Cyber Risk Leader">
  <title>Subhajit Kar — Senior IAM Assistant Manager &amp; Cyber Risk Leader</title>
  <desc>Widescreen cinematic GitHub profile hero featuring Subhajit Kar, Senior IAM Assistant Manager at Deloitte, governing 300K+ monthly enterprise identities.</desc>
  <defs>
    <!-- Fonts -->
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&amp;family=Space+Grotesk:wght@500;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap');

      .f-mono {{ font-family: 'JetBrains Mono', monospace; }}
      .f-display {{ font-family: 'Space Grotesk', -apple-system, sans-serif; }}
      .f-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      /* Animations */
      @keyframes radarSpin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      @keyframes scanVertical {{
        0% {{ transform: translateY(-160px); opacity: 0; }}
        20% {{ opacity: 0.85; }}
        80% {{ opacity: 0.85; }}
        100% {{ transform: translateY(160px); opacity: 0; }}
      }}
      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.35; filter: drop-shadow(0 0 15px rgba(0,242,254,0.4)); }}
        50% {{ opacity: 0.75; filter: drop-shadow(0 0 30px rgba(0,242,254,0.8)); }}
      }}
      @keyframes floatChip1 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(0, -7px); }}
      }}
      @keyframes floatChip2 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(0, 7px); }}
      }}
      @keyframes dotPulse {{
        0%, 100% {{ r: 4px; opacity: 1; }}
        50% {{ r: 6px; opacity: 0.6; }}
      }}
      @keyframes dashFlow {{
        to {{ stroke-dashoffset: -32; }}
      }}

      .anim-radar {{ transform-origin: 1040px 270px; animation: radarSpin 24s linear infinite; }}
      .anim-scan {{ animation: scanVertical 4s ease-in-out infinite; }}
      .anim-pulse {{ animation: pulseGlow 4s ease-in-out infinite; }}
      .anim-float1 {{ animation: floatChip1 5s ease-in-out infinite; }}
      .anim-float2 {{ animation: floatChip2 6s ease-in-out infinite; }}
      .anim-dot {{ animation: dotPulse 2s ease-in-out infinite; }}
      .anim-dash {{ stroke-dasharray: 6 6; animation: dashFlow 2s linear infinite; }}
    </style>

    <!-- Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#080E1C"/>
      <stop offset="100%" stop-color="#04070E"/>
    </linearGradient>

    <linearGradient id="cyanGoldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="45%" stop-color="#38BDF8"/>
      <stop offset="85%" stop-color="#FFDB70"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>

    <linearGradient id="neonCyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>

    <linearGradient id="goldAmberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFDB70"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>

    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#0A0F1D" stop-opacity="0.95"/>
    </linearGradient>

    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00F2FE" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="cyanAmbient" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="#3B82F6" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="emeraldAmbient" cx="20%" cy="30%" r="40%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <!-- Cyber Grid Pattern -->
    <pattern id="cyberGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1E293B" stroke-width="0.7" stroke-opacity="0.45"/>
      <circle cx="40" cy="40" r="1" fill="#38BDF8" fill-opacity="0.3"/>
    </pattern>

    <!-- Filters -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="subtleGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Portrait Clip Path (Rounded Hexagon / Squircle) -->
    <clipPath id="portraitClip">
      <rect x="910" y="140" width="260" height="260" rx="36" ry="36"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="1280" height="540" fill="url(#bgGrad)"/>
  <rect width="1280" height="540" fill="url(#cyberGrid)"/>
  <rect width="1280" height="540" fill="url(#cyanAmbient)"/>
  <rect width="1280" height="540" fill="url(#emeraldAmbient)"/>

  <!-- Outer Frame Border -->
  <rect x="16" y="16" width="1248" height="508" rx="20" fill="none" stroke="#1E293B" stroke-width="1.2"/>
  <rect x="22" y="22" width="1236" height="496" rx="16" fill="none" stroke="#00F2FE" stroke-opacity="0.15" stroke-width="0.8"/>

  <!-- Corner Brackets -->
  <path d="M 28 50 L 28 28 L 50 28" fill="none" stroke="#00F2FE" stroke-width="2.5"/>
  <path d="M 1252 50 L 1252 28 L 1230 28" fill="none" stroke="#00F2FE" stroke-width="2.5"/>
  <path d="M 28 490 L 28 512 L 50 512" fill="none" stroke="#00F2FE" stroke-width="2.5"/>
  <path d="M 1252 490 L 1252 512 L 1230 512" fill="none" stroke="#00F2FE" stroke-width="2.5"/>

  <!-- Top System Status Strip -->
  <g transform="translate(56, 52)">
    <rect x="0" y="0" width="410" height="30" rx="15" fill="#0A1324" stroke="#00F2FE" stroke-opacity="0.35" stroke-width="1"/>
    <circle cx="16" cy="15" r="4.5" fill="#10B981" class="anim-dot"/>
    <text x="32" y="19" class="f-mono" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1.2">DELOITTE CYBER &amp; STRATEGIC RISK</text>
    <line x1="285" y1="8" x2="285" y2="22" stroke="#1E293B" stroke-width="1"/>
    <text x="298" y="19" class="f-mono" font-size="10.5" font-weight="700" fill="#10B981" letter-spacing="1">LIVE IGA</text>
  </g>

  <!-- Top Right Operational Timestamp -->
  <g transform="translate(1030, 52)">
    <text x="0" y="18" class="f-mono" font-size="10.5" fill="#64748B" letter-spacing="1">NODE: SEC-AUTH-PROD</text>
    <circle cx="140" cy="15" r="3.5" fill="#00F2FE" opacity="0.8"/>
  </g>

  <!-- ==================== LEFT COLUMN: IDENTITY & METRICS ==================== -->
  <g transform="translate(56, 115)">
    <!-- Primary Subtitle Pre-heading -->
    <text x="0" y="14" class="f-mono" font-size="12.5" font-weight="600" fill="#00F2FE" letter-spacing="2.8">// ENTERPRISE IDENTITY ARCHITECTURE</text>

    <!-- Authoritative Name Headline -->
    <text x="0" y="62" class="f-display" font-size="46" font-weight="800" fill="url(#cyanGoldGrad)" letter-spacing="-0.5" filter="url(#subtleGlow)">SUBHAJIT KAR</text>

    <!-- Role Title -->
    <text x="0" y="98" class="f-sans" font-size="20" font-weight="700" fill="#F1F5F9" letter-spacing="0.2">Senior IAM Assistant Manager &amp; Cyber Risk Leader</text>

    <!-- Specialization & Scope -->
    <text x="0" y="126" class="f-sans" font-size="14.5" font-weight="400" fill="#94A3B8" letter-spacing="0.2">Enterprise Identity Governance · Saviynt IGA · Workday &amp; Azure AD Architecture</text>

    <!-- Terminal HUD Box -->
    <g transform="translate(0, 150)">
      <rect x="0" y="0" width="760" height="136" rx="12" fill="#070D18" stroke="#1E293B" stroke-width="1.2"/>
      <rect x="0" y="0" width="760" height="28" rx="12" fill="#0B1528"/>
      <!-- Window Dots -->
      <circle cx="16" cy="14" r="4" fill="#EF4444" opacity="0.85"/>
      <circle cx="30" cy="14" r="4" fill="#F59E0B" opacity="0.85"/>
      <circle cx="44" cy="14" r="4" fill="#10B981" opacity="0.85"/>
      <text x="64" y="18" class="f-mono" font-size="10" fill="#64748B" letter-spacing="1">TELEMETRY_LOG · IAM-CORE-PIPELINE</text>

      <!-- Terminal Output Lines -->
      <text x="20" y="52" class="f-mono" font-size="11.5" fill="#38BDF8">
        <tspan fill="#00F2FE" font-weight="700">&gt; GOVERNANCE:</tspan> 300K+ Monthly Identities Reconciled across 9 Global Regions
      </text>
      <text x="20" y="74" class="f-mono" font-size="11.5" fill="#E2E8F0">
        <tspan fill="#10B981" font-weight="700">&gt; CORE STACK:</tspan> Saviynt IGA Core · Workday HRMS · Microsoft Entra ID · AD DS
      </text>
      <text x="20" y="96" class="f-mono" font-size="11.5" fill="#CBD5E1">
        <tspan fill="#FFDB70" font-weight="700">&gt; COMPLIANCE:</tspan> Continuous SoD Auditing · Automated JML Workflows · Zero Trust
      </text>
      <text x="20" y="118" class="f-mono" font-size="11.5" fill="#94A3B8">
        <tspan fill="#A855F7" font-weight="700">&gt; ENGINEERING:</tspan> Python ETL Engine · 13 Deloitte Awards · Autonomous AI Dev Team
      </text>
    </g>

    <!-- Key Metrics Ribbon Chips -->
    <g transform="translate(0, 304)">
      <!-- Chip 1 -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="232" height="48" rx="10" fill="#0A1426" stroke="#00F2FE" stroke-opacity="0.35" stroke-width="1"/>
        <text x="14" y="23" class="f-display" font-size="16" font-weight="700" fill="#00F2FE">300K+</text>
        <text x="76" y="23" class="f-mono" font-size="11" font-weight="700" fill="#E2E8F0">IDENTITIES / MO</text>
        <text x="14" y="39" class="f-sans" font-size="10" fill="#64748B">Reconciled Enterprise Volume</text>
      </g>

      <!-- Chip 2 -->
      <g transform="translate(248, 0)">
        <rect x="0" y="0" width="232" height="48" rx="10" fill="#0A1426" stroke="#FFDB70" stroke-opacity="0.35" stroke-width="1"/>
        <text x="14" y="23" class="f-display" font-size="16" font-weight="700" fill="#FFDB70">13 AWARDS</text>
        <text x="110" y="23" class="f-mono" font-size="11" font-weight="700" fill="#E2E8F0">DELOITTE</text>
        <text x="14" y="39" class="f-sans" font-size="10" fill="#64748B">Firm-wide Honors &amp; Badges</text>
      </g>

      <!-- Chip 3 -->
      <g transform="translate(496, 0)">
        <rect x="0" y="0" width="264" height="48" rx="10" fill="#0A1426" stroke="#10B981" stroke-opacity="0.35" stroke-width="1"/>
        <text x="14" y="23" class="f-display" font-size="16" font-weight="700" fill="#10B981">M.TECH</text>
        <text x="80" y="23" class="f-mono" font-size="11" font-weight="700" fill="#E2E8F0">CYBER SECURITY</text>
        <text x="14" y="39" class="f-sans" font-size="10" fill="#64748B">NFSU Gujarat · Digital Forensics</text>
      </g>
    </g>
  </g>

  <!-- ==================== RIGHT COLUMN: CINEMATIC PORTRAIT & HUD ==================== -->
  <!-- Ambient Radar & Targeting Rings -->
  <g class="anim-radar">
    <circle cx="1040" cy="270" r="190" fill="none" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="4 8"/>
    <circle cx="1040" cy="270" r="165" fill="none" stroke="#00F2FE" stroke-opacity="0.25" stroke-width="1.2" stroke-dasharray="8 6"/>
    <circle cx="1040" cy="270" r="145" fill="none" stroke="#38BDF8" stroke-opacity="0.2" stroke-width="0.8"/>
    <line x1="850" y1="270" x2="1230" y2="270" stroke="#00F2FE" stroke-opacity="0.12" stroke-width="0.8"/>
    <line x1="1040" y1="80" x2="1040" y2="460" stroke="#00F2FE" stroke-opacity="0.12" stroke-width="0.8"/>
  </g>

  <!-- Glowing Aura behind portrait -->
  <rect x="898" y="128" width="284" height="284" rx="42" fill="none" stroke="url(#cyanGoldGrad)" stroke-width="2.5" class="anim-pulse"/>

  <!-- Portrait Container Card -->
  <rect x="904" y="134" width="272" height="272" rx="38" fill="#0B1324" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Authentic Portrait Image (Base64) -->
  <g clip-path="url(#portraitClip)">
    <image xlink:href="data:image/jpeg;base64,{portrait_b64}" x="910" y="140" width="260" height="260" preserveAspectRatio="xMidYMid slice"/>
    <!-- Subtle Cyan Tint Overlay -->
    <rect x="910" y="140" width="260" height="260" fill="#00F2FE" opacity="0.04"/>
    <!-- Vertical Scanner Effect -->
    <g class="anim-scan">
      <rect x="910" y="260" width="260" height="24" fill="url(#scanlineGrad)"/>
      <line x1="910" y1="272" x2="1170" y2="272" stroke="#00F2FE" stroke-width="1.8" filter="url(#subtleGlow)"/>
    </g>
  </g>

  <!-- Corner Reticle Brackets on Portrait -->
  <path d="M 900 160 L 900 130 L 930 130" fill="none" stroke="#00F2FE" stroke-width="2"/>
  <path d="M 1180 160 L 1180 130 L 1150 130" fill="none" stroke="#00F2FE" stroke-width="2"/>
  <path d="M 900 380 L 900 410 L 930 410" fill="none" stroke="#FFDB70" stroke-width="2"/>
  <path d="M 1180 380 L 1180 410 L 1150 410" fill="none" stroke="#FFDB70" stroke-width="2"/>

  <!-- ==================== FLOATING GLASS CHIPS ==================== -->
  <!-- Chip 1: Saviynt Core (Top-Right) -->
  <g transform="translate(1120, 105)" class="anim-float1">
    <rect x="0" y="0" width="124" height="34" rx="17" fill="#08101E" stroke="#00F2FE" stroke-width="1.2" filter="url(#subtleGlow)"/>
    <circle cx="16" cy="17" r="5" fill="#00F2FE"/>
    <text x="28" y="21" class="f-mono" font-size="10.5" font-weight="700" fill="#F1F5F9" letter-spacing="0.5">SAVIYNT IGA</text>
  </g>

  <!-- Chip 2: Deloitte AM (Top-Left) -->
  <g transform="translate(830, 115)" class="anim-float2">
    <rect x="0" y="0" width="130" height="34" rx="17" fill="#08101E" stroke="#10B981" stroke-width="1.2" filter="url(#subtleGlow)"/>
    <circle cx="16" cy="17" r="5" fill="#10B981"/>
    <text x="28" y="21" class="f-mono" font-size="10.5" font-weight="700" fill="#34D399" letter-spacing="0.5">DELOITTE AM</text>
  </g>

  <!-- Chip 3: 300K+ Recon (Bottom-Left) -->
  <g transform="translate(830, 395)" class="anim-float1">
    <rect x="0" y="0" width="138" height="34" rx="17" fill="#08101E" stroke="#FFDB70" stroke-width="1.2" filter="url(#subtleGlow)"/>
    <circle cx="16" cy="17" r="5" fill="#FFDB70"/>
    <text x="28" y="21" class="f-mono" font-size="10.5" font-weight="700" fill="#FFDB70" letter-spacing="0.5">300K+ RECON</text>
  </g>

  <!-- Chip 4: AI Dev Team (Bottom-Right) -->
  <g transform="translate(1120, 405)" class="anim-float2">
    <rect x="0" y="0" width="132" height="34" rx="17" fill="#08101E" stroke="#A855F7" stroke-width="1.2" filter="url(#subtleGlow)"/>
    <circle cx="16" cy="17" r="5" fill="#A855F7"/>
    <text x="28" y="21" class="f-mono" font-size="10.5" font-weight="700" fill="#D8B4FE" letter-spacing="0.5">AI DEV TEAM</text>
  </g>

  <!-- Authentication Status Hash at Bottom Right of Portrait -->
  <g transform="translate(930, 440)">
    <rect x="0" y="0" width="220" height="24" rx="6" fill="#070E1A" stroke="#1E293B" stroke-width="0.8"/>
    <text x="12" y="16" class="f-mono" font-size="9" fill="#64748B" letter-spacing="1">AUTH_ID: SKS-DEL-7170-MTECH</text>
  </g>
</svg>
'''

    # XML Validation
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as err:
        print(f"❌ XML error in generated hero SVG: {err}", file=sys.stderr)
        return False

    HERO_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    with open(HERO_OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)

    with open(HERO_BANNER_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)

    with open(HERO_DIR_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ Generated cinematic hero SVG at {HERO_OUTPUT_SVG}")
    print(f"   Size: {os.path.getsize(HERO_OUTPUT_SVG) / 1024:.1f} KB")
    return True

if __name__ == "__main__":
    success = generate_hero()
    sys.exit(0 if success else 1)
