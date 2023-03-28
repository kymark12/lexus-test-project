from .homepage import HomePage


class ModelPage(HomePage):
    def verify_features_section(self):
        features_section = self.is_element_visible("section[id='features']")
        assert features_section is True, "Features section is NOT visible!"

    def book_a_test_drive(self, model):
        self.select_model_test_drive(model=model)
