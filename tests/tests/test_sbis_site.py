from tests.pages.sbis_site import SbisSite


class TestSbisSite:

    def test_navigate_and_validate_sbis_site_first_scenario(
        self, open_website_and_clear
    ):
        page = SbisSite(open_website_and_clear)
        page.test_first_scenario()

    def test_navigate_and_validate_sbis_site_second_scenario(
        self, open_website_and_clear
    ):
        page = SbisSite(open_website_and_clear)
        page.test_second_scenario()

    def test_file_search_and_download_sbis_site_third_scenario(
        self, open_website_and_clear
    ):
        page = SbisSite(open_website_and_clear)
        page.file_search_and_download_sbis_site_third_scenario()

