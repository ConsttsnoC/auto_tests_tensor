import time

from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех страниц.

    Этот класс предоставляет общие методы для взаимодействия с веб-элементами.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует объект BasePage с драйвером.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def find_element(self, locator: tuple, timeout=10):
        """
        Находит один элемент на странице по указанным параметрам.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Найденный веб-элемент.
        """
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by: By, value: str, timeout=10):
        """
        Находит несколько элементов на странице по указанным параметрам.

        :param by: Способ поиска элемента (например, By.ID, By.XPATH).
        :param value: Значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Список найденных веб-элементов.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(by, value))

    def wait_for_body_to_load(self, timeout=10):
        """
        Ожидает, пока элемент <body> не станет полностью загруженным.

        :param timeout: Максимальное время ожидания в секундах.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def find_and_click_element(self, locator: tuple, timeout=10):
        """
        Находит элемент по локатору, ждет его доступности и кликает по нему.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        """
        self.wait_for_body_to_load(timeout)
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def scroll_to_element(self, locator: tuple, timeout=10):
        """
        Прокручивает страницу до элемента, чтобы он оказался в видимой области.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        """
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located((by, value)))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element,
        )
        time.sleep(0.5)

    def get_current_url(self):
        """
        Возвращает текущий URL страницы.

        :return: Текущий URL.
        """
        return self.driver.current_url

    def get(self, url: str):
        """
        Открывает указанный URL.

        :param url: URL для открытия.
        """
        self.driver.get(url)

    def switch_to_last_tab(self):
        """
        Переключение на последнюю открытую вкладку браузера.
        """
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def wait_for_text_in_element(self, locator: tuple, text: str, timeout=10):
        """
        Ожидает появления текста в указанном элементе.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param text: Текст, который должен появиться в элементе.
        :param timeout: Максимальное время ожидания в секундах.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(locator, text))

    def assert_url_is_equal(self, expected_url: str):
        """
        Проверяет, что текущий URL соответствует ожидаемому.

        :param expected_url: Ожидаемый URL.
        :raises AssertionError: Если текущий URL не соответствует ожидаемому.
        """
        current_url = self.get_current_url()
        assert (
            expected_url == current_url
        ), f"Ожидали url {expected_url}, получили {current_url}"

    def find_and_send(self, locator: tuple, key: str, timeout=10):
        """
        Находит элемент по локатору и отправляет в него текст.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param key: Текст для отправки в элемент.
        :param timeout: Максимальное время ожидания в секундах.
        """
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located((by, value)))
        element.send_keys(key)

    def check_partners_list(self, list_locator: tuple, item_selector: str, timeout=10):
        """
        Проверяет отображение списка партнёров и наличие элементов.

        :param list_locator: Кортеж, содержащий способ поиска элемента списка и значение для поиска.
        :param item_selector: Селектор для поиска элементов внутри списка.
        :param timeout: Максимальное время ожидания в секундах.
        :raises AssertionError: Если элемент списка не отображается или в списке нет элементов.
        """
        by, value = list_locator
        wait = WebDriverWait(self.driver, timeout)
        partners_list = wait.until(EC.presence_of_element_located((by, value)))
        assert (
            partners_list.is_displayed()
        ), "LIST_OF_PARTNERS элемент не отображается на странице"
        elements = partners_list.find_elements(By.CSS_SELECTOR, item_selector)
        count = len(elements)
        assert count > 0, "Нет элементов с классом 'sbisru-Contacts-List__name'"
        print(f"Количество элементов с классом '{item_selector}': {count}")

    def wait_for_element(self, locator, timeout=10):
        """
        Ожидание загрузки элемента на странице.

        :param driver: Экземпляр WebDriver.
        :param locator: Кортеж, содержащий стратегию поиска (например, By.ID) и значение поиска (например, 'element_id').
        :param timeout: Максимальное время ожидания в секундах. По умолчанию 10 секунд.
        :return: Найденный элемент.
        :raises TimeoutException: Если элемент не найден в течение времени ожидания.
        """
        time.sleep(1)
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

