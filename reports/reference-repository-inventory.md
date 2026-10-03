# Reference Repository Inventory & Technical Analysis

## 1. Inventory Summary
This document catalogs every artifact in `reference-base/` (cloned from `https://github.com/Meghamittal0920/Meghamittal0920.git`), analyzing its role, legal reuse status, and transformation requirements for Subhajit Kar's profile.

---

## 2. File-by-File Catalog & Transformation Matrix

| File Path | File Size | Architectural Role | Reusable Implementation | Personal Content to Remove | Transformation Action |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **`README.md`** | 2.8 KB | Main profile orchestrator | Centered layout, table formatting, 3D city integration, badge styles | Personal bio, anime projects table, author's social links | Adopt markdown structure; replace table with Subhajit's 5 verified repos; replace links. |
| **`hero.svg`** | 493.2 KB | Animated viewfinder hero (`1280x540`) | Corner brackets, REC dot, timecode, scrubber bar, SMIL frame switching, name gradient, role cycle | 46 female video frames, "Megha Mittal" text, "Frontend Developer" role | Adopt exact SVG defs, styles, HUD markup; embed Subhajit's 30 male character frames; update text. |
| **`about-life.svg`** | 1,079.9 KB | Dual-panel card (`1280x640`) | Left browser window chrome (URL bar, traffic lights, cursor, capability rows) + Right Instagram carousel (progress segments, daily rings) | Embedded raster female illustration, personal hobbies (sketching, anime, travel) | Adopt exact card layout, browser frame, and carousel mechanics; replace left art with IAM architecture visual; replace right slides with verified research & leadership. |
| **`stack.svg`** | 99.2 KB | Orbital tech constellation (`1280x766`) | Central glowing atom core, 3 tilted elliptical orbits, orbiting icons, grouped chip grid with glowing borders | Only author's subset of frontend/design technologies (~30 items) | Adopt exact orbital math, core glow, and chip CSS; inject ALL 56 verified portfolio technologies without omissions. |
| **`id-dashboard.svg`** | 137.6 KB | Swinging lanyard & dashboard (`1280x600`) | Pendulum swing animation (`drop` + `sway`), metal clasp, strap text, gold chip, barcode, foil sweep, KPI tiles, bar chart, "now" panel | Author's photo, author's name/ID, generic design stats | Adopt exact lanyard physics, smartcard markup, and dashboard tiles; insert Subhajit's male character portrait; remove Deloitte; insert real metrics (300K+ identities, 13 awards). |
| **`connect.svg`** | 102.2 KB | Contact footer (`1280x470`) | Floating card, glowing aura, 4 glass link cards with brand icons and nudging arrows | Female pointing character, author's links | Adopt exact glass card layout and hover/arrow animations; insert Subhajit's male pointing character; insert verified professional links. |
| **`profile-3d.yml`** | 781 B | Daily cron workflow | GitHub Actions schedule, action runner syntax | Author's username (`Meghamittal0920`) | Adopt workflow; update target username to `ha4kerspidersks`; verify permissions. |
| **`profile-3d-contrib/`** | ~1.8 MB | 3D city contribution SVG assets | Isometric SVG night view rendering output (`profile-night-view.svg`) | Author's past commit graph | Pre-populate night view city; refreshed automatically upon workflow run. |
| **`animated-*-guide.pdf`** | ~29 KB | 2-page and 5-page build guides | Implementation rules, SMIL constraints, prompt recipes | N/A | Retained as primary design and constraint specification. |
| **`megha-*.svg`** | ~300 KB | Legacy profile components | Trophies, stats, language banners | Author's metrics and legacy headers | Deprecated; superseded by the modern 5-card architecture. |

---

## 3. Transformation Strategy Confirmation
- **Do NOT reinvent from scratch**: Directly transform the structural SVG files (`hero.svg`, `about-life.svg`, `stack.svg`, `id-dashboard.svg`, `connect.svg`) from `reference-base/`.
- **Preserve exact vector coordinates, styling, and filter definitions**: Retain `<filter id="blur60">`, `<filter id="glow">`, `<pattern id="dots">`, `<style>`, and font declarations.
- **Surgically update**: Swap the embedded base64 images, update text content, and expand technology counts.
