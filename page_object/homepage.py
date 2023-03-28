from utilities.base_class import BaseTestCase


class HomePage(BaseTestCase):
    def verify_banner_homepage(self):
        banner_status = self.is_element_visible("section[class*='masthead']")
        assert banner_status is True, "Masthead Banner is missing!"

    def access_ux_series_page(self):
        self.select_vehicle_model(model='UX')

