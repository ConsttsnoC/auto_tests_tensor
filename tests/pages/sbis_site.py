import os
import time
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

    @allure.step("Проверка, что все изображения в указанном блоке имеют одинаковую ширину и высоту")
    def assert_all_images_equal(self):
        """
        Проверка, что все изображения в указанном блоке имеют одинаковую ширину и высоту.

        Эта функция находит все изображения в блоке, определенном локатором IMAGES_BLOCK,
        и проверяет, что их ширина и высота одинаковы. Если изображения не найдены,
        тест завершается с ошибкой. Если размеры изображений различаются, тест также
        завершается с ошибкой, выводя информацию о несоответствии.
        """
        try:
            logger.info("Находим блок с изображениями")
            block = self.find_element(Locators.IMAGES_BLOCK)
            images = block.find_elements(By.CSS_SELECTOR, "img")

            if not images:
                logger.error("Изображения не найдены")
                pytest.fail("Изображения не найдены")

            first_width = images[0].get_attribute("width")
            first_height = images[0].get_attribute("height")

            logger.info(f"Ожидаемая ширина: {first_width}, Ожидаемая высота: {first_height}")

            for img in images:
                width = img.get_attribute("width")
                height = img.get_attribute("height")
                print(f"Width: {width}, Height: {height}")
                logger.info(f"Текущее изображение - Ширина: {width}, Высота: {height}")
                assert (
                    width == first_width
                ), f"Несоответствие ширины: {width} != {first_width}"
                assert (
                    height == first_height
                ), f"Несоответствие высоты: {height} != {first_height}"
                logger.info("Все изображения имеют одинаковую ширину и высоту")
        except Exception as e:
            logger.error(f"Ошибка теста проверки изображения: {e}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            pytest.fail(f"Ошибка теста проверки изображения: {e}")

    @allure.step("Загрузка и проверка файла на соответствие его размеру, очищение директории")
    def download_and_verify_file_size_and_clear_directory(self):
        try:
            # Получение пути к директории проекта и определение пути к директории загрузок
            project_dir = os.path.abspath(os.path.dirname(__file__))
            download_dir = os.path.join(project_dir, "..\downloads")
            logger.info(f"Путь к директории загрузок: {download_dir}")
            # Проверка наличия директории загрузок
            if not os.path.exists(download_dir):
                logger.error(f"Не удалось найти директорию: {download_dir}")
                pytest.fail(f"Директория не найдена: {download_dir}")
            # Получение списка файлов в директории загрузок
            files = os.listdir(download_dir)
            if not files:
                logger.error("В директории нет файлов.")
                pytest.fail("В директории нет файлов.")
            # Нахождение последнего загруженного файла по времени модификации
            latest_file = max(
                files, key=lambda f: os.path.getmtime(os.path.join(download_dir, f))
            )
            latest_file_path = os.path.join(download_dir, latest_file)
            logger.info(f"Последний загруженный файл: {latest_file}")
            # Получение размера последнего загруженного файла в мегабайтах
            file_size = os.path.getsize(latest_file_path)
            file_size_mb = file_size / (1024 * 1024)
            logger.info(f"Размер последнего скачанного файла '{latest_file}': {file_size_mb:.2f} МБ")
            # Ожидаемый размер файла и допустимая погрешность
            expected_size_mb = 11.05
            tolerance_mb = 0.01  # Допустимая погрешность
            # Проверка соответствия размера файла ожидаемому значению
            assert abs(file_size_mb - expected_size_mb) <= tolerance_mb, (
                f"Размер файла ({file_size_mb:.2f} МБ) не соответствует ожидаемому значению "
                f"({expected_size_mb} МБ)."
            )
            logger.info("Размер файла соответствует ожидаемому значению")
            # Удаление всех файлов из директории загрузок
            for file_name in files:
                file_path = os.path.join(download_dir, file_name)
                try:
                    os.remove(file_path)
                    logger.info(f"Удалён файл: {file_path}")
                except Exception as e:
                    logger.error(f"Не удалось удалить файл {file_path}: {e}")
        except Exception as e:
            logger.error(f"Ошибка при загрузке и проверке файла: {e}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            pytest.fail(
                f"Загрузка и проверка файла на соответствие его размеру, очищение директории: {e}"
            )

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
            self.wait_for_text_in_element(Locators.MAIN_CONTENT_BLOCK, "Сила в людях")
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
            logger.info("Нажимаем на кнопку 'Контакты'")
            self.find_and_click_element(Locators.CONTACTS_BUTTON)
            logger.info("Проверяем, что местоположение определено как 'Самарская обл.'")
            self.wait_for_text_in_element(Locators.LOCATION_DEFINE, "Самарская обл.")
            logger.info("Проверяем, что город определен как 'Самара'")
            self.wait_for_text_in_element(Locators.CITY_LOCATION_DEFINE, "Самара")
            logger.info("Проверяем список партнеров для Самарской области")
            self.check_partners_list(
                Locators.LIST_OF_PARTNERS, "div.sbisru-Contacts-List__name"
            )
            logger.info("Открываем выбор региона")
            self.find_and_click_element(Locators.SELECT_REGION)
            logger.info("Вводим 'Камчатский край' в поле выбора региона")
            self.find_and_send(Locators.INPUT_NAME_REGION, "Камчатский край")
            logger.info("Ожидаем элемент кнопки выбора региона 'Камчатский край'")
            self.wait_for_element(Locators.BUTTON_REGION_KAMCHATKA)
            logger.info("Нажимаем кнопку выбора региона 'Камчатский край'")
            self.find_and_click_element(Locators.BUTTON_REGION_KAMCHATKA)
            logger.info("Проверяем, что местоположение изменено на 'Камчатский край'")
            self.wait_for_text_in_element(Locators.LOCATION_DEFINE, "Камчатский край")
            logger.info("Проверяем, что город изменен на 'Петропавловск-Камчатский'")
            self.wait_for_text_in_element(
                Locators.CITY_LOCATION_DEFINE, "Петропавловск-Камчатский"
            )
            logger.info("Проверяем список партнеров для Камчатского края")
            self.check_partners_list(
                Locators.LIST_OF_PARTNERS, "div.sbisru-Contacts-List__name"
            )
            current_url = self.get_current_url()
            logger.info(f"Текущий URL: {current_url}")
            assert (
                "kamchatskij-kraj" in current_url
            ), f"Текущий URL не совпадает с 'kamchatskij-kraj': {current_url}"
            title = self.driver.title
            logger.info(f"Текущий заголовок страницы: {title}")
            assert (
                "Камчатский край" in title
            ), f"Заголовок страницы не 'Камчатский край': {title}"
        except Exception as e:
            logger.error(f"Ошибка теста сценария 2: {e}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            pytest.fail(f"Ошибка теста сценария 2: {e}")

    @allure.step("Запускаем третий сценарий")
    def test_third_scenario(self):
        try:
            logger.info("Скроллим до кнопки 'Скачать локальные версии'")
            self.scroll_to_element(Locators.BUTTON_DOWNLOAD_LOCAL_VERSIONS)
            logger.info("Нажимаем кнопку 'Скачать локальные версии'")
            self.find_and_click_element(Locators.BUTTON_DOWNLOAD_LOCAL_VERSIONS)
            logger.info("Ожидаем загрузку страницы")
            self.driver.implicitly_wait(5)
            logger.info("Нажимаем на элемент для скачивания файла")
            self.find_and_click_element(Locators.DOWNLOAD_FILE)
            logger.info("Ожидаем завершение загрузки файла")
            time.sleep(3) #ожидание окончания загрузки файла
            logger.info("Проверяем размер загруженного файла и очищаем директорию")
            self.download_and_verify_file_size_and_clear_directory()

        except Exception as e:
            logger.error(f"Ошибка теста сценария 3: {e}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            pytest.fail(f"Ошибка теста сценария 3: {e}")
