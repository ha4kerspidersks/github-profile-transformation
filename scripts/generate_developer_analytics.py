#!/usr/bin/env python3
"""
generate_developer_analytics.py
Generates assets/developer-analytics.svg by combining:
1. templates/05-dashboard/analytics-grid (KPI cards, sparklines, velocity chart, radar-blip)
2. templates/13-purpose-built/oss-maintainer (Engineering activity table, status pills, commitments)
3. templates/08-markdown-tricks/collapsible-projects (High information density)
from beydemirfurkan/awesome-github-profile, adapted for Subhajit Kar's verified portfolio data.
"""

import os
import sys

def build_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="1200" height="680" role="img" aria-label="Developer Analytics — Subhajit Kar Engineering Activity &amp; Telemetry">
  <title>Developer Analytics — Subhajit Kar</title>
  <desc>Engineering activity at a glance: 300K+ monthly identities, 80-90% defect reduction, 250+ ServiceNow RITMs, active builds, 90-day velocity, and zero-trust engineering signals.</desc>
  <defs>
    <!-- Stage & Card Gradients -->
    <linearGradient id="ag-stage" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0d0e16"/>
      <stop offset="100%" stop-color="#080a12"/>
    </linearGradient>
    <linearGradient id="ag-card" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#13182c"/>
      <stop offset="100%" stop-color="#0c1020"/>
    </linearGradient>
    <linearGradient id="ag-card-subtle" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#111628"/>
      <stop offset="100%" stop-color="#0a0d1a"/>
    </linearGradient>

    <!-- Sparkline Gradients -->
    <linearGradient id="ag-spark-cyan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#22d3ee" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="ag-spark-violet" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#a78bfa" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#a78bfa" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="ag-spark-pink" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f472b6" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#f472b6" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="ag-spark-emerald" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#34d399" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#34d399" stop-opacity="0.0"/>
    </linearGradient>

    <!-- Subtle Drop Shadow Filter -->
    <filter id="ag-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="680" fill="url(#ag-stage)"/>

  <!-- Top Status Strip -->
  <g font-family="'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace" font-size="10" letter-spacing="3.5">
    <g transform="translate(60,46)" fill="#22d3ee">
      <circle cx="6" cy="-3" r="3.5">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="1.4s" repeatCount="indefinite"/>
      </circle>
      <text x="20" y="0">LIVE TELEMETRY · PRODUCTION VERIFIED</text>
    </g>
    <g transform="translate(1140,46)" fill="#64748b" text-anchor="end">
      <text x="-16" y="0">DEVELOPER ANALYTICS · 2026 Q2</text>
      <line x1="-10" y1="-3" x2="0" y2="-3" stroke="#64748b" stroke-width="0.8"/>
    </g>
  </g>

  <!-- Section Header -->
  <g transform="translate(60,0)">
    <text x="0" y="92" font-family="'Inter', -apple-system, system-ui, sans-serif" font-size="28" font-weight="700" fill="#f1f5f9">Engineering activity at a glance.</text>
    <text x="0" y="116" font-family="'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace" font-size="11" fill="#64748b" letter-spacing="2">SUBHAJIT KAR  ·  ENTERPRISE IAM &amp; IGA  ·  ZERO TRUST  ·  AUTONOMOUS AI</text>
  </g>

  <!-- ============================================================ -->
  <!-- ROW 1: 4 ANALYTICS KPI CARDS (from templates/05-dashboard/analytics-grid) -->
  <!-- ============================================================ -->

  <!-- Card 1: RECONCILIATION SCALE (Cyan) -->
  <g transform="translate(60,138)" filter="url(#ag-shadow)">
    <rect width="258" height="130" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>
    <text x="18" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2.5">RECONCILIATION · SCALE</text>
    <text x="18" y="68" font-family="'Inter', system-ui, sans-serif" font-size="34" font-weight="700" fill="#f1f5f9">300K+</text>
    <text x="18" y="88" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#22d3ee">▲ 99.8% precision · 9 zones</text>
    <!-- Sparkline polyline -->
    <polyline points="18,124 38,120 58,122 78,114 98,118 118,110 138,113 158,106 178,109 198,103 218,107 238,101" fill="none" stroke="#22d3ee" stroke-width="1.5"/>
    <polyline points="18,124 38,120 58,122 78,114 98,118 118,110 138,113 158,106 178,109 198,103 218,107 238,101 238,126 18,126" fill="url(#ag-spark-cyan)"/>
  </g>

  <!-- Card 2: DEFECT REDUCTION (Violet) -->
  <g transform="translate(334,138)" filter="url(#ag-shadow)">
    <rect width="258" height="130" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>
    <text x="18" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2.5">DEFECT REDUCTION · IMPACT</text>
    <text x="18" y="68" font-family="'Inter', system-ui, sans-serif" font-size="32" font-weight="700" fill="#f1f5f9">80–90%</text>
    <text x="18" y="88" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#a78bfa">→ mismatch elimination</text>
    <!-- Animated streak bars -->
    <g fill="#a78bfa">
      <rect x="18" y="117" width="8" height="7" opacity="0.35"/>
      <rect x="32" y="115" width="8" height="9" opacity="0.4"/>
      <rect x="46" y="112" width="8" height="12" opacity="0.45"/>
      <rect x="60" y="114" width="8" height="10" opacity="0.5"/>
      <rect x="74" y="111" width="8" height="13" opacity="0.55"/>
      <rect x="88" y="108" width="8" height="16" opacity="0.6"/>
      <rect x="102" y="110" width="8" height="14" opacity="0.65"/>
      <rect x="116" y="106" width="8" height="18" opacity="0.7"/>
      <rect x="130" y="108" width="8" height="16" opacity="0.75"/>
      <rect x="144" y="104" width="8" height="20" opacity="0.8"/>
      <rect x="158" y="105" width="8" height="19" opacity="0.85"/>
      <rect x="172" y="102" width="8" height="22" opacity="0.9"/>
      <rect x="186" y="100" width="8" height="24" opacity="0.95"/>
      <rect x="200" y="98" width="8" height="26">
        <animate attributeName="height" values="26;22;26" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="y" values="98;102;98" dur="2s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>

  <!-- Card 3: SERVICENOW RITMs (Pink) -->
  <g transform="translate(608,138)" filter="url(#ag-shadow)">
    <rect width="258" height="130" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>
    <text x="18" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2.5">SERVICENOW · REMEDIATION</text>
    <text x="18" y="68" font-family="'Inter', system-ui, sans-serif" font-size="34" font-weight="700" fill="#f1f5f9">250+</text>
    <text x="18" y="88" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#f472b6">▲ 100% root-cause resolved</text>
    <!-- Sparkline polyline -->
    <polyline points="18,124 38,119 58,115 78,118 98,111 118,113 138,108 158,110 178,104 198,106 218,101 238,102" fill="none" stroke="#f472b6" stroke-width="1.5"/>
    <polyline points="18,124 38,119 58,115 78,118 98,111 118,113 138,108 158,110 178,104 198,106 218,101 238,102 238,126 18,126" fill="url(#ag-spark-pink)"/>
  </g>

  <!-- Card 4: CORE ECOSYSTEMS (Emerald) -->
  <g transform="translate(882,138)" filter="url(#ag-shadow)">
    <rect width="258" height="130" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>
    <text x="18" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2.5">PRODUCTION STACK · BREADTH</text>
    <text x="18" y="68" font-family="'Inter', system-ui, sans-serif" font-size="32" font-weight="700" fill="#f1f5f9">56 TECH</text>
    <text x="18" y="88" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#34d399">multi-cloud · 4 ecosystems</text>
    <!-- 7 Ecosystem Cadence Nodes -->
    <g font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b">
      <circle cx="28" cy="108" r="4.5" fill="#22d3ee"/><text x="28" y="122" text-anchor="middle">IAM</text>
      <circle cx="61" cy="108" r="4.5" fill="#22d3ee" opacity="0.85"/><text x="61" y="122" text-anchor="middle">IGA</text>
      <circle cx="94" cy="108" r="4.5" fill="#a78bfa"/><text x="94" y="122" text-anchor="middle">SEC</text>
      <circle cx="127" cy="108" r="4.5" fill="#a78bfa" opacity="0.85"/><text x="127" y="122" text-anchor="middle">CLOUD</text>
      <circle cx="160" cy="108" r="4.5" fill="#f472b6"/><text x="160" y="122" text-anchor="middle">AI</text>
      <circle cx="193" cy="108" r="4.5" fill="#34d399"/><text x="193" y="122" text-anchor="middle">DEV</text>
      <circle cx="226" cy="108" r="4.5" fill="#34d399" opacity="0.75"/><text x="226" y="122" text-anchor="middle">OPS</text>
    </g>
  </g>

  <!-- ============================================================ -->
  <!-- ROW 2: ENGINEERING ACTIVITY & BUILDS (from templates/13-purpose-built/oss-maintainer) -->
  <!-- ============================================================ -->
  <g transform="translate(60,286)" filter="url(#ag-shadow)">
    <rect width="1080" height="196" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>

    <!-- Header line -->
    <text x="24" y="26" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748b" letter-spacing="3">ENGINEERING ACTIVITY &amp; ARCHITECTURAL BUILDS</text>
    <text x="1056" y="26" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="10" fill="#22d3ee" letter-spacing="2">4 VERIFIED BUILDS · REPRODUCIBLE CODE</text>

    <!-- Column labels -->
    <g font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2">
      <text x="24" y="48">SYSTEM / REPOSITORY</text>
      <text x="270" y="48">CORE ARCHITECTURE &amp; ROLE</text>
      <text x="650" y="48">STACK</text>
      <text x="830" y="48">ASSURANCE</text>
      <text x="1056" y="48" text-anchor="end">STATUS</text>
    </g>
    <line x1="24" y1="56" x2="1056" y2="56" stroke="#1f2540" stroke-width="0.8"/>

    <!-- Project 1: AI-Dev-Team -->
    <g transform="translate(0,62)">
      <line x1="24" y1="0" x2="1056" y2="0" stroke="#151b30" stroke-width="0.6"/>
      <text x="24" y="20" font-family="'Inter', system-ui, sans-serif" font-size="13.5" font-weight="700" fill="#22d3ee">AI-Dev-Team</text>
      <text x="270" y="20" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">Autonomous multi-agent dev team coordinating 18,000+ skills</text>
      <text x="650" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">Python · MCP · Node</text>
      <text x="830" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#e2e8f0">Multi-Model Routing</text>
      <rect x="978" y="7" width="78" height="18" rx="9" fill="#142823"/>
      <text x="1017" y="20" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#34d399">ACTIVE ARCH</text>
    </g>

    <!-- Project 2: User-Role-Recommendations -->
    <g transform="translate(0,96)">
      <line x1="24" y1="0" x2="1056" y2="0" stroke="#151b30" stroke-width="0.6"/>
      <text x="24" y="20" font-family="'Inter', system-ui, sans-serif" font-size="13.5" font-weight="700" fill="#22d3ee">User-Role-Recommendations</text>
      <text x="270" y="20" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">ML role mining &amp; access anomaly detection for least-privilege</text>
      <text x="650" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">Python · scikit-learn</text>
      <text x="830" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#e2e8f0">Toxic Grant Audit</text>
      <rect x="978" y="7" width="78" height="18" rx="9" fill="#1e1b38"/>
      <text x="1017" y="20" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#a78bfa">ML PIPELINE</text>
    </g>

    <!-- Project 3: React-Auth0-PermissionManager -->
    <g transform="translate(0,130)">
      <line x1="24" y1="0" x2="1056" y2="0" stroke="#151b30" stroke-width="0.6"/>
      <text x="24" y="20" font-family="'Inter', system-ui, sans-serif" font-size="13.5" font-weight="700" fill="#22d3ee">React-Auth0-PermissionManager</text>
      <text x="270" y="20" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">Enterprise RBAC permission dashboard with OAuth 2.0 / OIDC</text>
      <text x="650" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">React · TS · Auth0</text>
      <text x="830" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#e2e8f0">Policy Enforcement</text>
      <rect x="978" y="7" width="78" height="18" rx="9" fill="#2d172e"/>
      <text x="1017" y="20" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#f472b6">RBAC ENGINE</text>
    </g>

    <!-- Project 4: CAN-Bus-Intrusion-Defense -->
    <g transform="translate(0,164)">
      <line x1="24" y1="0" x2="1056" y2="0" stroke="#151b30" stroke-width="0.6"/>
      <text x="24" y="20" font-family="'Inter', system-ui, sans-serif" font-size="13.5" font-weight="700" fill="#22d3ee">CAN-Bus-Intrusion-Defense</text>
      <text x="270" y="20" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1">Automotive vehicular network anomaly detection &amp; telemetry</text>
      <text x="650" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#a78bfa">Python · SocketCAN</text>
      <text x="830" y="20" font-family="'JetBrains Mono', monospace" font-size="11" fill="#e2e8f0">Telemetry Defense</text>
      <rect x="978" y="7" width="78" height="18" rx="9" fill="#142823"/>
      <text x="1017" y="20" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#34d399">RESEARCH SEC</text>
    </g>
  </g>

  <!-- ============================================================ -->
  <!-- ROW 3: SPLIT PANELS (Velocity Trend Chart + Engineering Signals) -->
  <!-- ============================================================ -->

  <!-- Left: CONTRIBUTION & RECONCILIATION VELOCITY (from analytics-grid) -->
  <g transform="translate(60,500)" filter="url(#ag-shadow)">
    <rect width="526" height="136" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>
    <text x="20" y="24" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2.5">RECONCILIATION &amp; COMMIT VELOCITY · 90 DAYS</text>

    <!-- Trend polyline area & line -->
    <polyline points="20,108 50,102 80,105 110,95 140,99 170,88 200,92 230,80 260,84 290,72 320,78 350,66 380,72 410,58 440,64 470,52 485,50" fill="url(#ag-spark-violet)"/>
    <polyline points="20,108 50,102 80,105 110,95 140,99 170,88 200,92 230,80 260,84 290,72 320,78 350,66 380,72 410,58 440,64 470,52 485,50 485,114 20,114" fill="url(#ag-spark-violet)"/>
    <polyline points="20,108 50,102 80,105 110,95 140,99 170,88 200,92 230,80 260,84 290,72 320,78 350,66 380,72 410,58 440,64 470,52 485,50" fill="none" stroke="#a78bfa" stroke-width="1.8"/>

    <!-- Concentric circles radar-blip live indicator (from analytics-grid) -->
    <circle cx="485" cy="50" r="4" fill="#fef3c7">
      <animate attributeName="r" values="4;7;4" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="485" cy="50" r="10" fill="none" stroke="#fef3c7" stroke-width="0.8">
      <animate attributeName="r" values="10;18;10" dur="1.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0;0.7" dur="1.6s" repeatCount="indefinite"/>
    </circle>

    <text x="485" y="122" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="9" fill="#a78bfa">peak · sustained cadence · 90d</text>
  </g>

  <!-- Right: ENGINEERING SIGNALS & GOVERNANCE COMMITMENTS (from oss-maintainer) -->
  <g transform="translate(614,500)" filter="url(#ag-shadow)">
    <rect width="526" height="136" rx="12" fill="url(#ag-card)" stroke="#1f2540" stroke-width="0.8"/>
    <text x="20" y="24" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="2.5">ENGINEERING SIGNALS &amp; OPERATIONAL DISCIPLINE</text>

    <!-- 4 Structured Signal Blocks -->
    <g transform="translate(20,44)">
      <!-- Signal 1: Architecture -->
      <g transform="translate(0,0)">
        <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b" letter-spacing="2">CORE ARCHITECTURE</text>
        <text x="0" y="18" font-family="'Inter', system-ui, sans-serif" font-size="14" font-weight="700" fill="#22d3ee">Zero Trust Core</text>
        <text x="0" y="32" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#94a3b8">Continuous verification</text>
      </g>

      <!-- Signal 2: Scale -->
      <g transform="translate(260,0)">
        <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b" letter-spacing="2">IDENTITY SCALE</text>
        <text x="0" y="18" font-family="'Inter', system-ui, sans-serif" font-size="14" font-weight="700" fill="#a78bfa">300K+ Monthly</text>
        <text x="0" y="32" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#94a3b8">Reconciled across 9 zones</text>
      </g>

      <!-- Signal 3: Quality -->
      <g transform="translate(0,44)">
        <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b" letter-spacing="2">TEST ASSURANCE</text>
        <text x="0" y="18" font-family="'Inter', system-ui, sans-serif" font-size="14" font-weight="700" fill="#34d399">90% Coverage</text>
        <text x="0" y="32" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#94a3b8">Automated pipeline tests</text>
      </g>

      <!-- Signal 4: JML Lifecycle -->
      <g transform="translate(260,44)">
        <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b" letter-spacing="2">LIFECYCLE SPEEDUP</text>
        <text x="0" y="18" font-family="'Inter', system-ui, sans-serif" font-size="14" font-weight="700" fill="#f472b6">30–40% Fast</text>
        <text x="0" y="32" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#94a3b8">Joiner-Mover-Leaver JML</text>
      </g>
    </g>
  </g>

  <!-- ============================================================ -->
  <!-- FOOTER SIGNATURE -->
  <!-- ============================================================ -->
  <g transform="translate(60,658)" font-family="'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace" font-size="10" letter-spacing="3" fill="#475569">
    <text>SUBHAJIT KAR  ·  DELOITTE CYBER RISK  ·  VERIFIED PORTFOLIO TELEMETRY</text>
    <text x="1080" y="0" text-anchor="end" fill="#22d3ee" letter-spacing="2">● PURPOSE-BUILT ARCHITECTURE</text>
  </g>
</svg>'''
    return svg

def main():
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    profile_repo_root = os.path.join(workspace_root, "profile-repo")

    svg_content = build_svg()

    # Target 1: workspace assets
    target_1 = os.path.join(workspace_root, "assets", "developer-analytics.svg")
    with open(target_1, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated: {target_1}")

    # Target 2: profile-repo assets (if nested workspace)
    if os.path.isdir(profile_repo_root):
        target_2 = os.path.join(profile_repo_root, "assets", "developer-analytics.svg")
        with open(target_2, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated: {target_2}")

if __name__ == "__main__":
    main()
