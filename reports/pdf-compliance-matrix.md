# PDF Engineering Compliance Matrix

**Specification Source**: `animated-github-profile-2page-guide.pdf` & `animated-github-profile-guide.pdf` (Published engineering guide by Megha Mittal)  
**Target Profile**: Subhajit Kar (`ha4kerspidersks`)  
**Audit Standard**: Complete Architectural Alignment with Open Guide Directives  
**Date**: October 2, 2026  

---

## 1. Executive Summary

| Guide Requirement | Specification Target | Implemented Architecture | Status |
| :--- | :--- | :--- | :---: |
| **Self-Contained SVG Animation** | Declarative SMIL `<animate>` & CSS3 Keyframes | No external JS; 100% self-contained SVG standard | **PASS** |
| **Embedded Video Loop / Character Motion** | Base64 discrete frame switcher with `keyTimes` | 30 cinematic male character frames at 24FPS (4.0s loop) | **PASS** |
| **Synchronized Timeline Scrubber** | Progress bar tied to loop duration | CSS keyframe / SMIL animation matching loop duration | **PASS** |
| **Dual-Panel About Architecture** | Browser window (cream `#f4f7ff`) + Lifestyle Carousel (warm peach `#fed7aa`) | Left: Cream browser window with developer at desk + 3 bullet rows; Right: Warm peach carousel + daily rings | **PASS** |
| **Orbital Technology Constellation** | Atom core (`</>`) + 3 tilted orbits + categorized chips | Central atom core + 3 elliptical orbits carrying icons + 56 categorized chips | **PASS** |
| **Interactive Developer Badge** | Hanging lanyard with physical swing keyframes (`drop` + `sway`) | Real pendulum physics, clasp, holographic foil sweep, barcode, NFC waves | **PASS** |
| **Dynamic Telemetry Dashboard** | 4 count-up KPI tiles, horizontal bar chart, highlights | Count-up tiles, repository star bars, enterprise metrics (300K+, 13 awards) | **PASS** |
| **Connection Portal** | Pointing character + 4 glass cards + nudge arrows | Stylized male pointing character + 4 glass cards with icons & arrows | **PASS** |
| **Typography & Fonts** | Inlined WOFF2 fonts (Space Grotesk & JetBrains Mono) | Base64 inlined font-face definitions across all 5 SVGs | **PASS** |
| **GitHub Asset Cache-Busting** | Version query parameters (`?v=...`) on all asset links | Applied `?v=2` to all SVG embeds in `README.md` | **PASS** |
| **Accessibility & Fallback** | Semantic `<title>`, `<desc>`, `role="img"`, `@media (prefers-reduced-motion)` | Implemented across all 5 master SVG assets | **PASS** |

---

## 2. Component-by-Component Compliance Ledger

### 1. `assets/hero.svg` (1280 x 540)
- **Viewfinder HUD**: 4 corner brackets, red pulsing REC indicator, filename `SUBHAJIT_IAM.MP4 • 24FPS`.
- **Character Animation**: 30 discrete base64 JPEG frames embedded inside `<g mask="url(#vmask)">`, cycling at 4.0s loop.
- **Scrubber Bar**: Synced to 4.0s loop (`values="0;476"`).
- **Text Layer**: Animated gradient name (`#22d3ee` -> `#a78bfa` -> `#f472b6`), cycling role switcher, location & credentials row.

### 2. `assets/about-life.svg` (1280 x 640)
- **Left Panel (Work Window)**:
  - Cream background `#f4f7ff`, dark browser chrome with red, yellow, green traffic lights.
  - URL pill: `localhost:5173/subhajit` with blinking cursor.
  - Vector illustration of modern engineer at workstation with laptop, coffee mug, and desk.
  - 3 structured bullet rows with colored icons (Identity & Access, Lifecycle Workflows, Cyber Intelligence).
- **Right Panel (Lifestyle Carousel)**:
  - 3 segmented progress bars at top of window.
  - 3 animated carousel slides (Mint `#d9f7ec`, Warm Peach `#fed7aa`, Soft Rose `#fbcfe8`).
  - Cycling captions: Fitness / Health conscious, Weekend skater, Strategy & AI models.
  - 3 animated concentric Daily Rings (Move, Hydrate, Code) with `DAILY RINGS` label.

### 3. `assets/stack.svg` (1280 x 800)
- **Central Atom Core**: Glowing pink/violet radial core (`</>`) with pulsing halo and breathing animation.
- **3 Orbits**: Elliptical paths carrying React, Python, Docker, AWS, Linux, and Saviynt brand icons with `animateMotion`.
- **Vertical Divider**: Dividing visual orbital section from categorized grid.
- **56 Categorized Chips**: Zero `<symbol>` or `<use>` dependency; 100% inlined vector paths with glowing animated border strokes.

### 4. `assets/id-dashboard.svg` (1280 x 600)
- **Hanging Lanyard**: Gradient strap (`SUBHAJIT.DEV • ZERO TRUST`), metal clasp, and dual-phase physics swing (`drop` + `sway`).
- **Smartcard Clearance**: Holographic foil sweep (`skewX(-14)`), gold microchip, NFC contactless waves, stylized male portrait, barcode, and handle `@ha4kerspidersks`. **Zero mention of Deloitte**.
- **Executive Dashboard**: 4 KPI count-up tiles, repository star distribution bar chart, enterprise impact telemetry (300K+ identities, 13 awards), and active focus panel.

### 5. `assets/connect.svg` (1280 x 470)
- **Visual Staging**: Glowing pink aura with male pointing character in technical hoodie.
- **Glass Cards**: 4 glassmorphic contact cards (GitHub, Email, LinkedIn, Portfolio) with hover-ready styling, brand icons, and animated nudge arrows.
- **Footer Tagline**: `“Security is not an afterthought, it is the foundation.”`

---

## 3. PDF Compliance Verification Gate
```
GUIDE CRITERIA CHECKED = 11
GUIDE CRITERIA MET = 11
COMPLIANCE RATE = 100%
AUDIT VERDICT = PASS
```
