from selenium.webdriver.common.by import By


class Locators:
    CONTACTS_BUTTON = (
        By.CSS_SELECTOR,
        "li.sbisru-Header__menu-item.sbisru-Header__menu-item-1 a.sbisru-Header__menu-link",
    )
    CLIENT_BANNER = (
        By.XPATH,
        '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a',
    )
    MAIN_CONTENT_BLOCK = (
        By.CSS_SELECTOR,
        "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg",
    )
    DETAILS_BUTTON = (
        By.CSS_SELECTOR,
        "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a",
    )
    WORK_BLOCK = (
        By.CSS_SELECTOR,
        "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3",
    )
    IMAGES_BLOCK = (
        By.CSS_SELECTOR,
        "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container",
    )
    LOCATION_DEFINE = (
        By.CSS_SELECTOR,
        "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span",
    )
    CITY_LOCATION_DEFINE = (By.NAME, "itemsContainer")
    LIST_OF_PARTNERS = (By.ID, "contacts_list")
    SELECT_REGION = (
        By.CSS_SELECTOR,
        "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span",
    )
    INPUT_NAME_REGION = (
        By.CSS_SELECTOR,
        "#popup > div.controls-Popup.ws-float-area-show-complete.controls-Popup_shown.controls_themes__wrapper.controls-Scroll_webkitOverflowScrollingTouch.controls-Popup__lastItem > div > div.controls-Scroll-ContainerBase.controls_scroll_theme-sbisru.controls-Scroll__content.controls-Scroll__content_hideNativeScrollbar.controls-Scroll__content_hideNativeScrollbar_ff-ie-edge.controls-Scroll-ContainerBase__scroll_vertical.controls-Scroll-ContainerBase__scrollPosition-regular.controls-Scroll-Container__base.controls-BlockLayout__blockGroup.undefined > div > div > div.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l > div > div > div.ws-flexbox.ws-align-items-baseline > div.controls-Render.js-controls-Render.controls-Render_background-same.controls-Render_textAlign-left.controls-Render_search_borderRadius.controls-Render_state-search-valid.controls-fontsize-xl.controls-fontsize-xl.controls-fontweight-default.controls-Render-fontsize-xl.controls-text-default.controls-Render_state-search-valid_caretEmpty.controls-inlineheight-l.controls-Render-inlineheight-l.controls-search.controls_search_theme-sbisru.controls-notFocusOnEnter.sbis_ru-Region-Panel__search.ws-flex-grow-1.s-Grid--hide-sm > div > div.controls-InputBase__field.controls-Search__field_margin-null.controls-Search__field_theme_sbisru_margin-null.controls-Render__field.controls-Render__field_textAlign_left.ws-ellipsis.controls-Render__field_zIndex > input",
    )
    BUTTON_REGION_KAMCHATKA = (
        By.CSS_SELECTOR,
        "#popup > div.controls-Popup.ws-float-area-show-complete.controls-Popup_shown.controls_themes__wrapper.controls-Scroll_webkitOverflowScrollingTouch.controls-Popup__lastItem > div > div > div > div > div.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l > div > ul > li > span > span > span",
    )
