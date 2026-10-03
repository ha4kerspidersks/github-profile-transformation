import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const QA_DIR = path.resolve(process.cwd(), 'qa');

async function main() {
  const b1 = fs.readFileSync(path.join(QA_DIR, 'architect-card-before.png')).toString('base64');
  const a1 = fs.readFileSync(path.join(QA_DIR, 'architect-card-after.png')).toString('base64');

  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Architect Card Transformation Audit</title>
        <style>
          body {
            margin: 0;
            padding: 40px;
            background: #06080f;
            color: #eceef6;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
          }
          h1 {
            font-size: 26px;
            margin: 0 0 10px 0;
            letter-spacing: -0.5px;
            text-align: center;
            background: linear-gradient(135deg, #22d3ee, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }
          .subtitle {
            text-align: center;
            font-size: 14px;
            color: #8d93ab;
            margin-bottom: 30px;
          }
          .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
            max-width: 1360px;
            margin: 0 auto;
          }
          .card {
            background: #0d111c;
            border: 1px solid #1e2438;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 12px 30px rgba(0,0,0,0.5);
          }
          .card-header {
            padding: 14px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 13px;
            font-weight: 600;
            border-bottom: 1px solid #1a2035;
          }
          .tag-before {
            background: rgba(239, 68, 68, 0.15);
            color: #ef4444;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-family: monospace;
          }
          .tag-after {
            background: rgba(34, 197, 94, 0.15);
            color: #22c55e;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-family: monospace;
          }
          img {
            width: 100%;
            height: auto;
            display: block;
          }
          .feature-list {
            padding: 16px 20px;
            background: #0a0d16;
            font-size: 12px;
            color: #94a3b8;
            line-height: 1.6;
          }
          .feature-list span {
            color: #22d3ee;
            font-weight: 600;
          }
        </style>
      </head>
      <body>
        <h1>ARCHITECT CARD — CYBERSECURITY ENGINEER TRANSFORMATION AUDIT</h1>
        <div class="subtitle">
          Identity Transformation • Canonical Male Hero Character Alignment • 100% Zero-Trust, IAM &amp; AI Focus
        </div>

        <div class="grid">
          <div class="card">
            <div class="card-header">
              <span>REFERENCE BASELINE</span>
              <span class="tag-before">BEFORE: Female Frontend Dev</span>
            </div>
            <img src="data:image/png;base64,${b1}" />
            <div class="feature-list">
              ❌ Female character from reference template<br/>
              ❌ Generic frontend headline: "Interfaces people remember"<br/>
              ❌ Generic web skills: "HTML, CSS, JavaScript, React"
            </div>
          </div>
          <div class="card">
            <div class="card-header">
              <span>SUBHAJIT KAR IDENTITY</span>
              <span class="tag-after">AFTER: Cybersecurity &amp; Identity Architect</span>
            </div>
            <img src="data:image/png;base64,${a1}" />
            <div class="feature-list">
              ✅ <span>Male Subhajit Kar</span> character matching approved Hero visual identity<br/>
              ✅ <span>"Security, Identity &amp; AI systems that scale"</span> headline<br/>
              ✅ <span>Cybersecurity, IAM/IGA, Automation &amp; AI</span> capability rows + custom icons
            </div>
          </div>
        </div>
      </body>
    </html>
  `;

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1440, height: 960 },
    deviceScaleFactor: 2
  });

  await page.setContent(html);
  await page.waitForTimeout(600);

  const outPath = path.join(QA_DIR, 'architect-before-after.png');
  await page.screenshot({ path: outPath, fullPage: true });
  console.log(`✅ Saved: ${outPath}`);

  await browser.close();
}

main().catch(console.error);
