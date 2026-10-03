import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';

const ROOT_DIR = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const STACK_SVG_PATH = path.join(ROOT_DIR, 'assets', 'stack.svg');
const QA_DIR = path.join(ROOT_DIR, 'qa');

async function capture() {
  console.log('📸 Rendering Category Carousel assets/stack.svg in Playwright Chromium...');
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1400, height: 950 },
    deviceScaleFactor: 2,
    colorScheme: 'dark'
  });
  const page = await context.newPage();

  const svgContent = fs.readFileSync(STACK_SVG_PATH, 'utf-8');
  const htmlContent = `<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      margin: 0;
      padding: 40px;
      background: #0d1117;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    .svg-container {
      width: 1280px;
      max-width: 100%;
      box-shadow: 0 10px 40px rgba(0,0,0,0.6);
      border-radius: 24px;
      overflow: hidden;
    }
  </style>
</head>
<body>
  <div class="svg-container">
    ${svgContent}
  </div>
</body>
</html>`;

  await page.setContent(htmlContent);
  const container = await page.$('.svg-container');
  const target = container || page;

  // 1. Category 1: IAM at t=4.0s
  console.log('⏳ Capturing Category 1: IDENTITY & ACCESS GOVERNANCE (t=4.0s)...');
  await page.waitForTimeout(4000);
  await target.screenshot({ path: path.join(QA_DIR, 'carousel-cat-1-iam.png') });
  console.log('✅ Saved: carousel-cat-1-iam.png');

  // 2. Category 2: CLOUD at t=12.0s (+8.0s)
  console.log('⏳ Capturing Category 2: CLOUD & INFRASTRUCTURE (t=12.0s)...');
  await page.waitForTimeout(8000);
  await target.screenshot({ path: path.join(QA_DIR, 'carousel-cat-2-cloud.png') });
  console.log('✅ Saved: carousel-cat-2-cloud.png');

  // 3. Category 3: DEV at t=20.0s (+8.0s)
  console.log('⏳ Capturing Category 3: DEVELOPMENT & ARCHITECTURE (t=20.0s)...');
  await page.waitForTimeout(8000);
  await target.screenshot({ path: path.join(QA_DIR, 'carousel-cat-3-dev.png') });
  console.log('✅ Saved: carousel-cat-3-dev.png');

  // 4. Category 4: SEC at t=28.0s (+8.0s)
  console.log('⏳ Capturing Category 4: SECURITY & DEFENSE (t=28.0s)...');
  await page.waitForTimeout(8000);
  await target.screenshot({ path: path.join(QA_DIR, 'carousel-cat-4-sec.png') });
  console.log('✅ Saved: carousel-cat-4-sec.png');

  // 5. Category 5: DATA_AI at t=36.0s (+8.0s)
  console.log('⏳ Capturing Category 5: DATA, AI & ENTERPRISE (t=36.0s)...');
  await page.waitForTimeout(8000);
  await target.screenshot({ path: path.join(QA_DIR, 'carousel-cat-5-data-ai.png') });
  console.log('✅ Saved: carousel-cat-5-data-ai.png');

  await browser.close();
  console.log('🎉 All 5 Category Carousel frames captured successfully!');
}

capture().catch(err => {
  console.error('❌ Error during capture:', err);
  process.exit(1);
});
