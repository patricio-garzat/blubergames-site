// Toma una captura de cada <section> de designs.html al tamaño exacto (PNG).
// Uso: NODE_PATH=<carpeta con puppeteer-core>/node_modules node render.js
const puppeteer = require("puppeteer-core");
const path = require("path");

(async () => {
  const browser = await puppeteer.launch({
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: true,
    args: ["--allow-file-access-from-files"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 1500, deviceScaleFactor: 1 });
  await page.goto("file://" + path.join(__dirname, "designs.html"), { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  await new Promise((r) => setTimeout(r, 500));
  const names = { profile: "profile-bear", "profile-navy": "profile-bear-navy", p1: "post-1-hello", p2: "post-2-cube-swipe", p3: "post-3-how-to-play" };
  for (const [id, name] of Object.entries(names)) {
    const el = await page.$("#" + id);
    await el.screenshot({ path: path.join(__dirname, "..", name + ".png") });
    console.log(name);
  }
  await browser.close();
})();
