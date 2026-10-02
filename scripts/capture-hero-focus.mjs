import { chromium } from 'playwright';
import http from 'http';
import fs from 'fs';
import path from 'path';

const PROJECT_ROOT = '/Users/subhajkar/Developer/GitHub-Profile-Transformation';
const PREVIEW_DIR = path.join(PROJECT_ROOT, 'preview');

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

server.listen(4115, async () => {
  const browser = await chromium.launch();
  try {
    const context = await browser.newContext({
      viewport: { width: 1200, height: 1000 },
      deviceScaleFactor: 2,
      colorScheme: 'dark'
    });
    const page = await context.newPage();
    await page.goto('http://localhost:4115/preview/index.html', { waitUntil: 'networkidle' });
    await page.waitForTimeout(600);

    const container = await page.$('.github-container');
    if (container) {
      const box = await container.boundingBox();
      await page.screenshot({
        path: '/Users/subhajkar/.gemini/antigravity-ide/brain/45d10e8f-c39d-442b-8041-1f8ec53b597e/preview-hero-focus-dark.png',
        clip: { x: box.x, y: box.y, width: box.width, height: 860 }
      });
      console.log('Saved focused hero screenshot successfully');
    }
  } finally {
    await browser.close();
    server.close();
  }
});
