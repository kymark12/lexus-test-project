from .vehicle_model_page import ModelPage
from data.constants import TestDriveData


class TestDriveForm(ModelPage, TestDriveData):
    def fill_test_drive_form(self):
        self.fill("input[id*='first']", self.first_name)
        self.fill("input[id='input_last_name']", self.last_name)
        self.fill("input[id$='address']", self.email)
        self.click("div[class$='selected-flag']")
        self.select_country_code(country="Singapore")
        self.fill("input[id$='number']", self.phone)
        self.click("input[id*='preferred']")
        self.select_date(month="April", date="10")
        self.click("//div[contains(@class, 'choices__list')][.//button[contains(@aria-label, \"time'\")]]", by="xpath")
        self.select_time(sample_time=self.preferred_time)
        self.click("/html/body/div[1]/main/article/section/section/div/form/div[10]/div/div[1]/div[1]/div", by="xpath")
        self.select_test_drive_options(option=self.test_drive_option)

    def tick_all_checkboxes(self):
        self.click("//div[contains(@style, 'fg')][.//*[@id='checkbox_driving_license']]", by="xpath")
        self.click("//div[contains(@style, 'fg')][.//*[@id='checkbox_terms_conditions']]", by="xpath")
        self.click("//div[contains(@style, 'fg')][.//*[@id='checkbox_privacy_policy']]", by="xpath")
        self.click("//div[contains(@style, 'fg')][.//*[@id='checkbox_marketing']]", by="xpath")
