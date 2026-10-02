#!/usr/bin/env python3
"""
Export & Synchronize Generated Assets to Live Profile Repository.
Safely copies preview/README.md and all required vector assets
into profile-repo/ without modifying any git commit state automatically.
"""

import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PROFILE_REPO = ROOT_DIR / "profile-repo"
PREVIEW_README = ROOT_DIR / "preview/README.md"

def main():
    if not PROFILE_REPO.exists():
        print(f"❌ Target profile repository not found at {PROFILE_REPO}", file=sys.stderr)
        return False

    print(f"📦 Synchronizing profile assets to {PROFILE_REPO}...")

    # 1. Copy README.md
    shutil.copy2(PREVIEW_README, PROFILE_REPO / "README.md")
    print("  ✓ Synchronized README.md")

    # 2. Copy Hero Banner & Banners
    dest_assets = PROFILE_REPO / "assets"
    dest_assets.mkdir(parents=True, exist_ok=True)
    
    for banner in ["hero-banner.svg", "architecture-matrix.svg", "metrics-banner.svg", "tech-stack-header.svg"]:
        src_banner = ROOT_DIR / f"assets/{banner}"
        if src_banner.exists():
            shutil.copy2(src_banner, dest_assets / banner)
            print(f"  ✓ Synchronized assets/{banner}")

    # 3. Copy Skill Cards
    dest_cards = dest_assets / "skills/cards"
    dest_cards.mkdir(parents=True, exist_ok=True)
    src_cards = ROOT_DIR / "assets/skills/cards"
    card_count = 0
    for card in src_cards.glob("*.svg"):
        shutil.copy2(card, dest_cards / card.name)
        card_count += 1
    print(f"  ✓ Synchronized {card_count} skill cards to assets/skills/cards/")

    # 4. Copy Profile Avatar Image
    dest_profile = dest_assets / "profile"
    dest_profile.mkdir(parents=True, exist_ok=True)
    src_profile = ROOT_DIR / "assets/profile"
    if src_profile.exists():
        for img in src_profile.glob("*.*"):
            shutil.copy2(img, dest_profile / img.name)
            print(f"  ✓ Synchronized assets/profile/{img.name}")

    print("\n✅ Synchronization complete!")
    print("   To publish, navigate to profile-repo, review git status/diff, and commit.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
