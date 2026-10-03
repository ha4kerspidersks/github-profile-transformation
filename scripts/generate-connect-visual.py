#!/usr/bin/env python3
"""
Generate Cyber Communications Connect Panel (Master V2) for Subhajit Kar.
Synthesizes a 1280x380 widescreen SVG featuring:
- Futuristic terminal header and encrypted communication status
- 5 Verified professional network channels (Portfolio, LinkedIn, GitHub, Medium, X)
- Deloitte Cyber Risk location & availability status
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CONNECT_OUTPUT_SVG = ROOT_DIR / "assets/connect.svg"

def generate_connect():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 380" width="100%" height="auto" role="img" aria-label="Secure Communications &amp; Professional Channels — Subhajit Kar">
  <title>Secure Communications &amp; Professional Channels</title>
  <desc>Direct professional communication panel for Subhajit Kar: Executive Portfolio, LinkedIn, GitHub, Medium, and X.</desc>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&amp;family=Space+Grotesk:wght@600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap');

      .f-mono { font-family: 'JetBrains Mono', monospace; }
      .f-display { font-family: 'Space Grotesk', -apple-system, sans-serif; }
      .f-sans { font-family: 'Inter', -apple-system, sans-serif; }

      @keyframes neonPulse {
        0%, 100% { opacity: 0.35; filter: drop-shadow(0 0 10px rgba(0,242,254,0.4)); }
        50% { opacity: 0.8; filter: drop-shadow(0 0 20px rgba(0,242,254,0.8)); }
      }
      @keyframes signalBeacon {
        0%, 100% { r: 4px; opacity: 1; }
        50% { r: 6.5px; opacity: 0.4; }
      }

      .anim-pulse { animation: neonPulse 3.5s ease-in-out infinite; }
      .anim-beacon { animation: signalBeacon 2s ease-in-out infinite; }
    </style>

    <!-- Gradients -->
    <linearGradient id="connBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050812"/>
      <stop offset="50%" stop-color="#070D1D"/>
      <stop offset="100%" stop-color="#04060E"/>
    </linearGradient>

    <linearGradient id="connCardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F1A30"/>
      <stop offset="100%" stop-color="#080E1B"/>
    </linearGradient>

    <linearGradient id="connTitleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#FFDB70"/>
    </linearGradient>

    <!-- Pattern -->
    <pattern id="connGrid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#162238" stroke-width="0.6" stroke-opacity="0.4"/>
    </pattern>

    <!-- Filters -->
    <filter id="cardGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect width="1280" height="380" fill="url(#connBg)"/>
  <rect width="1280" height="380" fill="url(#connGrid)"/>

  <!-- Outer Frame -->
  <rect x="16" y="16" width="1248" height="348" rx="18" fill="none" stroke="#1E293B" stroke-width="1.2"/>
  <rect x="22" y="22" width="1236" height="336" rx="14" fill="none" stroke="#00F2FE" stroke-opacity="0.12" stroke-width="0.8"/>

  <!-- Corner Brackets -->
  <path d="M 28 44 L 28 28 L 44 28" fill="none" stroke="#00F2FE" stroke-width="2"/>
  <path d="M 1252 44 L 1252 28 L 1236 28" fill="none" stroke="#00F2FE" stroke-width="2"/>
  <path d="M 28 336 L 28 352 L 44 352" fill="none" stroke="#00F2FE" stroke-width="2"/>
  <path d="M 1252 336 L 1252 352 L 1236 352" fill="none" stroke="#00F2FE" stroke-width="2"/>

  <!-- Top Status Pill -->
  <g transform="translate(48, 48)">
    <rect x="0" y="0" width="340" height="26" rx="13" fill="#0A1424" stroke="#00F2FE" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="14" cy="13" r="4" fill="#10B981" class="anim-beacon"/>
    <text x="26" y="17" class="f-mono" font-size="10.5" font-weight="700" fill="#38BDF8" letter-spacing="1.2">// SECURE COMMUNICATIONS</text>
    <text x="210" y="17" class="f-mono" font-size="10" fill="#10B981">· ENCRYPTED</text>
  </g>

  <!-- Section Title & Subtitle -->
  <g transform="translate(48, 92)">
    <text x="0" y="26" class="f-display" font-size="28" font-weight="800" fill="url(#connTitleGrad)" letter-spacing="-0.3">Let's Engineer Enterprise Security Together</text>
    <text x="0" y="52" class="f-sans" font-size="13.5" fill="#94A3B8">Open to enterprise IAM architecture, identity governance leadership, and autonomous AI engineering collaborations.</text>
  </g>

  <!-- 5 Professional Channel Cards -->
  <g transform="translate(48, 175)">
    <!-- Card 1: Official Portfolio -->
    <a href="https://subhajitkar.com">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="224" height="110" rx="14" fill="url(#connCardGrad)" stroke="#00F2FE" stroke-opacity="0.5" stroke-width="1.2" filter="url(#cardGlow)"/>
        <!-- Specular Highlight -->
        <path d="M 14 1 L 210 1" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="1.2" stroke-linecap="round"/>
        <!-- Globe Icon -->
        <circle cx="36" cy="38" r="16" fill="#0A1426" stroke="#00F2FE" stroke-width="1"/>
        <text x="36" y="44" text-anchor="middle" font-size="16">🌐</text>
        <!-- Label -->
        <text x="64" y="34" class="f-display" font-size="15" font-weight="700" fill="#FFFFFF">subhajitkar.com</text>
        <text x="64" y="48" class="f-mono" font-size="10" font-weight="700" fill="#00F2FE">EXECUTIVE HUB</text>
        <text x="16" y="82" class="f-sans" font-size="11" fill="#CBD5E1">Official Portfolio &amp; Manuals</text>
        <text x="16" y="98" class="f-mono" font-size="9" fill="#64748B">&#8594; Open Interactive Site</text>
      </g>
    </a>

    <!-- Card 2: LinkedIn -->
    <a href="https://www.linkedin.com/in/subhajit-kar/">
      <g transform="translate(240, 0)">
        <rect x="0" y="0" width="224" height="110" rx="14" fill="url(#connCardGrad)" stroke="#0A66C2" stroke-opacity="0.6" stroke-width="1.2"/>
        <path d="M 14 1 L 210 1" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="1.2" stroke-linecap="round"/>
        <circle cx="36" cy="38" r="16" fill="#0A1426" stroke="#0A66C2" stroke-width="1"/>
        <text x="36" y="44" text-anchor="middle" font-size="15" font-weight="800" fill="#0A66C2">in</text>
        <text x="64" y="34" class="f-display" font-size="15" font-weight="700" fill="#FFFFFF">LinkedIn</text>
        <text x="64" y="48" class="f-mono" font-size="10" font-weight="700" fill="#38BDF8">in/subhajit-kar</text>
        <text x="16" y="82" class="f-sans" font-size="11" fill="#CBD5E1">Professional Network &amp; Posts</text>
        <text x="16" y="98" class="f-mono" font-size="9" fill="#64748B">&#8594; Connect on LinkedIn</text>
      </g>
    </a>

    <!-- Card 3: GitHub -->
    <a href="https://github.com/ha4kerspidersks">
      <g transform="translate(480, 0)">
        <rect x="0" y="0" width="224" height="110" rx="14" fill="url(#connCardGrad)" stroke="#F1F5F9" stroke-opacity="0.45" stroke-width="1.2"/>
        <path d="M 14 1 L 210 1" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="1.2" stroke-linecap="round"/>
        <circle cx="36" cy="38" r="16" fill="#0A1426" stroke="#F1F5F9" stroke-width="1"/>
        <text x="36" y="44" text-anchor="middle" font-size="16">🐙</text>
        <text x="64" y="34" class="f-display" font-size="15" font-weight="700" fill="#FFFFFF">GitHub</text>
        <text x="64" y="48" class="f-mono" font-size="10" font-weight="700" fill="#E2E8F0">ha4kerspidersks</text>
        <text x="16" y="82" class="f-sans" font-size="11" fill="#CBD5E1">Public Repos &amp; AI Systems</text>
        <text x="16" y="98" class="f-mono" font-size="9" fill="#64748B">&#8594; View Source Code</text>
      </g>
    </a>

    <!-- Card 4: Medium -->
    <a href="https://medium.com/@ha4ker_spider_sks">
      <g transform="translate(720, 0)">
        <rect x="0" y="0" width="224" height="110" rx="14" fill="url(#connCardGrad)" stroke="#10B981" stroke-opacity="0.5" stroke-width="1.2"/>
        <path d="M 14 1 L 210 1" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="1.2" stroke-linecap="round"/>
        <circle cx="36" cy="38" r="16" fill="#0A1426" stroke="#10B981" stroke-width="1"/>
        <text x="36" y="44" text-anchor="middle" font-size="15" font-weight="800" fill="#10B981">M</text>
        <text x="64" y="34" class="f-display" font-size="15" font-weight="700" fill="#FFFFFF">Medium</text>
        <text x="64" y="48" class="f-mono" font-size="10" font-weight="700" fill="#34D399">@ha4ker_spider_sks</text>
        <text x="16" y="82" class="f-sans" font-size="11" fill="#CBD5E1">Cybersecurity Engineering</text>
        <text x="16" y="98" class="f-mono" font-size="9" fill="#64748B">&#8594; Read Articles</text>
      </g>
    </a>

    <!-- Card 5: X / Twitter -->
    <a href="https://x.com/Ha4ker_spider">
      <g transform="translate(960, 0)">
        <rect x="0" y="0" width="224" height="110" rx="14" fill="url(#connCardGrad)" stroke="#A855F7" stroke-opacity="0.5" stroke-width="1.2"/>
        <path d="M 14 1 L 210 1" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="1.2" stroke-linecap="round"/>
        <circle cx="36" cy="38" r="16" fill="#0A1426" stroke="#A855F7" stroke-width="1"/>
        <text x="36" y="44" text-anchor="middle" font-size="15" font-weight="800" fill="#A855F7">𝕏</text>
        <text x="64" y="34" class="f-display" font-size="15" font-weight="700" fill="#FFFFFF">X / Twitter</text>
        <text x="64" y="48" class="f-mono" font-size="10" font-weight="700" fill="#D8B4FE">@Ha4ker_spider</text>
        <text x="16" y="82" class="f-sans" font-size="11" fill="#CBD5E1">Tech Discussions &amp; AI</text>
        <text x="16" y="98" class="f-mono" font-size="9" fill="#64748B">&#8594; Follow &amp; Engage</text>
      </g>
    </a>
  </g>

  <!-- Bottom Location & Status Bar -->
  <g transform="translate(48, 308)">
    <rect x="0" y="0" width="1184" height="32" rx="8" fill="#060C18" stroke="#1E293B" stroke-width="0.8"/>
    <circle cx="20" cy="16" r="3.5" fill="#10B981"/>
    <text x="32" y="20" class="f-mono" font-size="10" font-weight="700" fill="#38BDF8">DELOITTE CYBER &amp; STRATEGIC RISK</text>
    <text x="280" y="20" class="f-sans" font-size="10.5" fill="#64748B">· Kolkata, India (IST / UTC+5:30) · Open to Enterprise Security Architecture Inquiries</text>
  </g>
</svg>'''

    # Validate XML
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as err:
        print(f"❌ XML error in generated connect SVG: {err}", file=sys.stderr)
        return False

    CONNECT_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    with open(CONNECT_OUTPUT_SVG, "w", encoding="utf-8") as out:
        out.write(svg_content)

    print(f"✅ Generated Cyber Communications Connect Panel at {CONNECT_OUTPUT_SVG}")
    print(f"   Size: {CONNECT_OUTPUT_SVG.stat().st_size / 1024:.1f} KB")
    return True

if __name__ == "__main__":
    success = generate_connect()
    sys.exit(0 if success else 1)
