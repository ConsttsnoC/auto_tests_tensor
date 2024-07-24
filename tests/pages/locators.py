from selenium.webdriver.common.by import By


class Locators:
    CONTACTS_BUTTON = (
    By.CSS_SELECTOR, 'li.sbisru-Header__menu-item.sbisru-Header__menu-item-1 a.sbisru-Header__menu-link')
    CLIENT_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    MAIN_CONTENT_BLOCK = (
    By.CSS_SELECTOR, '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg')
    DETAILS_BUTTON = (By.CSS_SELECTOR,
                    '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a')
    WORK_BLOCK = (By.CSS_SELECTOR,
                  '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    IMAGES_BLOCK = (By.CSS_SELECTOR,
                    '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container')

