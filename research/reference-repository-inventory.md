# Reference Repository Inventory & Technical Analysis
**Repository**: `https://github.com/Meghamittal0920/Meghamittal0920.git`  
**Working Copy**: `/Users/subhajkar/Developer/GitHub-Profile-Transformation/reference-base/`  

---

## Comprehensive Component Inventory

### 1. `README.md`
- **FILE**: `README.md`
- **PURPOSE**: Master profile entrypoint for GitHub user profile page.
- **USED BY**: GitHub profile page renderer (`github.com/username`).
- **VISUAL ROLE**: Defines page layout, section sequence, centered presentation, projects table, 3D contribution city, contact cards, profile badges, and view counter.
- **DEPENDENCIES**: `hero.svg`, `about-life.svg`, `stack.svg`, `id-dashboard.svg`, `connect.svg`, `profile-3d-contrib/profile-night-view.svg`.
- **GENERATION METHOD**: Hand-authored GitHub Flavored Markdown with embedded HTML and SVG image links.
- **REUSABLE?**: YES (Structural markdown and table layout).
- **REQUIRES TRANSFORMATION?**: YES — Replace all personal projects, anime themes, links, and text with Subhajit Kar's verified portfolio and GitHub data.
- **LICENSE STATUS**: `REUSE_WITH_ATTRIBUTION`.

---

### 2. `hero.svg`
- **FILE**: `hero.svg` (1280 x 540)
- **PURPOSE**: Video hero banner with camera viewfinder HUD, typed introduction, animated gradient name, cycling roles, and metadata row.
- **USED BY**: `README.md` (Top banner).
- **VISUAL ROLE**: Primary visual hook and identity presentation.
- **DEPENDENCIES**: Inlined WOFF2 fonts (`Space Grotesk`, `JetBrains Mono`), embedded JPEG frames.
- **GENERATION METHOD**: SVG 1.1 + CSS3 keyframes + SMIL `<animate>` discrete frame switcher.
- **REUSABLE?**: YES — Complete SVG architecture, HUD graphics, CSS styles, timing, and SMIL framework.
- **REQUIRES TRANSFORMATION?**: YES — Replace 46 female video frames with Subhajit's 30 male character frames; update text to "Subhajit Kar", roles to IAM Architect, location, and bio.
- **LICENSE STATUS**: `REUSE_WITH_ATTRIBUTION`.

---

### 3. `about-life.svg`
- **FILE**: `about-life.svg` (1280 x 640)
- **PURPOSE**: Dual-panel capability and lifestyle showcase.
- **USED BY**: `README.md` (Section 2).
- **VISUAL ROLE**: 
  - Left panel: Browser window with URL bar, traffic lights, cursor, and 3 capability rows.
  - Right panel: 3-slide carousel with Instagram-style segmented progress bars, captions, and 3 animated daily rings.
- **DEPENDENCIES**: Inlined WOFF2 fonts, SVG declarative animations (`animateTransform`, `animate`).
- **GENERATION METHOD**: Pure vector SVG + SMIL / CSS keyframes.
- **REUSABLE?**: YES — Dual-card layout, browser window frame, URL bar, carousel timing, progress bar animations, and daily ring mechanics.
- **REQUIRES TRANSFORMATION?**: YES — Replace personal drawing and female character with Subhajit's Enterprise IAM Architecture; replace personal hobbies (skating/anime/ramen) with verified cyber research & governance SLA.
- **LICENSE STATUS**: `REUSE_WITH_ATTRIBUTION`.

---

### 4. `stack.svg`
- **FILE**: `stack.svg` (1280 x 480 / 1280 x 766)
- **PURPOSE**: Orbital technology visualization and categorized chip grid.
- **USED BY**: `README.md` (Section 3).
- **VISUAL ROLE**: Left: Central glowing atom core (`</>`) with 3 tilted elliptical orbits carrying brand icons. Right: Grouped chip grid with sequential glowing border animations.
- **DEPENDENCIES**: Simple Icons SVG brand paths, Inlined WOFF2 fonts.
- **GENERATION METHOD**: SVG vector geometry + CSS keyframe glow pulses.
- **REUSABLE?**: YES — Atom core visual, orbital paths, chip grid geometry, glowing animation.
- **REQUIRES TRANSFORMATION?**: YES — Expand technology list to include ALL 56 verified portfolio technologies without omissions; update headers to Subhajit's domain.
- **LICENSE STATUS**: `REUSE_WITH_ATTRIBUTION`.

---

### 5. `id-dashboard.svg`
- **FILE**: `id-dashboard.svg` (1280 x 600)
- **PURPOSE**: Executive telemetry console and swinging smartcard clearance badge.
- **USED BY**: `README.md` (Section 4).
- **VISUAL ROLE**: 
  - Left: Hanging lanyard with printed strap text, metal clasp, pendulum physics swing (`drop` + `sway`), card frame with orbiting white dot, gold smart chip, barcode, and holographic foil sweep.
  - Right: 4 count-up KPI tiles, horizontal single-hue repository star bar chart, and "Now" active focus panel.
- **DEPENDENCIES**: Inlined WOFF2 fonts, embedded photo asset, CSS pendulum keyframes.
- **GENERATION METHOD**: SVG vector + base64 image + CSS animation + SMIL count-ups.
- **REUSABLE?**: YES — Lanyard mechanics, physics formulas, smartcard structure, telemetry cards, bar chart layout.
- **REQUIRES TRANSFORMATION?**: YES — Replace photo with stylized male character portrait; remove all Deloitte branding; update KPIs (300K+ identities, 13 awards), top repos, and active focus.
- **LICENSE STATUS**: `REUSE_WITH_ATTRIBUTION`.

---

### 6. `connect.svg`
- **FILE**: `connect.svg` (1280 x 470)
- **PURPOSE**: Contact footer and connection call-to-action.
- **USED BY**: `README.md` (Section 7).
- **VISUAL ROLE**: Left: Character in pointing pose. Right: 4 glass connection cards with brand icons and nudging arrows.
- **DEPENDENCIES**: Inlined WOFF2 fonts, embedded character graphic.
- **GENERATION METHOD**: SVG vector + embedded graphic + CSS float/arrow animations.
- **REUSABLE?**: YES — Card background, glowing aura, 4 glass card layout, arrow animations.
- **REQUIRES TRANSFORMATION?**: YES — Replace female character with full-body male character in pointing pose; replace social links with Subhajit's verified channels.
- **LICENSE STATUS**: `REUSE_WITH_ATTRIBUTION`.

---

### 7. `profile-3d-contrib/` & `profile-3d.yml`
- **FILE**: `profile-3d.yml` and `profile-3d-contrib/profile-night-view.svg`
- **PURPOSE**: Daily automated isometric 3D city generation from GitHub commits.
- **USED BY**: `README.md` (Section 6) and GitHub Actions.
- **VISUAL ROLE**: 3D night-view isometric city visualization of contribution history.
- **DEPENDENCIES**: `yoshi389111/github-profile-3d-contrib` GitHub Action.
- **GENERATION METHOD**: Automated workflow run via cron / dispatch.
- **REUSABLE?**: YES — Workflow syntax and action parameters.
- **REQUIRES TRANSFORMATION?**: YES — Configure username to `ha4kerspidersks`.
- **LICENSE STATUS**: `REUSE_ALLOWED` (MIT License).

---

### 8. Supporting Assets & Legacy Files
- **FILES**: `megha-banner.svg`, `megha-banner-light.svg`, `megha-lanyard.svg`, `megha-stats.svg`, `megha-langs.svg`, `megha-trophies.svg`.
- **PURPOSE**: Legacy profile generation components (previous versions).
- **USED BY**: Deprecated / unused by current reference `README.md`.
- **VISUAL ROLE**: Fallback / legacy cards.
- **REUSABLE?**: NO — Superseded by the unified 5-card architecture.
- **REQUIRES TRANSFORMATION?**: NO — Retained in `reference-base` for reference only.
- **LICENSE STATUS**: `DO_NOT_REUSE`.
