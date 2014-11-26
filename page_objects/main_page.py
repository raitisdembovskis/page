from config import settings

class MainPage():

    POST_CODE = 'post-code-input'
    GREEN_BUTTON = 'cta-homepage'

    def __init__(self, driver):
        self.driver = driver

    def fill_postcode(self, post_code):
        input_text_field = self.driver.find_element_by_id(self.POST_CODE)
        input_text_field.send_keys(post_code)

    def click_green_button(self):
        submit_button = self.driver.find_element_by_id(self.GREEN_BUTTON)
        submit_button.click()

    def go_to_main_page(self):
        self.driver.get(settings.CONSOLE)