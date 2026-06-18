from playwright.sync_api import sync_playwright
from datetime import datetime
import logging
import time

logging.basicConfig(level=logging.INFO)


class BrowserAgent:

    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--start-maximized",
                "--disable-blink-features=AutomationControlled"
            ]
        )

        self.context = self.browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )

        self.page = self.context.new_page()

        logging.info("Browser started")

    def open(self, url: str):
        self.page.goto(url)
        logging.info(f"Open {url}")

    def click(self, selector: str):
        self.page.click(selector)

    def type(self, selector: str, text: str):
        self.page.fill(selector, text)

    def press(self, selector: str, key: str):
        self.page.press(selector, key)

    def wait(self, seconds: int):
        time.sleep(seconds)

    def screenshot(self, path: str):
        self.page.screenshot(path=path)

    def html(self):
        return self.page.content()

    def title(self):
        return self.page.title()

    def current_url(self):
        return self.page.url

    def execute(self, script: str):
        return self.page.evaluate(script)

    def refresh(self):
        self.page.reload()

    def back(self):
        self.page.go_back()

    def forward(self):
        self.page.go_forward()

    def close(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        logging.info("Browser closed")


if __name__ == "__main__":

    browser = BrowserAgent(headless=False)

    browser.start()

    browser.open("https://www.google.com")

    print(browser.title())

    browser.close()
