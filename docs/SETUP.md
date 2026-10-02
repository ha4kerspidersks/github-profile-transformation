# Setup & Environment Guide

This repository contains the automated source pipeline, 3D vector generator, data models, and validation engine for generating and maintaining Subhajit Kar's GitHub profile.

---

## 1. Prerequisites

The build and validation system requires only standard Python with no required third-party PIP packages:

- **Python 3.9+** (uses standard library: `json`, `xml.etree.ElementTree`, `re`, `html`, `pathlib`, `subprocess`, `http.server`).
- **Bash / Zsh shell** (macOS or Linux).
- **Node.js 18+** *(Optional)*: Only required if you wish to run headless browser screenshot capture (`Playwright`) or axe-core automated accessibility audits.

---

## 2. Quick Start

Clone this repository and run the automated build pipeline:

```bash
# 1. Clone the repository
git clone https://github.com/ha4kerspidersks/github-profile-transformation.git
cd github-profile-transformation

# 2. Run the pre-flight validation suite
./scripts/validate

# 3. Execute the full build pipeline
./scripts/build

# 4. Launch the local interactive preview server
./scripts/preview
```

Open your browser to `http://localhost:4114/preview/index.html` to inspect the generated profile rendered in GitHub Dark/Light mode styles.

---

## 3. Directory Layout

```
github-profile-transformation/
│
├── README.md                      # Source repository overview & documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Security & cleanliness exclusions
│
├── profile/                       # Structured Data Models (Source of Truth)
│   ├── profile-data.json          # Personal identity, title, hero badges, links
│   ├── technology-stack.json      # 56 technologies with metadata & logo paths
│   ├── projects.json              # 4 featured engineering projects
│   ├── experience.json            # Deloitte career progression & achievements
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
│   ├── profile/                   # High-res profile avatars (sidebar only)
│   ├── skills/
│   │   ├── logos/                 # 56 raw SVG brand logos
│   │   └── cards/                 # 56 generated 3D elevated vector cards
│   └── generated/                 # Automated output mirror
│
├── scripts/                       # Automation Pipeline
│   ├── build                      # Master build pipeline runner
│   ├── build.py                   # Python implementation of build runner
│   ├── validate                   # Validation & security audit suite runner
│   ├── validate.py                # Python validation & secret scanner
│   ├── generate-readme            # Template compiler runner
│   ├── generate-readme.py         # Python template compiler
│   ├── generate-tech-wall         # 3D SVG card generator runner
│   ├── generate-tech-wall.py      # Python 3D card generator
│   ├── generate-hero.py           # Technical hero banner generator
│   ├── render-preview.py          # HTML preview generator
│   └── preview                    # Local HTTP preview server launcher
│
├── preview/                       # Local HTML & Markdown Preview
│   ├── index.html                 # GitHub-styled preview page
│   └── README.md                  # Compiled target README
│
├── docs/                          # Detailed Guides
│   ├── SETUP.md                   # Environment & installation
│   ├── CUSTOMIZATION.md           # How to customize profile data & design
│   └── WORKFLOW.md                # Maintenance lifecycle & deploy guide
│
└── ci/
    └── validate.yml               # CI validation automation template
```

---

## 4. Verification

To verify that all dependencies and tools are functioning:

```bash
# Validate data integrity and check for secrets
./scripts/validate
```

Expected output:
```text
✅ ALL VALIDATION CHECKS PASSED!
  ✓ Zero missing assets
  ✓ All 56 technology cards XML-validated
  ✓ Profile configuration data complete
  ✓ Zero secrets, credentials, or .env files detected
```
