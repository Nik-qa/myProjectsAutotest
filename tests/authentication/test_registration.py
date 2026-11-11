import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.check_visible_title_page()
    registration_page.registration_form.check_visible()
    registration_page.registration_form.fill(email='qwe4@gmil.com', username='nine', password='2412')
    registration_page.check_visible_button_registration()
    registration_page.click_button_registration()
    dashboard_page.sidebar.check_visible()
    dashboard_page.navbar.check_visible(username='nine')
    dashboard_page.dashboard_toolbar.check_visible()


def test_navigation_click_link_registration_to_login(registration_page: RegistrationPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.click_login_link()
