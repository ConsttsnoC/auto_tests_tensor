import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL


@pytest.fixture
def driver(request):
    """
        Фикстура для инициализации веб-драйвера Chrome с переданными опциями.
        Запускает браузер в режиме инкогнито и разворачивает его на весь экран.
        """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


