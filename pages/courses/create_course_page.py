from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # toolbar component
        self.toolbar_title_create_course = page.get_by_test_id('create-course-toolbar-title-text')
        self.button_create_course = page.get_by_test_id('create-course-toolbar-create-course-button')

        # preview pictures component
        self.empty_view_preview_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.empty_view_preview_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.empty_view_preview_description = page.get_by_test_id('create-course-preview-empty-view-description-text')
        self.preview_pictures = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        # upload widget component
        self.upload_widget_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_widget_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_widget_description = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text')
        self.upload_image_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button').locator('input')
        self.remove_image_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

        # create course forme. component
        self.form_title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.form_estimated_time = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.form_description = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.form_max_score = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.form_min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        # Exercises empty state. component
        self.exercises_empty_state_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_state_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_state_description = page.get_by_test_id(
            'create-course-exercises-empty-view-description-text')

        # toolbar  Exercises. component
        self.exercise_toolbar_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercise_toolbar_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        # exercises form. component
        self.exercise_form_subtitle = page.get_by_test_id('create-course-exercise-{index}-box-toolbar-subtitle-text')
        self.exercise_form_delete_button = page.get_by_test_id(
            'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        self.exercise_title_input = page.get_by_test_id('create-course-exercise-form-title-{index}-input').locator(
            'input')
        self.exercise_description_input = page.get_by_test_id(
            'create-course-exercise-form-description-{index}-input').locator('input')

    # toolbar component
    def check_visible_toolbar(self, button_is_disabled=True):
        expect(self.toolbar_title_create_course).to_have_text("Create course")

        if button_is_disabled:
            expect(self.button_create_course).to_be_visible()
            expect(self.button_create_course).to_be_disabled()

        if not button_is_disabled:
            expect(self.button_create_course).to_be_visible()
            expect(self.button_create_course).to_be_enabled()

    def click_button_create_course(self):
        self.button_create_course.click()

    # preview pictures component
    def check_visible_empty_view_preview(self):
        expect(self.empty_view_preview_icon).to_be_visible()
        expect(self.empty_view_preview_title).to_be_visible()
        expect(self.empty_view_preview_title).to_have_text("No image selected")
        expect(self.empty_view_preview_description).to_be_visible()
        expect(self.empty_view_preview_description).to_have_text("Preview of selected image will be displayed here")

    def check_visible_preview_pictures(self):
        expect(self.preview_pictures).to_be_visible()

    # upload widget component
    def check_visible_upload_widget(self, is_image_uploaded: bool = False):
        expect(self.upload_widget_icon).to_be_visible()

        expect(self.upload_widget_title).to_be_visible()
        expect(self.upload_widget_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.upload_widget_description).to_be_visible()
        expect(self.upload_widget_description).to_have_text('Recommended file size 540X300')

        expect(self.upload_image_button).to_be_visible()

        if is_image_uploaded:
            expect(self.remove_image_button).to_be_visible()
            expect(self.preview_pictures).to_be_visible()

        if not is_image_uploaded:
            expect(self.empty_view_preview_title).to_be_visible()
            expect(self.empty_view_preview_title).to_have_text("No image selected")

    def click_remove_image_button(self):
        self.remove_image_button.click()

    def check_upload_image_button(self):
        self.upload_image_button.set_input_files(files='./testdata/files/image.jpg')

    # create course forme. component
    def check_visible_form_create_course(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str,
    ):
        expect(self.form_title).to_be_visible()
        expect(self.form_title).to_have_value(title)

        expect(self.form_estimated_time).to_be_visible()
        expect(self.form_estimated_time).to_have_value(estimated_time)

        expect(self.form_description).to_be_visible()
        expect(self.form_description).to_have_value(description)

        expect(self.form_max_score).to_be_visible()
        expect(self.form_max_score).to_have_value(max_score)

        expect(self.form_min_score).to_be_visible()
        expect(self.form_min_score).to_have_value(min_score)

    def fill_form_create_course(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str,
    ):
        self.form_title.fill(title)
        self.form_estimated_time.fill(estimated_time)
        self.form_description.fill(description)
        self.form_max_score.fill(max_score)
        self.form_min_score.fill(min_score)

    # Exercises empty state. component
    def check_visible_exercises_empty_state(self):
        expect(self.exercises_empty_state_icon).to_be_visible()
        expect(self.exercises_empty_state_title).to_be_visible()
        expect(self.exercises_empty_state_title).to_have_text("There is no exercises")
        expect(self.exercises_empty_state_description).to_be_visible()
        expect(self.exercises_empty_state_description).to_have_text(
            'Click on "Create exercise" button to create new exercise')

    # toolbar  Exercises. component
    def check_visible_exercise_toolbar(self):
        expect(self.exercise_toolbar_title).to_be_visible()
        expect(self.exercise_toolbar_title).to_have_text("Exercises")
        expect(self.exercise_toolbar_button).to_be_visible()

    def click_exercise_toolbar_button(self):
        self.exercise_toolbar_button.click()
        expect(self.exercise_form_subtitle).to_be_visible()

    # exercises form. component
    def check_visible_exercise_form(self, index: int, exercise_title: str, exercise_description: str):
        expect(self.exercise_form_subtitle).to_be_visible(index=index)
        expect(self.exercise_form_subtitle).to_have_text(f"#{index + 1} Exercise", index=index)

        expect(self.exercise_title_input).to_be_visible(index=index)
        expect(self.exercise_title_input).to_have_value(exercise_title, index=index)

        expect(self.exercise_description_input).to_be_visible(index=index)
        expect(self.exercise_description_input).to_be_visible(exercise_description, index=index)

        expect(self.exercise_form_delete_button).to_be_visible(index=index)

    def fill_exercise_form(self, index: int, exercise_title: str, exercise_description: str):
        expect(self.exercise_title_input).to_be_visible(index=index)
        expect(self.exercise_title_input).to_have_value(exercise_title, index=index)

        self.exercise_description_input.fill(index=index)
        self.exercise_description_input.fill(exercise_description, index=index)

    def click_exercise_delete_button(self, index: int):
        self.exercise_form_delete_button.click(index=index)
