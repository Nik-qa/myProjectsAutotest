from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.view.empty_view_component import EmptyViewComponent


class ViewUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_state = EmptyViewComponent(page, 'create-course-preview-empty')

        self.icon = page.get_by_test_id(f'{identifier}-info-icon')
        self.title = page.get_by_test_id(f'{identifier}-info-title-text')
        self.description = page.get_by_test_id(f'{identifier}-info-description-text')
        self.upload_image_button = page.get_by_test_id(f'{identifier}-upload-button').locator('input')
        self.remove_image_button = page.get_by_test_id(f'{identifier}-remove-button')

        self.preview_pictures = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

    def check_visible(self, is_image_uploaded: bool = False):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.description).to_be_visible()
        expect(self.description).to_have_text('Recommended file size 540X300')

        expect(self.upload_image_button).to_be_visible()

        if is_image_uploaded:
            expect(self.remove_image_button).to_be_visible()
            expect(self.preview_pictures).to_be_visible()

        if not is_image_uploaded:
            self.preview_empty_state.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_image_button.click()

    def check_upload_image_button(self):
        self.upload_image_button.set_input_files(files='./testdata/files/image.jpg')
