from seleniumbase import BaseCase

from pages.base_page import BasePage
from pages.extranjeria_page import ExtranjeriaPage, Script, Vichitka, Chrometests


class TestExtranjeria:
    class TestExtranjeriaFields:

        def test_extranjeria(self, driver):
            extranjeria_page = ExtranjeriaPage(driver, 'https://icp.administracionelectronica.gob.es/icpplus/index.html')
            extranjeria_page.open()
            extranjeria_page.fill_extranjeria_fields('Julia', 'Julia')
    #
        def test_script(self, driver):
            script_page = Script(driver, 'https://staff.mamba.ru/support/message/client.php?select_mode=7&fid=228&client_id=34644371')
            script_page.open()
            #script_page.unban_auto()
            script_page.ban_machine()


        # def test_vichitki(self, driver):
        #     vichitka_page = Vichitka(driver, 'https://staff.mamba.ru/proxy?file=%2Fmoderation%2Fnew_anketas.phtml')
        #     vichitka_page.open()
        #     vichitka_page.vichitka_anket()

    class TestChrometests:  # Убедитесь, что ваш тест наследует BaseCase
        def test_downloads(self, driver):
            # Создаем экземпляр класса ShadowDOM и передаем self.driver (экземпляр браузера)
             vichitka_page = Chrometests(driver, 'chrome://downloads/')
             vichitka_page.open()
             vichitka_page.downloads()
