# Maintenance & Development Workflow

This document explains the standard operating procedure for modifying, building, verifying, and publishing updates to your GitHub profile.

---

## 1. Operating Lifecycle

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  EDIT DATA   │ ──> │  RUN BUILD   │ ──> │ LOCAL PREVIEW│
│ profile/*.json     │ ./scripts/build     │./scripts/preview
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  DEPLOY/PUSH │ <── │  COMMIT GIT  │ <── │ QA & AUDIT   │
│ profile repo │     │ git commit   │     │./scripts/validate
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## 2. Step-by-Step Execution

### Step 1: Edit Structured Source Data
Never edit `README.md` directly. Make your changes in the corresponding JSON source file under `profile/`:
- Personal title / hero: `profile/profile-data.json`
- Tech cards / logos: `profile/technology-stack.json`
- Projects: `profile/projects.json`
- Career roles: `profile/experience.json`
- Metrics: `profile/metrics.json`
- Certifications: `profile/certifications.json`

### Step 2: Run the Build Pipeline
Execute the master build script from the repository root:

```bash
./scripts/build
```

This single command:
1. Validates all input data.
2. Regenerates any changed 3D skill cards.
3. Updates the technical vector hero banner.
4. Compiles the markdown template into `preview/README.md`.
5. Renders `preview/index.html`.
6. Executes post-build XML validation and secret scanning.

### Step 3: Inspect Local Preview
Launch the local HTTP preview server:

```bash
./scripts/preview
```

Navigate to `http://localhost:4114/preview/index.html` to inspect the visual rendering in both Dark Mode and Light Mode.

### Step 4: Run QA & Security Audit
Run the automated verification suite:

```bash
./scripts/validate
```

The script ensures:
- All 56 cards exist and contain valid XML.
- All asset paths are intact with 0 missing files.
- Zero secrets, API tokens, private keys, or `.env` files exist.

### Step 5: Commit Changes to Source Repository
Once verified, commit the updated source data and generated assets:

```bash
git add profile/ assets/ preview/ templates/
git status
git commit -m "Update profile data: <description of change>"
git push origin main
```

---

## 3. Deploying to the Live Profile Repository

Your live GitHub profile README lives in the special user repository [`ha4kerspidersks/ha4kerspidersks`](https://github.com/ha4kerspidersks/ha4kerspidersks).

To publish changes to your live GitHub profile:

1. Build with the `--sync-profile` flag:
   ```bash
   python3 scripts/generate-readme.py --sync-profile
   ```
2. Or use the provided synchronization script:
   ```bash
   python3 scripts/export-to-profile.py
   ```
3. Navigate to your local profile repository clone, review diffs, commit, and push:
   ```bash
   cd ~/Developer/GitHub-Profile-Transformation/profile-repo
   git status
   git diff
   git commit -am "Update GitHub profile README"
   git push origin main
   ```
