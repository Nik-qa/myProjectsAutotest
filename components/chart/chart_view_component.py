from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.chart.chart_item_list_component import ChartItemListComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.students_chart_component = ChartItemListComponent(page, "students", "bar")
        self.activities_chart_component = ChartItemListComponent(page,"activities", "line")
        self.courses_chart_component = ChartItemListComponent(page, 'courses', "pie")
        self.scores_chart_component = ChartItemListComponent(page, 'scores', "scatter")

    def check_visible(self):
        self.students_chart_component.check_visible("Students")
        self.activities_chart_component.check_visible("Activities")
        self.courses_chart_component.check_visible("Courses")
        self.scores_chart_component.check_visible("Scores")

