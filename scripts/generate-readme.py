#!/usr/bin/env python3
"""
Generate GitHub Profile README from structured profile data and markdown template.
Consumes:
- templates/README.template.md
- profile/profile-data.json
- profile/technology-stack.json
- profile/projects.json
- profile/experience.json
- profile/certifications.json
Outputs:
- preview/README.md
- optionally synchronizes to profile-repo/README.md if present
"""

import json
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_FILE = ROOT_DIR / "templates/README.template.md"
PROFILE_DATA_FILE = ROOT_DIR / "profile/profile-data.json"
TECH_STACK_FILE = ROOT_DIR / "profile/technology-stack.json"
PROJECTS_FILE = ROOT_DIR / "profile/projects.json"
EXPERIENCE_FILE = ROOT_DIR / "profile/experience.json"
CERTS_FILE = ROOT_DIR / "profile/certifications.json"

PREVIEW_README = ROOT_DIR / "preview/README.md"
PROFILE_REPO_README = ROOT_DIR / "profile-repo/README.md"

def build_cta_links(links_data):
    lines = []
    keys = ["portfolio", "linkedin", "github", "medium", "x"]
    for k in keys:
        item = links_data.get(k)
        if not item:
            continue
        url = item["url"]
        badge = item["badgeUrl"]
        label = item.get("label", k.capitalize())
        lines.append(f'  <a href="{url}">\n    <img src="{badge}" alt="{label}" />\n  </a>')
    return "&nbsp;\n".join(lines)

def build_tech_stack_wall(tech_data):
    # Sort by displayOrder
    sorted_tech = sorted(tech_data, key=lambda x: x.get("displayOrder", 999))
    elements = []
    for t in sorted_tech:
        name = t.get("name", t["id"])
        card_path = t.get("cardPath", f"assets/skills/cards/{t['id']}.svg")
        tab_url = t.get("portfolioTabUrl", "https://subhajitkar.com/?tab=iam")
        elements.append(f'<a href="{tab_url}" title="{name}"><img src="{card_path}" width="98" alt="{name}" /></a>')
    return "\n".join(elements)

def build_projects_table(projects_data):
    if len(projects_data) < 4:
        return "<!-- Insufficient projects -->"
    
    p0, p1, p2, p3 = projects_data[0], projects_data[1], projects_data[2], projects_data[3]

    p0_tech = " &middot; ".join([f"`{x}`" for x in p0["tech"]])
    p1_tech = " &middot; ".join([f"`{x}`" for x in p1["tech"]])
    p2_tech = " &middot; ".join([f"`{x}`" for x in p2["tech"]])
    p3_tech = " &middot; ".join([f"`{x}`" for x in p3["tech"]])

    table = f"""| {p0['icon']} [{p0['name']}]({p0['repoUrl']}) | {p1['icon']} [{p1['name']}]({p1['repoUrl']}) |
| :--- | :--- |
| {p0['description']}<br/><br/>**Tech:** {p0_tech}<br/>&rarr; [**View Repository**]({p0['repoUrl']}) | {p1['description']}<br/><br/>**Tech:** {p1_tech}<br/>&rarr; [**View Repository**]({p1['repoUrl']}) |
| {p2['icon']} [{p2['name']}]({p2['repoUrl']}) | {p3['icon']} [{p3['name']}]({p3['repoUrl']}) |
| {p2['description']}<br/><br/>**Tech:** {p2_tech}<br/>&rarr; [**View Repository**]({p2['repoUrl']}) | {p3['description']}<br/><br/>**Tech:** {p3_tech}<br/>&rarr; [**View Repository**]({p3['repoUrl']}) |"""
    return table

def build_experience_section(exp_data):
    sections = []
    for exp in exp_data:
        company = exp["company"]
        role = exp["role"]
        division = exp.get("division", "")
        period = exp["period"]
        div_text = f" *({division} | {period})*" if division else f" *({period})*"
        
        header = f"### **{role} &middot; {company}**{div_text}"
        bullet_lines = "\n".join([f"- {b}" for b in exp.get("responsibilities", [])])
        sections.append(f"{header}\n{bullet_lines}")
    
    return "\n\n".join(sections)

def build_certifications_section(certs_data):
    badges = []
    for c in certs_data:
        name = c["name"]
        badge_url = c["badgeUrl"]
        verify_url = c["verificationUrl"]
        badges.append(f"[![{name}]({badge_url})]({verify_url})")
    return "\n".join(badges)

def generate_readme():
    if not TEMPLATE_FILE.exists():
        print(f"❌ Template not found: {TEMPLATE_FILE}", file=sys.stderr)
        return False

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    with open(PROFILE_DATA_FILE, "r", encoding="utf-8") as f:
        profile_data = json.load(f)

    with open(TECH_STACK_FILE, "r", encoding="utf-8") as f:
        tech_data = json.load(f)

    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        projects_data = json.load(f)

    with open(EXPERIENCE_FILE, "r", encoding="utf-8") as f:
        experience_data = json.load(f)

    with open(CERTS_FILE, "r", encoding="utf-8") as f:
        certs_data = json.load(f)

    personal = profile_data.get("personal", {})
    hero_alt = f"{personal.get('name', 'Subhajit Kar')} - {personal.get('role', 'Senior IAM Assistant Manager')} - {personal.get('specialization', 'Enterprise Identity Governance & Data Analytics')}"
    
    cta_links = build_cta_links(profile_data.get("links", {}))
    tech_wall = build_tech_stack_wall(tech_data)
    projects_table = build_projects_table(projects_data)
    experience_section = build_experience_section(experience_data)
    certs_section = build_certifications_section(certs_data)

    content = template.replace("{{HERO_ALT}}", hero_alt)
    content = content.replace("{{CTA_LINKS}}", cta_links)
    content = content.replace("{{TECH_STACK_WALL}}", tech_wall)
    content = content.replace("{{PROJECTS_TABLE}}", projects_table)
    content = content.replace("{{EXPERIENCE_SECTION}}", experience_section)
    content = content.replace("{{CERTIFICATIONS_SECTION}}", certs_section)

    PREVIEW_README.parent.mkdir(parents=True, exist_ok=True)
    with open(PREVIEW_README, "w", encoding="utf-8") as out:
        out.write(content)
    print(f"✅ Generated README at {PREVIEW_README}")

    sync_profile = "--sync-profile" in sys.argv
    if sync_profile and PROFILE_REPO_README.parent.exists():
        with open(PROFILE_REPO_README, "w", encoding="utf-8") as out:
            out.write(content)
        print(f"✅ Synchronized README to {PROFILE_REPO_README}")
    elif not sync_profile:
        print("ℹ️ Note: Profile repository synchronization skipped (pass --sync-profile to update).")

    return True

if __name__ == "__main__":
    success = generate_readme()
    sys.exit(0 if success else 1)
