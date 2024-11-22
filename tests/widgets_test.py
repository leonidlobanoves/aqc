import time

from generator.generator import generated_select_menu, generated_color
from pages.widgets_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


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

    class TestTabsPage:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_title, what_content_length = tabs_page.check_tabs('what')
            origin_title, origin_content_length = tabs_page.check_tabs('origin')
            use_title, use_content_length = tabs_page.check_tabs('use')
            more_title, more_content_length = tabs_page.check_tabs('more')
            assert what_title == 'What' and what_content_length > 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_title == 'Origin' and origin_content_length > 0, 'the tab "origin" was not pressed or the text is missing'
            assert use_title == 'Use' and use_content_length > 0, 'the tab "use" was not pressed or the text is missing'
            assert more_title == 'More' and more_content_length == 0, 'the tab "more" was clickable or the text is added'

    class TestToolTipsPage:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    class TestMenuPage:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], "menu items do not exist or have not been selected"

    class TestSelectMenuPage:
        def test_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select_menu_page.fill_selected_menu()
            time.sleep(1)
            option, title,  old, multi, standard = select_menu_page.get_text_from_menu()
            data = next(generated_select_menu())
            assert option in data.select_value, "The value has not been changed, or was not filled"
            assert title in data.select_title, "The title has not been changed, or was not filled"
            assert old != 'Red', "The field has not been changed"
            assert multi in data.multiselect_color, "The field has not been changed, or was not filled"
            assert standard in data.car_select, "The field has not been changed, or was not filled"

        def check_response_order(context, key, order):
            is_reversed = True if order = "DESC" else False

            response_body = json.loads(context.response.text)
            element_list = []

            for element in response_body['content']:
                if isinstance(element[key], str):
                    element_list.append(element[key].upper())
                else:
                    element_list.append(element[key])
            ordered_element_list = element_list.copy()
            ordered_element_list.sort(reverse=is_reversed)
            print(element_list)
            print(ordered_element_list)

            if element_list != ordered_element_list:
                raise AssertionErrorror

        def get_component_with_given_field(context, field, r_key, given_file, key):
            response = json.loads(context.response.text)
            list = response['content']
            for item in list:
                response_value = find_value_by_key_in_dictionary(item, r_key)
                if response_value is not None:
                    id = item[field]
                    break

            update_user_value(context, settings_type='profiles', value=str(id), filename=given_file, key=key)

        def find_value_by_key_in_dictionary(data, target):
            for key, value in data.items():
                if key == target:
                    return value
                elif isinstance(value, dict):
                    list_find = find_value_by_key_in_dictionary(value, target)
                    if list_find is not None:
                        return list_find
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            list_find = find_value_by_key_in_dictionary(item, target)
                            if list_find is not None:
                                return list_find
            return None


def get_component_with_given_field(context, key_path, given_file, key):
    response = json.loads(context.response.text)
    items_list = response['content']

    for item in items_list:
        response_value = find_value_by_key_in_dictionary(item, key_path)
        if response_value is not None:
            # Получаем значение по пути к ключу key_path
            value = response_value
            break

    update_user_value(context, settings_type='profiles', value=str(value), filename=given_file, key=key)