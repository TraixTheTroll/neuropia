const { defineConfig, devices } = require("@playwright/test");
const path = require("node:path");
module.exports = defineConfig({
  testDir: __dirname,
  testMatch: "site.spec.cjs",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  workers: process.env.CI ? 2 : 3,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    baseURL: process.env.SITE_URL || "http://127.0.0.1:4176",
    reducedMotion: "reduce",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
    launchOptions: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE } : {},
  },
  projects: [
    { name: "desktop-chromium", use: { browserName: "chromium", viewport: { width: 1440, height: 1000 } } },
    { name: "mobile-chromium", use: { ...devices["Pixel 7"] } },
    { name: "narrow-chromium", use: { browserName: "chromium", viewport: { width: 320, height: 780 } } },
    { name: "mobile-webkit", use: { ...devices["iPhone 13"], launchOptions: {} } },
  ],
  webServer: process.env.SITE_URL
    ? undefined
    : {
        command: "node test/site/server.cjs",
        cwd: path.resolve(__dirname, "../.."),
        url: "http://127.0.0.1:4176",
        reuseExistingServer: !process.env.CI,
      },
});
