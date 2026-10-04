import { chromium } from 'playwright';

async function testResponsive() {
  const browser = await chromium.launch();
  const viewports = [1920, 1600, 1440, 1280, 1024, 900, 768, 600];
  const results = [];

  for (const width of viewports) {
    const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 2 });
    await page.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
    await page.waitForTimeout(600);

    const heroImg = await page.locator('img[src*="hero.svg"]').first();
    const box = await heroImg.boundingBox();

    if (width === 1280 || width === 768 || width === 600) {
      await page.screenshot({
        path: `preview/hero-focus-${width}px.png`,
        clip: box ? { x: Math.max(0, box.x - 10), y: Math.max(0, box.y - 10), width: box.width + 20, height: box.height + 20 } : undefined
      });
    }

    results.push({
      viewportWidth: width,
      heroBox: box,
      heroVisible: await heroImg.isVisible()
    });
    await page.close();
  }

  console.log(JSON.stringify(results, null, 2));
  await browser.close();
}

testResponsive().catch(console.error);
