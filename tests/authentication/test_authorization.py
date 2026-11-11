import pytest

from pages.authentication.login_page import LoginPage


@pytest.mark.parametrize(
    "email, password",
    [
        ("e@@gmail.com", "password"),
        ("e email@gmail.com", " "),
        (" ", "password")
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.login_form.fill_login_form(email, password)
    login_page.check_visible_login_button_active()
    login_page.click_login_button()


def test_check_alert(login_page: LoginPage):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.fill_input_email_and_password(email=" ", password="password")
    login_page.click_login_button()
    login_page.check_visible_alert()

