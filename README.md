# GitHub Profile Transformation & Design System

<div align="center">

[![CI Pipeline](https://img.shields.io/badge/CI-Automated_Validation-10B981?style=flat-square&logo=githubactions&logoColor=white)](ci/validate.yml)
[![Live GitHub Profile](https://img.shields.io/badge/Live_Profile-ha4kerspidersks-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ha4kerspidersks)
[![Portfolio](https://img.shields.io/badge/Portfolio-subhajitkar.com-00F2FE?style=flat-square&logo=googlechrome&logoColor=black)](https://subhajitkar.com)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Zero Secrets](https://img.shields.io/badge/Security_Scan-PASSED-10B981?style=flat-square&logo=shield)](scripts/validate.py)

**The automated source engine, 3D vector card generator, data pipeline, and design system that powers Subhajit Kar's official GitHub profile.**

[Live Profile](https://github.com/ha4kerspidersks) &nbsp;&bull;&nbsp; [Quick Start](#quick-start) &nbsp;&bull;&nbsp; [Customization Guide](docs/CUSTOMIZATION.md) &nbsp;&bull;&nbsp; [Workflow](docs/WORKFLOW.md) &nbsp;&bull;&nbsp; [Setup Guide](docs/SETUP.md)

</div>

---

## Overview

This repository is the dedicated **source and maintenance workspace** for generating, testing, and updating [`ha4kerspidersks/ha4kerspidersks`](https://github.com/ha4kerspidersks).

Instead of maintaining a fragile, monolithic, hand-edited markdown file, this system enforces **clean separation of data from visual design**:

```text
┌───────────────────────────┐      ┌───────────────────────────┐
│   STRUCTURED DATA (JSON)  │      │    MARKDOWN TEMPLATES     │
│  profile/profile-data.json│      │ templates/README.template │
│  profile/tech-stack.json  │      └─────────────┬─────────────┘
│  profile/projects.json    │                    │
│  profile/experience.json  │                    │
└─────────────┬─────────────┘                    │
              │                                  │
              ▼                                  ▼
      ┌──────────────────────────────────────────────────┐
      │             MASTER BUILD PIPELINE                │
      │                ./scripts/build                   │
      └───────────────────────┬──────────────────────────┘
                              │
       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  3D CARDS    │      │ HERO BANNER  │      │TARGET README │
│56 Vector SVGs│      │1200x340 SVG  │      │preview/README│
└──────────────┘      └──────────────┘      └──────┬───────┘
                                                   │
                                                   ▼
                                            ┌──────────────┐
                                            │ LIVE PROFILE │
                                            │ha4kerspidersks│
                                            └──────────────┘
```

---

## Key Features

1. **Separation of Data from Design:**
   - Modify name, title, role, or badges in [`profile/profile-data.json`](profile/profile-data.json).
   - Add, reorder, or update any of the 56 technologies in [`profile/technology-stack.json`](profile/technology-stack.json).
   - Update engineering projects in [`profile/projects.json`](profile/projects.json).
   - Update career experience in [`profile/experience.json`](profile/experience.json).
2. **3D Dimensional Technology Wall Generator:**
   - Script [`scripts/generate-tech-wall.py`](scripts/generate-tech-wall.py) generates physical elevated 3D cards with multi-layer drop shadows, bevel extrusion lips, specular glass chamfers, and gold primary badges.
   - Outputs 100% vector SVGs that render natively in GitHub Dark/Light mode with zero broken assets.
   - **Zero Category Clutter:** Enforces a unified 56-card visual wall without category titles or explanatory prose.
3. **Wide Horizontal Technical Hero Banner:**
   - Script [`scripts/generate-hero.py`](scripts/generate-hero.py) generates a 1200×340 vector banner with a live status chip, technical coordinate grid, typography, focus rule, capability pills, and a subtle right-side cybersecurity/IAM radar network.
   - **Zero Profile Photos in Banner/README:** Keeps profile imagery reserved exclusively for the GitHub account avatar.
4. **Automated Validation & Secret Audit Suite:**
   - [`scripts/validate.py`](scripts/validate.py) enforces zero broken assets, validates XML well-formedness on all cards and banners, verifies JSON schemas, and scans for accidental API tokens or `.env` files.
5. **Local High-Fidelity Preview:**
   - [`scripts/preview.py`](scripts/preview.py) serves the profile locally with GitHub markdown stylesheets and interactive dark/light mode toggles.

---

## Quick Start

### 1. Run the Validation Suite
```bash
./scripts/validate
```

### 2. Execute the Full Build Pipeline
```bash
./scripts/build
```

### 3. Launch the Local Preview
```bash
./scripts/preview
```
Open [http://localhost:4114/preview/index.html](http://localhost:4114/preview/index.html) in your browser.

---

## Project Structure

```
github-profile-transformation/
│
├── README.md                      # This documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules & security exclusions
│
├── profile/                       # Structured Source Data
│   ├── profile-data.json          # Personal identity, title, hero badges, links
│   ├── technology-stack.json      # Complete 56-tech inventory with logo paths
│   ├── projects.json              # 4 featured engineering projects
│   ├── experience.json            # Deloitte career progression & responsibilities
│   ├── metrics.json               # 4 verified impact metrics
│   └── certifications.json        # Professional credentials & badges
│
├── templates/                     # Layout Templates
│   └── README.template.md         # Master markdown profile template
│
├── assets/                        # Design System Assets
│   ├── hero/                      # Hero banner SVGs
│   ├── hero-banner.svg            # 1200x340 vector hero banner
│   ├── architecture-matrix.svg    # Pipeline architecture vector diagram
│   ├── metrics-banner.svg         # Verified metrics vector banner
│   ├── profile/                   # High-res profile avatar source images
│   ├── skills/
│   │   ├── logos/                 # 56 raw SVG brand logos
│   │   └── cards/                 # 56 generated 3D elevated vector cards
│   └── generated/                 # Mirrored output directory
│
├── scripts/                       # Automation Pipeline
│   ├── build                      # Master build pipeline runner
│   ├── build.py                   # Python build orchestration
│   ├── validate                   # Validation & security audit runner
│   ├── validate.py                # Python validation suite
│   ├── generate-readme            # Template compiler runner
│   ├── generate-readme.py         # Python template compiler
│   ├── generate-tech-wall         # 3D SVG card generator runner
│   ├── generate-tech-wall.py      # Python 3D card generator
│   ├── generate-hero.py           # Technical hero banner generator
│   ├── render-preview.py          # HTML preview generator
│   ├── export-to-profile.py       # Live profile repo synchronization tool
│   └── preview                    # Local HTTP preview server launcher
│
├── preview/                       # Local HTML & Markdown Preview
│   ├── index.html                 # GitHub-styled preview page
│   └── README.md                  # Compiled target README
│
├── docs/                          # Detailed Documentation
│   ├── SETUP.md                   # Environment & installation
│   ├── CUSTOMIZATION.md           # How to customize profile data & design
│   └── WORKFLOW.md                # Maintenance lifecycle & deploy guide
│
└── ci/
    └── validate.yml               # CI validation automation template
```

---

## Documentation

- **[docs/SETUP.md](docs/SETUP.md):** System requirements, prerequisites, and setup instructions.
- **[docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md):** How to change your title, add/remove technologies, update projects, or modify 3D visual styles.
- **[docs/WORKFLOW.md](docs/WORKFLOW.md):** Complete development lifecycle (`EDIT -> BUILD -> PREVIEW -> QA -> DEPLOY`).

---

## Publishing to the Live GitHub Profile

When you are ready to publish updates to [`ha4kerspidersks/ha4kerspidersks`](https://github.com/ha4kerspidersks):

```bash
# 1. Synchronize compiled README and assets to local profile clone
python3 scripts/export-to-profile.py

# 2. Inspect diffs and push from the profile repository
cd profile-repo
git status
git diff
git commit -am "Update GitHub profile README"
git push origin main
```

---

## Security & Compliance

- **Zero Secrets Policy:** Automated secret scanning in `scripts/validate.py` blocks tokens, private keys, and `.env` files.
- **Strict Project Isolation:** The live profile repository clone is isolated and managed through explicit opt-in deployment.

---

## License

MIT &copy; 2026 [Subhajit Kar](https://subhajitkar.com).
