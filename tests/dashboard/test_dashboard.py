import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.navbar.check_visible('test_username')
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.chart_view.check_visible()
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.sidebar.click_courses()
        dashboard_page_with_state.sidebar.click_dashboard()
        dashboard_page_with_state.sidebar.click_logout()
