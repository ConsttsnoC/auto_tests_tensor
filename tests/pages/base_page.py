from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by: By, value: str):
        """Находит один элемент на странице по указанным параметрам."""
        return self.driver.find_element(by, value)

    def find_elements(self, by: By, value: str):
        """Находит несколько элементов на странице по указанным параметрам."""
        return self.driver.find_elements(by, value)

    def wait_for_body_to_load(self, timeout=10):
        """Ожидает, пока элемент <body> не станет полностью загруженным."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def find_and_click_element(self, locator, timeout=10):
        """Находит элемент по локатору, ждет его доступности и кликает по нему."""
        self.wait_for_body_to_load(timeout)
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        # Ожидание, пока элемент станет доступным
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def scroll_to_element(self, locator):
        """Прокручивает страницу до элемента, чтобы он оказался в видимой области."""
        by, value = locator
        wait = WebDriverWait(self.driver, 10)

        # Ожидание, пока элемент станет доступным
        element = wait.until(EC.presence_of_element_located((by, value)))

        # Прокрутка до элемента
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element
        )

    def get_current_url(self):
        return self.driver.current_url

    def get(self, url: str):
        """Открывает указанный URL."""
        self.driver.get(url)

    def switch_to_last_tab(self):
        """
        Переключение на последнюю открытую вкладку браузера.
        """
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def wait_for_text_in_element(self, locator, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(locator, text))

    def assert_url_is_equal(self, expected_url):
        current_url = self.get_current_url()
        assert expected_url == current_url, f"Ожидали url {expected_url}, получили {current_url}"