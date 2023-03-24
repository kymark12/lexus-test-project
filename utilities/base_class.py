from seleniumbase import BaseCase


class BaseTestCase(BaseCase):
    def setUp(self, **kwargs):
        super().setUp()
        self.open('http://localhost:3000/')
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