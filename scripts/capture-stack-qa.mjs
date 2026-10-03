import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';

const ROOT_DIR = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const STACK_SVG_PATH = path.join(ROOT_DIR, 'assets', 'stack.svg');
const QA_DIR = path.join(ROOT_DIR, 'qa');

async function capture() {
  console.log('📸 Rendering assets/stack.svg in Playwright Chromium...');
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1400, height: 950 },
    deviceScaleFactor: 2,
    colorScheme: 'dark'
  });
  const page = await context.newPage();

  // Create an HTML wrapper with dark background to view the SVG cleanly
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
  
  // Wait for initial fade-ins and capture t=3.5s
  console.log('⏳ Capturing t=3.5s snapshot...');
  await page.waitForTimeout(3500);

  const container = await page.$('.svg-container');
  const target = container || page;

  await target.screenshot({ path: path.join(QA_DIR, 'tech-stack-after.png') });
  console.log(`✅ Saved high-res screenshot to: ${path.join(QA_DIR, 'tech-stack-after.png')}`);

  // Capture at t=6.5s (+3.0s)
  console.log('⏳ Capturing t=6.5s snapshot...');
  await page.waitForTimeout(3000);
  await target.screenshot({ path: path.join(QA_DIR, 'tech-stack-frame-t6.png') });
  console.log(`✅ Saved frame at t=6.5s to: ${path.join(QA_DIR, 'tech-stack-frame-t6.png')}`);

  // Capture at t=12.5s (+6.0s)
  console.log('⏳ Capturing t=12.5s snapshot...');
  await page.waitForTimeout(6000);
  await target.screenshot({ path: path.join(QA_DIR, 'tech-stack-frame-t12.png') });
  console.log(`✅ Saved frame at t=12.5s to: ${path.join(QA_DIR, 'tech-stack-frame-t12.png')}`);

  // Capture at t=18.5s (+6.0s)
  console.log('⏳ Capturing t=18.5s snapshot...');
  await page.waitForTimeout(6000);
  await target.screenshot({ path: path.join(QA_DIR, 'tech-stack-frame-t18.png') });
  console.log(`✅ Saved frame at t=18.5s to: ${path.join(QA_DIR, 'tech-stack-frame-t18.png')}`);

  await browser.close();
}

capture().catch(err => {
  console.error('❌ Error during capture:', err);
  process.exit(1);
});
