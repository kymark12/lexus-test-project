import time

import pytest

from page_object.book_test_drive import TestDriveForm
'''
Scenarios:
1. Verify masthead banner
2. Verify UX page youtube video
3. Verify booking a UX model test drive
'''


class LexusSgTest(TestDriveForm):
    @pytest.mark.order("first")
    def test_verify_masthead_banner(self):
        self.verify_banner_homepage()

    @pytest.mark.order("second")
    def test_verify_ux_video(self):
        time.sleep(3)
        self.access_ux_series_page()
        time.sleep(3)
        self.verify_features_section()

    @pytest.mark.order("third")
    def test_book_a_test_drive(self):
        self.access_ux_series_page()
        self.book_a_test_drive(model="ux-250h")
        self.fill_test_drive_form()
        self.tick_all_checkboxes()


