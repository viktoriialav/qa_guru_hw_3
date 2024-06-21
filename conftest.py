import pytest
from selene import browser
from selene.support import webdriver


@pytest.fixture(autouse=True)
def browser_options():
    browser.config.base_url = 'https://www.google.ru/'
    browser.config.window_height = 600
    browser.config.window_width = 800

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'

    yield
    browser.quit()