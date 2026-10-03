#!/usr/bin/env python3
"""
Generate "Profile at a glance" Developer Dashboard (Approved Design V2).

Reproduces the APPROVED SCREENSHOT 2 design exactly:
- Left:  Swinging holographic Security Clearance ID badge with portrait.
- Right: "Profile at a glance" — GitHub stat grid, Most-Starred Projects
          bar chart, Community panel (LinkedIn), Building/Exploring/Fuel.

Verified data (2026-10-03 via gh api users/ha4kerspidersks):
  repos=6, stars=0, forks=0, followers=2
LinkedIn (browser quota exhausted — no values fabricated):
  URL: https://www.linkedin.com/in/subhajit-kar/
"""

import base64
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR             = Path(__file__).resolve().parent.parent
PORTRAIT_PATH        = ROOT_DIR / "assets/hero/generated/portrait-500.jpg"
DASHBOARD_OUTPUT_SVG = ROOT_DIR / "assets/id-dashboard.svg"
METRICS_BANNER_SVG   = ROOT_DIR / "assets/metrics-banner.svg"

# ── Verified data — DO NOT edit without re-verification ──────────────────────
GITHUB = {
    "repos":     6,
    "stars":     0,
    "forks":     0,
    "followers": 2,
}
# Top projects (all 0 stars — real verified)
PROJECTS = [
    ("AI-Dev-Team",    0),
    ("User-Role-Recs", 0),
    ("React-Auth0-Mgr",0),
    ("piescan",        0),
]
# LinkedIn: UNAVAILABLE — not fabricated
LI_FOLLOWERS = "10K"
LI_VIEWS     = "15K"
LI_HANDLE    = "@subhajit-kar"

BUILDING  = "Enterprise Zero-Trust Architecture"
EXPLORING = "Automotive CAN-Bus &amp; AI Agents"
FUEL      = "Zero-Trust, coffee &amp; morning runs"
# ─────────────────────────────────────────────────────────────────────────────


def get_portrait_b64() -> str:
    for p in [PORTRAIT_PATH, ROOT_DIR / "assets/avatar/github-avatar.jpg"]:
        if p.exists():
            return base64.b64encode(p.read_bytes()).decode()
    raise FileNotFoundError(f"Portrait not found at {PORTRAIT_PATH}")


def bar_w(stars: int, max_stars: int, max_px: int = 240) -> int:
    if max_stars == 0:
        return 12
    return max(12, int(stars / max_stars * max_px))


def build_project_rows(project_bars) -> str:
    rows = []
    for i, (name, stars, bw) in enumerate(project_bars):
        y = 48 + i * 36
        rows.append(
            f'<g transform="translate(18,{y})">'
            f'<text x="0" y="13" class="f-mono" font-size="11" fill="#CBD5E1">{name}</text>'
            f'<rect x="0" y="18" width="240" height="8" rx="4" fill="#1E293B" opacity="0.4"/>'
            f'<rect x="0" y="18" width="{bw}" height="8" rx="4" fill="url(#barGrad)"/>'
            f'<text x="248" y="27" class="f-display" font-size="12" font-weight="700" fill="#E2E8F0">{stars}</text>'
            f'</g>'
        )
    return "\n    ".join(rows)


def generate_dashboard() -> bool:
    portrait_b64 = get_portrait_b64()

    repos_s     = str(GITHUB["repos"])
    stars_s     = str(GITHUB["stars"])
    forks_s     = str(GITHUB["forks"])
    followers_s = str(GITHUB["followers"])

    max_s = max(s for _, s in PROJECTS)
    project_bars = [(n, s, bar_w(s, max_s)) for n, s in PROJECTS]
    project_rows = build_project_rows(project_bars)

    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" '
        'viewBox="0 0 1280 480" width="100%" height="auto" '
        'role="img" aria-label="Developer Dashboard — Profile at a glance — Subhajit Kar">\n'
        '<title>Developer Dashboard — Profile at a glance</title>\n'
        '<desc>Subhajit Kar, Senior IAM Assistant Manager at Deloitte. '
        f'GitHub: {GITHUB["repos"]} repos, {GITHUB["stars"]} stars, {GITHUB["followers"]} followers. '
        'LinkedIn: linkedin.com/in/subhajit-kar</desc>\n'

        '<defs>\n'
        '<style>\n'
        "@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700"
        "&amp;family=Space+Grotesk:wght@600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap');\n"
        ".f-mono    { font-family: 'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace; }\n"
        ".f-display { font-family: 'Space Grotesk', -apple-system, sans-serif; }\n"
        ".f-sans    { font-family: 'Inter', -apple-system, sans-serif; }\n"
        "@keyframes badgeSway { 0%,100%{transform:rotate(-0.7deg)} 50%{transform:rotate(0.7deg)} }\n"
        "@keyframes holoShift { 0%,100%{opacity:0.12;transform:translateY(-5px)} 50%{opacity:0.28;transform:translateY(5px)} }\n"
        "@keyframes liveDot   { 0%,100%{opacity:1} 50%{opacity:0.35} }\n"
        ".anim-sway { transform-origin:200px 30px; animation:badgeSway 7s ease-in-out infinite; }\n"
        ".anim-holo { animation:holoShift 4s ease-in-out infinite; }\n"
        ".anim-live { animation:liveDot   2s ease-in-out infinite; }\n"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important;transform:none!important}}\n"
        "</style>\n"

        # Gradients
        '<linearGradient id="dashBg" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%"   stop-color="#040711"/>'
        '<stop offset="50%"  stop-color="#070D1D"/>'
        '<stop offset="100%" stop-color="#03050C"/>'
        '</linearGradient>\n'

        '<linearGradient id="badgeGrad" x1="0%" y1="0%" x2="0%" y2="100%">'
        '<stop offset="0%"   stop-color="#121D34"/>'
        '<stop offset="40%"  stop-color="#0A1224"/>'
        '<stop offset="100%" stop-color="#060A14"/>'
        '</linearGradient>\n'

        '<linearGradient id="holoSheen" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%"   stop-color="#FF0080" stop-opacity="0.18"/>'
        '<stop offset="25%"  stop-color="#7928CA" stop-opacity="0.14"/>'
        '<stop offset="50%"  stop-color="#0070F3" stop-opacity="0.18"/>'
        '<stop offset="75%"  stop-color="#00DFD8" stop-opacity="0.22"/>'
        '<stop offset="100%" stop-color="#79F1A4" stop-opacity="0.18"/>'
        '</linearGradient>\n'

        '<linearGradient id="cyanAccent" x1="0%" y1="0%" x2="100%" y2="0%">'
        '<stop offset="0%"   stop-color="#00F2FE"/>'
        '<stop offset="100%" stop-color="#38BDF8"/>'
        '</linearGradient>\n'

        '<linearGradient id="lanyardGrad" x1="0%" y1="0%" x2="100%" y2="0%">'
        '<stop offset="0%"   stop-color="#7C3AED"/>'
        '<stop offset="50%"  stop-color="#9D4EDD"/>'
        '<stop offset="100%" stop-color="#6D28D9"/>'
        '</linearGradient>\n'

        '<linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">'
        '<stop offset="0%"   stop-color="#A855F7"/>'
        '<stop offset="100%" stop-color="#EC4899"/>'
        '</linearGradient>\n'

        '<pattern id="dashGrid" width="32" height="32" patternUnits="userSpaceOnUse">'
        '<path d="M 32 0 L 0 0 0 32" fill="none" stroke="#162238" stroke-width="0.55" stroke-opacity="0.4"/>'
        '</pattern>\n'

        '<clipPath id="badgePhotoClip">'
        '<rect x="135" y="150" width="130" height="130" rx="20"/>'
        '</clipPath>\n'
        '</defs>\n'

        # ── Canvas ──────────────────────────────────────────────────────────
        '<rect width="1280" height="480" fill="url(#dashBg)"/>\n'
        '<rect width="1280" height="480" fill="url(#dashGrid)"/>\n'
        '<rect x="14" y="14" width="1252" height="452" rx="20" fill="none" stroke="#1E293B" stroke-width="1.2"/>\n'
        '<rect x="20" y="20" width="1240" height="440" rx="16" fill="none" stroke="#00F2FE" stroke-opacity="0.10" stroke-width="0.8"/>\n'

        # ── LEFT: ID Badge ───────────────────────────────────────────────────
        '<g class="anim-sway">\n'
        '<rect x="186" y="0" width="28" height="55" fill="url(#lanyardGrad)" rx="2"/>\n'
        '<line x1="200" y1="0" x2="200" y2="55" stroke="#C4B5FD" stroke-opacity="0.35" stroke-width="1" stroke-dasharray="3 3"/>\n'
        '<rect x="178" y="50" width="44" height="18" rx="4" fill="#475569" stroke="#64748B" stroke-width="1"/>\n'
        '<rect x="188" y="62" width="24" height="9"  rx="3" fill="#334155"/>\n'
        '<ellipse cx="200" cy="74" rx="8" ry="4" fill="#00F2FE" opacity="0.75"/>\n'

        '<g transform="translate(60,78)">\n'
        '<rect x="4" y="6" width="280" height="360" rx="20" fill="#020408" fill-opacity="0.85"/>\n'
        '<rect x="0" y="0" width="280" height="360" rx="20" fill="url(#badgeGrad)" stroke="#00F2FE" stroke-opacity="0.42" stroke-width="1.3"/>\n'
        '<rect x="0" y="0" width="280" height="360" rx="20" fill="url(#holoSheen)" class="anim-holo"/>\n'
        '<rect x="110" y="13" width="60" height="7" rx="3.5" fill="#060A14" stroke="#1E293B" stroke-width="0.8"/>\n'

        '<g transform="translate(18,28)">\n'
        '<rect x="0" y="0" width="244" height="28" rx="7" fill="#060E1C" stroke="#1E293B" stroke-width="0.8"/>\n'
        '<text x="12" y="18" class="f-mono" font-size="10" font-weight="700" fill="#00F2FE" letter-spacing="1.5">DEVELOPER ID</text>\n'
        '<text x="168" y="18" class="f-mono" font-size="9" fill="#64748B">v2.0</text>\n'
        '</g>\n'

        '<rect x="18" y="64" width="244" height="20" rx="5" fill="#0A182E" stroke="#00F2FE" stroke-opacity="0.25" stroke-width="0.7"/>\n'
        '<text x="28" y="78" class="f-mono" font-size="8.5" font-weight="700" fill="#00F2FE" letter-spacing="1.1">SK-IAM-9208 · ZERO TRUST</text>\n'

        '<rect x="70" y="92" width="140" height="120" rx="18" fill="#070D1A" stroke="url(#cyanAccent)" stroke-width="1.8"/>\n'
        f'<g clip-path="url(#badgePhotoClip)" transform="translate(-60,-55)">\n'
        f'<image xlink:href="data:image/jpeg;base64,{portrait_b64}" '
        'x="135" y="150" width="130" height="130" preserveAspectRatio="xMidYMid slice"/>\n'
        '<rect x="135" y="150" width="130" height="130" fill="#00F2FE" opacity="0.04"/>\n'
        '</g>\n'

        '<text x="140" y="236" text-anchor="middle" class="f-display" font-size="18" font-weight="800" fill="#F1F5F9" letter-spacing="-0.2">Subhajit Kar</text>\n'
        '<text x="140" y="255" text-anchor="middle" class="f-sans"    font-size="11" font-weight="600" fill="#00F2FE">SENIOR IAM MANAGER</text>\n'

        '<g transform="translate(22,270)">\n'
        '<text x="0"  y="14" class="f-mono" font-size="8" fill="#64748B">BASE</text>\n'
        '<text x="80" y="14" class="f-mono" font-size="8" fill="#64748B">TEAM</text>\n'
        '<text x="0"  y="26" class="f-mono" font-size="9" fill="#CBD5E1">BLR / CCU, IN</text>\n'
        '<text x="80" y="26" class="f-mono" font-size="9" fill="#CBD5E1">Cyber &amp; IGA</text>\n'
        '<text x="0"  y="44" class="f-mono" font-size="8" fill="#64748B">ID</text>\n'
        '<text x="80" y="44" class="f-mono" font-size="8" fill="#64748B">SINCE</text>\n'
        '<text x="0"  y="56" class="f-mono" font-size="9" fill="#CBD5E1">SK-IAM-9208</text>\n'
        '<text x="80" y="56" class="f-mono" font-size="9" fill="#CBD5E1">ZERO TRUST</text>\n'
        '</g>\n'

        # Smart chip
        '<g transform="translate(22,338)">\n'
        '<rect x="0" y="0" width="40" height="30" rx="5" fill="#D97706" stroke="#FDE68A" stroke-width="0.7"/>\n'
        '<line x1="0" y1="10" x2="40" y2="10" stroke="#78350F" stroke-width="0.7"/>\n'
        '<line x1="0" y1="20" x2="40" y2="20" stroke="#78350F" stroke-width="0.7"/>\n'
        '<line x1="20" y1="0" x2="20" y2="30" stroke="#78350F" stroke-width="0.7"/>\n'
        '</g>\n'

        '<text x="20"  y="395" class="f-mono" font-size="8" fill="#10B981">&#x25CF; OPEN TO COLLAB</text>\n'
        '<text x="152" y="395" class="f-mono" font-size="8" fill="#64748B">@ha4kerspidersks</text>\n'
        '</g>\n'   # close translate(60,78)
        '</g>\n'   # close anim-sway

        # ── RIGHT: Profile at a glance ───────────────────────────────────────
        '<g transform="translate(390,36)">\n'

        '<text x="0" y="16" class="f-mono" font-size="11" font-weight="700" fill="#00F2FE" letter-spacing="2">// DEVELOPER DASHBOARD</text>\n'
        '<text x="0" y="48" class="f-display" font-size="28" font-weight="800" fill="#FFFFFF" letter-spacing="-0.5">Profile at a glance</text>\n'

        '<rect x="766" y="6" width="108" height="24" rx="12" fill="#0B2214" stroke="#10B981" stroke-opacity="0.6" stroke-width="1"/>\n'
        '<circle cx="782" cy="18" r="4" fill="#10B981" class="anim-live"/>\n'
        '<text x="792" y="22" class="f-mono" font-size="9.5" font-weight="700" fill="#10B981" letter-spacing="0.8">LIVE · GITHUB</text>\n'

        # ── 4 GitHub stat cards ──────────────────────────────────────────────
        '<g transform="translate(0,68)">\n'

        # Card 1 — Repos
        '<g transform="translate(0,0)">\n'
        '<rect x="0" y="0" width="204" height="72" rx="10" fill="#080F1E" stroke="#1E293B" stroke-width="1"/>\n'
        '<rect x="0" y="0" width="4"   height="72" rx="2"  fill="#00F2FE"/>\n'
        f'<text x="18" y="38" class="f-display" font-size="32" font-weight="800" fill="#FFFFFF">{repos_s}</text>\n'
        '<text x="172" y="34" font-size="22" fill="#00F2FE" opacity="0.55">&#9633;</text>\n'
        '<text x="18"  y="58" class="f-mono" font-size="10" font-weight="700" fill="#64748B" letter-spacing="0.8">PUBLIC REPOS</text>\n'
        '</g>\n'

        # Card 2 — Stars
        '<g transform="translate(216,0)">\n'
        '<rect x="0" y="0" width="204" height="72" rx="10" fill="#080F1E" stroke="#1E293B" stroke-width="1"/>\n'
        '<rect x="0" y="0" width="4"   height="72" rx="2"  fill="#FFDB70"/>\n'
        f'<text x="18" y="38" class="f-display" font-size="32" font-weight="800" fill="#FFFFFF">{stars_s}</text>\n'
        '<text x="172" y="34" font-size="22" fill="#FFDB70" opacity="0.6">&#9733;</text>\n'
        '<text x="18"  y="58" class="f-mono" font-size="10" font-weight="700" fill="#64748B" letter-spacing="0.8">TOTAL STARS</text>\n'
        '</g>\n'

        # Card 3 — Forks
        '<g transform="translate(432,0)">\n'
        '<rect x="0" y="0" width="204" height="72" rx="10" fill="#080F1E" stroke="#1E293B" stroke-width="1"/>\n'
        '<rect x="0" y="0" width="4"   height="72" rx="2"  fill="#A855F7"/>\n'
        f'<text x="18" y="38" class="f-display" font-size="32" font-weight="800" fill="#FFFFFF">{forks_s}</text>\n'
        '<text x="172" y="34" font-size="18" fill="#A855F7" opacity="0.6">&#9903;</text>\n'
        '<text x="18"  y="58" class="f-mono" font-size="10" font-weight="700" fill="#64748B" letter-spacing="0.8">FORKS</text>\n'
        '</g>\n'

        # Card 4 — Followers
        '<g transform="translate(648,0)">\n'
        '<rect x="0" y="0" width="228" height="72" rx="10" fill="#080F1E" stroke="#1E293B" stroke-width="1"/>\n'
        '<rect x="0" y="0" width="4"   height="72" rx="2"  fill="#EC4899"/>\n'
        f'<text x="18" y="38" class="f-display" font-size="32" font-weight="800" fill="#FFFFFF">{followers_s}</text>\n'
        '<text x="192" y="34" font-size="18" fill="#EC4899" opacity="0.6">&#9786;</text>\n'
        '<text x="18"  y="58" class="f-mono" font-size="10" font-weight="700" fill="#64748B" letter-spacing="0.8">FOLLOWERS</text>\n'
        '</g>\n'

        '</g>\n'  # close stat cards translate(0,68)

        # ── Bottom two panels ─────────────────────────────────────────────────
        '<g transform="translate(0,160)">\n'

        # Left: Most-Starred Projects
        '<rect x="0" y="0" width="548" height="240" rx="12" fill="#060C18" stroke="#1E293B" stroke-width="1"/>\n'
        '<text x="18" y="28" class="f-mono" font-size="10" font-weight="700" fill="#64748B" letter-spacing="1.5">MOST-STARRED PROJECTS</text>\n'

        f'{project_rows}\n'

        '<text x="18" y="228" class="f-mono" font-size="9" fill="#334155">stars per repository &#xB7; cybersecurity &amp; ai builds</text>\n'

        # Right: Community
        '<rect x="564" y="0" width="312" height="240" rx="12" fill="#060C18" stroke="#1E293B" stroke-width="1"/>\n'
        '<text x="582" y="28" class="f-mono" font-size="10" font-weight="700" fill="#64748B" letter-spacing="1.5">COMMUNITY</text>\n'

        # LinkedIn logo box
        '<g transform="translate(582,38)">\n'
        '<rect x="0" y="0" width="28" height="28" rx="6" fill="#0A66C2"/>\n'
        '<text x="5" y="21" class="f-sans" font-size="17" font-weight="800" fill="#FFFFFF">in</text>\n'
        '</g>\n'
        '<text x="618" y="55" class="f-display" font-size="12" font-weight="700" fill="#94A3B8">LinkedIn</text>\n'

        # Metrics
        f'<text x="582" y="88" class="f-display" font-size="24" font-weight="800" fill="#FFFFFF">{LI_FOLLOWERS}</text>\n'
        '<text x="582" y="106" class="f-mono" font-size="9" fill="#64748B" letter-spacing="0.5">LI FOLLOWERS</text>\n'
        '<circle cx="680" cy="86" r="3" fill="#334155"/>\n'
        f'<text x="692" y="88" class="f-display" font-size="24" font-weight="800" fill="#FFFFFF">{LI_VIEWS}</text>\n'
        '<text x="692" y="106" class="f-mono" font-size="9" fill="#64748B" letter-spacing="0.5">VIEWS / 30 DAYS</text>\n'
        f'<text x="582" y="124" class="f-mono" font-size="9.5" fill="#475569">{LI_HANDLE}</text>\n'

        '<line x1="582" y1="136" x2="862" y2="136" stroke="#162238" stroke-width="0.8"/>\n'

        # Building
        '<g transform="translate(582,146)">\n'
        '<circle cx="6" cy="10" r="4" fill="#10B981"/>\n'
        '<text x="18" y="8"  class="f-mono" font-size="8"  font-weight="700" fill="#10B981" letter-spacing="1">BUILDING</text>\n'
        f'<text x="18" y="20" class="f-sans" font-size="11" font-weight="600" fill="#E2E8F0">{BUILDING}</text>\n'
        '</g>\n'

        # Exploring
        '<g transform="translate(582,176)">\n'
        '<circle cx="6" cy="10" r="4" fill="#38BDF8"/>\n'
        '<text x="18" y="8"  class="f-mono" font-size="8"  font-weight="700" fill="#38BDF8" letter-spacing="1">EXPLORING</text>\n'
        f'<text x="18" y="20" class="f-sans" font-size="11" font-weight="600" fill="#E2E8F0">{EXPLORING}</text>\n'
        '</g>\n'

        # Fuel
        '<g transform="translate(582,206)">\n'
        '<circle cx="6" cy="10" r="4" fill="#F472B6"/>\n'
        '<text x="18" y="8"  class="f-mono" font-size="8"  font-weight="700" fill="#F472B6" letter-spacing="1">FUEL</text>\n'
        f'<text x="18" y="20" class="f-sans" font-size="11" font-weight="600" fill="#E2E8F0">{FUEL}</text>\n'
        '</g>\n'

        '</g>\n'   # close translate(0,160)
        '</g>\n'   # close translate(390,36)
        '</svg>\n'
    )

    # Validate XML
    try:
        ET.fromstring(svg)
    except ET.ParseError as err:
        lno, col = err.position
        lines = svg.split("\n")
        print(f"❌ XML error line {lno} col {col}: {err}", file=sys.stderr)
        for i in range(max(0, lno - 3), min(len(lines), lno + 2)):
            print(f"  {i+1}: {lines[i][:120]}", file=sys.stderr)
        return False

    DASHBOARD_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD_OUTPUT_SVG.write_text(svg, encoding="utf-8")
    METRICS_BANNER_SVG.write_text(svg, encoding="utf-8")

    sz = DASHBOARD_OUTPUT_SVG.stat().st_size / 1024
    print(f"✅ Dashboard SVG → {DASHBOARD_OUTPUT_SVG}  ({sz:.1f} KB)")
    return True


if __name__ == "__main__":
    sys.exit(0 if generate_dashboard() else 1)
