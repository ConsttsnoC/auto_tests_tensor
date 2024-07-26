import allure
from loguru import logger
import pytest
from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from tests.pages.locators import Locators


class SbisSite(BasePage):
    """
    Класс для тестирования функциональности сайта СБИС.

    Этот класс содержит методы для взаимодействия с различными элементами на сайте СБИС,
    а также для выполнения проверок.
    """

    @allure.step("Запускаем первый сценарий")
    def test_first_scenario(self):
        """
        Первый сценарий тестирования.

        Этот тестовый сценарий включает следующие шаги:
        1. Нажатие на кнопку "Контакты".
        2. Нажатие на баннер клиента.
        3. Переключение на новую вкладку.
        4. Прокрутка к основному блоку контента.
        5. Ожидание появления текста "Сила в людях" в основном блоке контента.
        6. Нажатие на кнопку "Подробнее".
        7. Проверка, что текущий URL соответствует ожидаемому URL.
        8. Прокрутка к блоку "Работа".
        9. Проверка, что все изображения в блоке имеют одинаковую ширину и высоту.

        Если какой-либо из шагов завершится неудачно, тест зафиксирует ошибку.
        """
        try:
            logger.info("Нажимаем на кнопку 'Контакты'.")
            self.find_and_click_element(Locators.CONTACTS_BUTTON)
            logger.info("Нажимаем на баннер клиента.")
            self.wait_for_element(Locators.CLIENT_BANNER)
            self.find_and_click_element(Locators.CLIENT_BANNER)
            logger.info("Переключаемся на последнюю вкладку.")
            self.switch_to_last_tab()
            logger.info("Прокручиваем к основному блоку контента.")
            self.scroll_to_element(Locators.MAIN_CONTENT_BLOCK)
            self.wait_for_text_in_element(
                Locators.MAIN_CONTENT_BLOCK, "Сила в людях")
            logger.info("Нажимаем на кнопку 'Подробнее'.")
            self.find_and_click_element(Locators.DETAILS_BUTTON)
            self.assert_url_is_equal("https://tensor.ru/about")
            logger.info("Прокручиваем к блоку 'Работаем'.")
            self.scroll_to_element(Locators.WORK_BLOCK)
            self.assert_all_images_equal()
        except Exception as e:

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            pytest.fail(f"Ошибка теста сценария 1: {e}")

    def assert_all_images_equal(self):
        """
        Проверка, что все изображения в указанном блоке имеют одинаковую ширину и высоту.

        Эта функция находит все изображения в блоке, определенном локатором IMAGES_BLOCK,
        и проверяет, что их ширина и высота одинаковы. Если изображения не найдены,
        тест завершается с ошибкой. Если размеры изображений различаются, тест также
        завершается с ошибкой, выводя информацию о несоответствии.
        """
        try:
            block = self.find_element(Locators.IMAGES_BLOCK)
            images = block.find_elements(By.CSS_SELECTOR, "img")

            if not images:
                pytest.fail("Изображения не найдены")

            first_width = images[0].get_attribute("width")
            first_height = images[0].get_attribute("height")

            for img in images:
                width = img.get_attribute("width")
                height = img.get_attribute("height")
                print(f"Width: {width}, Height: {height}")
                assert (
                    width == first_width
                ), f"Несоответствие ширины: {width} != {first_width}"
                assert (
                    height == first_height
                ), f"Несоответствие высоты: {height} != {first_height}"
        except Exception as e:
            pytest.fail(f"Ошибка теста проверки изображения: {e}")

    @allure.step("Запускаем второй сценарий")
    def test_second_scenario(self):
        """
        Второй сценарий тестирования.

        Этот тестовый сценарий включает следующие шаги:
        1. Нажатие на кнопку "Контакты".
        2. Ожидание появления текста "Самарская обл." в элементе.
        3. Ожидание появления текста "Самара" в элементе.
        4. Проверка отображения и наличия элементов в списке партнёров.
        5. Выбор региона "Камчатский край".
        6. Ожидание появления текста "Камчатский край" в элементе.
        7. Ожидание появления текста "Петропавловск-Камчатский" в элементе.
        8. Проверка отображения и наличия элементов в списке партнёров.
        9. Проверка, что текущий URL содержит "kamchatskij-kraj".
        10. Проверка, что заголовок страницы содержит "Камчатский край".

        Если какой-либо из шагов завершится неудачно, тест зафиксирует ошибку.
        """
        try:
            self.find_and_click_element(Locators.CONTACTS_BUTTON)
            self.wait_for_text_in_element(
                Locators.LOCATION_DEFINE, "Самарская обл.")
            self.wait_for_text_in_element(Locators.CITY_LOCATION_DEFINE, "Самара")
            self.check_partners_list(
                Locators.LIST_OF_PARTNERS, "div.sbisru-Contacts-List__name"
            )
            self.find_and_click_element(Locators.SELECT_REGION)
            self.find_and_send(Locators.INPUT_NAME_REGION, "Камчатский край")
            self.wait_for_element(Locators.BUTTON_REGION_KAMCHATKA)
            self.find_and_click_element(Locators.BUTTON_REGION_KAMCHATKA)
            self.wait_for_text_in_element(
                Locators.LOCATION_DEFINE, "Камчатский край")
            self.wait_for_text_in_element(
                Locators.CITY_LOCATION_DEFINE, "Петропавловск-Камчатский")
            self.check_partners_list(
                Locators.LIST_OF_PARTNERS, "div.sbisru-Contacts-List__name"
            )
            current_url = self.get_current_url()
            print(current_url)
            assert (
                "kamchatskij-kraj" in current_url
            ), f"URL does not contain 'kamchatskij-kraj': {current_url}"
            title = self.driver.title
            print(title)
            assert (
                "Камчатский край" in title
            ), f"Title does not contain 'Камчатский край': {title}"
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            pytest.fail(f"Ошибка теста сценария 2: {e}")
