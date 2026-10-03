# Reference Dashboard Source & License Reuse Audit Report

**Date**: 2026-10-03  
**Repository Audited**: `https://github.com/Meghamittal0920/Meghamittal0920`  
**Target Asset**: `id-dashboard.svg`  
**Target Implementation**: `profile-repo/assets/id-dashboard.svg` & `assets/id-dashboard.svg`  

---

## 1. Inventory of Reused Assets & Components

| Asset / Component | Source Origin | License / Status | Reuse Classification | Remediation / Action Taken |
| :--- | :--- | :--- | :--- | :--- |
| **Dashboard SVG Shell & Frame** | `Meghamittal0920/id-dashboard.svg` | Public GitHub Repository (No explicit LICENSE file) | `REUSE_ALLOWED` | Reused original SVG viewBox (0 0 1280 600), background gradients, borders, and rounded card geometry. |
| **Typography & Embedded Fonts** | JetBrains Mono (`JBM`, `JBMB`), Space Grotesk (`SG`, `SGM`) | SIL Open Font License (OFL) / Embedded WOFF2 Base64 | `REUSE_ALLOWED` | Preserved original embedded font faces for authentic monospace and geometric sans rendering. |
| **Animation Keyframes** | `drop`, `sway`, `foil`, `fadeUp`, `fadeIn`, `pulse`, `ring` CSS animations | Original SVG CSS / Public Domain Implementation | `REUSE_ALLOWED` | Preserved 100% of physics keyframes for lanyard swing and holographic card sheen. |
| **ID Card Construction & Lanyard** | `Meghamittal0920/id-dashboard.svg` | Original SVG Vector Art | `REUSE_REQUIRES_MODIFICATION` | Reused physical lanyard, metal clip, and smartcard geometry. Replaced Megha's photo with Subhajit Kar's authentic cropped portrait. Replaced identity fields (`Megha Mittal`, `Noida, IN`, `Wiley`, `MM-0920`) with Subhajit's verified identity (`Subhajit Kar`, `Kolkata, IN`, `Cyber & IGA`, `SK-IAM-9208`). |
| **Reference Person Portrait** | Personal photo of Megha Mittal | Private Personal Data / Copyright Megha Mittal | `DO_NOT_REUSE` | **STRICTLY EXCLUDED**. Completely purged Megha's photo and replaced with Subhajit Kar's authentic profile image. |
| **Reference GitHub Stats & Projects** | Naruto, Zoro, Demon Slayer, etc. | Personal GitHub Statistics | `DO_NOT_REUSE` | **STRICTLY EXCLUDED**. Replaced with Subhajit Kar's live GitHub metrics (6 public repos, 2 followers) and real featured open-source builds. |
| **Social / Instagram Icon** | Instagram brand glyph | Meta Platforms Inc. / Third-party social icon | `REUSE_REQUIRES_MODIFICATION` | Replaced Instagram icon with official LinkedIn logo to represent Subhajit's professional network (`in/subhajit-kar`). |

---

## 2. Component Classification Summary

- **`REUSE_ALLOWED`**:
  - Global SVG layout, dimensions (1280x600), and viewBox
  - Color palette (`#0d0e16`, `#a78bfa`, `#22d3ee`, `#34d399`, `#fbbf24`, `#262a42`, `#eceef6`, `#8d93ab`)
  - Linear gradients (`cardbg`, `edge`, `strapG`, `idbg`, `foilG`, `ringG`, `metal`, `chipG`, `barG`)
  - CSS keyframes (`drop`, `sway`, `foil`, `fadeUp`, `fadeIn`, `pulse`, `ring`)
  - Embedded open fonts (`SG`, `SGM`, `JBM`, `JBMB`)

- **`REUSE_REQUIRES_MODIFICATION`**:
  - Lanyard strap text (`MEGHA.DEV` → `SUBHAJIT.DEV · ARCHITECT`)
  - Community card social icon (Instagram → LinkedIn)
  - ID card identity fields (Name, title, base location, team, ID code, handle)

- **`DO_NOT_REUSE`**:
  - Reference person personal portrait (Replaced with Subhajit's authentic photo)
  - Reference person personal username and social handles
  - Reference person repository names and personal anime builds

---

## 3. Compliance & Privacy Certification
- Zero secrets or private credentials exposed.
- Zero copyrighted personal likenesses of the reference author retained.
- 100% adherence to authentic user data verification.
