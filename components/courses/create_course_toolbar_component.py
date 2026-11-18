from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CreateCourseToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.button_create_course = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, button_is_disabled=True):
        expect(self.title).to_have_text("Create course")

        if button_is_disabled:
            expect(self.button_create_course).to_be_visible()
            expect(self.button_create_course).to_be_disabled()

        if not button_is_disabled:
            expect(self.button_create_course).to_be_visible()
            expect(self.button_create_course).to_be_enabled()

    def click_button_create_course(self):
        self.button_create_course.click()
