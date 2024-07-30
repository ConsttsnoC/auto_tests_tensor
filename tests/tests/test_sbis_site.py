from tests.pages.sbis_site import SbisSite


class TestSbisSite:

    def test_navigate_and_validate_tensor_banner_and_size_images(self, open_website_and_clear):
        page = SbisSite(open_website_and_clear)
        page.test_first_scenario()

    def test_test_navigate_and_validate_region_and_partners(self, open_website_and_clear):
        page = SbisSite(open_website_and_clear)
        page.test_second_scenario()

    def test_download_and_verify_sbis_plugin(self, open_website_and_clear):
        page = SbisSite(open_website_and_clear)
        page.test_third_scenario()
