import re

from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.title_page = page.get_by_test_id('authentication-ui-course-title-text')
        self.button_registration = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def check_visible_title_page(self):
        expect(self.title_page).to_be_visible()
        expect(self.title_page).to_have_text('UI Course')

    def check_visible_button_registration(self):
        expect(self.button_registration).to_be_visible()

    def click_button_registration(self):
        self.button_registration.click()

    def check_visible_login_link(self):
        expect(self.login_link).to_be_visible()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login.*"))
