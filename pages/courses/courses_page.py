from playwright.sync_api import Page

from components.courses.course_menu_button_component import CourseMenuButton
from components.courses.course_preview_component import CoursePreview
from components.courses.course_toolbar_component import CourseToolbarComponent
from components.view.empty_view_component import EmptyViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent

from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar_course = CourseToolbarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.preview_picture = CoursePreview(page)
        self.course_menu_button = CourseMenuButton(page)

        # если в методы (в инит) отдельно не прописывать)
        # title_modal_confirm = self.page.get_by_test_id('modal-title-text')
        # expect(title_modal_confirm).to_be_visible()
