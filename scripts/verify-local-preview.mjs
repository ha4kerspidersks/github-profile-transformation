import { chromium } from 'playwright';

async function verify() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 2 });
  const failedRequests = [];
  const consoleMessages = [];

  page.on('response', response => {
    if (!response.ok() && !response.url().includes('favicon.ico')) {
      failedRequests.push({ url: response.url(), status: response.status() });
    }
  });

  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleMessages.push(msg.text());
    }
  });

  console.log('Navigating to http://localhost:4114/preview/index.html...');
  await page.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
  
  // Scroll down progressively to allow all SVG entry animations to trigger and settle
  const scrollSteps = [500, 1200, 1900, 2600, 3400, 4200, 0];
  for (const y of scrollSteps) {
    await page.evaluate(top => window.scrollTo({ top, behavior: 'instant' }), y);
    await page.waitForTimeout(400);
  }
  await page.waitForTimeout(3000);

  const screenshotPath = '/Users/subhajkar/Developer/GitHub-Profile-Transformation/preview/live-preview-verification.png';
  await page.screenshot({ path: screenshotPath, fullPage: true });

  const dashboardImg = await page.locator('img[src*="id-dashboard.svg"]');
  const dashboardCount = await dashboardImg.count();
  const dashboardVisible = dashboardCount > 0 ? await dashboardImg.first().isVisible() : false;

  console.log(JSON.stringify({
    title: await page.title(),
    dashboardVisible,
    dashboardCount,
    failedRequests,
    consoleErrors: consoleMessages,
    screenshotSaved: screenshotPath
  }, null, 2));

  await browser.close();
}

verify().catch(console.error);
