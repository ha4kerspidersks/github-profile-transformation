import sys
from pathlib import Path
from shared_svg_fonts import SHARED_FONTS

ABOUT_OUTPUT = Path("assets/about-life.svg")
IAM_OUTPUT = Path("assets/iam-architecture.svg")

def generate_reference_about():
    print("🎨 Generating reference-faithful dual-window about-life.svg (1280x640)...")

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 640" width="1280" height="640" role="img" aria-label="Subhajit Kar — Architecture &amp; Leadership"><title>Subhajit Kar — Architecture &amp; Leadership</title><desc>Dual-window showcase: Enterprise IAM Governance on the left, Cyber Risk Leadership and NFSU Research on the right.</desc><defs><style>{SHARED_FONTS}
text{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.sg{{font-family:'SG','Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}}
.sgm{{font-family:'SGM','Segoe UI',Helvetica,Arial,sans-serif;font-weight:500}}
.jb{{font-family:'JBM',ui-monospace,Menlo,Consolas,monospace}}
.jbb{{font-family:'JBMB',ui-monospace,Menlo,Consolas,monospace;font-weight:700}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@keyframes cursorBlink{{0%,100%{{opacity:1}}50%{{opacity:0}}}}
.fu{{animation:fadeUp .7s cubic-bezier(.2,.8,.2,1) both}}
.fi{{animation:fadeIn .7s ease both}}
.cursor{{animation:cursorBlink 1.1s infinite}}
.cardL{{animation:fadeIn .8s ease both}}
.cardR{{animation:fadeIn .8s ease .15s both}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}
</style>

<linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#141829"/>
  <stop offset="100%" stop-color="#0d0e16"/>
</linearGradient>

<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#a78bfa" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#262a42" stop-opacity=".8"/>
</linearGradient>

<linearGradient id="edgeR" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#f472b6" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#a78bfa" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#262a42" stop-opacity=".8"/>
</linearGradient>

<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
  <circle cx="11" cy="11" r=".8" fill="#ffffff" fill-opacity=".05"/>
</pattern>

<clipPath id="winClipL"><rect x="28" y="118" width="564" height="490" rx="16"/></clipPath>
<clipPath id="winClipR"><rect x="688" y="118" width="564" height="490" rx="16"/></clipPath>
</defs>

<!-- ========================================== -->
<!-- LEFT PANEL: ENTERPRISE IAM & IGA ARCHITECTURE -->
<!-- ========================================== -->
<g class="cardL">
  <!-- Outer Card Frame -->
  <rect x="0" y="0" width="620" height="640" rx="24" fill="url(#cardbg)"/>
  <rect x="0" y="0" width="620" height="640" rx="24" fill="url(#dots)"/>
  <rect x=".75" y=".75" width="618.5" height="638.5" rx="23.25" fill="none" stroke="url(#edge)" stroke-width="1.5"/>

  <!-- Left Header -->
  <text class="jbb" x="32" y="48" font-size="12.5" fill="#22d3ee" letter-spacing="2.2">// IDENTITY ARCHITECT</text>
  <text class="sg" x="32" y="88" font-size="28" fill="#eceef6" letter-spacing="-.5">Zero-trust identity at scale</text>

  <!-- Browser Window L -->
  <g clip-path="url(#winClipL)">
    <!-- Window Body -->
    <rect x="28" y="118" width="564" height="490" fill="#0f1224"/>
    <!-- Window Chrome Header -->
    <rect x="28" y="118" width="564" height="34" fill="#171a2c"/>
    <circle cx="46" cy="135" r="5" fill="#ff5f57"/>
    <circle cx="62" cy="135" r="5" fill="#febc2e"/>
    <circle cx="78" cy="135" r="5" fill="#28c840"/>

    <!-- URL Bar -->
    <rect x="160" y="126" width="300" height="18" rx="9" fill="#090b14"/>
    <text class="jb" x="300" y="139" font-size="11" fill="#8d93ab" text-anchor="middle">identity.governance/zero-trust</text>
    <rect class="cursor" x="395" y="130" width="1.5" height="11" fill="#22d3ee"/>

    <!-- Content Row 1: Saviynt Lifecycle -->
    <g transform="translate(48, 172)">
      <rect x="0" y="0" width="524" height="126" rx="14" fill="#ffffff" fill-opacity=".03" stroke="#262a42" stroke-width="1"/>
      <rect x="14" y="14" width="40" height="40" rx="10" fill="#22d3ee" fill-opacity=".12"/>
      <!-- Shield / Key Icon -->
      <path d="M34 24v8m-5-4h10m-13 14h16a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-16a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2z" stroke="#22d3ee" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <text class="sg" x="66" y="34" font-size="16" fill="#eceef6">Saviynt IGA &amp; Cloud Lifecycle</text>
      <text class="jb" x="66" y="52" font-size="11" fill="#22d3ee" letter-spacing="1">JML AUTOMATION &#183; ENTRA ID &#183; AD</text>
      <text class="sgm" x="66" y="78" font-size="13" fill="#8d93ab">End-to-end Joiner-Mover-Leaver automation,</text>
      <text class="sgm" x="66" y="98" font-size="13" fill="#8d93ab">hybrid directory sync, and automated birthright provisioning.</text>
      <!-- Active Pill -->
      <rect x="424" y="16" width="84" height="22" rx="11" fill="#34d399" fill-opacity=".1" stroke="#34d399" stroke-opacity=".4"/>
      <circle cx="436" cy="27" r="3.5" fill="#34d399"/>
      <text class="jbb" x="445" y="31" font-size="9" fill="#34d399" letter-spacing="1">SECURED</text>
    </g>

    <!-- Content Row 2: 300K+ Reconciliation -->
    <g transform="translate(48, 314)">
      <rect x="0" y="0" width="524" height="126" rx="14" fill="#ffffff" fill-opacity=".03" stroke="#262a42" stroke-width="1"/>
      <rect x="14" y="14" width="40" height="40" rx="10" fill="#a78bfa" fill-opacity=".12"/>
      <!-- Database / Flow Icon -->
      <path d="M34 22c5.5 0 10 1.8 10 4s-4.5 4-10 4-10-1.8-10-4 4.5-4 10-4zm-10 8c0 2.2 4.5 4 10 4s10-1.8 10-4m-20 8c0 2.2 4.5 4 10 4s10-1.8 10-4" stroke="#a78bfa" stroke-width="1.8" fill="none" stroke-linecap="round"/>
      <text class="sg" x="66" y="34" font-size="16" fill="#eceef6">300K+ Monthly Identity Reconciliation</text>
      <text class="jb" x="66" y="52" font-size="11" fill="#a78bfa" letter-spacing="1">ZERO DRIFT &#183; PYTHON PIPELINES &#183; WORKDAY</text>
      <text class="sgm" x="66" y="78" font-size="13" fill="#8d93ab">High-throughput reconciliation engines processing</text>
      <text class="sgm" x="66" y="98" font-size="13" fill="#8d93ab">over 300,000 enterprise identity records monthly.</text>
      <!-- Active Pill -->
      <rect x="420" y="16" width="88" height="22" rx="11" fill="#a78bfa" fill-opacity=".1" stroke="#a78bfa" stroke-opacity=".4"/>
      <circle cx="432" cy="27" r="3.5" fill="#a78bfa"/>
      <text class="jbb" x="441" y="31" font-size="9" fill="#a78bfa" letter-spacing="1">OPTIMIZED</text>
    </g>

    <!-- Content Row 3: SoD & Compliance -->
    <g transform="translate(48, 456)">
      <rect x="0" y="0" width="524" height="126" rx="14" fill="#ffffff" fill-opacity=".03" stroke="#262a42" stroke-width="1"/>
      <rect x="14" y="14" width="40" height="40" rx="10" fill="#34d399" fill-opacity=".12"/>
      <!-- Check Shield Icon -->
      <path d="M34 22l-10 4v8c0 6.6 4.3 12.8 10 14 5.7-1.2 10-7.4 10-14v-8l-10-4zm-3 12l2 2 5-5" stroke="#34d399" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <text class="sg" x="66" y="34" font-size="16" fill="#eceef6">SoD Matrix &amp; SOX 404 Compliance</text>
      <text class="jb" x="66" y="52" font-size="11" fill="#34d399" letter-spacing="1">AUDIT READINESS &#183; RBAC/ABAC &#183; RISK</text>
      <text class="sgm" x="66" y="78" font-size="13" fill="#8d93ab">Automated segregation-of-duties conflict detection</text>
      <text class="sgm" x="66" y="98" font-size="13" fill="#8d93ab">and continuous regulatory compliance enforcement.</text>
      <!-- Active Pill -->
      <rect x="424" y="16" width="84" height="22" rx="11" fill="#34d399" fill-opacity=".1" stroke="#34d399" stroke-opacity=".4"/>
      <circle cx="436" cy="27" r="3.5" fill="#34d399"/>
      <text class="jbb" x="445" y="31" font-size="9" fill="#34d399" letter-spacing="1">AUDITED</text>
    </g>
  </g>
</g>

<!-- ========================================== -->
<!-- RIGHT PANEL: LEADERSHIP & RESEARCH -->
<!-- ========================================== -->
<g class="cardR">
  <!-- Outer Card Frame -->
  <rect x="660" y="0" width="620" height="640" rx="24" fill="url(#cardbg)"/>
  <rect x="660" y="0" width="620" height="640" rx="24" fill="url(#dots)"/>
  <rect x="660.75" y=".75" width="618.5" height="638.5" rx="23.25" fill="none" stroke="url(#edgeR)" stroke-width="1.5"/>

  <!-- Right Header -->
  <text class="jbb" x="692" y="48" font-size="12.5" fill="#f472b6" letter-spacing="2.2">// LEADERSHIP &amp; RESEARCH</text>
  <text class="sg" x="692" y="88" font-size="28" fill="#eceef6" letter-spacing="-.5">Impact, innovation &amp; honors</text>

  <!-- Browser Window R -->
  <g clip-path="url(#winClipR)">
    <!-- Window Body -->
    <rect x="688" y="118" width="564" height="490" fill="#0f1224"/>
    <!-- Window Chrome Header -->
    <rect x="688" y="118" width="564" height="34" fill="#171a2c"/>
    <circle cx="706" cy="135" r="5" fill="#ff5f57"/>
    <circle cx="722" cy="135" r="5" fill="#febc2e"/>
    <circle cx="738" cy="135" r="5" fill="#28c840"/>

    <!-- URL Bar -->
    <rect x="820" y="126" width="300" height="18" rx="9" fill="#090b14"/>
    <text class="jb" x="960" y="139" font-size="11" fill="#8d93ab" text-anchor="middle">scholar.nfsu.ac.in/subhajit</text>
    <rect class="cursor" x="1055" y="130" width="1.5" height="11" fill="#f472b6"/>

    <!-- Content Row 1: 13x Deloitte Awards -->
    <g transform="translate(708, 172)">
      <rect x="0" y="0" width="524" height="126" rx="14" fill="#ffffff" fill-opacity=".03" stroke="#262a42" stroke-width="1"/>
      <rect x="14" y="14" width="40" height="40" rx="10" fill="#fbbf24" fill-opacity=".12"/>
      <!-- Trophy Icon -->
      <path d="M26 24h16v6a8 8 0 0 1-16 0v-6zm0 2h-4a3 3 0 0 1-3-3v-1h7m12 4h4a3 3 0 0 0 3-3v-1h-7m-9 12v6m-5 0h10" stroke="#fbbf24" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <text class="sg" x="66" y="34" font-size="16" fill="#eceef6">13x Deloitte Excellence Awards</text>
      <text class="jb" x="66" y="52" font-size="11" fill="#fbbf24" letter-spacing="1">APPLAUSE &#183; SPOT &#183; RECOGNITION</text>
      <text class="sgm" x="66" y="78" font-size="13" fill="#8d93ab">Honored across Cyber &amp; Strategic Risk practice</text>
      <text class="sgm" x="66" y="98" font-size="13" fill="#8d93ab">for client impact, innovation, and leadership.</text>
      <!-- Active Pill -->
      <rect x="424" y="16" width="84" height="22" rx="11" fill="#fbbf24" fill-opacity=".1" stroke="#fbbf24" stroke-opacity=".4"/>
      <circle cx="436" cy="27" r="3.5" fill="#fbbf24"/>
      <text class="jbb" x="445" y="31" font-size="9" fill="#fbbf24" letter-spacing="1">HONORED</text>
    </g>

    <!-- Content Row 2: NFSU Scholar -->
    <g transform="translate(708, 314)">
      <rect x="0" y="0" width="524" height="126" rx="14" fill="#ffffff" fill-opacity=".03" stroke="#262a42" stroke-width="1"/>
      <rect x="14" y="14" width="40" height="40" rx="10" fill="#f472b6" fill-opacity=".12"/>
      <!-- Scholar Cap Icon -->
      <path d="M34 22l-14 7 14 7 14-7-14-7zm-10 11v8c0 3 4.5 6 10 6s10-3 10-6v-8" stroke="#f472b6" stroke-width="1.8" fill="none" stroke-linecap="round"/>
      <text class="sg" x="66" y="34" font-size="16" fill="#eceef6">NFSU Cyber Security Scholar</text>
      <text class="jb" x="66" y="52" font-size="11" fill="#f472b6" letter-spacing="1">M.TECH CYBER SECURITY &#183; NATIONAL FORENSIC</text>
      <text class="sgm" x="66" y="78" font-size="13" fill="#8d93ab">Post-graduate specialization from India's Institution</text>
      <text class="sgm" x="66" y="98" font-size="13" fill="#8d93ab">of National Importance for Cyber Defense &amp; Forensics.</text>
      <!-- Active Pill -->
      <rect x="424" y="16" width="84" height="22" rx="11" fill="#f472b6" fill-opacity=".1" stroke="#f472b6" stroke-opacity=".4"/>
      <circle cx="436" cy="27" r="3.5" fill="#f472b6"/>
      <text class="jbb" x="445" y="31" font-size="9" fill="#f472b6" letter-spacing="1">SCHOLAR</text>
    </g>

    <!-- Content Row 3: Automotive CAN Bus Research -->
    <g transform="translate(708, 456)">
      <rect x="0" y="0" width="524" height="126" rx="14" fill="#ffffff" fill-opacity=".03" stroke="#262a42" stroke-width="1"/>
      <rect x="14" y="14" width="40" height="40" rx="10" fill="#38bdf8" fill-opacity=".12"/>
      <!-- Radar / Signal Wave Icon -->
      <circle cx="34" cy="34" r="3" fill="#38bdf8"/>
      <path d="M26 26a11 11 0 0 1 16 0m-22-6a19 19 0 0 1 28 0" stroke="#38bdf8" stroke-width="1.8" fill="none" stroke-linecap="round"/>
      <text class="sg" x="66" y="34" font-size="16" fill="#eceef6">Automotive CAN Bus Intrusion Defense</text>
      <text class="jb" x="66" y="52" font-size="11" fill="#38bdf8" letter-spacing="1">INTRUSION DETECTION &#183; TELEMETRY &#183; ML</text>
      <text class="sgm" x="66" y="78" font-size="13" fill="#8d93ab">Researched vehicular network bus security, real-time</text>
      <text class="sgm" x="66" y="98" font-size="13" fill="#8d93ab">frame timing analysis, and anomaly detection models.</text>
      <!-- Active Pill -->
      <rect x="424" y="16" width="84" height="22" rx="11" fill="#38bdf8" fill-opacity=".1" stroke="#38bdf8" stroke-opacity=".4"/>
      <circle cx="436" cy="27" r="3.5" fill="#38bdf8"/>
      <text class="jbb" x="445" y="31" font-size="9" fill="#38bdf8" letter-spacing="1">RESEARCH</text>
    </g>
  </g>
</g>
</svg>'''

    ABOUT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(ABOUT_OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(IAM_OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ Generated 1:1 Reference-Fidelity about-life.svg ({len(svg_content) / 1024:.1f} KB)")
    return True

if __name__ == "__main__":
    generate_reference_about()
