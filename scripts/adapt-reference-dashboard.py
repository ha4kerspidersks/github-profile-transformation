#!/usr/bin/env python3
"""
Adapt Reference Repository id-dashboard.svg for Subhajit Kar.
Directly uses reference-base/id-dashboard.svg (100% original Meghamittal0920 source).
Preserves:
- EXACT 1280x600 dimensions and viewBox
- EXACT layout, geometry, cards, borders, glow, gradients, filters
- EXACT fonts and CSS animation keyframes (drop, sway, foil, fadeUp, pulse, ring)
- EXACT swinging lanyard physics and holographic foil
- EXACT card structure (4 KPI cards, Most-Starred Projects, Community, Building/Exploring/Fuel)
Modifies ONLY:
- Replaces Megha's data with Subhajit's verified data
- Replaces Instagram icon with official LinkedIn logo (identical geometry and position)
- Replaces Megha's photo with Subhajit's authentic cropped profile photo
"""

import base64
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
REF_SVG_PATH = ROOT_DIR / "reference-base/id-dashboard.svg"
PHOTO_PATH = ROOT_DIR / "assets/avatar/icard-cropped.jpg"
OUTPUT_SVG = ROOT_DIR / "assets/id-dashboard.svg"
PROFILE_REPO_OUTPUT = ROOT_DIR / "profile-repo/assets/id-dashboard.svg"
METRICS_BANNER = ROOT_DIR / "assets/metrics-banner.svg"

def get_photo_b64() -> str:
    if not PHOTO_PATH.exists():
        raise FileNotFoundError(f"Cropped profile photo not found at {PHOTO_PATH}")
    with open(PHOTO_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def adapt_dashboard():
    print(f"📖 Reading original reference SVG: {REF_SVG_PATH}...")
    with open(REF_SVG_PATH, "r", encoding="utf-8") as f:
        svg = f.read()

    photo_b64 = get_photo_b64()

    # 1. Update Title & Desc
    svg = svg.replace(
        '<title>Developer ID and dashboard</title>',
        '<title>Developer ID and dashboard — Subhajit Kar</title>'
    )
    svg = svg.replace(
        '<desc>A swinging holographic ID badge beside a dashboard: repos, stars, forks, followers, most-starred projects, community reach and current focus.</desc>',
        '<desc>Developer ID badge and dashboard for Subhajit Kar: public repos, stars, forks, followers, most-starred projects, LinkedIn community reach, and current focus.</desc>'
    )

    # 2. Update Lanyard strap text
    svg = svg.replace(
        'MEGHA.DEV &#183; FRONTEND &#183; MEGHA.DEV &#183; FRONTEND',
        'SUBHAJIT.DEV &#183; ARCHITECT &#183; SUBHAJIT.DEV &#183; ARCHITECT'
    )

    # 3. Update ID Card photo
    # Look for <image x="144" y="204" width="136" height="168" href="data:image/jpeg;base64,..."/>
    img_pattern = re.compile(r'<image\s+x="144"\s+y="204"\s+width="136"\s+height="168"[^>]*/>')
    match = img_pattern.search(svg)
    if not match:
        raise ValueError("Could not find ID card <image> tag in reference SVG!")
    
    new_image_tag = f'<image x="144" y="204" width="136" height="168" preserveAspectRatio="xMidYMin slice" href="data:image/jpeg;base64,{photo_b64}"/>'
    svg = img_pattern.sub(new_image_tag, svg)

    # 4. Update ID Card identity fields
    # Name
    svg = svg.replace(
        '<text class="sg" x="212.0" y="412" font-size="25" fill="#eceef6" text-anchor="middle">Megha Mittal</text>',
        '<text class="sg" x="212.0" y="412" font-size="25" fill="#eceef6" text-anchor="middle">Subhajit Kar</text>'
    )
    # Role / Title
    svg = svg.replace(
        '<text class="jb" x="212.0" y="434" font-size="12" fill="#a78bfa" text-anchor="middle" letter-spacing="1.6">FRONTEND DEVELOPER</text>',
        '<text class="jb" x="212.0" y="434" font-size="11" fill="#a78bfa" text-anchor="middle" letter-spacing="1.4">LEAD IAM &amp; SRA ARCHITECT</text>'
    )
    # Location Base
    svg = svg.replace(
        '<text class="sgm" x="82" y="478" font-size="13" fill="#eceef6">Noida, IN</text>',
        '<text class="sgm" x="82" y="478" font-size="13" fill="#eceef6">Kolkata, IN</text>'
    )
    # Team (Zero Deloitte on icard)
    svg = svg.replace(
        '<text class="sgm" x="222" y="478" font-size="13" fill="#eceef6">Wiley</text>',
        '<text class="sgm" x="222" y="478" font-size="13" fill="#eceef6">Cyber &amp; IGA</text>'
    )
    # ID code
    svg = svg.replace(
        '<text class="sgm" x="82" y="508" font-size="13" fill="#eceef6">MM-0920</text>',
        '<text class="sgm" x="82" y="508" font-size="13" fill="#eceef6">SK-IAM-9208</text>'
    )
    # Since year
    svg = svg.replace(
        '<text class="sgm" x="222" y="508" font-size="13" fill="#eceef6">2022</text>',
        '<text class="sgm" x="222" y="508" font-size="13" fill="#eceef6">2021</text>'
    )
    # Handle
    svg = svg.replace(
        '<text class="jb" x="344" y="564" font-size="9.5" fill="#8d93ab" text-anchor="end">@Meghamittal0920</text>',
        '<text class="jb" x="344" y="564" font-size="9.5" fill="#8d93ab" text-anchor="end">@ha4kerspidersks</text>'
    )

    # 5. Top 4 KPI Cards
    # Card 1: 300K+ / IDENTITIES / MO (Scale)
    old_repos = '<text class="sg" x="438.0" y="188" font-size="36" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.4762;0.5810" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="36" fill="#eceef6" opacity="0">2<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5810;0.6857" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="36" fill="#eceef6" opacity="0">4<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6857;0.7905" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="36" fill="#eceef6" opacity="0">6<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7905;0.8952" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="36" fill="#eceef6" opacity="1">8<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8952" dur="2.10s" begin="0s" fill="freeze"/></text>'
    new_repos = '<text class="sg" x="438.0" y="188" font-size="34" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.4762;0.5810" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="34" fill="#eceef6" opacity="0">50K<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5810;0.6857" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="34" fill="#eceef6" opacity="0">120K<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6857;0.7905" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="34" fill="#eceef6" opacity="0">250K<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7905;0.8952" dur="2.10s" begin="0s" fill="freeze"/></text><text class="sg" x="438.0" y="188" font-size="34" fill="#eceef6" opacity="1">300K+<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8952" dur="2.10s" begin="0s" fill="freeze"/></text>'
    svg = svg.replace(old_repos, new_repos)

    old_repos_label = '<text class="jb" x="438.0" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.6">PUBLIC REPOS</text>'
    new_repos_label = '<text class="jb" x="438.0" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.4">IDENTITIES / MO</text>'
    svg = svg.replace(old_repos_label, new_repos_label)

    # Card 2: 80–90% / DEFECT REDUCTION (Impact)
    old_stars = '<text class="sg" x="646.5" y="188" font-size="36" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5045;0.6036" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="36" fill="#eceef6" opacity="0">13<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6036;0.7027" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="36" fill="#eceef6" opacity="0">27<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7027;0.8018" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="36" fill="#eceef6" opacity="0">43<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.8018;0.9009" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="36" fill="#eceef6" opacity="1">54<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.9009" dur="2.22s" begin="0s" fill="freeze"/></text>'
    new_stars = '<text class="sg" x="646.5" y="188" font-size="32" fill="#eceef6" opacity="0">0%<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5045;0.6036" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="32" fill="#eceef6" opacity="0">35%<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6036;0.7027" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="32" fill="#eceef6" opacity="0">60%<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7027;0.8018" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="32" fill="#eceef6" opacity="0">80%<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.8018;0.9009" dur="2.22s" begin="0s" fill="freeze"/></text><text class="sg" x="646.5" y="188" font-size="32" fill="#eceef6" opacity="1">80–90%<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.9009" dur="2.22s" begin="0s" fill="freeze"/></text>'
    svg = svg.replace(old_stars, new_stars)

    old_stars_label = '<text class="jb" x="646.5" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.6">TOTAL STARS</text>'
    new_stars_label = '<text class="jb" x="646.5" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.2">DEFECT REDUCTION</text>'
    svg = svg.replace(old_stars_label, new_stars_label)

    # Card 3: 250+ / SERVICENOW RITMs (Delivery)
    old_forks = '<text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5299;0.6239" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">5<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6239;0.7179" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">11<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7179;0.8120" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">18<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.8120;0.9060" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="1">23<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.9060" dur="2.34s" begin="0s" fill="freeze"/></text>'
    new_forks = '<text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5299;0.6239" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">50<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6239;0.7179" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">120<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7179;0.8120" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="0">200<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.8120;0.9060" dur="2.34s" begin="0s" fill="freeze"/></text><text class="sg" x="855.0" y="188" font-size="36" fill="#eceef6" opacity="1">250+<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.9060" dur="2.34s" begin="0s" fill="freeze"/></text>'
    svg = svg.replace(old_forks, new_forks)

    old_forks_label = '<text class="jb" x="855.0" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.6">FORKS</text>'
    new_forks_label = '<text class="jb" x="855.0" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.2">SERVICENOW RITMs</text>'
    svg = svg.replace(old_forks_label, new_forks_label)

    # Card 4: 56 / TECHNOLOGIES (Breadth)
    old_followers = '<text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5528;0.6423" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">6<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6423;0.7317" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">12<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7317;0.8211" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">20<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.8211;0.9106" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="1">25<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.9106" dur="2.46s" begin="0s" fill="freeze"/></text>'
    new_followers = '<text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">0<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.5528;0.6423" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">14<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.6423;0.7317" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">32<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.7317;0.8211" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="0">48<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.8211;0.9106" dur="2.46s" begin="0s" fill="freeze"/></text><text class="sg" x="1063.5" y="188" font-size="36" fill="#eceef6" opacity="1">56<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.9106" dur="2.46s" begin="0s" fill="freeze"/></text>'
    svg = svg.replace(old_followers, new_followers)

    old_followers_label = '<text class="jb" x="1063.5" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.6">FOLLOWERS</text>'
    new_followers_label = '<text class="jb" x="1063.5" y="208" font-size="10.5" fill="#8d93ab" letter-spacing="1.4">TECHNOLOGIES</text>'
    svg = svg.replace(old_followers_label, new_followers_label)

    # 6. Panel: MOST-STARRED PROJECTS -> KEY ACHIEVEMENTS (Distinct Operational Governance & Impact Metrics)
    svg = svg.replace(
        '<text class="jbb" x="442" y="272" font-size="11" fill="#8d93ab" letter-spacing="1.6">MOST-STARRED PROJECTS</text>',
        '<text class="jbb" x="442" y="272" font-size="11" fill="#8d93ab" letter-spacing="1.6">KEY ACHIEVEMENTS</text>'
    )

    # Row 1: Global Regions -> 9
    svg = svg.replace('Naruto — Sage Mode', 'Global Regions')
    # Row 2: JML Acceleration -> 30–40%
    svg = svg.replace('Zoro — King of Hell', 'JML Acceleration')
    # Row 3: Exception Drop -> 20–30%
    svg = svg.replace('Demon Slayer', 'Exception Drop')
    # Row 4: Test Coverage -> 90%
    svg = svg.replace('JJK — Sukuna', 'Test Coverage')
    # Row 5: Deloitte Awards -> 13
    svg = svg.replace('One Piece 3D', 'Deloitte Awards')

    # Subtitle
    svg = svg.replace(
        'stars per repository &#183; anime web builds',
        'verified enterprise impact &#183; cybersecurity &amp; identity'
    )

    # Project bar widths and counts (visualizing achievement values across 5 descending rows):
    # Row 1: Global Regions Governed (width 210.0, 100%, count 9)
    svg = svg.replace(
        '<rect x="592" y="300" width="210.0" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;210.0" keyTimes="0;0.6087;1" dur="2.30s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="812" y="311" font-size="12" fill="#eceef6" opacity="1">25<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8800" dur="2.50s" begin="0s" fill="freeze"/></text>',
        '<rect x="592" y="300" width="210.0" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;210.0" keyTimes="0;0.6087;1" dur="2.30s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="812" y="311" font-size="12" fill="#eceef6" opacity="1">9<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8800" dur="2.50s" begin="0s" fill="freeze"/></text>'
    )
    # Row 2: JML SLA Acceleration (width 178.5, 85%, count 30–40%)
    svg = svg.replace(
        '<rect x="592" y="334" width="75.6" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;75.6" keyTimes="0;0.6281;1" dur="2.42s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="678" y="345" font-size="12" fill="#eceef6" opacity="1">9<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8855" dur="2.62s" begin="0s" fill="freeze"/></text>',
        '<rect x="592" y="334" width="178.5" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;178.5" keyTimes="0;0.6281;1" dur="2.42s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="812" y="345" font-size="12" fill="#eceef6" opacity="1">30–40%<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8855" dur="2.62s" begin="0s" fill="freeze"/></text>'
    )
    # Row 3: Access Exception Drop (width 147.0, 70%, count 20–30%)
    svg = svg.replace(
        '<rect x="592" y="368" width="67.2" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;67.2" keyTimes="0;0.6457;1" dur="2.54s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="669" y="379" font-size="12" fill="#eceef6" opacity="1">8<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8905" dur="2.74s" begin="0s" fill="freeze"/></text>',
        '<rect x="592" y="368" width="147.0" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;147.0" keyTimes="0;0.6457;1" dur="2.54s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="812" y="379" font-size="12" fill="#eceef6" opacity="1">20–30%<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8905" dur="2.74s" begin="0s" fill="freeze"/></text>'
    )
    # Row 4: Automated Test Coverage (width 117.6, 56%, count 90%)
    svg = svg.replace(
        '<rect x="592" y="402" width="67.2" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;67.2" keyTimes="0;0.6617;1" dur="2.66s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="669" y="413" font-size="12" fill="#eceef6" opacity="1">8<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8951" dur="2.86s" begin="0s" fill="freeze"/></text>',
        '<rect x="592" y="402" width="117.6" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;117.6" keyTimes="0;0.6617;1" dur="2.66s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="812" y="413" font-size="12" fill="#eceef6" opacity="1">90%<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8951" dur="2.86s" begin="0s" fill="freeze"/></text>'
    )
    # Row 5: Deloitte Awards & Badges (width 73.5, 35%, count 13)
    svg = svg.replace(
        '<rect x="592" y="436" width="16.8" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;16.8" keyTimes="0;0.6763;1" dur="2.78s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="619" y="447" font-size="12" fill="#eceef6" opacity="1">2<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8993" dur="2.98s" begin="0s" fill="freeze"/></text>',
        '<rect x="592" y="436" width="73.5" height="14" rx="7" fill="url(#barG)"><animate attributeName="width" values="0;0;73.5" keyTimes="0;0.6763;1" dur="2.78s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect><text class="jbb" x="812" y="447" font-size="12" fill="#eceef6" opacity="1">13<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8993" dur="2.98s" begin="0s" fill="freeze"/></text>'
    )

    # 7. COMMUNITY Card: Instagram -> LinkedIn
    # Replace Instagram icon with LinkedIn logo
    old_ig_pattern = re.compile(r'<g transform="translate\(936,268\) scale\(\.72\)" style="color:#f472b6"><path fill="#f472b6" d="[^"]*"/></g>')
    linkedin_path = "M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.45a1.62 1.62 0 1 0 0 3.24 1.62 1.62 0 0 0 0-3.24Z"
    new_li_icon = f'<g transform="translate(936,268) scale(.72)" style="color:#0a66c2"><path fill="#0a66c2" d="{linkedin_path}"/></g>'
    svg = old_ig_pattern.sub(new_li_icon, svg)

    # Community labels & numbers:
    # 4.7K / IG FOLLOWERS -> 10K / LI FOLLOWERS
    svg = svg.replace(
        '<text class="sg" x="936" y="322" font-size="30" fill="#eceef6">4.7K</text>',
        '<text class="sg" x="936" y="322" font-size="30" fill="#eceef6">10K</text>'
    )
    svg = svg.replace(
        '<text class="jb" x="936" y="342" font-size="10.5" fill="#8d93ab" letter-spacing="1.3">IG FOLLOWERS</text>',
        '<text class="jb" x="936" y="342" font-size="10.5" fill="#8d93ab" letter-spacing="1.3">LI FOLLOWERS</text>'
    )
    # 2.7M / VIEWS / 30 DAYS -> 15K / VIEWS / 30 DAYS
    svg = svg.replace(
        '<text class="sg" x="1074" y="322" font-size="30" fill="#eceef6">2.7M</text>',
        '<text class="sg" x="1074" y="322" font-size="30" fill="#eceef6">15K</text>'
    )
    # Handle: @meghamittal92000 -> @subhajit-kar
    svg = svg.replace(
        '<text class="jb" x="936" y="368" font-size="10" fill="#8d93ab" opacity=".8">@meghamittal92000</text>',
        '<text class="jb" x="936" y="368" font-size="10" fill="#8d93ab" opacity=".8">@subhajit-kar</text>'
    )

    # 8. BUILDING / EXPLORING / FOCUS Card
    svg = svg.replace(
        '<text class="sgm" x="952" y="452" font-size="13" fill="#eceef6">Cinematic anime web experiences</text>',
        '<text class="sgm" x="952" y="452" font-size="13" fill="#eceef6">Enterprise IAM &amp; IGA Architecture</text>'
    )
    svg = svg.replace(
        '<text class="sgm" x="952" y="492" font-size="13" fill="#eceef6">3D on the web &amp; AI pair-programming</text>',
        '<text class="sgm" x="952" y="492" font-size="13" fill="#eceef6">Agentic AI &amp; Identity Governance</text>'
    )
    svg = svg.replace(
        '<text class="jbb" x="952" y="514" font-size="9.5" fill="#f472b6" letter-spacing="1.6">FUEL</text>',
        '<text class="jbb" x="952" y="514" font-size="9.5" fill="#f472b6" letter-spacing="1.6">FOCUS</text>'
    )
    svg = svg.replace(
        '<text class="sgm" x="952" y="532" font-size="13" fill="#eceef6">Coffee, ramen &amp; morning runs</text>',
        '<text class="sgm" x="952" y="532" font-size="13" fill="#eceef6">Zero-Trust &amp; Security Automation</text>'
    )

    # Validate XML parsing
    try:
        ET.fromstring(svg)
        print("✅ XML structure is 100% valid!")
    except ET.ParseError as e:
        print(f"❌ XML Parse Error: {e}")
        raise

    # Write output to assets/id-dashboard.svg
    OUTPUT_SVG.write_text(svg, encoding="utf-8")
    print(f"✅ Written adapted dashboard to {OUTPUT_SVG}")

    # Write output to profile-repo/assets/id-dashboard.svg
    PROFILE_REPO_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PROFILE_REPO_OUTPUT.write_text(svg, encoding="utf-8")
    print(f"✅ Written adapted dashboard to {PROFILE_REPO_OUTPUT}")

    # Write to metrics-banner.svg if exists
    if METRICS_BANNER.exists():
        METRICS_BANNER.write_text(svg, encoding="utf-8")
        print(f"✅ Synchronized to {METRICS_BANNER}")

if __name__ == "__main__":
    adapt_dashboard()
