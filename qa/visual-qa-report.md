# Visual QA & Multi-Viewport Verification Report

**Target Profile**: Subhajit Kar (`ha4kerspidersks`)  
**Reference Benchmark**: `https://github.com/Meghamittal0920/Meghamittal0920.git`  
**Test Engine**: Playwright Headless Browser with High-DPI Capture (`deviceScaleFactor: 2`)  
**Date**: October 2026  

---

## 1. Viewport Test Matrix

| Viewport Category | Resolution | Device Emulated | Screenshot Artifact | Status | Visual Fidelity |
|:---|:---:|:---|:---|:---:|:---:|
| **Desktop Dark** | `1280 x 800` | High-DPI Desktop Display | `preview/preview-dark-desktop.png` | **PASS** | 1:1 Pixel-level symmetry |
| **Desktop Light** | `1280 x 800` | Light-Mode Browser Frame | `preview/preview-light-desktop.png` | **PASS** | High contrast borders preserved |
| **Tablet Dark** | `768 x 1024` | iPad / Medium Tablet | `preview/preview-dark-tablet.png` | **PASS** | Responsive downscaling; no clipping |
| **Mobile Dark** | `390 x 844` | iPhone 14 Pro Mobile Viewport | `preview/preview-dark-mobile.png` | **PASS** | 100% fluid SVG downscaling |

---

## 2. Component-Level Visual Audit

1. **Hero Banner (`assets/hero.svg`)**:
   - Camera HUD corners aligned at `(30, 50)`, `(1250, 50)`, `(30, 490)`, `(1250, 490)`.
   - Recording pulse indicator `#ef4444` blinking seamlessly.
   - Name title in Space Grotesk Bold with animated gradient transform (`#22d3ee` -> `#a78bfa` -> `#f472b6`).
   - Role cycle text transitions smoothly through 4 roles over 12s.
   - Right-side video frame player renders Subhajit's authentic portrait motion sequence with zero flickering or ghosting.
   - Zero static portrait card present in the README.

2. **Dual-Window Split Panel (`assets/about-life.svg`)**:
   - Exact 1280x640 canvas with two side-by-side browser windows (620px each).
   - Left window: Enterprise IAM Architecture, Saviynt JML, 300K+ Reconciliation, SoD Compliance.
   - Right window: 13x Deloitte Awards, NFSU Scholar, CAN Bus Intrusion Defense.
   - Window control dots (red, yellow, green) and URL bars rendered with pixel precision.

3. **Technology Constellation Wall (`assets/stack.svg`)**:
   - Exactly 56 verified technologies arranged in an 8x7 unified grid.
   - Zero category headings or artificial partitions.
   - Vector logos crisp at 28x28 within 38x40 container.
   - Primary skills highlighted with glowing indicator and cyan border.

4. **Dashboard & Smartcard (`assets/id-dashboard.svg`)**:
   - Left side: Swinging Zero-Trust Security Clearance smartcard with metallic clip, lanyard strap, RFID waves, and barcode.
   - Right side: 4 metric KPI tiles (`300K+`, `13`, `3+ YRS`, `56`) with rolling counters.
   - Bottom breakdown containers for credentials and pipeline telemetry.

5. **Featured Builds Table (`README.md`)**:
   - 4-column GitHub markdown table: Project | What it is | Stack | Stars.
   - Verified links to active repositories.

6. **3D Contribution City (`profile-3d-contrib/profile-night-view.svg`)**:
   - Night-view isometric skyscraper skyline displaying GitHub contribution density.

7. **Connect Section (`assets/connect.svg`)**:
   - Floating glowing isometric Zero-Trust Nexus visual.
   - 4 interactive connection cards (GitHub, LinkedIn, Email, Portfolio) with animated stroke highlights and arrow shifts.
   - Color-matched Shields.io badges and profile view counter.
