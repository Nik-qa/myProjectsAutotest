import re

from playwright.sync_api import Page, expect

from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.title_login_page = page.get_by_test_id('authentication-ui-course-title-text')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.alert_wrong_login_or_password = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        self.registration_link = page.get_by_test_id('login-page-registration-link')

    def check_visible_title_login_page(self):
        expect(self.title_login_page).to_be_visible()
        expect(self.title_login_page).to_have_text('UI Course')

    def check_visible_login_button_disabled(self):
        expect(self.login_button).to_be_visible()
        expect(self.login_button).to_be_disabled()

    def check_visible_login_button_active(self):
        expect(self.login_button).to_be_visible()
        expect(self.login_button).to_be_enabled()

    def click_login_button(self):
        self.login_button.click()

    def check_visible_alert(self):
        expect(self.alert_wrong_login_or_password).to_be_visible()
        expect(self.alert_wrong_login_or_password).to_have_text('Wrong email or password')

    def check_visible_registration_link(self):
        expect(self.registration_link).to_be_visible()
        expect(self.registration_link).to_have_text('Registration')

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))
