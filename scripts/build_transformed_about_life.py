#!/usr/bin/env python3
"""
scripts/build_transformed_about_life.py
Builds the complete, reference-faithful assets/about-life.svg:
1. Card 1 (// ARCHITECT):
   - Label: // ARCHITECT
   - Headline: Security, Identity & AI systems that scale
   - Browser URL: localhost:5173/subhajit
   - Illustration: Male Cybersecurity, IAM & AI Engineer (Subhajit Kar) at workstation
   - Subtle native SMIL animations (laptop screen glow, shield keyhole pulse, AI node pulse, idle float)
   - Capability Rows:
     * Row 1: Cybersecurity & Identity Engineering (IAM/IGA, Saviynt, Entra ID, Active Directory, Zero Trust)
     * Row 2: Security Automation & Engineering (Python, APIs, JML, RBAC/ABAC, reconciliation & security automation)
     * Row 3: AI, CTF & Security Research (AI agents, LLMs, security experimentation, CTFs & offensive security)
2. Card 2 (// OFF THE CLOCK):
   - Preserved 12s looping carousel with 3 canonical Subhajit Kar fitness illustrations:
     * Slide 0 (0s): FOOTBALL (⚽ Male football player)
     * Slide 1 (4s): BADMINTON (🏸 Male badminton player)
     * Slide 2 (8s): COOKING (👨‍🍳 Male cooking / chef)
   - Caption pills: FOOTBALL, BADMINTON, COOKING
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF_SVG = ROOT / "reference-base/about-life.svg"
OUT_SVG = ROOT / "assets/about-life.svg"
FITNESS_JSON = ROOT / "qa/fitness-assets.json"
ARCHITECT_JSON = ROOT / "qa/architect-asset.json"

def main():
    print("🚀 Transforming about-life.svg (Architect + Fitness)...")
    with open(REF_SVG, "r", encoding="utf-8") as f:
        svg = f.read()

    # Load assets
    with open(FITNESS_JSON, "r", encoding="utf-8") as f:
        fitness_assets = json.load(f)
    football_uri = fitness_assets['football']['webp']
    badminton_uri = fitness_assets['badminton']['webp']
    cooking_uri = fitness_assets['cooking']['webp']

    with open(ARCHITECT_JSON, "r", encoding="utf-8") as f:
        architect_asset = json.load(f)
    architect_uri = architect_asset['webpData']

    # =========================================================================
    # BACK-TO-FRONT REPLACEMENTS (PRESERVES EXACT STRING OFFSETS)
    # =========================================================================

    # 1. Slide 2: 👨‍🍳 Male Cooking
    s2_start = svg.find('<g class="slide" opacity="0" style="animation-delay:8s">')
    s2_end = svg.find('</svg></g>', s2_start) + len('</svg></g>')
    new_slide2 = f'''<g class="slide" opacity="0" style="animation-delay:8s">
      <svg x="748" y="148" width="444" height="312" viewBox="0 0 888 624" preserveAspectRatio="xMidYMid meet" overflow="hidden">
        <g>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="2s" repeatCount="indefinite" ease="ease-in-out"/>
          <image x="0" y="0" width="888" height="624" preserveAspectRatio="xMidYMid meet" href="{cooking_uri}"/>
        </g>
      </svg></g>'''
    svg = svg[:s2_start] + new_slide2 + svg[s2_end:]
    print("  ✅ Integrated Slide 2: 👨‍🍳 Male Cooking (Subhajit Kar)")

    # 2. Slide 1: 🏸 Male Badminton Player
    s1_start = svg.find('<g class="slide" opacity="0" style="animation-delay:4s">')
    s1_end = svg.find('</svg></g>', s1_start) + len('</svg></g>')
    new_slide1 = f'''<g class="slide" opacity="0" style="animation-delay:4s">
      <svg x="748" y="148" width="444" height="312" viewBox="0 0 888 624" preserveAspectRatio="xMidYMid meet" overflow="hidden">
        <g>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -8; 0 0" dur="2.2s" repeatCount="indefinite" ease="ease-in-out"/>
          <image x="0" y="0" width="888" height="624" preserveAspectRatio="xMidYMid meet" href="{badminton_uri}"/>
        </g>
      </svg></g>'''
    svg = svg[:s1_start] + new_slide1 + svg[s1_end:]
    print("  ✅ Integrated Slide 1: 🏸 Male Badminton Player (Subhajit Kar)")

    # 3. Slide 0: ⚽ Male Football Player
    s0_start = svg.find('<g class="slide" opacity="1" style="animation-delay:0s">')
    s0_end = svg.find('</svg></g>', s0_start) + len('</svg></g>')
    new_slide0 = f'''<g class="slide" opacity="1" style="animation-delay:0s">
      <svg x="748" y="148" width="444" height="312" viewBox="0 0 888 624" preserveAspectRatio="xMidYMid meet" overflow="hidden">
        <g>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -4; 0 0" dur="2s" repeatCount="indefinite" ease="ease-in-out"/>
          <image x="0" y="0" width="888" height="624" preserveAspectRatio="xMidYMid meet" href="{football_uri}"/>
        </g>
      </svg></g>'''
    svg = svg[:s0_start] + new_slide0 + svg[s0_end:]
    print("  ✅ Integrated Slide 0: ⚽ Male Football Player (Subhajit Kar)")

    # 4. Capability Rows
    r_start = svg.find('<g class="row" style="animation-delay:1.0s">')
    r_end = svg.find('\n</g>\n<g class="cardR">')
    new_rows = '''<g class="row" style="animation-delay:1.0s">
    <rect x="28" y="496" width="38" height="38" rx="10" fill="#22d3ee" fill-opacity=".12" stroke="#22d3ee" stroke-opacity=".35"/>
    <g transform="translate(47,515)" fill="none" stroke="#22d3ee" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M0 -9 L8 -5 V0 C8 5.5 4 9 0 10.5 C-4 9 -8 5.5 -8 0 V-5 Z"/>
      <circle cx="0" cy="-0.5" r="1.6" fill="#22d3ee"/>
      <path d="M-0.8 1.1 L0.8 1.1 L1.2 4 L-1.2 4 Z" fill="#22d3ee"/>
    </g>
    <text class="sg" x="82" y="512" font-size="15.5" fill="#eceef6">Cybersecurity &amp; Identity Engineering</text>
    <text class="jb" x="82" y="530" font-size="12" fill="#8d93ab">IAM / IGA, Saviynt, Entra ID, Active Directory, Zero Trust</text>
  </g>
  <g class="row" style="animation-delay:1.18s">
    <rect x="28" y="544" width="38" height="38" rx="10" fill="#a78bfa" fill-opacity=".12" stroke="#a78bfa" stroke-opacity=".35"/>
    <g transform="translate(47,563)" fill="none" stroke="#a78bfa" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="-9" y="-8" width="18" height="16" rx="3"/>
      <path d="M-5 -2 L-2 0.5 L-5 3 M0 3 L4 3"/>
    </g>
    <text class="sg" x="82" y="560" font-size="15.5" fill="#eceef6">Security Automation &amp; Engineering</text>
    <text class="jb" x="82" y="578" font-size="12" fill="#8d93ab">Python, APIs, JML, RBAC/ABAC, reconciliation &amp; security automation</text>
  </g>
  <g class="row" style="animation-delay:1.36s">
    <rect x="28" y="592" width="38" height="38" rx="10" fill="#fbbf24" fill-opacity=".12" stroke="#fbbf24" stroke-opacity=".35"/>
    <g transform="translate(47,611)" fill="none" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="0" cy="0" r="3.2" fill="#fbbf24" fill-opacity=".25"/>
      <circle cx="-6.5" cy="-5" r="1.6"/><circle cx="6.5" cy="-5" r="1.6"/>
      <circle cx="-6.5" cy="5" r="1.6"/><circle cx="6.5" cy="5" r="1.6"/>
      <path d="M-4.8 -3.8 L-1.8 -1.4 M4.8 -3.8 L1.8 -1.4 M-4.8 3.8 L-1.8 1.4 M4.8 3.8 L1.8 1.4"/>
    </g>
    <text class="sg" x="82" y="608" font-size="15.5" fill="#eceef6">AI, CTF &amp; Security Research</text>
    <text class="jb" x="82" y="626" font-size="12" fill="#8d93ab">AI agents, LLMs, security experimentation, CTFs &amp; offensive security</text>
  </g>'''
    svg = svg[:r_start] + new_rows + svg[r_end:]
    print("  ✅ Updated Capability Rows (Cybersecurity/IAM, Automation, AI/CTF)")

    # 5. Desk Illustration: Replace with Male Cybersecurity Architect
    desk_start = svg.find('<svg x="28" y="152"')
    desk_end = svg.find('</svg>', desk_start) + len('</svg>')
    new_architect_svg = f'''<svg x="28" y="152" width="564" height="318" viewBox="0 0 1080 608" preserveAspectRatio="xMidYMid meet" overflow="hidden">
      <defs>
        <linearGradient id="archbg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#edf2fe"/>
          <stop offset="100%" stop-color="#dce6f9"/>
        </linearGradient>
      </defs>
      <rect width="1080" height="608" fill="url(#archbg)"/>
      <g opacity=".35">
        <line x1="60" y1="140" x2="1020" y2="140" stroke="#94a3b8" stroke-dasharray="4,8" stroke-width="1.2"/>
        <line x1="60" y1="280" x2="1020" y2="280" stroke="#94a3b8" stroke-dasharray="4,8" stroke-width="1.2"/>
        <line x1="60" y1="420" x2="1020" y2="420" stroke="#94a3b8" stroke-dasharray="4,8" stroke-width="1.2"/>
        <line x1="220" y1="40" x2="220" y2="560" stroke="#94a3b8" stroke-dasharray="4,8" stroke-width="1.2"/>
        <line x1="540" y1="40" x2="540" y2="560" stroke="#94a3b8" stroke-dasharray="4,8" stroke-width="1.2"/>
        <line x1="860" y1="40" x2="860" y2="560" stroke="#94a3b8" stroke-dasharray="4,8" stroke-width="1.2"/>
      </g>
      <ellipse cx="540" cy="540" rx="420" ry="70" fill="#22d3ee" fill-opacity=".15">
        <animate attributeName="fill-opacity" values=".10;.22;.10" dur="3s" repeatCount="indefinite"/>
      </ellipse>
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -2.5; 0 0" dur="3.5s" repeatCount="indefinite" ease="ease-in-out"/>
        <image x="0" y="0" width="1080" height="608" preserveAspectRatio="xMidYMid meet" href="{architect_uri}"/>
        <circle cx="316" cy="172" r="3.5" fill="#22d3ee" opacity=".8">
          <animate attributeName="r" values="2.5; 7; 2.5" dur="2.4s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values=".9; .15; .9" dur="2.4s" repeatCount="indefinite"/>
        </circle>
        <circle cx="688" cy="262" r="4.5" fill="#a78bfa" opacity=".75">
          <animate attributeName="r" values="3.5; 8; 3.5" dur="2.8s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values=".85; .15; .85" dur="2.8s" repeatCount="indefinite"/>
        </circle>
        <rect x="583" y="380" width="3" height="8" fill="#22d3ee">
          <animate attributeName="opacity" values="1; 0; 1" dur="0.9s" repeatCount="indefinite" calcMode="discrete"/>
        </rect>
      </g>
    </svg>'''
    svg = svg[:desk_start] + new_architect_svg + svg[desk_end:]
    print("  ✅ Replaced desk illustration with Cybersecurity Architect (Subhajit Kar)")

    # 6. Global Header Text & Address Bar
    svg = svg.replace('// DEVELOPER', '// ARCHITECT')
    svg = svg.replace('font-size="29" fill="#eceef6" letter-spacing="-.5">Security, Identity &amp; AI systems that scale',
                      'font-size="27" fill="#eceef6" letter-spacing="-.5">Security, Identity &amp; AI systems that scale')
    svg = svg.replace('localhost:5173/megha', 'subhajitkar.com/architecture')
    svg = svg.replace('localhost:5173/subhajit', 'subhajitkar.com/architecture')

    # 7. Card 2: Caption Badges
    old_cap0 = '<g class="cap" opacity="1" style="animation-delay:0s"><rect x="688" y="494" width="53" height="24" rx="12" fill="#34d399" fill-opacity=".14" stroke="#34d399" stroke-opacity=".45"/><text class="jbb" x="701" y="510" font-size="11.5" fill="#34d399" letter-spacing="1.5">RUN</text><text class="sg" x="755" y="512" font-size="20" fill="#eceef6">Health conscious</text><text class="sgm" x="688" y="544" font-size="15.5" fill="#8d93ab">Morning runs &amp; mindful habits fuel long build days.</text></g>'
    new_cap0 = '<g class="cap" opacity="1" style="animation-delay:0s"><rect x="688" y="494" width="86" height="24" rx="12" fill="#34d399" fill-opacity=".14" stroke="#34d399" stroke-opacity=".45"/><text class="jbb" x="701" y="510" font-size="11.5" fill="#34d399" letter-spacing="1.5">FOOTBALL</text><text class="sg" x="788" y="512" font-size="20" fill="#eceef6">Dynamic on the pitch</text><text class="sgm" x="688" y="544" font-size="15.5" fill="#8d93ab">Tactical teamwork, explosive energy &amp; weekend matches.</text></g>'

    old_cap1 = '<g class="cap" opacity="0" style="animation-delay:4s"><rect x="688" y="494" width="71" height="24" rx="12" fill="#fbbf24" fill-opacity=".14" stroke="#fbbf24" stroke-opacity=".45"/><text class="jbb" x="701" y="510" font-size="11.5" fill="#fbbf24" letter-spacing="1.5">SKATE</text><text class="sg" x="773" y="512" font-size="20" fill="#eceef6">Weekend skater</text><text class="sgm" x="688" y="544" font-size="15.5" fill="#8d93ab">Balance on the board, balance in life.</text></g>'
    new_cap1 = '<g class="cap" opacity="0" style="animation-delay:4s"><rect x="688" y="494" width="96" height="24" rx="12" fill="#fbbf24" fill-opacity=".14" stroke="#fbbf24" stroke-opacity=".45"/><text class="jbb" x="701" y="510" font-size="11.5" fill="#fbbf24" letter-spacing="1.5">BADMINTON</text><text class="sg" x="798" y="512" font-size="20" fill="#eceef6">Smash &amp; agility</text><text class="sgm" x="688" y="544" font-size="15.5" fill="#8d93ab">High-speed rallies, fast footwork &amp; court instincts.</text></g>'

    old_cap2 = '<g class="cap" opacity="0" style="animation-delay:8s"><rect x="688" y="494" width="71" height="24" rx="12" fill="#f472b6" fill-opacity=".14" stroke="#f472b6" stroke-opacity=".45"/><text class="jbb" x="701" y="510" font-size="11.5" fill="#f472b6" letter-spacing="1.5">ANIME</text><text class="sg" x="773" y="512" font-size="20" fill="#eceef6">Anime &amp; ramen</text><text class="sgm" x="688" y="544" font-size="15.5" fill="#8d93ab">Where most of my project ideas are born.</text></g>'
    new_cap2 = '<g class="cap" opacity="0" style="animation-delay:8s"><rect x="688" y="494" width="82" height="24" rx="12" fill="#f472b6" fill-opacity=".14" stroke="#f472b6" stroke-opacity=".45"/><text class="jbb" x="701" y="510" font-size="11.5" fill="#f472b6" letter-spacing="1.5">COOKING</text><text class="sg" x="784" y="512" font-size="20" fill="#eceef6">Culinary craft</text><text class="sgm" x="688" y="544" font-size="15.5" fill="#8d93ab">Fresh ingredients, sauté pan tosses &amp; mindful recipes.</text></g>'

    svg = svg.replace(old_cap0, new_cap0)
    svg = svg.replace(old_cap1, new_cap1)
    svg = svg.replace(old_cap2, new_cap2)
    print("  ✅ Updated Fitness Caption Badges")

    # =========================================================================
    # 8. XML VALIDATION & OUTPUT
    # =========================================================================
    try:
        ET.fromstring(svg)
        print("🌟 XML is 100% Well-Formed and Valid!")
    except ET.ParseError as e:
        print("❌ XML Validation Failed:", e)
        raise e

    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"🎉 Successfully written to {OUT_SVG} ({len(svg)} bytes)")

if __name__ == "__main__":
    main()
