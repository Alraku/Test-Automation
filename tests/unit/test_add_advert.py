import pytest
import logging
import utils.globals as globals

from pages.add_advert import PageAddAdvert
from utils.helpers import CookieOperations
from data.test_data import testdata_advert_form_fields


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class TestAddAdvert:

    @pytest.fixture()
    def class_setup(self):
        self.driver.get(globals.BASE_URL)
        CookieOperations.load_cookie(self.driver)
        self.page_add_advert = PageAddAdvert(self.driver)
        self.driver.get(globals.BASE_URL + '/nowe-ogloszenie')


    @pytest.mark.order(1)
    @pytest.mark.parametrize('advert', testdata_advert_form_fields)
    def test_add_advert_basic(self, class_setup, advert):
        self.page_add_advert.advert = advert
        self.page_add_advert.fill_in_fields()
        self.page_add_advert.submit_advert()
        self.driver.get(globals.BASE_URL + '/mojolx/waiting/')
        assert self.page_add_advert.verify_new_advert() == advert.get('title')