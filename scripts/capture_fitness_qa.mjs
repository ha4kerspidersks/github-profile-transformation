import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');
const qaDir = path.resolve(root, 'qa');

async function renderSvgToPng(svgPath, pngPath, width = 600, height = 432, bgColor = '#0f172a') {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width, height },
    deviceScaleFactor: 2
  });

  const svgContent = fs.readFileSync(svgPath, 'utf-8');
  const html = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {
      margin: 0;
      padding: 0;
      background: ${bgColor};
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }
    svg {
      width: 100%;
      height: 100%;
    }
  </style>
</head>
<body>
  ${svgContent}
</body>
</html>`;

  await page.setContent(html);
  await page.waitForTimeout(400); // Allow SMIL / CSS initial frame to settle
  await page.screenshot({ path: pngPath });
  await browser.close();
  console.log(`📸 Rendered ${path.basename(svgPath)} -> ${path.basename(pngPath)}`);
}

async function main() {
  const scenes = [
    { svg: path.join(qaDir, 'fitness-football.svg'), png: path.join(qaDir, 'fitness-football.png'), bg: '#064e3b' },
    { svg: path.join(qaDir, 'fitness-badminton.svg'), png: path.join(qaDir, 'fitness-badminton.png'), bg: '#78350f' },
    { svg: path.join(qaDir, 'fitness-cooking.svg'), png: path.join(qaDir, 'fitness-cooking.png'), bg: '#4c1d95' },
  ];

  for (const s of scenes) {
    await renderSvgToPng(s.svg, s.png, 600, 432, s.bg);
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
