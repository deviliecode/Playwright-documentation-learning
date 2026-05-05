import pytest
from playwright.sync_api import Page
from tests.saucedemo_sign_in import login_to_page

@pytest.fixture
def login_to_secret_sauce(page: Page):
    login_to_page(page)
    return page