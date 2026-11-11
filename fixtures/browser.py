import pytest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(
        email='testemail@gmail.com', username='test_username', password='qwerty1241'
    )
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

    page.wait_for_timeout(1000)

    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state: Page, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    # page = context.new_page()
    yield context.new_page()
    browser.close()
