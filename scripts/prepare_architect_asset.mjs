import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const QA_DIR = path.resolve(process.cwd(), 'qa');
const SRC_IMAGE = '/Users/subhajkar/.gemini/antigravity-ide/brain/2fc54a86-6ca7-47e2-886b-55749f461968/architect_subhajit_cybersecurity_1791003078852.jpg';

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const imgBase64 = fs.readFileSync(SRC_IMAGE).toString('base64');

  await page.setContent(`
    <html><body style="margin:0;padding:0;">
      <canvas id="c"></canvas>
      <script>
        async function processImage(dataUri, threshold = 35) {
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
            } else if (dist < threshold + 16) {
              const alpha = (dist - threshold) / 16;
              d[p4+3] = Math.round(d[p4+3] * alpha);
            }
          }

          ctx.putImageData(imgData, 0, 0);

          // Find bounding box of visible pixels
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

          const cropW = maxX - minX + 1;
          const cropH = maxY - minY + 1;

          // Target canvas: 1080 x 608 (standard 16:9 matching 564x318 browser window)
          const targetW = 1080;
          const targetH = 608;
          const outCanvas = document.createElement('canvas');
          outCanvas.width = targetW;
          outCanvas.height = targetH;
          const outCtx = outCanvas.getContext('2d');

          // Scale and center character into 1080x608
          // Leave comfortable margins (padding ~ 24px)
          const availW = targetW - 48;
          const availH = targetH - 24;
          const scale = Math.min(availW / cropW, availH / cropH);

          const drawW = cropW * scale;
          const drawH = cropH * scale;
          const drawX = (targetW - drawW) / 2;
          const drawY = targetH - drawH; // Anchor near bottom of desk

          outCtx.drawImage(
            c,
            minX, minY, cropW, cropH,
            drawX, drawY, drawW, drawH
          );

          return {
            fullData: outCanvas.toDataURL('image/png'),
            webpData: outCanvas.toDataURL('image/webp', 0.92),
            bounds: { minX, maxX, minY, maxY, cropW, cropH, drawX, drawY, drawW, drawH }
          };
        }
        window.processImage = processImage;
      </script>
    </body></html>
  `);

  const res = await page.evaluate(async (uri) => {
    return await window.processImage('data:image/jpeg;base64,' + uri);
  }, imgBase64);

  // Write standalone transparent PNG for QA
  const base64Png = res.fullData.replace(/^data:image\/png;base64,/, '');
  fs.writeFileSync(path.join(QA_DIR, 'architect-subhajit.png'), Buffer.from(base64Png, 'base64'));

  // Save asset JSON
  fs.writeFileSync(
    path.join(QA_DIR, 'architect-asset.json'),
    JSON.stringify(res, null, 2)
  );

  console.log('✅ Created qa/architect-subhajit.png');
  console.log('   Bounds:', res.bounds);
  console.log('   WebP payload size:', Math.round(res.webpData.length / 1024), 'KB');

  await browser.close();
}

main().catch(console.error);
