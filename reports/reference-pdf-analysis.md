# Reference PDF Analysis: `animated-github-profile-2page-guide.pdf`

## Executive Summary
This document provides a comprehensive, section-by-section extraction and mapping of all implementation requirements defined in the primary reference document: **`animated-github-profile-2page-guide.pdf`** (authored as *ANIMATED GITHUB PROFILE // BUILD GUIDE · 2 PAGES · NO CODING REQUIRED*).

---

## Page-by-Page Extraction & Implementation Matrix

| PDF Section | Requirement | Reference Implementation | Required Technology | GitHub Constraint | Mapping to Subhajit Kar's Profile | Implementation Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Page 1: Overview** | Turn profile into an animated portfolio with pure SVG | Pure SVG file bundle loaded in README.md | SVG 1.1, CSS3, SMIL | GitHub sanitizes `<script>` and iframe tags; only SVG + CSS/SMIL survives | Fully self-contained SVGs with zero external JS runtime dependencies | **COMPLIANT** |
| **Page 1: What You Get (Hero)** | Video hero framed like camera viewfinder | 46 embedded frames cycling via SMIL | SMIL `<set attributeName="opacity">`, CSS animation | Image size limits, cache-busting required | Full-body male character video loop with HUD viewfinder, REC dot, scrubber | **IN PROGRESS (V3 Male Character)** |
| **Page 1: What You Get (Panels)** | Two panels: what you build + hobbies carousel | Dual cards inside `about-life.svg` | SVG layout, CSS cross-fade, segment progress bars | Cannot execute JS timers; must use keyframed CSS / SMIL | Left: Enterprise IAM & Architecture browser card; Right: Cyber Research & Innovation carousel | **COMPLIANT** |
| **Page 1: What You Get (Tech Orbit)** | Real brand icons circling an atom core + chip grid | 3 tilted elliptical orbits, glowing core, chip wall | SVG `<animateMotion>` on `<path>`, SVG filter glow | Performance overhead with many SVG filter elements | 56 verified portfolio technologies mapped without arbitrary omissions | **COMPLIANT** |
| **Page 1: What You Get (ID Badge)** | Swinging holographic card with live stats & project chart | Damped pendulum swing, metallic clasp, barcode | CSS `@keyframes sway`, SVG linear gradients | Strict origin isolation | Swinging lanyard card with male character portrait, KPI tiles, starred repos chart, NO Deloitte text | **COMPLIANT** |
| **Page 1: What You Get (3D City)** | 3D skyline built from commits, refreshed daily | GitHub Actions workflow outputting 3D isometric city SVG | `yoshi389111/github-profile-3d-contrib` | GITHUB_TOKEN permissions, workflow permissions | Reusable GitHub Actions workflow configured in `.github/workflows/profile-3d.yml` | **COMPLIANT** |
| **Page 1: What You Get (Connect)** | Pointing character next to link cards | SVG card with pointing character graphic & link chips | SVG layout, hover-glow styling | Links must be standard `<a>` or markdown clickable badges | Full-body male pointing character with verified LinkedIn, GitHub, Email, Portfolio links | **COMPLIANT** |
| **Page 1: Step 1 (Video)** | Short looping clip (2s max), play once, hold, fade | 46 JPEG frames at 560x418 px | Playwright/Canvas frame generation, JPEG base64 | Payload size must remain under GitHub 2MB rendering soft-limit | 30-40 frames, 4.0s cycle: play motion, hold 1.4s, fade, repeat | **ACTIVE (Updating with Male Character)** |
| **Page 1: Step 2 (Character Art)** | Image Prompt A (ID badge portrait) & Image Prompt B (Pointing pose) | Anime-style developer illustration | Text-to-Image / Native Generative Engine | Transparent or dark background (#0d0e16) | Generated custom male tech character derived from Subhajit's portrait | **COMPLETED** |
| **Page 2: Style & Colors** | "Midnight Glass" cards (`#0d0e16`), aurora accent ramp | Cyan `#22d3ee`, Violet `#a78bfa`, Pink `#f472b6` | CSS custom tokens, radial/linear gradients | Visual contrast across light/dark GitHub themes | Exact reference hex codes applied across all SVGs | **COMPLIANT** |
| **Page 2: Typography** | Embedded display font and mono font as base64 WOFF2 | Space Grotesk (`SG`, `SGM`) + JetBrains Mono (`JBM`, `JBMB`) | `@font-face` with inline base64 WOFF2 strings | External web fonts fail to load due to CSP | Inlined base64 WOFF2 in `<style>` of each SVG | **COMPLIANT** |
| **Page 2: Hero Architecture** | Viewfinder brackets, REC dot, filename label, scrubber, collabs pill, typing intro, animated name gradient | Corner bracket paths, blinking REC, animated mask for name, cycling roles | SVG `<mask id="reveal">`, SMIL keyTimes | Rendering glitches if SMIL does not start at 0s | Exact camera HUD and left-side typography layout matching reference | **COMPLIANT** |
| **Page 2: Tech Stack Architecture** | 3 tilted elliptical orbits around glowing core, grouped chip grid | Atom core with orbiting simple icons + glowing border chips | SVG `<ellipse>`, `<path>`, Simple Icons paths | Path mathematics must avoid icon collisions | Atom core with 3 orbits + 56-tech categorized chip grid | **COMPLIANT** |
| **Page 2: ID Badge Physics** | Damped pendulum swing, strap text, metal clasp, holographic foil sweep | CSS keyframed sway with decreasing amplitude | CSS `transform-origin: top center` | CSS transform origin must be absolute in SVG | Swinging lanyard, holographic foil linear gradient sweep, male character | **COMPLIANT** |
| **Page 2: Rules That Keep It Working** | 1. Only CSS + SMIL<br>2. Nothing loaded from network<br>3. PNG/JPEG inline base64<br>4. `animation-fill-mode: both`<br>5. SMIL starting at 0s with keyTimes<br>6. Namespaced IDs<br>7. `?v=1` cache-busting | Embedded base64 assets, namespaced IDs (`h_`, `ab_`, `st_`, `id_`, `cn_`) | SVG architecture rules | Aggressive GitHub image proxy caching (camo.githubusercontent.com) | Full compliance verified by `scripts/validate.py` | **COMPLIANT** |

---

## Detailed Section Mapping

### 1. Hero (`hero.svg`)
- **Dimensions**: `1280 x 540`
- **Left Column**:
  - Open to collabs status pill with pulsing cyan indicator.
  - Subtitle: `Hi there, I'm` typed intro.
  - Name: `SUBHAJIT KAR` with aurora gradient fill (cyan -> violet -> pink).
  - Cycling role lines:
    1. `Lead Identity & Access Management Architect`
    2. `Enterprise Security & Zero Trust Specialist`
    3. `Cloud Security & Governance Engineer`
  - Concise Pitch: `Architecting scalable Zero-Trust Identity governance and secure cloud ecosystems.`
  - Meta Row: `📍 Kolkata, India` · `🏢 Enterprise Security` · `⭐ 3+ Yrs Exp / 300K+ Identities`
- **Right Column**:
  - Camera Viewfinder HUD:
    - Top-left corner bracket, Top-right corner bracket, Bottom-left, Bottom-right (`#22d3ee`).
    - Flashing red/cyan `● REC` indicator with `00:04:00` timecode.
    - Filename label: `SUBHAJIT_IAM_CORE.RAW`.
    - Scrubber bar running along bottom edge of viewfinder synced to 4.0s loop.
  - Motion Character:
    - Full-body male character in dark tech hoodie, joggers, sneakers, holding glowing IAM cyber-tablet.
    - Discrete SMIL frame sequence (4.0s total cycle: 2.6s motion, 1.4s final hold, fade, repeat).

### 2. Capability & Research (`about-life.svg`)
- **Dimensions**: `1280 x 640`
- **Left Panel (Browser Architecture View)**:
  - Title: `Enterprise Architecture & Governance`
  - Browser chrome: URL bar `https://identity.governance/zero-trust`, traffic lights, blinking cursor.
  - Capability Rows:
    1. Identity Lifecycle Management (JML workflows, SailPoint IIQ & ISC)
    2. Zero Trust & Cloud IAM (AWS IAM, Azure AD / Entra ID, GCP IAM)
    3. Access Certification & SOD (Compliance, Audit, Least Privilege)
- **Right Panel (Innovation & Research Carousel)**:
  - Title: `Cyber Research & Innovation`
  - Instagram-style segmented progress bars (3 segments, 4s cycle).
  - Daily Activity Rings: Identity Analytics, Cloud Governance, Security Automation.
  - Research Captions: AI in Identity Governance, Threat Detection, Automated RBAC.

### 3. Tech Stack Orbit & Chip Wall (`stack.svg`)
- **Dimensions**: `1280 x 766`
- **Core Atom System**:
  - Central glowing cyber core (`#22d3ee` + `#a78bfa` aura).
  - 3 tilted elliptical orbits carrying key platform icons (SailPoint, AWS, Python, Azure, Linux, Docker).
- **Grouped Chip Grid (56 Verified Portfolio Technologies)**:
  - All 56 technologies from portfolio manifest included with real logos.
  - Staggered glowing border animations using CSS keyframes.

### 4. ID Badge & Analytics Dashboard (`id-dashboard.svg`)
- **Dimensions**: `1280 x 600`
- **Swinging ID Badge**:
  - Lanyard strap with printed text: `IDENTITY ARCHITECT // ZERO TRUST VERIFIED`.
  - Realistic metallic clasp and eyelet.
  - Character photo frame: Uses the generated **male character illustration** (NO static desk photograph, NO female reference art).
  - Security chip: Gold contact pad with circuit lines.
  - Barcode & Holographic foil sweep line moving across the badge.
  - **Zero Deloitte branding**: Badge header reads `ENTERPRISE SECURITY` / `SECURITY ARCHITECT`.
- **Analytics Dashboard**:
  - KPI Tiles:
    - `300K+` Monthly Active Identities
    - `99.98%` Governance SLA
    - `13` Professional & Leadership Awards
    - `3+` Years Enterprise Experience
  - Repository Bar Chart: Single-hue cyan-to-violet gradient bars representing Subhajit's top repositories.
  - "Now / Active Focus" Panel: Current architectural initiatives and certifications.

### 5. Connect Footer (`connect.svg`)
- **Dimensions**: `1280 x 470`
- **Left Column**:
  - Full-body male character in pointing stance, directing viewer towards the link cards.
- **Right Column**:
  - Glass link cards with official brand icons:
    - LinkedIn: `linkedin.com/in/ha4kerspidersks`
    - GitHub: `github.com/ha4kerspidersks`
    - Email: `subhajit.kar@security.internal` / portfolio contact
    - Portfolio: `subhajitkar.dev`

---
*Report generated and validated autonomously against `animated-github-profile-2page-guide.pdf`.*
