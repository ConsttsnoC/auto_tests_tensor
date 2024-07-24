from tests.pages.sbis_site import SbisSite

class TestSbisSite:

    def test_navigate_and_validate_sbis_site(self, driver):
        page = SbisSite(driver)
        page.test_first_scenario()



