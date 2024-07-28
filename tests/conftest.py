import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL


def pytest_addoption(parser):
    """
    Эта функция используется для добавления опции `--headless` к командной строке pytest.
    Если эта опция указана, браузер будет запускаться в headless режиме, что позволяет
    запускать тесты без отображения пользовательского интерфейса браузера.
    """
    parser.addoption(
        "--headless", action="store_true", help="run browser in headless mode"
    )


@pytest.fixture
def driver(request):
    """
    Фикстура для инициализации веб-драйвера Chrome с переданными опциями.
    Запускает браузер в режиме инкогнито и разворачивает его на весь экран.
    """
    # Определяем путь к директории проекта
    project_dir = os.path.abspath(os.path.dirname(__file__))
    download_dir = os.path.join(project_dir, "downloads")  # Путь к папке для загрузок

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--incognito")
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def open_website_and_clear(driver):
    """
    Фикстура для открытия сайта, очистки localStorage, sessionStorage и cookies.
    """
    driver.get(BASE_URL)
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
    yield driver
