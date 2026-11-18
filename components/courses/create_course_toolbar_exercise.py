from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class CreateCourseToolbarExercise(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercise_toolbar_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercise_toolbar_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    # toolbar  Exercises. component
    def check_visible(self):
        expect(self.exercise_toolbar_title).to_be_visible()
        expect(self.exercise_toolbar_title).to_have_text("Exercises")
        expect(self.exercise_toolbar_button).to_be_visible()

    def click_button(self):
        self.exercise_toolbar_button.click()