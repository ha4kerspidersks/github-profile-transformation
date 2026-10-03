# Reference Color System Specification

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
