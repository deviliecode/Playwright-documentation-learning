import os
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()

login = os.getenv("SAUCE_USERNAME")
password = os.getenv("SAUCE_PASSWORD")
saucedemo_url = "https://www.saucedemo.com/"

def login_to_page(page: Page):
    page.goto(saucedemo_url)
    page.locator("#user-name").fill(login)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()