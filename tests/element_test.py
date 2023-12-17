import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            test_box_page.open()
            full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()
            output_name, output_email, output_c, output_p = test_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_c
            assert permanent_address == output_p

