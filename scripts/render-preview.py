#!/usr/bin/env python3
"""
Renders preview/README.md into a high-fidelity GitHub-styled HTML preview (preview/index.html).
Supports toggling between GitHub Dark Mode and Light Mode.
"""

from pathlib import Path
import re
import time

PREVIEW_DIR = Path("/Users/subhajkar/Developer/GitHub-Profile-Transformation/preview")
README_FILE = PREVIEW_DIR / "README.md"
OUTPUT_HTML = PREVIEW_DIR / "index.html"

def main():
    content = README_FILE.read_text(encoding="utf-8")
    ts = int(time.time())

    # In index.html, relative assets are at ../assets/
    adjusted_content = content.replace('src="assets/', 'src="../assets/')
    adjusted_content = adjusted_content.replace('src="profile-3d-contrib/', 'src="../profile-3d-contrib/')
    # Inject timestamp cache buster on all local SVG images
    adjusted_content = re.sub(r'(\.\./assets/[a-zA-Z0-9_\-\./]+\.svg)(\?[^"]*)?', rf'\1?t={ts}', adjusted_content)

    html_template = f"""<!DOCTYPE html>
<html lang="en" data-color-mode="dark" data-dark-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>GitHub Profile Preview — Subhajit Kar (@ha4kerspidersks)</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

  <style>
    body {{
      background-color: #0d1117;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .preview-header {{
      width: 100%;
      max-width: 1012px;
      margin-bottom: 20px;
      padding: 16px 20px;
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-sizing: border-box;
    }}
    .preview-title {{
      font-weight: 600;
      font-size: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .theme-toggle-btn {{
      background: #21262d;
      color: #c9d1d9;
      border: 1px solid #30363d;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
      font-weight: 500;
    }}
    .theme-toggle-btn:hover {{
      background: #30363d;
    }}
    .github-container {{
      width: 100%;
      max-width: 1012px;
      border: 1px solid #30363d;
      border-radius: 6px;
      background-color: #0d1117;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .repo-banner {{
      padding: 12px 16px;
      background-color: #161b22;
      border-bottom: 1px solid #30363d;
      font-size: 13px;
      color: #8b949e;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .repo-banner strong {{
      color: #58a6ff;
    }}
    .markdown-body {{
      padding: 32px 40px;
      box-sizing: border-box;
      background-color: transparent !important;
      color: inherit;
    }}
    .markdown-body table {{
      display: table !important;
      width: 100% !important;
      border-collapse: collapse !important;
    }}
    .markdown-body table th, .markdown-body table td {{
      border: 1px solid #30363d !important;
      padding: 12px 16px !important;
    }}
  </style>
</head>
<body>

  <header class="preview-header" role="banner">
    <div class="preview-title">
      <svg height="20" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="20" fill="currentColor">
        <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
      </svg>
      <h1 style="margin:0;font-size:16px;font-weight:600;display:inline;">GitHub Profile Preview: <strong>ha4kerspidersks / README.md</strong></h1>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="theme-toggle-btn" onclick="forceReloadAssets()">🔄 Refresh SVGs</button>
      <button class="theme-toggle-btn" onclick="toggleTheme()">🌓 Toggle Dark/Light Mode</button>
    </div>
  </header>

  <main class="github-container" role="main">
    <div class="repo-banner">
      <span>📁 ha4kerspidersks / <strong>README.md</strong> (Profile Landing Page)</span>
    </div>
    <div id="content" class="markdown-body"></div>
  </main>

  <script>
    const rawMarkdown = {repr(adjusted_content)};
    document.getElementById('content').innerHTML = marked.parse(rawMarkdown);

    // Auto-bust cache on initial page load
    forceReloadAssets();

    function forceReloadAssets() {{
      const imgs = document.querySelectorAll('#content img');
      const now = Date.now();
      imgs.forEach(img => {{
        const src = img.getAttribute('src');
        if (src && !src.startsWith('https://img.shields.io') && !src.startsWith('https://komarev.com')) {{
          const cleanSrc = src.split('?')[0];
          img.src = `${{cleanSrc}}?t=${{now}}`;
        }}
      }});
    }}

    let isDark = true;
    function toggleTheme() {{
      isDark = !isDark;
      if (isDark) {{
        document.body.style.backgroundColor = '#0d1117';
        document.body.style.color = '#e6edf3';
        document.querySelector('.github-container').style.backgroundColor = '#0d1117';
        document.querySelector('.preview-header').style.backgroundColor = '#161b22';
        document.querySelector('.repo-banner').style.backgroundColor = '#161b22';
      }} else {{
        document.body.style.backgroundColor = '#f6f8fa';
        document.body.style.color = '#1f2328';
        document.querySelector('.github-container').style.backgroundColor = '#ffffff';
        document.querySelector('.preview-header').style.backgroundColor = '#eaeef2';
        document.querySelector('.repo-banner').style.backgroundColor = '#eaeef2';
      }}
    }}
  </script>
</body>
</html>
"""
    OUTPUT_HTML.write_text(html_template, encoding="utf-8")
    print(f"Preview HTML generated at {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
