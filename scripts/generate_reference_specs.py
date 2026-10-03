from pathlib import Path

reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

# 1. reports/reference-color-system.md
color_spec_path = reports_dir / "reference-color-system.md"
with open(color_spec_path, "w", encoding="utf-8") as f:
    f.write("""# Reference Color System Specification

**Reference Repository**: `https://github.com/Meghamittal0920/Meghamittal0920.git`  
**Purpose**: Complete mathematical and hex breakdown of the reference profile color palette to ensure 100% color fidelity across all generated SVGs.

---

## 1. Master Color Palette

| Token Name | Hex Code | Role in Visual Hierarchy | Usage in Reference Components |
|:---|:---:|:---|:---|
| **Canvas Background** | `#0d0e16` | Global deep obsidian canvas | SVG background base, body background |
| **Card Surface Base** | `#121423` | Elevated card container fill | Main card body, browser window backgrounds |
| **Card Surface Secondary** | `#171a2c` | Interactive tiles & inner cards | Metric tiles, lanyard badge face, connect cards |
| **Surface Hover / Highlight** | `#ffffff` (0.03 opacity) | Specular sheen on cards | Tile background overlay (`fill="#ffffff" fill-opacity=".03"`) |
| **Structural Border** | `#262a42` | Crisp container outlines | Card stroke (`stroke="#262a42"`), separator lines |
| **Electric Cyan** | `#22d3ee` | Primary cyber accent & glow | Code tags, section headers (`// TECH STACK`), animated borders |
| **Vivid Pink** | `#f472b6` | Secondary vibrant accent | `// LET'S CONNECT`, email badges, status highlights |
| **Lavender Purple** | `#a78bfa` | Tertiary royal accent | `// DEVELOPER DASHBOARD`, profile views badge, card glows |
| **Mint Emerald** | `#34d399` | Success / Live telemetry indicator | `LIVE · GITHUB` badges, pulsing radar rings, status lights |
| **Warm Amber / Gold** | `#fbbf24` / `#fec220` | Star counter & trophy accents | Star icons, achievement medals |
| **Signal Red** | `#ef4444` | Recording / Alert indicator | `REC` blinking recording dot in hero camera HUD |
| **Heading Text** | `#eceef6` | Primary high-contrast text | Space Grotesk headings, titles, name typography |
| **Muted Text** | `#8d93ab` | Secondary descriptive text | JetBrains Mono subtitles, labels, metadata, URLs |

---

## 2. Gradient System

1. **Card Background Gradient (`url(#cardbg)`)**:
   ```xml
   <linearGradient id="cardbg" x1="0%" y1="0%" x2="0%" y2="100%">
     <stop offset="0%" stop-color="#171a2c"/>
     <stop offset="100%" stop-color="#0d0e16"/>
   </linearGradient>
   ```

2. **Specular Edge Border Gradient (`url(#edge)`)**:
   ```xml
   <linearGradient id="edge" x1="0%" y1="0%" x2="100%" y2="100%">
     <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.4"/>
     <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.2"/>
     <stop offset="100%" stop-color="#262a42" stop-opacity="0.8"/>
   </linearGradient>
   ```

3. **Title Text Gradient (`url(#nameGrad)`)**:
   ```xml
   <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
     <stop offset="0%" stop-color="#eceef6"/>
     <stop offset="50%" stop-color="#22d3ee"/>
     <stop offset="100%" stop-color="#a78bfa"/>
   </linearGradient>
   ```

4. **Background Ambient Glows**:
   - Cyan radial: `#22d3ee` at 12% opacity blurring into transparent.
   - Purple radial: `#a78bfa` at 10% opacity blurring into transparent.
   - Pink radial: `#f472b6` at 8% opacity blurring into transparent.

---

## 3. Strict Compliance Directive
Under NO circumstances should this palette be replaced with generic blues, greens, or unrelated enterprise corporate palettes. All SVGs (`hero.svg`, `about-life.svg`, `stack.svg`, `id-dashboard.svg`, `connect.svg`) must strictly utilize these exact hex codes.
""")
print("Generated:", color_spec_path)

# 2. reports/reference-reproduction-spec.md
spec_path = reports_dir / "reference-reproduction-spec.md"
with open(spec_path, "w", encoding="utf-8") as f:
    f.write("""# Reference Reproduction Specification

**Reference Target**: `https://github.com/Meghamittal0920/Meghamittal0920.git`  
**Target Profile**: `https://github.com/ha4kerspidersks`  
**Date**: October 2026  

---

## 1. Architectural Blueprint & Dimensions

| Section | Source File | Canvas Dimensions | Visual Architecture | Adaptations for Subhajit Kar |
|:---|:---|:---:|:---|:---|
| **1. Hero** | `hero.svg` | `1280 x 540` | Camera HUD on left (`REC`, `HELLO.MP4 · 24FPS`, `OPEN TO COLLABS`, Name in Space Grotesk, role cycle). Right side has 46-frame cinematic motion player. | Left: `PORTFOLIO.MP4 · 24FPS`, `OPEN TO COLLABS`, `Hi there, I'm Subhajit Kar`, IAM / Cyber Risk leadership role cycle. Right: Subtle cinematic motion frames generated from Subhajit's authentic portfolio portrait. NO static avatar card. |
| **2. About Split** | `about-life.svg` | `1280 x 640` | Dual browser window containers. Left: `// DEVELOPER` (What I build - 3 cards). Right: `// OFF THE CLOCK` (Life beyond code - 3 cards). | Dual browser windows. Left: `// IDENTITY ARCHITECT` (Zero-Trust IAM, 300K+ Reconciliation, Saviynt & Cloud). Right: `// LEADERSHIP & RESEARCH` (13x Deloitte Awards, NFSU M.Tech Cyber Security, Automotive CAN Bus intrusion detection). |
| **3. Tech Stack** | `stack.svg` | `1280 x 520` | Unified technology wall. Left: Atomic orbital constellation. Right: Technology card grid with exact borders, glows, and badges. | Complete 56-technology constellation featuring all verified skills from Subhajit's portfolio. Zero category headings, exactly matching reference density and geometry. |
| **4. ID Dashboard** | `id-dashboard.svg` | `1280 x 600` | Left: Swinging lanyard badge with holographic chip and barcode. Right: Developer dashboard with rolling counters, commit progress, and language distribution. | Left: Enterprise Zero-Trust Identity Security Token / Deloitte Clearance smartcard. Right: Verified metrics (300K+ Identities Secured, 13 Deloitte Awards, 3+ Years Exp, 56 Verified Technologies, Education & Security Clearances). |
| **5. Featured Builds** | `README.md` | Markdown Table | 4-column table: `Project \| What it is \| Stack \| Stars` | Curated showcase of Subhajit's authentic repositories & portfolio projects (AI Dev Team, Automotive CAN Bus IDS, Saviynt Automation, etc.) formatted identically. |
| **6. 3D Contribution City** | `profile-3d.yml` | Full Width SVG | `profile-3d-contrib/profile-night-view.svg` with isometric commit skyline. | Direct integration of automated daily 3D contribution skyline workflow for `ha4kerspidersks`. |
| **7. Connect Section** | `connect.svg` | `1280 x 470` | Left: Floating glowing isometric visual. Right: `// LET'S CONNECT` header with 4 interactive connection cards (`GitHub`, `LinkedIn`, `Portfolio`, `Email`). | Left: Glowing holographic Cyber Key / Zero-Trust nexus. Right: Subhajit's verified channels (LinkedIn, GitHub, Portfolio, Email) + Shields.io badges + profile view counter. |

---

## 2. Typography Standard
All SVGs embed or declare the reference font system:
- **Display Headings**: `Space Grotesk Bold` (`.sg`), `Space Grotesk Medium` (`.sgm`), fallback to `'Segoe UI', Helvetica, Arial, sans-serif`.
- **Monospace & Metadata**: `JetBrains Mono` (`.jb`), `JetBrains Mono Bold` (`.jbb`), fallback to `ui-monospace, Menlo, Consolas, monospace`.
- **Font Sizes**:
  - Section Tag: `12.5px`, `letter-spacing: 2.2px` (uppercase)
  - Section Title: `29px` - `31px`, `letter-spacing: -0.5px`
  - Card Titles: `16px` - `17px`
  - Metric Big Numbers: `36px`
  - Badges & Micro-labels: `9.5px` - `10.5px`, `letter-spacing: 1.2px` - `1.6px`

---

## 3. Animation Principles
- **CSS Keyframes**: `fadeUp` (`animation: fadeUp .7s cubic-bezier(.2,.8,.2,1) both`), `fadeIn`, `pulse` (2-way opacity ping), `ring` (expanding radar ring).
- **SMIL Opacity Sequencing**: Used for video frame playback in `hero.svg` and rolling counters in `id-dashboard.svg`.
- **Performance**: Zero heavy external JavaScript; purely native browser-compatible SVG animations that execute smoothly in GitHub READMEs.
""")
print("Generated:", spec_path)
