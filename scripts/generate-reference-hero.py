import os
import sys
import glob
import base64
from pathlib import Path
from shared_svg_fonts import SHARED_FONTS

HERO_OUTPUT = Path("assets/hero.svg")
HERO_BANNER_OUTPUT = Path("assets/hero-banner.svg")

def generate_reference_hero():
    frames = sorted(glob.glob("assets/hero/generated/frames/*.jpg"))
    if not frames:
        print("❌ No frames found in assets/hero/generated/frames/", file=sys.stderr)
        return False

    total_frames = len(frames)
    duration = 4.0
    print(f"🎬 Compiling {total_frames} cinematic frames into reference-faithful hero SVG...")

    # Calculate SMIL keytimes
    image_tags = []
    for i, frame_path in enumerate(frames):
        with open(frame_path, "rb") as f:
            b64_data = base64.b64encode(f.read()).decode("utf-8")
        
        t_start = i / total_frames
        t_end = (i + 1) / total_frames
        
        if i == 0:
            initial_opacity = "1"
            anim_xml = f'<animate attributeName="opacity" calcMode="discrete" values="1;0" keyTimes="0;{t_end:.4f}" dur="{duration:.1f}s" repeatCount="indefinite"/>'
        else:
            initial_opacity = "0"
            anim_xml = f'<animate attributeName="opacity" calcMode="discrete" values="0;1;0" keyTimes="0;{t_start:.4f};{t_end:.4f}" dur="{duration:.1f}s" repeatCount="indefinite"/>'

        img_tag = f'<image x="560" y="0" width="724" height="540" href="data:image/jpeg;base64,{b64_data}" opacity="{initial_opacity}" preserveAspectRatio="none">{anim_xml}</image>'
        image_tags.append(img_tag)

    all_images_xml = "\n".join(image_tags)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 540" width="1280" height="540" role="img" aria-label="Subhajit Kar — Senior IAM Assistant Manager"><title>Subhajit Kar — Senior IAM Assistant Manager</title><desc>Cinematic animated hero: Subhajit Kar alongside enterprise IAM credentials, role cycle, and camera HUD.</desc><defs><style>{SHARED_FONTS}
text{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.sg{{font-family:'SG','Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}}
.sgm{{font-family:'SGM','Segoe UI',Helvetica,Arial,sans-serif;font-weight:500}}
.jb{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.jbb{{font-family:'JBMB',ui-monospace,Menlo,Consolas,monospace;font-weight:700}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@keyframes ring{{0%{{r:4;opacity:.8}}100%{{r:13;opacity:0}}}}
.fu{{animation:fadeUp .7s cubic-bezier(.2,.8,.2,1) both}}
.fi{{animation:fadeIn .7s ease both}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}

.role{{animation:role 12s cubic-bezier(.2,.8,.2,1) infinite}}
@keyframes role{{0%{{opacity:0;transform:translateY(16px)}}4%{{opacity:1;transform:translateY(0)}}22%{{opacity:1;transform:translateY(0)}}25.5%{{opacity:0;transform:translateY(-16px)}}100%{{opacity:0;transform:translateY(-16px)}}}}
.blob{{animation:drift 14s ease-in-out infinite alternate}}
@keyframes drift{{from{{transform:translate(0,0)}}to{{transform:translate(40px,-30px)}}}}
.blob2{{animation:drift2 16s ease-in-out infinite alternate}}
@keyframes drift2{{from{{transform:translate(0,0)}}to{{transform:translate(-50px,26px)}}}}
.corner{{stroke-dasharray:60;animation:draw .8s ease both}}
@keyframes draw{{from{{stroke-dashoffset:60}}to{{stroke-dashoffset:0}}}}
</style>
<linearGradient id="nameG" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
  <stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/>
  <animateTransform attributeName="gradientTransform" type="translate" values="-.35 0;.35 0;-.35 0" dur="7s" repeatCount="indefinite"/>
</linearGradient>
<linearGradient id="nameG2" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#22d3ee"/><stop offset=".55" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/>
</linearGradient>
<linearGradient id="fadeL" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#000"/><stop offset=".26" stop-color="#fff"/><stop offset="1" stop-color="#fff"/>
</linearGradient>
<linearGradient id="fadeB" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#fff"/><stop offset=".86" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
</linearGradient>
<mask id="vmask" maskUnits="userSpaceOnUse" x="560" y="0" width="724" height="540">
  <rect x="560" y="0" width="724" height="540" fill="url(#fadeL)"/>
</mask>
<mask id="vmaskB" maskUnits="userSpaceOnUse" x="560" y="0" width="724" height="540">
  <rect x="560" y="0" width="724" height="540" fill="url(#fadeB)"/>
</mask>
<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="13" cy="13" r=".9" fill="#ffffff" fill-opacity=".06"/></pattern>
<filter id="blur60" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="card"><rect width="1280" height="540" rx="26"/></clipPath>
<clipPath id="hiClip"><rect x="60" y="130" width="330" height="46"><animate attributeName="width" values="0;0;330" keyTimes="0;.4167;1" dur="1.2s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.3 0 .2 1"/></rect></clipPath>
<clipPath id="nameClip"><rect x="50" y="170" width="560" height="100"><animate attributeName="y" values="262;262;170" keyTimes="0;.5263;1" dur="1.9s" begin="0s" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1"/></rect></clipPath>
</defs>

<g clip-path="url(#card)">
  <rect width="1280" height="540" fill="#0d0e16"/>
  <ellipse cx="180" cy="180" rx="260" ry="200" fill="#22d3ee" fill-opacity=".12" filter="url(#blur60)" class="blob"/>
  <ellipse cx="760" cy="120" rx="300" ry="240" fill="#a78bfa" fill-opacity=".12" filter="url(#blur60)" class="blob2"/>
  <ellipse cx="440" cy="460" rx="280" ry="200" fill="#f472b6" fill-opacity=".09" filter="url(#blur60)" class="blob"/>
  <rect width="1280" height="540" fill="url(#dots)"/>

  <!-- Cinematic Video Frame Player (Subhajit Kar Portrait Motion) -->
  <g mask="url(#vmask)">
    <g mask="url(#vmaskB)">
      {all_images_xml}
    </g>
  </g>

  <!-- Gradient Vignette Edges matching reference -->
  <rect x="560" y="0" width="724" height="540" fill="url(#fadeL)" opacity="0.15"/>
  <rect x="560" y="0" width="724" height="540" fill="url(#fadeB)" opacity="0.15"/>

  <!-- Camera HUD Corners -->
  <path class="corner" d="M30 50v-20h20" stroke="#22d3ee" stroke-width="2" fill="none"/>
  <path class="corner" d="M1250 50v-20h-20" stroke="#22d3ee" stroke-width="2" fill="none"/>
  <path class="corner" d="M30 490v20h20" stroke="#22d3ee" stroke-width="2" fill="none"/>
  <path class="corner" d="M1250 490v20h-20" stroke="#22d3ee" stroke-width="2" fill="none"/>

  <!-- Camera HUD Status Bar -->
  <g class="fi" style="animation-delay:.3s">
    <circle cx="70" cy="42" r="4.5" fill="#ef4444"><animate attributeName="opacity" values="1;.2;1" dur="1.2s" repeatCount="indefinite"/></circle>
    <text class="jbb" x="84" y="47" font-size="12" fill="#ef4444" letter-spacing="2">REC</text>
    <text class="jb" x="135" y="47" font-size="12" fill="#8d93ab" letter-spacing="1.5">PORTFOLIO.MP4 &#183; 24FPS</text>
  </g>

  <!-- Open to Collabs Badge -->
  <g class="fi" style="animation-delay:.5s">
    <rect x="64" y="66" width="195" height="28" rx="14" fill="#34d399" fill-opacity=".1" stroke="#34d399" stroke-opacity=".45"/>
    <circle cx="84" cy="80" r="4.5" fill="#34d399"/>
    <circle cx="84" cy="80" r="4" fill="none" stroke="#34d399" stroke-width="1.5"><animate attributeName="r" values="4;11" dur="1.6s" repeatCount="indefinite"/><animate attributeName="opacity" values=".9;0" dur="1.6s" repeatCount="indefinite"/></circle>
    <text class="jbb" x="98" y="85" font-size="12" fill="#34d399" letter-spacing="1.6">OPEN TO COLLABS</text>
  </g>

  <!-- Greeting & Name -->
  <text clip-path="url(#hiClip)" class="sgm" x="64" y="164" font-size="30" fill="#eceef6">Hi there, I'm</text>
  <g clip-path="url(#nameClip)">
    <text class="sg" x="60" y="250" font-size="76" letter-spacing="-1.5" fill="url(#nameG)" filter="url(#glow)">Subhajit Kar</text>
  </g>
  <rect x="64" y="272" width="120" height="3" rx="1.5" fill="url(#nameG2)"><animate attributeName="width" values="0;0;120" keyTimes="0;.68;1" dur="2.5s" begin="0s" fill="freeze"/></rect>

  <!-- Dynamic Role Cycle -->
  <text class="jbb fi" x="64" y="340" font-size="21" fill="#22d3ee" style="animation-delay:1.8s">&gt;</text>
  <text class="role jb" x="92" y="340" font-size="21" fill="#eceef6" opacity="1" style="animation-delay:1.9s">Senior IAM Assistant Manager</text>
  <text class="role jb" x="92" y="340" font-size="21" fill="#eceef6" opacity="0" style="animation-delay:4.9s">Enterprise Identity Governance (IGA)</text>
  <text class="role jb" x="92" y="340" font-size="21" fill="#eceef6" opacity="0" style="animation-delay:7.9s">Deloitte Cyber &amp; Strategic Risk</text>
  <text class="role jb" x="92" y="340" font-size="21" fill="#eceef6" opacity="0" style="animation-delay:10.9s">Zero-Trust Identity Architect</text>

  <!-- Subtitle Description -->
  <text class="sgm fu" x="64" y="392" font-size="18" fill="#8d93ab" style="animation-delay:2.5s">Architecting zero-trust enterprise identity governance,</text>
  <text class="sgm fu" x="64" y="418" font-size="18" fill="#8d93ab" style="animation-delay:2.62s">Saviynt IGA automation, and cloud security at scale.</text>

  <!-- Footer Metadata Badges -->
  <g class="fu" style="animation-delay:3.0s">
    <g transform="translate(72,453)">
      <path d="M0-8a6 6 0 0 1 6 6c0 4.5-6 10-6 10s-6-5.5-6-10a6 6 0 0 1 6-6z" fill="none" stroke="#22d3ee" stroke-width="1.8"/>
      <circle cy="-2" r="2" fill="#22d3ee"/>
    </g>
    <text class="jb" x="88" y="458" font-size="14.5" fill="#8d93ab">Kolkata / Bengaluru, IN</text>
  </g>

  <g class="fu" style="animation-delay:3.15s">
    <g transform="translate(310,453)">
      <rect x="-7" y="-5" width="14" height="11" rx="2" fill="none" stroke="#a78bfa" stroke-width="1.8"/>
      <path d="M-3-5v-2.5h6V-5" fill="none" stroke="#a78bfa" stroke-width="1.8"/>
    </g>
    <text class="jb" x="326" y="458" font-size="14.5" fill="#8d93ab">Deloitte Cyber &amp; Risk</text>
  </g>

  <g class="fu" style="animation-delay:3.3s">
    <g transform="translate(535,453)">
      <path d="M0-8l2.4 5 5.4.6-4 3.7 1.1 5.4L0 4 -4.9 6.7-3.8 1.3-7.8-2.4l5.4-.6z" fill="none" stroke="#f472b6" stroke-width="1.7" stroke-linejoin="round"/>
    </g>
    <text class="jb" x="551" y="458" font-size="14.5" fill="#8d93ab">300K+ identities &#183; 13 awards</text>
  </g>
</g>

<!-- Outer Border -->
<rect x=".75" y=".75" width="1278.5" height="538.5" rx="25.5" fill="none" stroke="#262a42" stroke-width="1.5"/>
</svg>'''

    HERO_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(HERO_OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(HERO_BANNER_OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ Generated 1:1 Reference-Fidelity hero.svg ({len(svg_content) / 1024:.1f} KB)")
    return True

if __name__ == "__main__":
    generate_reference_hero()
