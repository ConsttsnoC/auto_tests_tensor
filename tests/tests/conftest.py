import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.config import BASE_URL


@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Проверка наличия параметра --headless в командной строке
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")  # Возможно потребуется для некоторых ОС
        chrome_options.add_argument("--window-size=1920,1080")  # Установить размер окна для headless режима
    else:
        chrome_options.add_argument("--start-maximized")

    # Инициализация драйвера с переданными опциями
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")





