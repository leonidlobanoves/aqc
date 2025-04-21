import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_executable_driver_path(driver_path):
    base_dir = os.path.dirname(driver_path)
    for file in os.listdir(base_dir):
        # Ensure it's a file and not THIRD_PARTY_NOTICES
        full_path = os.path.join(base_dir, file)
        if os.path.isfile(full_path) and file != "THIRD_PARTY_NOTICES.chromedriver":
            return full_path
    raise FileNotFoundError("Не удалось найти исполняемый chromedriver")


@pytest.fixture(scope='function')
def driver():
    # Настройка ChromeOptions для подключения к порту отладки
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:51819")

    # Загрузка и проверка пути к драйверу
    chrome_driver_path = ChromeDriverManager().install()
    chrome_driver_path = get_executable_driver_path(chrome_driver_path)

    # Убедиться, что файл драйвера исполняемый
    if not os.access(chrome_driver_path, os.X_OK):
        os.chmod(chrome_driver_path, 0o755)

    # Инициализация ChromeDriver
    chrome_service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Развернуть окно браузера
    driver.maximize_window()

    yield driver

    # Закрыть драйвер
    driver.quit()

