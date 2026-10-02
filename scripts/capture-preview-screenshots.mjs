import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import http from 'http';
import fs from 'fs';
import path from 'path';

const PROJECT_ROOT = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const PREVIEW_DIR = path.join(PROJECT_ROOT, 'preview');
const ASSETS_DIR = path.join(PROJECT_ROOT, 'assets');
const QA_DIR = path.join(PROJECT_ROOT, 'qa');

// Simple static server for preview
const server = http.createServer((req, res) => {
  let reqPath = req.url.split('?')[0];
  let filePath = path.join(PROJECT_ROOT, reqPath);
  
  if (reqPath === '/' || reqPath === '/preview' || reqPath === '/preview/') {
    filePath = path.join(PREVIEW_DIR, 'index.html');
  }

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath);
    let contentType = 'text/plain';
    if (ext === '.html') contentType = 'text/html';
    else if (ext === '.css') contentType = 'text/css';
    else if (ext === '.svg') contentType = 'image/svg+xml';
    else if (ext === '.png') contentType = 'image/png';
    else if (ext === '.js') contentType = 'application/javascript';

    res.writeHead(200, { 'Content-Type': contentType });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(4114, async () => {
  console.log('Static preview server listening on port 4114');

  const browser = await chromium.launch();
  try {
    // 1. Desktop Dark Mode (1280x800)
    const contextDark = await browser.newContext({
      viewport: { width: 1280, height: 800 },
      deviceScaleFactor: 2,
      colorScheme: 'dark'
    });
    const pageDark = await contextDark.newPage();
    await pageDark.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
    await pageDark.waitForTimeout(1000);

    const darkDesktopPath = path.join(PREVIEW_DIR, 'preview-dark-desktop.png');
    await pageDark.screenshot({ path: darkDesktopPath, fullPage: true });
    console.log('Saved:', darkDesktopPath);

    // Run Axe Accessibility Scan on Desktop Dark
    const axeResults = await new AxeBuilder({ page: pageDark }).analyze();
    const a11yReportPath = path.join(QA_DIR, 'accessibility-report.json');
    fs.writeFileSync(a11yReportPath, JSON.stringify({
      violations: axeResults.violations.length,
      details: axeResults.violations
    }, null, 2));
    console.log(`A11y Violations: ${axeResults.violations.length}`);

    // 2. Mobile Dark Mode (390x844 - iPhone 14 / modern smartphone)
    const contextMobile = await browser.newContext({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
      isMobile: true,
      hasTouch: true,
      colorScheme: 'dark'
    });
    const pageMobile = await contextMobile.newPage();
    await pageMobile.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
    await pageMobile.waitForTimeout(1000);

    const darkMobilePath = path.join(PREVIEW_DIR, 'preview-dark-mobile.png');
    await pageMobile.screenshot({ path: darkMobilePath, fullPage: true });
    console.log('Saved:', darkMobilePath);

    // 3. Desktop Light Mode
    const contextLight = await browser.newContext({
      viewport: { width: 1280, height: 800 },
      deviceScaleFactor: 2,
      colorScheme: 'light'
    });
    const pageLight = await contextLight.newPage();
    await pageLight.goto('http://localhost:4114/preview/index.html', { waitUntil: 'networkidle' });
    await pageLight.waitForTimeout(500);

    // Toggle to Light mode in UI if toggle exists
    const toggleBtn = await pageLight.$('.theme-toggle-btn');
    if (toggleBtn) {
      await toggleBtn.click();
      await pageLight.waitForTimeout(500);
    }

    const lightDesktopPath = path.join(PREVIEW_DIR, 'preview-light-desktop.png');
    await pageLight.screenshot({ path: lightDesktopPath, fullPage: true });
    console.log('Saved:', lightDesktopPath);

  } catch (err) {
    console.error('Screenshot error:', err);
  } finally {
    await browser.close();
    server.close();
    console.log('Verification & screenshot capture complete.');
  }
});
