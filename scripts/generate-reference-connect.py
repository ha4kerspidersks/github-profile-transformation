#!/usr/bin/env python3
"""
Generate Reference-Faithful Connect Banner (assets/connect.svg).
1280x470 SVG featuring:
- Left: Glowing floating isometric Zero-Trust Nexus / Cyber Key visual
- Right: // LET'S CONNECT header with 4 interactive connection cards (GitHub, LinkedIn, Email, Portfolio)
- Exact reference palette (#0d0e16, #f472b6, #22d3ee, #a78bfa, #34d399, #262a42, #eceef6, #8d93ab)
- Embedded reference WOFF2 fonts
- Animated stroke highlights and arrow shifts
"""

import sys
import base64
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))
from shared_svg_fonts import SHARED_FONTS

CONNECT_OUTPUT_SVG = ROOT_DIR / "assets/connect.svg"
CHAR_PHOTO_PATH = ROOT_DIR / "assets/avatar/male-character-pointing-opt.jpg"

def generate_reference_connect():
    print("💌 Generating reference-faithful connect.svg (1280x470) with male pointing character...")
    with open(CHAR_PHOTO_PATH, "rb") as f:
        char_b64 = base64.b64encode(f.read()).decode("utf-8")

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 470" width="1280" height="470" role="img" aria-label="Let's Connect — Subhajit Kar"><title>Let's Connect — Subhajit Kar</title><desc>Left: Male cybersecurity engineer pointing to verified contact channels. Right: Communication channels for Subhajit Kar.</desc><defs><style>{SHARED_FONTS}
text{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.sg{{font-family:'SG','Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}}
.sgm{{font-family:'SGM','Segoe UI',Helvetica,Arial,sans-serif;font-weight:500}}
.jb{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.jbb{{font-family:'JBMB',ui-monospace,Menlo,Consolas,monospace;font-weight:700}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes floatAnim{{
  0%,100%{{transform:translateY(0);}}
  50%{{transform:translateY(-12px);}}
}}
@keyframes arrowShift{{
  0%,100%{{transform:translateX(0);}}
  50%{{transform:translateX(6px);}}
}}
.fu{{animation:fadeUp .7s cubic-bezier(.2,.8,.2,1) both}}
.fi{{animation:fadeIn .7s ease both}}
.float{{animation:floatAnim 6s ease-in-out infinite;}}
.arrow{{animation:arrowShift 2.2s ease-in-out infinite;}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}
</style>

<linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#141829"/>
  <stop offset="100%" stop-color="#0d0e16"/>
</linearGradient>

<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#f472b6" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#22d3ee" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#262a42" stop-opacity=".8"/>
</linearGradient>

<radialGradient id="glowNexus" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".25"/>
  <stop offset="50%" stop-color="#a78bfa" stop-opacity=".15"/>
  <stop offset="100%" stop-color="#0d0e16" stop-opacity="0"/>
</radialGradient>

<filter id="blur50" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="50"/>
</filter>

<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
  <circle cx="11" cy="11" r=".8" fill="#ffffff" fill-opacity=".05"/>
</pattern>
</defs>

<!-- Outer Card Frame matching Reference -->
<rect width="1280" height="470" rx="24" fill="url(#cardbg)"/>
<rect width="1280" height="470" rx="24" fill="url(#dots)"/>
<rect x=".75" y=".75" width="1278.5" height="468.5" rx="23.25" fill="none" stroke="url(#edge)" stroke-width="1.5"/>

<!-- ========================================== -->
<!-- LEFT: POINTING MALE CHARACTER VISUAL       -->
<!-- ========================================== -->
<ellipse cx="250" cy="270" rx="190" ry="160" fill="url(#glowNexus)" filter="url(#blur50)"/>
<g class="fu" style="animation-delay:.2s">
  <g class="float">
    <image x="65" y="24" width="370" height="422" href="data:image/jpeg;base64,{char_b64}" preserveAspectRatio="xMidYMid meet"/>
  </g>
</g>

<!-- ========================================== -->
<!-- RIGHT: HEADER & CONNECT CARDS              -->
<!-- ========================================== -->
<g class="fu" style="animation-delay:.3s">
  <text class="jbb" x="470" y="96" font-size="12.5" fill="#f472b6" letter-spacing="2.2">// LET'S CONNECT</text>
  <text class="sg" x="470" y="140" font-size="31" fill="#eceef6" letter-spacing="-.5">Let's build something together</text>
  <text class="sgm" x="470" y="174" font-size="16" fill="#8d93ab">Open to enterprise IAM collaborations, security advisory, and zero-trust discussions.</text>
</g>

<!-- 4 CONNECT CARDS (2x2 Grid) -->

<!-- Card 1: GitHub (x=470, y=216) -->
<g class="tile" style="animation-delay:.4s">
  <rect x="470" y="216" width="378" height="92" rx="18" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="470" y="216" width="378" height="92" rx="18" fill="none" stroke="#22d3ee" stroke-opacity="0">
    <animate attributeName="stroke-opacity" values="0;.75;0;0" keyTimes="0;.06;.2;1" dur="7s" begin="1.0s" repeatCount="indefinite"/>
  </rect>
  <rect x="488" y="238" width="48" height="48" rx="14" fill="#22d3ee" fill-opacity=".12"/>
  <!-- GitHub Icon -->
  <g transform="translate(500,250) scale(1)">
    <path fill="#eceef6" d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
  </g>
  <text class="sg" x="552" y="258" font-size="17" fill="#eceef6">GitHub</text>
  <text class="jb" x="552" y="280" font-size="12.5" fill="#8d93ab">ha4kerspidersks</text>
  <g class="arrow" transform="translate(818,262)">
    <path d="M-6 0h12M2-5l5 5-5 5" fill="none" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</g>

<!-- Card 2: LinkedIn (x=864, y=216) -->
<g class="tile" style="animation-delay:.5s">
  <rect x="864" y="216" width="378" height="92" rx="18" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="864" y="216" width="378" height="92" rx="18" fill="none" stroke="#a78bfa" stroke-opacity="0">
    <animate attributeName="stroke-opacity" values="0;.75;0;0" keyTimes="0;.06;.2;1" dur="7s" begin="2.5s" repeatCount="indefinite"/>
  </rect>
  <rect x="882" y="238" width="48" height="48" rx="14" fill="#a78bfa" fill-opacity=".12"/>
  <!-- LinkedIn Icon -->
  <g transform="translate(894,250) scale(1)">
    <path fill="#eceef6" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
  </g>
  <text class="sg" x="946" y="258" font-size="17" fill="#eceef6">LinkedIn</text>
  <text class="jb" x="946" y="280" font-size="12.5" fill="#8d93ab">subhajit-kar-iam</text>
  <g class="arrow" transform="translate(1212,262)">
    <path d="M-6 0h12M2-5l5 5-5 5" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</g>

<!-- Card 3: Email (x=470, y=324) -->
<g class="tile" style="animation-delay:.6s">
  <rect x="470" y="324" width="378" height="92" rx="18" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="470" y="324" width="378" height="92" rx="18" fill="none" stroke="#f472b6" stroke-opacity="0">
    <animate attributeName="stroke-opacity" values="0;.75;0;0" keyTimes="0;.06;.2;1" dur="7s" begin="4.0s" repeatCount="indefinite"/>
  </rect>
  <rect x="488" y="346" width="48" height="48" rx="14" fill="#f472b6" fill-opacity=".12"/>
  <!-- Email Icon -->
  <g transform="translate(500,358) scale(1)">
    <path fill="#eceef6" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
  </g>
  <text class="sg" x="552" y="366" font-size="17" fill="#eceef6">Email</text>
  <text class="jb" x="552" y="388" font-size="12.5" fill="#8d93ab">subhajit.kar.official@gmail.com</text>
  <g class="arrow" transform="translate(818,370)">
    <path d="M-6 0h12M2-5l5 5-5 5" fill="none" stroke="#f472b6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</g>

<!-- Card 4: Portfolio (x=864, y=324) -->
<g class="tile" style="animation-delay:.7s">
  <rect x="864" y="324" width="378" height="92" rx="18" fill="#ffffff" fill-opacity=".03" stroke="#262a42"/>
  <rect x="864" y="324" width="378" height="92" rx="18" fill="none" stroke="#34d399" stroke-opacity="0">
    <animate attributeName="stroke-opacity" values="0;.75;0;0" keyTimes="0;.06;.2;1" dur="7s" begin="5.5s" repeatCount="indefinite"/>
  </rect>
  <rect x="882" y="346" width="48" height="48" rx="14" fill="#34d399" fill-opacity=".12"/>
  <!-- Globe / Portfolio Icon -->
  <g transform="translate(894,358) scale(1)">
    <path fill="#eceef6" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
  </g>
  <text class="sg" x="946" y="366" font-size="17" fill="#eceef6">Portfolio Website</text>
  <text class="jb" x="946" y="388" font-size="12.5" fill="#8d93ab">subhajitkar.com</text>
  <g class="arrow" transform="translate(1212,370)">
    <path d="M-6 0h12M2-5l5 5-5 5" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</g>
</svg>'''

    CONNECT_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    with open(CONNECT_OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ Generated Reference-Faithful connect.svg ({len(svg_content) / 1024:.1f} KB)")
    return True

if __name__ == "__main__":
    generate_reference_connect()
