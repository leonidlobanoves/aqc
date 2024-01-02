import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinkPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result


    class TestRadiobutton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_random_radiobutton()
            radio_button_page.get_output_result()

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            added_person = web_table_page.add_new_person()
            result = web_table_page.check_new_added_person()
            print(added_person)
            print(result)
            assert added_person in result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_searched_person()
            assert key_word in table_result, "The person was not found"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_searched_person()
            print(age)
            print(row)
            assert age in row

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100]

    class TestButtonsPage:

        def test_different_click_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_buttons('double')
            right = buttons_page.click_on_different_buttons("right")
            single = buttons_page.click_on_different_buttons("single")
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert single == "You have done a dynamic click", "The dynamic click button was not pressed"

    class TestLinkPage:
        def test_check_link(self, driver):
            links_page = LinkPage(driver, 'https://demoqa.com/links')
            links_page.open()
            link_href, current_url = links_page.check_new_tab_single_link()
            assert link_href == current_url, "the link is broken or url is incorrect"
        def test_broken_link(self, driver):
            links_page = LinkPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response == 400, "the link works or the status code in son 400"

    class TestUploadAndDownload:
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result_text = upload_download_page.upload_file()
            assert file_name == result_text, "the file has not been uploaded"
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "the file has not been downloaded"

    class TestDynamicPropertiesPage:
        def test_five_seconds_buttons(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_color_change()
            assert color_after != color_before, 'colors have not been changed'

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, 'button did not appear after 5 second'

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'button did not enable after 5 second'
