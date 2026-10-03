#!/usr/bin/env python3
"""
scripts/build-transformed-stack.py
Builds the Category-by-Category Orbital Tool Carousel (assets/stack.svg):
1. LEFT SIDE: Category-by-Category 3D Orbital Carousel System
   - Central Core (</>) with radial glow halo and breathing ripples
   - Exactly ONE Category Active at a time:
     * CATEGORY 1: IDENTITY & ACCESS GOVERNANCE (8 tools) -> 8 tools orbit in 3D
     * CATEGORY 2: CLOUD & INFRASTRUCTURE (10 tools) -> 10 tools orbit in 3D
     * CATEGORY 3: DEVELOPMENT & ARCHITECTURE (17 tools) -> 17 tools orbit in 3D
     * CATEGORY 4: SECURITY & DEFENSE (5 tools) -> 5 tools orbit in 3D
     * CATEGORY 5: DATA, AI & ENTERPRISE (16 tools) -> 16 tools orbit in 3D
   - Smooth 40-second continuous cycle (8s per category) with 0.8s dissolve/materialize transition
   - Dynamic node distribution across 3D elliptical orbital planes
   - Zero cross-category leakage (inactive categories are strictly opacity:0 / visibility:hidden)
   - 3D depth parallax scaling and subtle node micro-motion
2. RIGHT SIDE: All 56 Categorized Technology Chips with authentic brand logos (Strictly Preserved)
   - Synchronized subtle active category accent indicator
"""

import json
import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
REF_STACK_PATH = ROOT / "reference-base/stack.svg"
OUTPUT_STACK_PATH = ROOT / "assets/stack.svg"

def make_ellipse_path(cx, cy, rx, ry, angle_deg):
    """Generates an SVG path for an ellipse rotated by angle_deg."""
    rad = math.radians(angle_deg)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    p1_x = cx + rx * cos_a
    p1_y = cy + rx * sin_a
    p2_x = cx - rx * cos_a
    p2_y = cy - rx * sin_a
    
    return f"M {p1_x:.2f} {p1_y:.2f} A {rx:.2f} {ry:.2f} {angle_deg:.2f} 1 1 {p2_x:.2f} {p2_y:.2f} A {rx:.2f} {ry:.2f} {angle_deg:.2f} 1 1 {p1_x:.2f} {p1_y:.2f} Z"

def extract_logo_inner(svg_path: Path, tech_color: str, target_size: float = 18.0):
    raw = svg_path.read_text(encoding='utf-8')
    m_svg = re.search(r'<svg([^>]*)>(.*)</svg>', raw, re.DOTALL)
    if not m_svg:
        return f'<circle cx="0" cy="0" r="{target_size/2:.1f}" fill="{tech_color}"/>'
    
    attrs, inner = m_svg.group(1), m_svg.group(2)
    inner = re.sub(r'<\?xml.*?\?>', '', inner, flags=re.DOTALL)
    inner = re.sub(r'<!DOCTYPE.*?>', '', inner, flags=re.DOTALL)
    inner = re.sub(r'<!--.*?-->', '', inner, flags=re.DOTALL)
    inner = re.sub(r'xlink:href=', 'href=', inner)
    
    vb_m = re.search(r'viewBox=["\']([^"\']+)["\']', attrs)
    if vb_m:
        parts = [float(x) for x in vb_m.group(1).split()]
        min_x, min_y, vb_w, vb_h = parts if len(parts) == 4 else (0, 0, 24, 24)
    else:
        w_m = re.search(r'width=["\']([^"\']+)["\']', attrs)
        h_m = re.search(r'height=["\']([^"\']+)["\']', attrs)
        w = float(re.sub(r'[^\d.]', '', w_m.group(1))) if w_m else 24
        h = float(re.sub(r'[^\d.]', '', h_m.group(1))) if h_m else 24
        min_x, min_y, vb_w, vb_h = 0, 0, w, h
    
    fill_m = re.search(r'\bfill=["\']([^"\']+)["\']', attrs)
    root_fill = fill_m.group(1) if fill_m else None
    
    stroke_m = re.search(r'\bstroke=["\']([^"\']+)["\']', attrs)
    root_stroke = stroke_m.group(1) if stroke_m else None

    max_dim = max(vb_w, vb_h)
    scale = target_size / max_dim if max_dim > 0 else 1.0
    cx = min_x + vb_w / 2.0
    cy = min_y + vb_h / 2.0

    effective_fill = root_fill if root_fill and root_fill != 'none' else tech_color
    fill_attr = f'fill="{effective_fill}"' if effective_fill else ''
    stroke_attr = f'stroke="{root_stroke}"' if root_stroke and root_stroke != 'none' else ''

    wrapped = f'''<g transform="scale({scale:.4f}) translate({-cx:.2f}, {-cy:.2f})" {fill_attr} {stroke_attr} style="color:{tech_color}">
      {inner.strip()}
    </g>'''
    return wrapped

def generate_carousel_keyframe_data(cat_idx, num_cats=5, cat_dur=8.0, trans_dur=0.8):
    """Calculates unified keyTimes, opacity, and scale values for carousel presentation."""
    total_dur = num_cats * cat_dur
    t_start = cat_idx * cat_dur
    t_enter = t_start + trans_dur
    t_exit = t_start + cat_dur - trans_dur
    t_end = (cat_idx + 1) * cat_dur

    points = [0.0]
    for i in range(num_cats):
        s = i * cat_dur
        e = s + trans_dur
        x = s + cat_dur - trans_dur
        d = (i + 1) * cat_dur
        for pt in [s, e, x, d]:
            if 0.0 <= pt <= total_dur:
                points.append(pt)
    points.append(total_dur)
    points = sorted(list(set(points)))

    opacities = []
    scales = []
    visibilities = []

    for pt in points:
        if pt < t_start or pt > t_end:
            opacities.append(0.0)
            scales.append(0.82)
            visibilities.append("hidden")
        elif pt == t_start:
            opacities.append(0.0)
            scales.append(0.82)
            visibilities.append("visible")
        elif pt == t_end:
            opacities.append(0.0)
            scales.append(0.82)
            visibilities.append("hidden")
        elif t_enter <= pt <= t_exit:
            opacities.append(1.0)
            scales.append(1.0)
            visibilities.append("visible")
        elif t_start < pt < t_enter:
            frac = (pt - t_start) / trans_dur
            opacities.append(round(frac, 3))
            scales.append(round(0.82 + 0.18 * frac, 3))
            visibilities.append("visible")
        elif t_exit < pt < t_end:
            frac = (t_end - pt) / trans_dur
            opacities.append(round(frac, 3))
            scales.append(round(0.82 + 0.18 * frac, 3))
            visibilities.append("visible")
        else:
            opacities.append(0.0)
            scales.append(0.82)
            visibilities.append("hidden")

    norm_times = [round(pt / total_dur, 4) for pt in points]
    return norm_times, opacities, scales, visibilities

def main():
    print("⚛️ Generating Category-by-Category 3D Orbital Tech Stack (assets/stack.svg)...")

    with open(REF_STACK_PATH, "r", encoding="utf-8") as f:
        ref_svg = f.read()

    # Extract base styles
    styles_match = re.search(r'<style>(.*?)</style>', ref_svg, re.DOTALL)
    styles = styles_match.group(1) if styles_match else ""

    # Load technologies
    with open(ROOT / "profile/technology-stack.json", "r", encoding="utf-8") as f:
        techs = json.load(f)

    tech_by_short = {t["shortName"]: t for t in techs}

    # =========================================================================
    # 1. DEFINE SHARED 3D ORBITAL ELLIPTICAL PATHS
    # =========================================================================
    cx, cy = 262, 290

    # 3 distinct 3D orbital plane rings:
    # Plane 0: Equatorial tilt (-12 deg)
    # Plane 1: Ascending 3D diagonal (+46 deg)
    # Plane 2: Descending 3D diagonal (-50 deg)
    # Shield Plane: Dedicated perimeter orbit (+22 deg)
    orbit_definitions = {
        "orb_ring_0": {"rx": 180, "ry": 78, "angle": -12},
        "orb_ring_1": {"rx": 175, "ry": 82, "angle": 46},
        "orb_ring_2": {"rx": 175, "ry": 82, "angle": -50},
        "orb_ring_shield": {"rx": 165, "ry": 75, "angle": 22},
    }

    orbit_paths_defs = []
    for pid, odef in orbit_definitions.items():
        pstr = make_ellipse_path(cx, cy, odef["rx"], odef["ry"], odef["angle"])
        orbit_paths_defs.append(f'<path id="{pid}" d="{pstr}" fill="none"/>')

    # =========================================================================
    # 2. CATEGORY-BY-CATEGORY DEFINITIONS & RING DISTRIBUTIONS
    # =========================================================================
    # Source of truth: matches right-side categorized chips exactly
    category_order = [
        {
            "id": "iam",
            "title": "IDENTITY &amp; ACCESS GOVERNANCE",
            "chip_title": "IDENTITY &amp; ACCESS GOVERNANCE",
            "color": "#00f2fe",
            "lead": "Saviynt",
            "rings": [
                {"path_id": "orb_ring_0", "tools": ["Saviynt", "Entra ID", "Active Directory", "Okta"]},
                {"path_id": "orb_ring_1", "tools": ["SoD & RBAC", "JML Lifecycle", "OAuth & SAML", "FIDO2 & MFA"]}
            ]
        },
        {
            "id": "cloud",
            "title": "CLOUD &amp; INFRASTRUCTURE",
            "chip_title": "CLOUD &amp; INFRASTRUCTURE",
            "color": "#38bdf8",
            "lead": "AWS",
            "rings": [
                {"path_id": "orb_ring_0", "tools": ["AWS", "Azure", "Firebase", "Vercel", "Docker"]},
                {"path_id": "orb_ring_2", "tools": ["Jenkins", "Git", "GitHub", "Linux", "Bash"]}
            ]
        },
        {
            "id": "dev",
            "title": "DEVELOPMENT &amp; ARCHITECTURE",
            "chip_title": "DEVELOPMENT &amp; ARCHITECTURE",
            "color": "#a78bfa",
            "lead": "TypeScript",
            "rings": [
                {"path_id": "orb_ring_0", "tools": ["TypeScript", "React", "Node.js", "Next.js", "Vite", "VS Code"]},
                {"path_id": "orb_ring_1", "tools": ["Java", "JavaScript", "FastAPI", "Flask", "Three.js", "GSAP"]},
                {"path_id": "orb_ring_2", "tools": ["Postman", "Tailwind", "HTML5", "CSS3", "C++"]}
            ]
        },
        {
            "id": "sec",
            "title": "SECURITY &amp; DEFENSE",
            "chip_title": "SECURITY &amp; DEFENSE",
            "color": "#10b981",
            "lead": "Zero Trust",
            "rings": [
                {"path_id": "orb_ring_shield", "tools": ["Zero Trust", "CyberArk", "OWASP", "Burp Suite", "Wireshark"]}
            ]
        },
        {
            "id": "data_ai",
            "title": "DATA, AI &amp; ENTERPRISE",
            "chip_title": "DATA, AI &amp; ENTERPRISE",
            "color": "#f472b6",
            "lead": "Agentic AI",
            "rings": [
                {"path_id": "orb_ring_1", "tools": ["Agentic AI", "MCP", "LLM Eng", "AI Workflows", "Python", "Snowflake"]},
                {"path_id": "orb_ring_0", "tools": ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Identity Recon"]},
                {"path_id": "orb_ring_2", "tools": ["Workday", "ServiceNow", "Jira", "SOX 404", "Figma"]}
            ]
        }
    ]

    total_orbital_techs = 0
    all_seen_orbital = set()
    for cat in category_order:
        c_tools = []
        for r in cat["rings"]:
            c_tools.extend(r["tools"])
        total_orbital_techs += len(c_tools)
        all_seen_orbital.update(c_tools)
        print(f"  Category '{cat['id']}': {len(c_tools)} tools -> {c_tools}")

    print(f"  Verified Total Orbital Technologies: {total_orbital_techs}/56 ({len(all_seen_orbital)} unique)")
    if total_orbital_techs != 56 or len(all_seen_orbital) != 56:
        raise ValueError(f"Expected 56 unique orbital technologies, got {total_orbital_techs} (unique {len(all_seen_orbital)})!")

    # =========================================================================
    # 3. GENERATE CATEGORY CAROUSEL ORBITAL MARKUP
    # =========================================================================
    num_cats = len(category_order)
    cat_dur = 8.0
    total_cycle_dur = num_cats * cat_dur
    orbit_period = 18.0  # Speed of tools orbiting along the ring

    category_carousel_markups = []
    right_side_indicator_animations = {}

    for cat_idx, cat in enumerate(category_order):
        norm_times, opacities, scales, visibilities = generate_carousel_keyframe_data(cat_idx, num_cats, cat_dur)

        kt_str = "; ".join(f"{t:.3f}" for t in norm_times)
        op_str = "; ".join(f"{o:.2f}" for o in opacities)
        sc_str = "; ".join(f"{s:.2f}" for s in scales)
        vis_str = "; ".join(visibilities)

        # Build visual orbital path lines for this category
        ring_paths_markup = []
        used_pids = list(dict.fromkeys(r["path_id"] for r in cat["rings"]))
        for pid in used_pids:
            odef = orbit_definitions[pid]
            pstr = make_ellipse_path(cx, cy, odef["rx"], odef["ry"], odef["angle"])
            ring_paths_markup.append(
                f'<path d="{pstr}" fill="none" stroke="{cat["color"]}" stroke-opacity=".22" '
                f'stroke-width="1.3" stroke-dasharray="5,7"/>'
            )
        rings_str = "\n    ".join(ring_paths_markup)

        # Build tools for this category
        nodes_markup = []
        float_counter = 0

        for r_spec in cat["rings"]:
            pid = r_spec["path_id"]
            ring_tools = r_spec["tools"]
            k = len(ring_tools)

            for j, sname in enumerate(ring_tools):
                t = tech_by_short[sname]
                tech_color = t.get("color", cat["color"])
                logo_p = ROOT / t.get("logoPath", t.get("logo_source", ""))
                
                is_lead = (sname == cat["lead"])
                r_size = 14.0 if is_lead else 12.5
                target_logo_sz = 14.0 if is_lead else 12.5
                logo_markup = extract_logo_inner(logo_p, tech_color, target_logo_sz)

                # Equidistant phase offset along this ring
                offset = (j / float(k)) * orbit_period

                # Micro-motion parameters
                float_offset = -2.0 if (float_counter % 2 == 0) else 2.0
                float_dur = 2.4 + (float_counter % 3) * 0.4
                float_counter += 1

                lead_glow = ""
                if is_lead:
                    lead_glow = f'''<circle r="{r_size + 4.0:.1f}" fill="none" stroke="{cat['color']}" stroke-opacity=".5" stroke-width="1.2" stroke-dasharray="3,3">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
          </circle>'''

                sname_esc = sname.replace("&", "&amp;")
                nodes_markup.append(f'''      <!-- Tool Node: {sname_esc} -->
      <g>
        <animateMotion dur="{orbit_period:.1f}s" begin="-{offset:.2f}s" repeatCount="indefinite">
          <mpath href="#{pid}"/>
        </animateMotion>
        <g>
          <animateTransform attributeName="transform" type="scale" values="1.0; 1.15; 1.0; 0.85; 1.0" keyTimes="0; 0.25; 0.5; 0.75; 1" dur="{orbit_period:.1f}s" begin="-{offset:.2f}s" repeatCount="indefinite" ease="ease-in-out"/>
          <g>
            <animateTransform attributeName="transform" type="translate" values="0 0; 0 {float_offset}; 0 0" dur="{float_dur:.1f}s" repeatCount="indefinite" ease="ease-in-out"/>
            <title>{sname_esc} — {cat['title']}</title>
            {lead_glow}
            <circle r="{r_size}" fill="#111424" stroke="{tech_color}" stroke-opacity=".82" stroke-width="1.3"/>
            {logo_markup}
          </g>
        </g>
      </g>''')

        all_nodes_str = "\n".join(nodes_markup)
        cat_tool_count = sum(len(r["tools"]) for r in cat["rings"])

        # Assembled Category Carousel Group
        # Scaling centered on (cx, cy) via translate(cx, cy) -> scale -> translate(-cx, -cy)
        category_carousel_markups.append(f'''  <!-- ======================================================================= -->
  <!-- CAROUSEL CATEGORY: {cat['title']} ({cat_tool_count} TOOLS) -->
  <!-- ======================================================================= -->
  <g id="carousel-cat-{cat['id']}">
    <animate attributeName="opacity" values="{op_str}" keyTimes="{kt_str}" dur="{total_cycle_dur:.1f}s" repeatCount="indefinite" ease="ease-in-out"/>
    <animate attributeName="visibility" values="{vis_str}" keyTimes="{kt_str}" dur="{total_cycle_dur:.1f}s" repeatCount="indefinite"/>
    
    <!-- Smooth Center Materialize / Dissolve Transform -->
    <g transform="translate({cx}, {cy})">
      <g>
        <animateTransform attributeName="transform" type="scale" values="{sc_str}" keyTimes="{kt_str}" dur="{total_cycle_dur:.1f}s" repeatCount="indefinite" ease="ease-in-out"/>
        <g transform="translate(-{cx}, -{cy})">
          <!-- Active Category Badge -->
          <text class="jbb" x="{cx}" y="112" font-size="11" fill="{cat['color']}" letter-spacing="2.2" text-anchor="middle" opacity=".9">// ACTIVE LAYER: {cat['title']} ({cat_tool_count} TOOLS)</text>
          
          <!-- Category 3D Orbital Rings -->
          {rings_str}
          
          <!-- Category Technology Nodes (ONLY {cat_tool_count} Tools) -->
{all_nodes_str}
        </g>
      </g>
    </g>
  </g>''')

        # Synchronized right-side indicator animation data
        right_side_indicator_animations[cat["id"]] = {
            "kt_str": kt_str,
            "width_str": "; ".join("26" if o > 0.5 else "14" for o in opacities),
            "op_str": "; ".join("1.0" if o > 0.5 else "0.5" for o in opacities),
            "text_color_str": "; ".join(cat["color"] if o > 0.5 else "#8d93ab" for o in opacities)
        }

    carousel_markups_str = "\n\n".join(category_carousel_markups)

    # =========================================================================
    # 4. RIGHT SIDE CHIPS (STRICTLY PRESERVED ALL 56 TECHNOLOGIES)
    # =========================================================================
    categories_chips = [
        ("IDENTITY &amp; ACCESS GOVERNANCE", "iam", "#00f2fe", [t for t in techs if t["category"] == "iam"]),
        ("CLOUD &amp; INFRASTRUCTURE", "cloud", "#38bdf8", [t for t in techs if t["category"] in ["cloud", "devops"] and t["shortName"] not in ["Vite", "VS Code"]]),
        ("DEVELOPMENT &amp; ARCHITECTURE", "dev", "#a78bfa", [t for t in techs if t["category"] == "programming" or t["shortName"] in ["Vite", "VS Code"]]),
        ("SECURITY &amp; DEFENSE", "sec", "#10b981", [t for t in techs if t["category"] == "security"]),
        ("DATA, AI &amp; ENTERPRISE", "data_ai", "#f472b6", [t for t in techs if t["category"] in ["data", "ai", "enterprise"]])
    ]

    chips_svg = []
    start_x = 552
    max_x = 1240
    curr_y = 120
    row_height = 38
    gap_x = 8
    gap_y = 8
    delay = 0.5

    for cat_name, cat_id, cat_color, items in categories_chips:
        ind_anim = right_side_indicator_animations.get(cat_id)
        ind_rect_anim = ""
        ind_text_anim = ""
        if ind_anim:
            ind_rect_anim = f'''<animate attributeName="width" values="{ind_anim['width_str']}" keyTimes="{ind_anim['kt_str']}" dur="{total_cycle_dur:.1f}s" repeatCount="indefinite"/>
      <animate attributeName="fill-opacity" values="{ind_anim['op_str']}" keyTimes="{ind_anim['kt_str']}" dur="{total_cycle_dur:.1f}s" repeatCount="indefinite"/>'''
            ind_text_anim = f'''<animate attributeName="fill" values="{ind_anim['text_color_str']}" keyTimes="{ind_anim['kt_str']}" dur="{total_cycle_dur:.1f}s" repeatCount="indefinite"/>'''

        chips_svg.append(f'''  <!-- Section: {cat_name} -->
  <g class="chip" style="animation-delay:{delay:.2f}s">
    <rect x="{start_x}" y="{curr_y}" width="14" height="3" rx="1.5" fill="{cat_color}">
      {ind_rect_anim}
    </rect>
    <text class="jbb" x="{start_x + 22}" y="{curr_y + 5}" font-size="11" fill="#8d93ab" letter-spacing="1.8">
      {ind_text_anim}
      {cat_name}
    </text>
  </g>''')
        delay += 0.05
        curr_y += 20
        curr_x = start_x

        for t in items:
            name = t["shortName"].replace("&", "&amp;")
            color = t.get("color", "#22d3ee")
            w = max(86, int(len(t["shortName"]) * 7.4 + 46))
            if curr_x + w > max_x:
                curr_y += row_height + gap_y
                curr_x = start_x

            chip_x = curr_x
            chip_y = curr_y

            logo_p = ROOT / t.get("logoPath", t.get("logo_source", ""))
            if logo_p.exists():
                logo_inner = extract_logo_inner(logo_p, color, 18.0)
                logo_markup = f'''<g transform="translate({chip_x + 20}, {chip_y + int(row_height / 2)})">
      {logo_inner}
    </g>'''
            else:
                logo_markup = f'''<circle cx="{chip_x + 20}" cy="{chip_y + int(row_height / 2)}" r="6" fill="{color}"/>'''

            chips_svg.append(f'''  <g class="chip" style="animation-delay:{delay:.2f}s">
    <rect x="{chip_x}" y="{chip_y}" width="{w}" height="{row_height}" rx="12" fill="{color}" fill-opacity=".08"/>
    <rect x="{chip_x + 0.5}" y="{chip_y + 0.5}" width="{w - 1}" height="{row_height - 1}" rx="11.5" fill="none" stroke="{color}" stroke-opacity=".3">
      <animate attributeName="stroke-opacity" values=".3;1;.3;.3" keyTimes="0;.04;.14;1" dur="7.20s" begin="{delay + 1.5:.2f}s" repeatCount="indefinite"/>
    </rect>
    {logo_markup}
    <text class="jb" x="{chip_x + 36}" y="{chip_y + int(row_height / 2) + 4.5}" font-size="12" fill="#eceef6">{name}</text>
  </g>''')

            curr_x += w + gap_x
            delay += 0.02

        curr_y += row_height + 16

    svg_height = max(800, curr_y + 24)

    # =========================================================================
    # 5. FULL ASSEMBLED SVG
    # =========================================================================
    orbit_paths_str = "\n".join(orbit_paths_defs)
    chips_str = "\n".join(chips_svg)

    svg_output = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 {svg_height}" width="1280" height="{svg_height}" role="img" aria-label="Tools I build with — 56 Technologies">
<title>Tech Stack — Subhajit Kar</title>
<desc>Category-by-category 3D orbital constellation carousel with central code core and all 56 verified portfolio technologies.</desc>
<defs>
<style>
{styles}
</style>
<radialGradient id="coreG" cx=".35" cy=".3" r=".8">
  <stop offset="0" stop-color="#f472b6"/>
  <stop offset=".55" stop-color="#a78bfa"/>
  <stop offset="1" stop-color="#7c3aed"/>
</radialGradient>
<radialGradient id="halo">
  <stop offset="0" stop-color="#a78bfa" stop-opacity=".35"/>
  <stop offset="1" stop-color="#a78bfa" stop-opacity="0"/>
</radialGradient>
<linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#171a2c"/>
  <stop offset="1" stop-color="#0d0e16"/>
</linearGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#22d3ee" stop-opacity=".5"/>
  <stop offset=".5" stop-color="#a78bfa" stop-opacity=".3"/>
  <stop offset="1" stop-color="#f472b6" stop-opacity=".5"/>
</linearGradient>
<pattern id="dots3" width="22" height="22" patternUnits="userSpaceOnUse">
  <circle cx="11" cy="11" r=".8" fill="#fff" fill-opacity=".05"/>
</pattern>
{orbit_paths_str}
</defs>

<!-- Card Frame -->
<rect width="1280" height="{svg_height}" rx="24" fill="url(#cardbg)"/>
<rect width="1280" height="{svg_height}" rx="24" fill="url(#dots3)"/>
<rect x=".75" y=".75" width="1278.5" height="{svg_height - 1.5}" rx="23.25" fill="none" stroke="url(#edge)" stroke-width="1.5"/>

<!-- Header -->
<g class="fu" style="animation-delay:.1s">
  <text class="jbb" x="40" y="54" font-size="12.5" fill="#22d3ee" letter-spacing="2.2">// TECH STACK</text>
  <text class="sg" x="40" y="94" font-size="29" fill="#eceef6" letter-spacing="-.5">Tools I build with</text>
</g>

<!-- Divider Line -->
<line x1="520" y1="120" x2="520" y2="{svg_height - 45}" stroke="#262a42" stroke-width="1"/>

<!-- LEFT SIDE: CATEGORY CAROUSEL 3D ORBITAL SYSTEM -->
<g transform="translate(0, 130)">
  <!-- CENTRAL CODE CORE (Dominant Anchor - Always Visible) -->
  <circle cx="{cx}" cy="{cy}" r="120" fill="url(#halo)"/>
  <circle cx="{cx}" cy="{cy}" r="46" fill="none" stroke="#f472b6" stroke-width="1.5">
    <animate attributeName="r" values="46;78" dur="2.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".7;0" dur="2.8s" repeatCount="indefinite"/>
  </circle>
  <g class="core">
    <circle cx="{cx}" cy="{cy}" r="46" fill="url(#coreG)"/>
    <text class="sg" x="{cx}" y="{cy + 10}" font-size="28" fill="#fff" text-anchor="middle">&lt;/&gt;</text>
  </g>

  <!-- CATEGORY CAROUSEL LAYERS (Exactly ONE Active at a Time) -->
{carousel_markups_str}
</g>

<!-- RIGHT SIDE: ALL 56 CATEGORIZED CHIPS -->
{chips_str}

</svg>'''

    # Strictly validate XML
    try:
        ET.fromstring(svg_output)
        print("  XML Validation: 100% VALID!")
    except ET.ParseError as pe:
        print(f"  ❌ XML ParseError: {pe}")
        raise

    with open(OUTPUT_STACK_PATH, "w", encoding="utf-8") as f:
        f.write(svg_output)

    print(f"🎉 Successfully generated Category-by-Category Orbital Tech Stack: {len(svg_output)} bytes ({svg_output.count('<title')} nodes/chips)")

if __name__ == "__main__":
    main()
