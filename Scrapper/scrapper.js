const puppeteer = require("puppeteer");
const fs = require("fs");

const scrapImages = async (url) => {
  const brower = await puppeteer.launch({
    headless: false,
  });
  const page = await brower.newPage();
  await page.setUserAgent("UA-TEST");
  let counter = 0;
  page.on("response", async (response) => {
    const matches = /.*\.(jpg)$/.exec(response.url());
    if (matches && matches.length === 2) {
      const extension = matches[1];
      const buffer = await response.buffer();
      fs.writeFileSync(
        `../Images/Atypical-melanocytic/image-${counter}.${extension}`,
        buffer,
        "base64"
      );
      counter += 1;
    }
  });
  await page.goto(url, { waitUntil: "networkidle0" });
  await brower.close();
};

scrapImages("https://dermnetnz.org/topics/atypical-naevus-images?stage=Live");
