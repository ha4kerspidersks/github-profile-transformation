import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

async function cropPhoto() {
  const inputPath = path.resolve('assets/avatar/male-character-portrait.jpg');
  const inputBase64 = fs.readFileSync(inputPath).toString('base64');
  const inputDataUrl = `data:image/jpeg;base64,${inputBase64}`;

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 400, height: 500 } });

  // 136 x 168 at 2x = 272 x 336
  const W = 272;
  const H = 336;

  const html = `
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      body { margin: 0; padding: 0; background: #0d0e16; overflow: hidden; }
      #cropBox {
        position: relative;
        width: ${W}px;
        height: ${H}px;
        overflow: hidden;
      }
      #img {
        position: absolute;
        width: 272px;
        height: auto;
        top: -10px;
        left: 0;
        object-fit: cover;
      }
    </style>
  </head>
  <body>
    <div id="cropBox">
      <img id="img" src="${inputDataUrl}" />
    </div>
  </body>
  </html>
  `;

  await page.setContent(html);
  const cropBox = await page.$('#cropBox');
  const outputPath = path.resolve('assets/avatar/icard-cropped.jpg');
  await cropBox.screenshot({ path: outputPath, type: 'jpeg', quality: 95 });
  await browser.close();

  const outSize = fs.statSync(outputPath).size;
  console.log(`✅ Cropped icard photo saved to ${outputPath} (${(outSize / 1024).toFixed(1)} KB)`);
}

cropPhoto().catch(err => {
  console.error('Error cropping photo:', err);
  process.exit(1);
});
