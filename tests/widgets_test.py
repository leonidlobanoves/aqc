import time

from pages.widgets_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage


class TestWidgets:
    class TestWidgetsPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'


    class TestAutocompletePage:
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'the added colors are missing in the input'


        def test_remove_value_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            count_value_before = autocomplete_page.fill_input_multi()
            count_value_after = autocomplete_page.remove_input_value_multi()
            assert count_value_before != count_value_after, "value was not deleted"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, 'the added colors are missing in the input'

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_page.open()
            date_before, date_after = date_page.select_date()
            assert date_before != date_after, 'the date has not been changed'

        def test_change_date_and_time(self, driver):
            date_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_page.open()
            date_before, date_after = date_page.select_date_and_time()
            assert date_before != date_after, 'the date and time has not been changed'

    class TestSliderPage:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.check_slider()
            assert before != after, 'the slider value has not been changed'

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.check_progress_bar()
            assert before != after, 'the progress bar value has not been changed'

