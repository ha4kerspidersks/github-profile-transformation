#!/usr/bin/env python3
import os
import re
from pathlib import Path

SKILLS_DIR = Path("/Users/subhajkar/Developer/AI-Dev-Team/skills")
OUTPUT_FILE = Path("/Users/subhajkar/Developer/GitHub-Profile-Transformation/research/available-ai-dev-team-skills.md")

RELEVANCE_KEYWORDS = {
    "UI/UX & Design": ["ui", "ux", "design", "taste", "styleseed", "color", "layout", "aesthetic", "css", "visual"],
    "Browser QA & Testing": ["browser", "qa", "playwright", "puppeteer", "devtools", "testing", "audit", "screenshot"],
    "Accessibility & SEO": ["a11y", "accessibility", "seo", "wcag", "screen-reader"],
    "GitHub & Git Workflows": ["github", "git", "pr", "repo", "readme", "markdown", "commit", "release"],
    "Security & Secret Detection": ["security", "secret", "sast", "audit", "vulnerability", "cred", "007"],
    "IAM & Cloud Identity": ["iam", "identity", "iga", "saviynt", "entra", "azure", "aws"],
    "AI Agents & Orchestration": ["agent", "orchestrat", "mcp", "llm", "copilot", "prompt", "team"]
}

def parse_skill_md(file_path):
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return None, None
    
    # Extract YAML frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    name = file_path.parent.name
    desc = ""
    if fm_match:
        fm_text = fm_match.group(1)
        name_match = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
        if name_match:
            name = name_match.group(1).strip().strip("'\"")
        desc_match = re.search(r"^description:\s*(.+)$", fm_text, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip().strip("'\"")
    
    if not desc:
        # Fallback to first non-heading paragraph
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
        if lines:
            desc = lines[0][:200]
            
    return name, desc

def main():
    skill_files = []
    for root, dirs, files in os.walk(SKILLS_DIR, followlinks=True):
        if "SKILL.md" in files:
            skill_files.append(Path(root) / "SKILL.md")
    print(f"Discovered {len(skill_files)} SKILL.md files.")
    
    categorized_skills = {k: [] for k in RELEVANCE_KEYWORDS}
    all_skills = []

    for sf in sorted(skill_files):
        try:
            rel_path = sf.relative_to(SKILLS_DIR)
        except ValueError:
            rel_path = sf.name
        name, desc = parse_skill_md(sf)
        if not name:
            name = sf.parent.name
        
        assigned_categories = []
        full_text = f"{name} {desc} {str(rel_path)}".lower()
        for cat, kws in RELEVANCE_KEYWORDS.items():
            if any(kw in full_text for kw in kws):
                assigned_categories.append(cat)
                categorized_skills[cat].append({
                    "name": name,
                    "rel_path": str(sf),
                    "desc": desc,
                    "cat": cat
                })
        
        all_skills.append({
            "name": name,
            "path": str(sf),
            "desc": desc,
            "categories": assigned_categories
        })

    # Generate Markdown
    lines = [
        "# AI Dev Team Skills Inventory & Ecosystem Mapping",
        "",
        f"**Discovery Root:** `{SKILLS_DIR}`  ",
        f"**Total Skills Found:** {len(skill_files)}  ",
        f"**Timestamp:** 2026-10-02  ",
        "",
        "This catalog inventories the complete AI Dev Team skills ecosystem, specifically mapping capabilities directly applicable to the **Autonomous GitHub Profile Transformation** pipeline.",
        "",
        "---",
        "",
        "## 1. Primary Skill Orchestration for Profile Transformation",
        "",
        "| Transformation Phase | Lead Skill / Discipline | Ecosystem Path | Specific Value & Applied Capability |",
        "|---|---|---|---|",
        "| **1. UI/UX & Visual Architecture** | `styleseed-design-review`, `design-taste-frontend` | `skills/agentic-awesome-skills/styleseed-design-review` | Anti-AI-slop design review, high-end typography, visual hierarchy, spacing, modern layout design |",
        "| **2. Modern Web & Presentation** | `modern-web-guidance`, `ui-skills` | `skills/agentic-awesome-skills/ui-skills` | Semantic markup, dark/light contrast, SVG design tokens, mobile responsiveness |",
        "| **3. Browser QA & Verification** | `browser-qa`, `browser-e2e-audit` | `skills/browser-qa`, `skills/browser-e2e-audit` | Headless browser verification, rendering checks, screenshot regression, broken link detection |",
        "| **4. Accessibility (A11y)** | `ui-a11y`, `screen-reader-testing` | `skills/agentic-awesome-skills/ui-a11y` | WCAG contrast ratio for SVG badges/cards, screen-reader semantic alt tags, ARIA attributes |",
        "| **5. SEO & Social Discovery** | `frontend-seo` | `skills/agentic-awesome-skills/frontend-seo` | OpenGraph tags, metadata descriptions, structured schema, profile discoverability |",
        "| **6. Security & Secret Defense** | `007`, `security-audit-recon`, `cred-omega` | `skills/007`, `skills/security-audit-recon` | Strict credential/token pre-push scanning (Git history, config, env leaks) |",
        "| **7. GitHub & Git Operations** | `github`, `git-workflow`, `smart-git-automation` | `skills/agentic-awesome-skills/smart-git-automation` | Atomic commit crafting, branch control, remote push gating, release integrity |",
        "| **8. Multi-Agent Review** | `code-reviewer`, `multi-agent-review` | `skills/multi-agent-review` | Independent multi-perspective verification before human approval gate |",
        "",
        "---",
        "",
        "## 2. Categorized Skill Inventory for Profile Engineering",
        ""
    ]

    for cat, skills in categorized_skills.items():
        lines.append(f"### {cat} ({len(skills)} Skills Found)")
        lines.append("")
        lines.append("| Skill Name | Location | Description & Capabilities | Relevance to GitHub Profile |")
        lines.append("|---|---|---|---|")
        for s in skills[:25]:
            desc_clean = s['desc'].replace("|", "/").replace("\n", " ")[:140]
            rel_path_short = s['rel_path'].replace("/Users/subhajkar/Developer/AI-Dev-Team/", "")
            lines.append(f"| **`{s['name']}`** | `{rel_path_short}` | {desc_clean}... | Directly applicable to {cat.lower()} audit & verification |")
        if len(skills) > 25:
            lines.append(f"| *...and {len(skills) - 25} more* | *Various* | Additional specialist skills available in ecosystem | Extended catalog available |")
        lines.append("")

    lines.append("---")
    lines.append(f"## 3. Total Inventory Summary")
    lines.append(f"- **Total Cataloged Skills:** {len(all_skills)}")
    for cat in RELEVANCE_KEYWORDS:
        lines.append(f"- **{cat}:** {len(categorized_skills[cat])}")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Inventory saved successfully to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
