import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const QA_DIR = path.resolve(process.cwd(), 'qa');

const rawAssets = [
  {
    id: 'football',
    name: 'fitness-football.png',
    bg: '#c6ecd9', // Slide 0 background
    src: '/Users/subhajkar/.gemini/antigravity-ide/brain/2fc54a86-6ca7-47e2-886b-55749f461968/fitness_subhajit_football_1790991674731.jpg'
  },
  {
    id: 'badminton',
    name: 'fitness-badminton.png',
    bg: '#fed7aa', // Slide 1 background
    src: '/Users/subhajkar/.gemini/antigravity-ide/brain/2fc54a86-6ca7-47e2-886b-55749f461968/fitness_subhajit_badminton_1790991742015.jpg'
  },
  {
    id: 'cooking',
    name: 'fitness-cooking.png',
    bg: '#e9d5ff', // Slide 2 background
    src: '/Users/subhajkar/.gemini/antigravity-ide/brain/2fc54a86-6ca7-47e2-886b-55749f461968/fitness_subhajit_cooking_1790991761419.jpg'
  }
];

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const results = {};

  for (const asset of rawAssets) {
    const imgBase64 = fs.readFileSync(asset.src).toString('base64');

    await page.setContent(`
      <html><body style="margin:0;padding:0;">
        <canvas id="c"></canvas>
        <script>
          async function processImage(dataUri, threshold = 48) {
            const img = new Image();
            img.src = dataUri;
            await new Promise(r => img.onload = r);

            const c = document.getElementById('c');
            c.width = img.width;
            c.height = img.height;
            const ctx = c.getContext('2d');
            ctx.drawImage(img, 0, 0);

            const imgData = ctx.getImageData(0, 0, c.width, c.height);
            const d = imgData.data;
            const w = c.width, h = c.height;

            // Sample background color from corners
            const samples = [
              0, 1, 2,
              (w - 1) * 4, (w - 1) * 4 + 1, (w - 1) * 4 + 2,
              (h - 1) * w * 4, (h - 1) * w * 4 + 1, (h - 1) * w * 4 + 2,
              (h * w - 1) * 4, (h * w - 1) * 4 + 1, (h * w - 1) * 4 + 2
            ];

            const bgR = (d[0] + d[(w-1)*4] + d[(h-1)*w*4] + d[(h*w-1)*4]) / 4;
            const bgG = (d[1] + d[(w-1)*4+1] + d[(h-1)*w*4+1] + d[(h*w-1)*4+1]) / 4;
            const bgB = (d[2] + d[(w-1)*4+2] + d[(h-1)*w*4+2] + d[(h*w-1)*4+2]) / 4;

            const visited = new Uint8Array(w * h);
            const queue = [];

            function push(x, y) {
              const idx = y * w + x;
              if (visited[idx]) return;
              visited[idx] = 1;
              queue.push(idx);
            }

            for (let x = 0; x < w; x++) { push(x, 0); push(x, h - 1); }
            for (let y = 0; y < h; y++) { push(0, y); push(w - 1, y); }

            let head = 0;
            while (head < queue.length) {
              const idx = queue[head++];
              const px = idx % w;
              const py = Math.floor(idx / w);
              const p4 = idx * 4;

              const r = d[p4], g = d[p4+1], b = d[p4+2];
              const dist = Math.sqrt((r - bgR)**2 + (g - bgG)**2 + (b - bgB)**2);

              if (dist < threshold) {
                d[p4+3] = 0; // Transparent
                if (px > 0) push(px - 1, py);
                if (px < w - 1) push(px + 1, py);
                if (py > 0) push(px, py - 1);
                if (py < h - 1) push(px, py + 1);
              } else if (dist < threshold + 18) {
                const alpha = (dist - threshold) / 18;
                d[p4+3] = Math.round(d[p4+3] * alpha);
              }
            }

            ctx.putImageData(imgData, 0, 0);

            // Bounding box crop calculation
            let minX = w, maxX = 0, minY = h, maxY = 0;
            for (let y = 0; y < h; y++) {
              for (let x = 0; x < w; x++) {
                const a = d[(y * w + x) * 4 + 3];
                if (a > 20) {
                  if (x < minX) minX = x;
                  if (x > maxX) maxX = x;
                  if (y < minY) minY = y;
                  if (y > maxY) maxY = y;
                }
              }
            }

            // Create target 888x624 canvas (2x of 444x312 viewport)
            const targetW = 888;
            const targetH = 624;
            const outCanvas = document.createElement('canvas');
            outCanvas.width = targetW;
            outCanvas.height = targetH;
            const outCtx = outCanvas.getContext('2d');

            const contentW = maxX - minX;
            const contentH = maxY - minY;
            const scale = Math.min((targetW * 0.90) / contentW, (targetH * 0.90) / contentH);

            const drawW = contentW * scale;
            const drawH = contentH * scale;
            const drawX = (targetW - drawW) / 2;
            const drawY = (targetH - drawH) / 2;

            outCtx.drawImage(c, minX, minY, contentW, contentH, drawX, drawY, drawW, drawH);

            return {
              transparentPng: outCanvas.toDataURL('image/png'),
              transparentWebp: outCanvas.toDataURL('image/webp', 0.88),
              width: targetW,
              height: targetH
            };
          }
          window.processImage = processImage;
        </script>
      </body></html>
    `);

    console.log(`Processing ${asset.id}...`);
    const processed = await page.evaluate(async (uri) => {
      return await window.processImage(`data:image/jpeg;base64,${uri}`);
    }, imgBase64);

    // Save individual QA PNG on its card background for visual inspection
    const cardCanvas = await page.evaluate(async ({ pngUri, bg, w, h }) => {
      const c = document.createElement('canvas');
      c.width = w;
      c.height = h;
      const ctx = c.getContext('2d');
      ctx.fillStyle = bg;
      ctx.fillRect(0, 0, w, h);

      const img = new Image();
      img.src = pngUri;
      await new Promise(r => img.onload = r);
      ctx.drawImage(img, 0, 0);
      return c.toDataURL('image/png');
    }, { pngUri: processed.transparentPng, bg: asset.bg, w: processed.width, h: processed.height });

    const rawPng = cardCanvas.replace(/^data:image\/png;base64,/, '');
    fs.writeFileSync(path.join(QA_DIR, asset.name), Buffer.from(rawPng, 'base64'));
    console.log(`✅ Saved ${path.join(QA_DIR, asset.name)}`);

    results[asset.id] = {
      webp: processed.transparentWebp,
      png: processed.transparentPng
    };
  }

  fs.writeFileSync(path.join(QA_DIR, 'fitness-assets.json'), JSON.stringify(results, null, 2));
  console.log('✅ Exported qa/fitness-assets.json');

  await browser.close();
}

main().catch(console.error);
