import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const ROOT = process.cwd();
const SVG_PATH = path.join(ROOT, 'assets/about-life.svg');
const QA_DIR = path.join(ROOT, 'qa');

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1280, height: 640 },
    deviceScaleFactor: 2
  });

  const svgContent = fs.readFileSync(SVG_PATH, 'utf-8');

  // Helper to snap the fitness card with a specific active slide
  async function snapFitnessCard(activeSlideIndex, outPath) {
    let modifiedSvg = svgContent;
    if (activeSlideIndex === 0) {
      // Default: Slide 0 is already active
    } else if (activeSlideIndex === 1) {
      // Make Slide 1 and Cap 1 active
      modifiedSvg = modifiedSvg
        .replace('class="slide" opacity="1" style="animation-delay:0s"', 'class="slide" opacity="0" style="animation:none"')
        .replace('class="slide" opacity="0" style="animation-delay:4s"', 'class="slide" opacity="1" style="animation:none"')
        .replace('class="bgfade" opacity="1" style="animation-delay:0s"', 'class="bgfade" opacity="0" style="animation:none"')
        .replace('class="bgfade" opacity="0" style="animation-delay:4s"', 'class="bgfade" opacity="1" style="animation:none"')
        .replace('class="cap" opacity="1" style="animation-delay:0s"', 'class="cap" opacity="0" style="animation:none"')
        .replace('class="cap" opacity="0" style="animation-delay:4s"', 'class="cap" opacity="1" style="animation:none"');
    } else if (activeSlideIndex === 2) {
      // Make Slide 2 and Cap 2 active
      modifiedSvg = modifiedSvg
        .replace('class="slide" opacity="1" style="animation-delay:0s"', 'class="slide" opacity="0" style="animation:none"')
        .replace('class="slide" opacity="0" style="animation-delay:8s"', 'class="slide" opacity="1" style="animation:none"')
        .replace('class="bgfade" opacity="1" style="animation-delay:0s"', 'class="bgfade" opacity="0" style="animation:none"')
        .replace('class="bgfade" opacity="0" style="animation-delay:8s"', 'class="bgfade" opacity="1" style="animation:none"')
        .replace('class="cap" opacity="1" style="animation-delay:0s"', 'class="cap" opacity="0" style="animation:none"')
        .replace('class="cap" opacity="0" style="animation-delay:8s"', 'class="cap" opacity="1" style="animation:none"');
    }

    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <style>
            body, html { margin: 0; padding: 0; background: #0b0e14; overflow: hidden; }
            svg { display: block; width: 1280px; height: 640px; }
          </style>
        </head>
        <body>
          ${modifiedSvg}
        </body>
      </html>
    `);

    await page.waitForTimeout(600);

    await page.screenshot({
      path: outPath,
      clip: { x: 640, y: 0, width: 640, height: 640 }
    });
    console.log(`✅ Snapped ${path.basename(outPath)}`);
  }

  // 1. Capture complete final fitness card (Slide 0 active)
  await snapFitnessCard(0, path.join(QA_DIR, 'fitness-final.png'));
  await snapFitnessCard(1, path.join(QA_DIR, 'fitness-slide1-badminton.png'));
  await snapFitnessCard(2, path.join(QA_DIR, 'fitness-slide2-cooking.png'));

  // 2. Build high-resolution comparison: qa/fitness-before-after.png
  // Creates a clean, labeled 2x3 comparison grid:
  // Top row: BEFORE (1. Running Girl, 2. Skateboarding Girl, 3. Ramen Anime)
  // Bottom row: AFTER (1. ⚽ Male Football, 2. 🏸 Male Badminton, 3. 👨‍🍳 Male Cooking)
  const compPage = await browser.newPage({
    viewport: { width: 1800, height: 1240 },
    deviceScaleFactor: 2
  });

  const refS0 = fs.readFileSync(path.join(QA_DIR, 'fitness-card-before.png')).toString('base64');
  const refS1 = fs.readFileSync(path.join(QA_DIR, 'ref-fitness-slide1.png')).toString('base64');
  const refS2 = fs.readFileSync(path.join(QA_DIR, 'ref-fitness-slide2.png')).toString('base64');

  const afterS0 = fs.readFileSync(path.join(QA_DIR, 'fitness-final.png')).toString('base64');
  const afterS1 = fs.readFileSync(path.join(QA_DIR, 'fitness-slide1-badminton.png')).toString('base64');
  const afterS2 = fs.readFileSync(path.join(QA_DIR, 'fitness-slide2-cooking.png')).toString('base64');

  await compPage.setContent(`
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        * { box-sizing: border-box; }
        body {
          margin: 0;
          padding: 40px;
          background: #07090e;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          color: #f1f5f9;
        }
        .header {
          text-align: center;
          margin-bottom: 30px;
        }
        h1 {
          font-size: 28px;
          font-weight: 800;
          margin: 0 0 8px 0;
          letter-spacing: -0.5px;
          background: linear-gradient(135deg, #38bdf8, #818cf8, #c084fc);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
        p {
          color: #94a3b8;
          font-size: 15px;
          margin: 0;
        }
        .section-title {
          font-size: 18px;
          font-weight: 700;
          margin: 25px 0 15px 0;
          display: flex;
          align-items: center;
          gap: 10px;
        }
        .badge-before {
          background: rgba(239, 68, 68, 0.15);
          color: #f87171;
          border: 1px solid rgba(239, 68, 68, 0.35);
          padding: 3px 10px;
          border-radius: 6px;
          font-size: 12px;
          font-weight: 700;
          letter-spacing: 1px;
        }
        .badge-after {
          background: rgba(34, 197, 94, 0.15);
          color: #4ade80;
          border: 1px solid rgba(34, 197, 94, 0.35);
          padding: 3px 10px;
          border-radius: 6px;
          font-size: 12px;
          font-weight: 700;
          letter-spacing: 1px;
        }
        .grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 20px;
        }
        .card {
          background: #0f172a;
          border-radius: 18px;
          border: 1px solid rgba(255, 255, 255, 0.08);
          overflow: hidden;
          box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        }
        .card img {
          width: 100%;
          display: block;
        }
        .card-meta {
          padding: 12px 16px;
          background: #0b1120;
          border-top: 1px solid rgba(255, 255, 255, 0.06);
          font-size: 13px;
          font-weight: 600;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        .pill-old { color: #f87171; font-family: monospace; }
        .pill-new { color: #38bdf8; font-family: monospace; }
      </style>
    </head>
    <body>
      <div class="header">
        <h1>FITNESS CARD — BEFORE vs AFTER TRANSFORMATION AUDIT</h1>
        <p>100% Male Subhajit Kar Illustrations • 3-Stage Rotation: ⚽ Football → 🏸 Badminton → 👨‍🍳 Cooking</p>
      </div>

      <div class="section-title">
        <span class="badge-before">BEFORE</span>
        <span>Reference Assets (Female Characters &amp; Anime)</span>
      </div>
      <div class="grid">
        <div class="card">
          <img src="data:image/png;base64,${refS0}" />
          <div class="card-meta"><span>Slide 1: Female Runner</span><span class="pill-old">REPLACED</span></div>
        </div>
        <div class="card">
          <img src="data:image/png;base64,${refS1}" />
          <div class="card-meta"><span>Slide 2: Female Skateboarder</span><span class="pill-old">REPLACED</span></div>
        </div>
        <div class="card">
          <img src="data:image/png;base64,${refS2}" />
          <div class="card-meta"><span>Slide 3: Naruto Anime Ramen</span><span class="pill-old">REPLACED</span></div>
        </div>
      </div>

      <div class="section-title">
        <span class="badge-after">AFTER</span>
        <span>Pristine Male Subhajit Kar Illustrations (Identical Identity Family)</span>
      </div>
      <div class="grid">
        <div class="card">
          <img src="data:image/png;base64,${afterS0}" />
          <div class="card-meta"><span>Slide 1: ⚽ Male Football Player</span><span class="pill-new">FOOTBALL</span></div>
        </div>
        <div class="card">
          <img src="data:image/png;base64,${afterS1}" />
          <div class="card-meta"><span>Slide 2: 🏸 Male Badminton Player</span><span class="pill-new">BADMINTON</span></div>
        </div>
        <div class="card">
          <img src="data:image/png;base64,${afterS2}" />
          <div class="card-meta"><span>Slide 3: 👨‍🍳 Male Lifestyle Chef</span><span class="pill-new">COOKING</span></div>
        </div>
      </div>
    </body>
    </html>
  `);

  await compPage.screenshot({
    path: path.join(QA_DIR, 'fitness-before-after.png')
  });
  console.log('✅ Generated qa/fitness-before-after.png');

  await browser.close();
}

main().catch(console.error);
