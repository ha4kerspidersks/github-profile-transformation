# GitHub Profile Transformation Engine

[![Build Pipeline](https://img.shields.io/badge/Build_Pipeline-Active-success.svg)](scripts/build)
[![Zero Secrets](https://img.shields.io/badge/Security-Zero_Secrets-brightgreen.svg)](docs/SETUP.md#security-assurance)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated engineering toolchain, structured data compiler, vector SVG card generator, and quality assurance framework powering **Subhajit Kar's GitHub Profile**.

---

## 📌 Project Overview

`github-profile-transformation` decouples profile content from presentation. Instead of manually editing markdown or maintaining hardcoded HTML/SVG files, profile content is modeled as structured JSON schemas (`profile/*.json`).

The compilation pipeline transforms these data sources into:
1. **Dynamic SVG Vector Assets**: 56 curated technology cards, hero identity banners, and architectural diagrams.
2. **Deterministic Markdown Templates**: Compiled into `preview/README.md` and synced to the profile repository `ha4kerspidersks/ha4kerspidersks`.
3. **Automated Quality & Security Gates**: Schema validation, XML well-formedness testing, dead-link auditing, and secret detection.

---

## 🏛️ System Architecture

```text
┌───────────────────────────────┐
│     Structured Data Source    │
│  profile/*.json (True Origin) │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      Transformation Engine    │
│  • scripts/build              │
│  • scripts/generate-cards.py  │
│  • scripts/generate-readme.py │
└───────────────┬───────────────┘
                │
                ├────────────────────────────────┐
                ▼                                ▼
┌───────────────────────────────┐┌───────────────────────────────┐
│     Compiled Vector Assets    ││       Profile Markdown        │
│ assets/*.svg (Cards & Banners)││ preview/README.md (Compiled)  │
└───────────────┬───────────────┘└───────────────┬───────────────┘
                │                                │
                └───────────────┬────────────────┘
                                │
                                ▼
                ┌───────────────────────────────┐
                │    QA & Validation Gates      │
                │  • XML / SVG Linting          │
                │  • Broken Link Detection      │
                │  • Gitleaks & Secret Scans    │
                └───────────────┬───────────────┘
                                │
                                ▼
                ┌───────────────────────────────┐
                │   Target Distribution Sync    │
                │   ha4kerspidersks/README.md   │
                └───────────────────────────────┘
```

---

## 📁 Repository Structure

```text
GitHub-Profile-Transformation/
├── profile/                 # Structured JSON schemas (Source of Truth)
│   ├── profile-data.json    # Personal identity, verified title, credentials
│   ├── technology-stack.json# 56 verified production technologies
│   ├── projects.json        # Flagship repositories & metadata
│   ├── experience.json      # Enterprise IAM / Security career roles
│   └── metrics.json         # Enterprise identity reconciliation telemetry
├── assets/                  # Compiled SVGs, banners, and vector assets
├── scripts/                 # Automation scripts (build, validate, preview, sync)
│   ├── build                # Master build pipeline runner
│   ├── validate             # Post-build validation & security audit
│   ├── preview              # Local HTTP preview server
│   ├── generate-readme.py   # Markdown template compiler
│   └── export-to-profile.py # Syncs build output to ha4kerspidersks repo
├── templates/               # Markdown templates with handlebars syntax
├── docs/                    # Architectural and setup documentation
│   ├── SETUP.md             # Environment setup and dependencies
│   ├── WORKFLOW.md          # Step-by-step operating lifecycle
│   └── CUSTOMIZATION.md     # Guide for adding cards, roles, and themes
└── preview/                 # Local compiled artifacts for browser inspection
```

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.9+** (uses standard library: `json`, `xml.etree`, `pathlib`, `http.server`)
- **Bash / Zsh** (macOS or Linux)

### 2. Execution Workflow

```bash
# Clone repository
git clone https://github.com/ha4kerspidersks/github-profile-transformation.git
cd github-profile-transformation

# 1. Run pre-flight validation
./scripts/validate

# 2. Execute full compilation pipeline
./scripts/build

# 3. Launch local interactive preview
./scripts/preview
```

Open `http://localhost:4114/preview/index.html` to inspect the generated profile rendered in dark and light modes.

---

## 🛡️ Security & Integrity

- **Zero Secrets Policy**: All API keys, tokens, session cookies, and local configurations are strictly excluded via `.gitignore`.
- **Authentic Metrics**: Hardcoded fake stars and fabricated stats are prohibited; all data must reflect authentic repository state and verified enterprise achievements.
- **Automated Validation**: The `./scripts/validate` suite runs automated checks ensuring zero missing assets, zero broken links, and full XML compliance before any commit.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
