import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.courses.courses_page import CoursesPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
class TestCourses:
    def test_authentication(
            self, login_page: LoginPage, registration_page: RegistrationPage, dashboard_page: DashboardPage
    ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='World@gmai.com', username='World', password='41_HI')
        registration_page.click_button_registration()
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()
        # login_page.page.wait_for_timeout(2000)
        login_page.login_form.fill(email='World@gmai.com', password='41_HI')
        login_page.click_login_button()
        dashboard_page.navbar.check_visible('World')

    def test_check_empty_state_view(self, courses_page_with_state: CoursesPage):
        courses_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_page_with_state.check_visible_toolbar()
        courses_page_with_state.check_visible_empty_state()

    def test_create_course(self, courses_page_with_state: CoursesPage, create_course_page_with_state: CreateCoursePage):
        create_course_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )
        create_course_page_with_state.check_visible_toolbar()
        create_course_page_with_state.check_visible_empty_view_preview()
        create_course_page_with_state.check_visible_upload_widget(is_image_uploaded=False)
        create_course_page_with_state.check_upload_image_button()
        create_course_page_with_state.check_visible_form_create_course(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )
        create_course_page_with_state.fill_form_create_course(
            title='Python',
            estimated_time='100',
            description='Autotest',
            max_score='100',
            min_score='9'
        )
        create_course_page_with_state.check_visible_form_create_course(
            title='Python',
            estimated_time='100',
            description='Autotest',
            max_score='100',
            min_score='9'
        )
        create_course_page_with_state.click_button_create_course()

        courses_page_with_state.check_preview_image(index=0)

        courses_page_with_state.page.wait_for_timeout(2000)
