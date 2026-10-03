import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const ROOT_DIR = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const PREVIEW_DIR = path.join(ROOT_DIR, 'preview');
const REF_DIR = path.join(PREVIEW_DIR, 'reference');
const CURR_DIR = path.join(PREVIEW_DIR, 'current');
const COMP_DIR = path.join(PREVIEW_DIR, 'comparison');
const QA_DIR = path.join(ROOT_DIR, 'qa');
const REPORTS_DIR = path.join(ROOT_DIR, 'reports');

fs.mkdirSync(REF_DIR, { recursive: true });
fs.mkdirSync(CURR_DIR, { recursive: true });
fs.mkdirSync(COMP_DIR, { recursive: true });
fs.mkdirSync(QA_DIR, { recursive: true });
fs.mkdirSync(REPORTS_DIR, { recursive: true });

async function runVisualComparison() {
  console.log('🚀 Starting Comprehensive Visual Comparison & Baseline Capture...');
  const browser = await chromium.launch();

  // 1. CAPTURE REFERENCE PROFILE (Meghamittal0920)
  console.log('📸 1/4: Capturing live Reference Profile (Meghamittal0920)...');
  const refContext = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1.5,
    colorScheme: 'dark'
  });
  const refPage = await refContext.newPage();
  
  try {
    await refPage.goto('https://github.com/Meghamittal0920', { waitUntil: 'networkidle', timeout: 30000 });
    await refPage.waitForTimeout(2500);

    // Full page desktop
    await refPage.screenshot({ path: path.join(REF_DIR, 'reference-desktop.png'), fullPage: true });

    // Target the README container
    const readmeElem = await refPage.$('article.markdown-body');
    if (readmeElem) {
      await readmeElem.screenshot({ path: path.join(COMP_DIR, 'reference.png') });
      console.log('✅ Captured reference README article to comparison/reference.png');
    } else {
      await refPage.screenshot({ path: path.join(COMP_DIR, 'reference.png') });
    }
  } catch (err) {
    console.warn('⚠️ Could not load remote reference profile, using cached fallback if available:', err.message);
  }

  // Reference Mobile
  const refMobileContext = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    colorScheme: 'dark'
  });
  const refMobilePage = await refMobileContext.newPage();
  try {
    await refMobilePage.goto('https://github.com/Meghamittal0920', { waitUntil: 'networkidle', timeout: 30000 });
    await refMobilePage.waitForTimeout(2000);
    await refMobilePage.screenshot({ path: path.join(REF_DIR, 'reference-mobile.png'), fullPage: true });
    console.log('✅ Captured reference mobile profile');
  } catch (err) {
    console.warn('⚠️ Could not capture reference mobile:', err.message);
  }

  // 2. CAPTURE CURRENT PROFILE (ha4kerspidersks)
  console.log('📸 2/4: Capturing live Current Profile (ha4kerspidersks)...');
  const currContext = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1.5,
    colorScheme: 'dark'
  });
  const currPage = await currContext.newPage();
  try {
    await currPage.goto('https://github.com/ha4kerspidersks', { waitUntil: 'networkidle', timeout: 30000 });
    await currPage.waitForTimeout(2000);
    await currPage.screenshot({ path: path.join(CURR_DIR, 'current-desktop.png'), fullPage: true });

    const currReadme = await currPage.$('article.markdown-body');
    if (currReadme) {
      await currReadme.screenshot({ path: path.join(CURR_DIR, 'current-readme.png') });
    }
    console.log('✅ Captured current live profile');
  } catch (err) {
    console.warn('⚠️ Could not load remote current profile:', err.message);
  }

  // 3. CAPTURE LOCAL GENERATED PREVIEW
  console.log('📸 3/4: Capturing Local Generated Preview (http://localhost:4114/preview/index.html)...');
  const localContext = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1.5,
    colorScheme: 'dark'
  });
  const localPage = await localContext.newPage();
  await localPage.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
  await localPage.waitForTimeout(2000);

  // Screenshot markdown-body
  const localReadme = await localPage.$('.markdown-body');
  if (localReadme) {
    await localReadme.screenshot({ path: path.join(COMP_DIR, 'generated.png') });
    console.log('✅ Captured generated README to comparison/generated.png');
  } else {
    await localPage.screenshot({ path: path.join(COMP_DIR, 'generated.png'), fullPage: true });
  }

  // Local Mobile
  const localMobileContext = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    colorScheme: 'dark'
  });
  const localMobilePage = await localMobileContext.newPage();
  await localMobilePage.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
  await localMobilePage.waitForTimeout(2000);
  await localMobilePage.screenshot({ path: path.join(COMP_DIR, 'generated-mobile.png'), fullPage: true });

  // 4. GENERATE COMPOSITE IMAGES (Side-by-Side, Overlay, Difference)
  console.log('🎨 4/4: Generating Side-by-Side, Overlay, and Difference composites...');
  const refImgPath = path.join(COMP_DIR, 'reference.png');
  const genImgPath = path.join(COMP_DIR, 'generated.png');

  if (fs.existsSync(refImgPath) && fs.existsSync(genImgPath)) {
    const compPage = await browser.newPage();
    const refB64 = fs.readFileSync(refImgPath).toString('base64');
    const genB64 = fs.readFileSync(genImgPath).toString('base64');

    const htmlComposite = `
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body { margin: 0; padding: 20px; background: #0d1117; font-family: -apple-system, sans-serif; color: #fff; }
        .row { display: flex; gap: 24px; align-items: flex-start; justify-content: center; }
        .col { display: flex; flex-direction: column; align-items: center; }
        .label { margin-bottom: 12px; font-size: 16px; font-weight: 600; padding: 6px 16px; border-radius: 6px; }
        .ref-label { background: #f472b6; color: #0d0e16; }
        .gen-label { background: #22d3ee; color: #0d0e16; }
        .img-card { border: 1px solid #30363d; border-radius: 8px; overflow: hidden; background: #0d0e16; }
        img { display: block; max-width: 600px; height: auto; }
      </style>
    </head>
    <body>
      <div id="sideBySide" class="row">
        <div class="col">
          <div class="label ref-label">REFERENCE PROFILE (Meghamittal0920)</div>
          <div class="img-card"><img src="data:image/png;base64,${refB64}" /></div>
        </div>
        <div class="col">
          <div class="label gen-label">REBUILT MALE IDENTITY (Subhajit Kar)</div>
          <div class="img-card"><img src="data:image/png;base64,${genB64}" /></div>
        </div>
      </div>
    </body>
    </html>
    `;

    await compPage.setContent(htmlComposite);
    await compPage.waitForTimeout(1000);
    const sideBySideElem = await compPage.$('#sideBySide');
    await sideBySideElem.screenshot({ path: path.join(COMP_DIR, 'side-by-side.png') });
    console.log('✅ Generated preview/comparison/side-by-side.png');

    // Create Difference & Overlay using Canvas
    const diffHtml = `
    <!DOCTYPE html>
    <html>
    <body>
      <canvas id="c"></canvas>
      <script>
        async function run() {
          const img1 = new Image();
          const img2 = new Image();
          await Promise.all([
            new Promise(r => { img1.onload = r; img1.src = 'data:image/png;base64,${refB64}'; }),
            new Promise(r => { img2.onload = r; img2.src = 'data:image/png;base64,${genB64}'; })
          ]);
          
          const W = Math.max(img1.width, img2.width);
          const H = Math.max(img1.height, img2.height);
          const c = document.getElementById('c');
          c.width = W; c.height = H;
          const ctx = c.getContext('2d');

          // Draw Difference
          ctx.drawImage(img1, 0, 0);
          ctx.globalCompositeOperation = 'difference';
          ctx.drawImage(img2, 0, 0);
        }
        window.ready = run();
      </script>
    </body>
    </html>
    `;
    await compPage.setContent(diffHtml);
    await compPage.evaluate(() => window.ready);
    await compPage.waitForTimeout(500);
    const canvasElem = await compPage.$('#c');
    await canvasElem.screenshot({ path: path.join(COMP_DIR, 'difference.png') });
    console.log('✅ Generated preview/comparison/difference.png');

    // Overlay 50%
    const overlayHtml = `
    <!DOCTYPE html>
    <html>
    <body>
      <canvas id="c"></canvas>
      <script>
        async function run() {
          const img1 = new Image();
          const img2 = new Image();
          await Promise.all([
            new Promise(r => { img1.onload = r; img1.src = 'data:image/png;base64,${refB64}'; }),
            new Promise(r => { img2.onload = r; img2.src = 'data:image/png;base64,${genB64}'; })
          ]);
          const W = Math.max(img1.width, img2.width);
          const H = Math.max(img1.height, img2.height);
          const c = document.getElementById('c');
          c.width = W; c.height = H;
          const ctx = c.getContext('2d');
          ctx.drawImage(img1, 0, 0);
          ctx.globalAlpha = 0.5;
          ctx.drawImage(img2, 0, 0);
        }
        window.ready = run();
      </script>
    </body>
    </html>
    `;
    await compPage.setContent(overlayHtml);
    await compPage.evaluate(() => window.ready);
    await compPage.waitForTimeout(500);
    const overlayCanvas = await compPage.$('#c');
    await overlayCanvas.screenshot({ path: path.join(COMP_DIR, 'overlay.png') });
    console.log('✅ Generated preview/comparison/overlay.png');

    // Copy to qa/ directory
    fs.copyFileSync(path.join(COMP_DIR, 'reference.png'), path.join(QA_DIR, 'reference.png'));
    fs.copyFileSync(path.join(COMP_DIR, 'generated.png'), path.join(QA_DIR, 'transformed.png'));
    fs.copyFileSync(path.join(COMP_DIR, 'side-by-side.png'), path.join(QA_DIR, 'side-by-side.png'));
    fs.copyFileSync(path.join(COMP_DIR, 'overlay.png'), path.join(QA_DIR, 'overlay.png'));
    fs.copyFileSync(path.join(COMP_DIR, 'difference.png'), path.join(QA_DIR, 'difference.png'));
    console.log('✅ Synchronized all comparison artifacts to qa/ directory');
  }

  await browser.close();
  console.log('🎉 Visual comparison and screenshot capture completed successfully!');
}

runVisualComparison().catch(err => {
  console.error('❌ Error running visual comparison:', err);
  process.exit(1);
});
