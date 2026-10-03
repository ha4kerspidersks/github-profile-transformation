# Hero Animation Engineering Report

## 1. Character Synthesis & Identity Fidelity
- **Subject**: Subhajit Kar (`ha4kerspidersks`)
- **Gender**: **Male**
- **Anatomy**: **Full Body** (Head, Torso, Arms, Hands, Legs, Feet)
- **Styling**: Modern cybersecurity & IAM tech aesthetic — dark tech hoodie with subtle cyan/violet cyber trim, dark joggers with cargo utility pockets, low-top sneakers, holding an illuminated cyber-tablet with IAM shield emblem.
- **Reference Portrait Used**: Authentic desk portrait `assets/avatar/icard-photo-original.jpg`.
- **Output Asset**: `assets/hero/source/male-character-fullbody.jpg` (896 x 1200 px).

---

## 2. Frame Extraction & Optimization Pipeline
- **Orchestration Tool**: Playwright Headless Chromium Frame Capturer (`scripts/generate-cinematic-frames.mjs`).
- **Target Dimensions**: `560 x 418` pixels per frame (aspect ratio 1.34:1 matching reference hero SVG `<image x="560" y="0" width="724" height="540">`).
- **Total Frames Generated**: **30 discrete frames** (`frame_000.jpg` to `frame_029.jpg`).
- **Compression**: Optimized baseline JPEG at quality 50.
- **Average Size Per Frame**: ~11 KB.
- **Total Base64 Frame Payload**: ~330 KB.
- **Total Hero SVG Size**: **457.4 KB** (Reference hero: 493.2 KB).

---

## 3. SMIL Animation Architecture & Loop Timing
The timing adheres strictly to the PDF specification (*"about 4s: play once, hold the last frame ~1.4s, fade, repeat"*):

| Timeline Phase | Time Slice | Frames | SMIL KeyTimes | Visual Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **Motion Phase** | `0.0s - 2.6s` | `frame_000` to `frame_019` | `0.000` to `0.650` | Active breathing motion, subtle 1.025x parallax zoom, scanning cyber light sweep, HUD scanline sweep top-to-bottom. |
| **Final Hold Phase** | `2.6s - 3.55s` | `frame_020` to `frame_026` | `0.650` to `0.8875` | Final frame holds steady with full 100% opacity for ~1.0 - 1.4s. |
| **Fade & Reset Phase** | `3.55s - 4.0s` | `frame_027` to `frame_029` | `0.8875` to `1.000` | Smooth fade-out to dark background (`#0d0e16`) and seamless reset for next loop cycle. |

### Discrete SMIL Switching Implementation
Each embedded `<image>` is governed by a discrete `<animate>` node:
```xml
<!-- Frame 0: Visible initially, switches off at t = 0.0333 -->
<image x="560" y="0" width="724" height="540" href="data:image/jpeg;base64,..." opacity="1" preserveAspectRatio="none">
  <animate attributeName="opacity" calcMode="discrete" values="1;0" keyTimes="0;0.0333" dur="4.0s" repeatCount="indefinite"/>
</image>

<!-- Subsequent Frames: Hidden initially, on during [t_start, t_end], off thereafter -->
<image x="560" y="0" width="724" height="540" href="data:image/jpeg;base64,..." opacity="0" preserveAspectRatio="none">
  <animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;0.0333;0.0667" dur="4.0s" repeatCount="indefinite"/>
</image>
```

---

## 4. Camera Viewfinder HUD Elements
1. **Corner Brackets**: 4 animated corner brackets (`M760 74V40H794`, `M1236 74V40H1202`, etc.) drawn via `stroke-dasharray: 60; animation: draw .8s ease both`.
2. **REC Indicator**: Blinking red recording indicator (`<circle cx="782" cy="483" r="5" fill="#ef4444"/>`) with text `REC` and animated timecode `00:04:00`.
3. **Filename Label**: `SUBHAJIT_IAM_CORE.RAW` rendered in JetBrains Mono (`letter-spacing: 2`).
4. **Scrubber Bar**: Synced progress track at bottom of viewfinder with animated scrubber pill travelling from left to right over 4.0s.

---

## 5. Left Column Information Architecture
- **Status Pill**: `OPEN TO COLLABS` with pulsing cyan dot (`#22d3ee`).
- **Typing Intro**: `Hi there, I'm` revealed via expanding clip-path `<clipPath id="hiClip">`.
- **Animated Name**: `SUBHAJIT KAR` rendered in Space Grotesk Bold with dynamic linear gradient `url(#nameG)` (cyan -> violet -> pink).
- **Role Cycle**:
  1. `Lead Identity & Access Management Architect`
  2. `Enterprise Security & Zero Trust Specialist`
  3. `Cloud Security & Governance Engineer`
- **One-line Pitch**: `Architecting scalable Zero-Trust Identity governance and secure cloud ecosystems.`
- **Metadata Badges**: `📍 Kolkata, India` · `🏢 Enterprise Security` · `⭐ 3+ Yrs Exp / 300K+ Identities`.

---

## 6. Static Fallback Safety
If a browser or markdown viewer disables SMIL animations or SVG animations:
- `animation-fill-mode: both` ensures all keyframe states resolve to their finished appearance.
- Frame 0 begins with `opacity="1"`, guaranteeing an immediate visual render without blank frames.
- Left-side name and role text remain 100% readable and fully opaque.
