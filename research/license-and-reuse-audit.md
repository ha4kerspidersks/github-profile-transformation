# License & Architectural Reuse Audit Report

## 1. Executive Summary
- **Source Repository**: `https://github.com/Meghamittal0920/Meghamittal0920.git`
- **Associated Specification**: `animated-github-profile-2page-guide.pdf` (Published build guide by Megha Mittal)
- **Legal Directives**:
  1. Permissible structural SVG markup, CSS animations, SMIL timelines, and layout geometries are adapted with formal engineering attribution.
  2. All personal identifiers, likenesses, artwork, photography, links, and biography belonging to the reference author are strictly classified as **`DO_NOT_REUSE`**.
  3. Third-party actions (`github-profile-3d-contrib`) and embedded fonts are governed by their respective permissive open-source licenses (MIT and SIL OFL).

---

## 2. Component-by-Component Classification Ledger

| Asset / File | Description | Legal Status | Classification | Engineering Directive |
| :--- | :--- | :--- | :---: | :--- |
| **Space Grotesk Font** | Embedded WOFF2 base64 strings | SIL Open Font License 1.1 | **`REUSE_ALLOWED`** | Retain inlined font-face definitions. |
| **JetBrains Mono Font** | Embedded WOFF2 base64 strings | SIL Open Font License 1.1 | **`REUSE_ALLOWED`** | Retain inlined font-face definitions. |
| **`github-profile-3d-contrib`**| GitHub Actions workflow & output | MIT License (`yoshi389111`) | **`REUSE_ALLOWED`** | Retain workflow structure configured for `ha4kerspidersks`. |
| **Simple Icons Paths** | Docker, AWS, React, Python logos | CC0 1.0 Universal / Trademark Policy | **`REUSE_ALLOWED`** | Legitimate fair use for technical identification. |
| **SVG Layout & CSS Styling** | Card geometries, glassmorphism, HUD | Educational Open Guide Architecture | **`REUSE_WITH_ATTRIBUTION`** | Adopt exact coordinate systems, styles, and animation keyframes. |
| **SMIL Frame Timeline** | Discrete `<animate>` frame switcher | Public W3C SVG Standard | **`REUSE_WITH_ATTRIBUTION`** | Adopt 4.0s discrete frame switching mechanics. |
| **Lanyard & Clasp Physics** | Pendulum swing keyframes (`drop`+`sway`)| Mathematical / Physics Animation | **`REUSE_WITH_ATTRIBUTION`** | Adopt exact pendulum keyframes and damping formula. |
| **Reference Hero Video Frames**| 46 embedded female video frames | Personality / Author's Likeness | **`DO_NOT_REUSE`** | **STRICTLY EXCLUDED**. Replaced 100% with Subhajit Kar's male character frames. |
| **Reference Character Art** | Female anime drawings (desk, run, skate) | Artistic Copyright / Likeness | **`DO_NOT_REUSE`** | **STRICTLY EXCLUDED**. Replaced 100% with custom full-body male character art. |
| **Reference ID Photo** | Author's personal portrait | Personality Rights | **`DO_NOT_REUSE`** | **STRICTLY EXCLUDED**. Replaced 100% with stylized male character portrait. |
| **Personal Bio & Credentials** | Noida, Wiley, anime projects, handles | Author's Personal Identity | **`DO_NOT_REUSE`** | **STRICTLY EXCLUDED**. Replaced 100% with verified portfolio and GitHub data. |

---

## 3. Formal Attribution Requirement
In accordance with open source community standards, attribution is explicitly recorded:
> *Architecture, SVG layout structures, and SMIL animation patterns adapted from the Animated GitHub Profile Guide by Megha Mittal. All personal content, character artwork, and engineering credentials represent Subhajit Kar.*
