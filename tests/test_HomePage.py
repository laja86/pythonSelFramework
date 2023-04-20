import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+get_data["firstname"])
        homepage.getName().send_keys(get_data["firstname"])
        homepage.getEmail().send_keys(get_data["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), get_data["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        print (get_data["firstname"] + ": Gender: " + get_data["gender"] + ": " + alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def get_data(self, request):
        return request.param

