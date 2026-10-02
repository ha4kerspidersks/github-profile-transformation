import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

async function generateAvatar() {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 600, height: 600 },
    deviceScaleFactor: 2
  });

  const imagePath = path.join(rootDir, 'assets/profile/subhajit-kar-profile-cartoon.png');
  const imageBase64 = fs.readFileSync(imagePath).toString('base64');
  const imageSrc = `data:image/png;base64,${imageBase64}`;

  const html = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      width: 600px;
      height: 600px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: transparent;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    .avatar-wrapper {
      position: relative;
      width: 440px;
      height: 440px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* Ambient Outer Glow Layer */
    .glow-aura {
      position: absolute;
      width: 410px;
      height: 410px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 242, 254, 0.28) 0%, rgba(59, 130, 246, 0.22) 40%, rgba(99, 102, 241, 0.12) 65%, transparent 75%);
      filter: blur(22px);
      z-index: 1;
    }

    /* 3D Drop Shadow Ring */
    .shadow-ring {
      position: absolute;
      width: 400px;
      height: 400px;
      border-radius: 50%;
      background: #000000;
      top: 24px;
      filter: blur(18px);
      opacity: 0.65;
      z-index: 2;
    }

    /* Outer Cyber Gradient Ring (Portfolio Signature: Cyan -> Blue -> Indigo -> Violet) */
    .outer-cyber-ring {
      position: relative;
      width: 400px;
      height: 400px;
      border-radius: 50%;
      padding: 6px;
      background: conic-gradient(
        from 210deg,
        #00F2FE 0deg,
        #3B82F6 90deg,
        #6366F1 180deg,
        #A855F7 250deg,
        #00F2FE 360deg
      );
      box-shadow: 
        0 14px 34px rgba(0, 0, 0, 0.7),
        0 0 24px rgba(0, 242, 254, 0.35),
        inset 0 0 12px rgba(0, 242, 254, 0.2);
      z-index: 3;
    }

    /* Top Specular Rim Reflection */
    .specular-rim {
      position: absolute;
      top: 6px;
      left: 15%;
      width: 70%;
      height: 3px;
      border-radius: 50%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.85), transparent);
      z-index: 6;
      filter: blur(0.5px);
    }

    /* Inner Dark Bezel / Extruded Trench */
    .inner-bezel {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      padding: 8px;
      background: radial-gradient(circle at 35% 25%, #182234 0%, #0c121e 60%, #030712 100%);
      box-shadow: 
        inset 0 4px 12px rgba(0, 0, 0, 0.95),
        0 0 0 2px rgba(0, 242, 254, 0.25);
      position: relative;
    }

    /* Image Clip Container */
    .image-container {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      overflow: hidden;
      position: relative;
      background: #030712;
      border: 3px solid rgba(255, 255, 255, 0.12);
      box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.8);
    }

    .image-container img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transform: scale(1.02);
    }

    /* Status Pill Badge at Bottom Center */
    .status-badge {
      position: absolute;
      bottom: -6px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(3, 7, 18, 0.94);
      border: 1.5px solid rgba(0, 242, 254, 0.6);
      box-shadow: 
        0 6px 18px rgba(0, 0, 0, 0.8),
        0 0 14px rgba(0, 242, 254, 0.35);
      backdrop-filter: blur(12px);
      padding: 6px 16px;
      border-radius: 9999px;
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 10;
      white-space: nowrap;
    }

    .status-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #10B981;
      box-shadow: 0 0 8px #10B981, 0 0 14px #10B981;
    }

    .status-text {
      color: #00F2FE;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 1.2px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <div class="avatar-wrapper">
    <div class="glow-aura"></div>
    <div class="shadow-ring"></div>
    <div class="outer-cyber-ring">
      <div class="specular-rim"></div>
      <div class="inner-bezel">
        <div class="image-container">
          <img src="${imageSrc}" alt="Subhajit Kar" />
        </div>
      </div>
    </div>
    <div class="status-badge">
      <div class="status-dot"></div>
      <span class="status-text">CLEARANCE: DELOITTE AM</span>
    </div>
  </div>
</body>
</html>
  `;

  await page.setContent(html);
  await page.waitForTimeout(300);

  const outputPath1 = path.join(rootDir, 'assets/profile/subhajit-kar-avatar.png');
  const outputPath2 = path.join(rootDir, 'profile-repo/assets/profile/subhajit-kar-avatar.png');

  const element = await page.$('.avatar-wrapper');
  await element.screenshot({
    path: outputPath1,
    omitBackground: true
  });

  fs.copyFileSync(outputPath1, outputPath2);
  console.log('✅ Generated 3D framed avatar PNG at:', outputPath1);

  await browser.close();
}

generateAvatar().catch(err => {
  console.error(err);
  process.exit(1);
});
