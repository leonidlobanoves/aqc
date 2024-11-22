import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():

    # Указываем порт, на котором работает отладочный интерфейс Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:51819")  # Подставьте свой порт здесь

    # Получаем путь к ChromeDriver, скачанный webdriver_manager
    chrome_driver_path = ChromeDriverManager().install()

    # Проверяем, что это действительно исполняемый файл
    if not chrome_driver_path.endswith("/chromedriver"):
        chrome_driver_path = os.path.join(os.path.dirname(chrome_driver_path), "chromedriver")


    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=chrome_options)

    driver.maximize_window()

    yield driver

    driver.quit()



