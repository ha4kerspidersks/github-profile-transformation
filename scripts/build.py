#!/usr/bin/env python3
"""
Master Build Runner for GitHub Profile Transformation.
Orchestrates:
1. Validation of source data
2. Generation of 3D technology cards
3. Generation of wide horizontal technical hero banner
4. Compilation of profile README from templates and JSON data
5. Generation of HTML preview (preview/index.html)
6. Final integrity validation & security audit
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
    print("       GITHUB PROFILE TRANSFORMATION — BUILD PIPELINE       ")
    print("============================================================")

    steps = [
        ("Pre-build Validation", [sys.executable, str(SCRIPTS_DIR / "validate.py")]),
        ("Generate 3D Technology Wall Cards", [sys.executable, str(SCRIPTS_DIR / "generate-tech-wall.py")]),
        ("Generate Technical Hero Banner", [sys.executable, str(SCRIPTS_DIR / "generate-hero.py")]),
        ("Compile README from Template & Profile Data", [sys.executable, str(SCRIPTS_DIR / "generate-readme.py")]),
        ("Render HTML Preview", [sys.executable, str(SCRIPTS_DIR / "render-preview.py")]),
        ("Post-build Verification & Security Scan", [sys.executable, str(SCRIPTS_DIR / "validate.py")]),
    ]

    for name, cmd in steps:
        if not run_step(name, cmd):
            sys.exit(1)

    print("\n" + "=" * 60)
    print("🎉 BUILD COMPLETE & VERIFIED!")
    print("   Output README: preview/README.md")
    print("   Preview HTML:  preview/index.html")
    print("   Hero Banner:   assets/hero-banner.svg")
    print("   3D Tech Wall:  assets/skills/cards/ (56 SVGs)")
    print("============================================================")

if __name__ == "__main__":
    main()
