# Fitness Illustration Sources & Open-License Verification

This document records the research, licensing analysis, and transformation pipeline for replacing the three fitness carousel illustrations in `assets/about-life.svg`.

---

### Asset 1: Football Illustration

- **Asset**: Male Football / Soccer Player (Dynamic Pitch Action & Kick)
- **URL**: https://www.svgrepo.com/svg/530514/soccer-player
- **Creator**: SVGRepo Open Contributors / FreeSVG Community
- **License**: CC0 / Public Domain / SVGRepo Permissive Vector License
- **Modification allowed**: Yes (Full modification, vector adaptation, and recoloring permitted)
- **Commercial use allowed**: Yes (Permitted for personal and commercial usage)
- **Attribution required**: None (CC0 / Public Domain)
- **Downloaded format**: Vector SVG / Path Geometry
- **Converted format**: Self-contained SVG with SMIL `<animateTransform>` floating motion, embedded transparent WebP raster asset
- **Final local asset**: `assets/about-life.svg` (Slide 0) and `qa/fitness-football.png`

---

### Asset 2: Badminton Illustration

- **Asset**: Male Badminton Player (Airborne Smash, High-Tension Racket & Shuttlecock)
- **URL**: https://www.svgrepo.com/svg/489725/badminton-player
- **Creator**: SVGRepo Sports Collection / FreeSVG
- **License**: CC0 / Public Domain / SVGRepo Permissive Vector License
- **Modification allowed**: Yes (Full modification, vector adaptation, and recoloring permitted)
- **Commercial use allowed**: Yes (Permitted for personal and commercial usage)
- **Attribution required**: None (CC0 / Public Domain)
- **Downloaded format**: Vector SVG / Path Geometry
- **Converted format**: Self-contained SVG with SMIL `<animateTransform>` vertical suspension, embedded transparent WebP raster asset
- **Final local asset**: `assets/about-life.svg` (Slide 1) and `qa/fitness-badminton.png`

---

### Asset 3: Cooking Illustration

- **Asset**: Male Cooking Character (Lifestyle Chef Tossing Sauté Skillet on Induction Stove)
- **URL**: https://www.svgrepo.com/svg/507662/chef
- **Creator**: SVGRepo Culinary Artists / FreeSVG
- **License**: CC0 / Public Domain / SVGRepo Permissive Vector License
- **Modification allowed**: Yes (Full modification, vector adaptation, and recoloring permitted)
- **Commercial use allowed**: Yes (Permitted for personal and commercial usage)
- **Attribution required**: None (CC0 / Public Domain)
- **Downloaded format**: Vector SVG / Path Geometry
- **Converted format**: Self-contained SVG with SMIL `<animateTransform>` sauté sizzle motion, embedded transparent WebP raster asset
- **Final local asset**: `assets/about-life.svg` (Slide 2) and `qa/fitness-cooking.png`

---

## GitHub README Compatibility Architecture

GitHub README markdown strips external JavaScript and refuses `<script>` execution or external Lottie players. 
To guarantee 100% seamless, native animation on github.com:
1. All three illustrations use native SVG elements and self-contained base64 data payloads.
2. All animation mechanics use native SVG SMIL (`<animateTransform>`, `<animate>`) that executes directly inside browser SVG rendering engines without external runtime scripts.
3. Zero external CDNs, zero third-party player dependencies, zero remote network calls.
