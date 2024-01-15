import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date, generated_select_menu
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, len(section_content)


class AutocompletePage(BasePage):
    locators = AutocompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_input_value_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_visible(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_from_the_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.select_date_from_the_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.select_date_from_the_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2021')
        self.select_date_from_the_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.select_date_from_the_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_from_the_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def check_slider(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def check_progress_bar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        slider_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        slider_button.click()
        time.sleep(random.randint(2, 5))
        slider_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tabs_num):
        tabs = {'what':
                     {'title': self.locators.TABS_WHAT,
                      'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT},
                     }

        tabs_title = self.element_is_clickable(tabs[tabs_num]['title'])
        try:
            tabs_title.click()
            tabs_content = self.element_is_present(tabs[tabs_num]['content']).text
        except ElementClickInterceptedException:
            tabs_content = ''

        return tabs_title.text, len(tabs_content)

class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS).text
        return tool_tip_text


    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section

class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_check_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_check_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data

class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def fill_selected_menu(self):
        value = random.choice(next(generated_select_menu()).select_value)
        title = random.choice(next(generated_select_menu()).select_title)
        self.element_is_visible(self.locators.SELECT_OPTION).send_keys(value, Keys.ENTER)
        self.element_is_visible(self.locators.SELECT_TITLE).send_keys(title, Keys.ENTER)
        self.select_by_text(self.locators.SELECT_COLOR_OLD, random.choice(next(generated_color()).color_name))
        color_dropdown = random.choice(next(generated_select_menu()).multiselect_color)
        self.element_is_visible(self.locators.MULTISELECT_DROPDOWN).send_keys(color_dropdown, Keys.ENTER)
        self.select_by_text(self.locators.MULTISELECT_STANDARD, random.choice(next(generated_select_menu()).car_select))


    def get_text_from_menu(self):
        res_check_list = self.elements_are_visible(self.locators.RESULT_FIRST)
        data = []
        for item in res_check_list:
            data.append(item.text)
        old_style_new_color = Select(self.element_is_visible(self.locators.SELECT_COLOR_OLD)).first_selected_option.text
        multi_result = self.element_is_present(self.locators.MULTISELECT_RESULT).text
        standard = Select(self.element_is_visible(self.locators.MULTISELECT_STANDARD)).first_selected_option.text
        return *data, old_style_new_color, multi_result, standard



