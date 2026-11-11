import re
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_item_list_component import SidebarItemListComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_component = SidebarItemListComponent(page, 'dashboard')
        self.courses_component = SidebarItemListComponent(page, 'courses')
        self.logout_component = SidebarItemListComponent(page, 'logout')

    def check_visible(self):
        self.dashboard_component.check_visible("Dashboard")
        self.courses_component.check_visible("Courses")
        self.logout_component.check_visible("Logout")

    def click_courses(self):
        self.courses_component.click_button_and_to_go_new_page(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.dashboard_component.click_button_and_to_go_new_page(re.compile(r".*/#/dashboard"))

    def click_logout(self):
        self.logout_component.click_button_and_to_go_new_page(re.compile(r".*/#/auth/login"))
