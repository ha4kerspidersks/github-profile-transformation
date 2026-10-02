import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const QA_DIR = '/Users/subhajkar/Developer/GitHub-Profile-Transformation/qa';
const PROFILE_URL = 'https://github.com/ha4kerspidersks';

async function verifyLive() {
  console.log('Navigating to live GitHub profile:', PROFILE_URL);
  const browser = await chromium.launch();
  
  try {
    // 1. Desktop Dark Mode
    const contextDark = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      deviceScaleFactor: 2,
      colorScheme: 'dark'
    });
    const pageDark = await contextDark.newPage();
    
    const errors = [];
    pageDark.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    pageDark.on('pageerror', err => errors.push(err.message));

    const response = await pageDark.goto(PROFILE_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
    console.log(`HTTP Status: ${response.status()}`);
    await pageDark.waitForSelector('article.markdown-body', { timeout: 15000 }).catch(() => console.log('Selector timeout or not present'));
    await pageDark.waitForTimeout(3000);

    // Check if README exists on page
    const readmeExists = await pageDark.evaluate(() => {
      const readme = document.querySelector('article.markdown-body');
      return !!readme;
    });
    console.log('README rendered on live profile:', readmeExists);

    // Inspect all images in the README
    const imagesInfo = await pageDark.evaluate(() => {
      const imgs = Array.from(document.querySelectorAll('article.markdown-body img'));
      return imgs.map(img => ({
        src: img.src,
        alt: img.alt,
        complete: img.complete,
        naturalWidth: img.naturalWidth,
        naturalHeight: img.naturalHeight,
        broken: img.naturalWidth === 0
      }));
    });
    console.log('Images in README:', JSON.stringify(imagesInfo, null, 2));

    const desktopScreenshotPath = path.join(QA_DIR, 'live-github-profile-desktop-dark.png');
    await pageDark.screenshot({ path: desktopScreenshotPath, fullPage: true });
    console.log('Saved:', desktopScreenshotPath);

    // 2. Mobile Dark Mode (iPhone 14 / 390px)
    const contextMobile = await browser.newContext({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
      isMobile: true,
      hasTouch: true,
      colorScheme: 'dark'
    });
    const pageMobile = await contextMobile.newPage();
    await pageMobile.goto(PROFILE_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await pageMobile.waitForSelector('article.markdown-body', { timeout: 15000 }).catch(() => console.log('Mobile selector timeout'));
    await pageMobile.waitForTimeout(2000);

    const mobileScreenshotPath = path.join(QA_DIR, 'live-github-profile-mobile-dark.png');
    await pageMobile.screenshot({ path: mobileScreenshotPath, fullPage: true });
    console.log('Saved:', mobileScreenshotPath);

    const liveAuditResults = {
      timestamp: new Date().toISOString(),
      url: PROFILE_URL,
      httpStatus: response.status(),
      readmeRendered: readmeExists,
      imagesTotal: imagesInfo.length,
      brokenImages: imagesInfo.filter(i => i.broken).length,
      images: imagesInfo,
      consoleErrors: errors
    };

    fs.writeFileSync(path.join(QA_DIR, 'live-profile-audit.json'), JSON.stringify(liveAuditResults, null, 2));
    console.log('Live audit results written to live-profile-audit.json');

  } catch (err) {
    console.error('Error during live verification:', err);
  } finally {
    await browser.close();
  }
}

verifyLive();
