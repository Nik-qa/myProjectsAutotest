from playwright.sync_api import Page


from pages.base_page import BasePage
from components.view.empty_view_component import EmptyViewComponent
from components.view.upload_widget_component import ViewUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_exercise import CreateCourseToolbarExercise
from components.courses.create_course_form_exercise import CreateCourseFormExercise
from components.courses.create_course_toolbar_component import CreateCourseToolbarComponent

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.toolbar_create_course = CreateCourseToolbarComponent(page)
        self.preview_empty_state = EmptyViewComponent(page, 'create-course-preview-empty')
        self.view_upload_widget = ViewUploadWidgetComponent(page, 'create-course-preview-image-upload-widget')
        self.create_course_forme = CreateCourseFormComponent(page)
        self.toolbar_exercise = CreateCourseToolbarExercise(page)
        self.exercise_empty_state = EmptyViewComponent(page, 'create-course-exercises-empty')
        self.form_exercise = CreateCourseFormExercise(page)

    def check_visible_picture_empty_state(self):
        self.preview_empty_state.check_visible(
            title='No image selected',
            description='Preview of selected image will be displayed here'
        )

    def check_visible_exercise_empty_state(self):
        self.exercise_empty_state.check_visible(
            title="There is no exercises",
            description='Click on "Create exercise" button to create new exercise'
        )
