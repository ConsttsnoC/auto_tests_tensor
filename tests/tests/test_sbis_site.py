from tests.pages.sbis_site import SbisSite

class TestSbisSite:

    def test_navigate_and_validate_sbis_site_first_scenario(self, driver):
        page = SbisSite(driver)
        page.test_first_scenario()

    def test_navigate_and_validate_sbis_site_second_scenario(self, driver):
        page = SbisSite(driver)
        page.test_second_scenario()