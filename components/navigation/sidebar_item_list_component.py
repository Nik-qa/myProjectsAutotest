from typing import Pattern

from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class SidebarItemListComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.button).to_be_visible()

    def click_button_and_to_go_new_page(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)