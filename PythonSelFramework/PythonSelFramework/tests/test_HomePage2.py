import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage2(BaseClass):

    def test_formSubmission_failed(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + HomePageData.test_HomePage_data["firstname"])
        homepage.getName().send_keys(HomePageData.test_HomePage_data["firstname"])
        homepage.getEmail().send_keys(HomePageData.test_HomePage_data["email"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), HomePageData.test_HomePage_data["gender"])

        homepage.submitForm().click()

        alertText = homepage.getFailerMessage().text

        assert ("Name should be at least 2 characters" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
