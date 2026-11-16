from playwright.sync_api import Page, expect
import re
from components.base_component import BaseComponent

class CourseMenuButton(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.menu_button_edit = page.get_by_test_id('course-view-edit-menu-item')
        self.menu_button_delete = page.get_by_test_id('course-view-delete-menu-item')

        self.modal_title = page.get_by_test_id('modal-title-text')

    def check_visible(self, index: int):
        expect(self.menu_button.nth(index)).to_be_visible()

    def click_menu(self, index: int):
        self.menu_button.nth(index).click()

    def check_visible_menu_items(self, index: int):
        expect(self.menu_button_edit.nth(index)).to_be_visible()
        expect(self.menu_button_delete.nth(index)).to_be_visible()

    def click_button_edit(self, index: int):
        self.menu_button_edit.nth(index).click()
        self.check_current_url(re.compile(".*/#/courses/*"))

    def click_button_delete(self, index: int):
        self.menu_button_delete.nth(index).click()

        expect(self.modal_title).to_be_visible()
        expect(self.modal_title).to_have_text('Confirm deleting course')