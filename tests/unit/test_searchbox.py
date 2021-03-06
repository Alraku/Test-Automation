import pytest
import logging
import utils.globals as globals

from pages.home import PageHome
from pages.login import PageLogin
from data.test_data import testdata_searchbox, testdata_searchbox_filters
from pages.search_results import PageSearchResults

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class TestSearchbox():

    @pytest.fixture()
    def class_setup(self):
        self.page_home = PageHome(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_search_results = PageSearchResults(self.driver)
        self.driver.get(globals.BASE_URL)


    @pytest.mark.order(1)
    @pytest.mark.parametrize("data_search_term, data_location, data_result", testdata_searchbox)
    def test_searchbox_term_one(self, class_setup, data_search_term, data_location, data_result):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(search_term=data_search_term, location=data_location)
        assert data_result in self.driver.title, "Assertion Failed - Title does not match"


    @pytest.mark.order(2)
    @pytest.mark.parametrize("checkbox_name", testdata_searchbox_filters)
    def test_search_in_descriptions(self, class_setup, checkbox_name):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(search_term="Vintage", location="Toruń")
        self.page_search_results.click_checkbox(checkbox_name)

        element_updated = self.page_search_results.check_if_element_reloaded()
        assert element_updated != None, "None type of element, assertion failed."



    