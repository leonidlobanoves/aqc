from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from seleniumbase import BaseCase


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        #self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        #self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")


    def element_is_visible(self, locator, timeout=1):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=3):
        try:
            return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            return None
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def element_is_not_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until_not(EC.element_to_be_clickable(locator))
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def select_by_text(self, element, value):
        #self.go_to_element(self.element_is_present(element))
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, coords_x, coords_y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, coords_x, coords_y)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def find_element(self, locator):
        return self.driver.find_element


class ShadowDOMHelper:
    def __init__(self, base_case):
        self.base = base_case# Сохраняем переданный драйвер

    def wait_for_shadow_element(self, locator):
        # Ждем, пока элемент с Shadow DOM загрузится
        shadow_element = self.base.wait_for_element(self, locator) # Используем локатор
        return shadow_element

    def click_example_button(self, locator):
        example_button = self.base.wait_for_element(locator)  # Используем локатор
        self.base.click(example_button)  # Кликаем на кнопку