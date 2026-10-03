#!/usr/bin/env python3
"""
Generate Enterprise IAM/IGA Visual Pipeline Architecture (Master V2) for Subhajit Kar.
Synthesizes a 1280x620 widescreen SVG representing the end-to-end identity governance pipeline:
1. Workday HRMS (HR Source of Truth)
2. Python Reconciliation Engine (300K+ Identities / Mo, Data Gap SOPs)
3. Saviynt IGA Enterprise (JML Lifecycle, Continuous SoD, Access Certifications)
4. Target Cloud & Hybrid Endpoints (Entra ID, Active Directory, AWS IAM, ServiceNow)
5. AI Dev Team Risk Governance (Autonomous Auditing, Anomaly Detection, SOX 404 Readiness)
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
IAM_OUTPUT_SVG = ROOT_DIR / "assets/iam-architecture.svg"
IAM_ALT_SVG = ROOT_DIR / "assets/architecture-matrix.svg"

def generate_iam_visual():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 620" width="100%" height="auto" role="img" aria-label="Enterprise IAM &amp; IGA Pipeline Architecture — Deloitte Cyber Risk">
  <title>Enterprise IAM &amp; IGA Pipeline Architecture</title>
  <desc>Visual pipeline representing Subhajit Kar's enterprise identity governance platform: Workday HRMS to Python Reconciliation, Saviynt IGA Core, Target Endpoints, and AI Dev Team governance.</desc>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&amp;family=Space+Grotesk:wght@600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap');

      .f-mono { font-family: 'JetBrains Mono', monospace; }
      .f-display { font-family: 'Space Grotesk', -apple-system, sans-serif; }
      .f-sans { font-family: 'Inter', -apple-system, sans-serif; }

      @keyframes flowDash {
        to { stroke-dashoffset: -36; }
      }
      @keyframes beaconPulse {
        0%, 100% { r: 5px; opacity: 1; filter: drop-shadow(0 0 6px rgba(0,242,254,0.8)); }
        50% { r: 8px; opacity: 0.5; filter: drop-shadow(0 0 14px rgba(0,242,254,1)); }
      }

      .anim-flow { stroke-dasharray: 6 6; animation: flowDash 2.5s linear infinite; }
      .anim-beacon { animation: beaconPulse 2s ease-in-out infinite; }
    </style>

    <!-- Gradients -->
    <linearGradient id="iamBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040710"/>
      <stop offset="50%" stop-color="#070D1C"/>
      <stop offset="100%" stop-color="#03060E"/>
    </linearGradient>

    <linearGradient id="pillarGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E172B"/>
      <stop offset="100%" stop-color="#080E1B"/>
    </linearGradient>

    <linearGradient id="saviyntPillarGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#142340"/>
      <stop offset="100%" stop-color="#091326"/>
    </linearGradient>

    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#FFDB70"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="archGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#162238" stroke-width="0.7" stroke-opacity="0.5"/>
    </pattern>

    <!-- Glow Filter -->
    <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect width="1280" height="620" fill="url(#iamBg)"/>
  <rect width="1280" height="620" fill="url(#archGrid)"/>

  <!-- Outer Frame -->
  <rect x="16" y="16" width="1248" height="588" rx="20" fill="none" stroke="#1E293B" stroke-width="1.2"/>
  <rect x="22" y="22" width="1236" height="576" rx="16" fill="none" stroke="#00F2FE" stroke-opacity="0.15" stroke-width="0.8"/>

  <!-- Corner Brackets -->
  <path d="M 28 50 L 28 28 L 50 28" fill="none" stroke="#00F2FE" stroke-width="2.5"/>
  <path d="M 1252 50 L 1252 28 L 1230 28" fill="none" stroke="#00F2FE" stroke-width="2.5"/>
  <path d="M 28 570 L 28 592 L 50 592" fill="none" stroke="#00F2FE" stroke-width="2.5"/>
  <path d="M 1252 570 L 1252 592 L 1230 592" fill="none" stroke="#00F2FE" stroke-width="2.5"/>

  <!-- Header Section -->
  <g transform="translate(48, 52)">
    <text x="0" y="14" class="f-mono" font-size="12" font-weight="700" fill="#00F2FE" letter-spacing="2.5">// ENTERPRISE IDENTITY GOVERNANCE &amp; AUTOMATION PIPELINE</text>
    <text x="0" y="44" class="f-display" font-size="24" font-weight="800" fill="url(#titleGrad)" letter-spacing="-0.3">Enterprise JML Lifecycle, Continuous SoD &amp; 300K+ Identity Reconciliation</text>
    <text x="0" y="68" class="f-sans" font-size="13" fill="#94A3B8">Production architecture implemented across 9 Global Operational Zones · Deloitte Cyber &amp; Strategic Risk</text>
  </g>

  <!-- Connective Pipeline Circuit Bus (Behind Pillars) -->
  <g stroke="#1E293B" stroke-width="3">
    <line x1="260" y1="280" x2="300" y2="280"/>
    <line x1="520" y1="280" x2="560" y2="280"/>
    <line x1="780" y1="280" x2="820" y2="280"/>
    <line x1="1040" y1="280" x2="1070" y2="280"/>
  </g>

  <!-- Animated Data Flow Line -->
  <path d="M 260 280 L 1050 280" fill="none" stroke="#00F2FE" stroke-width="2" class="anim-flow" stroke-opacity="0.85"/>

  <!-- ==================== 5 ARCHITECTURAL PILLARS ==================== -->

  <!-- PILLAR 1: HR SOURCE OF TRUTH (Workday) -->
  <g transform="translate(48, 145)">
    <!-- Shadow & Box -->
    <rect x="0" y="0" width="216" height="340" rx="14" fill="url(#pillarGrad)" stroke="#38BDF8" stroke-opacity="0.4" stroke-width="1.2"/>
    <!-- Top Accent Bar -->
    <rect x="0" y="0" width="216" height="5" rx="2" fill="#38BDF8"/>
    <!-- Stage Header -->
    <text x="16" y="32" class="f-mono" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.2">STAGE 01 · HR TRUTH</text>
    <text x="16" y="58" class="f-display" font-size="18" font-weight="700" fill="#FFFFFF">Workday HRMS</text>
    <text x="16" y="76" class="f-sans" font-size="11" fill="#64748B">Authoritative Worker Record</text>

    <!-- Inner Cards / Modules -->
    <g transform="translate(14, 94)">
      <rect x="0" y="0" width="188" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Employee &amp; Contractor Feed</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Full lifecycle event streams</text>
    </g>

    <g transform="translate(14, 154)">
      <rect x="0" y="0" width="188" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Position &amp; Org Management</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Dept, Cost Center, Manager ID</text>
    </g>

    <g transform="translate(14, 214)">
      <rect x="0" y="0" width="188" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">JML Trigger Generation</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Real-time Joiner, Mover, Leaver</text>
    </g>

    <!-- Status Tag -->
    <rect x="14" y="284" width="188" height="32" rx="6" fill="#081424" stroke="#38BDF8" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="28" cy="300" r="3.5" fill="#38BDF8"/>
    <text x="38" y="303" class="f-mono" font-size="9.5" font-weight="700" fill="#38BDF8">DAILY FULL &amp; DELTA SYNC</text>
  </g>

  <!-- PILLAR 2: PYTHON RECONCILIATION ENGINE -->
  <g transform="translate(296, 145)">
    <!-- Shadow & Box -->
    <rect x="0" y="0" width="224" height="340" rx="14" fill="url(#pillarGrad)" stroke="#10B981" stroke-opacity="0.45" stroke-width="1.2"/>
    <rect x="0" y="0" width="224" height="5" rx="2" fill="#10B981"/>
    <!-- Stage Header -->
    <text x="16" y="32" class="f-mono" font-size="10" font-weight="700" fill="#10B981" letter-spacing="1.2">STAGE 02 · HIGH-VOL ETL</text>
    <text x="16" y="58" class="f-display" font-size="18" font-weight="700" fill="#FFFFFF">Python Recon Engine</text>
    <text x="16" y="76" class="f-sans" font-size="11" fill="#64748B">300K+ Monthly Identities</text>

    <!-- Modules -->
    <g transform="translate(14, 94)">
      <rect x="0" y="0" width="196" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Automated Data Gap SOPs</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#34D399">80–90% defect elimination</text>
    </g>

    <g transform="translate(14, 154)">
      <rect x="0" y="0" width="196" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Attribute Normalization</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Cross-region schema standard</text>
    </g>

    <g transform="translate(14, 214)">
      <rect x="0" y="0" width="196" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Discrepancy Remediation</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Orphan &amp; rogue account pruning</text>
    </g>

    <rect x="14" y="284" width="196" height="32" rx="6" fill="#061812" stroke="#10B981" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="28" cy="300" r="3.5" fill="#10B981"/>
    <text x="38" y="303" class="f-mono" font-size="9.5" font-weight="700" fill="#10B981">300K+ IDENTITY PIPELINE</text>
  </g>

  <!-- PILLAR 3: SAVIYNT IGA CORE (CENTERPIECE) -->
  <g transform="translate(552, 135)">
    <!-- Elevated Centerpiece Box -->
    <rect x="0" y="0" width="232" height="360" rx="16" fill="url(#saviyntPillarGrad)" stroke="#00F2FE" stroke-width="1.8" filter="url(#cyanGlow)"/>
    <rect x="0" y="0" width="232" height="6" rx="3" fill="#00F2FE"/>
    <!-- Stage Header -->
    <text x="18" y="34" class="f-mono" font-size="10.5" font-weight="700" fill="#00F2FE" letter-spacing="1.5">STAGE 03 · CORE GOVERNANCE</text>
    <text x="18" y="62" class="f-display" font-size="20" font-weight="800" fill="#FFFFFF">Saviynt IGA Core</text>
    <text x="18" y="80" class="f-sans" font-size="11.5" fill="#38BDF8">Enterprise Identity Administration</text>

    <!-- Modules -->
    <g transform="translate(16, 98)">
      <rect x="0" y="0" width="200" height="54" rx="8" fill="#060E1E" stroke="#00F2FE" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="23" class="f-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">JML Lifecycle Engine</text>
      <text x="12" y="40" class="f-mono" font-size="9.5" fill="#38BDF8">Zero-delay birthright grants</text>
    </g>

    <g transform="translate(16, 160)">
      <rect x="0" y="0" width="200" height="54" rx="8" fill="#060E1E" stroke="#00F2FE" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="23" class="f-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">Continuous SoD Matrix</text>
      <text x="12" y="40" class="f-mono" font-size="9.5" fill="#FFDB70">Toxic combination mitigation</text>
    </g>

    <g transform="translate(16, 222)">
      <rect x="0" y="0" width="200" height="54" rx="8" fill="#060E1E" stroke="#00F2FE" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="23" class="f-sans" font-size="12.5" font-weight="700" fill="#FFFFFF">Access Certifications</text>
      <text x="12" y="40" class="f-mono" font-size="9.5" fill="#E2E8F0">Campaigns across 9 regions</text>
    </g>

    <rect x="16" y="296" width="200" height="36" rx="8" fill="#08182E" stroke="#00F2FE" stroke-opacity="0.6" stroke-width="1"/>
    <circle cx="32" cy="314" r="4.5" fill="#00F2FE" class="anim-beacon"/>
    <text x="44" y="318" class="f-mono" font-size="10" font-weight="700" fill="#00F2FE" letter-spacing="0.5">SAVIYNT CERTIFIED CORE</text>
  </g>

  <!-- PILLAR 4: HYBRID & MULTI-CLOUD TARGET ENDPOINTS -->
  <g transform="translate(816, 145)">
    <rect x="0" y="0" width="224" height="340" rx="14" fill="url(#pillarGrad)" stroke="#38BDF8" stroke-opacity="0.4" stroke-width="1.2"/>
    <rect x="0" y="0" width="224" height="5" rx="2" fill="#38BDF8"/>
    <text x="16" y="32" class="f-mono" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.2">STAGE 04 · TARGET ECOSYSTEM</text>
    <text x="16" y="58" class="f-display" font-size="18" font-weight="700" fill="#FFFFFF">Hybrid Endpoints</text>
    <text x="16" y="76" class="f-sans" font-size="11" fill="#64748B">Cloud &amp; On-Prem Directory</text>

    <!-- Modules -->
    <g transform="translate(14, 94)">
      <rect x="0" y="0" width="196" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Microsoft Entra ID</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Cloud tenant &amp; SSO provisioning</text>
    </g>

    <g transform="translate(14, 154)">
      <rect x="0" y="0" width="196" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">Active Directory (AD DS)</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">Enterprise Kerberos / LDAP</text>
    </g>

    <g transform="translate(14, 214)">
      <rect x="0" y="0" width="196" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="12" y="22" class="f-sans" font-size="12" font-weight="600" fill="#E2E8F0">AWS Cloud &amp; ServiceNow</text>
      <text x="12" y="38" class="f-mono" font-size="9.5" fill="#94A3B8">IAM roles &amp; 250+ RITM tickets</text>
    </g>

    <rect x="14" y="284" width="196" height="32" rx="6" fill="#0A1828" stroke="#38BDF8" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="28" cy="300" r="3.5" fill="#38BDF8"/>
    <text x="38" y="303" class="f-mono" font-size="9.5" font-weight="700" fill="#38BDF8">FEDERATED HYBRID IAM</text>
  </g>

  <!-- PILLAR 5: AI DEV TEAM & RISK OVERSIGHT -->
  <g transform="translate(1072, 145)">
    <rect x="0" y="0" width="160" height="340" rx="14" fill="url(#pillarGrad)" stroke="#A855F7" stroke-opacity="0.4" stroke-width="1.2"/>
    <rect x="0" y="0" width="160" height="5" rx="2" fill="#A855F7"/>
    <text x="14" y="32" class="f-mono" font-size="9.5" font-weight="700" fill="#A855F7" letter-spacing="1">STAGE 05 · AI</text>
    <text x="14" y="58" class="f-display" font-size="16" font-weight="700" fill="#FFFFFF">AI Dev Team</text>
    <text x="14" y="76" class="f-sans" font-size="10.5" fill="#64748B">Audit &amp; Oversight</text>

    <!-- Modules -->
    <g transform="translate(10, 94)">
      <rect x="0" y="0" width="140" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="10" y="22" class="f-sans" font-size="11" font-weight="600" fill="#E2E8F0">Role Mining</text>
      <text x="10" y="38" class="f-mono" font-size="8.5" fill="#C084FC">ML recommendations</text>
    </g>

    <g transform="translate(10, 154)">
      <rect x="0" y="0" width="140" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="10" y="22" class="f-sans" font-size="11" font-weight="600" fill="#E2E8F0">Anomaly Audit</text>
      <text x="10" y="38" class="f-mono" font-size="8.5" fill="#94A3B8">Continuous gates</text>
    </g>

    <g transform="translate(10, 214)">
      <rect x="0" y="0" width="140" height="52" rx="8" fill="#060C16" stroke="#1E293B" stroke-width="0.8"/>
      <text x="10" y="22" class="f-sans" font-size="11" font-weight="600" fill="#E2E8F0">SOX 404 Ready</text>
      <text x="10" y="38" class="f-mono" font-size="8.5" fill="#FFDB70">Defect prevention</text>
    </g>

    <rect x="10" y="284" width="140" height="32" rx="6" fill="#140A24" stroke="#A855F7" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="22" cy="300" r="3.5" fill="#A855F7"/>
    <text x="32" y="303" class="f-mono" font-size="9" font-weight="700" fill="#D8B4FE">AI GOVERNANCE</text>
  </g>

  <!-- Bottom Telemetry Metric Strip -->
  <g transform="translate(48, 510)">
    <rect x="0" y="0" width="1184" height="66" rx="12" fill="#070E1C" stroke="#1E293B" stroke-width="1"/>

    <!-- Metric 1 -->
    <g transform="translate(24, 14)">
      <text x="0" y="24" class="f-display" font-size="20" font-weight="800" fill="#00F2FE">300,000+</text>
      <text x="0" y="42" class="f-sans" font-size="11" font-weight="600" fill="#94A3B8">Monthly Identities Reconciled</text>
    </g>
    <line x1="290" y1="12" x2="290" y2="54" stroke="#1E293B" stroke-width="1"/>

    <!-- Metric 2 -->
    <g transform="translate(320, 14)">
      <text x="0" y="24" class="f-display" font-size="20" font-weight="800" fill="#10B981">80–90%</text>
      <text x="0" y="42" class="f-sans" font-size="11" font-weight="600" fill="#94A3B8">Data Gap Discrepancy Reduction</text>
    </g>
    <line x1="590" y1="12" x2="590" y2="54" stroke="#1E293B" stroke-width="1"/>

    <!-- Metric 3 -->
    <g transform="translate(620, 14)">
      <text x="0" y="24" class="f-display" font-size="20" font-weight="800" fill="#A855F7">20–30%</text>
      <text x="0" y="42" class="f-sans" font-size="11" font-weight="600" fill="#94A3B8">Access Exceptions Decreased</text>
    </g>
    <line x1="880" y1="12" x2="880" y2="54" stroke="#1E293B" stroke-width="1"/>

    <!-- Metric 4 -->
    <g transform="translate(910, 14)">
      <text x="0" y="24" class="f-display" font-size="20" font-weight="800" fill="#FFDB70">90% API Coverage</text>
      <text x="0" y="42" class="f-sans" font-size="11" font-weight="600" fill="#94A3B8">Critical IGA Lifecycle Automation</text>
    </g>
  </g>
</svg>'''

    # Validate XML
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as err:
        print(f"❌ XML error in generated IAM visual SVG: {err}", file=sys.stderr)
        return False

    IAM_OUTPUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    with open(IAM_OUTPUT_SVG, "w", encoding="utf-8") as out:
        out.write(svg_content)

    with open(IAM_ALT_SVG, "w", encoding="utf-8") as out:
        out.write(svg_content)

    print(f"✅ Generated IAM/IGA Pipeline Architecture SVG at {IAM_OUTPUT_SVG} and {IAM_ALT_SVG}")
    return True

if __name__ == "__main__":
    success = generate_iam_visual()
    sys.exit(0 if success else 1)
