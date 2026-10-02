# Profile Customization Guide

This guide details how to modify your identity, technologies, featured projects, career experience, and visual styling without manually editing markdown files.

---

## 1. Modifying Identity, Title & Hero Content

All personal identity and hero banner content is controlled by [`profile/profile-data.json`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/profile/profile-data.json).

### To Change Name, Role, or Specialization:
Edit the `personal` block:

```json
{
  "personal": {
    "name": "SUBHAJIT KAR",
    "role": "Senior IAM Assistant Manager",
    "specialization": "Enterprise Identity Governance & Large-Scale Data Analytics",
    "organization": "Deloitte Cyber & Strategic Risk",
    "statusIndicator": {
      "leftText": "DELOITTE CYBER & STRATEGIC RISK",
      "rightText": "ENTERPRISE IGA",
      "dotColor": "#10B981"
    },
    "focusLine": "Saviynt IGA · Identity Recon (300K+) · JML Workflows · AI Dev Team"
  }
}
```

### To Update Hero Badges:
Edit the `badges` array in `profile/profile-data.json`:

```json
{
  "badges": [
    { "id": "saviynt", "label": "SAVIYNT IGA", "color": "#00F2FE", "borderColor": "#00F2FE", "order": 1 },
    { "id": "iam_iga", "label": "IAM / IGA", "color": "#E2E8F0", "borderColor": "#38BDF8", "order": 2 },
    { "id": "cybersecurity", "label": "CYBERSECURITY", "color": "#34D399", "borderColor": "#10B981", "order": 3 },
    { "id": "ai_automation", "label": "AI & AUTOMATION", "color": "#D8B4FE", "borderColor": "#A855F7", "order": 4 }
  ]
}
```

### To Update Social & Portfolio Links:
Edit the `links` object in `profile/profile-data.json`.

Then re-run:
```bash
./scripts/build
```

---

## 2. Managing the Technology Stack

The technology stack is stored in [`profile/technology-stack.json`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/profile/technology-stack.json).

> [!IMPORTANT]
> The generated README **never displays category headings or explanatory text between logos**. Internal `category` fields exist solely for internal organization.

### How to Add a New Technology:
1. Place the SVG logo in `assets/skills/logos/<tech_id>/<tech_id>.svg`.
2. Add an entry to `profile/technology-stack.json`:

```json
{
  "id": "kubernetes",
  "name": "Kubernetes",
  "shortName": "Kubernetes",
  "category": "devops",
  "color": "#326CE5",
  "isPrimary": false,
  "technologyType": "Container Orchestration",
  "expertiseTier": "intermediate",
  "logoPath": "assets/skills/logos/kubernetes/kubernetes.svg",
  "cardPath": "assets/skills/cards/kubernetes.svg",
  "displayOrder": 57,
  "portfolioTabUrl": "https://subhajitkar.com/?tab=iam"
}
```

3. Re-run `./scripts/build`. The 3D card will be generated automatically and inserted into the unified wall.

### How to Remove a Technology:
1. Delete the corresponding JSON object from `profile/technology-stack.json`.
2. Re-run `./scripts/build`.

### How to Mark a Technology as Primary (Gold Indicator):
Set `"isPrimary": true` in `profile/technology-stack.json`. This automatically adds:
- Golden top-right radiant halo and dot (`#FFDB70`)
- Subtle warm gold label color (`#FFEDB3`)
- Higher border brightness and opacity

---

## 3. Updating Featured Engineering Projects

Projects are managed in [`profile/projects.json`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/profile/projects.json).

Edit any project's metadata:

```json
{
  "id": "AI-Dev-Team",
  "name": "AI-Dev-Team",
  "icon": "🤖",
  "repoUrl": "https://github.com/ha4kerspidersks/AI-Dev-Team",
  "description": "Autonomous multi-agent AI engineering dev team coordinating 3,200+ specialized skills across Gemini, Claude, and Copilot backends.",
  "tech": [
    "Python",
    "Node.js",
    "Model Context Protocol (MCP)",
    "Multi-Agent"
  ]
}
```

The 2×2 project table in the README is automatically reconstructed on build.

---

## 4. Updating Career Experience & Metrics

- **Career Roles & Bullets:** Edit [`profile/experience.json`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/profile/experience.json).
- **Impact Metrics:** Edit [`profile/metrics.json`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/profile/metrics.json).
- **Certifications & Badges:** Edit [`profile/certifications.json`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/profile/certifications.json).

---

## 5. Customizing the 3D Card Visual Aesthetics

The physical 3D appearance of the skill cards is governed by [`scripts/generate-tech-wall.py`](file:///Users/subhajkar/Developer/GitHub-Profile-Transformation/scripts/generate-tech-wall.py):

- **Extrusion Depth:** Modify the bevel thickness rectangle in line 114:
  `rx="12" fill="url(#bevelShadow)"`
- **Elevation Drop Shadows:** Modify opacity and offset on the ambient drop shadow rects (lines 110-111).
- **Glass Chamfer Highlight:** Modify stroke opacity of inner reflection rect (line 120).
- **Card Dimensions:** Standard 104×106 viewBox (renders at `width="98"` in markdown for uniform grid layout).

---

## 6. Regenerating Output

Whenever any file in `profile/` or `templates/` is edited:

```bash
./scripts/build
```

To view the updated profile:
```bash
./scripts/preview
```
