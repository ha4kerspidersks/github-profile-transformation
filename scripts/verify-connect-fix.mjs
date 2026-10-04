import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const PROJECT_ROOT = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const PREVIEW_DIR = path.join(PROJECT_ROOT, 'preview');

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1800 },
    deviceScaleFactor: 2,
    colorScheme: 'dark'
  });

  // Navigate to live preview server
  await page.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // Locate connect image
  const connectImg = page.locator('img[src*="connect.svg"]');

  // Scroll into view
  await connectImg.scrollIntoViewIfNeeded();
  await page.waitForTimeout(500);

  // Take screenshot of entire connect image
  const connectPngPath = path.join(PREVIEW_DIR, 'connect-after-fix.png');
  await connectImg.screenshot({ path: connectPngPath });
  console.log('Saved:', connectPngPath);

  // Take screenshot of the connect image with padding
  const boxInView = await connectImg.boundingBox();
  console.log('Connect bounding box in view:', boxInView);

  // 1. Top-Left Corner (where the stray mark used to be)
  const tlCropPath = path.join(PREVIEW_DIR, 'connect-tl-corner-after.png');
  await page.screenshot({
    path: tlCropPath,
    clip: {
      x: Math.round(boxInView.x),
      y: Math.round(boxInView.y),
      width: 80,
      height: 80
    }
  });
  console.log('Saved Top-Left Corner Crop:', tlCropPath);

  // 2. Top-Right Corner
  const trCropPath = path.join(PREVIEW_DIR, 'connect-tr-corner-after.png');
  await page.screenshot({
    path: trCropPath,
    clip: {
      x: Math.round(boxInView.x + boxInView.width - 80),
      y: Math.round(boxInView.y),
      width: 80,
      height: 80
    }
  });
  console.log('Saved Top-Right Corner Crop:', trCropPath);

  // 3. Bottom-Left Corner
  const blCropPath = path.join(PREVIEW_DIR, 'connect-bl-corner-after.png');
  await page.screenshot({
    path: blCropPath,
    clip: {
      x: Math.round(boxInView.x),
      y: Math.round(boxInView.y + boxInView.height - 80),
      width: 80,
      height: 80
    }
  });
  console.log('Saved Bottom-Left Corner Crop:', blCropPath);

  // 4. Bottom-Right Corner
  const brCropPath = path.join(PREVIEW_DIR, 'connect-br-corner-after.png');
  await page.screenshot({
    path: brCropPath,
    clip: {
      x: Math.round(boxInView.x + boxInView.width - 80),
      y: Math.round(boxInView.y + boxInView.height - 80),
      width: 80,
      height: 80
    }
  });
  console.log('Saved Bottom-Right Corner Crop:', brCropPath);

  // 5. GitHub Card Arrow Area (inside the card on the right)
  const ghArrowClip = {
    x: Math.round(boxInView.x + boxInView.width * (790 / 1280)),
    y: Math.round(boxInView.y + boxInView.height * (240 / 470)),
    width: 60,
    height: 50
  };
  const ghArrowPath = path.join(PREVIEW_DIR, 'connect-github-arrow-verified.png');
  await page.screenshot({ path: ghArrowPath, clip: ghArrowClip });
  console.log('Saved GitHub Card Arrow Verified:', ghArrowPath);

  // 6. Test Responsive Viewports (1920, 1600, 1440, 1280, 1024, 900, 768, 600)
  const viewports = [1920, 1600, 1440, 1280, 1024, 900, 768, 600];
  console.log('\n--- RESPONSIVE VIEWPORT CHECKS ---');
  for (const w of viewports) {
    await page.setViewportSize({ width: w, height: 1200 });
    await page.waitForTimeout(300);
    const b = await connectImg.boundingBox();
    console.log(`Viewport ${w}px: width=${b.width.toFixed(1)}px, height=${b.height.toFixed(1)}px, x=${b.x.toFixed(1)}, y=${b.y.toFixed(1)}`);
  }

  await browser.close();
  console.log('\n✅ Playwright verification completed successfully!');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
