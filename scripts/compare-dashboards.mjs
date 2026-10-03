import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const ROOT_DIR = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const REF_SVG_PATH = path.join(ROOT_DIR, 'reference-base/id-dashboard.svg');
const GEN_SVG_PATH = path.join(ROOT_DIR, 'assets/id-dashboard.svg');
const COMP_DIR = path.join(ROOT_DIR, 'preview/comparison');

async function renderSVG(svgPath, outPngPath) {
  const svgContent = fs.readFileSync(svgPath, 'utf-8');
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1280, height: 600 },
    deviceScaleFactor: 2
  });

  const html = `
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      body { margin: 0; padding: 0; background: #0d1117; display: flex; justify-content: center; align-items: center; }
      svg { width: 1280px; height: 600px; display: block; }
    </style>
  </head>
  <body>
    ${svgContent}
  </body>
  </html>
  `;

  await page.setContent(html);
  // Wait for initial animation frame to stabilize
  await page.waitForTimeout(3000);
  await page.screenshot({ path: outPngPath });
  await browser.close();
  console.log(`Rendered ${svgPath} -> ${outPngPath}`);
}

async function main() {
  fs.mkdirSync(COMP_DIR, { recursive: true });

  const refPng = path.join(COMP_DIR, 'reference-dashboard.png');
  const genPng = path.join(COMP_DIR, 'generated-dashboard.png');

  console.log('Rendering reference dashboard...');
  await renderSVG(REF_SVG_PATH, refPng);

  console.log('Rendering generated dashboard...');
  await renderSVG(GEN_SVG_PATH, genPng);

  // Build HTML side-by-side and difference composite using browser canvas
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1280, height: 1300 },
    deviceScaleFactor: 2
  });

  const refB64 = fs.readFileSync(refPng).toString('base64');
  const genB64 = fs.readFileSync(genPng).toString('base64');

  const compHtml = `
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      body {
        margin: 0;
        padding: 30px;
        background: #0b0f19;
        color: #e2e8f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
      }
      h2 {
        margin: 0 0 16px 0;
        font-size: 20px;
        color: #38bdf8;
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .badge {
        font-size: 12px;
        padding: 4px 10px;
        border-radius: 6px;
        background: #1e293b;
        color: #a78bfa;
        font-weight: bold;
      }
      .container {
        display: flex;
        flex-direction: column;
        gap: 30px;
      }
      .card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 20px;
      }
      img {
        width: 100%;
        max-width: 1220px;
        height: auto;
        border-radius: 8px;
        border: 1px solid #374151;
        display: block;
      }
      .diff-canvas {
        width: 100%;
        max-width: 1220px;
        border-radius: 8px;
        border: 1px solid #374151;
        display: block;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="card">
        <h2>REFERENCE DASHBOARD <span class="badge">Meghamittal0920 Original Design</span></h2>
        <img src="data:image/png;base64,${refB64}" id="refImg" />
      </div>

      <div class="card">
        <h2>GENERATED DASHBOARD <span class="badge">Subhajit Kar (@ha4kerspidersks) with LinkedIn</span></h2>
        <img src="data:image/png;base64,${genB64}" id="genImg" />
      </div>

      <div class="card">
        <h2>VISUAL DIFFERENCE &amp; OVERLAY <span class="badge">Diff Highlights</span></h2>
        <canvas id="diffCanvas" class="diff-canvas"></canvas>
      </div>
    </div>

    <script>
      const refImg = document.getElementById('refImg');
      const genImg = document.getElementById('genImg');
      const canvas = document.getElementById('diffCanvas');

      function drawDiff() {
        canvas.width = refImg.naturalWidth;
        canvas.height = refImg.naturalHeight;
        const ctx = canvas.getContext('2d');

        // Draw reference image
        ctx.drawImage(refImg, 0, 0);
        const refData = ctx.getImageData(0, 0, canvas.width, canvas.height);

        // Draw generated image to temp canvas
        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = canvas.width;
        tempCanvas.height = canvas.height;
        const tempCtx = tempCanvas.getContext('2d');
        tempCtx.drawImage(genImg, 0, 0);
        const genData = tempCtx.getImageData(0, 0, canvas.width, canvas.height);

        const diffData = ctx.createImageData(canvas.width, canvas.height);
        for (let i = 0; i < refData.data.length; i += 4) {
          const dr = Math.abs(refData.data[i] - genData.data[i]);
          const dg = Math.abs(refData.data[i+1] - genData.data[i+1]);
          const db = Math.abs(refData.data[i+2] - genData.data[i+2]);
          const diff = (dr + dg + db) / 3;

          if (diff > 25) {
            // Highlight difference in vibrant magenta/cyan
            diffData.data[i] = 244;     // R
            diffData.data[i+1] = 114;   // G
            diffData.data[i+2] = 182;   // B
            diffData.data[i+3] = 255;   // A
          } else {
            // Identical background slightly dimmed
            diffData.data[i] = refData.data[i] * 0.2;
            diffData.data[i+1] = refData.data[i+1] * 0.2;
            diffData.data[i+2] = refData.data[i+2] * 0.2;
            diffData.data[i+3] = 255;
          }
        }
        ctx.putImageData(diffData, 0, 0);
      }

      window.addEventListener('load', () => {
        setTimeout(drawDiff, 500);
      });
    </script>
  </body>
  </html>
  `;

  await page.setContent(compHtml);
  await page.waitForTimeout(1500);

  const sideBySidePath = path.join(COMP_DIR, 'dashboard-side-by-side.png');
  await page.screenshot({ path: sideBySidePath, fullPage: true });
  console.log(`Saved composite comparison -> ${sideBySidePath}`);

  await browser.close();
}

main().catch(console.error);
