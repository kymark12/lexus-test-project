import time

from seleniumbase import BaseCase


class BaseTestCase(BaseCase):
    def setUp(self, **kwargs):
        super().setUp()
        self.open('https://www.lexus.com.sg/en.html')
        time.sleep(3)
        self.click("a#consent_prompt_submit")
        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>

    def tearDown(self):
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot"
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            pass
            # <<< Run custom code if the test passed. >>>
        # (Wrap unreliable tearDown() code in a try/except block.)
        # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
        super().tearDown()

    def select_vehicle_model(self, model):
        vehicle_list = self.find_elements("//ul[.//img[contains(@src, 'main')]]//li", by="xpath")

        for item in vehicle_list:
            if model in item.text:
                self.execute_script("arguments[0].scrollIntoView();", item)
                item.click()
                break

    def select_model_test_drive(self, model):
        self.click(f".list__explore li[data-id='{model}'] div[class='list__explore_cont'] "
                   f"div:nth-of-type(4) p a span")

    def select_country_code(self, country):
        country_list = self.find_elements("ul[id$='country-listbox'] li")
        for item in country_list:
            if country in item.text:
                item.click()
                break

    def select_date(self, month, date):
        self.select_option_by_text("select[class='flatpickr-monthDropdown-months']", month)
        date_list = self.find_elements("div[class='dayContainer'] span")
        for item in date_list:
            if date in item.text:
                item.click()
                break

    def select_time(self, sample_time):
        time_slots = self.find_elements("div[class$='is-active'] div[class='choices__list'] div")
        for selected_time in time_slots:
            if sample_time in selected_time.text:
                selected_time.click()
                break

    def select_test_drive_options(self, option):
        test_drive_options = self.find_elements("div[class$='is-active'] div[class='choices__list'] div")
        for item in test_drive_options:
            if option in item.text:
                item.click()
                break
