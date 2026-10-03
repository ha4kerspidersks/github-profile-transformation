#!/usr/bin/env python3
"""
Generate Reference-Faithful Professional Dashboard (assets/id-dashboard.svg).
1280x600 SVG featuring:
- Left: Swinging Reference-Exact Lanyard ID Card with:
  * User-provided authentic desk portrait (base64 encoded)
  * Orbiting glowing white dot around photo frame
  * Smart chip, RFID indicator, barcode
  * ZERO mention of Deloitte on the icard
- Right: Executive telemetry dashboard with verified KPI metrics (300K+ identities, 13 awards, 3+ yrs exp, 56 engines)
- Exact reference palette (#0d0e16, #a78bfa, #22d3ee, #34d399, #fbbf24, #262a42, #eceef6, #8d93ab)
- Embedded reference WOFF2 fonts
- Physical drop and swaying lanyard animation
"""

import sys
import base64
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))
from shared_svg_fonts import SHARED_FONTS

DASHBOARD_OUTPUT_SVG = ROOT_DIR / "assets/id-dashboard.svg"
METRICS_BANNER_SVG = ROOT_DIR / "assets/metrics-banner.svg"
ICARD_PHOTO_PATH = ROOT_DIR / "assets/avatar/icard-cropped.jpg"

def get_icard_photo_b64():
    if not ICARD_PHOTO_PATH.exists():
        raise FileNotFoundError(f"Cropped icard photo not found at {ICARD_PHOTO_PATH}")
    with open(ICARD_PHOTO_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def generate_reference_dashboard():
    print("📊 Generating reference-faithful id-dashboard.svg with user photo & zero Deloitte on icard...")
    photo_b64 = get_icard_photo_b64()

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 600" width="1280" height="600" role="img" aria-label="Developer ID and Dashboard — Subhajit Kar"><title>Developer ID and Dashboard — Subhajit Kar</title><desc>Swinging Zero-Trust Clearance Smartcard with authentic portrait on the left, executive metrics and credential breakdown on the right.</desc><defs><style>{SHARED_FONTS}
text{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.sg{{font-family:'SG','Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}}
.sgm{{font-family:'SGM','Segoe UI',Helvetica,Arial,sans-serif;font-weight:500}}
.jb{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.jbb{{font-family:'JBMB',ui-monospace,Menlo,Consolas,monospace;font-weight:700}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

.swing{{transform-box:view-box;transform-origin:212px -30px;animation:drop 2.6s cubic-bezier(.3,1,.5,1) forwards, sway 6s ease-in-out 2.6s infinite}}
@keyframes drop{{0%{{transform:translateY(-640px) rotate(0deg)}}22%{{transform:translateY(0) rotate(0deg)}}42%{{transform:rotate(3.4deg)}}62%{{transform:rotate(-2.2deg)}}80%{{transform:rotate(1.2deg)}}100%{{transform:rotate(0deg)}}}}
@keyframes sway{{0%,100%{{transform:rotate(-1.9deg)}}50%{{transform:rotate(1.9deg)}}}}
.foil{{animation:foil 6s ease-in-out infinite}}
@keyframes foil{{0%{{transform:translateX(-320px)}}55%,100%{{transform:translateX(360px)}}}}
.fu{{animation:fadeUp .7s cubic-bezier(.2,.8,.2,1) both}}
.fi{{animation:fadeIn .7s ease both}}
.tile{{animation:fadeUp .7s cubic-bezier(.2,.8,.2,1) both}}

@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}
</style>

<linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#141829"/>
  <stop offset="100%" stop-color="#0d0e16"/>
</linearGradient>

<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#a78bfa" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#22d3ee" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#262a42" stop-opacity=".8"/>
</linearGradient>

<linearGradient id="strapG" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#7c3aed"/>
  <stop offset=".5" stop-color="#f472b6"/>
  <stop offset="1" stop-color="#7c3aed"/>
</linearGradient>

<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#d7dbe6"/>
  <stop offset=".45" stop-color="#8c93a6"/>
  <stop offset=".55" stop-color="#6b7280"/>
  <stop offset="1" stop-color="#aab1c2"/>
</linearGradient>

<linearGradient id="idbg" x1="0" y1="0" x2=".6" y2="1">
  <stop offset="0" stop-color="#1b2140"/>
  <stop offset=".55" stop-color="#141829"/>
  <stop offset="1" stop-color="#191330"/>
</linearGradient>

<linearGradient id="ringG" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#22d3ee"/>
  <stop offset=".5" stop-color="#a78bfa"/>
  <stop offset="1" stop-color="#f472b6"/>
</linearGradient>

<linearGradient id="chipG" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#fde68a"/>
  <stop offset="1" stop-color="#d6a13a"/>
</linearGradient>

<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
  <circle cx="11" cy="11" r=".8" fill="#ffffff" fill-opacity=".05"/>
</pattern>

<clipPath id="idClip"><rect x="56" y="150" width="312" height="424" rx="22"/></clipPath>
<clipPath id="photoClip"><rect x="144" y="204" width="136" height="168" rx="16"/></clipPath>
<filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
  <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#000" flood-opacity=".55"/>
</filter>
</defs>

<!-- Outer Container Frame matching Reference -->
<rect width="1280" height="600" rx="24" fill="url(#cardbg)"/>
<rect width="1280" height="600" rx="24" fill="url(#dots)"/>
<rect x=".75" y=".75" width="1278.5" height="598.5" rx="23.25" fill="none" stroke="url(#edge)" stroke-width="1.5"/>

<!-- ========================================== -->
<!-- LEFT: SWINGING LANYARD ICARD WITH PHOTO    -->
<!-- (ZERO MENTION OF DELOITTE ON ICARD)        -->
<!-- ========================================== -->
<g class="swing">
  <!-- Lanyard Strap -->
  <path d="M192 -40 L232 -40 L229 104 L195 104 Z" fill="url(#strapG)"/>
  <text class="jbb" font-size="9" fill="#fff" fill-opacity=".85" letter-spacing="2.4" transform="translate(216,-30) rotate(90)">SUBHAJIT.DEV &#183; ZERO TRUST &#183; SUBHAJIT.DEV &#183; IAM</text>
  <!-- Metallic Buckle & Ring -->
  <rect x="186" y="102" width="52" height="24" rx="6" fill="url(#metal)"/>
  <rect x="200" y="108" width="24" height="7" rx="3.5" fill="#39405020"/>
  <circle cx="212" cy="140" r="13" fill="none" stroke="url(#metal)" stroke-width="5"/>

  <!-- Card Body with Drop Shadow -->
  <g filter="url(#shadow)">
    <rect x="56" y="150" width="312" height="424" rx="22" fill="url(#idbg)" stroke="url(#ringG)" stroke-opacity=".55" stroke-width="1.5"/>
  </g>

  <!-- Card Content with idClip -->
  <g clip-path="url(#idClip)">
    <rect x="56" y="150" width="312" height="424" fill="url(#dots)"/>
    <rect x="56" y="150" width="312" height="34" fill="#ffffff" fill-opacity=".04"/>
    <!-- Top Header on Card: ZERO DELOITTE -->
    <text class="jbb" x="76" y="172" font-size="10.5" fill="#22d3ee" letter-spacing="2">SECURITY ID</text>
    <text class="jb" x="348" y="172" font-size="10.5" fill="#8d93ab" text-anchor="end" letter-spacing="1.4">v2.0</text>

    <!-- Photo Frame with Glowing Orbiting White Dot -->
    <rect id="pframe" x="140" y="200" width="144" height="176" rx="20" fill="none" stroke="url(#ringG)" stroke-opacity=".75" stroke-width="2"/>
    <path id="ppath" d="M140 220v136a20 20 0 0 0 20 20h104a20 20 0 0 0 20-20V70a20 20 0 0 0-20-20H160a20 20 0 0 0-20 20z" fill="none"/>
    <circle r="3.4" fill="#fff"><animateMotion dur="7s" repeatCount="indefinite"><mpath href="#ppath"/></animateMotion></circle>

    <!-- USER-UPLOADED AUTHENTIC DESK PORTRAIT (CLIPPED) -->
    <g clip-path="url(#photoClip)">
      <image x="144" y="204" width="136" height="168" href="data:image/jpeg;base64,{photo_b64}" preserveAspectRatio="xMidYMin slice"/>
    </g>

    <!-- Golden Smart Chip -->
    <rect x="80" y="212" width="34" height="26" rx="5" fill="url(#chipG)"/>
    <path d="M80 221h34M97 212v26" stroke="#8a6a1e" stroke-width="1" stroke-opacity=".6"/>

    <!-- RFID Waves -->
    <g stroke="#34d399" stroke-width="1.6" fill="none" opacity=".9" transform="translate(310,226)">
      <path d="M0-8a11 11 0 0 1 0 16"/><path d="M-5-5a6.5 6.5 0 0 1 0 10"/><circle cx="-9" cy="0" r="1.6" fill="#34d399" stroke="none"/>
    </g>

    <!-- Name & Role (NO DELOITTE) -->
    <text class="sg" x="212.0" y="412" font-size="25" fill="#eceef6" text-anchor="middle">Subhajit Kar</text>
    <text class="jb" x="212.0" y="434" font-size="12" fill="#22d3ee" text-anchor="middle" letter-spacing="1.6">SENIOR IAM MANAGER</text>

    <!-- Divider Line -->
    <line x1="82" y1="450" x2="342" y2="450" stroke="#262a42"/>

    <!-- Metadata Grid (NO DELOITTE) -->
    <text class="jb" x="82" y="462" font-size="9.5" fill="#8d93ab" letter-spacing="1.6">BASE</text>
    <text class="sgm" x="82" y="478" font-size="13" fill="#eceef6">BLR / CCU, IN</text>
    <text class="jb" x="222" y="462" font-size="9.5" fill="#8d93ab" letter-spacing="1.6">DOMAIN</text>
    <text class="sgm" x="222" y="478" font-size="13" fill="#eceef6">Cyber &amp; IGA</text>

    <text class="jb" x="82" y="494" font-size="9.5" fill="#8d93ab" letter-spacing="1.6">ID</text>
    <text class="sgm" x="82" y="510" font-size="13" fill="#eceef6">SK-IAM-9208</text>
    <text class="jb" x="222" y="494" font-size="9.5" fill="#8d93ab" letter-spacing="1.6">CLEARANCE</text>
    <text class="sgm" x="222" y="510" font-size="13" fill="#34d399">ZERO TRUST</text>

    <!-- Barcode Strip (NO DELOITTE) -->
    <g transform="translate(82, 526)">
      <path d="M0 0v16M4 0v16M10 0v16M14 0v16M20 0v16M26 0v16M30 0v16M38 0v16M44 0v16M50 0v16M56 0v16M64 0v16M70 0v16M76 0v16M84 0v16M90 0v16M98 0v16M104 0v16M110 0v16M118 0v16M124 0v16M130 0v16M138 0v16M144 0v16M152 0v16M160 0v16M168 0v16M176 0v16M184 0v16M192 0v16M202 0v16M210 0v16M218 0v16M226 0v16M234 0v16M242 0v16M250 0v16M258 0v16" stroke="#22d3ee" stroke-width="1.6" opacity=".65"/>
    </g>

    <!-- Holographic Diagonal Sheen -->
    <g class="foil" opacity=".18">
      <polygon points="0,150 70,150 160,574 90,574" fill="url(#ringG)"/>
    </g>
  </g>
</g>

<!-- ========================================== -->
<!-- RIGHT: EXECUTIVE DASHBOARD & METRICS       -->
<!-- ========================================== -->
<g class="fu" style="animation-delay:.15s">
  <text class="jbb" x="420" y="54" font-size="12.5" fill="#a78bfa" letter-spacing="2.2">// ENTERPRISE DASHBOARD</text>
  <text class="sg" x="420" y="94" font-size="29" fill="#eceef6" letter-spacing="-.5">Profile at a glance</text>

  <!-- Live Status Badge matching Reference -->
  <g transform="translate(1090,70)">
    <rect x="0" y="-18" width="150" height="28" rx="14" fill="#34d399" fill-opacity=".1" stroke="#34d399" stroke-opacity=".4"/>
    <circle cx="16" cy="-4" r="4" fill="#34d399"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
    <text class="jbb" x="28" y="0" font-size="10" fill="#34d399" letter-spacing="1.2">LIVE &#183; GITHUB</text>
  </g>
</g>

<!-- 4 TOP KPI TILES -->
<!-- Tile 1: 300K+ Identities -->
<g class="tile" style="animation-delay:.3s">
  <rect x="420" y="126" width="190" height="96" rx="16" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="438" y="140" width="22" height="3" rx="1.5" fill="#22d3ee"/>
  <!-- Animated Rolling Counter -->
  <text class="sg" x="438" y="186" font-size="34" fill="#eceef6">300K+</text>
  <text class="jb" x="438" y="208" font-size="10" fill="#8d93ab" letter-spacing="1.4">IDENTITIES SECURED</text>
</g>

<!-- Tile 2: 13 Excellence Awards -->
<g class="tile" style="animation-delay:.4s">
  <rect x="628" y="126" width="190" height="96" rx="16" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="646" y="140" width="22" height="3" rx="1.5" fill="#fbbf24"/>
  <text class="sg" x="646" y="186" font-size="34" fill="#eceef6">13</text>
  <text class="jb" x="646" y="208" font-size="10" fill="#8d93ab" letter-spacing="1.4">EXCELLENCE AWARDS</text>
</g>

<!-- Tile 3: 3+ Years Exp -->
<g class="tile" style="animation-delay:.5s">
  <rect x="836" y="126" width="190" height="96" rx="16" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="854" y="140" width="22" height="3" rx="1.5" fill="#a78bfa"/>
  <text class="sg" x="854" y="186" font-size="34" fill="#eceef6">3+ YRS</text>
  <text class="jb" x="854" y="208" font-size="10" fill="#8d93ab" letter-spacing="1.4">IAM LEADERSHIP</text>
</g>

<!-- Tile 4: 56 Verified Engines -->
<g class="tile" style="animation-delay:.6s">
  <rect x="1044" y="126" width="196" height="96" rx="16" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="1062" y="140" width="22" height="3" rx="1.5" fill="#34d399"/>
  <text class="sg" x="1062" y="186" font-size="34" fill="#eceef6">56</text>
  <text class="jb" x="1062" y="208" font-size="10" fill="#8d93ab" letter-spacing="1.4">VERIFIED ENGINES</text>
</g>

<!-- BOTTOM BREAKDOWN CONTAINERS -->
<!-- Container L: Credentials & Impact (x=420, y=242, w=398, h=314) -->
<g class="fu" style="animation-delay:.7s">
  <rect x="420" y="242" width="398" height="314" rx="18" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <text class="jbb" x="444" y="274" font-size="11.5" fill="#22d3ee" letter-spacing="1.8">// CREDENTIALS &amp; GOVERNANCE</text>

  <!-- Item 1 -->
  <g transform="translate(444, 292)">
    <circle cx="6" cy="14" r="3" fill="#22d3ee"/>
    <text class="sg" x="20" y="18" font-size="14.5" fill="#eceef6">Enterprise Identity Governance</text>
    <text class="jb" x="20" y="34" font-size="11" fill="#8d93ab">Senior IAM Manager &#183; Saviynt &amp; Cloud IGA</text>
  </g>

  <!-- Item 2 -->
  <g transform="translate(444, 348)">
    <circle cx="6" cy="14" r="3" fill="#a78bfa"/>
    <text class="sg" x="20" y="18" font-size="14.5" fill="#eceef6">NFSU M.Tech in Cyber Security</text>
    <text class="jb" x="20" y="34" font-size="11" fill="#8d93ab">National Forensic Sciences University &#183; Post-Grad</text>
  </g>

  <!-- Item 3 -->
  <g transform="translate(444, 404)">
    <circle cx="6" cy="14" r="3" fill="#34d399"/>
    <text class="sg" x="20" y="18" font-size="14.5" fill="#eceef6">IEM B.Tech in Electronics &amp; Comm</text>
    <text class="jb" x="20" y="34" font-size="11" fill="#8d93ab">Institute of Engineering &amp; Management &#183; Honors</text>
  </g>

  <!-- Item 4 -->
  <g transform="translate(444, 460)">
    <circle cx="6" cy="14" r="3" fill="#fbbf24"/>
    <text class="sg" x="20" y="18" font-size="14.5" fill="#eceef6">13 Industry &amp; Firm-Wide Honors</text>
    <text class="jb" x="20" y="34" font-size="11" fill="#8d93ab">Applause, Spot &amp; Special Recognition Awards</text>
  </g>
</g>

<!-- Container R: Architecture Telemetry (x=836, y=242, w=404, h=314) -->
<g class="fu" style="animation-delay:.8s">
  <rect x="836" y="242" width="404" height="314" rx="18" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <text class="jbb" x="860" y="274" font-size="11.5" fill="#a78bfa" letter-spacing="1.8">// ENTERPRISE PIPELINE TELEMETRY</text>

  <!-- Bar 1: JML Automation SLA -->
  <g transform="translate(860, 296)">
    <text class="sgm" x="0" y="14" font-size="13" fill="#eceef6">JML Pipeline Automation</text>
    <text class="jb" x="350" y="14" font-size="12" fill="#22d3ee" text-anchor="end">99.98%</text>
    <rect x="0" y="24" width="350" height="8" rx="4" fill="#0f1224"/>
    <rect x="0" y="24" width="345" height="8" rx="4" fill="#22d3ee"/>
  </g>

  <!-- Bar 2: Reconciliation Accuracy -->
  <g transform="translate(860, 350)">
    <text class="sgm" x="0" y="14" font-size="13" fill="#eceef6">Monthly Reconciliation Accuracy</text>
    <text class="jb" x="350" y="14" font-size="12" fill="#a78bfa" text-anchor="end">100.00%</text>
    <rect x="0" y="24" width="350" height="8" rx="4" fill="#0f1224"/>
    <rect x="0" y="24" width="350" height="8" rx="4" fill="#a78bfa"/>
  </g>

  <!-- Bar 3: Defect Reduction -->
  <g transform="translate(860, 404)">
    <text class="sgm" x="0" y="14" font-size="13" fill="#eceef6">Defect Reduction in Production</text>
    <text class="jb" x="350" y="14" font-size="12" fill="#34d399" text-anchor="end">85-90%</text>
    <rect x="0" y="24" width="350" height="8" rx="4" fill="#0f1224"/>
    <rect x="0" y="24" width="305" height="8" rx="4" fill="#34d399"/>
  </g>

  <!-- Telemetry System Tag -->
  <g transform="translate(860, 468)">
    <rect x="0" y="0" width="350" height="48" rx="10" fill="#0f1224" stroke="#262a42" stroke-width="1"/>
    <circle cx="20" cy="24" r="4" fill="#34d399"><animate attributeName="opacity" values="1;.3;1" dur="1.4s" repeatCount="indefinite"/></circle>
    <text class="jbb" x="34" y="21" font-size="10.5" fill="#eceef6">ZERO DRIFT ARCHITECTURE</text>
    <text class="jb" x="34" y="36" font-size="9" fill="#8d93ab">Continuous identity reconciliation across 300K+ objects</text>
  </g>
</g>
</svg>'''

    DASHBOARD_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    with open(DASHBOARD_OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(METRICS_BANNER_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ Generated Reference-Faithful id-dashboard.svg ({len(svg_content) / 1024:.1f} KB)")
    print("   ✓ User photo embedded in icard")
    print("   ✓ Zero mention of Deloitte on icard")
    return True

if __name__ == "__main__":
    generate_reference_dashboard()
