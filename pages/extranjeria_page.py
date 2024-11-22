import pdb
import random
import time
import logging
import re

from selenium.webdriver.common.by import By

from locators.extranjeria_locators import ExtranjeriaPageLocators, ShadowDOMLocators
from pages.base_page import BasePage
from seleniumbase import BaseCase
from pages.base_page import ShadowDOMHelper

logging.basicConfig(
    level=logging.DEBUG,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[
        logging.FileHandler("scraper.log"),  # Запись логов в файл
        logging.StreamHandler()  # Вывод логов в консоль
    ]
)
class ExtranjeriaPage(BasePage):
    locators = ExtranjeriaPageLocators()

    def fill_extranjeria_fields(self, name, tel):
        self.select_by_text(self.locators.PROVINCIAS_DISPONIBLES, 'León')
        self.element_is_clickable(self.locators.COOKIES).click()
        self.element_is_clickable(self.locators.ACCEPTAR_BUTTON).click()
        time.sleep(3)
        self.select_by_text(self.locators.OFICINA, 'Extranjería Expedición LEÓN, C/ de la GUARDIA CIVIL, 6')
        time.sleep(3)
        self.select_by_text(self.locators.TRAMITE, 'POLICIA - COMUNICACIÓN DE CAMBIO DE DOMICILIO')
        time.sleep(1)
        self.element_is_clickable(self.locators.ACCEPTAR_BUTTON).click()
        time.sleep(3)
        self.element_is_clickable(self.locators.ENTRAR).click()
        time.sleep(3)
        data = {'Julia':
                    {'nie': self.element_is_visible(self.locators.NIE).send_keys('Z0226954H'),
                     'nombre_appedido': self.element_is_visible(self.locators.NOMBRE_Y_APEDIDOS).send_keys('IULIIA ROMANOVA'),
                     'pais': self.select_by_text(self.locators.PAIS, 'RUSIA')},
                'Leo':
                    {'nie': self.element_is_visible(self.locators.NIE).send_keys('Z0226866H'),
                     'nombre_appedido': self.element_is_visible(self.locators.NOMBRE_Y_APEDIDOS).send_keys('LEONID LOBANOV'),
                     'pais': self.select_by_text(self.locators.PAIS, 'RUSIA')},
                }
        self.element_is_clickable(data[name])
        self.element_is_clickable(self.locators.BTN_ACEPTAR).click()
        time.sleep(3)
        self.element_is_clickable(self.locators.SOLICITAR_CITA).click()
        time.sleep(3)
        teldata = {'Julia':
                    {'tel': self.element_is_visible(self.locators.TELEFONO).send_keys('623313597'),
                     'email1': self.element_is_visible(self.locators.EMAIL1).send_keys('romanovajulia272727@gmail.com'),
                     'email2': self.element_is_visible(self.locators.EMAIL2).send_keys('romanovajulia272727@gmail.com')},
                'Leo':
                    {'tel': self.element_is_visible(self.locators.TELEFONO).send_keys('675412956'),
                     'email1': self.element_is_visible(self.locators.EMAIL1).send_keys('leonidlobanov.es@gmail.com'),
                     'email2': self.element_is_visible(self.locators.EMAIL2).send_keys('leonidlobanov.es@gmail.com')},
                }
        self.element_is_clickable(teldata[tel])
        self.element_is_clickable(self.locators.SIGUIENTE).click()
        time.sleep(2)
        pdb.set_trace()

class Script(BasePage):
    locators = ExtranjeriaPageLocators()

    def unban(self):
        users_count = self.element_is_present(self.locators.count_text).text
        print(users_count)
        while not users_count == "Не переносить сюда (Заблокированные) (0)":
            intim_element = self.element_is_present(self.locators.intim_text)
            osk_element = self.element_is_present(self.locators.osk_text)
            if intim_element or osk_element:
                self.element_is_clickable(self.locators.moderation).click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                self.element_is_visible(self.locators.unbanned).click()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.select_by_text(self.locators.reason, 'Интим и\или оскорбления в сообщениях, комментариях к стримам и т.п. Предупреждение.')
                #time.sleep(1)
            else:
                self.element_is_clickable(self.locators.moderation).click()
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                self.element_is_visible(self.locators.unbanned).click()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                #time.sleep(2)
                self.select_by_text(self.locators.reason, 'Сбой')
                #time.sleep(1)
            self.element_is_clickable(self.locators.accept).click()
            #time.sleep(1)
            users_count = self.element_is_present(self.locators.count_text).text
            if users_count == "Не переносить сюда (Заблокированные) (0)":
                break
        print("the folder is empty")

    def unban_auto(self):
        fid_value = self.element_is_present(self.locators.fid_number).get_attribute("value")
        users_count_auto_loc = self.locators.count_text_auto.format(key=fid_value)
        users_count_auto = self.element_is_present((By.XPATH, users_count_auto_loc)).text
        print(users_count_auto)
        female_reasons = ['Однотипные норм сообщения. Разъяснение. (Не спам !)', 'Сбой', "Интим и\или оскорбления в сообщениях, комментариях к стримам и т.п. Предупреждение."]
        while users_count_auto not in ["Не переносить сюда (Заблокированные антиспамом) (0)","Не переносить сюда (Неплатёжные заблокированные антиспам) (0)", "Не переносить сюда (Заблокированные) (0)"]:
            element_unban = self.element_is_present(self.locators.fast_unban)
            if element_unban:
                element_unban.click()
            else:
                self.element_is_clickable(self.locators.moderation).click()
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.element_is_visible(self.locators.unbanned).click()
                self.element_is_visible(self.locators.unbanned).click()
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            main_reason = random.choice([True, False])
            if main_reason == True:
                field = self.element_is_visible(self.locators.text_field)
                field.send_keys('''В некоторых случаях отправка сообщений, содержащих: наименование социальных сетей, мессенджеров и т.п., а также любые контактные данные или просьбу их предоставить - может идентифицироваться как деловые или коммерческие предложения, что категорически запрещено в сервисе знакомств и ведёт к окончательной блокировке.
Попробуйте придерживаться более нейтральных тем при общении с новыми собеседниками. Анкета разблокирована.''')
            else:
                reason = random.choice(female_reasons)
                self.select_by_text(self.locators.reason, reason)
            time.sleep(1)
            self.element_is_clickable(self.locators.accept).click()
            time.sleep(1)
            users_count_auto = self.element_is_present((By.XPATH, users_count_auto_loc)).text
            if users_count_auto in ["Не переносить сюда (Заблокированные антиспамом) (0)","Не переносить сюда (Неплатёжные заблокированные антиспам) (0)", "Не переносить сюда (Заблокированные) (0)"]:
                break
        print("the folder is empty")



class Vichitka(BasePage):
    locators = ExtranjeriaPageLocators()

    def contains_keywords(self, text, keywords):
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in keywords)

    def vichitka_anket(self):
        frame = self.element_is_present(self.locators.frame_loc)
        self.driver.switch_to.frame(frame)
        messages = self.elements_are_present(self.locators.all_messages)
        pattern = re.compile(r'\((.*?)\)')
        keywords = ['тг', 'tg', '@', 'Whatsapp', 'вотсап','встреч']
        for index, message in enumerate(messages, start=1):
            matches = pattern.findall(message.text)
            xpath = f"(//select[@name='reason'])[{index}]"
            select_locator = (By.XPATH, xpath)
            if any(self.contains_keywords(match, keywords) for match in matches):
                print(f"Итерация {index}: найдено 'тг' или 'tg' в тексте - {message.text}")
                self.select_by_text(select_locator, "Спам")
                anketa_xpath = f"(//input[@value='забанить'])[{index}]/ancestor::td//a"
                anketa_locator = (By.XPATH, anketa_xpath)
                print(self.element_is_present(anketa_locator).text)
                ban_xpath = f"(//input[@value='забанить'])[{index}]"
                ban_locator = (By.XPATH, ban_xpath)
                #self.element_is_clickable(ban_locator).click()




class Chrometests(BasePage):
    def downloads(self):
        time.sleep(10)
        downloads_manager = self.element_is_present(By.CSS_SELECTOR, "body > downloads-manager")
        if downloads_manager is None:
            raise Exception("Element 'downloads-manager' not found.")

        # Доступ к shadow_root
        frb0 = downloads_manager.shadow_root.find_element(By.CSS_SELECTOR, "#frb0")
        if frb0 is None:
            raise Exception("Element '#frb0' not found in 'downloads-manager' shadow root.")

        # Доступ к следующему shadow_root
        quick_show_in_folder = frb0.shadow_root.find_element(By.CSS_SELECTOR, "#quick-show-in-folder")
        if quick_show_in_folder is None:
            raise Exception("Element '#quick-show-in-folder' not found in '#frb0' shadow root.")

        # Доступ к последнему элементу
        masked_image = quick_show_in_folder.shadow_root.find_element(By.CSS_SELECTOR, "#maskedImage")
        if masked_image is None:
            raise Exception("Element '#maskedImage' not found in '#quick-show-in-folder' shadow root.")

        # Получение атрибута 'src' и проверка его значения через assert
        src_value = masked_image.get_attribute("src")
        assert src_value == "expected_value", f"Expected 'src' to be 'expected_value', but got {src_value}"







def get_data(context, structure):
    value = context.config.userdata["profiles"]
    struct_split = structure.split(".")
    for n in range(len(struct_split)):
        try:
            value = value[struct_split[n]]
        except TypeError:
            value = value[0][struct_split[n]]

def get_r_data(context, data):
    data_split = data[1:len(data)].split(":")
    name_json = change_name(context, data_split[0])
    value = get_data(context, name_json + '.' + data.split[1])
    return value