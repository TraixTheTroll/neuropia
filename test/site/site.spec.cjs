const { test, expect } = require("@playwright/test");
const fs = require("node:fs");
const path = require("node:path");
const YAML = require("yaml");
const root = path.resolve(__dirname, "../..");
const members = YAML.parse(fs.readFileSync(path.join(root, "_data/members.yml"), "utf8"));
const publicationKeys = [...fs.readFileSync(path.join(root, "_bibliography/neuropia.bib"), "utf8").matchAll(/^@\w+\s*\{\s*([^,\s]+),/gm)].map(
  (match) => match[1]
);

test.beforeEach(async ({ page }) => {
  page.on("pageerror", (error) => {
    throw error;
  });
});

test("homepage sections, navigation and layout", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "NEUROPIA", exact: true })).toBeVisible();
  for (const id of ["about", "research", "people", "publications", "contact"]) {
    const link = page.locator(`nav a[href="#${id}"]`);
    if (test.info().project.use.hasTouch) await link.tap();
    else await link.click();
    await expect(page).toHaveURL(new RegExp(`#${id}$`));
    const top = await page.locator(`#${id}`).evaluate((element) => element.getBoundingClientRect().top);
    const navBottom = await page.locator("nav").evaluate((element) => element.getBoundingClientRect().bottom);
    expect(top).toBeGreaterThanOrEqual(navBottom - 1);
  }
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
});

test("shared standalone pages remain available", async ({ page }) => {
  for (const [route, title] of [
    ["research", "Research"],
    ["people", "People"],
    ["contact", "Contact"],
  ]) {
    const response = await page.goto(`/${route}/`);
    expect(response.status()).toBe(200);
    await expect(page.getByRole("heading", { level: 1 })).toHaveText(title);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  }
});

test("directory loads small portraits instead of full-size photos", async ({ page }) => {
  const originals = members.map((member) => `/assets/img/${member.image}`);
  const requestedOriginals = [];
  page.on("request", (request) => {
    if (originals.includes(new URL(request.url()).pathname)) requestedOriginals.push(request.url());
  });
  await page.goto("/");
  for (const member of members) {
    const card = page.getByRole("link", { name: `View profile of ${member.name}`, exact: true });
    await expect(card).toHaveAttribute("href", `/people/${member.slug}/`);
    const image = card.locator("img");
    await image.scrollIntoViewIfNeeded();
    await expect(image).toHaveAttribute("src", `/assets/img/${member.thumbnail}`);
    await image.evaluate((element) => element.decode());
    expect(await image.evaluate((element) => [element.naturalWidth, element.naturalHeight])).toEqual([330, 330]);
  }
  expect(requestedOriginals).toEqual([]);
  await page.locator('.person[href="/people/andrea-gremes/"]').click();
  await expect(page).toHaveURL(/\/people\/andrea-gremes\/$/);
  await expect(page.locator(".neuropia-profile-photo")).toHaveAttribute("src", "/assets/img/people/ag-updated.jpg");
});

for (const member of members) {
  test(`profile: ${member.name}`, async ({ page }) => {
    const response = await page.goto(`/people/${member.slug}/`);
    expect(response.status()).toBe(200);
    await expect(page.getByRole("heading", { level: 1 })).toHaveText(member.name);
    const image = page.locator(".neuropia-profile-photo");
    await expect(image).toHaveAttribute("src", `/assets/img/${member.image}`);
    await image.evaluate((element) => element.decode());
    expect(await image.evaluate((element) => [element.naturalWidth, element.naturalHeight])).toEqual([member.image_width, member.image_height]);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await page.getByRole("link", { name: "← All people" }).click();
    await expect(page).toHaveURL(/\/#people$/);
  });
}

test("publications match the bibliography and year toggles work", async ({ page }) => {
  await page.goto("/publications/");
  expect((await page.locator("article.pub").evaluateAll((elements) => elements.map((element) => element.id))).sort()).toEqual(
    [...publicationKeys].sort()
  );
  const year = page.locator("details.publication-year").first();
  await expect(year).toHaveAttribute("open", "");
  await year.locator("summary").focus();
  await page.keyboard.press("Enter");
  await expect(year).not.toHaveAttribute("open", "");
  await page.keyboard.press("Space");
  await expect(year).toHaveAttribute("open", "");
  if (test.info().project.use.hasTouch) {
    await year.locator("summary").tap();
    await expect(year).not.toHaveAttribute("open", "");
  }
});

test("missing page stays visible and returns home on request", async ({ page }) => {
  const response = await page.goto("/missing-page-smoke-check/");
  expect(response.status()).toBe(404);
  await expect(page.getByRole("heading", { name: "Page not found" })).toBeVisible();
  await expect(page.locator('meta[http-equiv="refresh"]')).toHaveCount(0);
  await page.waitForTimeout(3300);
  await expect(page).toHaveURL(/\/missing-page-smoke-check\/$/);
  await page.getByRole("link", { name: "Return to homepage" }).click();
  await expect(page.getByRole("heading", { name: "NEUROPIA", exact: true })).toBeVisible();
});

test("animations are preserved and reduced motion works", async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "no-preference" });
  await page.goto("/");
  expect(await page.locator(".logo").evaluate((element) => getComputedStyle(element).animationName)).toBe("float, glow");
  expect(await page.locator(".neuropia-group-photo").evaluate((element) => getComputedStyle(element).animationName)).toBe("group-float, glow");
  await page.emulateMedia({ reducedMotion: "reduce" });
  await expect.poll(() => page.locator(".logo").evaluate((element) => getComputedStyle(element).animationName)).toBe("none");
  await page.waitForTimeout(100);
  const first = await page.locator("#canvas").evaluate((element) => element.toDataURL());
  await page.waitForTimeout(100);
  expect(await page.locator("#canvas").evaluate((element) => element.toDataURL())).toBe(first);
});

test("skip link provides keyboard access to content", async ({ page }) => {
  await page.goto("/");
  await page.keyboard.press("Tab");
  await expect(page.getByRole("link", { name: "Skip to content" })).toBeFocused();
  await page.keyboard.press("Enter");
  await page.keyboard.press("Tab");
  await expect(page.locator(".cta")).toBeFocused();
});

test("publications remain readable without JavaScript", async ({ browser, baseURL }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  await page.goto(`${baseURL}/publications/`);
  await expect(page.locator("article.pub")).toHaveCount(publicationKeys.length);
  await expect(page.locator("article.pub").first()).toBeVisible();
  await context.close();
});
