import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const ROOT = process.cwd();
const QA_DIR = path.join(ROOT, 'qa');

async function main() {
  const b1 = fs.readFileSync(path.join(QA_DIR, 'architect-card-before.png')).toString('base64');
  const a1 = fs.readFileSync(path.join(QA_DIR, 'architect-card-after.png')).toString('base64');
  const b2 = fs.readFileSync(path.join(QA_DIR, 'fitness-card-before.png')).toString('base64');
  const a2 = fs.readFileSync(path.join(QA_DIR, 'fitness-card-after.png')).toString('base64');

  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <style>
          body {
            margin: 0;
            padding: 32px;
            background: #090a10;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #ffffff;
          }
          h1 {
            text-align: center;
            font-size: 24px;
            margin-bottom: 24px;
            letter-spacing: 0.5px;
          }
          .section-title {
            font-size: 16px;
            color: #22d3ee;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin: 20px 0 10px 0;
          }
          .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            margin-bottom: 32px;
          }
          .card {
            background: #111420;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
          }
          .card-header {
            padding: 12px 18px;
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 1px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255,255,255,0.06);
          }
          .tag-before {
            background: rgba(244, 63, 94, 0.15);
            color: #f43f5e;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
          }
          .tag-after {
            background: rgba(34, 197, 94, 0.15);
            color: #22c55e;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
          }
          img {
            width: 100%;
            height: auto;
            display: block;
          }
        </style>
      </head>
      <body>
        <h1>CHARACTER ARTWORK REPLACEMENT — VISUAL AUDIT</h1>

        <div class="section-title">Target Card 1: // ARCHITECT (Desk Character)</div>
        <div class="grid">
          <div class="card">
            <div class="card-header">
              <span>REFERENCE ORIGINAL</span>
              <span class="tag-before">BEFORE (Female Reference)</span>
            </div>
            <img src="data:image/png;base64,${b1}" />
          </div>
          <div class="card">
            <div class="card-header">
              <span>SUBHAJIT KAR TRANSFORMED</span>
              <span class="tag-after">AFTER (Male Architect)</span>
            </div>
            <img src="data:image/png;base64,${a1}" />
          </div>
        </div>

        <div class="section-title">Target Card 2: // OFF THE CLOCK (Slide 0 Runner)</div>
        <div class="grid">
          <div class="card">
            <div class="card-header">
              <span>REFERENCE ORIGINAL</span>
              <span class="tag-before">BEFORE (Female Runner w/ Ponytail)</span>
            </div>
            <img src="data:image/png;base64,${b2}" />
          </div>
          <div class="card">
            <div class="card-header">
              <span>SUBHAJIT KAR TRANSFORMED</span>
              <span class="tag-after">AFTER (Male Runner, Zero Ponytail)</span>
            </div>
            <img src="data:image/png;base64,${a2}" />
          </div>
        </div>
      </body>
    </html>
  `;

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1400, height: 1650 },
    deviceScaleFactor: 2
  });

  await page.setContent(html);
  await page.waitForTimeout(500);

  const outPath = path.join(QA_DIR, 'character-replacement-comparison.png');
  await page.screenshot({ path: outPath, fullPage: true });
  console.log(`✅ Saved composite comparison to: ${outPath}`);

  await browser.close();
}

main().catch(console.error);
