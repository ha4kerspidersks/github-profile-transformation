import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const TOTAL_FRAMES = 30;
const DURATION = 4.0;
const WIDTH = 560;
const HEIGHT = 418;

const characterPath = path.resolve('assets/hero/source/male-character-fullbody.jpg');
const characterBase64 = fs.readFileSync(characterPath).toString('base64');
const characterDataUrl = `data:image/jpeg;base64,${characterBase64}`;

const framesDir = path.resolve('assets/hero/generated/frames');
fs.mkdirSync(framesDir, { recursive: true });

async function generateFrames() {
  console.log('🚀 Launching Playwright to render full-body male character motion frames...');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 800, height: 600 } });

  const htmlContent = `
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <style>
      body { margin: 0; padding: 0; background: #0d0e16; overflow: hidden; }
      #stage {
        position: relative;
        width: ${WIDTH}px;
        height: ${HEIGHT}px;
        background: #0d0e16;
        overflow: hidden;
      }
      #characterContainer {
        position: absolute;
        inset: 0;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        transform-origin: center bottom;
      }
      #character {
        height: 96%;
        width: auto;
        max-width: 100%;
        object-fit: contain;
        object-position: center bottom;
        filter: contrast(1.05) brightness(1.0);
      }
      #vignette {
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 50% 50%, transparent 55%, rgba(13, 14, 22, 0.4) 75%, rgba(13, 14, 22, 0.95) 100%);
        pointer-events: none;
      }
      #leftFade {
        position: absolute;
        inset: 0;
        background: linear-gradient(to right, rgba(13, 14, 22, 1) 0%, rgba(13, 14, 22, 0.5) 12%, transparent 28%);
        pointer-events: none;
      }
      #bottomFade {
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(13, 14, 22, 0.85) 0%, transparent 18%);
        pointer-events: none;
      }
      #lightScan {
        position: absolute;
        top: -50%;
        left: -100%;
        width: 300%;
        height: 200%;
        background: linear-gradient(115deg, transparent 40%, rgba(34, 211, 238, 0.12) 48%, rgba(167, 139, 250, 0.18) 52%, transparent 60%);
        pointer-events: none;
      }
      #hudScanline {
        position: absolute;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(to right, transparent, rgba(34, 211, 238, 0.5), transparent);
        box-shadow: 0 0 8px rgba(34, 211, 238, 0.7);
        pointer-events: none;
      }
      #gridOverlay {
        position: absolute;
        inset: 0;
        background-size: 28px 28px;
        background-image: 
          linear-gradient(to right, rgba(38, 42, 66, 0.12) 1px, transparent 1px),
          linear-gradient(to bottom, rgba(38, 42, 66, 0.12) 1px, transparent 1px);
        opacity: 0.5;
        pointer-events: none;
      }
      #auraGlow {
        position: absolute;
        bottom: 10%;
        left: 50%;
        width: 280px;
        height: 280px;
        transform: translateX(-50%);
        border-radius: 50%;
        background: radial-gradient(circle, rgba(34, 211, 238, 0.15) 0%, rgba(167, 139, 250, 0.08) 50%, transparent 70%);
        pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="stage">
      <div id="gridOverlay"></div>
      <div id="auraGlow"></div>
      <div id="characterContainer">
        <img id="character" src="${characterDataUrl}" />
      </div>
      <div id="lightScan"></div>
      <div id="hudScanline"></div>
      <div id="vignette"></div>
      <div id="leftFade"></div>
      <div id="bottomFade"></div>
    </div>
  </body>
  </html>
  `;

  await page.setContent(htmlContent);
  const stage = await page.$('#stage');

  console.log(`📸 Rendering ${TOTAL_FRAMES} full-body male character cinematic frames...`);
  const framePaths = [];

  for (let i = 0; i < TOTAL_FRAMES; i++) {
    const t = i / TOTAL_FRAMES;

    // Timing behavior per PDF:
    // 0.0 to 0.65 (0s - 2.6s): Motion phase (subtle breathing, pan, scanline sweep)
    // 0.65 to 0.8875 (2.6s - 3.55s): Hold final frame steady (~1.0 - 1.4s)
    // 0.8875 to 1.0 (3.55s - 4.0s): Fade & reset
    
    let scale = 1.0;
    let translateY = 0;
    let scanLeft = -100;
    let scanlineY = -10;
    let opacity = 1.0;

    if (t < 0.65) {
      // Active motion phase normalized 0..1
      const p = t / 0.65;
      // Gentle breathing/weight-shift: translateY 0 -> -5px -> 0
      translateY = -5 * Math.sin(p * Math.PI * 2);
      // Subtle scale 1.00 -> 1.025 -> 1.00
      scale = 1.0 + 0.02 * Math.sin(p * Math.PI * 2);
      // Scanning light sweep across character
      scanLeft = -100 + p * 200;
      // Scanline sweep top to bottom
      scanlineY = ((p * 2.0) % 1.0) * HEIGHT;
      opacity = 1.0;
    } else if (t < 0.8875) {
      // Hold phase: steady final confident pose
      translateY = 0;
      scale = 1.0;
      scanLeft = 100;
      scanlineY = HEIGHT + 20;
      opacity = 1.0;
    } else {
      // Fade phase: smooth fade out to black
      const f = (t - 0.8875) / (1.0 - 0.8875);
      translateY = 0;
      scale = 1.0;
      scanLeft = 100;
      scanlineY = HEIGHT + 20;
      opacity = Math.max(0, 1.0 - f * 0.9);
    }

    await page.evaluate(({ scale, translateY, scanLeft, scanlineY, opacity }) => {
      const charContainer = document.getElementById('characterContainer');
      charContainer.style.transform = `scale(${scale}) translateY(${translateY}px)`;
      charContainer.style.opacity = `${opacity}`;

      const lightScan = document.getElementById('lightScan');
      lightScan.style.transform = `translateX(${scanLeft}%)`;

      const hudScanline = document.getElementById('hudScanline');
      hudScanline.style.top = `${scanlineY}px`;
    }, { scale, translateY, scanLeft, scanlineY, opacity });

    const frameFile = path.join(framesDir, `frame_${String(i).padStart(3, '0')}.jpg`);
    await stage.screenshot({ path: frameFile, type: 'jpeg', quality: 50 });
    framePaths.push(frameFile);
  }

  await browser.close();
  console.log(`✅ Successfully generated ${framePaths.length} full-body male character frames in ${framesDir}`);
  return framePaths;
}

generateFrames().catch(err => {
  console.error('❌ Error generating frames:', err);
  process.exit(1);
});
