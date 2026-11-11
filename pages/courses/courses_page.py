import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.toolbar_button_create_courses = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.empty_state_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_state_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_state_description = page.get_by_test_id('courses-list-empty-view-description-text')

        self.widget_title = page.get_by_test_id('course-widget-title-text')
        self.widget_preview_image = page.get_by_test_id('course-preview-image')
        self.widget_max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        self.widget_min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        self.widget_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.widget_menu_button = page.get_by_test_id('course-view-menu-button')
        self.widget_menu_button_edit = page.get_by_test_id('course-view-edit-menu-item')
        self.widget_menu_button_delete = page.get_by_test_id('course-view-delete-menu-item')

        self.modal_title = page.get_by_test_id('modal-title-text')

    # Toolbar (it's component)

    def check_visible_toolbar(self):
        expect(self.toolbar_title).to_be_visible()
        expect(self.toolbar_title).to_have_text('Courses')

        expect(self.toolbar_button_create_courses).to_be_visible()

    def click_toolbar_button_create_courses(self):
        self.toolbar_button_create_courses.click()
        self.check_current_url(re.compile(".*/#/courses/create"))

    # Empty state. When courses is not available (it's component)
    def check_visible_empty_state(self):
        expect(self.empty_state_icon).to_be_visible()

        expect(self.empty_state_title).to_be_visible()
        expect(self.empty_state_title).to_have_text('There is no results')

        expect(self.empty_state_description).to_be_visible()
        expect(self.empty_state_description).to_have_text('Results from the load test pipeline will be displayed here')

    # Widget. (it's component)
    def check_preview_image(self, index: int):
        expect(self.widget_preview_image.nth(index)).to_be_visible()

    def check_visible_widget(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        expect(self.widget_title.nth(index)).to_be_visible()
        expect(self.widget_title.nth(index)).to_have_text(title)

        expect(self.widget_preview_image.nth(index)).to_be_visible()

        expect(self.widget_max_score.nth(index)).to_be_visible()
        expect(self.widget_max_score.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.widget_min_score.nth(index)).to_be_visible()
        expect(self.widget_min_score.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.widget_estimated_time.nth(index)).to_be_visible()
        expect(self.widget_estimated_time.nth(index)).to_have_text(f"Estimated time: {estimated_time}")

    # Widget menu button. (it's component)

    def check_visible_widget_menu_button(self, index: int):
        expect(self.widget_menu_button).to_be_visible(nth=index)

    def click_widget_menu_button(self, index: int):
        self.widget_menu_button.click(nth=index)

    def check_visible_widget_menu_button_edit_and_delete(self, index: int):
        expect(self.widget_menu_button_edit).to_be_visible(nth=index)
        expect(self.widget_menu_button_delete).to_be_visible(nth=index)

    def click_widget_menu_button_edit(self, index: int):
        self.widget_menu_button_edit.click(nth=index)
        self.check_current_url(re.compile(".*/#/courses/*"))

    def click_widget_menu_button_delete(self, index: int):
        self.widget_menu_button_delete.click(nth=index)
        expect(self.modal_title).to_be_visible(nth=index)
        expect(self.modal_title).to_have_text('Confirm deleting course', nth=index)

        # если в методы (в инит) отдельно не прописывать)
        # title_modal_confirm = self.page.get_by_test_id('modal-title-text')
        # expect(title_modal_confirm).to_be_visible()
