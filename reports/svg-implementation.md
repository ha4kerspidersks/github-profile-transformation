# SVG Implementation & GitHub Compliance Specification

## 1. Zero JavaScript Dependency Invariant
GitHub README Markdown is aggressively sanitized:
- Any `<script>` tag is stripped immediately.
- Inline event handlers (`onload`, `onclick`, `onmouseover`) are excised.
- Foreign objects and iframes pointing to external runtimes are blocked.

**Solution**: All animations are implemented exclusively using:
1. **Declarative SMIL (Synchronized Multimedia Integration Language)**:
   - `<animate attributeName="...">`
   - `<animateTransform attributeName="...">`
   - `<animateMotion dur="..." repeatCount="...">`
   - `<set attributeName="...">`
2. **CSS3 Animation & Keyframes**:
   - `@keyframes` for continuous ambient oscillations, glowing pulses, and swinging physics.
   - `@media (prefers-reduced-motion: reduce)` accessibility overrides.

---

## 2. Font Embedding Strategy (Inlined Base64 WOFF2)
Because GitHub blocks external `@import url('https://fonts.googleapis.com/...')` via Content Security Policy (CSP), external fonts will silently fall back to system sans-serif or serif.

To guarantee 1:1 identical typography across all operating systems:
- Reference WOFF2 fonts are extracted and base64-encoded directly into each SVG's `<style>` block via `scripts/shared_svg_fonts.py`:
  - `SG`: Space Grotesk Bold 700 (Display headers and name titles)
  - `SGM`: Space Grotesk Medium 500 (Subtitles, body descriptions)
  - `JBM`: JetBrains Mono Regular 400 (Terminal labels, code metadata)
  - `JBMB`: JetBrains Mono Bold 700 (HUD indicators, status tags)

---

## 3. Self-Contained Base64 Asset Inlining
- **No External Image URLs**: Zero references to external CDNs, Imgur, or third-party image hosts inside SVGs.
- **Embedded Payloads**:
  - `assets/hero.svg`: 30 JPEG frames inlined as base64 data URIs.
  - `assets/id-dashboard.svg`: Character ID badge portrait inlined as base64 data URI.
  - `assets/connect.svg`: Male pointing character inlined as base64 data URI.
- **Asset Size Budget**:
  - `hero.svg`: 457.4 KB (< 500 KB target)
  - `about-life.svg`: 42.7 KB
  - `stack.svg`: 155.1 KB
  - `id-dashboard.svg`: 65.1 KB
  - `connect.svg`: 99.2 KB
  - Total README Bundle: ~820 KB (well within GitHub's 2MB rendering budget).

---

## 4. SMIL Timing and Static Fallback Rules
To prevent rendering glitches on browsers that don't support or delay SMIL:
1. **Timelines Begin at `0s`**: All `<animate>` and `<set>` elements begin at `begin="0s"`.
2. **KeyTimes for Delays**: Animation timing offsets are defined via normalized `keyTimes` (e.g., `keyTimes="0;0.4167;1"`), rather than delayed `begin="2s"`.
3. **`animation-fill-mode: both`**: Ensures that initial and final CSS keyframe styles are applied both before animation starts and after it ends.
4. **Instant Initial Opacity**: In `hero.svg`, Frame 0 has `opacity="1"` hardcoded on the `<image>` element, preventing any initial flicker or blank card render.

---

## 5. Namespace ID Isolation
When multiple SVGs are embedded into the same HTML or Markdown document, global ID collisions can cause styles and gradients in one SVG to bleed into another.

To guarantee complete isolation, each SVG utilizes namespaced element IDs:
- **Hero**: `nameG`, `vmask`, `vmaskB`, `dots`, `blur60`, `hiClip`, `nameClip`
- **About Life**: `ab_cardbg`, `ab_leftWindow`, `ab_rightWindow`, `ab_dots`, `ab_glow`
- **Stack**: `st_bg`, `st_coreGlow`, `st_orbitPath1`, `st_orbitPath2`, `st_orbitPath3`
- **Dashboard**: `id_strapG`, `id_metal`, `id_idbg`, `id_ringG`, `id_chipG`, `id_photoClip`
- **Connect**: `cn_cardbg`, `cn_edge`, `cn_glowNexus`, `cn_dots`

---

## 6. Aggressive GitHub Camo Cache-Busting
GitHub uses `camo.githubusercontent.com` to proxy and cache images aggressively. If an SVG is updated in the repository, GitHub may serve the cached version indefinitely.

**Standard Deployment Protocol**:
1. Commit and push the updated SVG assets first.
2. Update the README image links with an incremented query string:
   - `<img src="assets/hero.svg?v=3" ... />`
   - `<img src="assets/about-life.svg?v=3" ... />`
   - `<img src="assets/stack.svg?v=3" ... />`
   - `<img src="assets/id-dashboard.svg?v=3" ... />`
   - `<img src="assets/connect.svg?v=3" ... />`
3. Commit and push the README file second.
