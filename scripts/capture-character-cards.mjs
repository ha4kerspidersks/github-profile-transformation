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
        ${svgContent}
      </body>
    </html>
  `);

  // Wait for fonts and all entrance animations (row delays up to 1.36s + 0.7s duration = 2.06s)
  await page.waitForTimeout(2500);

  // Capture Architect Card (Left half: 0 to 640)
  await page.screenshot({
    path: path.join(QA_DIR, 'architect-card-after.png'),
    clip: { x: 0, y: 0, width: 640, height: 640 }
  });
  console.log('✅ Captured qa/architect-card-after.png');

  // Capture Fitness Card (Right half: 640 to 1280)
  await page.screenshot({
    path: path.join(QA_DIR, 'fitness-card-after.png'),
    clip: { x: 640, y: 0, width: 640, height: 640 }
  });
  console.log('✅ Captured qa/fitness-card-after.png');

  await browser.close();
}

main().catch(console.error);
