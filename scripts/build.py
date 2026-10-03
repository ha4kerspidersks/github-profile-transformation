#!/usr/bin/env python3
"""
Master Build Runner for GitHub Profile Transformation (Master V2).
Orchestrates:
1. Pre-build validation of source data
2. Generation of 56 individual 3D technology cards
3. Generation of widescreen cinematic hero banner (assets/hero.svg)
4. Generation of unified 56-technology constellation wall (assets/stack.svg)
5. Generation of enterprise IAM/IGA pipeline architecture (assets/iam-architecture.svg)
6. Generation of holographic security clearance ID badge & dashboard (assets/id-dashboard.svg)
7. Generation of cyber communications connect panel (assets/connect.svg)
8. Compilation of profile README from templates and JSON data
9. Generation of high-fidelity HTML preview (preview/index.html)
10. Post-build verification & security audit
"""

import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"

def run_step(step_name, command):
    print(f"\n🚀 STEP: {step_name}")
    print(f"   Command: {' '.join(command)}")
    result = subprocess.run(command, cwd=str(ROOT_DIR))
    if result.returncode != 0:
        print(f"\n❌ Step '{step_name}' failed with exit code {result.returncode}", file=sys.stderr)
        return False
    return True

def main():
    print("============================================================")
    print("   GITHUB PROFILE TRANSFORMATION — MASTER V2 BUILD PIPELINE ")
    print("============================================================")

    steps = [
        ("Pre-build Validation", [sys.executable, str(SCRIPTS_DIR / "validate.py")]),
        ("Generate 3D Technology Wall Cards", [sys.executable, str(SCRIPTS_DIR / "generate-tech-wall.py")]),
        ("Generate Cinematic Widescreen Hero Banner", [sys.executable, str(SCRIPTS_DIR / "generate-hero-v2.py")]),
        ("Generate Unified 56-Tech Constellation Wall", [sys.executable, str(SCRIPTS_DIR / "generate-unified-stack.py")]),
        ("Generate Enterprise IAM/IGA Visual Pipeline", [sys.executable, str(SCRIPTS_DIR / "generate-iam-visual.py")]),
        ("Generate Holographic Clearance ID & Dashboard", [sys.executable, str(SCRIPTS_DIR / "generate-id-dashboard.py")]),
        ("Generate Cyber Communications Connect Panel", [sys.executable, str(SCRIPTS_DIR / "generate-connect-visual.py")]),
        ("Compile README from Template & Profile Data", [sys.executable, str(SCRIPTS_DIR / "generate-readme.py")]),
        ("Render HTML Preview", [sys.executable, str(SCRIPTS_DIR / "render-preview.py")]),
        ("Post-build Verification & Security Scan", [sys.executable, str(SCRIPTS_DIR / "validate.py")]),
    ]

    for name, cmd in steps:
        if not run_step(name, cmd):
            sys.exit(1)

    # Sync preview/README.md to root README.md
    preview_readme = ROOT_DIR / "preview/README.md"
    root_readme = ROOT_DIR / "README.md"
    if preview_readme.exists():
        root_readme.write_text(preview_readme.read_text(encoding="utf-8"), encoding="utf-8")

    print("\n" + "=" * 60)
    print("🎉 MASTER V2 BUILD COMPLETE & VERIFIED!")
    print("   Output README:       README.md & preview/README.md")
    print("   Preview HTML:        preview/index.html")
    print("   Hero Banner:         assets/hero.svg")
    print("   Tech Constellation:  assets/stack.svg (56 Verified Engines)")
    print("   IAM/IGA Visual:      assets/iam-architecture.svg")
    print("   Holographic ID:      assets/id-dashboard.svg")
    print("   Connect Panel:       assets/connect.svg")
    print("   Square Avatar:       assets/avatar/github-avatar.png")
    print("============================================================")

if __name__ == "__main__":
    main()
