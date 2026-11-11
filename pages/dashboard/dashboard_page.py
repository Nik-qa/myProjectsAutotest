from playwright.sync_api import Page

from components.chart.chart_view_component import ChartViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.chart_view = ChartViewComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)
        self.navbar = NavbarComponent(page)
