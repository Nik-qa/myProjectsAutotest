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
        courses_page_with_state.toolbar_course.check_visible()
        courses_page_with_state.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here"
        )

    def test_create_course(self, courses_page_with_state: CoursesPage, create_course_page_with_state: CreateCoursePage):
        create_course_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
        )

        create_course_page_with_state.toolbar_create_course.check_visible()
        create_course_page_with_state.check_visible_picture_empty_state()
        create_course_page_with_state.view_upload_widget.check_visible()
        create_course_page_with_state.view_upload_widget.check_upload_image_button()
        create_course_page_with_state.view_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page_with_state.create_course_forme.fill_form(
            title='Python',
            estimated_time='777',
            description='Pytest',
            max_score='99',
            min_score='10'
        )
        create_course_page_with_state.create_course_forme.check_visible(
            title='Python',
            estimated_time='777',
            description='Pytest',
            max_score='99',
            min_score='10'
        )
        create_course_page_with_state.toolbar_exercise.check_visible()
        create_course_page_with_state.check_visible_exercise_empty_state()
        create_course_page_with_state.toolbar_exercise.click_button()
        create_course_page_with_state.form_exercise.check_visible(
            index=0,
            title='Exercise title',
            description='Exercise description'
        )

        # courses_page_with_state.course_menu_button.check_visible(index=0)
        # courses_page_with_state.course_menu_button.click_menu(index=0)
        # courses_page_with_state.course_menu_button.check_visible_menu_items(index=0)

        courses_page_with_state.page.wait_for_timeout(1000)
