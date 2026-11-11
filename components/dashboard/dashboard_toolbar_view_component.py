from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_toolbar = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self):
        expect(self.dashboard_toolbar).to_be_visible()
        expect(self.dashboard_toolbar).to_have_text('Dashboard')
