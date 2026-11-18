from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

#локаторы в конструкторе класс определить нельзя, т.к. они динамические: https://stepik.org/lesson/1456882/step/11?split=true&unit=1476151
class CreateCourseFormExercise(BaseComponent):
    def click_delete_button(self, index: int):
        delete_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input").locator('input')
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input").locator('input')

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input").locator('input')
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input").locator('input')

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)
    # def __init__(self, page: Page):
    #     super().__init__(page)
    #
    #     self.subtitle = page.get_by_test_id('create-course-exercise-{index}-box-toolbar-subtitle-text')
    #     self.delete_button = page.get_by_test_id(
    #         'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
    #     self.title_input = page.get_by_test_id('create-course-exercise-form-title-{index}-input').locator(
    #         'input')
    #     self.description_input = page.get_by_test_id(
    #         'create-course-exercise-form-description-{index}-input').locator('input')

    # def check_visible(self, index: int, exercise_title: str, exercise_description: str):
    #     expect(self.subtitle.nth(index)).to_be_visible()
    #     expect(self.subtitle.nth(index)).to_have_text(f"#{index + 1} Exercise")
    #
    #     expect(self.title_input.nth(index)).to_be_visible()
    #     expect(self.title_input.nth(index)).to_have_value(exercise_title)
    #
    #     expect(self.description_input.nth(index)).to_be_visible()
    #     expect(self.description_input.nth(index)).to_have_value(exercise_description)
    #
    #     expect(self.delete_button.nth(index)).to_be_visible()
    #
    # def fill_form(self, index: int, exercise_title: str, exercise_description: str):
    #     self.title_input.nth(index).fill(exercise_title)
    #     self.description_input.nth(index).fill(exercise_description)
    #
    # def click_exercise_delete_button(self, index: int):
    #     self.delete_button.nth(index).click()
